# User-confirmed research and acceptance policy — 2026-10-15

This policy records the user's explicit clarification for new experiments. It
supersedes the earlier requirement for exact agreement with a stochastic Codex
reference. Historical reports and comparison metrics remain unchanged.

## Research unit

Describe the paper's principal agentic subsystem in the 18 taxonomy fields.
Identify the subsystem and whether it operates at task time, data generation,
training, or evaluation. Describe other phases separately in notes. Do not mix
the controller's inputs with a downstream generator's outputs or training reward
with task-time feedback.

## Graphics action and scope

The central subject is graphics-related work in which an agent emits an action
or decision that operates on a graphics environment or graphics artifact. For a
core claim, identify the controller, the action/decision, and its graphics target
in primary evidence. The controller need not be an LLM if the agentic relation is
otherwise demonstrated.

An explicitly agent-facing graphics component may be enabling_or_adjacent when
its intended or evaluated agent use is supported. A graphics-related mechanism
that could materially inform such an agent, but does not establish this action
relation, can be displayed as borderline: use scope_dependent, explain the
possible connection and the missing evidence, and show it in a separate section.
Do not infer an agent merely from words such as memory, iterative, or feedback.
Do not exclude a defensible borderline contribution merely to force agreement.
Ordinary graphics work without a material connection to an agent system still
fails the relevance test. No paper-specific inclusion answers are supplied here.

## Acceptance

The user selected: evidence is correct, coverage is auditable, failures are
recoverable, and classification disagreements are explicitly preserved.

- Bind specific claims to the actual paper/version and page or section. Preserve
  uncertainty when primary evidence or taxonomy definitions do not resolve a label.
- Preserve source coverage, missing metadata, title/abstract triage, unread leads,
  and failed retrievals. A keyword non-match or an unreviewed item is not exclusion.
- Persist work, recover bounded transient failures, retain exhausted failures and
  partial outputs, and never replay an uncertain mutation or extend old budgets.
- Show paper-set and taxonomy differences without treating Codex as ground truth.
  Exact cross-harness or repeated-output equality is a diagnostic, not a pass gate.

Structural validation and delivery receipts support these checks but do not
prove semantic correctness. Do not claim exhaustive discovery or guaranteed
availability of the external model/source services.
