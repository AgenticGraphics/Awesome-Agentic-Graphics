---
name: agentic-graphics-research
description: Run portable, taxonomy-grounded Agentic Graphics research with browser-based same-day discovery, resumable code-assisted historical discovery, screening and reading, taxonomy curation, literature QA, comparison, novelty assessment, gap analysis, and future planning. Use when the bundled taxonomy and discussed-paper corpus should govern the research workflow.
---

# Agentic Graphics Research

Act as a portable Agentic Graphics research-knowledge agent. This folder is self-contained: do not assume a particular username, home directory, repository checkout, Codex installation path, or the presence of companion skills. Return English output unless the user explicitly requests another language. Daily reports use the dedicated workflow below; scheduling is separate.

## Resolve and validate the local bundle

Treat the directory containing this `SKILL.md` as `SKILL_ROOT`. Resolve every path below relative to `SKILL_ROOT`, regardless of the current working directory.

Before research, read:

- [references/METHOD_TAXONOMY_TABLE.md](references/METHOD_TAXONOMY_TABLE.md): bundled Agentic Graphics taxonomy and source definitions;
- [references/PAPER_READING_LIST.md](references/PAPER_READING_LIST.md): current discussed-paper corpus;
- [references/source-registry.md](references/source-registry.md): source roles, status boundaries, and refresh rules.

For a new installation, copied bundle, or suspected corruption, run `python3 SKILL_ROOT/scripts/validate_portable_skill.py --skill-dir SKILL_ROOT`. Stop and report the missing or invalid resource if validation fails. Read [references/portability.md](references/portability.md) when installing, copying, or diagnosing the skill.

Companion skills `$agentic-graphics-paper-discovery`, `$agentic-graphics-paper-screening`, and `$agentic-graphics-taxonomy-curation` are optional. Do not delegate to them by default: execute the local scripts, rubrics, and schemas below as the authoritative standalone workflow. Use a companion only when the user explicitly invokes it or its full workflow version has been verified against this bundle. Its absence must never block the workflow.

## Route the request

### Same-day paper research

For today's papers, a dated daily search, or taxonomy-structured daily reporting, execute [references/daily-workflow.md](references/daily-workflow.md). Use browser/web tools for retrieval and `scripts/daily_report.py` for offline preparation, date/label validation, and rendering. The current snapshot and exact field codebook supersede the old V4 contract. Preserve new papers, updates, catch-up and unresolved dates separately. Do not schedule recurring work unless requested.

### Historical landscape research

For historical landscape work, corpus expansion, coverage analysis, taxonomy stress testing, or a request phrased as “all papers”:

1. Read [references/historical-output-contract.md](references/historical-output-contract.md) and run one bounded foreground batch of the two-lane collector. Query augmentation runs first and interleaves OpenAlex, Crossref, Semantic Scholar, DBLP, and Hugging Face for each taxonomy query; arXiv category/date enumeration then proceeds newest-first. These choices improve early utility but do not narrow the configured final scope.
2. Keep the normal foreground budget finite. Use 60 seconds by default with a 10-second request timeout, two total attempts, short bounded backoff, and page-level progress. Never set `--max-runtime-seconds 0` during an ordinary interactive agent turn. The collector must finalize a checkpoint report when the budget is reached; an exit code of `3` is an expected partial checkpoint, not a reason to hide the output or keep waiting indefinitely.
3. Read final `progress.json`, `report.md`, and `coverage.json` immediately after the process returns. If `resume_required` is true, report the current findings and coverage limits now. Continue only by re-running the identical command with the **same output directory** so verified pages, query batches, and slices are reused. When no end date was supplied, the first checkpoint freezes it for overnight resumes. Do not restart into a fresh directory unless the input fingerprint changed or the user intentionally extends the end date.
4. Preserve raw records, low-confidence records, failed slices, pagination limits, checkpoints, and source provenance before filtering.
5. Screen a bounded tranche of the highest-priority unscreened candidates per response—5 by default—using the bundled screening rubric and schema. State how many candidates were screened and how many remain. Lexical filtering is never the inclusion decision, and a full historical collection plus paper-level reading is a resumable multi-run workflow rather than one silent foreground call.
6. Populate current cells and record per-paper taxonomy deltas for the screened tranche using the bundled curation rules and schema.

