# Harness guide

[Back to quick start](../README.md)

## Configuration and budgets

The runner reads configuration from the environment. It does not load `.env` automatically.

| Variable | Purpose |
| --- | --- |
| `OPENAI_API_KEY` | Your provider credential; required for live runs |
| `AGENT_MODEL` | Default agent model; `--model` overrides it |
| `OPENAI_BASE_URL` | API root; defaults to `https://api.openai.com/v1` |
| `SEARCH_MODEL` | Hosted-search model; defaults to the agent model |
| `INPUT_COST_PER_MILLION` | Optional input-token rate in USD |
| `OUTPUT_COST_PER_MILLION` | Optional output-token rate in USD |

Set **both** cost rates for unknown or custom-priced models. Otherwise, estimates use the installed LiteLLM price table. Unknown pricing fails before the first model call. `--cost-limit` is an estimate for successful agent-model turns, not an invoice or a total spending cap: hosted search and rejected provider responses can incur additional charges. Use provider-side limits for a billing cap.

The provider must support Responses image inputs and a model that follows fenced JSON tool instructions. Search must return actual hosted `web_search` actions; an ungrounded answer is rejected. Provider compatibility needs live verification with your account.

## Resume and history

Resume by repeating the original `run.py` command with `--resume`. Keep the prompt, model, reasoning, code, knowledge snapshot, and budgets unchanged. The runner restores its own checkpoints and observations, refuses changed inputs, and cannot extend the original budget. If the budget is exhausted, prepare a new run.

To carry prior findings into a new day, build a history bundle from earlier local runs:

```bash
python daily_history.py --runs runs/previous-day \
  --output knowledge/daily-history/previous-day
```

Add `--history-dir knowledge/daily-history/previous-day` when preparing the next run. Source runs must precede the target day and satisfy its cutoff. Keep current peer results separate. Prior findings remain fallible context, and no author-specific history is shipped.

Date-targeted retrieval happens when you run the system; the cutoff does not recreate a historical search index. New submissions, revisions, catch-up discoveries, borderline work, and unresolved leads remain separate.

## Use the tools through MCP

`research_tools.py` defines 30 tools for retrieval, PDF reading/rendering, knowledge search, shell/Python execution, checkpoints, and report validation. An MCP-capable host can launch the same tools over standard input/output after preparing a run:

```bash
RESEARCH_RUN_DIR="$PWD/runs/example-day" python mcp_server.py
```

Run this from the harness directory with the same API configuration. The server supplies research tools; it does not reproduce a host application's private prompts, browser control, or account-bound connectors.

## Troubleshooting

| Symptom | What to do |
| --- | --- |
| Missing model or key | Set `AGENT_MODEL` and `OPENAI_API_KEY` in the current shell. |
| Unknown model pricing | Set both token rates listed above. |
| Unsupported reasoning parameter | Pass `--reasoning ''`. |
| Search returns no search actions | Choose a provider/model supporting hosted Responses `web_search`. |
| Run name already exists | Use `--resume` for the same run, or prepare a new name. |
| Exit code `3` | Read `progress.json` and `agent_meta.json`; preserve partial work. |
| Resume rejects changed inputs | Restore the original inputs or start a new run. |

Full observations are saved under `tool-events.jsonl`, `model-turns.jsonl`, and `provider-responses/`. PDF receipts record delivered pages, not comprehension. Unreviewed candidates and failed sources remain coverage gaps.

## Tests and privacy

From the harness directory:

```bash
python -m pip install -r requirements-dev.txt
python -m pytest -q
python ../skill/scripts/validate_portable_skill.py --skill-dir ../skill
python -m unittest discover -s ../skill/scripts -p 'test_*.py'
```

The tests run offline with synthetic responses and no paid model calls. See [release validation](../../VALIDATION.md) for tested environments and limits.

The file tools restrict writes to the selected run, but the shell runs with the OS account's privileges. This is not an OS sandbox. Retrieved papers and webpages are untrusted data.

Key/token/password environment variables are removed from tool subprocesses. Traces can still contain prompts, local paths, source text, and provider state; review them before sharing. Credentials, environments, caches, runs, and generated history are ignored by Git.

After staging a contribution, run `python check_release.py` from the harness directory. It scans staged/tracked files and reports locations and categories without printing matched secrets. It does not sanitize arbitrary future run output.
