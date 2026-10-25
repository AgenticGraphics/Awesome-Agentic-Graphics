# Daily discovery and taxonomy report

Read this for an exact-date search, daily report, or daily-system validation. Run the whole discovery → screen → curate → validate → render loop. The helper is offline: it does not retrieve papers and an empty prepared file is NOT a completed search.

## Start and source refresh

Read `source-manifest.json`, `taxonomy-codebook.json`, and `paper-corpus.json` in this directory. The public bundle is a frozen research snapshot, not a live connection to the authors' documents. Record `bundled_snapshot_not_live_refreshed` unless the caller supplies a newer authorized source. For an explicit refresh, compare source definitions and the corpus, rebuild the snapshots and schema together, and validate them before classification. Never call the bundled snapshot current without verification. Private source identifiers and account-bound connectors are not required.

The codebook has 18 system fields. Application families and Generation/Reconstruction/Editing/Auditing are separate paper-list routing facets, not replacements for system axes. Multi-select across applications is allowed. Tools labels are provisional: preserve alternative schemes from the raw source in `taxonomy_delta`; do not make them a settled taxonomy. Memory wording in the source is inconsistent (Working Memory within a call vs definition beyond a call); keep that caveat. Do not infer adaptation, memory, verifier use, or planning from model names. 2D SVG, figures, posters and slides are explicitly in scope. World auditing is a benchmark task, not asset authoring. Simulation-ready static geometry does not by itself establish dynamic authoring.

## Execution

Use a date explicitly supplied by the user, otherwise the client current date, with America/Chicago unless overridden. Obtain an actual offset-aware as-of time. For a past date use the whole local day; for today use midnight through as-of. Do not use the host date when client context differs.

```
python3 SKILL_ROOT/scripts/daily_report.py prepare --date YYYY-MM-DD --as-of OFFSET_AWARE_TIMESTAMP --output-dir RUN_DIRECTORY
```

Read the generated query plan. Use browser/web search for retrieval, never the historical collector or a scraper in this mode. The offline helper above is allowed for dates, provenance, validation and rendering. Default bounded pass: 6 minutes, 10 search batches, 24 primary-page opens, one retry; record actual counts. One search batch means one web-tool invocation containing searches; `search_queries` counts its individual query strings separately. `primary_opens` counts attempted source pages. Do not substitute query count for batch count. If a past tool-call count is unavailable, set that count to null and disclose the limitation. Search broadly across the nine application/harness query families and the five source families before deep reads. Within a batch combine independent queries. Use broad new/recent pages and undated technical queries as well as date strings; exact-date-only queries miss indexing. If the budget expires, record unreached families and return a partial report. Do not mark a category complete merely because an index may contain it.

For arXiv inspect category new/recent pages (prioritize cs.GR, cs.CV; rotate/record cs.AI, cs.HC, cs.RO, cs.MM, eess.IV) and submission history of each plausible lead. Check Hugging Face daily pages, OpenReview, official venues/proceedings, official projects/authors/labs. Search older paper-list aliases for related new work, but do not inject known papers as discoveries. Open primary pages for title/identity, submission/version history and technical evidence. Snippets, HF curation dates, GitHub activity, conference year and search indexing dates cannot establish a new-paper event. Repository-only releases stay signals or unresolved leads. Preserve earlier candidates as late discovery rather than padding today's results.

## Date semantics and persistence

Each event has `type` (first_submission/revision/formal_publication/artifact_release), `value`, `precision` (timestamp/date/unknown), `timezone`, `primary_url`, `authority` (primary/secondary), and a short `evidence` paraphrase. Timestamp values must include an offset; convert to target timezone. A date-only source without a timezone that resolves to the target calendar day remains date-unresolved. Preserve both raw source value and timezone. arXiv v1 submission is different from public announcement; label the event as submission and do not invent first-publication timing. Weekend/holiday silence or index delay cannot prove no new paper exists.

