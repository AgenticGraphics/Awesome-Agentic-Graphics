# Historical Discovery Output Contract

Read this reference when running, resuming, auditing, or interpreting `scripts/historical_sweep.py`.

## Collection semantics

The runner has two independent recall lanes:

1. **Enumeration:** arXiv category-by-submission-date slices, adaptive splitting, pagination to the observed total, raw retention, and recent-slice stability verification.
2. **Query augmentation:** every maintained taxonomy query across OpenAlex, Crossref, Semantic Scholar, DBLP, and Hugging Face. Query search is relevance-ranked rather than an index enumeration.

Enumeration is streamed through the local prefilter so a full backfile does not need to be held in memory. Every rejected enumeration record remains in `enumerated_raw.jsonl` and `low_confidence_records.jsonl`.

## Foreground batch semantics

Historical coverage is a resumable collection, not one unbounded interactive process. A normal invocation:

1. searches taxonomy-derived query batches first, interleaving maintained sources for each query;
2. enumerates arXiv slices newest-first so recent work becomes available early;
3. stops starting network work at the finite foreground deadline;
4. materializes all required artifacts and an independently audited checkpoint; and
5. exits with an explicit `resume_required` value.

Query-first and newest-first change execution priority only. They do not remove older dates, categories, query families, or sources from the eventual configured scope. Use `--max-runtime-seconds 60 --timeout 10 --max-attempts 2 --retry-base-delay 1 --retry-max-delay 6 --progress-every-pages 1` for an ordinary interactive run. A runtime value of `0` is intentionally unbounded and must not be used in a normal foreground agent turn.

When the checkpoint says `resume_required: true`, return its findings and limitations to the user. Resume by running the identical collection command against the same output directory. Do not silently chain an indefinite number of batches, and do not create a new output directory for an unchanged fingerprint. Each resumed batch verifies and reuses completed pages, query batches, and arXiv slices.

## Required artifacts

| Artifact | Meaning |
|---|---|
| `enumerated_raw.jsonl` | All successfully enumerated arXiv source records before filtering |
| `query_raw.jsonl` | All successfully collected query-lane source records before filtering |
| `candidates.jsonl` | Deduplicated records retained for downstream paper screening |
| `low_confidence_records.jsonl` | Records not promoted to screening, retained for audit and filter refinement |
| `enumeration_slices/` | Completed per-slice arXiv checkpoints |
| `query_pages/` and `query_batches/` | Per-page and consolidated query checkpoints |
| `state.json` | Resumable state bound to the input-file and configuration fingerprint |
| `slice_manifest.jsonl` | Completed slice coverage ledger |
| `run_manifest.json` | Inputs, hashes, scope, pagination, retry policy, and selected label |
| `coverage.json` | Source coverage, truncation, exact date coverage, recall probes, gates, and blockers |
| `progress.json` | Live phase during collection; finalized non-running checkpoint state, counts, and resume decision after collection |
| `report.md` | Concise English interpretation using the machine-selected label |
| `audit.json` | Independent artifact-contract audit produced after the run |

Do not delete `.partial.jsonl` files to make a run appear clean. They are evidence of incomplete work and are consumed on resume.

## Gates

Interpret the gates hierarchically:

1. `audit.json -> artifact_contract_passed`: files parse, counts agree, hashes match, the report label agrees with `coverage.json`, and finalized progress/resume fields agree across artifacts.
2. `coverage.json -> collection_integrity_gate.passed`: exact configured date coverage, complete query augmentation, raw retention, live execution, and non-injection recall checks all pass.
3. `coverage.json -> comprehensive_wording_gate.passed`: the integrity gate passes and the run also covers the maintained full date/category/source/query scope.

`automated_coverage_gate` is a compatibility alias of `comprehensive_wording_gate`; the auditor requires them to be identical.

Use `coverage.json -> recommended_label` verbatim:

- `best-effort comprehensive automated historical sweep` only when the comprehensive-wording gate passes;
- `targeted historical candidate sweep with explicit coverage limits` when a narrower live run passes collection integrity;
- `partial historical candidate sweep; coverage gates not passed` otherwise.

No gate permits `all papers found`, `complete literature`, `fully exhaustive`, or `provably exhaustive`.

## Exit codes

- `0`: artifact contract and collection-integrity gate passed. The run may still be targeted.
- `2`: invalid inputs, unsupported configuration, or incompatible checkpoint fingerprint/schema.
- `3`: artifacts are internally consistent, but one or more collection-integrity requirements failed. This is the expected result for a valid foreground checkpoint that still requires resume.
- `4`: the independent artifact audit failed.

## Resume and source updates

Re-run the same command with the same output directory to resume. Completed files are reused only when record counts and SHA-256 hashes match. Failed pages and slices keep partial checkpoints. Recent arXiv slices are rechecked for stable totals and first-page identity before completion. If `--until-date` was omitted, the first batch freezes that day's end date in `run_manifest.json`; later batches recover it from the same output directory so an overnight resume does not change the fingerprint. Start a new output directory when intentionally extending the end date. Read `progress.json -> in_progress`, `resume_required`, `completed_query_batches`, and `completed_slices` after every invocation; a finalized batch must have `in_progress: false` even when the overall collection is partial.

The fingerprint includes the taxonomy, paper list, query-family file, scope, pagination, and retry policy. If any of these change, use a new output directory rather than mixing runs.

HTTP 429, transient network failures, malformed responses, and selected server errors use bounded exponential backoff. When attempts are exhausted, the run remains partial and preserves already fetched pages.

`--query-pages` is a per-query safety cap; `0` means paginate until a short page. A positive cap is not automatically a failure when the source exhausts early, but a full final page at the cap is recorded as truncation and blocks both gates. Hugging Face's non-paginated search is likewise marked truncated when it returns the requested maximum.

## Examples

Maintained full-scope attempt:

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

Targeted diagnostic:

```bash
python3 SKILL_ROOT/scripts/historical_sweep.py \
  --taxonomy SKILL_ROOT/references/METHOD_TAXONOMY_TABLE.md \
  --paper-list SKILL_ROOT/references/PAPER_READING_LIST.md \
  --from-date 2026-01-01 \
  --until-date 2026-06-30 \
  --categories cs.GR,cs.CV,cs.AI \
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

Independent re-audit:

```bash
python3 SKILL_ROOT/scripts/audit_historical_run.py --output-dir OUTPUT_DIRECTORY
```

After automated collection, manually cover official proceedings and venue archives, OpenReview, project/author pages, and backward/forward citations. Record each as completed, failed, blocked, or not run; do not imply that an index substitutes for an archive.
