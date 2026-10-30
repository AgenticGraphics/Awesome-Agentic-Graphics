# Paper library

The library combines **337 historical papers** from the survey’s audited collection with daily search results. “All papers” merges duplicate IDs and uses the latest saved annotation. Choose “Survey collection” for the historical snapshot, or browse the calendar by **Publication date** or **Search date**. Use the month selector to jump through the historical collection; “View whole month” includes records whose exact day is unavailable.

## Publication dates

All 337 historical records have date provenance: 322 use arXiv first-submission dates, and 15 use retained publication dates. Of these, five are known only to the month; no day is inferred. Exact arXiv API timestamps, where available, are retained in UTC. Date sources appear under “Taxonomy & evidence”.

Publication-date browsing uses the original release date, even when a newer search report contains a revision. Search-date browsing continues to show what the system found on that day. The historical snapshot date is never treated as a publication date. Paper counts remain deduplicated.

## What the records mean

- Historical titles, links, and original publication dates come from the corpus used for the survey’s literature-growth figure. The snapshot is dated October 19, 2026; it is not a search run on that date.
- Short descriptions are retained curation notes, not newly generated abstracts.
- Taxonomy labels reuse existing primary-source readings (grade A) and evidence-backed recodings (grade B). Provisional or unsupported positive labels are displayed as **Unclear**. Existing **Not Reported** and **Not Applicable** values are preserved. Expand “Taxonomy & evidence” to inspect the sources.
- Application filters use the existing task annotations. Records without a specific mapped application remain **Cross-category**; this does not claim that every such paper spans multiple applications.
- The historical selection follows the growth figure’s scope and September 2026 cutoff. Background references, out-of-scope entries, and undated records are not added to reach a target count. The growth chart and the entire library can have different totals because the daily feed also includes adjacent and scope-dependent papers.

## Corrections

Select **Suggest a correction** on a paper, enter the proposed value and evidence, then review the GitHub draft. Maintainers review changes before merging them. The automation setup is described in [the contribution guide](contributing.md).

## Updating the snapshot

`scripts/import-survey.py` accepts the audited paper list, taxonomy records, and task annotations as explicit input paths. It exports only public paper metadata and selected evidence fields; internal file paths and private document links are excluded. It replaces only the historical collection and preserves daily reports. Run `node scripts/check-feed.cjs` and `node --test scripts/*.test.cjs` before proposing an update.

Do not reimport over reviewed community corrections without reconciling them with the source corpus first.

To attach date provenance to a newly imported historical collection, run `scripts/enrich-publication-dates.py --papers papers.json --metadata arxiv_metadata.json candidate_metadata.json --output data/daily-results.json`. The inputs are audited corpus records and optional saved arXiv API metadata. The exporter checks conflicting timestamps and includes only public date fields, never cache paths. Reimporting the same IDs preserves their existing date provenance.
