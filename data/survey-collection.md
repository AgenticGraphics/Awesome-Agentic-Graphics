# Paper library

The library combines **337 historical papers** from the survey’s audited collection with daily search results. “All papers” merges duplicate IDs and uses the latest saved annotation. Choose “Survey collection” for the historical snapshot, or use the calendar for an actual daily search.

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
