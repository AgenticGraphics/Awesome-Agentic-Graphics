# Portability and Installation

This skill is distributed as one self-contained `agentic-graphics-research/` directory. Copy the entire directory, not only `SKILL.md`.

## Runtime requirements

- an agent that can read a `SKILL.md` instruction file and its relative references;
- browser or web-search access for same-day research;
- Python 3.10 or newer for historical collection and validation;
- outbound HTTPS access to scholarly APIs for historical collection;
- writable output storage chosen by the caller.

The bundled Python programs use only the Python standard library. No package installation, API key, fixed username, fixed home directory, repository checkout, or absolute local path is required. A `GITHUB_TOKEN` is optional when artifact discovery is explicitly enabled.

## Codex installation

Place the whole directory under the target machine's Codex skills directory so that the final path ends in:

```text
skills/agentic-graphics-research/SKILL.md
```

Restart or refresh the client if it does not immediately discover the skill. Invoke it as `$agentic-graphics-research` or with a natural-language request that matches its description.

## Other agents

For an agent without Codex skill discovery, provide the complete directory and instruct the agent to read `SKILL.md` first. The main skill contains a browser-based same-day workflow, standalone historical scripts, and screening, curation, source, and research-intelligence references. The three companion Agentic Graphics skills are optional and are not required.

## Validation after copying

From any working directory, run:

```bash
python3 PATH_TO_SKILL/scripts/validate_portable_skill.py --skill-dir PATH_TO_SKILL
```

Then run the offline test suite:

```bash
python3 -m unittest discover -s PATH_TO_SKILL/scripts -p 'test_*.py' -v
```

Validation checks required files, JSON syntax, Markdown-relative links, Python syntax, the bundled taxonomy markers, the current discussed-paper corpus, schema handoff compatibility, and accidental machine-specific paths.

## Refreshing the bundled research sources

Replace only these canonical files after verifying the new survey source:

- `references/METHOD_TAXONOMY_TABLE.md`
- `references/PAPER_READING_LIST.md`

Do not merge an accepted corpus with candidates, missing-paper lists, news, or discovery output. Re-run the portable validator and offline tests after every refresh. If optional companion skills are installed, synchronize their copies separately or use this standalone bundle as the sole source of truth.

## Failure behavior

Network failure is not a valid no-results finding. Same-day research must record browser source failures and scope any zero-result statement to the browsed source set. The historical collector records coverage gates and an independent audit. When historical Python networking is unavailable, retain the blocked ledger and use available web/connectors only as explicitly reported follow-up without claiming complete coverage.