Use a seven-day lookback ONLY as a separately labeled catch-up discovery lane, never as the target day. When earlier run.json files are supplied/available in the selected report directory, compare identity+event type+version/value across them, report already-seen events and new-to-us older papers separately, and preserve prior runs. On the first run state that prior-run comparison is unavailable. Maintain a pending queue for inaccessible primary sources and revisit it next invocation. A skill does not schedule itself; create a recurring automation only on an explicit scheduling request.

## Fill run-input.json

Preserve the prepared frame and codebook version. Update `snapshot_status`, `source_ledger`, `query_coverage`, `counts`, `coverage_limits`, and `papers`. A source check contains `query_or_url`, `checked_at` (offset-aware), and `outcome`. If exact retrieval time was not captured, set `checked_at: null`, `time_basis: "recorded_only"`, and `recorded_at` to an actual offset-aware ledger-recording time. Bare "unknown", guessed timestamps, and timezone-free timestamps fail validation; record exact executed pages/queries including errors, not a planned query paraphrase. Read the clock for recorded observation times; never invent minute-by-minute timestamps. If exact retrieval time was not captured, use the actual ledger-recording time and say so in outcome. Source statuses: complete/partial/failed/blocked/not_applicable/not_reached_within_budget. Here complete means the declared source check finished, never literature completeness.

Every paper record needs:
- `canonical_title`, `authors` (empty if unknown), `identifiers` (arxiv/doi/openreview where verified), `canonical_urls`, `abstract`, `source_records`, `events`;
- `screening_status` (core/enabling_or_adjacent/scope_dependent/excluded/unresolved), `screening_reason`, `screening_evidence`, `confidence` (High/Medium/Low);
- `application_families`, `operations`, `contribution`, `limitations`;
- `taxonomy_cells`: every one of the 18 codebook keys, nonempty arrays with exact permitted labels or a single Not Reported/Not Applicable/Unclear;
- `field_evidence`: for each concrete cell, an object with `primary_url`, `evidence`, `locator` (e.g. abstract, Section 3, page 5), `level` (reported/derived) and `reasoning` for derived values;
- `taxonomy_delta` (array, empty when none); optional nearest known papers with an evidence-based difference, artifact links, evaluation datasets/metrics, and a next action.

Merge duplicates using versionless arXiv, DOI, OpenReview IDs, canonical URLs, then normalized titles/aliases, preserving all source records and events. Fuzzy matches are review candidates, not automatic merges. Different IterCAD papers, for example, must not merge on acronym alone. Known corpus status is computed against the discussed list; it does not imply accepted manuscript membership. For unresolved candidates use Unclear where evidence is unavailable, not invented taxonomy values. Read up to 10 plausible candidates in the bounded pass; retain the rest as unresolved queue.

```
python3 SKILL_ROOT/scripts/daily_report.py finalize --input RUN_DIRECTORY/run-input.json --output-dir RUN_DIRECTORY
```

For recurring/manual repeated runs, pass `--history-dir EXISTING_REPORT_ROOT` to finalize so previously reported identity+event+version combinations enter `already_reported`. No supplied history is explicitly marked unavailable. Fix errors and rerun. Deliver report.md, papers.jsonl, run.json, and audit.json. A structural pass does not establish evidence truth or discovery recall. Review the report against inspected primary sources. It separates same_day_new, same_day_updates, late_discovery, date_unresolved, unresolved and excluded. Report same-day new and same-day updates separately and retain evidence, taxonomy and coverage even at zero results. Say only: No qualifying same-day Agentic Graphics paper was verified in the browsed source set. Give limits immediately. Never guarantee all papers were found.

## Intended report information

Lead with target window, taxonomy/list revision, source status and new/update counts. For each relevant paper provide title/link, actual event date/type, application/task, scope decision, one-sentence contribution, 18-field taxonomy table with citations, known-list match, closest known method/difference when supported, code/data links when verified, missing evidence and recommended read/add/monitor action. Keep taxonomy deltas separate from the source taxonomy. Finish with pending leads, exclusions, exact source/query ledger and uncovered families. Machine-readable records preserve evidence for subsequent survey table updates; those updates require a separate request.

The historical screening/curation schemas retain legacy single-date handoff fields for compatibility. The daily contract uses the `events` array as its date authority; never flatten multiple versions into one ambiguous publication date.
