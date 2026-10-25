# Experimental annotation protocol, revision 4

This operational protocol applies identically to both harnesses. It supplements
the frozen taxonomy without adding labels or supplying paper-specific decisions.
It is an experimental policy, not an edit to the live Google Doc.
The explicit user scope and acceptance clarifications in user-acceptance-policy.md
take precedence over older broad inclusion examples.

- Classify the principal agentic subsystem and name its phase. Put other phases
  in notes. Require an evidenced agent action/decision on a graphics environment
  or artifact for core scope; keep defensible but unestablished connections in a
  separately displayed scope_dependent (borderline) group.

- Read the original taxonomy definitions and curation rules, not only the label list.
- For each selected label, identify the exact described mechanism and page or section.
  Review all 18 fields before saving. Add a second label only with independent support.
- `input_form` describes inputs provided for the task. Internally rendered observations
  belong under feedback or representation unless also supplied as task inputs.
- `output` describes products exposed by the method. Temporary intermediate state
  alone does not establish a second output label. `representation` may cover all stages.
- Task and application labels describe the graphics purpose. The presence of a
  renderer, simulator, or layout operation alone does not establish another purpose.
- Memory labels require a described retained state and evidence of lifetime/reach.
  A conversation, multiple roles, or the word "shared" alone does not establish
  cross-run persistence or access by all agents. Use the original definitions.
- Model training concerns the decision-making model. Do not infer off-the-shelf
  use from a model name, or fine-tuning from use of an adapted perception component.
- Tools must be callable capabilities used in the workflow; a component mentioned
  only in related work or final evaluation is not a system tool.
- Feedback means evidence used to change a subsequent action. Final evaluation
  metrics alone are not feedback scores or loop verifiers.
- Use `Not Reported` for silence after full reading, `Unclear` for actual ambiguity
  or conflicting evidence, and `Not Applicable` when the concept cannot apply.
  Explain the reason; do not guess merely to fill a cell.
- If the paper supports multiple interpretations that the taxonomy cannot resolve,
  preserve that uncertainty in evidence and taxonomy_delta. Do not consult another
  harness's labels or change a result solely to match it.

## Evidence boundaries that require an explicit check

- First identify one principal agentic subsystem, phase and deployed configuration.
  Use this same unit for application facets, operations and all 18 cells. Do not
  mix a separate image-reconstruction benchmark or 3D variant into the primary
  drawing configuration. Describe meaningful alternative configurations in notes.
- A graphics creation task is not automatically Visualization just because it
  renders an image, nor Modeling just because it writes code. Match the stated
  graphics purpose to source definitions/examples. If those do not settle the
  distinction, keep the uncertainty in taxonomy_delta instead of inventing a rule.
- The model_type and model_training fields refer to the model responsible for
  agentic decisions. If the analyzed component has no such decision-maker,
  Not Applicable can be appropriate even if its verifier is itself a VLM.
  If a decision-maker exists but its architecture/training is omitted, use
  Not Reported. Use Unclear for contradictory or genuinely ambiguous reporting.
  Named commercial/pretrained model use alone does not prove Off-the-Shelf.
- For each feedback label identify the observation, who judges it, and the next
  action it changes. An execution-status/error message supports Runtime; geometry,
  constraints or task statistics may instead be structural observations. Running
  a program alone does not establish Runtime feedback. Output formatting checks
  establish a Programmatic verifier only when their result controls a later action.
- Identify an explicit plan representation before assigning a planning degree.
  An action request is not automatically a multi-step plan. For workflow, describe
  the actual stage dependencies; a repeated single path can be Sequential, while
  substantive alternative branches, hierarchy or search dependencies support
  Graph-Structured. Record ambiguous boundaries rather than forcing agreement.
- For resources, distinguish reusable assets/examples/rules actually accessed by
  the selected subsystem from its freshly generated state, final evaluation data,
  and unrelated downstream training material. For outputs, distinguish externally
  exposed products from temporary helper code or intermediate decisions.
- For derived multi-select cells, give the evidence-to-label bridge for EACH
  label. A blanket claim that all labels follow the paper is insufficient.
  Perform a final consistency review against analysis_target before checkpointing.

These are paper-independent operational checks, not new taxonomy labels, a change
to the live source, or a requirement to reproduce either harness's prior answers.
