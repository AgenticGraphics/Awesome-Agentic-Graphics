#!/usr/bin/env python3
"""Multi-source Agentic Graphics candidate collector.

The collector preserves raw evidence, normalizes identifiers, deduplicates across
sources, and applies a deliberately high-recall local lexical prefilter. Final
paper inclusion and taxonomy assignment belong to downstream skills.
"""

from __future__ import annotations

import argparse
import html
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from datetime import date, datetime, timedelta, timezone
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any, Iterable
from zoneinfo import ZoneInfo


USER_AGENT = "agentic-graphics-research/2026.09 (literature discovery; contact via local user)"
DEFAULT_SOURCES = [
    "arxiv",
    "openalex",
    "crossref",
    "semantic_scholar",
    "dblp",
    "huggingface",
    "github",
]
PROFILES = {
    "smoke": {
        "family_limit": 3, "variants": 1, "pages": 1, "per_page": 10,
        "sources": ["arxiv", "openalex", "crossref"],
        "timeout": 8, "request_delay": 0.0,
        "source_time_budget_seconds": 20.0, "max_runtime_seconds": 90.0,
    },
    # The normal same-day profile deliberately covers every query family and
    # source family without multiplying each query by three pages. Exact-day
    # filters make one 100-record page per query a practical high-recall first
    # pass; targeted official-web follow-up remains mandatory.
    "daily": {
        "family_limit": None, "variants": 2, "pages": 1, "per_page": 100,
        "sources": DEFAULT_SOURCES,
        "timeout": 10, "request_delay": 0.05,
        "source_time_budget_seconds": 45.0, "max_runtime_seconds": 360.0,
    },
    "standard": {
        "family_limit": None, "variants": 2, "pages": 1, "per_page": 25,
        "sources": ["arxiv", "openalex", "crossref", "semantic_scholar", "dblp", "huggingface"],
        "timeout": 12, "request_delay": 0.05,
        "source_time_budget_seconds": 60.0, "max_runtime_seconds": 420.0,
    },
    # Retained for explicit diagnostics. It is bounded so an unavailable API
    # cannot turn a requested report into an unbounded silent process.
    "exhaustive": {
        "family_limit": None, "variants": 4, "pages": 3, "per_page": 100,
        "sources": DEFAULT_SOURCES,
        "timeout": 15, "request_delay": 0.05,
        "source_time_budget_seconds": 120.0, "max_runtime_seconds": 900.0,
    },
}

AGENT_TERMS = [
    "agent", "agentic", "multi-agent", "multi agent", "planner", "executor",
    "critic", "tool use", "tool-use", "tool using", "tool-using", "function calling",
    "computer use", "workflow", "language model", "llm", "vision-language model",
    "vision language model", "vlm", "mcp", "self-refinement", "self refinement",
]
GRAPHICS_TERMS = [
    "computer graphics", "graphics", "3d", "cad", "blender", "freecad", "cadquery",
    "scene", "render", "rendering", "inverse graphics", "geometry", "geometric",
    "mesh", "shape", "procedural", "animation", "rigging", "motion authoring",
    "simulation", "simulator", "physical world", "svg", "vector graphic", "slide",
    "presentation", "document layout", "material", "lighting", "dcc", "unreal engine",
    "ue5", "game engine", "world generation", "asset generation", "visual authoring",
    "photoshop", "illustrator", "maya", "unity", "creative software", "image editing",
    "visual design", "spatial reasoning", "spatial intelligence", "physical grounding",
    "pdf", "document editing", "diagram", "gui",
]
STRONG_COMBINED_TERMS = [
    "agentic graphics", "graphics agent", "3d agent", "cad agent", "blender agent",
    "scene agent", "inverse graphics agent", "simulation agent", "svg agent",
    "graphics code generation", "procedural graphics program", "shape program",
]
NEGATIVE_DOMAINS = [
    "molecule", "molecular", "protein", "drug discovery", "clinical", "genomic",
    "wireless network", "financial trading", "cybersecurity", "medical imaging",
]
ADJACENT_QUERY_FAMILIES = {
    "spatial_reasoning_components",
    "tool_interfaces",
    "benchmarks_and_evaluation",
    "training_and_adaptation",
    "historical_executable_representations",
}


