# Agentic Graphics Research Skill

A portable, self-contained research agent for taxonomy-grounded Agentic Graphics literature discovery and research intelligence.

The skill implements the workflow:

```text
Discover -> Screen & Read -> Curate -> Retrieve -> Reason -> Identify Gaps -> Plan
```

It supports two main capabilities:

1. **Taxonomy-aware discovery**: browser-based exact same-day paper discovery and auditable, code-assisted historical candidate sweeps.
2. **Research intelligence**: literature QA, method comparison, novelty assessment, gap analysis, and evidence-grounded future planning.

Daily reporting runs on demand. Scheduling is optional and belongs to the host agent. For a standalone Python runner with budgets and recovery, see [Harness](https://github.com/AgenticGraphics/Awesome-Agentic-Graphics/tree/main/agentic-literature-system/harness). The public bundle pins an October 15, 2026 snapshot: 18 taxonomy fields and 259 discussed-paper occurrences. This experimental codebook is distinct from later manuscript and website terminology; the source heading/version ambiguity is retained in its metadata.

## Quick start

In Codex or another agent that supports skills, invoke:

```text
Use $agentic-graphics-research to browse for and classify Agentic Graphics papers released today.
```

The skill returns English output by default. Ask explicitly for another language when needed.

## Installation

Copy this complete `skill/` directory and rename the copied folder to `agentic-graphics-research`. Keep the original repository layout unchanged for the harness. Do not copy only `SKILL.md`, because the taxonomy, paper corpus, scripts, schemas, and research instructions are bundled as relative resources.

For Codex, place the directory so that the installed entrypoint is:

```text
<skills-directory>/agentic-graphics-research/SKILL.md
```

For an agent without native skill discovery, provide the complete directory and instruct the agent to read [SKILL.md](SKILL.md) first.

Runtime requirements:

- browser or web-search access for same-day research;
- Python 3.10 or newer and outbound scholarly-API access for historical collection and validation;
- a writable output directory selected by the caller.

The bundled programs use only the Python standard library. No fixed username, home directory, repository checkout, third-party Python package, or companion skill is required. See [portability.md](references/portability.md) for details.

## Validate the installation

Run the portable validator from any working directory:

```bash
python3 PATH_TO_SKILL/scripts/validate_portable_skill.py \
  --skill-dir PATH_TO_SKILL
```

Run the offline tests:

```bash
python3 -m unittest discover \
  -s PATH_TO_SKILL/scripts \
  -p 'test_*.py' \
  -v
```

The validator checks the complete bundle, relative links, machine-specific paths, JSON and Python syntax, the Google Docs taxonomy, the current discussed-paper corpus, query families, and cross-stage evidence contracts.

## Sources of truth

The skill always loads these bundled files before discovery, comparison, novelty assessment, or research planning:

- [METHOD_TAXONOMY_TABLE.md](references/METHOD_TAXONOMY_TABLE.md): current Google Docs Agentic Graphics system taxonomy and source definitions;
- [PAPER_READING_LIST.md](references/PAPER_READING_LIST.md): current discussed-paper corpus.

The taxonomy determines scope, terminology, comparison dimensions, and curation cells. The paper list determines discussed-corpus membership, known-versus-new status, citation keys, aliases, and task groupings. Absence from the paper list does not prove that a paper or idea does not exist.

## Common invocations

### Discover today's papers

```text
Use $agentic-graphics-research to browse for, verify, screen, and classify Agentic Graphics papers released today. Use America/Chicago as the exact calendar-day window, report every source checked, and do not run collection code or include older papers in the main findings.
```

### Run a historical landscape sweep

```text
Use $agentic-graphics-research to run an auditable historical Agentic Graphics candidate sweep across the full current taxonomy. Preserve coverage limits, screen retained candidates, classify verified papers, and do not claim that all papers were found.
```

A full historical collection is resumable and normally takes multiple bounded foreground batches. The first response should still contain the current checkpoint, highest-priority candidates, and coverage status; continue with the same output directory when requested. For a narrower study, specify dates or taxonomy areas:

```text
Use $agentic-graphics-research to search historical papers from 2024-01-01 through 2026-08-27 related to graphics-agent feedback, evaluators, and update strategies. Screen and classify the retained papers.
```

### Ask a domain question

```text
Use $agentic-graphics-research to explain how current Agentic Graphics systems use rendered, geometric-state, runtime, and quantitative feedback. Separate evidence from the maintained corpus, adjacent literature, and taxonomy-grounded inference.
```

### Compare methods

```text
Use $agentic-graphics-research to compare SceneCraft and VULCAN using the current taxonomy, focusing on organization, orchestration, topology, feedback, update strategy, interaction interface, observation space, resources, and evaluation.
```

### Assess idea novelty

```text
Use $agentic-graphics-research to assess the novelty of an agent that repairs Blender scenes using rendered, runtime, and geometric feedback. Retrieve the closest precedents, run targeted historical discovery, and give a calibrated—not absolute—novelty judgment.
```

### Identify gaps and plan future work

```text
Use $agentic-graphics-research to identify the most defensible gaps in the current Agentic Graphics taxonomy and literature, then propose three falsifiable research directions with baselines, evaluation plans, risks, and early invalidation experiments.
```

## Same-day browser and historical script usage

Agents should normally follow [SKILL.md](SKILL.md), because discovery results require primary-source screening and taxonomy curation.

### Same-day browser workflow

`Browser/Web Search → Primary-Source Date Verification → Agent Screening & Taxonomy Curation → Markdown Report`

Same-day research uses browser or web-search tools directly. It does **not** run `scripts/discover_papers.py`, call scholarly API endpoints, or create a scraper. It first makes a breadth-first pass across arXiv, Hugging Face Daily Papers, OpenReview, official proceedings, and targeted project/author/lab searches, then verifies promising leads. The default interactive limits are 6 minutes, 10 search batches, 24 candidate/primary-page opens, and one retry per failed page/query. At the first limit, save a partial English Markdown report with the source ledger and return its path; never keep searching silently.

The retained `discover_papers.py` file supplies shared normalization and query utilities to the historical collector and supports compatibility tests; it is not the current same-day entrypoint.

### Historical collector

`Python/API Collection → Local High-Recall Prefiltering → Agent Screening & Taxonomy Curation → Audited Checkpoint`

```bash
python3 PATH_TO_SKILL/scripts/historical_sweep.py \
  --taxonomy PATH_TO_SKILL/references/METHOD_TAXONOMY_TABLE.md \
  --paper-list PATH_TO_SKILL/references/PAPER_READING_LIST.md \
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

The historical runner combines:

- arXiv category-by-submission-date enumeration without keyword preselection;
- taxonomy-query augmentation across OpenAlex, Crossref, Semantic Scholar, DBLP, and Hugging Face;
- raw and low-confidence record retention;
- per-page and per-slice checkpoints;
- non-injection recall checks;
- explicit coverage gates and an independent artifact audit.

The foreground run is deliberately finite. It searches taxonomy-derived queries across sources first, enumerates recent arXiv slices before older slices, and then materializes a complete checkpoint artifact set. Exit code `3` usually means “valid partial checkpoint; resume required.” Read `progress.json`, `report.md`, and `coverage.json`, report the partial results, and re-run the same command with the same output directory to continue. An omitted end date is frozen by the first checkpoint, so overnight resumes keep the same fingerprint. Do not set `--max-runtime-seconds 0` in a normal interactive turn.

After each collection batch, screen at most 5 highest-priority unscreened candidates by default and report the remaining queue. Collection, primary-source reading, and taxonomy curation across a large historical corpus are intentionally incremental; the agent should not remain silent while trying to finish the entire corpus in one response.

Read [historical-output-contract.md](references/historical-output-contract.md) before running or interpreting a historical collection.

## Screening and taxonomy curation

Discovery candidates are leads, not accepted survey papers.

For every candidate:

1. apply the two-pass rules in [screening-rubric.md](references/screening-rubric.md);
2. preserve a record conforming to [screening-record.schema.json](references/screening-record.schema.json);
3. map verified evidence with [curation-rules.md](references/curation-rules.md);
4. preserve the final record using [curation-record.schema.json](references/curation-record.schema.json).

Use `Not Reported`, `Not Applicable`, or `Unclear` rather than guessing. Keep taxonomy changes in a separate delta layer; do not silently edit the taxonomy or accepted paper list.

## Research intelligence

Read [research-intelligence.md](references/research-intelligence.md) for the evidence protocol used by domain QA, comparison, novelty assessment, gap analysis, and future planning.

Research-intelligence conclusions should distinguish:

- findings established by the bundled literature;
- evidence from newly verified or adjacent work;
- taxonomy-grounded inference;
- unresolved uncertainty or search limitations;
- research hypotheses and proposed future work.

Novelty and field-wide gap claims require targeted or full historical discovery before a conclusion. The skill never provides an absolute novelty guarantee.

## Coverage and limitations

No automated workflow can prove that every relevant paper has been found.

- Same-day discovery is browser-based and restricted to authoritative paper events inside the exact current calendar day.
- Historical discovery is a high-recall, auditable candidate sweep, not a mathematical completeness guarantee.
- Search-index coverage, lag, rate limits, blocked sources, pagination caps, and manual archive coverage must be reported.
- Official proceedings, venue archives, project and author pages, and citation chaining remain important follow-up sources.
- News, repositories, social posts, and company announcements can generate leads, but they are not paper-publication evidence unless they are the authoritative release source.

The allowed historical labels are controlled by the run's coverage gates. Never upgrade the wording to `all papers found`, `complete literature`, `fully exhaustive`, or equivalent.

## Refresh the taxonomy and paper corpus

After verifying the current survey source, replace only:

```text
references/METHOD_TAXONOMY_TABLE.md
references/PAPER_READING_LIST.md
```

Keep candidates, missing-paper lists, discovery outputs, news, and adjacent literature separate from the discussed survey corpus. Re-run the validator and offline tests after every refresh.

## Directory structure

```text
agentic-graphics-research/
├── SKILL.md
├── README.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── METHOD_TAXONOMY_TABLE.md
│   ├── PAPER_READING_LIST.md
│   ├── data-sources.md
│   ├── historical-output-contract.md
│   ├── screening-rubric.md
│   ├── screening-record.schema.json
│   ├── curation-rules.md
│   ├── curation-record.schema.json
│   ├── research-intelligence.md
│   └── portability.md
└── scripts/
    ├── discover_papers.py        # historical shared utilities; not the same-day entrypoint
    ├── historical_sweep.py
    ├── audit_historical_run.py
    ├── validate_portable_skill.py
    └── test_*.py
```
