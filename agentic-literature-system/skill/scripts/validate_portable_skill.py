#!/usr/bin/env python3
"""Validate the self-contained Agentic Graphics skill without third-party packages."""

from __future__ import annotations

import argparse
import ast
import json
import re
import sys
from pathlib import Path
from typing import Any


REQUIRED_FILES = [
    "SKILL.md",
    "README.md",
    "agents/openai.yaml",
    "references/METHOD_TAXONOMY_TABLE.md",
    "references/PAPER_READING_LIST.md",
    "references/source-registry.md",
    "references/data-sources.md",
    "references/historical-output-contract.md",
    "references/search-query-families.json",
    "references/screening-rubric.md",
    "references/screening-record.schema.json",
    "references/curation-rules.md",
    "references/curation-record.schema.json",
    "references/research-intelligence.md",
    "references/portability.md",
    "references/taxonomy-codebook.json",
    "references/paper-corpus.json",
    "references/source-manifest.json",
    "references/daily-workflow.md",
    "scripts/daily_report.py",
    "scripts/test_daily_report.py",
    "scripts/discover_papers.py",
    "scripts/historical_sweep.py",
    "scripts/audit_historical_run.py",
    "scripts/test_discover_papers.py",
    "scripts/test_historical_sweep.py",
    "scripts/validate_portable_skill.py",
]

PIPELINE_FIELDS = {
    "canonical_title",
    "authors",
    "identifiers",
    "canonical_urls",
    "source_records",
    "published_date",
    "updated_date",
    "event_type",
    "abstract",
    "known_corpus_status",
    "triage_status",
    "screening_status",
    "screening_reason",
    "screening_evidence",
    "extracted_system_evidence",
    "confidence",
}

CURATION_FIELDS = PIPELINE_FIELDS | {
    "taxonomy_cells",
    "field_evidence",
    "outside_current_taxonomy",
    "taxonomy_delta",
}




def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--skill-dir",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Directory containing SKILL.md; defaults to this script's parent skill",
    )
    return parser.parse_args()


def add_check(checks: list[dict[str, Any]], name: str, passed: bool, detail: Any) -> None:
    checks.append({"name": name, "passed": bool(passed), "detail": detail})


def load_json(path: Path, checks: list[dict[str, Any]]) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
        add_check(checks, f"json:{path.name}", isinstance(value, dict), "parsed")
        return value if isinstance(value, dict) else {}
    except Exception as exc:
        add_check(checks, f"json:{path.name}", False, f"{type(exc).__name__}: {exc}")
        return {}


def check_frontmatter(skill_dir: Path, checks: list[dict[str, Any]]) -> None:
    path = skill_dir / "SKILL.md"
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n", text, flags=re.DOTALL)
    if not match:
        add_check(checks, "frontmatter", False, "missing YAML frontmatter block")
        return
    fields = {}
    for line in match.group(1).splitlines():
        key, separator, value = line.partition(":")
        if separator:
            fields[key.strip()] = value.strip()
    name = fields.get("name", "")
    description = fields.get("description", "")
    passed = (
        (name == skill_dir.name or (skill_dir.name == "skill" and name == "agentic-graphics-research"))
        and bool(re.fullmatch(r"[a-z0-9-]{1,63}", name))
        and bool(description)
    )
    add_check(
        checks,
        "frontmatter",
        passed,
        {"name": name, "folder": skill_dir.name, "description_present": bool(description)},
    )


