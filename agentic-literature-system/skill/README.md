# Agentic Graphics Research Skill

Discover, read, and classify Agentic Graphics papers inside your existing agent. You can also compare methods, review related work, and explore research gaps.

**Needs:** an agent with web search and PDF-reading tools, plus Python 3.10+ for the bundled helpers. The helpers use only the Python standard library.

## Install

1. Copy this entire `skill/` folder into your agent's skills directory.
2. Rename the **copy** to `agentic-graphics-research`.
3. Refresh your agent's skill list if needed.

The installed entrypoint should be:

```text
<skills-directory>/agentic-graphics-research/SKILL.md
```

Keep the original repository folders unchanged if you also use the harness. For agents without skill discovery, provide the folder and ask the agent to read [SKILL.md](SKILL.md) first.

## Try it

**Find today's papers**

```text
Use $agentic-graphics-research to find and classify today's Agentic Graphics papers.
Save a report with paper links, supporting evidence, and source coverage.
```

**Explore earlier work**

```text
Use $agentic-graphics-research to find papers from 2024–2026 on feedback and
verification in graphics agents. Save a checkpoint so we can continue later.
```

**Compare methods**

```text
Use $agentic-graphics-research to compare these papers using the bundled taxonomy.
Explain each difference with evidence from the papers: [paper links]
```

Reports are in English by default; ask for another language when needed. You can specify a date, timezone, topic, or output directory. Daily searches default to America/Chicago.

## What you get

A report with verified paper links, date and scope decisions, taxonomy annotations, supporting evidence, and remaining gaps. New submissions, revisions, and older discoveries stay separate.

Daily discovery uses the host's web tools. Historical collection runs in bounded batches; continue with the **same output directory** to reuse its checkpoint. Collected candidates still need paper-level review.

## Check your installation

From the installed skill folder:

```bash
python3 scripts/validate_portable_skill.py
python3 -m unittest discover -s scripts -p 'test_*.py'
```

These checks run offline. The bundle uses a frozen October 15, 2026 research snapshot; it does not refresh private source documents automatically. Follow the [source registry](references/source-registry.md) to update the taxonomy, corpus, and schemas together.

## Details

[Daily workflow](references/daily-workflow.md) · [Historical collection](references/historical-output-contract.md) · [Screening rules](references/screening-rubric.md) · [Taxonomy curation](references/curation-rules.md) · [Installation help](references/portability.md)

For a standalone Python runner, use the [harness](https://github.com/AgenticGraphics/Awesome-Agentic-Graphics/tree/main/agentic-literature-system/harness). Neither version guarantees that every relevant paper will be found.
