# Discovery Compatibility Routing

The callable specialist skill `$agentic-graphics-paper-discovery` is an optional accelerator, not a dependency.

- Route today's or daily paper requests to the 6-minute bounded browser-based same-day workflow in `SKILL.md` and `data-sources.md`. Do not run local collection code or call scholarly APIs for this mode; return a source-ledger report at the first time/query/page limit.
- Route all-history, comprehensive, coverage, or corpus-expansion requests to bundled `scripts/historical_sweep.py`, which must use query-first multi-index augmentation plus newest-first category/date enumeration in 60-second resumable foreground checkpoints.
- Treat “all papers” as a recall target. The output must retain explicit limits and must never be presented as a proof of literature completeness.
- Use the historical run's independently audited `recommended_label`; do not upgrade its wording manually.
- After each historical batch, return its checkpoint instead of waiting silently for the entire backfile. Resume with the same output directory, and screen/curate a bounded candidate tranche when the request asks for research-ready results. Synchronized companion skills may perform these stages when available.

This compatibility reference remains so older prompts that mention `taxonomy_discovery`, `same_day_release_discovery`, or `historical_taxonomy_sweep` continue to route correctly.
