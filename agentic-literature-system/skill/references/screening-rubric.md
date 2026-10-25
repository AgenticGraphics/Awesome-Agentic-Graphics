# Agentic Graphics Screening Rubric

## Core inclusion test

A paper is `core` when both conditions hold:

1. It contains an agentic-system contribution or evaluation target: a model adapted for agentic behavior, an inference-time harness, iterative planning/refinement, tool/computer interaction, an agent-facing representation, an agentic toolkit, or a benchmark for such systems.
2. Its task, environment, actions, observations, outputs, or evaluation are materially about computer graphics, visual authoring, geometric content, rendering, animation, simulation/world construction, CAD/engineering design, or a maintained optional graphics task.

The paper need not use the phrase “agentic graphics.”

## Adjacent inclusion test

Use `enabling_or_adjacent` when the work materially informs one component but is not a complete core system. Examples:

- training or evaluating spatial/3D reasoning for models intended to serve agents;
- graphics program induction, shape programs, executable representations, or structured scene specifications;
- graphics code-generation models without an inference-time agent;
- general GUI/computer-use or coding-agent work with a transferable graphics interface or feedback design;
- graphics benchmarks that evaluate model/harness capability without providing a full agent;
- task-specific pipelines with local generator–critic loops but no global controller.

## Scope boundaries

2D SVG/vector graphics, editable figures, slides/presentations and posters are explicitly represented in the current paper list; apply the same core-system evidence test to them. General document/PDF automation without a graphics contribution remains scope-dependent. Distinguish asset authoring from downstream robot control; interactive world auditing belongs to benchmarks. Preserve list-specific notes and alternatives; membership alone does not establish inclusion.

## Exclusion codes

- `E1_DOMAIN`: no meaningful graphics relationship;
- `E2_NON_AGENTIC`: graphics work with no agentic or enabling component;
- `E3_ONE_SHOT`: ordinary text/image/3D generation without system, tool, feedback, or representation contribution;
- `E4_NON_RESEARCH`: marketing, commentary, or repository with no identifiable research contribution;
- `E5_DUPLICATE`: duplicate version or alias merged elsewhere;
- `E6_UNVERIFIABLE`: record cannot be resolved to a credible primary source;
- `E7_OUTSIDE_TASK_BOUNDARY`: optional area explicitly excluded by the user/current survey.

## Evidence standard

- `High`: full paper or authoritative proceedings/project source supports the decision and key mechanism.
- `Medium`: canonical abstract plus official project/artifact evidence supports the decision, but one or more mechanism fields remain unclear.
- `Low`: plausible lead without sufficient primary evidence; normally label `unresolved`.

Do not infer control flow from a system diagram alone when the text contradicts it. Do not infer model availability, training, feedback usage, or memory from common practice. Distinguish a metric used only for final reporting from a quantitative signal used inside the refinement loop.

## Two-pass status handling

Use `triage_status` for the first pass: `retain`, `needs_full_read`, or `reject_obvious`. Keep `screening_status` as `unresolved` until the second-pass primary-source decision is complete. Final `screening_status` must be exactly one of `core`, `enabling_or_adjacent`, `scope_dependent`, `excluded`, or `unresolved`.