def clean_text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, list):
        value = " ".join(str(x) for x in value)
    text = html.unescape(str(value))
    text = re.sub(r"<[^>]+>", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def normalize_title(title: str) -> str:
    value = clean_text(title).lower()
    value = re.sub(r"https?://\S+", " ", value)
    value = re.sub(r"[^a-z0-9]+", " ", value)
    return re.sub(r"\s+", " ", value).strip()


def title_bucket(title: str) -> str:
    """Bound fuzzy comparisons to a narrow prefix bucket at corpus scale."""
    return normalize_title(title)[:48]


def contains_term(text: str, term: str) -> bool:
    """Match a normalized token or phrase, never an arbitrary substring."""
    needle = normalize_title(term)
    return bool(needle) and f" {needle} " in f" {text} "


def matched_terms(text: str, terms: Iterable[str]) -> list[str]:
    result = []
    seen = set()
    for term in terms:
        normalized = normalize_title(term)
        if normalized not in seen and contains_term(text, term):
            seen.add(normalized)
            result.append(term)
    return sorted(result)


def normalize_doi(value: str) -> str:
    value = clean_text(value).lower()
    value = re.sub(r"^https?://(dx\.)?doi\.org/", "", value)
    return value.strip()


def normalize_arxiv(value: str) -> str:
    match = re.search(r"(?:arxiv:|arxiv\.org/(?:abs|pdf)/)?(\d{4}\.\d{4,5})(?:v\d+)?", value or "", re.I)
    return match.group(1) if match else ""


def iso_day(value: str) -> str:
    if not value:
        return ""
    match = re.match(r"^(\d{4}-\d{2}-\d{2})", value)
    return match.group(1) if match else ""


def date_parts_to_iso(parts: Any) -> str:
    try:
        values = parts[0] if parts and isinstance(parts[0], list) else parts
        if not values or len(values) < 3:
            return ""
        return f"{int(values[0]):04d}-{int(values[1]):02d}-{int(values[2]):02d}"
    except (TypeError, ValueError, IndexError):
        return ""


def open_url(url: str, timeout: int, headers: dict[str, str]) -> bytes:
    """Perform one bounded request; the historical runner owns retry policy.

    Keeping retries in one layer prevents an outer retry from multiplying an
    inner retry into long silent stalls. Standalone diagnostic collection is
    intentionally fail-fast and records the failed source.
    """
    request = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return response.read()


def get_json(url: str, timeout: int, token: str = "") -> Any:
    headers = {"User-Agent": USER_AGENT, "Accept": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return json.loads(open_url(url, timeout, headers).decode("utf-8", errors="replace"))


def get_text(url: str, timeout: int) -> str:
    return open_url(url, timeout, {"User-Agent": USER_AGENT}).decode("utf-8", errors="replace")


def base_record(source: str, kind: str = "paper") -> dict[str, Any]:
    return {
        "kind": kind,
        "source": source,
        "title": "",
        "authors": [],
        "abstract": "",
        "identifiers": {},
        "urls": [],
        "venue": "",
        "event_dates": [],
        "query_family": "",
        "query": "",
    }


def event(kind: str, value: str, source: str, precision: str = "day") -> dict[str, str]:
    return {"kind": kind, "value": value, "date": iso_day(value), "source": source, "precision": precision}


def fetch_arxiv(
    query: str,
    family: str,
    page: int,
    per_page: int,
    timeout: int,
    target_day: str = "",
) -> list[dict[str, Any]]:
    search_query = f'all:"{query}"'
    if target_day:
        # Query a deliberately wider UTC submission window, then let the local
        # America/Chicago event gate make the exact inclusion decision. This
        # avoids filling the page with old relevance-ranked results without
        # introducing a timezone-boundary false negative.
        center = date.fromisoformat(target_day)
        start = (center - timedelta(days=1)).strftime("%Y%m%d0000")
        end = (center + timedelta(days=1)).strftime("%Y%m%d2359")
        search_query = f'({search_query}) AND submittedDate:[{start} TO {end}]'
    params = {
        "search_query": search_query,
        "start": page * per_page,
        "max_results": per_page,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    }
    suffix = "/api/query?" + urllib.parse.urlencode(params)
    last_error: Exception | None = None
    xml = ""
    for base in ("https://export.arxiv.org", "https://arxiv.org"):
        try:
            xml = get_text(base + suffix, timeout)
            break
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError) as exc:
            last_error = exc
    if not xml:
        assert last_error is not None
        raise last_error
    root = ET.fromstring(xml)
    ns = {"atom": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}
    records = []
    for entry in root.findall("atom:entry", ns):
        rec = base_record("arxiv")
        rec["query_family"], rec["query"] = family, query
        rec["title"] = clean_text(entry.findtext("atom:title", default="", namespaces=ns))
        rec["abstract"] = clean_text(entry.findtext("atom:summary", default="", namespaces=ns))
        rec["authors"] = [clean_text(x.findtext("atom:name", default="", namespaces=ns)) for x in entry.findall("atom:author", ns)]
        entry_id = clean_text(entry.findtext("atom:id", default="", namespaces=ns))
        arxiv_id = normalize_arxiv(entry_id)
        rec["identifiers"] = {"arxiv": arxiv_id} if arxiv_id else {}
        rec["urls"] = [entry_id] if entry_id else []
        published = clean_text(entry.findtext("atom:published", default="", namespaces=ns))
        updated = clean_text(entry.findtext("atom:updated", default="", namespaces=ns))
        if published:
            rec["event_dates"].append(event("published", published, "arxiv"))
        if updated:
            rec["event_dates"].append(event("updated", updated, "arxiv"))
        rec["event_dates"] = unique_dicts(rec["event_dates"])
        records.append(rec)
    return records


def fetch_arxiv_ids(ids: list[str], timeout: int) -> list[dict[str, Any]]:
    if not ids:
        return []
    url = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode({"id_list": ",".join(ids), "max_results": len(ids)})
    root = ET.fromstring(get_text(url, timeout))
    ns = {"atom": "http://www.w3.org/2005/Atom"}
    records = []
    for entry in root.findall("atom:entry", ns):
        rec = base_record("arxiv")
        rec["query_family"], rec["query"] = "must_include", "direct arXiv ID"
        rec["title"] = clean_text(entry.findtext("atom:title", default="", namespaces=ns))
        rec["abstract"] = clean_text(entry.findtext("atom:summary", default="", namespaces=ns))
        rec["authors"] = [clean_text(x.findtext("atom:name", default="", namespaces=ns)) for x in entry.findall("atom:author", ns)]
        entry_id = clean_text(entry.findtext("atom:id", default="", namespaces=ns))
        arxiv_id = normalize_arxiv(entry_id)
        rec["identifiers"] = {"arxiv": arxiv_id} if arxiv_id else {}
        rec["urls"] = [entry_id] if entry_id else []
        for field in ("published", "updated"):
            value = clean_text(entry.findtext(f"atom:{field}", default="", namespaces=ns))
            if value:
                rec["event_dates"].append(event(field, value, "arxiv"))
        records.append(rec)
    return records


def fetch_openalex(query: str, family: str, page: int, per_page: int, timeout: int, target_day: str = "") -> list[dict[str, Any]]:
    filters = []
    if target_day:
        filters.extend([f"from_publication_date:{target_day}", f"to_publication_date:{target_day}"])
    params = {"search": query, "per-page": per_page, "page": page + 1}
    if filters:
        params["filter"] = ",".join(filters)
    url = "https://api.openalex.org/works?" + urllib.parse.urlencode(params)
    data = get_json(url, timeout)
    records = []
    for item in data.get("results", []):
        rec = base_record("openalex")
        rec["query_family"], rec["query"] = family, query
        rec["title"] = clean_text(item.get("display_name"))
        rec["abstract"] = inverted_abstract(item.get("abstract_inverted_index"))
        rec["authors"] = [clean_text(a.get("author", {}).get("display_name")) for a in item.get("authorships", [])]
        ids = item.get("ids") or {}
        rec["identifiers"] = {
            k: v for k, v in {
                "doi": normalize_doi(ids.get("doi", "")),
                "openalex": clean_text(ids.get("openalex", "")),
                "arxiv": normalize_arxiv(" ".join(str(x) for x in ids.values())),
            }.items() if v
        }
        primary = item.get("primary_location") or {}
        rec["urls"] = [u for u in [primary.get("landing_page_url"), primary.get("pdf_url"), ids.get("doi"), ids.get("openalex")] if u]
        rec["venue"] = clean_text((primary.get("source") or {}).get("display_name"))
        published = clean_text(item.get("publication_date"))
        if published:
            rec["event_dates"].append(event("published", published, "openalex"))
        records.append(rec)
    return records


def inverted_abstract(index: Any) -> str:
    if not isinstance(index, dict):
        return ""
    words = []
    for token, positions in index.items():
        for pos in positions:
            words.append((int(pos), token))
    return clean_text(" ".join(token for _, token in sorted(words)))


def fetch_crossref(query: str, family: str, page: int, per_page: int, timeout: int, target_day: str = "") -> list[dict[str, Any]]:
    params = {"query.bibliographic": query, "rows": per_page, "offset": page * per_page}
    if target_day:
        params["filter"] = f"from-online-pub-date:{target_day},until-online-pub-date:{target_day}"
    url = "https://api.crossref.org/works?" + urllib.parse.urlencode(params)
    data = get_json(url, timeout)
    records = []
    for item in data.get("message", {}).get("items", []):
        rec = base_record("crossref")
        rec["query_family"], rec["query"] = family, query
        rec["title"] = clean_text(item.get("title", []))
        rec["abstract"] = clean_text(item.get("abstract", ""))
        rec["authors"] = [clean_text(" ".join([a.get("given", ""), a.get("family", "")])) for a in item.get("author", [])]
        doi = normalize_doi(item.get("DOI", ""))
        rec["identifiers"] = {"doi": doi} if doi else {}
        rec["urls"] = [u for u in [item.get("URL"), f"https://doi.org/{doi}" if doi else ""] if u]
        rec["venue"] = clean_text(item.get("container-title", []))
        for label, key in (("published", "published-online"), ("published", "published-print"), ("published", "issued")):
            value = date_parts_to_iso((item.get(key) or {}).get("date-parts"))
            if value:
                rec["event_dates"].append(event(label, value, "crossref"))
        records.append(rec)
    return records


def fetch_semantic_scholar(
    query: str,
    family: str,
    page: int,
    per_page: int,
    timeout: int,
    target_day: str = "",
) -> list[dict[str, Any]]:
    fields = "title,abstract,authors,year,publicationDate,externalIds,url,venue,openAccessPdf"
    params = {"query": query, "limit": min(per_page, 100), "offset": page * min(per_page, 100), "fields": fields}
    if target_day:
        params["publicationDateOrYear"] = f"{target_day}:{target_day}"
    url = "https://api.semanticscholar.org/graph/v1/paper/search?" + urllib.parse.urlencode(params)
    data = get_json(url, timeout)
    records = []
    for item in data.get("data", []):
        rec = base_record("semantic_scholar")
        rec["query_family"], rec["query"] = family, query
        rec["title"] = clean_text(item.get("title"))
        rec["abstract"] = clean_text(item.get("abstract"))
        rec["authors"] = [clean_text(a.get("name")) for a in item.get("authors", [])]
        external = item.get("externalIds") or {}
        rec["identifiers"] = {
            k: v for k, v in {
                "doi": normalize_doi(external.get("DOI", "")),
                "arxiv": normalize_arxiv(external.get("ArXiv", "")),
                "semantic_scholar": clean_text(item.get("paperId")),
            }.items() if v
        }
        pdf = (item.get("openAccessPdf") or {}).get("url")
        rec["urls"] = [u for u in [item.get("url"), pdf] if u]
        rec["venue"] = clean_text(item.get("venue"))
        published = clean_text(item.get("publicationDate"))
        if published:
            rec["event_dates"].append(event("published", published, "semantic_scholar"))
        records.append(rec)
    return records


def fetch_dblp(query: str, family: str, page: int, per_page: int, timeout: int) -> list[dict[str, Any]]:
    params = {"q": query, "h": per_page, "f": page * per_page, "format": "json"}
    url = "https://dblp.org/search/publ/api?" + urllib.parse.urlencode(params)
    data = get_json(url, timeout)
    records = []
    for hit in data.get("result", {}).get("hits", {}).get("hit", []):
        item = hit.get("info", {})
        rec = base_record("dblp")
        rec["query_family"], rec["query"] = family, query
        rec["title"] = clean_text(item.get("title"))
        authors = (item.get("authors") or {}).get("author", [])
        if isinstance(authors, dict):
            authors = [authors]
        rec["authors"] = [clean_text(a.get("text") if isinstance(a, dict) else a) for a in authors]
        doi = normalize_doi(item.get("doi", ""))
        rec["identifiers"] = {"doi": doi} if doi else {}
        rec["urls"] = [u for u in [item.get("url"), item.get("ee")] if u]
        rec["venue"] = clean_text(item.get("venue"))
        year = clean_text(item.get("year"))
        if re.fullmatch(r"\d{4}", year):
            rec["event_dates"].append(event("published", year, "dblp", precision="year"))
        records.append(rec)
    return records


def huggingface_records(data: Any, family: str, query: str) -> list[dict[str, Any]]:
    if isinstance(data, dict):
        data = data.get("papers") or data.get("results") or []
    records = []
    for wrapper in data if isinstance(data, list) else []:
        item = wrapper.get("paper") if isinstance(wrapper, dict) and isinstance(wrapper.get("paper"), dict) else wrapper
        if not isinstance(item, dict):
            continue
        rec = base_record("huggingface")
        rec["query_family"], rec["query"] = family, query
        rec["title"] = clean_text(item.get("title"))
        rec["abstract"] = clean_text(item.get("summary") or item.get("abstract"))
        authors = item.get("authors") or []
        rec["authors"] = [clean_text(a.get("name") if isinstance(a, dict) else a) for a in authors]
        arxiv_id = normalize_arxiv(clean_text(item.get("id") or item.get("paperId") or item.get("arxivId")))
        rec["identifiers"] = {"arxiv": arxiv_id} if arxiv_id else {}
        rec["urls"] = [u for u in [item.get("url"), f"https://huggingface.co/papers/{arxiv_id}" if arxiv_id else ""] if u]
        curated = clean_text(item.get("publishedAt") or item.get("published_at") or item.get("publishedOn"))
        if curated:
            rec["event_dates"].append(event("curated", curated, "huggingface"))
        records.append(rec)
    return records


def fetch_huggingface_daily(timeout: int, target_day: str, page: int, per_page: int) -> list[dict[str, Any]]:
    params = {"p": page, "limit": min(per_page, 100), "date": target_day, "sort": "publishedAt"}
    data = get_json("https://huggingface.co/api/daily_papers?" + urllib.parse.urlencode(params), timeout)
    return huggingface_records(data, "daily_papers", f"daily papers {target_day}")


def fetch_huggingface_search(query: str, family: str, per_page: int, timeout: int) -> list[dict[str, Any]]:
    params = {"q": query, "limit": min(per_page, 120)}
    data = get_json("https://huggingface.co/api/papers/search?" + urllib.parse.urlencode(params), timeout)
    return huggingface_records(data, family, query)


def fetch_github(query: str, family: str, page: int, per_page: int, timeout: int, target_day: str = "") -> list[dict[str, Any]]:
    gh_query = f"{query} in:name,description,readme"
    if target_day:
        gh_query += f" created:{target_day}"
    params = {"q": gh_query, "per_page": min(per_page, 100), "page": page + 1, "sort": "updated", "order": "desc"}
    url = "https://api.github.com/search/repositories?" + urllib.parse.urlencode(params)
    data = get_json(url, timeout, token=os.environ.get("GITHUB_TOKEN", ""))
    records = []
    for item in data.get("items", []):
        rec = base_record("github", kind="artifact")
        rec["query_family"], rec["query"] = family, query
        rec["title"] = clean_text(item.get("full_name"))
        rec["abstract"] = clean_text(item.get("description"))
        rec["authors"] = [clean_text((item.get("owner") or {}).get("login"))]
        rec["identifiers"] = {"github": clean_text(item.get("full_name"))}
        rec["urls"] = [item.get("html_url")] if item.get("html_url") else []
        for label, key in (("created", "created_at"), ("updated", "updated_at"), ("pushed", "pushed_at")):
            value = clean_text(item.get(key))
            if value:
                rec["event_dates"].append(event(label, value, "github"))
        records.append(rec)
    return records


FETCHERS = {
    "arxiv": fetch_arxiv,
    "openalex": fetch_openalex,
    "crossref": fetch_crossref,
    "semantic_scholar": fetch_semantic_scholar,
    "dblp": fetch_dblp,
    "github": fetch_github,
}


def read_query_families(path: Path, limit: int | None, variants: int, selected: set[str]) -> list[dict[str, Any]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    families = data.get("families", [])
    if selected:
        families = [f for f in families if f.get("id") in selected]
    if limit is not None:
        families = families[:limit]
    result = []
    for family in families:
        copy = dict(family)
        queries = list(family.get("queries", []))
        copy["queries"] = queries[:variants] if variants > 0 else queries
        result.append(copy)
    return result


def extract_known(path: Path) -> tuple[set[str], set[str]]:
    text = path.read_text(encoding="utf-8")
    names = set()
    for match in re.findall(r"\*\*([^*]{3,180})\*\*", text):
        value = normalize_title(match)
        if len(value.split()) >= 1 and value not in {"base model", "harness", "benchmark", "taxonomy"}:
            names.add(value)
    ids = set(re.findall(r"\b\d{4}\.\d{4,5}\b", text))
    return names, ids


def record_key(record: dict[str, Any]) -> str:
    ids = record.get("identifiers") or {}
    if ids.get("doi"):
        return "doi:" + normalize_doi(ids["doi"])
    if ids.get("arxiv"):
        return "arxiv:" + normalize_arxiv(ids["arxiv"])
    title = normalize_title(record.get("title", ""))
    if title:
        return "title:" + title
    urls = record.get("urls") or []
    return "url:" + (urls[0] if urls else json.dumps(record, sort_keys=True))


def merge_records(records: Iterable[dict[str, Any]]) -> list[dict[str, Any]]:
    merged: list[dict[str, Any]] = []
    by_key: dict[str, int] = {}
    fuzzy_title_buckets: dict[str, set[int]] = defaultdict(set)
    for raw in records:
        key = record_key(raw)
        idx = by_key.get(key)
        if idx is None:
            for url in raw.get("urls") or []:
                if clean_text(url) and ("url:" + clean_text(url)) in by_key:
                    idx = by_key["url:" + clean_text(url)]
                    break
        title = normalize_title(raw.get("title", ""))
        if idx is None and title:
            idx = by_key.get("title:" + title)
        if idx is None and title:
            bucket = title_bucket(title)
            for pos in fuzzy_title_buckets.get(bucket, set()):
                existing = merged[pos]
                other = normalize_title(existing.get("canonical_title", ""))
                raw_ids = raw.get("identifiers") or {}
                existing_ids = existing.get("identifiers") or {}
                conflicting_arxiv = raw_ids.get("arxiv") and existing_ids.get("arxiv") and normalize_arxiv(raw_ids["arxiv"]) != normalize_arxiv(existing_ids["arxiv"])
                conflicting_doi = raw_ids.get("doi") and existing_ids.get("doi") and normalize_doi(raw_ids["doi"]) != normalize_doi(existing_ids["doi"])
                if conflicting_arxiv or conflicting_doi:
                    continue
                if title and other and SequenceMatcher(None, title, other).ratio() >= 0.965:
                    idx = pos
                    break
        source_record = {
            "source": raw.get("source"), "query_family": raw.get("query_family"),
            "query": raw.get("query"), "urls": raw.get("urls", []),
            "event_dates": raw.get("event_dates", []), "identifiers": raw.get("identifiers", {}),
            "categories": raw.get("categories", []),
            "enumeration_window": raw.get("enumeration_window", ""),
        }
        if idx is None:
            item = {
                "kind": raw.get("kind", "paper"),
                "canonical_title": clean_text(raw.get("title")),
                "authors": [x for x in raw.get("authors", []) if x],
                "abstract": clean_text(raw.get("abstract")),
                "identifiers": dict(raw.get("identifiers") or {}),
                "canonical_urls": list(dict.fromkeys(raw.get("urls") or [])),
                "venue": clean_text(raw.get("venue")),
                "event_dates": list(raw.get("event_dates") or []),
                "query_families": [raw.get("query_family")] if raw.get("query_family") else [],
                "sources": [raw.get("source")],
                "source_records": [source_record],
            }
            merged.append(item)
            idx = len(merged) - 1
        else:
            item = merged[idx]
            if len(clean_text(raw.get("abstract"))) > len(item.get("abstract", "")):
                item["abstract"] = clean_text(raw.get("abstract"))
            item["authors"] = list(dict.fromkeys(item.get("authors", []) + [x for x in raw.get("authors", []) if x]))
            item["identifiers"].update({k: v for k, v in (raw.get("identifiers") or {}).items() if v})
            item["canonical_urls"] = list(dict.fromkeys(item.get("canonical_urls", []) + (raw.get("urls") or [])))
            item["event_dates"] = unique_dicts(item.get("event_dates", []) + (raw.get("event_dates") or []))
            item["sources"] = list(dict.fromkeys(item.get("sources", []) + [raw.get("source")]))
            if raw.get("query_family"):
                item["query_families"] = list(dict.fromkeys(item.get("query_families", []) + [raw["query_family"]]))
            item["source_records"].append(source_record)
        by_key[key] = idx
        ids = merged[idx].get("identifiers", {})
        if ids.get("doi"):
            by_key["doi:" + normalize_doi(ids["doi"])] = idx
        if ids.get("arxiv"):
            by_key["arxiv:" + normalize_arxiv(ids["arxiv"])] = idx
        title_key = normalize_title(merged[idx].get("canonical_title", ""))
        if title_key:
            by_key["title:" + title_key] = idx
            fuzzy_title_buckets[title_bucket(title_key)].add(idx)
        for url in merged[idx].get("canonical_urls", []):
            if clean_text(url):
                by_key["url:" + clean_text(url)] = idx
    for item in merged:
        normalize_primary_dates(item)
    return merged


def unique_dicts(items: list[dict[str, Any]]) -> list[dict[str, Any]]:
    seen, result = set(), []
    for item in items:
        key = json.dumps(item, sort_keys=True)
        if key not in seen:
            seen.add(key)
            result.append(item)
    return result


def normalize_primary_dates(item: dict[str, Any]) -> None:
    """Expose stable top-level dates without discarding event provenance."""
    events = item.get("event_dates") or []
    published = sorted({e.get("date") or iso_day(e.get("value", "")) for e in events if e.get("kind") == "published"})
    updated = sorted({e.get("date") or iso_day(e.get("value", "")) for e in events if e.get("kind") == "updated"})
    item["published_date"] = published[0] if published else ""
    item["updated_date"] = updated[-1] if updated else ""
    kinds = [e.get("kind") for e in events if e.get("kind")]
    item["event_type"] = "updated" if "updated" in kinds else ("published" if "published" in kinds else (kinds[0] if kinds else ""))


def local_score(item: dict[str, Any], hints_by_family: dict[str, list[str]]) -> tuple[int, list[str], list[str], list[str], bool]:
    text = normalize_title(item.get("canonical_title", "") + " " + item.get("abstract", ""))
    agents = matched_terms(text, AGENT_TERMS)
    graphics = matched_terms(text, GRAPHICS_TERMS)
    combined = any(contains_term(text, term) for term in STRONG_COMBINED_TERMS)
    negative = any(contains_term(text, term) for term in NEGATIVE_DOMAINS) and not combined
    score = min(6, len(agents) * 2) + min(8, len(graphics) * 2) + (5 if combined else 0) - (6 if negative else 0)
    hints = []
    for family in item.get("query_families", []):
        hints.extend(hints_by_family.get(family, []))
    adjacent_family_hit = bool(set(item.get("query_families", [])) & ADJACENT_QUERY_FAMILIES)
    # Adjacent component papers can omit graphics vocabulary in their title and
    # abstract. Retain them as leads when the discovery query itself came from a
    # controlled adjacent family and the text still contains an agent/system cue.
    keep = (bool(agents) and bool(graphics) and score >= 4) or combined or (adjacent_family_hit and bool(agents) and not negative)
    return score, agents, graphics, list(dict.fromkeys(hints)), keep


def event_day_in_timezone(value: str, timezone_name: str) -> str:
    if not value:
        return ""
    if "T" not in value:
        return iso_day(value)
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
        if parsed.tzinfo is None:
            return parsed.date().isoformat()
        return parsed.astimezone(ZoneInfo(timezone_name)).date().isoformat()
    except (ValueError, KeyError):
        return iso_day(value)


def same_day_qualifies(item: dict[str, Any], target_day: str, timezone_name: str = "America/Chicago") -> tuple[bool, list[dict[str, Any]]]:
    allowed = {"published", "updated"} if item.get("kind") == "paper" else {"created", "updated", "pushed"}
    evidence = []
    for candidate in item.get("event_dates", []):
        if candidate.get("precision") != "day" or candidate.get("kind") not in allowed:
            continue
        local_day = event_day_in_timezone(candidate.get("value", ""), timezone_name)
        if local_day == target_day:
            enriched = dict(candidate)
            enriched["local_date"] = local_day
            enriched["timezone"] = timezone_name
            evidence.append(enriched)
    return bool(evidence), evidence


def mark_known(item: dict[str, Any], paper_names: set[str], paper_ids: set[str], taxonomy_names: set[str], taxonomy_ids: set[str]) -> str:
    title = normalize_title(item.get("canonical_title", ""))
    arxiv_id = normalize_arxiv((item.get("identifiers") or {}).get("arxiv", ""))
    if title in paper_names or (arxiv_id and arxiv_id in paper_ids):
        return "known_discussed_paper"
    if title in taxonomy_names or (arxiv_id and arxiv_id in taxonomy_ids):
        return "known_taxonomy_method"
    return "new_relative_to_bundled_corpus"


def write_jsonl(path: Path, records: Iterable[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8") as handle:
        for item in records:
            handle.write(json.dumps(item, ensure_ascii=False, sort_keys=True) + "\n")


def write_json_atomic(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(
        json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    os.replace(temporary, path)


def estimate_request_plan(
    sources: list[str],
    families: list[dict[str, Any]],
    pages: int,
    include_artifacts: bool,
    direct_id_request: bool = False,
) -> dict[str, Any]:
    """Return a transparent upper bound before the live run starts."""
    query_count = sum(len(family.get("queries", [])) for family in families)
    by_source: dict[str, int] = {}
    for source in sources:
        if source == "huggingface":
            by_source[source] = pages
        elif source == "github" and not include_artifacts:
            by_source[source] = 0
        else:
            by_source[source] = query_count * pages
    direct = 1 if direct_id_request else 0
    return {
        "query_families": len(families),
        "query_variants": query_count,
        "pages_per_query": pages,
        "estimated_max_requests_by_source": by_source,
        "direct_id_requests": direct,
        "estimated_max_requests": sum(by_source.values()) + direct,
    }


def budget_exhaustion_reason(
    run_started: float,
    source_started: float,
    now: float,
    max_runtime_seconds: float,
    source_time_budget_seconds: float,
) -> str:
    if max_runtime_seconds > 0 and now - run_started >= max_runtime_seconds:
        return f"global runtime budget of {max_runtime_seconds:g}s exhausted"
    if source_time_budget_seconds > 0 and now - source_started >= source_time_budget_seconds:
        return f"source runtime budget of {source_time_budget_seconds:g}s exhausted"
    return ""


def write_progress(
    output_dir: Path,
    coverage: dict[str, Any],
    run_started: float,
    current_source: str,
    message: str,
) -> None:
    progress = {
        "mode": coverage.get("mode"),
        "profile": coverage.get("profile"),
        "target_day": coverage.get("target_day"),
        "timezone": coverage.get("timezone"),
        "in_progress": True,
        "current_source": current_source,
        "message": message,
        "elapsed_seconds": round(time.monotonic() - run_started, 3),
        "request_plan": coverage.get("request_plan", {}),
        "sources": coverage.get("sources", {}),
    }
    write_json_atomic(output_dir / "progress.json", progress)
    print(
        f"[same-day] {message}; elapsed={progress['elapsed_seconds']:.1f}s",
        file=sys.stderr,
        flush=True,
    )


def evaluate_same_day_coverage(
    source_ledger: dict[str, dict[str, Any]],
    requested_sources: list[str],
    fixture_used: bool,
) -> dict[str, Any]:
    """Prevent a failed collection from being reported as a valid empty run."""
    if fixture_used:
        return {
            "usable": True,
            "scripted_source_coverage_complete": False,
            "recommended_label": "offline same-day fixture validation; live source coverage not tested",
            "usable_sources": ["fixture"],
            "failed_sources": [],
            "blockers": ["offline fixture does not establish live source coverage"],
        }

    requested_paper_sources = [name for name in requested_sources if name != "github"]
    usable_sources = [
        name for name in requested_paper_sources
        if (source_ledger.get(name) or {}).get("status") in {"queried", "partial"}
    ]
    failed_sources = [
        name for name in requested_paper_sources
        if (source_ledger.get(name) or {}).get("status") in {"failed", "blocked"}
    ]
    missing_sources = [name for name in requested_paper_sources if name not in source_ledger]
    usable = bool(usable_sources)
    complete = bool(requested_paper_sources) and all(
        (source_ledger.get(name) or {}).get("status") == "queried"
        for name in requested_paper_sources
    )
    blockers = []
    if not usable:
        blockers.append("no requested scripted paper source succeeded")
    if failed_sources:
        blockers.append("failed sources: " + ", ".join(sorted(failed_sources)))
    if missing_sources:
        blockers.append("missing source ledger entries: " + ", ".join(sorted(missing_sources)))
    if complete:
        label = "same-day candidate search with complete scripted source coverage"
    elif usable:
        label = "partial same-day candidate search; scripted source coverage incomplete"
    else:
        label = "blocked same-day candidate search; no scripted paper source succeeded"
    return {
        "usable": usable,
        "scripted_source_coverage_complete": complete,
        "recommended_label": label,
        "usable_sources": sorted(usable_sources),
        "failed_sources": sorted(failed_sources),
        "blockers": blockers,
    }


def collect_live_records(
    args: argparse.Namespace,
    target_day: str,
    families: list[dict[str, Any]],
    sources: list[str],
    coverage: dict[str, Any],
    timeout: int,
    request_delay: float,
    max_runtime_seconds: float,
    source_time_budget_seconds: float,
    progress_every: int,
) -> tuple[list[dict[str, Any]], bool]:
    """Collect live records with visible progress and bounded source runtimes."""
    raw_records: list[dict[str, Any]] = []
    run_started = time.monotonic()
    stopped_early = False
    active_source = "initialization"
    active_source_index = -1

    def stop_status(status: dict[str, Any], reason: str) -> None:
        nonlocal stopped_early
        stopped_early = True
        status["errors"].append(reason)
        status["status"] = "partial" if status.get("records", 0) else "blocked"

    def remaining_blocked(start_index: int, reason: str) -> None:
        for remaining in sources[start_index:]:
            coverage["sources"].setdefault(remaining, {
                "status": "blocked",
                "pages_attempted": 0,
                "records": 0,
                "errors": [reason],
                "pagination_limit": coverage.get("max_pages", 0),
            })

    try:
        if args.must_include_id:
            active_source = "arxiv_direct_ids"
            status = coverage["sources"].setdefault(
                active_source,
                {"status": "queried", "pages_attempted": 0, "records": 0, "errors": []},
            )
            reason = budget_exhaustion_reason(
                run_started, run_started, time.monotonic(), max_runtime_seconds, 0,
            )
            if reason:
                stop_status(status, reason)
            else:
                status["pages_attempted"] = 1
                write_progress(args.output_dir, coverage, run_started, active_source, "fetching direct arXiv recall probes")
                try:
                    direct = fetch_arxiv_ids(
                        [normalize_arxiv(x) for x in args.must_include_id if normalize_arxiv(x)], timeout,
                    )
                    raw_records.extend(direct)
                    status["records"] = len(direct)
                except Exception as exc:
                    status["status"] = "failed"
                    status["errors"].append(f"{type(exc).__name__}: {exc}")

        for source_index, source in enumerate(sources):
            active_source_index = source_index
            active_source = source
            global_reason = budget_exhaustion_reason(
                run_started, run_started, time.monotonic(), max_runtime_seconds, 0,
            )
            if global_reason:
                stopped_early = True
                remaining_blocked(source_index, global_reason)
                write_progress(args.output_dir, coverage, run_started, source, global_reason)
                break

            source_started = time.monotonic()
            source_status = {
                "status": "queried",
                "pages_attempted": 0,
                "records": 0,
                "errors": [],
                "pagination_limit": coverage.get("max_pages", 0),
                "time_budget_seconds": source_time_budget_seconds,
            }
            coverage["sources"][source] = source_status
            write_progress(args.output_dir, coverage, run_started, source, f"starting source {source}")

            if source == "github" and not args.include_artifacts:
                source_status["status"] = "not_applicable"
                source_status["errors"].append(
                    "artifact collection disabled; use targeted repository follow-up or pass --include-artifacts",
                )
                write_progress(args.output_dir, coverage, run_started, source, "skipped optional GitHub artifact sweep")
                continue
            if source not in FETCHERS and source != "huggingface":
                source_status["status"] = "failed"
                source_status["errors"].append(f"unsupported source: {source}")
                write_progress(args.output_dir, coverage, run_started, source, f"failed unsupported source {source}")
                continue

            source_stopped = False
            global_stop = False

            def before_request() -> bool:
                nonlocal source_stopped, global_stop
                now = time.monotonic()
                reason = budget_exhaustion_reason(
                    run_started, source_started, now,
                    max_runtime_seconds, source_time_budget_seconds,
                )
                if reason:
                    stop_status(source_status, reason)
                    source_stopped = True
                    global_stop = reason.startswith("global")
                    return False
                source_status["pages_attempted"] += 1
                if progress_every > 0 and source_status["pages_attempted"] % progress_every == 0:
                    write_progress(
                        args.output_dir,
                        coverage,
                        run_started,
                        source,
                        f"source {source}: {source_status['pages_attempted']} requests attempted, {source_status['records']} records",
                    )
                return True

            try:
                if source == "huggingface":
                    for page in range(coverage.get("max_pages", 0)):
                        if not before_request():
                            break
                        batch = fetch_huggingface_daily(timeout, target_day, page, coverage.get("per_page", 0))
                        raw_records.extend(batch)
                        source_status["records"] += len(batch)
                        if len(batch) < coverage.get("per_page", 0):
                            break
                        if request_delay:
                            time.sleep(request_delay)
                else:
                    for family in families:
                        if source_stopped:
                            break
                        for query in family.get("queries", []):
                            if source_stopped:
                                break
                            for page in range(coverage.get("max_pages", 0)):
                                if not before_request():
                                    break
                                kwargs: dict[str, Any] = {}
                                if source in {"arxiv", "openalex", "crossref", "semantic_scholar", "github"}:
                                    kwargs["target_day"] = target_day
                                try:
                                    batch = FETCHERS[source](
                                        query, family["id"], page,
                                        coverage.get("per_page", 0), timeout, **kwargs,
                                    )
                                    raw_records.extend(batch)
                                    source_status["records"] += len(batch)
                                    if len(batch) < coverage.get("per_page", 0):
                                        break
                                except (
                                    urllib.error.HTTPError,
                                    urllib.error.URLError,
                                    TimeoutError,
                                    ET.ParseError,
                                    json.JSONDecodeError,
                                ) as exc:
                                    http_code = exc.code if isinstance(exc, urllib.error.HTTPError) else None
                                    source_status["errors"].append(
                                        f"{family['id']} page {page + 1}: {type(exc).__name__}: {exc}",
                                    )
                                    if isinstance(exc, urllib.error.HTTPError):
                                        exc.close()
                                    # Authentication and rate-limit failures are source-wide;
                                    # repeating them for every taxonomy query caused the observed
                                    # unbounded-looking run.
                                    if http_code in {401, 403, 429}:
                                        source_status["errors"].append(
                                            f"source stopped after HTTP {http_code} to avoid repeated failing requests",
                                        )
                                        source_stopped = True
                                        break
                                if request_delay:
                                    time.sleep(request_delay)
            except Exception as exc:
                source_status["errors"].append(f"{type(exc).__name__}: {exc}")

            if source_status["errors"] and source_status["status"] == "queried":
                source_status["status"] = "partial" if source_status["records"] else "failed"
            source_status["elapsed_seconds"] = round(time.monotonic() - source_started, 3)
            write_progress(
                args.output_dir,
                coverage,
                run_started,
                source,
                f"finished source {source} with status {source_status['status']} and {source_status['records']} records",
            )
            if global_stop:
                remaining_blocked(source_index + 1, source_status["errors"][-1])
                break
    except KeyboardInterrupt:
        stopped_early = True
        status = coverage["sources"].setdefault(
            active_source,
            {"status": "blocked", "pages_attempted": 0, "records": 0, "errors": []},
        )
        status["status"] = "partial" if status.get("records", 0) else "blocked"
        status.setdefault("errors", []).append("collection interrupted; partial evidence preserved")
        remaining_blocked(active_source_index + 1, "not attempted because collection was interrupted")
        write_progress(args.output_dir, coverage, run_started, active_source, "collection interrupted; finalizing partial outputs")

    coverage["collection_elapsed_seconds"] = round(time.monotonic() - run_started, 3)
    return raw_records, stopped_early


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", choices=["same_day"], required=True, help="Historical work must use historical_sweep.py")
    parser.add_argument("--profile", choices=sorted(PROFILES), default="daily")
    parser.add_argument("--taxonomy", type=Path, required=True)
    parser.add_argument("--paper-list", type=Path, required=True)
    parser.add_argument("--queries", type=Path, default=Path(__file__).resolve().parents[1] / "references" / "search-query-families.json")
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--date", help="Target date for same_day mode (YYYY-MM-DD); defaults to America/Chicago today")
    parser.add_argument("--timezone", default="America/Chicago")
    parser.add_argument("--sources", help="Comma-separated source names")
    parser.add_argument("--families", help="Comma-separated query-family IDs")
    parser.add_argument("--max-pages", type=int)
    parser.add_argument("--per-page", type=int)
    parser.add_argument("--timeout", type=int, help="Per-request timeout; defaults to the selected profile")
    parser.add_argument("--request-delay", type=float, help="Delay between requests; defaults to the selected profile")
    parser.add_argument("--source-time-budget-seconds", type=float, help="Bound each source; 0 disables the bound")
    parser.add_argument("--max-runtime-seconds", type=float, help="Bound the full live collection; 0 disables the bound")
    parser.add_argument("--progress-every", type=int, default=10, help="Write progress after this many source requests; 0 disables periodic updates")
    parser.add_argument("--include-artifacts", action="store_true")
    parser.add_argument("--must-include-id", action="append", default=[], help="Expected arXiv ID; fetched directly and used as a recall gate")
    parser.add_argument("--fixture", type=Path, help="Offline JSONL source records; skips network")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    for required in (args.taxonomy, args.paper_list, args.queries):
        if not required.is_file():
            print(f"Missing required file: {required}", file=sys.stderr)
            return 2
    try:
        target_day = args.date or datetime.now(ZoneInfo(args.timezone)).date().isoformat()
        date.fromisoformat(target_day)
    except Exception as exc:
        print(f"Invalid date/timezone: {exc}", file=sys.stderr)
        return 2

    profile = dict(PROFILES[args.profile])
    pages = args.max_pages if args.max_pages is not None else profile["pages"]
    per_page = args.per_page if args.per_page is not None else profile["per_page"]
    timeout = args.timeout if args.timeout is not None else profile["timeout"]
    request_delay = args.request_delay if args.request_delay is not None else profile["request_delay"]
    source_time_budget_seconds = (
        args.source_time_budget_seconds
        if args.source_time_budget_seconds is not None
        else profile["source_time_budget_seconds"]
    )
    max_runtime_seconds = (
        args.max_runtime_seconds
        if args.max_runtime_seconds is not None
        else profile["max_runtime_seconds"]
    )
    if (
        pages < 1 or per_page < 1 or timeout < 1 or request_delay < 0
        or source_time_budget_seconds < 0 or max_runtime_seconds < 0
        or args.progress_every < 0
    ):
        print("Invalid pagination, timeout, delay, runtime-budget, or progress setting", file=sys.stderr)
        return 2
    sources = [x.strip() for x in args.sources.split(",")] if args.sources else list(profile["sources"])
    selected_families = {x.strip() for x in args.families.split(",")} if args.families else set()
    families = read_query_families(args.queries, profile["family_limit"], profile["variants"], selected_families)
    hints_by_family = {f["id"]: f.get("taxonomy_hints", []) for f in families}
    args.output_dir.mkdir(parents=True, exist_ok=True)
    request_plan = estimate_request_plan(
        sources, families, pages, args.include_artifacts, bool(args.must_include_id),
    )

    started = datetime.now(timezone.utc).isoformat()
    coverage: dict[str, Any] = {
        "mode": args.mode, "profile": args.profile, "target_day": target_day if args.mode == "same_day" else None,
        "timezone": args.timezone, "started_at_utc": started, "query_family_count": len(families),
        "query_count": sum(len(f.get("queries", [])) for f in families), "requested_sources": sources,
        "max_pages": pages, "per_page": per_page, "sources": {},
        "request_plan": request_plan,
        "runtime_limits": {
            "request_timeout_seconds": timeout,
            "request_delay_seconds": request_delay,
            "source_time_budget_seconds": source_time_budget_seconds,
            "max_runtime_seconds": max_runtime_seconds,
        },
        "manual_follow_up_required": ["OpenReview", "official venue archives", "Hugging Face paper pages", "project/author/lab pages", "official artifact pages"],
    }
    raw_records: list[dict[str, Any]] = []
    collection_stopped_early = False

    print(
        f"[same-day] profile={args.profile}; sources={len(sources)}; "
        f"query_families={len(families)}; planned_max_requests={request_plan['estimated_max_requests']}; "
        f"max_runtime={max_runtime_seconds:g}s",
        file=sys.stderr,
        flush=True,
    )

    if args.fixture:
        with args.fixture.open(encoding="utf-8") as handle:
            raw_records = [json.loads(line) for line in handle if line.strip()]
        coverage["sources"]["fixture"] = {"status": "queried", "pages_attempted": 1, "records": len(raw_records), "errors": []}
        write_progress(args.output_dir, coverage, time.monotonic(), "fixture", "loaded offline fixture")
    else:
        raw_records, collection_stopped_early = collect_live_records(
            args=args,
            target_day=target_day,
            families=families,
            sources=sources,
            coverage=coverage,
            timeout=timeout,
            request_delay=request_delay,
            max_runtime_seconds=max_runtime_seconds,
            source_time_budget_seconds=source_time_budget_seconds,
            progress_every=args.progress_every,
        )

    merged = merge_records(raw_records)
    paper_names, paper_ids = extract_known(args.paper_list)
    taxonomy_names, taxonomy_ids = extract_known(args.taxonomy)
    candidates = []
    for item in merged:
        score, agents, graphics, hints, keep = local_score(item, hints_by_family)
        item["prefilter_score"] = score
        item["matched_agent_terms"] = agents
        item["matched_graphics_terms"] = graphics
        item["taxonomy_hints"] = hints
        item["known_corpus_status"] = mark_known(item, paper_names, paper_ids, taxonomy_names, taxonomy_ids)
        item["screening_status"] = "not_screened"
        item["confidence"] = "lead"
        if args.mode == "same_day":
            qualifies, evidence = same_day_qualifies(item, target_day, args.timezone)
            item["same_day_qualified"] = qualifies
            item["same_day_evidence"] = evidence
            keep = keep and qualifies
        if item.get("kind") == "artifact" and not args.include_artifacts:
            keep = False
        if keep:
            candidates.append(item)

    raw_merged = sorted(merged, key=lambda x: normalize_title(x.get("canonical_title", "")))
    candidates.sort(key=lambda x: (-x.get("prefilter_score", 0), normalize_title(x.get("canonical_title", ""))))
    coverage["finished_at_utc"] = datetime.now(timezone.utc).isoformat()
    coverage["collection_stopped_early"] = collection_stopped_early
    coverage["raw_source_records"] = len(raw_records)
    coverage["deduplicated_records"] = len(raw_merged)
    coverage["candidate_records"] = len(candidates)
    coverage["candidate_sources"] = dict(Counter(source for item in candidates for source in item.get("sources", [])))
    coverage["candidate_query_families"] = dict(Counter(family for item in candidates for family in item.get("query_families", [])))
    coverage["known_status_counts"] = dict(Counter(item.get("known_corpus_status") for item in candidates))

    gate = {"expected_ids": [], "passed": True}
    for value in args.must_include_id:
        expected = normalize_arxiv(value)
        in_raw = any(normalize_arxiv((x.get("identifiers") or {}).get("arxiv", "")) == expected for x in raw_merged)
        in_candidates = any(normalize_arxiv((x.get("identifiers") or {}).get("arxiv", "")) == expected for x in candidates)
        gate["expected_ids"].append({"arxiv": expected, "in_raw": in_raw, "in_candidates": in_candidates})
        gate["passed"] = gate["passed"] and in_raw and in_candidates
    coverage["recall_gate"] = gate
    coverage["same_day_coverage_gate"] = evaluate_same_day_coverage(
        coverage["sources"], sources, bool(args.fixture)
    )

    write_jsonl(args.output_dir / "raw_records.jsonl", raw_merged)
    write_jsonl(args.output_dir / "candidates.jsonl", candidates)
    write_json_atomic(args.output_dir / "coverage.json", coverage)
    source_lines = [f"- {name}: {info['status']}; {info.get('records', 0)} records; {info.get('pages_attempted', 0)} requests/pages; {len(info.get('errors', []))} errors" for name, info in coverage["sources"].items()]
    frame = f"Exact target date: {target_day} ({args.timezone})" if args.mode == "same_day" else "Historical range: no cutoff"
    same_day_gate = coverage["same_day_coverage_gate"]
    report = "\n".join([
        "# Agentic Graphics Discovery Run", "", f"- Mode: `{args.mode}`", f"- Profile: `{args.profile}`",
        f"- {frame}", f"- Query families: {len(families)}", f"- Deduplicated raw records: {len(raw_merged)}",
        f"- Locally retained candidates: {len(candidates)}",
        f"- Planned request upper bound: {request_plan['estimated_max_requests']}",
        f"- Collection stopped early: `{str(collection_stopped_early).lower()}`",
        f"- Coverage label: `{same_day_gate['recommended_label']}`",
        f"- Coverage usable: `{str(same_day_gate['usable']).lower()}`",
        "", "## Structured source coverage", "", *source_lines,
        "", "## Required follow-up", "", "Use primary paper pages, Hugging Face Papers, OpenReview, official venue archives, and project/author pages to verify retained leads and fill non-API coverage.",
        "", "The local score is a high-recall prefilter, not a survey-inclusion decision.",
    ]) + "\n"
    (args.output_dir / "report.md").write_text(report, encoding="utf-8")
    write_json_atomic(args.output_dir / "progress.json", {
        "mode": args.mode,
        "profile": args.profile,
        "target_day": target_day,
        "timezone": args.timezone,
        "in_progress": False,
        "message": "collection finalized; inspect coverage.json before interpreting candidates",
        "collection_stopped_early": collection_stopped_early,
        "request_plan": request_plan,
        "sources": coverage["sources"],
        "finished_at_utc": coverage["finished_at_utc"],
    })
    print(json.dumps({
        "output_dir": str(args.output_dir),
        "raw": len(raw_merged),
        "candidates": len(candidates),
        "collection_stopped_early": collection_stopped_early,
        "request_plan": request_plan,
        "recall_gate": gate,
        "same_day_coverage_gate": same_day_gate,
    }, indent=2))
    complete_live_run = bool(args.fixture) or same_day_gate["scripted_source_coverage_complete"]
    return 0 if gate["passed"] and same_day_gate["usable"] and complete_live_run and not collection_stopped_early else 3


if __name__ == "__main__":
    raise SystemExit(main())
