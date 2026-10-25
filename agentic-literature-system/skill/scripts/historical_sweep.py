#!/usr/bin/env python3
"""Resumable historical Agentic Graphics paper discovery.

This runner deliberately separates two recall mechanisms:

1. an arXiv category-by-date enumeration lane that does not depend on keywords;
2. a taxonomy-derived multi-index query lane for aliases and non-arXiv work.

It retains every fetched record before local filtering, records truncation and
failures, and never represents its output as a provably exhaustive paper set.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import xml.etree.ElementTree as ET
from collections import Counter
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Iterable
from zoneinfo import ZoneInfo


SCRIPT_DIR = Path(__file__).resolve().parent
DISCOVERY_SCRIPT = SCRIPT_DIR / "discover_papers.py"
SPEC = importlib.util.spec_from_file_location("agentic_graphics_discover", DISCOVERY_SCRIPT)
discovery = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(discovery)

DEFAULT_CATEGORIES = ["cs.GR", "cs.CV", "cs.AI", "cs.RO", "cs.HC", "cs.MM", "eess.IV"]
DEFAULT_QUERY_SOURCES = ["openalex", "crossref", "semantic_scholar", "dblp", "huggingface"]
STATE_SCHEMA_VERSION = 2
RUN_SCHEMA_VERSION = "2026-09-09.1"
ATOM_NS = {
    "atom": "http://www.w3.org/2005/Atom",
    "arxiv": "http://arxiv.org/schemas/atom",
    "opensearch": "http://a9.com/-/spec/opensearch/1.1/",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--taxonomy", type=Path, required=True)
    parser.add_argument("--paper-list", type=Path, required=True)
    parser.add_argument("--queries", type=Path, default=SCRIPT_DIR.parents[0] / "references" / "search-query-families.json")
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--from-date", default="1991-01-01")
    parser.add_argument("--until-date", help="Inclusive YYYY-MM-DD end date; defaults to today in --timezone")
    parser.add_argument("--timezone", default="America/Chicago")
    parser.add_argument("--categories", default=",".join(DEFAULT_CATEGORIES))
    parser.add_argument("--slice-days", type=int, default=92)
    parser.add_argument("--split-threshold", type=int, default=8000)
    parser.add_argument("--arxiv-per-page", type=int, default=200)
    parser.add_argument("--max-pages-per-slice", type=int, default=0, help="0 means no cap; any positive cap is reported as truncation")
    parser.add_argument("--arxiv-delay", type=float, default=3.1)
    parser.add_argument("--stability-days", type=int, default=14, help="Recheck totals and first-page identity for slices ending within this many days of --until-date")
    parser.add_argument("--query-sources", default=",".join(DEFAULT_QUERY_SOURCES))
    parser.add_argument("--query-variants", type=int, default=0, help="Queries per taxonomy family; 0 means all")
    parser.add_argument("--query-pages", type=int, default=3)
    parser.add_argument("--query-per-page", type=int, default=100)
    parser.add_argument("--query-delay", type=float, default=0.2)
    parser.add_argument("--timeout", type=int, default=10)
    parser.add_argument("--max-attempts", type=int, default=2, help="Total attempts for each network page")
    parser.add_argument("--retry-base-delay", type=float, default=1.0)
    parser.add_argument("--retry-max-delay", type=float, default=6.0)
    parser.add_argument("--stage-order", choices=["query_first", "enumeration_first"], default="query_first", help="Execution order only; does not change final scope")
    parser.add_argument("--slice-order", choices=["newest_first", "oldest_first"], default="newest_first", help="Enumeration order only; does not change final scope")
    parser.add_argument("--max-runtime-seconds", type=float, default=60.0, help="Foreground batch budget; 0 permits an unbounded run")
    parser.add_argument("--progress-every-pages", type=int, default=1, help="Emit progress during dense pages; 0 disables page-level updates")
    parser.add_argument("--expected-id", action="append", default=[], help="Non-injection recall check: do not fetch this ID directly")
    parser.add_argument("--skip-known-corpus-recall", action="store_true", help="Disable the default non-injection check for every arXiv ID in the bundled accepted corpus (tests only)")
    parser.add_argument("--enumeration-fixture", type=Path, help="Offline raw-record JSONL for the enumeration lane")
    parser.add_argument("--query-fixture", type=Path, help="Offline raw-record JSONL for the query lane")
    parser.add_argument("--skip-query-lane", action="store_true")
    return parser.parse_args()


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.is_file():
        return []
    with path.open(encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def atomic_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    os.replace(temporary, path)


def atomic_jsonl(path: Path, values: Iterable[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    discovery.write_jsonl(temporary, values)
    os.replace(temporary, path)


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def record_signature(records: list[dict[str, Any]]) -> tuple[str, ...]:
    values = []
    for item in records:
        arxiv_id = discovery.normalize_arxiv((item.get("identifiers") or {}).get("arxiv", ""))
        values.append(arxiv_id or discovery.normalize_title(item.get("title") or item.get("canonical_title", "")))
    return tuple(values)


class RetryExhausted(RuntimeError):
    def __init__(self, errors: list[str], last_error: Exception):
        super().__init__(errors[-1] if errors else str(last_error))
        self.errors = errors
        self.last_error = last_error


class RunBudgetExhausted(RuntimeError):
    """Signal a clean foreground checkpoint boundary, not a source failure."""


def run_deadline(args: argparse.Namespace) -> float | None:
    return getattr(args, "deadline_monotonic", None)


def remaining_runtime(args: argparse.Namespace) -> float | None:
    deadline = run_deadline(args)
    return None if deadline is None else deadline - time.monotonic()


def ensure_runtime_available(args: argparse.Namespace) -> None:
    remaining = remaining_runtime(args)
    if remaining is not None and remaining <= 0:
        raise RunBudgetExhausted("foreground runtime budget reached")


def bounded_sleep(args: argparse.Namespace, seconds: float) -> None:
    if seconds <= 0:
        return
    remaining = remaining_runtime(args)
    if remaining is not None and remaining <= seconds:
        if remaining > 0:
            time.sleep(remaining)
        raise RunBudgetExhausted("foreground runtime budget reached before the next request")
    time.sleep(seconds)


def effective_request_timeout(args: argparse.Namespace) -> int:
    """Cap one blocking request to the remaining foreground budget."""
    ensure_runtime_available(args)
    configured = max(1, int(args.timeout))
    remaining = remaining_runtime(args)
    if remaining is None:
        return configured
    return max(1, min(configured, int(max(1.0, remaining))))


def emit_progress(
    args: argparse.Namespace,
    state: dict[str, Any],
    phase: str,
    message: str,
    extra: dict[str, Any] | None = None,
) -> None:
    started = getattr(args, "batch_started_monotonic", time.monotonic())
    payload = {
        "mode": "historical",
        "in_progress": True,
        "phase": phase,
        "message": message,
        "elapsed_seconds": round(time.monotonic() - started, 3),
        "max_runtime_seconds": getattr(args, "max_runtime_seconds", 0),
        "remaining_runtime_seconds": None if remaining_runtime(args) is None else round(max(0.0, remaining_runtime(args) or 0.0), 3),
        "stage_order": getattr(args, "stage_order", "enumeration_first"),
        "slice_order": getattr(args, "slice_order", "oldest_first"),
        "completed_slices": len(state.get("completed_slices", {})),
        "failed_slices": len(state.get("failed_slices", {})),
        "completed_query_batches": len(state.get("completed_query_batches", {})),
        "failed_query_batches": len(state.get("failed_query_batches", {})),
    }
    if extra:
        payload.update(extra)
    atomic_json(args.output_dir / "progress.json", payload)
    print(f"[historical:{phase}] {message}", file=sys.stderr, flush=True)


def retryable_error(exc: Exception) -> bool:
    if isinstance(exc, urllib.error.HTTPError):
        return exc.code in {408, 425, 429, 500, 502, 503, 504}
    return isinstance(exc, (urllib.error.URLError, TimeoutError, ET.ParseError, json.JSONDecodeError))


def retry_after_seconds(exc: Exception) -> float:
    if isinstance(exc, urllib.error.HTTPError):
        try:
            return float(exc.headers.get("Retry-After", "0"))
        except (TypeError, ValueError):
            return 0.0
    return 0.0


def call_with_retry(
    operation,
    max_attempts: int,
    base_delay: float,
    max_delay: float,
    sleeper=time.sleep,
    deadline: float | None = None,
):
    errors: list[str] = []
    for attempt in range(1, max_attempts + 1):
        if deadline is not None and time.monotonic() >= deadline:
            raise RunBudgetExhausted("foreground runtime budget reached before retry attempt")
        try:
            return operation(), {"attempts": attempt, "retries": attempt - 1, "errors": errors}
        except RunBudgetExhausted:
            raise
        except Exception as exc:
            errors.append(f"attempt {attempt}: {type(exc).__name__}: {exc}")
            if attempt >= max_attempts or not retryable_error(exc):
                raise RetryExhausted(errors, exc) from exc
            delay = max(retry_after_seconds(exc), base_delay * (2 ** (attempt - 1)))
            delay = min(max_delay, delay)
            if deadline is not None and time.monotonic() + delay >= deadline:
                raise RunBudgetExhausted("foreground runtime budget reached during retry backoff")
            sleeper(delay)
    raise AssertionError("unreachable")


def parse_day(value: str) -> date:
    return date.fromisoformat(value)


def resolve_until_date(args: argparse.Namespace) -> tuple[str, str]:
    """Freeze an implicit end date to the first batch stored in an output dir."""
    if args.until_date:
        parse_day(args.until_date)
        return args.until_date, "explicit"
    manifest_path = args.output_dir / "run_manifest.json"
    if manifest_path.is_file():
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            saved = manifest.get("date_range", {}).get("until_inclusive")
            if not saved:
                raise ValueError("missing date_range.until_inclusive")
            parse_day(saved)
            return saved, "existing_checkpoint"
        except (OSError, json.JSONDecodeError, ValueError) as exc:
            raise ValueError(f"cannot recover the frozen end date from {manifest_path}: {exc}") from exc
    return datetime.now(ZoneInfo(args.timezone)).date().isoformat(), "current_day_at_first_batch"


def arxiv_id_intersects_range(arxiv_id: str, start: date, end_inclusive: date) -> bool:
    match = re.match(r"^(\d{2})(\d{2})\.", arxiv_id)
    if not match:
        return True
    year = 2000 + int(match.group(1))
    month = int(match.group(2))
    try:
        month_start = date(year, month, 1)
    except ValueError:
        return True
    next_month = date(year + (month == 12), 1 if month == 12 else month + 1, 1)
    month_end = next_month - timedelta(days=1)
    return month_start <= end_inclusive and month_end >= start


def slice_id(start: date, end_exclusive: date) -> str:
    return f"{start.isoformat()}__{(end_exclusive - timedelta(days=1)).isoformat()}"


def initial_slices(
    start: date,
    end_exclusive: date,
    days: int,
    order: str = "oldest_first",
) -> list[tuple[date, date]]:
    result = []
    cursor = start
    while cursor < end_exclusive:
        next_day = min(end_exclusive, cursor + timedelta(days=days))
        result.append((cursor, next_day))
        cursor = next_day
    return list(reversed(result)) if order == "newest_first" else result


def arxiv_query(categories: list[str], start: date, end_exclusive: date) -> str:
    category_part = " OR ".join(f"cat:{category}" for category in categories)
    final_day = end_exclusive - timedelta(days=1)
    return f"({category_part}) AND submittedDate:[{start:%Y%m%d}0000 TO {final_day:%Y%m%d}2359]"


def parse_arxiv_feed(xml: str, query: str, window_id: str) -> tuple[list[dict[str, Any]], int]:
    root = ET.fromstring(xml)
    total_text = root.findtext("opensearch:totalResults", default="0", namespaces=ATOM_NS)
    try:
        total = int(total_text)
    except ValueError:
        total = 0
    records = []
    record_files = []
    for entry in root.findall("atom:entry", ATOM_NS):
        rec = discovery.base_record("arxiv")
        rec["query_family"] = "category_date_enumeration"
        rec["query"] = query
        rec["enumeration_window"] = window_id
        rec["title"] = discovery.clean_text(entry.findtext("atom:title", default="", namespaces=ATOM_NS))
        rec["abstract"] = discovery.clean_text(entry.findtext("atom:summary", default="", namespaces=ATOM_NS))
        rec["authors"] = [discovery.clean_text(node.findtext("atom:name", default="", namespaces=ATOM_NS)) for node in entry.findall("atom:author", ATOM_NS)]
        entry_id = discovery.clean_text(entry.findtext("atom:id", default="", namespaces=ATOM_NS))
        arxiv_id = discovery.normalize_arxiv(entry_id)
        rec["identifiers"] = {"arxiv": arxiv_id} if arxiv_id else {}
        rec["urls"] = [entry_id] if entry_id else []
        rec["categories"] = sorted({node.attrib.get("term", "") for node in entry.findall("atom:category", ATOM_NS) if node.attrib.get("term")})
        rec["venue"] = "arXiv"
        for field in ("published", "updated"):
            value = discovery.clean_text(entry.findtext(f"atom:{field}", default="", namespaces=ATOM_NS))
            if value:
                rec["event_dates"].append(discovery.event(field, value, "arxiv"))
        records.append(rec)
    return records, total


def fetch_arxiv_page(query: str, window_id: str, start: int, per_page: int, timeout: int) -> tuple[list[dict[str, Any]], int]:
    params = {
        "search_query": query,
        "start": start,
        "max_results": per_page,
        "sortBy": "submittedDate",
        "sortOrder": "ascending",
    }
    suffix = "/api/query?" + urllib.parse.urlencode(params)
    last_error: Exception | None = None
    endpoints = ("https://export.arxiv.org", "https://arxiv.org")
    # Treat --timeout as the budget for the logical arXiv page, not for each
    # fallback endpoint. This prevents one page from silently consuming twice
    # the configured timeout before the outer bounded retry policy runs.
    endpoint_timeout = max(1, int(timeout) // len(endpoints))
    for base in endpoints:
        try:
            return parse_arxiv_feed(discovery.get_text(base + suffix, endpoint_timeout), query, window_id)
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError, ET.ParseError) as exc:
            last_error = exc
    assert last_error is not None
    raise last_error


def config_fingerprint(args: argparse.Namespace, categories: list[str], query_sources: list[str]) -> str:
    payload = {
        "run_schema_version": RUN_SCHEMA_VERSION,
        "from_date": args.from_date,
        "until_date": args.until_date,
        "timezone": args.timezone,
        "categories": categories,
        "slice_days": args.slice_days,
        "split_threshold": args.split_threshold,
        "arxiv_per_page": args.arxiv_per_page,
        "max_pages_per_slice": args.max_pages_per_slice,
        "stability_days": args.stability_days,
        "query_sources": query_sources,
        "query_variants": args.query_variants,
        "query_pages": args.query_pages,
        "query_per_page": args.query_per_page,
        "max_attempts": args.max_attempts,
        "retry_base_delay": args.retry_base_delay,
        "retry_max_delay": args.retry_max_delay,
        "taxonomy_sha256": file_sha256(args.taxonomy),
        "paper_list_sha256": file_sha256(args.paper_list),
        "queries_sha256": file_sha256(args.queries),
        "skip_query_lane": args.skip_query_lane,
        "skip_known_corpus_recall": args.skip_known_corpus_recall,
    }
    return hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest()


def load_or_create_state(path: Path, fingerprint: str) -> dict[str, Any]:
    if path.is_file():
        state = json.loads(path.read_text(encoding="utf-8"))
        if state.get("config_fingerprint") != fingerprint:
            raise ValueError("Output directory contains a checkpoint from a different configuration; use a new output directory")
        if state.get("schema_version") != STATE_SCHEMA_VERSION:
            raise ValueError("Output directory contains an older checkpoint schema; use a new output directory")
        return state
    return {
        "schema_version": STATE_SCHEMA_VERSION,
        "config_fingerprint": fingerprint,
        "completed_slices": {},
        "failed_slices": {},
        "completed_query_batches": {},
        "failed_query_batches": {},
    }


def completed_file_is_valid(path: Path, metadata: dict[str, Any]) -> bool:
    if not path.is_file():
        return False
    if metadata.get("sha256") and file_sha256(path) != metadata["sha256"]:
        return False
    try:
        return len(load_jsonl(path)) == metadata.get("records")
    except (OSError, json.JSONDecodeError):
        return False


def assess_date_coverage(manifest: list[dict[str, Any]], start: date, end_inclusive: date) -> dict[str, Any]:
    cursor = start
    gaps = []
    overlap_days = 0
    covered_days = 0
    for item in sorted(manifest, key=lambda value: value["start"]):
        item_start = parse_day(item["start"])
        item_end = parse_day(item["end_inclusive"])
        if item_end < start or item_start > end_inclusive:
            continue
        item_start = max(item_start, start)
        item_end = min(item_end, end_inclusive)
        if item_start > cursor:
            gaps.append({"from": cursor.isoformat(), "until_inclusive": (item_start - timedelta(days=1)).isoformat()})
        elif item_start < cursor:
            overlap_days += max(0, (min(item_end, cursor - timedelta(days=1)) - item_start).days + 1)
        effective_start = max(cursor, item_start)
        if item_end >= effective_start:
            covered_days += (item_end - effective_start).days + 1
        cursor = max(cursor, item_end + timedelta(days=1))
    if cursor <= end_inclusive:
        gaps.append({"from": cursor.isoformat(), "until_inclusive": end_inclusive.isoformat()})
    requested_days = (end_inclusive - start).days + 1
    return {
        "requested_days": requested_days,
        "covered_days": covered_days,
        "gap_ranges": gaps,
        "overlap_days": overlap_days,
        "exact": not gaps and overlap_days == 0 and covered_days == requested_days,
    }


def archive_stale(path: Path, output_dir: Path, label: str) -> None:
    if not path.exists():
        return
    diagnostics = output_dir / "diagnostics"
    diagnostics.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    os.replace(path, diagnostics / f"{label}.{stamp}.jsonl")


def enumerate_arxiv(args: argparse.Namespace, categories: list[str], state: dict[str, Any], state_path: Path) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    slices_dir = args.output_dir / "enumeration_slices"
    slices_dir.mkdir(parents=True, exist_ok=True)
    start = parse_day(args.from_date)
    end_inclusive = parse_day(args.until_date)
    end_exclusive = end_inclusive + timedelta(days=1)
    queue = initial_slices(start, end_exclusive, args.slice_days, getattr(args, "slice_order", "oldest_first"))
    recovered_integrity_errors = []
    total_requests = 0
    total_retries = 0
    stopped_for_runtime_budget = False

    while queue:
        try:
            ensure_runtime_available(args)
        except RunBudgetExhausted:
            stopped_for_runtime_budget = True
            emit_progress(args, state, "enumeration", "foreground budget reached; materializing completed arXiv slices")
            break
        window_start, window_end = queue.pop(0)
        window_id = slice_id(window_start, window_end)
        final_path = slices_dir / f"{window_id}.jsonl"
        partial_path = slices_dir / f"{window_id}.partial.jsonl"
        completed = state["completed_slices"].get(window_id)
        if completed and completed_file_is_valid(final_path, completed):
            continue
        if completed:
            recovered_integrity_errors.append({"slice": window_id, "reason": "completed file missing, corrupt, or count/hash mismatch"})
            archive_stale(final_path, args.output_dir, f"corrupt-slice-{window_id}")
            state["completed_slices"].pop(window_id, None)

        query = arxiv_query(categories, window_start, window_end)
        try:
            (first, total), request_meta = call_with_retry(
                lambda: fetch_arxiv_page(query, window_id, 0, args.arxiv_per_page, effective_request_timeout(args)),
                args.max_attempts, args.retry_base_delay, args.retry_max_delay,
                deadline=run_deadline(args),
            )
            total_requests += request_meta["attempts"]
            total_retries += request_meta["retries"]
            state["failed_slices"].pop(window_id, None)
        except RunBudgetExhausted:
            stopped_for_runtime_budget = True
            emit_progress(args, state, "enumeration", f"paused before completing slice {window_id}")
            break
        except RetryExhausted as exc:
            total_requests += len(exc.errors)
            total_retries += max(0, len(exc.errors) - 1)
            state["failed_slices"][window_id] = {
                "error": str(exc), "attempt_log": exc.errors,
                "partial_records_preserved": len(load_jsonl(partial_path)) if partial_path.is_file() else 0,
            }
            atomic_json(state_path, state)
            continue

        span = (window_end - window_start).days
        if total > args.split_threshold and span > 1:
            archive_stale(partial_path, args.output_dir, f"superseded-parent-{window_id}")
            midpoint = window_start + timedelta(days=max(1, span // 2))
            children = [(window_start, midpoint), (midpoint, window_end)]
            if getattr(args, "slice_order", "oldest_first") == "newest_first":
                children.reverse()
            queue[0:0] = children
            atomic_json(state_path, state)
            if args.arxiv_delay:
                try:
                    bounded_sleep(args, args.arxiv_delay)
                except RunBudgetExhausted:
                    stopped_for_runtime_budget = True
                    emit_progress(args, state, "enumeration", f"paused after splitting dense slice {window_id}")
                    break
            continue

        existing = []
        if partial_path.is_file():
            try:
                existing = load_jsonl(partial_path)
            except (OSError, json.JSONDecodeError):
                archive_stale(partial_path, args.output_dir, f"corrupt-partial-{window_id}")
        if existing and record_signature(existing[:len(first)]) != record_signature(first):
            recovered_integrity_errors.append({"slice": window_id, "reason": "first page changed since partial checkpoint"})
            archive_stale(partial_path, args.output_dir, f"unstable-partial-{window_id}")
            existing = []
        if existing and len(existing) > total:
            recovered_integrity_errors.append({"slice": window_id, "reason": "reported total decreased below partial checkpoint size"})
            archive_stale(partial_path, args.output_dir, f"oversized-partial-{window_id}")
            existing = []
        records = existing or list(first)
        atomic_jsonl(partial_path, records)
        page_count = max(1, (len(records) + args.arxiv_per_page - 1) // args.arxiv_per_page)
        truncated = False
        failed = None
        paused_slice = False

        if len(records) < total and args.arxiv_delay:
            try:
                bounded_sleep(args, args.arxiv_delay)
            except RunBudgetExhausted:
                stopped_for_runtime_budget = True
                paused_slice = True
                emit_progress(
                    args, state, "enumeration",
                    f"paused slice {window_id} after preserving its first page",
                    {"active_slice": window_id, "active_slice_records": len(records), "active_slice_total": total},
                )

        while len(records) < total and not paused_slice:
            if args.max_pages_per_slice and page_count >= args.max_pages_per_slice:
                truncated = True
                break
            offset = len(records)
            try:
                (batch, _), request_meta = call_with_retry(
                    lambda offset=offset: fetch_arxiv_page(query, window_id, offset, args.arxiv_per_page, effective_request_timeout(args)),
                    args.max_attempts, args.retry_base_delay, args.retry_max_delay,
                    deadline=run_deadline(args),
                )
                total_requests += request_meta["attempts"]
                total_retries += request_meta["retries"]
            except RunBudgetExhausted:
                stopped_for_runtime_budget = True
                paused_slice = True
                atomic_jsonl(partial_path, records)
                emit_progress(
                    args, state, "enumeration",
                    f"paused slice {window_id} at {len(records)}/{total} records; checkpoint preserved",
                    {"active_slice": window_id, "active_slice_records": len(records), "active_slice_total": total},
                )
                break
            except RetryExhausted as exc:
                total_requests += len(exc.errors)
                total_retries += max(0, len(exc.errors) - 1)
                failed = {
                    "error": f"offset {offset}: {exc}", "attempt_log": exc.errors,
                    "partial_records_preserved": len(records),
                }
                break
            if not batch:
                failed = {"error": f"empty page before totalResults was reached ({len(records)}/{total})", "partial_records_preserved": len(records)}
                break
            if record_signature(batch) == record_signature(records[-len(batch):]):
                failed = {"error": f"repeated page detected at offset {offset}", "partial_records_preserved": len(records)}
                break
            records.extend(batch)
            page_count += 1
            atomic_jsonl(partial_path, records)
            progress_every_pages = getattr(args, "progress_every_pages", 5)
            if progress_every_pages and page_count % progress_every_pages == 0:
                emit_progress(
                    args, state, "enumeration",
                    f"slice {window_id}: {len(records)}/{total} records across {page_count} pages",
                    {"active_slice": window_id, "active_slice_records": len(records), "active_slice_total": total, "active_slice_pages": page_count},
                )
            if args.arxiv_delay and len(records) < total:
                try:
                    bounded_sleep(args, args.arxiv_delay)
                except RunBudgetExhausted:
                    stopped_for_runtime_budget = True
                    paused_slice = True
                    emit_progress(
                        args, state, "enumeration",
                        f"paused after page {page_count} of slice {window_id}; checkpoint preserved",
                        {"active_slice": window_id, "active_slice_records": len(records), "active_slice_total": total},
                    )
                    break

        if paused_slice:
            atomic_json(state_path, state)
            break

        if failed:
            state["failed_slices"][window_id] = failed
            atomic_json(state_path, state)
            continue

        stability_verified = False
        window_end_inclusive = window_end - timedelta(days=1)
        if args.stability_days and window_end_inclusive >= end_inclusive - timedelta(days=args.stability_days - 1):
            try:
                if args.arxiv_delay:
                    bounded_sleep(args, args.arxiv_delay)
                (verify_first, verify_total), request_meta = call_with_retry(
                    lambda: fetch_arxiv_page(query, window_id, 0, args.arxiv_per_page, effective_request_timeout(args)),
                    args.max_attempts, args.retry_base_delay, args.retry_max_delay,
                    deadline=run_deadline(args),
                )
                total_requests += request_meta["attempts"]
                total_retries += request_meta["retries"]
            except RunBudgetExhausted:
                stopped_for_runtime_budget = True
                paused_slice = True
                emit_progress(args, state, "enumeration", f"paused before stability verification of slice {window_id}")
            except RetryExhausted as exc:
                total_requests += len(exc.errors)
                total_retries += max(0, len(exc.errors) - 1)
                state["failed_slices"][window_id] = {
                    "error": f"stability verification: {exc}", "attempt_log": exc.errors,
                    "partial_records_preserved": len(records),
                }
                atomic_json(state_path, state)
                continue
            if paused_slice:
                atomic_json(state_path, state)
                break
            if verify_total != total or record_signature(verify_first) != record_signature(first):
                state["failed_slices"][window_id] = {
                    "error": f"slice changed during pagination (total {total} -> {verify_total})",
                    "partial_records_preserved": len(records), "stability_check_failed": True,
                }
                atomic_json(state_path, state)
                continue
            stability_verified = True

        os.replace(partial_path, final_path)
        state["completed_slices"][window_id] = {
            "start": window_start.isoformat(),
            "end_inclusive": (window_end - timedelta(days=1)).isoformat(),
            "reported_total": total,
            "records": len(records),
            "pages": page_count,
            "truncated": truncated,
            "stability_verified": stability_verified,
            "sha256": file_sha256(final_path),
        }
        state["failed_slices"].pop(window_id, None)
        atomic_json(state_path, state)
        emit_progress(
            args, state, "enumeration",
            f"completed slice {window_id}: {len(records)} records across {page_count} pages",
            {"last_completed_slice": window_id, "last_completed_slice_records": len(records)},
        )
        if args.arxiv_delay and queue:
            try:
                bounded_sleep(args, args.arxiv_delay)
            except RunBudgetExhausted:
                stopped_for_runtime_budget = True
                emit_progress(args, state, "enumeration", "foreground budget reached after a completed slice; materializing checkpoint")
                break

    records = []
    record_files = []
    manifest = []
    integrity_errors = []
    for window_id, metadata in sorted(state["completed_slices"].items(), key=lambda pair: pair[1]["start"]):
        path = slices_dir / f"{window_id}.jsonl"
        if completed_file_is_valid(path, metadata):
            record_files.append(str(path))
            if getattr(args, "stream_results", True):
                records.extend(load_jsonl(path))
            manifest.append(metadata)
        else:
            integrity_errors.append({"slice": window_id, "reason": "final integrity validation failed"})
    date_coverage = assess_date_coverage(manifest, start, end_inclusive)
    truncated_slices = [item for item in manifest if item["truncated"]]
    complete = not state["failed_slices"] and not truncated_slices and not integrity_errors and date_coverage["exact"]
    summary = {
        "status": "complete" if complete else "partial",
        "categories": categories,
        "from_date": args.from_date,
        "until_date": args.until_date,
        "completed_slices": len(manifest),
        "failed_slices": dict(state["failed_slices"]),
        "truncated_slices": truncated_slices,
        "date_coverage": date_coverage,
        "integrity_errors": integrity_errors,
        "recovered_integrity_errors": recovered_integrity_errors,
        "records": sum(item["records"] for item in manifest),
        "record_files": record_files,
        "pages": sum(item["pages"] for item in manifest),
        "stability_verified_slices": sum(1 for item in manifest if item.get("stability_verified")),
        "network_attempts": total_requests,
        "network_retries": total_retries,
        "partial_checkpoint_files": len(list(slices_dir.glob("*.partial.jsonl"))),
        "stopped_for_runtime_budget": stopped_for_runtime_budget,
        "slice_order": getattr(args, "slice_order", "oldest_first"),
        "method": "arXiv category-by-submission-date enumeration",
    }
    return records, summary


def query_batch_id(source: str, family: str, query: str) -> str:
    digest = hashlib.sha1(query.encode()).hexdigest()[:12]
    return f"{source}__{family}__{digest}"


def collect_query_lane(args: argparse.Namespace, query_sources: list[str], state: dict[str, Any], state_path: Path) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    batch_dir = args.output_dir / "query_batches"
    page_dir = args.output_dir / "query_pages"
    batch_dir.mkdir(parents=True, exist_ok=True)
    page_dir.mkdir(parents=True, exist_ok=True)
    families = discovery.read_query_families(args.queries, None, args.query_variants, set())
    if getattr(args, "stage_order", "enumeration_first") == "query_first":
        work_items = [
            (source, family, query)
            for family in families
            for query in family.get("queries", [])
            for source in query_sources
        ]
    else:
        work_items = [
            (source, family, query)
            for source in query_sources
            for family in families
            for query in family.get("queries", [])
        ]
    requested = len(work_items)
    total_requests = 0
    total_retries = 0
    recovered_integrity_errors = []
    stopped_for_runtime_budget = False
    emit_progress(args, state, "query_augmentation", f"starting or resuming {requested} taxonomy/source query batches")

    for source, family, query in work_items:
        try:
            ensure_runtime_available(args)
        except RunBudgetExhausted:
            stopped_for_runtime_budget = True
            emit_progress(args, state, "query_augmentation", "foreground budget reached; materializing completed query batches")
            break

        batch_id = query_batch_id(source, family["id"], query)
        batch_path = batch_dir / f"{batch_id}.jsonl"
        partial_path = batch_dir / f"{batch_id}.partial.jsonl"
        completed = state["completed_query_batches"].get(batch_id)
        if completed and completed_file_is_valid(batch_path, completed):
            continue
        if completed:
            recovered_integrity_errors.append({"batch": batch_id, "reason": "completed file missing, corrupt, or count/hash mismatch"})
            archive_stale(batch_path, args.output_dir, f"corrupt-query-batch-{batch_id}")
            state["completed_query_batches"].pop(batch_id, None)

        batch_records = []
        error = None
        page = 0
        pages_collected = 0
        exhausted = False
        truncated = False
        paused_batch = False
        previous_signature: tuple[str, ...] | None = None

        while True:
            if source == "huggingface" and page >= 1:
                truncated = bool(batch_records and len(batch_records) >= args.query_per_page)
                break
            if source != "huggingface" and args.query_pages and page >= args.query_pages:
                truncated = bool(batch_records and len(batch_records[-args.query_per_page:]) >= args.query_per_page)
                break
            page_path = page_dir / f"{batch_id}__p{page:05d}.jsonl"
            current = []
            try:
                if page_path.is_file():
                    current = load_jsonl(page_path)
                else:
                    ensure_runtime_available(args)
                    def fetch_page():
                        request_timeout = effective_request_timeout(args)
                        if source == "huggingface":
                            return discovery.fetch_huggingface_search(query, family["id"], args.query_per_page, request_timeout)
                        if source in discovery.FETCHERS and source != "arxiv":
                            return discovery.FETCHERS[source](query, family["id"], page, args.query_per_page, request_timeout)
                        raise ValueError(f"unsupported historical query source: {source}")
                    current, request_meta = call_with_retry(
                        fetch_page,
                        args.max_attempts,
                        args.retry_base_delay,
                        args.retry_max_delay,
                        deadline=run_deadline(args),
                    )
                    total_requests += request_meta["attempts"]
                    total_retries += request_meta["retries"]
                    atomic_jsonl(page_path, current)
            except RunBudgetExhausted:
                stopped_for_runtime_budget = True
                paused_batch = True
                if batch_records:
                    atomic_jsonl(partial_path, batch_records)
                emit_progress(
                    args, state, "query_augmentation",
                    f"paused batch {batch_id} before page {page + 1}; checkpoint preserved",
                    {"active_query_batch": batch_id, "active_query_records": len(batch_records)},
                )
                break
            except (OSError, json.JSONDecodeError) as exc:
                archive_stale(page_path, args.output_dir, f"corrupt-query-page-{batch_id}-p{page}")
                error = {"error": f"page {page + 1}: corrupt checkpoint: {exc}", "next_page": page, "partial_records_preserved": len(batch_records)}
                break
            except RetryExhausted as exc:
                total_requests += len(exc.errors)
                total_retries += max(0, len(exc.errors) - 1)
                error = {"error": f"page {page + 1}: {exc}", "attempt_log": exc.errors, "next_page": page, "partial_records_preserved": len(batch_records)}
                break

            signature = record_signature(current)
            if current and previous_signature == signature:
                archive_stale(page_path, args.output_dir, f"repeated-query-page-{batch_id}-p{page}")
                error = {"error": f"repeated result page detected at page {page + 1}", "next_page": page, "partial_records_preserved": len(batch_records)}
                break
            batch_records.extend(current)
            atomic_jsonl(partial_path, batch_records)
            previous_signature = signature
            pages_collected += 1
            if len(current) < args.query_per_page:
                exhausted = True
                break
            next_page = page + 1
            another_page_allowed = (
                source != "huggingface"
                and (not args.query_pages or next_page < args.query_pages)
            )
            if args.query_delay and another_page_allowed:
                try:
                    bounded_sleep(args, args.query_delay)
                except RunBudgetExhausted:
                    stopped_for_runtime_budget = True
                    paused_batch = True
                    emit_progress(
                        args, state, "query_augmentation",
                        f"paused batch {batch_id} after page {page + 1}; checkpoint preserved",
                        {"active_query_batch": batch_id, "active_query_records": len(batch_records)},
                    )
                    break
            page = next_page

        if paused_batch:
            atomic_json(state_path, state)
            break
        if error:
            state["failed_query_batches"][batch_id] = {
                "source": source, "family": family["id"], "query": query,
                **error,
            }
        else:
            atomic_jsonl(batch_path, batch_records)
            if partial_path.is_file():
                partial_path.unlink()
            state["completed_query_batches"][batch_id] = {
                "source": source, "family": family["id"], "query": query,
                "records": len(batch_records), "pages": pages_collected,
                "exhausted": exhausted, "truncated": truncated,
                "sha256": file_sha256(batch_path),
            }
            state["failed_query_batches"].pop(batch_id, None)
        atomic_json(state_path, state)
        completed_count = len(state["completed_query_batches"])
        progress_every = max(1, getattr(args, "progress_every_pages", 5))
        if completed_count % progress_every == 0 or error:
            emit_progress(
                args, state, "query_augmentation",
                f"query batches: {completed_count}/{requested} complete; latest {source}/{family['id']}",
                {"requested_query_batches": requested, "last_query_source": source, "last_query_family": family["id"]},
            )

    completed = list(state["completed_query_batches"].values())
    failures = list(state["failed_query_batches"].values())
    records = []
    final_integrity_errors = []
    for batch_id, metadata in sorted(state["completed_query_batches"].items()):
        path = batch_dir / f"{batch_id}.jsonl"
        if completed_file_is_valid(path, metadata):
            records.extend(load_jsonl(path))
        else:
            final_integrity_errors.append({"batch": batch_id, "reason": "final integrity validation failed"})
    truncated_batches = [item for item in completed if item.get("truncated")]
    by_source = {}
    for source in query_sources:
        source_completed = [x for x in completed if x["source"] == source]
        source_failed = [x for x in failures if x["source"] == source]
        source_truncated = [x for x in source_completed if x.get("truncated")]
        by_source[source] = {
            "status": "complete" if source_completed and not source_failed and not source_truncated else ("failed" if source_failed and not source_completed else "partial"),
            "completed_batches": len(source_completed),
            "failed_batches": len(source_failed),
            "truncated_batches": len(source_truncated),
            "records": sum(x["records"] for x in source_completed),
            "pages": sum(x.get("pages", 0) for x in source_completed),
        }
    matrix = []
    for source in query_sources:
        for family in families:
            family_completed = [x for x in completed if x["source"] == source and x["family"] == family["id"]]
            family_failed = [x for x in failures if x["source"] == source and x["family"] == family["id"]]
            matrix.append({
                "source": source, "query_family": family["id"],
                "requested_queries": len(family.get("queries", [])),
                "completed_queries": len(family_completed),
                "failed_queries": len(family_failed),
                "truncated_queries": sum(1 for item in family_completed if item.get("truncated")),
                "records": sum(item["records"] for item in family_completed),
            })
    complete = len(completed) == requested and not failures and not truncated_batches and not final_integrity_errors
    summary = {
        "status": "complete" if complete else "partial",
        "requested_batches": requested,
        "completed_batches": len(completed),
        "failed_batches": len(failures),
        "truncated_batches": len(truncated_batches),
        "records": len(records),
        "sources": by_source,
        "family_source_matrix": matrix,
        "network_attempts": total_requests,
        "network_retries": total_retries,
        "recovered_integrity_errors": recovered_integrity_errors,
        "integrity_errors": final_integrity_errors,
        "partial_checkpoint_files": len(list(batch_dir.glob("*.partial.jsonl"))),
        "stopped_for_runtime_budget": stopped_for_runtime_budget,
        "execution_order": "taxonomy_query_then_source" if getattr(args, "stage_order", "enumeration_first") == "query_first" else "source_then_taxonomy_query",
        "limits": {"query_variants": args.query_variants, "pages_per_query": args.query_pages, "per_page": args.query_per_page},
        "method": "taxonomy query augmentation; not enumeration",
    }
    return records, summary


def publication_year(item: dict[str, Any]) -> str:
    if item.get("published_date"):
        return str(item["published_date"])[:4]
    arxiv_id = discovery.normalize_arxiv((item.get("identifiers") or {}).get("arxiv", ""))
    match = re.match(r"^(\d{2})\d{2}\.", arxiv_id)
    return str(2000 + int(match.group(1))) if match else "unknown"


def iter_jsonl_files(paths: Iterable[Path]):
    for path in paths:
        with path.open(encoding="utf-8") as handle:
            for line in handle:
                if line.strip():
                    yield json.loads(line)


def annotate_prefilter(item: dict[str, Any], hints_by_family: dict[str, list[str]]) -> tuple[dict[str, Any], bool]:
    score, agents, graphics, hints, keep = discovery.local_score(item, hints_by_family)
    item["prefilter_score"] = score
    item["matched_agent_terms"] = agents
    item["matched_graphics_terms"] = graphics
    item["taxonomy_hints"] = hints
    return item, keep


def stream_prefilter_enumeration(records: Iterable[dict[str, Any]], low_path: Path, hints_by_family: dict[str, list[str]], paper_names: set[str], paper_ids: set[str], taxonomy_names: set[str], taxonomy_ids: set[str]) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    retained_raw = []
    all_ids: set[str] = set()
    year_counts: Counter[str] = Counter()
    low_count = 0
    temporary = low_path.with_suffix(low_path.suffix + ".tmp")
    with temporary.open("w", encoding="utf-8") as low_handle:
        for raw in records:
            arxiv_id = discovery.normalize_arxiv((raw.get("identifiers") or {}).get("arxiv", ""))
            if arxiv_id:
                all_ids.add(arxiv_id)
            item = discovery.merge_records([raw])[0]
            year_counts[publication_year(item)] += 1
            item, keep = annotate_prefilter(item, hints_by_family)
            known_status = discovery.mark_known(item, paper_names, paper_ids, taxonomy_names, taxonomy_ids)
            if known_status != "new_relative_to_bundled_corpus":
                keep = True
            if keep:
                retained_raw.append(raw)
            else:
                item["known_corpus_status"] = known_status
                item["screening_status"] = "not_screened"
                item["confidence"] = "lead"
                item["prefilter_disposition"] = "low_confidence_retained_on_disk"
                item["prefilter_tier"] = "low_confidence_lead"
                low_handle.write(json.dumps(item, ensure_ascii=False, sort_keys=True) + "\n")
                low_count += 1
    os.replace(temporary, low_path)
    return retained_raw, {
        "raw_ids": all_ids,
        "raw_years": year_counts,
        "retained_for_merge": len(retained_raw),
        "low_confidence_streamed": low_count,
    }


def combine_jsonl(paths: Iterable[Path], output: Path) -> None:
    atomic_jsonl(output, iter_jsonl_files(paths))


def full_scope_reasons(args: argparse.Namespace, categories: list[str], query_sources: list[str], families: list[dict[str, Any]]) -> list[str]:
    reasons = []
    today = datetime.now(ZoneInfo(args.timezone)).date()
    if parse_day(args.from_date) > date(1991, 1, 1):
        reasons.append("date range starts after 1991-01-01")
    if parse_day(args.until_date) != today:
        reasons.append(f"date range does not end on the current {args.timezone} date")
    if set(categories) != set(DEFAULT_CATEGORIES):
        reasons.append("arXiv category set differs from the maintained default scope")
    if set(query_sources) != set(DEFAULT_QUERY_SOURCES):
        reasons.append("query-source set differs from the maintained default scope")
    source_data = json.loads(args.queries.read_text(encoding="utf-8"))
    expected_queries = sum(len(item.get("queries", [])) for item in source_data.get("families", []))
    actual_queries = sum(len(item.get("queries", [])) for item in families)
    if actual_queries != expected_queries:
        reasons.append("not every maintained query variant was used")
    if args.skip_query_lane:
        reasons.append("query-augmentation lane was disabled")
    if args.skip_known_corpus_recall:
        reasons.append("accepted-corpus recall probes were disabled")
    if args.enumeration_fixture or args.query_fixture:
        reasons.append("fixture data was used")
    if args.max_pages_per_slice:
        reasons.append("a positive arXiv page cap was configured")
    return reasons


def evaluate_gates(enumeration: dict[str, Any], query_summary: dict[str, Any], recall_gate: dict[str, Any], raw_retention_ok: bool, fixture_used: bool, full_scope_blockers: list[str]) -> tuple[dict[str, Any], dict[str, Any]]:
    integrity_blockers = []
    if enumeration.get("status") != "complete":
        integrity_blockers.append("arXiv enumeration is partial")
    if not enumeration.get("date_coverage", {}).get("exact", False):
        integrity_blockers.append("arXiv date slices do not exactly cover the requested range")
    if query_summary.get("status") != "complete":
        integrity_blockers.append("query augmentation is partial or disabled")
    if not recall_gate.get("passed"):
        integrity_blockers.append("non-injection recall gate failed")
    if not raw_retention_ok:
        integrity_blockers.append("raw retention outputs are missing")
    if fixture_used:
        integrity_blockers.append("fixture execution cannot establish live collection coverage")
    integrity_gate = {"passed": not integrity_blockers, "blockers": integrity_blockers}
    wording_blockers = list(integrity_blockers) + list(full_scope_blockers)
    comprehensive_gate = {"passed": not wording_blockers, "blockers": list(dict.fromkeys(wording_blockers))}
    return integrity_gate, comprehensive_gate


def run() -> int:
    args = parse_args()
    for required in (args.taxonomy, args.paper_list, args.queries):
        if not required.is_file():
            print(f"Missing required file: {required}", file=sys.stderr)
            return 2
    try:
        ZoneInfo(args.timezone)
        args.until_date, args.until_date_origin = resolve_until_date(args)
        start, end = parse_day(args.from_date), parse_day(args.until_date)
        if start > end or args.slice_days < 1 or args.arxiv_per_page < 1 or args.query_variants < 0 or args.query_pages < 0 or args.stability_days < 0:
            raise ValueError("invalid historical date or pagination parameters")
        if args.max_attempts < 1 or args.retry_base_delay < 0 or args.retry_max_delay < 0:
            raise ValueError("invalid retry parameters")
        if args.max_runtime_seconds < 0 or args.progress_every_pages < 0:
            raise ValueError("invalid foreground runtime or progress setting")
    except (ValueError, KeyError) as exc:
        print(str(exc), file=sys.stderr)
        return 2

    args.output_dir.mkdir(parents=True, exist_ok=True)
    args.batch_started_monotonic = time.monotonic()
    args.batch_started_at_utc = datetime.now(timezone.utc).isoformat()
    args.deadline_monotonic = (
        args.batch_started_monotonic + args.max_runtime_seconds
        if args.max_runtime_seconds > 0
        else None
    )
    categories = [x.strip() for x in args.categories.split(",") if x.strip()]
    query_sources = [] if args.skip_query_lane else [x.strip() for x in args.query_sources.split(",") if x.strip()]
    if not categories:
        print("At least one arXiv category is required", file=sys.stderr)
        return 2
    unsupported = sorted(set(query_sources) - set(DEFAULT_QUERY_SOURCES))
    if unsupported:
        print(f"Unsupported historical query sources: {', '.join(unsupported)}", file=sys.stderr)
        return 2
    fingerprint = config_fingerprint(args, categories, query_sources)
    state_path = args.output_dir / "state.json"
    try:
        state = load_or_create_state(state_path, fingerprint)
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 2
    state["started_at_utc"] = state.get("started_at_utc") or datetime.now(timezone.utc).isoformat()
    atomic_json(state_path, state)
    input_hashes = {
        "taxonomy_sha256": file_sha256(args.taxonomy),
        "paper_list_sha256": file_sha256(args.paper_list),
        "queries_sha256": file_sha256(args.queries),
    }
    run_manifest = {
        "schema_version": RUN_SCHEMA_VERSION,
        "execution_kind": "fixture" if args.enumeration_fixture or args.query_fixture else "live",
        "configuration_fingerprint": fingerprint,
        "started_at_utc": state["started_at_utc"],
        "last_foreground_batch_started_at_utc": args.batch_started_at_utc,
        "date_range": {"from": args.from_date, "until_inclusive": args.until_date, "timezone": args.timezone},
        "categories": categories,
        "query_sources": query_sources,
        "query_variants": args.query_variants,
        "pagination": {"slice_days": args.slice_days, "arxiv_per_page": args.arxiv_per_page, "max_pages_per_slice": args.max_pages_per_slice, "query_pages": args.query_pages, "query_per_page": args.query_per_page},
        "retry_policy": {"max_attempts": args.max_attempts, "base_delay_seconds": args.retry_base_delay, "max_delay_seconds": args.retry_max_delay},
        "execution_control": {
            "stage_order": args.stage_order,
            "slice_order": args.slice_order,
            "foreground_max_runtime_seconds": args.max_runtime_seconds,
            "resumable": True,
            "until_date_origin": args.until_date_origin,
        },
        "inputs": input_hashes,
    }
    atomic_json(args.output_dir / "run_manifest.json", run_manifest)
    paper_names, paper_ids = discovery.extract_known(args.paper_list)
    taxonomy_names, taxonomy_ids = discovery.extract_known(args.taxonomy)
    families = discovery.read_query_families(args.queries, None, args.query_variants, set())
    hints_by_family = {family["id"]: family.get("taxonomy_hints", []) for family in families}
    planned_slices = len(initial_slices(start, end + timedelta(days=1), args.slice_days))
    planned_query_batches = sum(len(family.get("queries", [])) for family in families) * len(query_sources)
    emit_progress(
        args,
        state,
        "initialization",
        f"foreground batch started: {planned_query_batches} query batches and {planned_slices} initial arXiv slices in full scope",
        {"planned_query_batches": planned_query_batches, "planned_initial_slices": planned_slices},
    )

    def load_enumeration_lane() -> tuple[list[dict[str, Any]], dict[str, Any]]:
        if args.enumeration_fixture:
            fixture_records = load_jsonl(args.enumeration_fixture)
            return fixture_records, {
                "status": "complete", "categories": categories, "from_date": args.from_date,
                "until_date": args.until_date, "completed_slices": 1, "failed_slices": {},
                "truncated_slices": [], "records": len(fixture_records), "pages": 1,
                "date_coverage": {"requested_days": (end - start).days + 1, "covered_days": (end - start).days + 1, "gap_ranges": [], "overlap_days": 0, "exact": True},
                "integrity_errors": [], "recovered_integrity_errors": [],
                "network_attempts": 0, "network_retries": 0, "partial_checkpoint_files": 0,
                "stopped_for_runtime_budget": False,
                "slice_order": args.slice_order,
                "method": "offline enumeration fixture",
            }
        args.stream_results = False
        return enumerate_arxiv(args, categories, state, state_path)

    def load_query_lane() -> tuple[list[dict[str, Any]], dict[str, Any]]:
        if args.skip_query_lane:
            return [], {"status": "not_applicable", "requested_batches": 0, "completed_batches": 0, "failed_batches": 0, "truncated_batches": 0, "records": 0, "sources": {}, "family_source_matrix": [], "stopped_for_runtime_budget": False, "method": "disabled by caller"}
        if args.query_fixture:
            fixture_records = load_jsonl(args.query_fixture)
            return fixture_records, {"status": "complete", "requested_batches": 1, "completed_batches": 1, "failed_batches": 0, "truncated_batches": 0, "records": len(fixture_records), "sources": {"fixture": {"status": "complete", "records": len(fixture_records)}}, "family_source_matrix": [], "stopped_for_runtime_budget": False, "method": "offline query fixture"}
        return collect_query_lane(args, query_sources, state, state_path)

    if args.stage_order == "query_first":
        query_records, query_summary = load_query_lane()
        enumerated, enumeration = load_enumeration_lane()
    else:
        enumerated, enumeration = load_enumeration_lane()
        query_records, query_summary = load_query_lane()

    if args.enumeration_fixture:
        enumeration_paths = [args.enumeration_fixture]
    else:
        enumeration_paths = [Path(value) for value in enumeration.get("record_files", [])]
    atomic_jsonl(args.output_dir / "enumerated_raw.jsonl", iter_jsonl_files(enumeration_paths))
    atomic_jsonl(args.output_dir / "query_raw.jsonl", query_records)
    streamed_low_path = args.output_dir / "enumeration_low_confidence.stage.jsonl"
    enumeration_retained, stream_stats = stream_prefilter_enumeration(
        iter_jsonl_files(enumeration_paths), streamed_low_path, hints_by_family,
        paper_names, paper_ids, taxonomy_names, taxonomy_ids,
    )
    raw_ids = set(stream_stats["raw_ids"])
    raw_years = Counter(stream_stats["raw_years"])
    for raw in query_records:
        arxiv_id = discovery.normalize_arxiv((raw.get("identifiers") or {}).get("arxiv", ""))
        if arxiv_id:
            raw_ids.add(arxiv_id)
        raw_years[publication_year(discovery.merge_records([raw])[0])] += 1
    combined = discovery.merge_records(enumeration_retained + query_records)

    candidates, low_confidence = [], []
    for item in combined:
        item, keep = annotate_prefilter(item, hints_by_family)
        score = item["prefilter_score"]
        item["known_corpus_status"] = discovery.mark_known(item, paper_names, paper_ids, taxonomy_names, taxonomy_ids)
        if item["known_corpus_status"] != "new_relative_to_bundled_corpus":
            keep = True
        item["screening_status"] = "not_screened"
        item["confidence"] = "lead"
        item["discovery_lanes"] = sorted({"enumeration" if record.get("query_family") == "category_date_enumeration" else "query_augmentation" for record in item.get("source_records", [])})
        if keep:
            item["prefilter_disposition"] = "retained_for_screening"
            item["prefilter_tier"] = "strong_lead" if score >= 9 else "plausible_lead"
            candidates.append(item)
        else:
            item["prefilter_disposition"] = "low_confidence_retained_on_disk"
            item["prefilter_tier"] = "low_confidence_lead"
            low_confidence.append(item)

    candidates.sort(key=lambda item: (-item["prefilter_score"], discovery.normalize_title(item["canonical_title"])))
    low_confidence.sort(key=lambda item: (-item["prefilter_score"], discovery.normalize_title(item["canonical_title"])))
    atomic_jsonl(args.output_dir / "candidates.jsonl", candidates)
    def all_low_confidence():
        yield from iter_jsonl_files([streamed_low_path])
        yield from low_confidence
    atomic_jsonl(args.output_dir / "low_confidence_records.jsonl", all_low_confidence())
    streamed_low_path.unlink()

    expected = []
    recall_passed = True
    expected_values = list(args.expected_id)
    if not args.skip_known_corpus_recall:
        expected_values.extend(sorted(paper_ids))
    for value in dict.fromkeys(expected_values):
        arxiv_id = discovery.normalize_arxiv(value)
        origin = "accepted_corpus" if arxiv_id in paper_ids else "caller_probe"
        applicable = origin == "caller_probe" or arxiv_id_intersects_range(arxiv_id, start, end)
        in_unfiltered = arxiv_id in raw_ids
        in_candidates = any(discovery.normalize_arxiv((item.get("identifiers") or {}).get("arxiv", "")) == arxiv_id for item in candidates)
        expected.append({"arxiv": arxiv_id, "origin": origin, "applicable_to_date_range": applicable, "range_basis": "caller_probe" if origin == "caller_probe" else "arXiv ID year-month", "in_unfiltered_union": in_unfiltered, "in_candidates": in_candidates, "injected": False})
        if applicable:
            recall_passed = recall_passed and in_unfiltered and in_candidates

    recall_gate = {
        "expected_ids": expected,
        "applicable_count": sum(1 for item in expected if item["applicable_to_date_range"]),
        "passed": recall_passed,
        "non_injection": True,
        "accepted_corpus_check_enabled": not args.skip_known_corpus_recall,
    }
    fixture_used = bool(args.enumeration_fixture or args.query_fixture)
    raw_retention_ok = (args.output_dir / "enumerated_raw.jsonl").is_file() and (args.output_dir / "query_raw.jsonl").is_file() and (args.output_dir / "low_confidence_records.jsonl").is_file()
    scope_blockers = full_scope_reasons(args, categories, query_sources, families)
    integrity_gate, comprehensive_gate = evaluate_gates(enumeration, query_summary, recall_gate, raw_retention_ok, fixture_used, scope_blockers)
    if comprehensive_gate["passed"]:
        recommended_label = "best-effort comprehensive automated historical sweep"
    elif integrity_gate["passed"]:
        recommended_label = "targeted historical candidate sweep with explicit coverage limits"
    else:
        recommended_label = "partial historical candidate sweep; coverage gates not passed"
    low_confidence_total = stream_stats["low_confidence_streamed"] + len(low_confidence)
    raw_record_total = enumeration["records"] + len(query_records)
    foreground_stopped = bool(
        enumeration.get("stopped_for_runtime_budget")
        or query_summary.get("stopped_for_runtime_budget")
    )
    enumeration_resume_required = enumeration.get("status") != "complete"
    query_resume_required = not args.skip_query_lane and query_summary.get("status") != "complete"
    resume_required = enumeration_resume_required or query_resume_required
    batch_elapsed_seconds = round(time.monotonic() - args.batch_started_monotonic, 3)
    foreground_batch = {
        "status": "checkpoint_ready" if resume_required else "collection_finished",
        "started_at_utc": args.batch_started_at_utc,
        "elapsed_seconds": batch_elapsed_seconds,
        "max_runtime_seconds": args.max_runtime_seconds,
        "stopped_for_runtime_budget": foreground_stopped,
        "resume_required": resume_required,
        "resume_same_output_directory": resume_required,
        "stage_order": args.stage_order,
        "slice_order": args.slice_order,
        "planned_initial_slices": planned_slices,
        "planned_query_batches": planned_query_batches,
    }
    coverage = {
        "mode": "historical",
        "claim_policy": {
            "forbidden": ["all papers", "complete literature", "provably exhaustive"],
            "allowed_when_automated_gate_passes": "best-effort comprehensive automated historical sweep",
            "default": "historical candidate sweep with explicit coverage limits",
            "note": "Even a passing automated gate does not cover every publisher, venue archive, or unindexed work.",
        },
        "recommended_label": recommended_label,
        "execution_kind": "fixture" if fixture_used else "live",
        "run_schema_version": RUN_SCHEMA_VERSION,
        "foreground_batch": foreground_batch,
        "date_range": {"from": args.from_date, "until_inclusive": args.until_date, "timezone": args.timezone},
        "enumeration_lane": enumeration,
        "query_augmentation_lane": query_summary,
        "records": {
            "enumerated_raw": enumeration["records"], "query_raw": len(query_records),
            "raw_records_across_lanes": raw_record_total,
            "enumeration_retained_for_merge": stream_stats["retained_for_merge"],
            "deduplicated_prefilter_union": len(combined), "candidates": len(candidates),
            "low_confidence_retained": low_confidence_total,
        },
        "candidate_sources": dict(Counter(source for item in candidates for source in item.get("sources", []))),
        "candidate_query_families": dict(Counter(family for item in candidates for family in item.get("query_families", []))),
        "candidate_years": dict(sorted(Counter(publication_year(item) for item in candidates).items())),
        "raw_record_years_before_cross_lane_deduplication": dict(sorted(raw_years.items())),
        "known_status_counts": dict(Counter(item.get("known_corpus_status") for item in candidates)),
        "prefilter_audit": {
            "retained": len(candidates),
            "low_confidence_retained_on_disk": low_confidence_total,
            "retention_rate_against_raw_records": (len(candidates) / raw_record_total) if raw_record_total else 0.0,
            "enumeration_stream_prefilter_retained": stream_stats["retained_for_merge"],
            "tiers": dict(Counter(item.get("prefilter_tier") for item in candidates + low_confidence)) | {"streamed_low_confidence_lead": stream_stats["low_confidence_streamed"]},
        },
        "recall_gate": recall_gate,
        "collection_integrity_gate": integrity_gate,
        "comprehensive_wording_gate": comprehensive_gate,
        "automated_coverage_gate": comprehensive_gate,
        "full_scope_blockers": scope_blockers,
        "manual_follow_up_required": ["OpenReview", "official venue/proceedings archives", "CVF/ACM/IEEE/Eurographics", "project and author/lab pages", "citation and reference chaining"],
        "finished_at_utc": datetime.now(timezone.utc).isoformat(),
    }
    atomic_json(args.output_dir / "coverage.json", coverage)
    manifest = sorted(state.get("completed_slices", {}).values(), key=lambda item: item["start"])
    atomic_jsonl(args.output_dir / "slice_manifest.jsonl", manifest)
    if resume_required:
        checkpoint_note = "This is a completed foreground checkpoint, not a finished historical collection. Re-run the same command with the same output directory to continue."
        next_action = "Re-run the same command with this exact output directory. Completed pages, query batches, and arXiv slices will be reused after integrity checks."
    else:
        checkpoint_note = "The automated collection stages finished for the configured scope; screening, curation, and manual archive follow-up may still remain."
        next_action = "Proceed to bounded candidate screening and taxonomy curation; preserve the manual follow-up limitations below."
    report = "\n".join([
        "# Agentic Graphics Historical Candidate Sweep",
        "",
        "> This is not an all-papers guarantee. It is an auditable, resumable candidate sweep.",
        f"> {checkpoint_note}",
        "",
        f"- Foreground batch: `{foreground_batch['status']}`; {batch_elapsed_seconds:.3f}s elapsed; configured budget {args.max_runtime_seconds:g}s",
        f"- Resume required: `{'yes' if resume_required else 'no'}`",
        f"- Date range: `{args.from_date}` through `{args.until_date}` (inclusive)",
        f"- Enumeration lane: `{enumeration['status']}`; {enumeration['records']} raw arXiv records; {enumeration['completed_slices']} completed slices",
        f"- Query-augmentation lane: `{query_summary['status']}`; {query_summary.get('completed_batches', 0)}/{query_summary.get('requested_batches', 0)} batches; {query_summary['records']} raw records",
        f"- Deduplicated prefilter union: {len(combined)}",
        f"- Retained for screening: {len(candidates)}",
        f"- Low-confidence records retained on disk: {low_confidence_total}",
        f"- Non-injection recall gate: `{'passed' if recall_passed else 'failed'}`",
        f"- Collection-integrity gate: `{'passed' if integrity_gate['passed'] else 'failed'}`",
        f"- Comprehensive-wording gate: `{'passed' if comprehensive_gate['passed'] else 'failed'}`",
        f"- Required report label: `{recommended_label}`",
        "",
        "## Next action",
        "",
        next_action,
        "",
        "## Blocking reasons",
        "",
        *([f"- {reason}" for reason in comprehensive_gate["blockers"]] or ["- None for the automated gate; manual archive follow-up is still required."]),
        "",
        "## Interpretation",
        "",
        "Use `best-effort comprehensive automated historical sweep` only when the automated coverage gate passes. Even then, report unqueried or manually followed-up archives and never claim that all papers were found.",
        "",
        "The candidate and low-confidence files are discovery outputs, not survey inclusion decisions. Send plausible candidates to paper screening and taxonomy curation.",
    ]) + "\n"
    (args.output_dir / "report.md").write_text(report, encoding="utf-8")
    run_manifest["finished_at_utc"] = coverage["finished_at_utc"]
    run_manifest["last_foreground_batch_elapsed_seconds"] = batch_elapsed_seconds
    run_manifest["foreground_checkpoint_ready"] = True
    run_manifest["resume_required"] = resume_required
    run_manifest["recommended_label"] = recommended_label
    run_manifest["collection_integrity_gate_passed"] = integrity_gate["passed"]
    run_manifest["comprehensive_wording_gate_passed"] = comprehensive_gate["passed"]
    atomic_json(args.output_dir / "run_manifest.json", run_manifest)
    state["last_foreground_batch_finished_at_utc"] = coverage["finished_at_utc"]
    state["last_foreground_batch_elapsed_seconds"] = batch_elapsed_seconds
    state["resume_required"] = resume_required
    atomic_json(state_path, state)
    final_progress = {
        "mode": "historical",
        "in_progress": False,
        "phase": "checkpoint_ready" if resume_required else "collection_finished",
        "message": next_action,
        "started_at_utc": args.batch_started_at_utc,
        "finished_at_utc": coverage["finished_at_utc"],
        "elapsed_seconds": batch_elapsed_seconds,
        "max_runtime_seconds": args.max_runtime_seconds,
        "stopped_for_runtime_budget": foreground_stopped,
        "resume_required": resume_required,
        "stage_order": args.stage_order,
        "slice_order": args.slice_order,
        "enumeration_status": enumeration.get("status"),
        "completed_slices": enumeration.get("completed_slices", 0),
        "query_status": query_summary.get("status"),
        "completed_query_batches": query_summary.get("completed_batches", 0),
        "requested_query_batches": query_summary.get("requested_batches", 0),
        "candidates": len(candidates),
        "recommended_label": recommended_label,
    }
    atomic_json(args.output_dir / "progress.json", final_progress)
    audit_script = SCRIPT_DIR / "audit_historical_run.py"
    audit_spec = importlib.util.spec_from_file_location("agentic_graphics_historical_audit", audit_script)
    audit_module = importlib.util.module_from_spec(audit_spec)
    assert audit_spec and audit_spec.loader
    audit_spec.loader.exec_module(audit_module)
    audit_result = audit_module.audit(args.output_dir)
    atomic_json(args.output_dir / "audit.json", audit_result)
    final_progress["artifact_contract_passed"] = audit_result["artifact_contract_passed"]
    atomic_json(args.output_dir / "progress.json", final_progress)
    print(json.dumps({"output_dir": str(args.output_dir), "foreground_status": foreground_batch["status"], "resume_required": resume_required, "elapsed_seconds": batch_elapsed_seconds, "enumerated_raw": enumeration["records"], "completed_slices": enumeration["completed_slices"], "query_raw": len(query_records), "completed_query_batches": query_summary.get("completed_batches", 0), "requested_query_batches": query_summary.get("requested_batches", 0), "candidates": len(candidates), "recommended_label": recommended_label, "artifact_contract": audit_result["artifact_contract_passed"], "collection_integrity_gate": integrity_gate["passed"], "comprehensive_wording_gate": comprehensive_gate["passed"]}, indent=2))
    if not audit_result["artifact_contract_passed"]:
        return 4
    return 0 if integrity_gate["passed"] else 3


if __name__ == "__main__":
    raise SystemExit(run())
