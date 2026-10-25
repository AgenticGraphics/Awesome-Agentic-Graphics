# Taxonomy Curation Rules

## Cell representation

- Use the exact current label spelling.
- Represent multi-select values as arrays, not prose joined by “and.”
- Put paper-specific names only where the taxonomy calls for a concrete value, such as Execution Environment or Evaluation Source.
- Store explanations in evidence fields, not inside compact taxonomy cells.
- Use `Not Applicable` when the concept cannot apply, `Not Reported` when it applies but the paper is silent, and `Unclear` when available evidence conflicts or remains ambiguous.

## Evidence levels

- `reported`: directly stated in the paper or official artifact;
- `derived`: a conservative classification derived from an explicitly described mechanism;
- `unclear`: evidence is incomplete or conflicting.

Every `derived` value must include the reasoning bridge. Do not infer proprietary/open status, fine-tuning, memory, feedback use, or agent organization from model/tool names alone.

## Important boundaries

- Training-time iterative generation is not automatically an inference-time agent.
- An evaluation harness is not automatically a generative agent.
- Fixed stages do not imply an autonomous planner. Use the current codebook: Planning PO-1/PO-2/PO-3 and Workflow Sequential/Parallel/Graph-Structured, according to the described mechanisms. Workflow-Driven is an obsolete label and must not be emitted.
- `Action Type` is the form of the operation; `graphics_software` describes agent readiness, not its brand.
- Separate feedback observations from assessment and the verifier actor.
- Final metrics belong under Benchmark & Evaluation; only loop-internal scores belong under `Score` assessment.

## Delta acceptance test

Score each proposed delta on:

1. evidence strength;
2. recurrence across papers;
3. ability to distinguish meaningful system choices;
4. relevance to graphics-specific agent design;
5. compatibility cost for the existing current discussed-paper table.

Recommend:

- `accept` when evidence is strong, recurrent, decision-relevant, and backward-compatible or worth the migration;
- `monitor` when important but supported by too few papers;
- `reject` when it is an implementation detail, duplicate concept, or unsupported inference.