def check_markdown_links(skill_dir: Path, checks: list[dict[str, Any]]) -> None:
    missing = []
    checked = 0
    for path in sorted(skill_dir.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
            if "://" in target or target.startswith(("#", "mailto:")):
                continue
            clean_target = target.split("#", 1)[0]
            if not clean_target:
                continue
            checked += 1
            resolved = (path.parent / clean_target).resolve()
            if not resolved.exists():
                missing.append({"from": str(path.relative_to(skill_dir)), "target": target})
    add_check(checks, "relative_markdown_links", not missing, {"checked": checked, "missing": missing})


def check_machine_paths(skill_dir: Path, checks: list[dict[str, Any]]) -> None:
    forbidden = [
        chr(47) + "Users" + chr(47),
        chr(47) + "home" + chr(47),
        ".codex" + chr(47) + "skills",
        "C:" + chr(92) + "Users" + chr(92),
    ]
    hits = []
    for path in sorted(skill_dir.rglob("*")):
        if not path.is_file() or "__pycache__" in path.parts or path.suffix == ".pyc":
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for line_number, line in enumerate(text.splitlines(), 1):
            if any(value in line for value in forbidden):
                hits.append({"file": str(path.relative_to(skill_dir)), "line": line_number})
    add_check(checks, "machine_specific_paths", not hits, hits)


def check_python(skill_dir: Path, checks: list[dict[str, Any]]) -> None:
    failures = []
    parsed = 0
    imported_modules = set()
    for path in sorted((skill_dir / "scripts").glob("*.py")):
        try:
            tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
            parsed += 1
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    imported_modules.update(alias.name.split(".", 1)[0] for alias in node.names)
                elif isinstance(node, ast.ImportFrom) and node.module:
                    imported_modules.add(node.module.split(".", 1)[0])
        except SyntaxError as exc:
            failures.append({"file": path.name, "line": exc.lineno, "message": exc.msg})
    allowed = set(sys.stdlib_module_names) | {"discover_papers", "daily_report"}
    nonstandard = sorted(imported_modules - allowed)
    add_check(
        checks,
        "python_scripts",
        not failures and not nonstandard,
        {"parsed": parsed, "syntax_failures": failures, "nonstandard_imports": nonstandard},
    )


def check_sources(skill_dir, checks):
    ref = skill_dir / "references"
    codebook = load_json(ref / "taxonomy-codebook.json", checks)
    corpus = load_json(ref / "paper-corpus.json", checks)
    manifest = load_json(ref / "source-manifest.json", checks)
    add_check(checks, "taxonomy_snapshot", bool(codebook.get("fields")) and codebook.get("source") == manifest, {"version": codebook.get("version"), "fields": len(codebook.get("fields", {}))})
    records = corpus.get("records", [])
    add_check(checks, "paper_corpus", bool(records) and len(records) == manifest.get("paper_occurrences") and all(r.get("title") and r.get("urls") for r in records), {"occurrences": len(records)})


def check_schemas(skill_dir: Path, checks: list[dict[str, Any]]) -> None:
    screening = load_json(skill_dir / "references/screening-record.schema.json", checks)
    curation = load_json(skill_dir / "references/curation-record.schema.json", checks)
    query_families = load_json(skill_dir / "references/search-query-families.json", checks)

    screening_required = set(screening.get("required", []))
    curation_required = set(curation.get("required", []))
    triage_values = set(
        screening.get("properties", {}).get("triage_status", {}).get("enum", [])
    )
    taxonomy_cells = curation.get("properties", {}).get("taxonomy_cells", {})
    taxonomy_properties = set(taxonomy_cells.get("properties", {}))
    taxonomy_required = set(taxonomy_cells.get("required", []))
    families = query_families.get("families", [])
    codebook = json.loads((skill_dir / "references/taxonomy-codebook.json").read_text())
    add_check(checks, "codebook_schema_alignment", taxonomy_required == set(codebook["fields"]) and all(set(taxonomy_cells["properties"][k]["items"]["enum"]) == set(v + codebook["sentinels"]) for k, v in codebook["fields"].items()), "Exact fields and labels must match")

    add_check(
        checks,
        "screening_handoff_contract",
        PIPELINE_FIELDS.issubset(screening_required) and "needs_full_read" in triage_values,
        {
            "missing_required_fields": sorted(PIPELINE_FIELDS - screening_required),
            "needs_full_read_allowed": "needs_full_read" in triage_values,
        },
    )
    add_check(
        checks,
        "curation_handoff_contract",
        CURATION_FIELDS.issubset(curation_required) and taxonomy_properties == taxonomy_required,
        {
            "missing_required_fields": sorted(CURATION_FIELDS - curation_required),
            "optional_taxonomy_cells": sorted(taxonomy_properties - taxonomy_required),
        },
    )
    add_check(
        checks,
        "query_families",
        bool(families)
        and len({item.get("id") for item in families}) == len(families)
        and all(item.get("queries") for item in families),
        {"families": len(families)},
    )


def main() -> int:
    args = parse_args()
    skill_dir = args.skill_dir.expanduser().resolve()
    checks: list[dict[str, Any]] = []
    missing = [value for value in REQUIRED_FILES if not (skill_dir / value).is_file()]
    add_check(checks, "required_files", not missing, {"required": len(REQUIRED_FILES), "missing": missing})

    if not missing:
        check_frontmatter(skill_dir, checks)
        check_markdown_links(skill_dir, checks)
        check_machine_paths(skill_dir, checks)
        check_python(skill_dir, checks)
        check_sources(skill_dir, checks)
        check_schemas(skill_dir, checks)

    passed = all(check["passed"] for check in checks)
    print(json.dumps({"skill_dir": str(skill_dir), "passed": passed, "checks": checks}, indent=2))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
