# Agentic Literature Research Harness

Run the literature workflow from Python: search, read PDFs, annotate papers, and save evidence-backed reports. Set time and cost limits, inspect progress, and resume interrupted work.

Keep this folder beside [skill/](../skill/README.md), which supplies the taxonomy, paper corpus, and report validators.

## Requirements

- **Python 3.11+, Git, and Bash** on macOS or Linux; use WSL on Windows.
- Your own API key and model supporting **Responses, image inputs, and the fenced-tool protocol**.
- A search model supporting hosted Responses **`web_search`**; it can be the same model.

## 1. Install

From the repository root:

```bash
cd agentic-literature-system/harness
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python validate_project_bundle.py
```

## 2. Configure

In Bash, enter your key without putting it in command history:

```bash
read -rsp 'API key: ' OPENAI_API_KEY; echo
export OPENAI_API_KEY
export AGENT_MODEL='YOUR_MODEL_ID'
```

Replace `YOUR_MODEL_ID` with a model available to your account. Optional settings are listed in [.env.example](.env.example): `OPENAI_BASE_URL` selects another provider; `SEARCH_MODEL` selects another search model. **`.env` files are not loaded automatically.**

## 3. Run

Choose an unused run name. Replace the example date and cutoff for your search; the cutoff must include a timezone offset. Reports use America/Chicago.

```bash
python prepare_experiment.py --name example-day --date 2026-10-20 \
  --as-of 2026-10-21T00:00:00-05:00 \
  --minutes 20 --read-candidates 10 --primary-opens 40

python run.py --run-dir runs/example-day --prompt runs/example-day/prompt.txt \
  --model "$AGENT_MODEL" --reasoning medium \
  --max-seconds 1200 --max-turns 80 --cost-limit 15
```

Preparation is offline. `run.py` makes live API calls. Keep the preparation and execution time limits aligned. Use `--reasoning ''` if your model does not support reasoning effort.

The cost limit covers **estimated agent-model usage**; hosted search is billed separately. Unknown model prices require explicit rates—see [configuration and budgets](docs/usage.md#configuration-and-budgets).

## Read the results

Start with `runs/example-day/report.md`.

| File | Purpose |
| --- | --- |
| `run.json`, `papers.jsonl` | Structured paper records |
| `audit.json`, `reading-audit.json`, `coverage-audit.json` | Validation and coverage checks |
| `progress.json`, `agent_meta.json` | Completion status and stop reason |
| `checkpoints/` | Saved paper decisions |

Exit code **0** means validated completion; **3** means incomplete or stopped. Inspect the status before using a report. To resume, repeat the same `run.py` command with `--resume`; use unchanged inputs and the original budgets.

## More

[History and MCP](docs/usage.md) · [Troubleshooting](docs/usage.md#troubleshooting) · [Tests and privacy](docs/usage.md#tests-and-privacy) · [Mini-BVB attribution](third_party/README.md)

The shell tool runs with your OS account's privileges; use a dedicated environment for untrusted tasks. Keep run traces private. Validation checks evidence delivery and structure, while paper interpretations still need review.