```bash
python3 SKILL_ROOT/scripts/historical_sweep.py \
  --taxonomy SKILL_ROOT/references/METHOD_TAXONOMY_TABLE.md \
  --paper-list SKILL_ROOT/references/PAPER_READING_LIST.md \
  --stage-order query_first \
  --slice-order newest_first \
  --max-runtime-seconds 60 \
  --timeout 10 \
  --max-attempts 2 \
  --retry-base-delay 1 \
  --retry-max-delay 6 \
  --progress-every-pages 1 \
  --output-dir OUTPUT_DIRECTORY
```

Apply no date cutoff unless the user supplies one. One foreground batch always materializes auditable outputs, even when the collection is incomplete. Return that checkpoint instead of launching an indefinite sequence of foreground batches. Use `coverage.json -> recommended_label` verbatim. The phrase `best-effort comprehensive automated historical sweep` requires a passing independent artifact audit and comprehensive-wording gate, but still does not establish field-wide completeness. Never say `all papers found`, `complete literature`, `fully exhaustive`, or equivalent. Manual venue archives, project/author pages, and backward/forward citation chaining remain required follow-up.

### Research intelligence

For domain QA, method comparison, novelty checks, gap analysis, or future-direction planning, read [references/research-intelligence.md](references/research-intelligence.md).

- Retrieve from the bundled taxonomy and paper list first.
- For existence, novelty, completeness, or field-wide gap claims, run a targeted or full historical pipeline before concluding.
- For questions about the current date, run the browser-based same-day workflow.
- Distinguish literature evidence, taxonomy-grounded inference, and research hypothesis.

For the daily system architecture, output rationale, and survey evaluation boundaries, read [references/daily-system-design.md](references/daily-system-design.md).

## Evidence-preserving pipeline contract

Keep these fields through discovery, screening, and curation:

`canonical_title`, `authors`, `identifiers`, `canonical_urls`, `source_records`, `published_date`, `updated_date`, `event_type`, `abstract`, `known_corpus_status`, `triage_status`, `screening_status`, `screening_reason`, `screening_evidence`, `extracted_system_evidence`, `taxonomy_cells`, `field_evidence`, `outside_current_taxonomy`, `taxonomy_delta`, `confidence`.

Never collapse source date, local discovery date, paper publication date, and revision date. Never turn `Not Reported` into an inferred negative. Never silently add a candidate to the discussed survey corpus or mutate the taxonomy.

## Completion gates

Do not present a run as complete unless all applicable gates pass:

- the portable-bundle validator passes;
- every requested source family has an explicit status;
- same-day retrieval uses browser/web search; offline daily_report.py validates and renders;
- the same-day report records the pages and queries checked for every maintained source family;
- same-day items have day-level primary-source evidence inside the exact window;
- a same-day zero-result statement is scoped to the documented browsed source set and accompanied by coverage limits;
- historical enumeration has exact slice coverage without hidden truncation and retains raw records;
- each historical foreground invocation ends with `progress.json -> in_progress: false`, an audited checkpoint report, and an explicit `resume_required` value;
- historical recall checks are non-injection checks against ordinary discovery output;
- the historical artifact audit passes and report wording does not exceed `coverage.json -> recommended_label`;
- every retained paper has human-readable screening evidence;
- taxonomy cells use current permitted values or `Not Reported`, `Not Applicable`, or `Unclear`;
- non-fitting evidence remains in a taxonomy delta rather than being forced into a cell;
- discussed-corpus membership remains separate from candidate status.

Use the research flow:

`Discover -> Screen & Read -> Curate -> Retrieve -> Reason -> Identify Gaps -> Plan`
