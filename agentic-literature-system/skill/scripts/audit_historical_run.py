#!/usr/bin/env python3
"""Independently audit an Agentic Graphics historical discovery run."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any


REQUIRED_FILES = [
    "enumerated_raw.jsonl",
    "query_raw.jsonl",
    "candidates.jsonl",
    "low_confidence_records.jsonl",
    "coverage.json",
    "state.json",
    "slice_manifest.jsonl",
    "run_manifest.json",
    "progress.json",
    "report.md",
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def jsonl_count(path: Path) -> int:
    count = 0
    with path.open(encoding="utf-8") as handle:
        for number, line in enumerate(handle, 1):
            if not line.strip():
                continue
            try:
                json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"{path.name}:{number}: invalid JSON: {exc}") from exc
            count += 1
    return count


def check(condition: bool, message: str, failures: list[str]) -> None:
    if not condition:
        failures.append(message)


def audit(output_dir: Path) -> dict[str, Any]:
    failures: list[str] = []
    missing = [name for name in REQUIRED_FILES if not (output_dir / name).is_file()]
    if missing:
        failures.append("missing required files: " + ", ".join(missing))
        return {"artifact_contract_passed": False, "failures": failures, "output_dir": str(output_dir)}

    try:
        coverage = read_json(output_dir / "coverage.json")
        state = read_json(output_dir / "state.json")
        run_manifest = read_json(output_dir / "run_manifest.json")
        progress = read_json(output_dir / "progress.json")
        counts = {
            "enumerated_raw": jsonl_count(output_dir / "enumerated_raw.jsonl"),
            "query_raw": jsonl_count(output_dir / "query_raw.jsonl"),
            "candidates": jsonl_count(output_dir / "candidates.jsonl"),
            "low_confidence_records": jsonl_count(output_dir / "low_confidence_records.jsonl"),
            "slice_manifest": jsonl_count(output_dir / "slice_manifest.jsonl"),
        }
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        failures.append(str(exc))
        return {"artifact_contract_passed": False, "failures": failures, "output_dir": str(output_dir)}

    records = coverage.get("records", {})
    check(counts["enumerated_raw"] == records.get("enumerated_raw"), "enumerated_raw count differs from coverage.json", failures)
    check(counts["query_raw"] == records.get("query_raw"), "query_raw count differs from coverage.json", failures)
    check(counts["candidates"] == records.get("candidates"), "candidate count differs from coverage.json", failures)
    check(counts["low_confidence_records"] == records.get("low_confidence_retained"), "low-confidence count differs from coverage.json", failures)
    check(run_manifest.get("schema_version") == coverage.get("run_schema_version"), "run schema versions disagree", failures)
    check(state.get("schema_version") == 2, "unexpected checkpoint schema version", failures)
    check(state.get("config_fingerprint") == run_manifest.get("configuration_fingerprint"), "checkpoint and run-manifest fingerprints disagree", failures)
    check(run_manifest.get("execution_kind") == coverage.get("execution_kind"), "execution kinds disagree", failures)
    check(run_manifest.get("recommended_label") == coverage.get("recommended_label"), "recommended labels disagree", failures)
    check(coverage.get("automated_coverage_gate") == coverage.get("comprehensive_wording_gate"), "legacy automated gate is not an exact alias of comprehensive wording gate", failures)
    foreground = coverage.get("foreground_batch", {})
    check(progress.get("mode") == "historical", "progress.json has the wrong mode", failures)
    check(progress.get("in_progress") is False, "progress.json still marks a finalized artifact set as running", failures)
    check(progress.get("resume_required") == foreground.get("resume_required"), "progress and coverage disagree about resume status", failures)
    check(run_manifest.get("resume_required") == foreground.get("resume_required"), "run manifest and coverage disagree about resume status", failures)
    check(progress.get("recommended_label") == coverage.get("recommended_label"), "progress and coverage disagree about the report label", failures)

    execution_kind = coverage.get("execution_kind")
    enumeration = coverage.get("enumeration_lane", {})
    if execution_kind == "live":
        check(counts["slice_manifest"] == enumeration.get("completed_slices"), "slice manifest count differs from live enumeration coverage", failures)
        for slice_id, metadata in state.get("completed_slices", {}).items():
            path = output_dir / "enumeration_slices" / f"{slice_id}.jsonl"
            check(path.is_file(), f"missing completed slice file: {slice_id}", failures)
            if path.is_file():
                try:
                    check(jsonl_count(path) == metadata.get("records"), f"slice record count mismatch: {slice_id}", failures)
                    check(sha256(path) == metadata.get("sha256"), f"slice hash mismatch: {slice_id}", failures)
                except (OSError, ValueError) as exc:
                    failures.append(str(exc))

    integrity_gate = coverage.get("collection_integrity_gate", {})
    comprehensive_gate = coverage.get("comprehensive_wording_gate", {})
    if integrity_gate.get("passed"):
        check(not list((output_dir / "enumeration_slices").glob("*.partial.jsonl")), "integrity gate passed with partial enumeration checkpoints", failures)
        check(not list((output_dir / "query_batches").glob("*.partial.jsonl")), "integrity gate passed with partial query checkpoints", failures)
        check(enumeration.get("date_coverage", {}).get("exact") is True, "integrity gate passed without exact date coverage", failures)
        check(coverage.get("query_augmentation_lane", {}).get("status") == "complete", "integrity gate passed without complete query augmentation", failures)
        check(coverage.get("recall_gate", {}).get("passed") is True, "integrity gate passed with failed recall gate", failures)
        check(execution_kind == "live", "integrity gate passed for fixture execution", failures)
    if comprehensive_gate.get("passed"):
        check(integrity_gate.get("passed") is True, "comprehensive wording gate passed without integrity gate", failures)
        check(not coverage.get("full_scope_blockers"), "comprehensive wording gate passed with scope blockers", failures)
        check(coverage.get("recommended_label") == "best-effort comprehensive automated historical sweep", "comprehensive gate passed with wrong report label", failures)

    report = (output_dir / "report.md").read_text(encoding="utf-8")
    check(coverage.get("recommended_label", "") in report, "report.md omits the machine-selected report label", failures)
    result = {
        "artifact_contract_passed": not failures,
        "collection_integrity_gate_passed": bool(integrity_gate.get("passed")),
        "comprehensive_wording_gate_passed": bool(comprehensive_gate.get("passed")),
        "counts": counts,
        "failures": failures,
        "output_dir": str(output_dir),
        "audited_files": REQUIRED_FILES,
    }
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--no-write", action="store_true")
    args = parser.parse_args()
    result = audit(args.output_dir)
    if not args.no_write:
        (args.output_dir / "audit.json").write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if result["artifact_contract_passed"] else 4


if __name__ == "__main__":
    raise SystemExit(main())
