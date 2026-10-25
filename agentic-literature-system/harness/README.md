# Agentic Literature System — Harness

A standalone, model-driven literature research runner. It discovers candidate papers, resolves identity and publication dates, reads PDFs, records scope and taxonomy evidence, and validates a dated report. The runtime adapts the Mini-BVB feedback loop and adds durable checkpoints, bounded retries, resumable state, and coverage audits.

The sibling [skill](../skill/README.md) supplies the frozen taxonomy, paper corpus, schemas, and offline report validators. Keep both folders together. This package contains the reusable research runtime, not the original private experiment environment or raw experiment logs.

## Requirements

- Python 3.11 or newer, Git, and Bash on Linux or macOS. Windows users can use WSL; native Windows process control is not supported.
- A provider supporting the Responses API, image inputs, and a model that follows the fenced JSON tool protocol. Hosted Responses `web_search` must be supported by the configured search model.
- Your own API credentials and model access. No account, endpoint override, key, or model entitlement is bundled.

Only the minimal upstream model adapter is included under `third_party/`. Its [source and license](third_party/README.md) are retained; no Blender or separate BVB checkout is needed.

## Install and verify offline

From the repository root:

```bash
cd agentic-literature-system/harness
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
python validate_project_bundle.py
python -m pytest -q
python ../skill/scripts/validate_portable_skill.py --skill-dir ../skill
python -m unittest discover -s ../skill/scripts -p 'test_*.py'
```

These checks do not require an API key or make paid model calls. Tests use synthetic responses. Runtime outputs go to ignored `runs/` and `cache/` folders.

## Configure a live run

Use [.env.example](.env.example) as a list of supported environment variables. The runner does not automatically load a `.env` file. Set credentials in your shell or secret manager; for example, in Bash:

```bash
read -rsp 'API key: ' OPENAI_API_KEY; echo
export OPENAI_API_KEY
export AGENT_MODEL='YOUR_MODEL_ID'
# Optional: set SEARCH_MODEL to a different model with hosted web_search.
# Optional: set OPENAI_BASE_URL to your provider's Responses API root.
```

Replace `YOUR_MODEL_ID` with a model available to your account. `OPENAI_BASE_URL` defaults to the public OpenAI API root. Use `--reasoning ''` if your model does not support a reasoning-effort parameter. Provider features are checked by actual responses: a search without returned search actions is rejected rather than counted as evidence.

Model cost is an estimate from LiteLLM's price table. For an unknown or custom-priced model, set **both** `INPUT_COST_PER_MILLION` and `OUTPUT_COST_PER_MILLION` to your provider's USD rates. Unknown pricing fails before a run instead of disabling the cost guard. Search usage is logged separately and is not included in the agent's cost limit; use provider-side spending limits for a billing cap.

## Prepare, run, resume

Choose a new run name and an offset-aware cutoff. The example below targets a fixed past date; replace both values for your own run. Retrieval happens now, so this is a date-targeted search, not a historical search-index replay. The report timezone is America/Chicago.

```bash
python prepare_experiment.py --name example-day --date 2026-10-20 \
  --as-of 2026-10-21T00:00:00-05:00 \
  --minutes 20 --read-candidates 10 --primary-opens 40

python run.py --run-dir runs/example-day --prompt runs/example-day/prompt.txt \
  --model "$AGENT_MODEL" --reasoning medium \
  --max-seconds 1200 --max-turns 80 --cost-limit 15
```

Preparation is offline. `run.py` starts live retrieval and model calls. Use the same time budget in preparation and execution. The model must return `DONE` and pass report validation before the run is complete. Exit code `3` means incomplete/stopped; inspect `progress.json` and `agent_meta.json`. Never present a partial run as an exhaustive search.

For an interrupted run, repeat the exact command with `--resume`. Preserve its prompt, model, reasoning, code, knowledge snapshot, and budgets. The runner restores its own state and journaled observations, refuses changed inputs, and cannot increase the original budget. If the original budget is exhausted, create a new run rather than overriding the guard.

## Outputs and history

Each run can contain:

- `report.md`, `papers.jsonl`, `run.json`, `audit.json`: rendered report and structural validation.
- `checkpoints/`, `triage.json`, `reading-plan.json`: durable paper decisions and pending work.
- `tool-events.jsonl`, `model-turns.jsonl`, `provider-responses/`: raw local observations and model output.
- `reading-audit.json`, `coverage-audit.json`: PDF delivery and collected-pool coverage checks.
- `progress.json`, `agent_meta.json`, `experiment-inputs.json`: status, limits, and input hashes.

New submissions, revisions, catch-up discoveries, borderline work, and unresolved leads remain separate. PDF delivery receipts establish which text reached the agent, not whether its interpretation is correct. Unreviewed candidates are not exclusions.

`daily_history.py --help` documents building an immutable history bundle from completed local runs. Pass an eligible bundle under `knowledge/` with `prepare_experiment.py --history-dir`. Only earlier runs at or before the new cutoff can be used; current peer results are not reference answers. No author-specific history bundle is shipped.

## Tool interface and optional host use

The runtime includes web search, HTML navigation, arXiv listing scans and Atom metadata, Hugging Face daily pages, PDF extraction/rendering, knowledge search, bounded shell/Python, checkpoints, and report validation. `research_tools.py` defines the exact 30-tool schema.

`mcp_server.py` exposes these same tools over standard input/output. An MCP-capable host can launch it with this environment:

```bash
RESEARCH_RUN_DIR="$PWD/runs/example-day" python mcp_server.py
```

This does not reproduce a desktop application's private prompts, browser control, or account-bound connectors. Machine-specific Codex launchers and provider-capture proxies from the original experiments are intentionally absent.

## Operational limits and privacy

The file tools constrain writes to the selected run, but the shell tool executes with the current OS account's privileges. This is **not an OS sandbox**. Use a dedicated environment for untrusted research tasks. Retrieved pages and PDFs are data, never instructions.

API key/token/password variables are removed from tool subprocess environments. Run traces may still contain source text, prompts, local paths, model responses, and opaque provider state: keep them private and review before sharing. `.gitignore` excludes credentials, environments, caches, runs and generated history. Before contributing, run `python check_release.py` after staging your changes from this Git checkout. The scanner reports file names and finding categories without printing matched secrets. It checks staged/tracked files; it is not a sanitizer for arbitrary future run output.

The public release was checked offline, including a clean relocated checkout. No paid end-to-end search was performed for this packaging task. Provider compatibility and semantic paper decisions still require live evaluation with the user's own configuration. Neither this harness nor the skill guarantees the same paper list on repeated runs or complete field coverage.
