#!/usr/bin/env python3
"""Offline contract tests for historical_sweep.py."""

from __future__ import annotations

import json
import importlib.util
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest import mock


SCRIPT = Path(__file__).with_name("historical_sweep.py")
SPEC = importlib.util.spec_from_file_location("historical_sweep", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)


def raw_record(source, title, arxiv_id, abstract, family):
    return {
        "kind": "paper",
        "source": source,
        "title": title,
        "authors": ["A. Researcher"],
        "abstract": abstract,
        "identifiers": {"arxiv": arxiv_id} if arxiv_id else {},
        "urls": [f"https://arxiv.org/abs/{arxiv_id}"] if arxiv_id else [],
        "venue": "arXiv" if source == "arxiv" else "",
        "event_dates": [{"kind": "published", "value": "2026-06-11T10:00:00Z", "date": "2026-06-11", "source": source, "precision": "day"}],
        "query_family": family,
        "query": "fixture",
    }


class HistoricalSweepTests(unittest.TestCase):
    def test_interactive_defaults_are_bounded_and_responsive(self):
        argv = [
            "historical_sweep.py",
            "--taxonomy", "taxonomy.md",
            "--paper-list", "papers.md",
            "--output-dir", "output",
        ]
        with mock.patch.object(sys, "argv", argv):
            args = MODULE.parse_args()
        self.assertEqual(args.max_runtime_seconds, 60.0)
        self.assertEqual(args.timeout, 10)
        self.assertEqual(args.max_attempts, 2)
        self.assertEqual(args.retry_base_delay, 1.0)
        self.assertEqual(args.retry_max_delay, 6.0)
        self.assertEqual(args.progress_every_pages, 1)

    def test_arxiv_fallbacks_share_one_logical_page_timeout(self):
        calls = []

        def stalled(url, timeout):
            calls.append((url, timeout))
            raise TimeoutError("stalled endpoint")

        with mock.patch.object(MODULE.discovery, "get_text", side_effect=stalled):
            with self.assertRaises(TimeoutError):
                MODULE.fetch_arxiv_page("cat:cs.GR", "window", 0, 10, 10)
        self.assertEqual(len(calls), 2)
        self.assertEqual([timeout for _, timeout in calls], [5, 5])

    def test_newest_first_slice_order_changes_priority_not_scope(self):
        start = MODULE.parse_day("2026-01-01")
        end = MODULE.parse_day("2026-01-11")
        oldest = MODULE.initial_slices(start, end, 3, "oldest_first")
        newest = MODULE.initial_slices(start, end, 3, "newest_first")
        self.assertEqual(newest, list(reversed(oldest)))
        self.assertEqual(set(newest), set(oldest))
        self.assertEqual(newest[0][1], end)

    def test_implicit_end_date_is_frozen_to_existing_checkpoint(self):
        with tempfile.TemporaryDirectory() as temp:
            output = Path(temp)
            (output / "run_manifest.json").write_text(json.dumps({
                "date_range": {"until_inclusive": "2026-08-31"},
            }), encoding="utf-8")
            args = SimpleNamespace(output_dir=output, until_date=None, timezone="America/Chicago")
            value, origin = MODULE.resolve_until_date(args)
            self.assertEqual(value, "2026-08-31")
            self.assertEqual(origin, "existing_checkpoint")
            args.until_date = "2026-07-01"
            value, origin = MODULE.resolve_until_date(args)
            self.assertEqual(value, "2026-07-01")
            self.assertEqual(origin, "explicit")

    def test_retry_helper_stops_after_success(self):
        calls = []
        sleeps = []
        def operation():
            calls.append(1)
            if len(calls) < 3:
                raise TimeoutError("temporary")
            return "ok"
        value, metadata = MODULE.call_with_retry(operation, 4, 2.0, 10.0, sleeper=sleeps.append)
        self.assertEqual(value, "ok")
        self.assertEqual(metadata["attempts"], 3)
        self.assertEqual(sleeps, [2.0, 4.0])

    def test_retry_helper_does_not_start_request_after_deadline(self):
        calls = []
        with self.assertRaises(MODULE.RunBudgetExhausted):
            MODULE.call_with_retry(
                lambda: calls.append(1),
                4,
                2.0,
                10.0,
                deadline=MODULE.time.monotonic() - 1,
            )
        self.assertEqual(calls, [])

    def test_date_coverage_detects_gaps_and_overlaps(self):
        gap = MODULE.assess_date_coverage([
            {"start": "2026-01-01", "end_inclusive": "2026-01-03"},
            {"start": "2026-01-05", "end_inclusive": "2026-01-10"},
        ], MODULE.parse_day("2026-01-01"), MODULE.parse_day("2026-01-10"))
        self.assertFalse(gap["exact"])
        self.assertEqual(gap["gap_ranges"][0]["from"], "2026-01-04")
        overlap = MODULE.assess_date_coverage([
            {"start": "2026-01-01", "end_inclusive": "2026-01-06"},
            {"start": "2026-01-06", "end_inclusive": "2026-01-10"},
        ], MODULE.parse_day("2026-01-01"), MODULE.parse_day("2026-01-10"))
        self.assertFalse(overlap["exact"])
        self.assertEqual(overlap["overlap_days"], 1)

    def test_query_page_cap_is_reported_as_truncation(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            queries = root / "queries.json"
            queries.write_text(json.dumps({"families": [{"id": "one", "queries": ["q"], "taxonomy_hints": []}]}), encoding="utf-8")
            args = SimpleNamespace(
                output_dir=root / "out", queries=queries, query_variants=0,
                query_pages=2, query_per_page=2, timeout=1, query_delay=0,
                max_attempts=1, retry_base_delay=0, retry_max_delay=0,
            )
            args.output_dir.mkdir()
            state = {"completed_query_batches": {}, "failed_query_batches": {}}
            state_path = args.output_dir / "state.json"
            old = MODULE.discovery.FETCHERS["openalex"]
            def fake_fetch(query, family, page, per_page, timeout):
                return [raw_record("openalex", f"Graphics Agent {page}-{i}", f"260{page}.{i:05d}", "An agent edits a 3D scene.", family) for i in range(per_page)]
            MODULE.discovery.FETCHERS["openalex"] = fake_fetch
            try:
                records, summary = MODULE.collect_query_lane(args, ["openalex"], state, state_path)
            finally:
                MODULE.discovery.FETCHERS["openalex"] = old
            self.assertEqual(len(records), 4)
            self.assertEqual(summary["status"], "partial")
            self.assertEqual(summary["truncated_batches"], 1)
            self.assertEqual(summary["sources"]["openalex"]["status"], "partial")

    def test_query_batch_finalizes_at_page_cap_without_sleeping_past_budget(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            queries = root / "queries.json"
            queries.write_text(json.dumps({"families": [{"id": "one", "queries": ["q"], "taxonomy_hints": []}]}), encoding="utf-8")
            args = SimpleNamespace(
                output_dir=root / "out", queries=queries, query_variants=0,
                query_pages=1, query_per_page=1, timeout=1, query_delay=10,
                max_attempts=1, retry_base_delay=0, retry_max_delay=0,
                deadline_monotonic=MODULE.time.monotonic() + 0.05,
                stage_order="query_first", progress_every_pages=100,
            )
            args.output_dir.mkdir()
            state = {"completed_query_batches": {}, "failed_query_batches": {}}
            state_path = args.output_dir / "state.json"
            old = MODULE.discovery.FETCHERS["openalex"]
            MODULE.discovery.FETCHERS["openalex"] = lambda query, family, page, per_page, timeout: [
                raw_record("openalex", "Graphics Agent", "2606.10001", "An agent edits a 3D scene.", family)
            ]
            try:
                records, summary = MODULE.collect_query_lane(args, ["openalex"], state, state_path)
            finally:
                MODULE.discovery.FETCHERS["openalex"] = old
            self.assertEqual(len(records), 1)
            self.assertEqual(summary["completed_batches"], 1)
            self.assertFalse(summary["stopped_for_runtime_budget"])

    def test_query_first_order_interleaves_sources_for_each_taxonomy_query(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            queries = root / "queries.json"
            queries.write_text(json.dumps({"families": [{"id": "one", "queries": ["q1", "q2"], "taxonomy_hints": []}]}), encoding="utf-8")
            args = SimpleNamespace(
                output_dir=root / "out", queries=queries, query_variants=0,
                query_pages=1, query_per_page=2, timeout=1, query_delay=0,
                max_attempts=1, retry_base_delay=0, retry_max_delay=0,
                stage_order="query_first", progress_every_pages=100,
            )
            args.output_dir.mkdir()
            state = {"completed_query_batches": {}, "failed_query_batches": {}}
            state_path = args.output_dir / "state.json"
            calls = []
            old_openalex = MODULE.discovery.FETCHERS["openalex"]
            old_crossref = MODULE.discovery.FETCHERS["crossref"]
            def fake_fetch(source):
                def run(query, family, page, per_page, timeout):
                    calls.append((source, query))
                    return []
                return run
            MODULE.discovery.FETCHERS["openalex"] = fake_fetch("openalex")
            MODULE.discovery.FETCHERS["crossref"] = fake_fetch("crossref")
            try:
                _, summary = MODULE.collect_query_lane(args, ["openalex", "crossref"], state, state_path)
            finally:
                MODULE.discovery.FETCHERS["openalex"] = old_openalex
                MODULE.discovery.FETCHERS["crossref"] = old_crossref
            self.assertEqual(calls, [
                ("openalex", "q1"), ("crossref", "q1"),
                ("openalex", "q2"), ("crossref", "q2"),
            ])
            self.assertEqual(summary["status"], "complete")
            self.assertEqual(summary["execution_order"], "taxonomy_query_then_source")

    def test_arxiv_slice_resumes_from_partial_checkpoint_and_verifies_stability(self):
        with tempfile.TemporaryDirectory() as temp:
            output = Path(temp) / "out"
            output.mkdir()
            args = SimpleNamespace(
                output_dir=output, from_date="2026-06-17", until_date="2026-06-17",
                slice_days=1, arxiv_per_page=2, timeout=1, arxiv_delay=0,
                max_pages_per_slice=0, split_threshold=100, stability_days=14,
                max_attempts=1, retry_base_delay=0, retry_max_delay=0,
            )
            state = {"completed_slices": {}, "failed_slices": {}}
            state_path = output / "state.json"
            page0 = [
                raw_record("arxiv", "Graphics Agent A", "2606.10001", "An agent edits a 3D scene.", "category_date_enumeration"),
                raw_record("arxiv", "Graphics Agent B", "2606.10002", "An agent edits a 3D scene.", "category_date_enumeration"),
            ]
            page1 = [
                raw_record("arxiv", "Graphics Agent C", "2606.10003", "An agent edits a 3D scene.", "category_date_enumeration"),
                raw_record("arxiv", "Graphics Agent D", "2606.10004", "An agent edits a 3D scene.", "category_date_enumeration"),
            ]
            fail_second_page = {"enabled": True}
            def fake_fetch(query, window, start, per_page, timeout):
                if start == 0:
                    return page0, 4
                if fail_second_page["enabled"]:
                    raise TimeoutError("temporary page failure")
                return page1, 4
            old = MODULE.fetch_arxiv_page
            MODULE.fetch_arxiv_page = fake_fetch
            try:
                first_records, first_summary = MODULE.enumerate_arxiv(args, ["cs.GR"], state, state_path)
                self.assertEqual(first_records, [])
                self.assertEqual(first_summary["status"], "partial")
                self.assertEqual(first_summary["partial_checkpoint_files"], 1)
                self.assertEqual(state["failed_slices"]["2026-06-17__2026-06-17"]["partial_records_preserved"], 2)
                fail_second_page["enabled"] = False
                records, summary = MODULE.enumerate_arxiv(args, ["cs.GR"], state, state_path)
            finally:
                MODULE.fetch_arxiv_page = old
            self.assertEqual(len(records), 4)
            self.assertEqual(summary["status"], "complete")
            self.assertTrue(summary["date_coverage"]["exact"])
            self.assertEqual(summary["stability_verified_slices"], 1)
            self.assertEqual(summary["partial_checkpoint_files"], 0)

    def test_arxiv_first_page_is_preserved_when_budget_ends_during_pacing(self):
        with tempfile.TemporaryDirectory() as temp:
            output = Path(temp) / "out"
            output.mkdir()
            args = SimpleNamespace(
                output_dir=output, from_date="2026-06-17", until_date="2026-06-17",
                slice_days=1, arxiv_per_page=2, timeout=1, arxiv_delay=10,
                max_pages_per_slice=0, split_threshold=100, stability_days=0,
                max_attempts=1, retry_base_delay=0, retry_max_delay=0,
                deadline_monotonic=MODULE.time.monotonic() + 0.02,
                slice_order="newest_first", progress_every_pages=5,
            )
            state = {"completed_slices": {}, "failed_slices": {}}
            state_path = output / "state.json"
            first_page = [
                raw_record("arxiv", "Graphics Agent A", "2606.10001", "An agent edits a 3D scene.", "category_date_enumeration"),
                raw_record("arxiv", "Graphics Agent B", "2606.10002", "An agent edits a 3D scene.", "category_date_enumeration"),
            ]
            old = MODULE.fetch_arxiv_page
            MODULE.fetch_arxiv_page = lambda query, window, start, per_page, timeout: (first_page, 4)
            try:
                records, summary = MODULE.enumerate_arxiv(args, ["cs.GR"], state, state_path)
            finally:
                MODULE.fetch_arxiv_page = old
            self.assertEqual(records, [])
            self.assertTrue(summary["stopped_for_runtime_budget"])
            self.assertEqual(summary["partial_checkpoint_files"], 1)
            partials = list((output / "enumeration_slices").glob("*.partial.jsonl"))
            self.assertEqual(len(MODULE.load_jsonl(partials[0])), 2)

    def test_query_lane_resumes_at_failed_page(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            queries = root / "queries.json"
            queries.write_text(json.dumps({"families": [{"id": "one", "queries": ["q"], "taxonomy_hints": []}]}), encoding="utf-8")
            args = SimpleNamespace(
                output_dir=root / "out", queries=queries, query_variants=0,
                query_pages=3, query_per_page=2, timeout=1, query_delay=0,
                max_attempts=1, retry_base_delay=0, retry_max_delay=0,
            )
            args.output_dir.mkdir()
            state = {"completed_query_batches": {}, "failed_query_batches": {}}
            state_path = args.output_dir / "state.json"
            calls = []
            fail_page_one = {"enabled": True}
            old = MODULE.discovery.FETCHERS["openalex"]
            def fake_fetch(query, family, page, per_page, timeout):
                calls.append(page)
                if page == 1 and fail_page_one["enabled"]:
                    raise TimeoutError("temporary")
                size = 2 if page == 0 else 1
                return [raw_record("openalex", f"Graphics Agent {page}-{i}", f"2606.{page}{i:04d}", "An agent edits a 3D scene.", family) for i in range(size)]
            MODULE.discovery.FETCHERS["openalex"] = fake_fetch
            try:
                first_records, first_summary = MODULE.collect_query_lane(args, ["openalex"], state, state_path)
                self.assertEqual(first_records, [])
                self.assertEqual(first_summary["partial_checkpoint_files"], 1)
                fail_page_one["enabled"] = False
                records, summary = MODULE.collect_query_lane(args, ["openalex"], state, state_path)
            finally:
                MODULE.discovery.FETCHERS["openalex"] = old
            self.assertEqual(calls, [0, 1, 1])
            self.assertEqual(len(records), 3)
            self.assertEqual(summary["status"], "complete")
            self.assertEqual(summary["partial_checkpoint_files"], 0)

    def test_category_date_query_and_atom_parser(self):
        query = MODULE.arxiv_query(["cs.GR", "cs.CV"], MODULE.parse_day("2026-06-10"), MODULE.parse_day("2026-06-12"))
        self.assertIn("cat:cs.GR OR cat:cs.CV", query)
        self.assertIn("submittedDate:[202606100000 TO 202606112359]", query)
        xml = """<?xml version="1.0" encoding="UTF-8"?>
        <feed xmlns="http://www.w3.org/2005/Atom" xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/">
          <opensearch:totalResults>1</opensearch:totalResults>
          <entry><id>https://arxiv.org/abs/2606.13368v1</id><updated>2026-06-17T00:00:00Z</updated><published>2026-06-17T00:00:00Z</published>
          <title>IterCAD: Iterative CAD Agent</title><summary>An agent uses CAD tools.</summary><author><name>A. Researcher</name></author><category term="cs.AI"/></entry>
        </feed>"""
        records, total = MODULE.parse_arxiv_feed(xml, query, "window")
        self.assertEqual(total, 1)
        self.assertEqual(records[0]["identifiers"]["arxiv"], "2606.13368")
        self.assertEqual(records[0]["categories"], ["cs.AI"])

    def test_offline_two_lane_run_and_non_injection_gate(self):
        root = SCRIPT.parents[1]
        with tempfile.TemporaryDirectory() as temp:
            temp_path = Path(temp)
            enumeration = temp_path / "enumeration.jsonl"
            query = temp_path / "query.jsonl"
            output = temp_path / "out"
            enumeration_records = [
                raw_record("arxiv", "IterCAD: Iterative CAD Agent", "2606.13368", "An agent iteratively uses CAD tools to create 3D geometry.", "category_date_enumeration"),
                raw_record("arxiv", "Unrelated Protein Model", "2606.00001", "A language model for molecular proteins.", "category_date_enumeration"),
            ]
            query_records = [
                raw_record("semantic_scholar", "Tool-Augmented Spatial Reasoning for Multimodal Agents", "", "An agent uses tools for physical grounding.", "spatial_reasoning_components")
            ]
            enumeration.write_text("".join(json.dumps(x) + "\n" for x in enumeration_records), encoding="utf-8")
            query.write_text("".join(json.dumps(x) + "\n" for x in query_records), encoding="utf-8")
            command = [
                sys.executable, str(SCRIPT),
                "--taxonomy", str(root / "references" / "METHOD_TAXONOMY_TABLE.md"),
                "--paper-list", str(root / "references" / "PAPER_READING_LIST.md"),
                "--output-dir", str(output),
                "--from-date", "2026-06-01", "--until-date", "2026-06-30",
                "--enumeration-fixture", str(enumeration), "--query-fixture", str(query),
                "--expected-id", "2606.13368", "--skip-known-corpus-recall",
            ]
            result = subprocess.run(command, check=False, capture_output=True, text=True)
            self.assertEqual(result.returncode, 3, result.stderr)
            for name in (
                "enumerated_raw.jsonl", "query_raw.jsonl", "candidates.jsonl",
                "low_confidence_records.jsonl", "coverage.json", "state.json",
                "slice_manifest.jsonl", "run_manifest.json", "audit.json", "report.md", "progress.json",
            ):
                self.assertTrue((output / name).is_file(), name)
            coverage = json.loads((output / "coverage.json").read_text())
            self.assertTrue(coverage["recall_gate"]["non_injection"])
            self.assertTrue(coverage["recall_gate"]["passed"])
            self.assertFalse(coverage["collection_integrity_gate"]["passed"])
            self.assertFalse(coverage["comprehensive_wording_gate"]["passed"])
            self.assertIn("fixture execution", " ".join(coverage["collection_integrity_gate"]["blockers"]))
            audit = json.loads((output / "audit.json").read_text())
            self.assertTrue(audit["artifact_contract_passed"])
            self.assertIn("all papers", coverage["claim_policy"]["forbidden"])
            candidates = [json.loads(line) for line in (output / "candidates.jsonl").read_text().splitlines()]
            titles = {item["canonical_title"] for item in candidates}
            self.assertIn("IterCAD: Iterative CAD Agent", titles)
            self.assertIn("Tool-Augmented Spatial Reasoning for Multimodal Agents", titles)
            progress = json.loads((output / "progress.json").read_text())
            self.assertFalse(progress["in_progress"])
            self.assertFalse(progress["resume_required"])

    def test_tiny_foreground_budget_returns_audited_resumable_checkpoint(self):
        root = SCRIPT.parents[1]
        with tempfile.TemporaryDirectory() as temp:
            output = Path(temp) / "out"
            command = [
                sys.executable, str(SCRIPT),
                "--taxonomy", str(root / "references" / "METHOD_TAXONOMY_TABLE.md"),
                "--paper-list", str(root / "references" / "PAPER_READING_LIST.md"),
                "--output-dir", str(output),
                "--max-runtime-seconds", "0.000001",
                "--skip-known-corpus-recall",
            ]
            first = subprocess.run(command, check=False, capture_output=True, text=True, timeout=15)
            second = subprocess.run(command, check=False, capture_output=True, text=True, timeout=15)
            self.assertEqual(first.returncode, 3, first.stderr)
            self.assertEqual(second.returncode, 3, second.stderr)
            progress = json.loads((output / "progress.json").read_text())
            coverage = json.loads((output / "coverage.json").read_text())
            audit = json.loads((output / "audit.json").read_text())
            report = (output / "report.md").read_text()
            self.assertFalse(progress["in_progress"])
            self.assertTrue(progress["resume_required"])
            self.assertTrue(progress["stopped_for_runtime_budget"])
            self.assertEqual(progress["phase"], "checkpoint_ready")
            self.assertEqual(coverage["foreground_batch"]["status"], "checkpoint_ready")
            self.assertTrue(coverage["foreground_batch"]["resume_same_output_directory"])
            self.assertTrue(audit["artifact_contract_passed"])
            self.assertIn("Re-run the same command with this exact output directory", report)

    def test_missing_expected_id_fails_without_injecting_it(self):
        root = SCRIPT.parents[1]
        with tempfile.TemporaryDirectory() as temp:
            temp_path = Path(temp)
            enumeration = temp_path / "enumeration.jsonl"
            enumeration.write_text(json.dumps(raw_record("arxiv", "A Blender Agent", "2601.00001", "An agent edits a 3D scene.", "category_date_enumeration")) + "\n", encoding="utf-8")
            output = temp_path / "out"
            command = [
                sys.executable, str(SCRIPT),
                "--taxonomy", str(root / "references" / "METHOD_TAXONOMY_TABLE.md"),
                "--paper-list", str(root / "references" / "PAPER_READING_LIST.md"),
                "--output-dir", str(output), "--from-date", "2026-01-01", "--until-date", "2026-01-31",
                "--enumeration-fixture", str(enumeration), "--skip-query-lane", "--expected-id", "2606.13368", "--skip-known-corpus-recall",
            ]
            result = subprocess.run(command, check=False, capture_output=True, text=True)
            self.assertEqual(result.returncode, 3)
            coverage = json.loads((output / "coverage.json").read_text())
            expected = coverage["recall_gate"]["expected_ids"][0]
            self.assertFalse(expected["in_unfiltered_union"])
            self.assertFalse(expected["injected"])

    def test_independent_auditor_detects_count_tampering(self):
        root = SCRIPT.parents[1]
        with tempfile.TemporaryDirectory() as temp:
            temp_path = Path(temp)
            enumeration = temp_path / "enumeration.jsonl"
            query = temp_path / "query.jsonl"
            record = raw_record("arxiv", "A Blender Agent", "2601.00001", "An agent edits a 3D scene.", "category_date_enumeration")
            enumeration.write_text(json.dumps(record) + "\n", encoding="utf-8")
            query.write_text("", encoding="utf-8")
            output = temp_path / "out"
            command = [
                sys.executable, str(SCRIPT), "--taxonomy", str(root / "references" / "METHOD_TAXONOMY_TABLE.md"),
                "--paper-list", str(root / "references" / "PAPER_READING_LIST.md"), "--output-dir", str(output),
                "--from-date", "2026-01-01", "--until-date", "2026-01-31", "--enumeration-fixture", str(enumeration),
                "--query-fixture", str(query), "--skip-known-corpus-recall",
            ]
            subprocess.run(command, check=False, capture_output=True, text=True)
            with (output / "candidates.jsonl").open("a", encoding="utf-8") as handle:
                handle.write(json.dumps(record) + "\n")
            audit_script = SCRIPT.with_name("audit_historical_run.py")
            result = subprocess.run([sys.executable, str(audit_script), "--output-dir", str(output), "--no-write"], check=False, capture_output=True, text=True)
            self.assertEqual(result.returncode, 4)
            audited = json.loads(result.stdout)
            self.assertFalse(audited["artifact_contract_passed"])
            self.assertIn("candidate count differs", " ".join(audited["failures"]))


if __name__ == "__main__":
    unittest.main()
