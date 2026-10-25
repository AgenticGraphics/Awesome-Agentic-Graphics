# Agentic Literature System

Two ways to run the evidence-preserving research workflow accompanying **Advances in Agentic Computer Graphics**:

| Package | How it runs | Start here |
| --- | --- | --- |
| Research skill | Instructions, taxonomy, schemas and standard-library helpers for an existing agent with web/PDF tools | [Skill README](skill/README.md) |
| Standalone harness | Python model/tool loop with explicit budgets, checkpoints, recovery, and report audits | [Harness README](harness/README.md) |

The workflow is **discover → screen and read → annotate → validate and curate**. Canonical identifiers, publication/revision dates, primary evidence, taxonomy cells, source coverage and unread queues are preserved. Knowledge is prior context, not proof of a new discovery.

```text
agentic-literature-system/
├── skill/       # Installable research skill and frozen reference bundle
└── harness/     # Standalone runner, shared research tools, tests and configuration
```

Both use the public October 15, 2026 experimental snapshot (18 taxonomy fields, 259 discussed-paper occurrences). This pinned codebook is distinct from later manuscript/website terminology. Source ambiguities and uncertain classifications remain explicit. Changing a snapshot requires updating its text, codebook, corpus, schemas and provenance together.

Skill retrieval uses the host's browser/search tools; harness retrieval uses its configured Responses search service plus public source APIs. They share research contracts but do not promise identical paper sets, labels, tools, or budgets. Output checks establish structural consistency and evidence delivery, not semantic correctness or exhaustive discovery.

The release excludes private document identifiers, account-bound connectors, developer machine paths, credentials, raw experiment runs and unpublished manuscript files. Configuration is caller-supplied. Original code follows the repository license; the vendored Mini-BVB adapter retains its [upstream license](harness/third_party/BVB-LICENSE). Public paper references retain their original attribution.

See [release validation](VALIDATION.md) for test results and remaining limits.
