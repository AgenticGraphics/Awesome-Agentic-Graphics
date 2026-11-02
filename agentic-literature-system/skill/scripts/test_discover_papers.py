#!/usr/bin/env python3
"""Offline tests for discover_papers.py."""

from __future__ import annotations

import importlib.util
import io
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest import mock


SCRIPT = Path(__file__).with_name("discover_papers.py")
SPEC = importlib.util.spec_from_file_location("discover_papers", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)


class CollectorTests(unittest.TestCase):
    def test_network_helper_is_fail_fast_without_nested_retries(self):
        with mock.patch.object(
            MODULE.urllib.request,
            "urlopen",
            side_effect=TimeoutError("stalled source"),
        ) as urlopen:
            with self.assertRaises(TimeoutError):
                MODULE.open_url("https://example.invalid", 1, {"User-Agent": "test"})
        self.assertEqual(urlopen.call_count, 1)

    def test_daily_profile_has_bounded_all_source_request_plan(self):
        root = SCRIPT.parents[1]
        profile = MODULE.PROFILES["daily"]
        families = MODULE.read_query_families(
            root / "references" / "search-query-families.json",
            profile["family_limit"],
            profile["variants"],
            set(),
        )
        plan = MODULE.estimate_request_plan(
            list(profile["sources"]), families, profile["pages"], False,
        )
        exhaustive = MODULE.PROFILES["exhaustive"]
        exhaustive_families = MODULE.read_query_families(
            root / "references" / "search-query-families.json",
            exhaustive["family_limit"],
            exhaustive["variants"],
            set(),
        )
        old_style_plan = MODULE.estimate_request_plan(
            list(exhaustive["sources"]), exhaustive_families,
            exhaustive["pages"], True,
        )
        self.assertGreater(plan["query_families"], 0)
        self.assertLess(plan["estimated_max_requests"], old_style_plan["estimated_max_requests"])
        self.assertLessEqual(plan["estimated_max_requests"], 181)

    def test_runtime_budget_reason_is_deterministic(self):
        self.assertIn(
            "source runtime budget",
            MODULE.budget_exhaustion_reason(0.0, 5.0, 16.0, 100.0, 10.0),
        )
        self.assertIn(
            "global runtime budget",
            MODULE.budget_exhaustion_reason(0.0, 5.0, 101.0, 100.0, 10.0),
        )
        self.assertEqual(
            MODULE.budget_exhaustion_reason(0.0, 5.0, 9.0, 100.0, 10.0),
            "",
        )

    def test_same_day_date_is_pushed_into_arxiv_and_semantic_scholar_queries(self):
        arxiv_urls = []
        semantic_urls = []
        old_text = MODULE.get_text
        old_json = MODULE.get_json
        def fake_text(url, timeout):
            arxiv_urls.append(url)
            return '<feed xmlns="http://www.w3.org/2005/Atom"></feed>'
        def fake_json(url, timeout, token=""):
            semantic_urls.append(url)
            return {"data": []}
        MODULE.get_text = fake_text
        MODULE.get_json = fake_json
        try:
            MODULE.fetch_arxiv("graphics agent", "one", 0, 10, 1, target_day="2026-08-31")
            MODULE.fetch_semantic_scholar("graphics agent", "one", 0, 10, 1, target_day="2026-08-31")
        finally:
            MODULE.get_text = old_text
            MODULE.get_json = old_json
        decoded_arxiv = MODULE.urllib.parse.unquote_plus(arxiv_urls[0])
        decoded_semantic = MODULE.urllib.parse.unquote_plus(semantic_urls[0])
        self.assertIn("submittedDate:[202608300000 TO 202609012359]", decoded_arxiv)
        self.assertIn("publicationDateOrYear=2026-08-31:2026-08-31", decoded_semantic)

    def test_source_wide_rate_limit_stops_repeated_queries(self):
        with tempfile.TemporaryDirectory() as temp:
            output = Path(temp)
            args = SimpleNamespace(
                output_dir=output,
                must_include_id=[],
                include_artifacts=False,
            )
            coverage = {
                "mode": "same_day", "profile": "daily",
                "target_day": "2026-08-31", "timezone": "America/Chicago",
                "max_pages": 1, "per_page": 10, "sources": {},
                "request_plan": {},
            }
            families = [
                {"id": "one", "queries": ["q1", "q2"]},
                {"id": "two", "queries": ["q3", "q4"]},
            ]
            calls = []
            old = MODULE.FETCHERS["openalex"]
            def rate_limited(*args, **kwargs):
                calls.append(1)
                raise MODULE.urllib.error.HTTPError(
                    "https://example.invalid", 429, "rate limited", {}, io.BytesIO(b""),
                )
            MODULE.FETCHERS["openalex"] = rate_limited
            try:
                records, stopped_early = MODULE.collect_live_records(
                    args=args,
                    target_day="2026-08-31",
                    families=families,
                    sources=["openalex"],
                    coverage=coverage,
                    timeout=1,
                    request_delay=0,
                    max_runtime_seconds=10,
                    source_time_budget_seconds=10,
                    progress_every=1,
                )
            finally:
                MODULE.FETCHERS["openalex"] = old
            self.assertEqual(records, [])
            self.assertFalse(stopped_early)
            self.assertEqual(len(calls), 1)
            self.assertEqual(coverage["sources"]["openalex"]["pages_attempted"], 1)
            self.assertEqual(coverage["sources"]["openalex"]["status"], "failed")

    def test_identifier_normalization(self):
        self.assertEqual(MODULE.normalize_arxiv("https://arxiv.org/abs/2606.13368v2"), "2606.13368")
        self.assertEqual(MODULE.normalize_doi("https://doi.org/10.1000/ABC"), "10.1000/abc")

    def test_dedup_preserves_sources(self):
        one = MODULE.base_record("arxiv")
        one.update({"title": "A Graphics Agent for Blender", "identifiers": {"arxiv": "2601.00001"}, "urls": ["https://arxiv.org/abs/2601.00001"]})
        two = MODULE.base_record("openalex")
        two.update({"title": "A Graphics Agent for Blender", "abstract": "A VLM uses tools to edit 3D scenes.", "identifiers": {"arxiv": "2601.00001"}})
        merged = MODULE.merge_records([one, two])
        self.assertEqual(len(merged), 1)
        self.assertEqual(set(merged[0]["sources"]), {"arxiv", "openalex"})
        self.assertIn("edit 3D scenes", merged[0]["abstract"])

    def test_dedup_matches_title_across_different_identifier_types(self):
        one = MODULE.base_record("arxiv")
        one.update({"title": "A Graphics Agent for Blender", "identifiers": {"arxiv": "2601.00001"}})
        two = MODULE.base_record("crossref")
        two.update({"title": "A Graphics Agent for Blender", "identifiers": {"doi": "10.1000/graphics-agent"}})
        merged = MODULE.merge_records([one, two])
        self.assertEqual(len(merged), 1)
        self.assertEqual(merged[0]["identifiers"]["arxiv"], "2601.00001")
        self.assertEqual(merged[0]["identifiers"]["doi"], "10.1000/graphics-agent")

    def test_near_title_dedup_uses_bounded_bucket(self):
        one = MODULE.base_record("arxiv")
        one.update({"title": "A Graphics Agent for Blender Scene Editing", "identifiers": {"arxiv": "2601.00001"}})
        two = MODULE.base_record("crossref")
        two.update({"title": "A Graphics Agent for Blender Scene-Editing", "identifiers": {"doi": "10.1000/graphics-agent"}})
        noise = []
        for index in range(1000):
            item = MODULE.base_record("arxiv")
            item.update({"title": f"Unrelated Unique Paper Number {index}", "identifiers": {"arxiv": f"2501.{index:05d}"}})
            noise.append(item)
        merged = MODULE.merge_records(noise + [one, two])
        self.assertEqual(len(merged), 1001)
        target = [item for item in merged if item["canonical_title"].startswith("A Graphics Agent")][0]
        self.assertEqual(set(target["sources"]), {"arxiv", "crossref"})

    def test_local_prefilter_requires_agent_and_graphics(self):
        good = {"canonical_title": "A VLM Agent for Iterative Blender Scene Editing", "abstract": "The agent uses visual feedback and tools.", "query_families": ["x"]}
        bad = {"canonical_title": "An Agent for Molecular Discovery", "abstract": "A language model finds proteins.", "query_families": ["x"]}
        self.assertTrue(MODULE.local_score(good, {"x": []})[-1])
        self.assertFalse(MODULE.local_score(bad, {"x": []})[-1])

    def test_local_prefilter_does_not_match_terms_inside_unrelated_words(self):
        noisy = {
            "canonical_title": "A Decade of Guided Community Research with Vendor-Agnostic Methods",
            "abstract": "A language model study.",
            "query_families": ["x"],
        }
        score, agents, graphics, _, keep = MODULE.local_score(noisy, {"x": []})
        self.assertIn("language model", agents)
        self.assertEqual(graphics, [])
        self.assertFalse(keep)
        self.assertEqual(score, 2)

    def test_adjacent_component_and_creative_software_leads_survive(self):
        spatial = {
            "canonical_title": "Tool-Augmented Spatial Reasoning for Multimodal Agents",
            "abstract": "An agent uses tools for physical grounding.",
            "query_families": ["spatial_reasoning_components"],
        }
        photoshop = {
            "canonical_title": "A GUI Agent for Adobe Photoshop",
            "abstract": "The language model controls creative software.",
            "query_families": ["tool_interfaces"],
        }
        self.assertTrue(MODULE.local_score(spatial, {"spatial_reasoning_components": []})[-1])
        self.assertTrue(MODULE.local_score(photoshop, {"tool_interfaces": []})[-1])

    def test_merged_record_exposes_primary_dates(self):
        item = MODULE.base_record("arxiv")
        item.update({
            "title": "A Graphics Agent",
            "event_dates": [
                MODULE.event("published", "2026-01-02T10:00:00Z", "arxiv"),
                MODULE.event("updated", "2026-02-03T10:00:00Z", "arxiv"),
            ],
        })
        merged = MODULE.merge_records([item])[0]
        self.assertEqual(merged["published_date"], "2026-01-02")
        self.assertEqual(merged["updated_date"], "2026-02-03")
        self.assertEqual(merged["event_type"], "updated")

    def test_same_day_requires_day_level_paper_event(self):
        item = {"kind": "paper", "event_dates": [MODULE.event("published", "2026-08-27T10:00:00Z", "arxiv")]}
        self.assertTrue(MODULE.same_day_qualifies(item, "2026-08-27")[0])
        self.assertFalse(MODULE.same_day_qualifies(item, "2026-08-26")[0])
        curated = {"kind": "paper", "event_dates": [MODULE.event("curated", "2026-08-27", "huggingface")]}
        self.assertFalse(MODULE.same_day_qualifies(curated, "2026-08-27")[0])
        boundary = {"kind": "paper", "event_dates": [MODULE.event("published", "2026-08-28T02:00:00Z", "arxiv")]}
        self.assertTrue(MODULE.same_day_qualifies(boundary, "2026-08-27", "America/Chicago")[0])

    def test_same_day_coverage_gate_blocks_total_source_failure(self):
        ledger = {
            "arxiv": {"status": "failed"},
            "openalex": {"status": "failed"},
        }
        gate = MODULE.evaluate_same_day_coverage(ledger, ["arxiv", "openalex"], False)
        self.assertFalse(gate["usable"])
        self.assertFalse(gate["scripted_source_coverage_complete"])
        self.assertIn("blocked same-day candidate search", gate["recommended_label"])

    def test_same_day_coverage_gate_labels_partial_run(self):
        ledger = {
            "arxiv": {"status": "queried"},
            "semantic_scholar": {"status": "partial"},
            "crossref": {"status": "failed"},
        }
        gate = MODULE.evaluate_same_day_coverage(
            ledger, ["arxiv", "semantic_scholar", "crossref"], False
        )
        self.assertTrue(gate["usable"])
        self.assertFalse(gate["scripted_source_coverage_complete"])
        self.assertIn("partial same-day candidate search", gate["recommended_label"])

    def test_offline_cli_writes_auditable_outputs(self):
        root = SCRIPT.parents[1]
        with tempfile.TemporaryDirectory() as temp:
            temp_path = Path(temp)
            fixture = temp_path / "fixture.jsonl"
            records = [
                {
                    "kind": "paper", "source": "arxiv", "title": "A VLM Agent for Blender Scene Editing",
                    "authors": ["A. Researcher"], "abstract": "An agent uses tools and visual feedback to edit a 3D scene.",
                    "identifiers": {"arxiv": "2608.99999"}, "urls": ["https://arxiv.org/abs/2608.99999"], "venue": "arXiv",
                    "event_dates": [{"kind": "published", "value": "2026-08-27T12:00:00Z", "date": "2026-08-27", "source": "arxiv", "precision": "day"}],
                    "query_family": "blender_and_dcc", "query": "Blender VLM agent"
                },
                {
                    "kind": "paper", "source": "openalex", "title": "An Agent for Molecular Discovery",
                    "authors": [], "abstract": "A language model for protein design.", "identifiers": {}, "urls": [], "venue": "",
                    "event_dates": [{"kind": "published", "value": "2026-08-27", "date": "2026-08-27", "source": "openalex", "precision": "day"}],
                    "query_family": "graphics_agents_general", "query": "agentic graphics"
                }
            ]
            fixture.write_text("".join(json.dumps(x) + "\n" for x in records), encoding="utf-8")
            output = temp_path / "out"
            command = [
                sys.executable, str(SCRIPT), "--mode", "same_day", "--profile", "smoke",
                "--date", "2026-08-27", "--taxonomy", str(root / "references" / "METHOD_TAXONOMY_TABLE.md"),
                "--paper-list", str(root / "references" / "PAPER_READING_LIST.md"), "--fixture", str(fixture),
                "--output-dir", str(output)
            ]
            result = subprocess.run(command, check=False, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            for name in ("raw_records.jsonl", "candidates.jsonl", "coverage.json", "progress.json", "report.md"):
                self.assertTrue((output / name).is_file())
            candidates = [json.loads(line) for line in (output / "candidates.jsonl").read_text().splitlines()]
            self.assertEqual(len(candidates), 1)
            self.assertEqual(candidates[0]["canonical_title"], "A VLM Agent for Blender Scene Editing")
            coverage = json.loads((output / "coverage.json").read_text())
            self.assertTrue(coverage["same_day_coverage_gate"]["usable"])
            self.assertIn("offline", coverage["same_day_coverage_gate"]["recommended_label"])
            self.assertEqual(coverage["request_plan"]["estimated_max_requests"], 9)
            progress = json.loads((output / "progress.json").read_text())
            self.assertFalse(progress["in_progress"])


if __name__ == "__main__":
    unittest.main()
