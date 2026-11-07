# Agentic Graphics daily report
Date: 2026-11-06 | Timezone: America/Chicago | As of: 2026-11-07T22:32:06+00:00
browser-based same-day search; documented source coverage
Taxonomy: google-doc-taxonomy-v3-2026-10-15 | Snapshot: authorized_live_snapshot_reconciled_and_frozen

## Coverage limits
- No qualifying same-day Agentic Graphics paper was verified in the browsed source set. This is not a zero-publication or exhaustive-discovery claim.
- Frozen target window: 2026-11-06T00:00:00-06:00 through 2026-11-07T00:00:00-06:00; as-of remains 2026-11-07T22:32:06+00:00. Retrieval later than cutoff does not extend eligible versions.
- Four listing scans resolved 1062 unique IDs, all metadata complete; catalog routes 935 lookback and 127 outside-window identities, zero target_and_uncertain. Historical listings/index delays may omit target-day releases.
- Reviewed all 139 catchup attention abstracts and 12 remaining title hints, plus additional leads: 159 individual decisions in triage.json. Nonattention catalog abstracts mostly remain unreviewed; absence of keyword hints is not exclusion. Catalog preserves their complete primary metadata.
- Fourteen version-pinned full PDF reads checkpointed: eight seven-day first submissions, three seven-day revisions and three newly completed older frozen-history backlog items. Zero verified same-day new or revised papers. No historical records imported as newly read.
- Harness instructed FINALIZE NOW at turn 47 on its estimated-cost/time reserve. Stopped after completing in-flight PICA checkpoint; six nominal PDF slots unused. No direct-action catch-up candidate remained in selected_next at stop; outside-window direct-action leads found during hint reconciliation remain unread.
- Reading queues: reading-plan.json ranked_unread (date-routed); additional-deferred.json superset of plausible unread arXiv candidates, including outside-window leads; additional-source-leads.json holds unresolved search mentions. Neither queue represents final exclusions or retained scope labels.
- Borderline and explicit-enabling candidates remain unread in queues, not silently rejected or promoted. No fully read borderline paper this run; all 14 selected full reads demonstrated graphics actions.
- Official venues and OpenReview coverage is search-only and partial; projects limited to two opens. Hugging Face is curation only. cs.AI/cs.HC/cs.RO/cs.MM/eess.IV listings not reached.
- 159 triage decisions include provisional abstract-based rejects; these are not final excluded full-paper records. No fabricated full-text taxonomy for ordinary unreviewed catalog items.
- Frozen prior INDEX fully reviewed; three reserved backlog reads completed (CADFather, Code2Worlds-2, CADForge). Remaining prior pending queue unchanged; see backlog-plan.json and authorized history bundle.
- Some official source records have surprising ID-month versus timestamp combinations; used authoritative timestamps rather than deriving dates from IDs. No unstated correction made.
- Prepared source snapshot and taxonomy preserved. Initial source-registry.json lookup failed and was corrected to source-registry.md. One local triage-write NameError was recovered by replaying only the failed deterministic local persistence command.
- See research-notes.md for grouped findings and scope/taxonomy caveats; coverage-audit.json supplies mechanical gaps. Evidence receipts validate delivery, not semantic truth.
- Final mechanical audit: required listing scans and collected target-focus metadata show no missing pages, pending metadata or target-focus triage gaps. This focus set is empty, so the pass does not certify the unreviewed remainder. Reading queue has no missing/duplicate ranks and no missing delivered attention abstracts; 20 date-routed unread plus a separately linked superset of 27 plausible unread arXiv IDs remain.
- Local finalization script first attempted unavailable python executable; corrected to python3 without repeating retrieval or PDF calls. The initial validation pass preceded ledger refresh; final validation is rerun on the completed file.

No qualifying same-day Agentic Graphics paper was verified in the browsed source set.
Coverage is limited to the sources and queries below; unpublished or unindexed papers may be missing.

## already_reported (0)

## same_day_new (0)

## same_day_updates (0)

## late_discovery (14)

### [ManimCode: Learning Visual Self-Correction for Educational Animation](https://arxiv.org/abs/2611.08294)
core | High | new_relative_to_snapshot
Application: 2D Graphics, Dynamic / Animation and temporal scene; operations: Generation
Learns the full visual self-correction loop in a small multimodal model from 24,034 verified trajectories; SFT+RL reaches 96.6%/97.0% render success on two scene benchmarks.
Scope: A trained multimodal controller emits executable Manim programs and rewrites them in response to rendered-frame critique, layout diagnostics and execution errors.
Limits: Render success does not ensure educational correctness. Appendix C.5 shows oscillating overlap/clipping defects; best-candidate retention can preserve an imperfect output. Human evaluation uses one team annotator on 98 pairs and agreement is poor for small judge-score differences. RL mainly improves render success rather than quality.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Animation | Educational animations show processes unfolding over time through generated Manim scenes. ([source](https://arxiv.org/pdf/2611.08294v1), Sections 1, 4) |
| input_form | Language | Inference starts from an open request with no reference video or code. ([source](https://arxiv.org/pdf/2611.08294v1), Section 4.2, Figure 3) |
| output | Program, Rendered Media | Retains the best successfully rendered program and its video. ([source](https://arxiv.org/pdf/2611.08294v1), Sections 3.2, 4.2; Figure 3) |
| model_type | VLM | One Qwen3.5-4B model writes code and reviews sampled video frames. ([source](https://arxiv.org/pdf/2611.08294v1), Sections 4.1–4.2) |
| model_training | Supervised Fine-Tuning, RL Post-Training | Role-conditioned SFT followed by RLOO training of Reviser; LoRA hyperparameters provided. ([source](https://arxiv.org/pdf/2611.08294v1), Sections 4.1–4.2; Appendix B.2) |
| planning | Not Applicable | Scene subsystem has no explicit task-plan object; lecture plans belong to external long-form systems. Full text and plan search checked. ([source](https://arxiv.org/pdf/2611.08294v1), Section 4.2; Appendix A.3 and C.3) |
| workflow | Sequential | Write, render, review and revise repeat within ten renders. ([source](https://arxiv.org/pdf/2611.08294v1), Figure 3; Appendix A.3) |
| update_strategy | Regeneration, Candidate Selection, Rollback | Reviser rewrites full program; retains better mean-score candidate; revision base reverts to best when alignment/completeness falls over 0.5. ([source](https://arxiv.org/pdf/2611.08294v1), Section 3.2; Appendix A.3 Table 7) |
| verifier | Self, Programmatic, Environment | Same model reviews frames; layout checker reports defects; renderer reports execution errors. ([source](https://arxiv.org/pdf/2611.08294v1), Sections 3.2, 4.2; Appendix A.3) |
| feedback_assessment | Score, Diagnosis, Binary | Four 1–5 scores, specific defect critique, and render success/failure guide revisions and acceptance. ([source](https://arxiv.org/pdf/2611.08294v1), Section 3.2; Table 7) |
| feedback_observation | Visual, Structural Scene State, Runtime | Eight rendered frames, object positions and layout diagnostics at pauses, execution error e. ([source](https://arxiv.org/pdf/2611.08294v1), Section 3.2) |
| memory_time | Short-Term Memory | Tracks current and best candidates and their scores across revision calls per request. ([source](https://arxiv.org/pdf/2611.08294v1), Section 4.2; Table 7) |
| memory_reach | Global Memory | Current program, review and revision state are passed between roles of the one inference loop. ([source](https://arxiv.org/pdf/2611.08294v1), Sections 3.2, 4.1; Table 7) |
| action_type | Code/Script | Writer and Reviser emit full Manim programs for execution. ([source](https://arxiv.org/pdf/2611.08294v1), Section 3.2) |
| graphics_software | General-Purpose | Native ManimCE v0.19.1 Python programs and eight domain plugins. ([source](https://arxiv.org/pdf/2611.08294v1), Appendix A.2–A.3) |
| tools | Execution Utilities, Static Validator | Renderer executes programs; layout checker flags outside-frame objects, overlap and tiny labels. ([source](https://arxiv.org/pdf/2611.08294v1), Section 3.2; Table 7) |
| resources | Documentation & Rules, Examples & Trajectories | 2,219 API cards include documentation, best-practice rules and rendered example scenes; inference retrieves cards. ([source](https://arxiv.org/pdf/2611.08294v1), Section 3.1; Appendix A.2) |
| representation | Code, Pixels | Manim Python program and sampled rendered video frames. ([source](https://arxiv.org/pdf/2611.08294v1), Sections 3.2, 4.2) |

Events: [{"type": "first_submission", "value": "2026-11-05T16:55:44+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2611.08294", "authority": "primary", "version": "v1", "local_value": "2026-11-05T10:55:44-06:00", "evidence": "Canonical submission history v1; latest and only version before cutoff.", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: ["Single backbone with explicit reviewer role makes Self versus Critic a boundary; use Self here because the same model reviews its own outputs.", "No explicit scene-task plan: do not import external lecture planning into planning cell."]

### [Parametric CAD Bench v3: Evaluating Agentic Parametric CAD Authoring from Text and Engineering Drawings](https://arxiv.org/abs/2611.02659)
core | High | new_relative_to_snapshot
Application: Static / CAD, Datasets and Benchmarks; operations: Generation, Reconstruction, Editing
A versioned 100-task CAD benchmark tests native document structure and dimensional consistency alongside geometry, with transparent evaluation of 13 complete agent systems.
Scope: Demonstrated evaluation of coding agents operating on native CAD documents and feature trees, not merely potentially transferable coding ability.
Limits: Only curated single-body FreeCAD parts; no assembly mating, FEM or manufacturing certification. Create-and-edit does not prove reuse of base history. Reference-based heuristics may penalize valid alternative constructions. Single trials, provider changes and differing harnesses confound model comparisons. Internal agent mechanisms are sparsely reported.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Modeling | Create, edit and reconstruct mechanical CAD parts. ([source](https://arxiv.org/pdf/2611.02659v1), Section 3 Table 1) |
| input_form | Language, Image | Text descriptions and edit instructions; engineering drawing images transported through multimodal bridge. ([source](https://arxiv.org/pdf/2611.02659v1), Section 3.1; Section 5.2) |
| output | Program, Graphics Artifact | Required answer.py and answer.FCStd, or base and edited native models. ([source](https://arxiv.org/pdf/2611.02659v1), Appendices B–C pp.19,24) |
| model_type | VLM | Opus 5.5 receives complete image payloads through a multimodal observation channel. ([source](https://arxiv.org/pdf/2611.02659v1), Section 5.2 pp.12–13) |
| model_training | Not Reported | Reports provider models, versions and serving configurations, not adaptation details. Full text and fine-tun search inspected. ([source](https://arxiv.org/pdf/2611.02659v1), Sections 5–6; Appendix A) |
| planning | Not Reported | No explicit agent task-plan mechanism described; planning search finds no matches. ([source](https://arxiv.org/pdf/2611.02659v1), Sections 4–6; Appendix A) |
| workflow | Not Reported | Interactive executions and configuration versions reported but internal agent scheduling is not specified. ([source](https://arxiv.org/pdf/2611.02659v1), Sections 4–5; Appendix A) |
| update_strategy | Not Reported | Two output documents do not prove reuse or preserved history; no repair mechanism found. ([source](https://arxiv.org/pdf/2611.02659v1), Sections 3.1, 5–6) |
| verifier | Not Reported | Separate held-back verifier scores submitted artifacts; no loop-internal checking implementation documented. ([source](https://arxiv.org/pdf/2611.02659v1), Sections 4.1–4.2) |
| feedback_assessment | Not Reported | Continuous task reward is final evaluation; feedback search only finds related work. ([source](https://arxiv.org/pdf/2611.02659v1), Section 4.2; Section 6) |
| feedback_observation | Not Reported | Drawing inputs are documented, but observations driving agent revision are not. ([source](https://arxiv.org/pdf/2611.02659v1), Sections 4–5) |
| memory_time | Not Reported | Saved logs are reproducibility artifacts, not a described agent memory. Memory search has no matches. ([source](https://arxiv.org/pdf/2611.02659v1), Sections 4–6; Appendix A) |
| memory_reach | Not Reported | No local/shared agent memory architecture documented. ([source](https://arxiv.org/pdf/2611.02659v1), Sections 4–6; Appendix A) |
| action_type | Code/Script | Write FreeCAD 1.1.0 Python script to answer.py. ([source](https://arxiv.org/pdf/2611.02659v1), Appendices B–C) |
| graphics_software | General-Purpose | FreeCAD native Python API and PartDesign documents in pinned runtime. ([source](https://arxiv.org/pdf/2611.02659v1), Sections 1, 4.1; Appendix B) |
| tools | Execution Utilities | Agent executes scripts and transports image content through shell output. ([source](https://arxiv.org/pdf/2611.02659v1), Sections 3.2, 5.2; Appendix B) |
| resources | Not Reported | No reusable documentation/example retrieval described for evaluated agents; references held back. ([source](https://arxiv.org/pdf/2611.02659v1), Sections 4–6; Appendix A) |
| representation | Code, Geometry | FreeCAD Python programs and native B-rep solids with feature trees. ([source](https://arxiv.org/pdf/2611.02659v1), Sections 1, 3.1; Appendix B) |

Events: [{"type": "first_submission", "value": "2026-11-02T07:19:55+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2611.02659", "authority": "primary", "version": "v1", "local_value": "2026-11-02T01:19:55-06:00", "evidence": "Canonical v1 history; the September 24 experimental snapshot is not this submission event.", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: ["Benchmark final verification is outside selected agents' feedback loop; unknown internals remain Not Reported rather than copying grader labels."]

### [GREP: Grounding Generated Room Evaluation in Principles](https://arxiv.org/abs/2611.05802)
core | High | new_relative_to_snapshot
Application: Static / Scene, Datasets and Benchmarks; operations: Auditing
Principle-grounded agentic room auditing with adaptive geometric/visual evidence; reports align with human majority on 13/15 pairs and improve a small downstream refinement study.
Scope: Evaluation agent autonomously chooses scene checks and operates geometric measurement and camera/render tools in a 3D environment. Auditing is the principal contribution, not the separate placement generator.
Limits: Single main judge may favor its own family; six-scene human validation has non-independent pair comparisons. Discovery covers instantiated checks, not all possible defects. Budget exhaustion forces binary judgments or default-valid decisions. Refinement uses a distinct score protocol and only five scenes; it is not simply normalized main GREP score.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Not Applicable | Inspects a fixed scene; does not model, animate, simulate or create visualization as its end task. ([source](https://arxiv.org/pdf/2611.05802v1), Sections 3, 5) |
| input_form | 3D Representation, Language | Scene assets, geometry, poses/scales and intended use/context supplied to evaluation. ([source](https://arxiv.org/pdf/2611.05802v1), Sections 3.1, A.1) |
| output | Not Applicable | Outputs diagnostic reports, scores and inspection records, not content specifications or authored graphics. ([source](https://arxiv.org/pdf/2611.05802v1), Section 3.4) |
| model_type | VLM | VLM inspects views and context; GPT-5.6 Sol used as evaluation agent. ([source](https://arxiv.org/pdf/2611.05802v1), Sections 3.1, 4.1.1) |
| model_training | Not Reported | Model and inference settings given; no adaptation statement found in full text or training/fine-tun/pretrained search. ([source](https://arxiv.org/pdf/2611.05802v1), Sections 3–5; Appendix C.3) |
| planning | PO-2 | VLM instantiates checks with targets/evidence requirements within fixed types; later requests extend observation goals. ([source](https://arxiv.org/pdf/2611.05802v1), Appendix A.2–A.4) |
| workflow | Graph-Structured | Deterministic conclusive paths bypass VLM; inconclusive checks branch to evidence collection and metric-specific adjudication loops. ([source](https://arxiv.org/pdf/2611.05802v1), Figure 7; Table 4) |
| update_strategy | Replanning | Evaluator requests missing observations; check goals supplemented by later requests and further camera acquisition. ([source](https://arxiv.org/pdf/2611.05802v1), Appendix A.3–A.4) |
| verifier | Critic, Programmatic | Metric evaluator judges whether views reveal needed properties; deterministic gate checks existence/decodability/nonblank observations. ([source](https://arxiv.org/pdf/2611.05802v1), Appendix A.3–A.5) |
| feedback_assessment | Binary, Diagnosis | Sufficient/insufficient decisions and missing-feature requests determine further acquisition. ([source](https://arxiv.org/pdf/2611.05802v1), Section 3.3; Appendix A.3) |
| feedback_observation | Visual, Structural Scene State | Evidence packets carry views, distances, relative orientation, geometry and gaps. ([source](https://arxiv.org/pdf/2611.05802v1), Section 3.3; Appendix A.3) |
| memory_time | Short-Term Memory | Retains acquired views for later checks; Function checks reuse group evidence bank in evaluation episode. ([source](https://arxiv.org/pdf/2611.05802v1), Section 3.3; Appendix A.3–A.4) |
| memory_reach | Local Memory | Function evidence bank scoped to object group; other metrics have own evidence scopes. ([source](https://arxiv.org/pdf/2611.05802v1), Table 4; Appendix A.3) |
| action_type | Tool/Function Call | Selects measurement, view retrieval and rendering operations. ([source](https://arxiv.org/pdf/2611.05802v1), Section 3.3) |
| graphics_software | Agent-Adapted | Custom evidence-acquisition tools around Blender EEVEE with deterministic camera candidates and VLM repair proposals. ([source](https://arxiv.org/pdf/2611.05802v1), Appendix C.3 and A.4) |
| tools | Execution Utilities, Static Validator, Graphics Operations | Renders evidence, checks geometric predicates and measures spatial relations, changes camera for targeted views. ([source](https://arxiv.org/pdf/2611.05802v1), Section 3.3; Appendix A) |
| resources | Assets, Documentation & Rules | Usable-side reference from asset catalog/previews; fixed check types and evidence requirements guide inspection. ([source](https://arxiv.org/pdf/2611.05802v1), Appendix A.2–A.3) |
| representation | Geometry, Pixels | Asset meshes, transforms and rendered 768-square views with smaller previews. ([source](https://arxiv.org/pdf/2611.05802v1), Section 3.3; Appendix C.3) |

Events: [{"type": "first_submission", "value": "2026-11-04T01:19:12+00:00", "precision": "timestamp", "timezone": "UTC", "local_value": "2026-11-03T19:19:12-06:00", "version": "v1", "primary_url": "https://arxiv.org/abs/2611.05802", "authority": "primary", "evidence": "Canonical v1 submission history; latest before cutoff.", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: ["Auditing produces diagnostic records, which existing task/output axes do not cleanly represent; propose monitoring an audit-report output label, without changing frozen codebook.", "Replanning here is evidence acquisition, not scene layout authoring."]

### [CADFather: Autonomous CAD Reconstruction through Coordinated Tool Use](https://arxiv.org/abs/2610.09127)
core | High | new_relative_to_snapshot
Application: Static / CAD; operations: Reconstruction
Coordinates complementary CAD proposal and optimization tools under visual, geometric and runtime feedback while retaining alternative programs and a protected best result.
Scope: VLM explicitly chooses candidate CAD programs, reconstruction tools, sampling counts and stopping; its choices operate on executable parametric geometry.
Limits: Limited operation library and budgets; optimization cannot repair wrong topology. Metrics assess fit/validity rather than engineering intent or original history. Baseline validity definitions and subsets differ. Tool ablations do not isolate assistant selection policy or equalize consumed compute; quoted token costs exclude geometric processing.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Modeling | Reconstruct executable CAD program from target mesh. ([source](https://arxiv.org/pdf/2610.09127v1), Section 3.1) |
| input_form | 3D Representation | Input is target mesh M-star; rendered views are generated internally. ([source](https://arxiv.org/pdf/2610.09127v1), Section 3.1) |
| output | Program, Graphics Artifact | Final CAD program and mesh of protected best candidate. ([source](https://arxiv.org/pdf/2610.09127v1), Figure 1; Sections 3.5, 6) |
| model_type | VLM | Vision-language assistant Qwen3.8-27B inspects labeled renders and numeric tables. ([source](https://arxiv.org/pdf/2610.09127v1), Sections 3.3, 4.1) |
| model_training | Off-the-Shelf | Both models frozen; generation and assistant require no additional training. ([source](https://arxiv.org/pdf/2610.09127v1), Section 4.1 p.8) |
| planning | Not Applicable | One short current-step rationale and up to four action calls; no explicit multi-step task-plan representation. ([source](https://arxiv.org/pdf/2610.09127v1), Section 3.3; full-text plan search) |
| workflow | Graph-Structured | Each candidate carries parent; extensions and optimizer results become children; earlier branches remain selectable. ([source](https://arxiv.org/pdf/2610.09127v1), Sections 3.2, 3.4) |
| update_strategy | Local Patch, Candidate Selection, Rollback | Appends operations or changes parameters; protected best selected by score; can revisit earlier valid candidate or root. ([source](https://arxiv.org/pdf/2610.09127v1), Sections 3.2, 3.4–3.5) |
| verifier | Self, Programmatic, Environment | Same assistant visually accepts proposals; program checks watertightness/volume and metrics; executor reports build failure and timeout. ([source](https://arxiv.org/pdf/2610.09127v1), Sections 3.5–3.6) |
| feedback_assessment | Score, Binary, Diagnosis | IoU/GMS scores, valid/invalid and accept/reject decisions, and reasons for unavailable/malformed actions enter later decisions. ([source](https://arxiv.org/pdf/2610.09127v1), Sections 3.5–3.6) |
| feedback_observation | Visual, Structural Scene State, Runtime | Target/candidate renders, operation counts and geometry measures, failed execution reports. ([source](https://arxiv.org/pdf/2610.09127v1), Sections 3.3, 3.5–3.6) |
| memory_time | Short-Term Memory | Pool and transcript of executed requests retained across steps for each target part; old renders omitted. ([source](https://arxiv.org/pdf/2610.09127v1), Sections 3.2–3.3) |
| memory_reach | Global Memory | Shared candidate representation and central pool connects assistant, executor and all tools; bounded view to assistant. ([source](https://arxiv.org/pdf/2610.09127v1), Sections 3.1–3.3) |
| action_type | Tool/Function Call | Assistant answers through act and finish function calls. ([source](https://arxiv.org/pdf/2610.09127v1), Section 3.3) |
| graphics_software | Agent-Adapted | CADENA CadQuery DSL with shared act interface for learned, algorithmic and optimization tools. ([source](https://arxiv.org/pdf/2610.09127v1), Sections 3.1, 3.3–3.4) |
| tools | Graphics Operations, Perception models, Solver Validator, Static Validator, Execution Utilities | Operation proposals, pretrained CADENA-RL, signed-distance optimizer, validity checks and execution/rendering. ([source](https://arxiv.org/pdf/2610.09127v1), Sections 3.4–3.6) |
| resources | Documentation & Rules | Persistent task/tool/cost/answer-format rules repeated each step. ([source](https://arxiv.org/pdf/2610.09127v1), Section 3.3 Figure 2) |
| representation | Code, Geometry, Pixels | CAD DSL programs, executed meshes/solids and candidate render images. ([source](https://arxiv.org/pdf/2610.09127v1), Sections 3.1–3.3) |

Events: [{"type": "first_submission", "value": "2026-10-06T21:20:59+00:00", "precision": "timestamp", "timezone": "UTC", "local_value": "2026-10-06T16:20:59-05:00", "version": "v1", "primary_url": "https://arxiv.org/abs/2610.09127", "authority": "primary", "evidence": "Canonical v1 history. Previously unresolved frozen-history backlog, not a seven-day or same-day event.", "prior_event_status": "already_seen"}]
Taxonomy deltas: ["Reactive one-step function choice is not an explicit task plan; preserve distinction despite authors using planning broadly.", "Global candidate pool exposes only bounded assistant context; this is not unrestricted global access."]

### [Code2Worlds-2: Physically Plausible Agent Harness for Embodied World Simulation](https://arxiv.org/abs/2610.17651)
core | High | new_relative_to_snapshot
Application: Dynamic / Physical simulation and effects; operations: Generation, Editing
An executable-world compiler and measured-physics repair harness extend visual 4D generation; fixed-source robust success rises from 45/180 to 60/180, with uncertainty explicitly reported.
Scope: Physical compiler/refiner emits specifications that change mass, friction, collision preparation and dynamics of executable simulated worlds under measured feedback.
Limits: Only 12 source cases and three matched prompts. The 8.3-point RTS gain has clustered interval −11.1 to 28.9 points; navigation regresses. State-only feedback outperforms fusion under fixed budgets. Limited articulation, general grasping and indoor wall collision remain open. Reference-package 225/225 readiness is not method success. Physical attributes are estimates, not measurements; fixed-source controller training/model identity are underspecified.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Simulation | Convert visual world to physically executable rigid/articulated simulation. ([source](https://arxiv.org/pdf/2610.17651v1), Sections 3–4) |
| input_form | 3D Representation, Language | Receives fixed visual scene and public task specification, not solved simulator world. ([source](https://arxiv.org/pdf/2610.17651v1), Appendix C.5) |
| output | Structured Specification, Graphics Artifact | Typed physical plan/dynamics overlay and exported world package containing MJCF and assets. ([source](https://arxiv.org/pdf/2610.17651v1), Sections 3, 4.2; Appendix C.5) |
| model_type | VLM | Physical compiler infers properties from geometry rendering, names and dimensions; VLM visual inputs explicit. ([source](https://arxiv.org/pdf/2610.17651v1), Appendix C.2, C.5; Section 3.1.2) |
| model_training | Not Reported | No training/adaptation description for selected compiler/refiner after full text and fine-tun/training search. ([source](https://arxiv.org/pdf/2610.17651v1), Sections 3,5; Appendices C–E) |
| planning | Not Applicable | Physical-plan JSON specifies properties/bindings, not an ordered task-action plan. Inherited generation planning is outside target. ([source](https://arxiv.org/pdf/2610.17651v1), Appendix C.5–C.6) |
| workflow | Sequential | Compile, simulate, critique, refine in an ordered repeated loop. ([source](https://arxiv.org/pdf/2610.17651v1), Figure 3; Section 3) |
| update_strategy | Regeneration | Return a full corrected plan in the same DSL, constrained to permitted physical fields. ([source](https://arxiv.org/pdf/2610.17651v1), Appendix C.6) |
| verifier | Critic, Programmatic, Environment | Visual critic returns issues; code evaluates measured physical predicates; compilation/execution diagnostics returned. ([source](https://arxiv.org/pdf/2610.17651v1), Section 3.2.1; Appendix C.4–C.6) |
| feedback_assessment | Binary, Diagnosis | Fused validity flag, issues and feedback_for_dyn_program returned to refiner. ([source](https://arxiv.org/pdf/2610.17651v1), Section 3.2.1; Appendix C.4) |
| feedback_observation | Visual, Structural Scene State, Runtime | Sampled frames, displacement/contact/speed records, execution errors accompany previous plan. ([source](https://arxiv.org/pdf/2610.17651v1), Appendix C.4, C.6) |
| memory_time | Short-Term Memory | Each repair round receives previous plan and structured diagnostics envelope. ([source](https://arxiv.org/pdf/2610.17651v1), Appendix C.6) |
| memory_reach | Local Memory | Repair model receives its stage-specific previous-plan target and evidence envelope. ([source](https://arxiv.org/pdf/2610.17651v1), Appendix C.6) |
| action_type | Structured Specification | Model returns typed JSON physical plan and dynamics blocks. ([source](https://arxiv.org/pdf/2610.17651v1), Appendix C.5–C.7) |
| graphics_software | Agent-Adapted | Custom compiler maps agent DSL/Embodied World Graph to MuJoCo MJCF and Blender dynamics. ([source](https://arxiv.org/pdf/2610.17651v1), Section 3; Appendix C) |
| tools | Graphics Operations, Solver Validator, Static Validator, Execution Utilities | CoACD and ray-casting construct collider geometry; MuJoCo settles/rolls out worlds; checks validation conditions; compiles and exports. ([source](https://arxiv.org/pdf/2610.17651v1), Sections 3.1–3.2) |
| resources | Documentation & Rules | Material density bounds and physical DSL bounds, allowed field rules explicitly supplied. ([source](https://arxiv.org/pdf/2610.17651v1), Appendix C.2, C.5–C.6) |
| representation | Geometry, Dynamic State, Code, Pixels | World graph meshes/colliders, physical rollout state, JSON/MJCF executable descriptions, rendered observations. ([source](https://arxiv.org/pdf/2610.17651v1), Section 3; Appendix C) |

Events: [{"type": "first_submission", "value": "2026-10-13T03:30:40+00:00", "precision": "timestamp", "timezone": "UTC", "local_value": "2026-10-12T22:30:40-05:00", "version": "v1", "primary_url": "https://arxiv.org/abs/2610.17651", "authority": "primary", "evidence": "Official metadata and canonical v1 history; newly completed frozen-history backlog, outside seven-day window.", "prior_event_status": "already_seen"}]
Taxonomy deltas: ["A physical-plan data structure is a content specification rather than necessarily a task plan.", "Retain model/configuration omissions; do not transfer Fable-5 upstream backbone into all physical refinement roles."]

### [CADForge: Agentic Single-View CAD Reconstruction with Explicit Geometry Reasoning](https://arxiv.org/abs/2610.04262)
core | High | new_relative_to_snapshot
Application: Static / CAD; operations: Reconstruction
Explicit image-to-constraint-to-mathematical-parameter reasoning supports component-wise editable CAD; reports lower geometric error and 81.6k average tokens versus 331.8k for Procedura.
Scope: VLM agents plan component construction, emit mathematical and CAD programs and route visual/technical errors back to editable geometry generation.
Limits: Extreme rear/side viewpoints can prevent recovering hidden geometry. Only 200 curated examples and five human raters. CPVR counts differ by native workflow, so not strictly comparable across methods. Tool construction uses 60 separate examples; articulation/editing are qualitative extensions rather than principal evaluated tasks.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Modeling | Construct part-aware parametric CAD geometry from image. ([source](https://arxiv.org/pdf/2610.04262v1), Section 3.1) |
| input_form | Image | Given single RGB image I. ([source](https://arxiv.org/pdf/2610.04262v1), Section 3.1) |
| output | Program, Graphics Artifact | Part-wise CadQuery programs and B-reps; STEP, STL, GLB exports. ([source](https://arxiv.org/pdf/2610.04262v1), Section 3.1; Appendix C.2) |
| model_type | VLM | All roles use GPT-5.5 LLM/VLM backbone; observer and reviewer consume images, code agent receives text contract. ([source](https://arxiv.org/pdf/2610.04262v1), Section 4.1; Appendix G) |
| model_training | Off-the-Shelf | Training-free framework without specialized fine-tuning. ([source](https://arxiv.org/pdf/2610.04262v1), Sections 2,5) |
| planning | PO-2 | VLM creates ordered inventory P based on component dependencies; fixed per-component geometry/code/review stages. ([source](https://arxiv.org/pdf/2610.04262v1), Section 3.2; Appendix G.1) |
| workflow | Graph-Structured | Reviewer routes geometry errors to observer/solver and modeling errors to code stage; runtime repair has separate loop. ([source](https://arxiv.org/pdf/2610.04262v1), Section 3.4.1; Figure 1) |
| update_strategy | Regeneration, Local Patch | Complete replacement observation and fresh component script for review corrections; technical repair changes only fragile operation preserving geometry. ([source](https://arxiv.org/pdf/2610.04262v1), Appendix G.2, G.4–G.5) |
| verifier | Critic, Programmatic, Environment | Separate Review Agent compares reference and renders; static validity and execution failures drive repair. ([source](https://arxiv.org/pdf/2610.04262v1), Section 3.4.1; G.5–G.6) |
| feedback_assessment | Binary, Diagnosis | Pass versus geometry/modeling/mixed errors with one-to-three correction sentences; execution success/failure. ([source](https://arxiv.org/pdf/2610.04262v1), G.5–G.6) |
| feedback_observation | Visual, Runtime | Reference/front/oblique comparison images; execution or static validation error text. ([source](https://arxiv.org/pdf/2610.04262v1), C.2; G.5–G.6) |
| memory_time | Short-Term Memory | Accepted component dictionaries accumulate within reconstruction and are retrieved for later parts. ([source](https://arxiv.org/pdf/2610.04262v1), Section 3.5 Eq.5) |
| memory_reach | Local Memory | Reference parameters retrieved specifically for geometry programming and code synthesis; reviewer gets comparison image and target. ([source](https://arxiv.org/pdf/2610.04262v1), Section 3.5; G.2–G.4) |
| action_type | Code/Script | Emits mathematical Python solver and executable CadQuery script. ([source](https://arxiv.org/pdf/2610.04262v1), Sections 3.3.2–3.4.1) |
| graphics_software | Agent-Adapted | Dedicated robust CadQuery helper library prepended to execution namespace with compact agent API manifest. ([source](https://arxiv.org/pdf/2610.04262v1), Appendix C.3) |
| tools | Graphics Operations, Execution Utilities, Static Validator | Robust solid construction helpers, local runner/VTK render, syntax and geometry validity checks. ([source](https://arxiv.org/pdf/2610.04262v1), C.2–C.3; G.5) |
| resources | Documentation & Rules, Examples & Trajectories | API manifest includes function signatures, selection rules and concise usage examples in generation/repair prompts. ([source](https://arxiv.org/pdf/2610.04262v1), C.3 pp.18–19) |
| representation | Code, Geometry, Pixels | CadQuery scripts, B-rep components and two-view renderings. ([source](https://arxiv.org/pdf/2610.04262v1), Sections 3.1,3.4; C.2) |

Events: [{"type": "first_submission", "value": "2026-10-03T03:39:54+00:00", "precision": "timestamp", "timezone": "UTC", "version": "v1", "local_value": "2026-10-02T22:39:54-05:00", "primary_url": "https://arxiv.org/abs/2610.04262", "authority": "primary", "evidence": "Canonical v1 history; newly read historical pending item, not a target-day/catch-up event.", "prior_event_status": "already_seen"}]
Taxonomy deltas: ["Reviewer is a dedicated role and thus Critic; do not infer separate model weights.", "Cross-run toolkit improvement is outside task-time memory classification."]

### [AgiWorld: An Agentic Video World Model for Building Persistent Worlds](https://arxiv.org/abs/2611.02341)
core | High | new_relative_to_snapshot
Application: Dynamic / Animation and temporal scene; operations: Generation
Co-designs agent-level world/journey planning with a persistent geometry-grounded video generator; explicit rollback and replan align intended world with actual generated content.
Scope: Agent explicitly designs world content and temporal journey, emits camera trajectories/prompts, and revises them from generated scene evidence.
Limits: Agent evaluation is mostly qualitative examples/ablations; main quantitative gains concern world-model benchmarks. Generated scenes are static and camera-controlled. Geometry errors can close doorways; failed path bounds can be accepted after three corrections. Regeneration is capped and persistent faults are only reported. Internal video training collection and unreleased full guidelines limit replication.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Animation | Long video journey with planned per-frame camera movement and temporal stages. ([source](https://arxiv.org/pdf/2611.02341v1), Section 2.1; Appendix A.4) |
| input_form | Image, Language | Single image I0 and free-form natural-language instruction g0. ([source](https://arxiv.org/pdf/2611.02341v1), Section 2.1) |
| output | Rendered Media | Output long video v that starts from image and explores world. ([source](https://arxiv.org/pdf/2611.02341v1), Section 2.1) |
| model_type | VLM | Both functions use one multimodal GPT-6-Astra with geometric tools. ([source](https://arxiv.org/pdf/2611.02341v1), Appendix A.1 p.19) |
| model_training | Not Reported | Controller model named; adaptation not stated. Training/fine-tuning is explicitly for Wan-based world model. ([source](https://arxiv.org/pdf/2611.02341v1), Appendix A.1; Section 5.2) |
| planning | PO-2 | Explicit ordered stages and 60-second waypoint plan selected by model inside fixed schemas/triggers. ([source](https://arxiv.org/pdf/2611.02341v1), Section 3.1; A.4 Tables 3–4) |
| workflow | Graph-Structured | Conditional revision, refresh, regeneration and replan invoke different subroutines with validation retries. ([source](https://arxiv.org/pdf/2611.02341v1), Algorithm 1; Table 3) |
| update_strategy | Regeneration, Local Patch, Replanning, Rollback | Reject chunk then restore memory/state, generate anew; apply small layout edits; regenerate route/stage plan. ([source](https://arxiv.org/pdf/2611.02341v1), Algorithm 1; A.6–A.7) |
| verifier | Self, Programmatic | Director reviews its generated chunk; tools check geometry, schemas and motion bounds and return errors. ([source](https://arxiv.org/pdf/2611.02341v1), A.1, A.6) |
| feedback_assessment | Binary, Diagnosis | Element absent/different/confirmed, mismatch severity and check violations cause revision or regeneration. ([source](https://arxiv.org/pdf/2611.02341v1), A.6 pp.23–24) |
| feedback_observation | Visual, Structural Scene State | Composite frame image, map and numeric camera-height/nearest-solid measurements. ([source](https://arxiv.org/pdf/2611.02341v1), Table 5; A.6) |
| memory_time | Short-Term Memory | State and complete video/geometry history retained over rollout; retired elements remain recorded. ([source](https://arxiv.org/pdf/2611.02341v1), Sections 2.2,3.4) |
| memory_reach | Global Memory | Shared spatial memory and world state used across director and state-update roles, with common geometric tools. ([source](https://arxiv.org/pdf/2611.02341v1), Section 2.2; Table 5) |
| action_type | Structured Specification | JSON schemas encode layout, stage edits, waypoints and start/middle/end prompts. ([source](https://arxiv.org/pdf/2611.02341v1), A.1, A.4–A.5) |
| graphics_software | Agent-Ready | World model and agent co-designed around metric camera and structured prompt interface with shared memory. ([source](https://arxiv.org/pdf/2611.02341v1), Sections 2–4) |
| tools | Perception models, Static Validator, Graphics Operations | World-model generator and geometry estimator; deterministic schema/trajectory checks; geometric projection and camera-path interpolation. ([source](https://arxiv.org/pdf/2611.02341v1), Sections 3.2,4; Table 5) |
| resources | Documentation & Rules | Shared world-model capabilities specification and step guidelines instruct camera/prompt practice. ([source](https://arxiv.org/pdf/2611.02341v1), A.1, A.4 Table 6) |
| representation | Geometry, Pixels | Metric point cloud and coarse 3D semantic layout, rendered video frames. ([source](https://arxiv.org/pdf/2611.02341v1), Sections 3.1–3.2,4.1) |

Events: [{"type": "first_submission", "value": "2026-11-02T00:39:40+00:00", "precision": "timestamp", "timezone": "UTC", "local_value": "2026-11-01T18:39:40-06:00", "version": "v1", "primary_url": "https://arxiv.org/abs/2611.02341", "authority": "primary", "evidence": "Official Atom and canonical only-version history.", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: ["Paper's long-term world consistency is within-run memory, not codebook Long-Term Memory.", "Full system generates video; structured state/waypoints are internal control outputs, not separately claimed exposed content products."]

### [LongBanana: An Expert-Verified Benchmark for Long-Context Multi-Reference Image Synthesis](https://arxiv.org/abs/2611.06856)
core | High | new_relative_to_snapshot
Application: 2D Graphics, Datasets and Benchmarks; operations: Generation
Auditable dense-reference benchmark and agent orchestration study; OpenClaw+RPR reaches 78.4 checklist average versus 74.6 for a structurally privileged non-agent baseline.
Scope: Evaluated harness agent selects references and calls an image generator/editor, then reviews draft pixels and revises requests; direct operation on graphics artifacts.
Limits: Only 90 high-density 2D cases, expensive annotation and backbone-dependent judging. RPR gains are harness-dependent; task pass rates can decline. Agent call budgets, costs, detailed prompt templates and reproducible environment files omitted. Appendix checklist says code/data reproduction not publicly available despite abstract project-release statement; availability not independently verified.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Visualization | Compose advertisements, posters, editorial panels and reference-grounded visual scenes. ([source](https://arxiv.org/pdf/2611.06856v1), Sections 1–2; Figures 9,13) |
| input_form | Language, Image | Structured instruction and about 32 reference images including distractors. ([source](https://arxiv.org/pdf/2611.06856v1), Section 2.1) |
| output | Rendered Media | One final synthesized image. ([source](https://arxiv.org/pdf/2611.06856v1), Section 2.1; Figure 18) |
| model_type | VLM | Sonnet agent observes reference images and generated drafts to reason and revise. ([source](https://arxiv.org/pdf/2611.06856v1), Section 4.1; C.1; Figure 18) |
| model_training | Not Reported | Controller model and harness versions named but no adaptation statement; targeted training/fine-tun search inspected. ([source](https://arxiv.org/pdf/2611.06856v1), Appendix C.1; checklist pp.40–42) |
| planning | PO-2 | Plan–Exec builds scene plan/prompt schedule and executable subgoals within RPR stages. ([source](https://arxiv.org/pdf/2611.06856v1), D.2 Figure 18) |
| workflow | Sequential | Explicitly describes RPR as serial workflow of evidence grounding, plan execution and reflection with repair loop. ([source](https://arxiv.org/pdf/2611.06856v1), Section 1 p.3; D.2) |
| update_strategy | Regeneration | Agent revises prompts and invokes generation/editing backend again on drafts. ([source](https://arxiv.org/pdf/2611.06856v1), Sections 4.1,4.3; Figure 18) |
| verifier | Self | Agent-directed draft review detects missing content/wrong bindings. ([source](https://arxiv.org/pdf/2611.06856v1), D.2 Figure 18) |
| feedback_assessment | Diagnosis | Detects missing content and wrong bindings to guide prompt repair. ([source](https://arxiv.org/pdf/2611.06856v1), D.2 Figure 18) |
| feedback_observation | Visual | Reflect inspects draft images and relevant reference evidence. ([source](https://arxiv.org/pdf/2611.06856v1), Section 4.1; D.2) |
| memory_time | Short-Term Memory | Harness maintains reference state and records revisions across synthesis steps. ([source](https://arxiv.org/pdf/2611.06856v1), Section 1 p.3; Figure 18) |
| memory_reach | Global Memory | Shared agent state connects ReAct, Plan–Exec and Reflect in single orchestrator. ([source](https://arxiv.org/pdf/2611.06856v1), D.2 Figure 18) |
| action_type | Tool/Function Call | Harness calls reference, image-generation, file and prompt tools. ([source](https://arxiv.org/pdf/2611.06856v1), C.1 p.33) |
| graphics_software | Agent-Adapted | Wraps fixed image generator with agent harness maintaining evidence and revision state. ([source](https://arxiv.org/pdf/2611.06856v1), Sections 1,4.1) |
| tools | Perception models, Static Validator, Execution Utilities | Generation harness calls OCR/count/layout, reference browsing, image-generation and file/prompt-management tools. ([source](https://arxiv.org/pdf/2611.06856v1), C.1) |
| resources | Assets | Reference inventory repeatedly browsed and retrieved across generation stages. ([source](https://arxiv.org/pdf/2611.06856v1), Section 1; D.2) |
| representation | Pixels | Reference and draft images; no editable vector or 3D output. ([source](https://arxiv.org/pdf/2611.06856v1), Sections 1,4.1) |

Events: [{"type": "first_submission", "value": "2026-11-04T18:11:56+00:00", "precision": "timestamp", "timezone": "UTC", "version": "v1", "local_value": "2026-11-04T12:11:56-06:00", "primary_url": "https://arxiv.org/abs/2611.06856", "authority": "primary", "evidence": "Official metadata and canonical v1 history; conference label not used as date.", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: ["Generic raster composition does not fit task axis perfectly; Visualization chosen for poster/editorial/product communication, not by mere existence of rendered pixels.", "Final rubric scores/critics must not be copied into RPR generation feedback."]

### [NeoWorld-Pro: Programming Interactive Scenes from Monocular Images for Embodied Simulation](https://arxiv.org/abs/2608.24212)
core | High | new_relative_to_snapshot
Application: Dynamic / Articulated assets; operations: Reconstruction
Zero-shot executable articulated reconstruction with both visual and physics feedback; v3 reports 11.83% joint miss rate and explicit stability/actuation improvements.
Scope: Object-level MLLM directly writes and corrects executable geometry/articulation programs from simulator-measured defects.
Limits: Only rigid/articulated quasi-static physics and scenes with fewer than ten objects. No deformable media. Runtime budgets, prompts, memory handling and numerical thresholds incompletely specified; claimed Appendix A.1 is not included in this 13-page PDF. Scene CEM results must not be attributed solely to object-level MLLM.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Modeling | Reconstruct articulated object's part geometry, joints and properties. ([source](https://arxiv.org/pdf/2608.24212v3), Section 3.2) |
| input_form | Image | Segmented object crop from single RGB input. ([source](https://arxiv.org/pdf/2608.24212v3), Section 3.2 step 2) |
| output | Program, Graphics Artifact | Executable Blender programs compiled to articulated URDF assets. ([source](https://arxiv.org/pdf/2608.24212v3), Sections 3.1–3.2) |
| model_type | VLM | MLLM Programmer/Reasoner uses input crop, renderings and simulation frames. ([source](https://arxiv.org/pdf/2608.24212v3), Section 3.2) |
| model_training | Off-the-Shelf | Zero-shot code synthesis, commonsense priors rather than dataset-specific training. ([source](https://arxiv.org/pdf/2608.24212v3), Introduction p.2) |
| planning | Not Applicable | Three prescribed synthesis stages; scene hierarchy is a content representation, no explicit object-action task plan. ([source](https://arxiv.org/pdf/2608.24212v3), Section 3.2; full-text plan search) |
| workflow | Sequential | Sequential geometry, articulation and URDF-export scripts; runtime repair then render critic then physical validation. ([source](https://arxiv.org/pdf/2608.24212v3), Section 3.2) |
| update_strategy | Local Patch | Edits code and changes selected torque, damping and mass parameters after physical failures. ([source](https://arxiv.org/pdf/2608.24212v3), Section 3.2; Figure 3) |
| verifier | Critic, Programmatic, Environment | MLLM-Critic compares images; numerical criteria accept trajectories; execution failures cause debugging. ([source](https://arxiv.org/pdf/2608.24212v3), Section 3.2 pp.5–6) |
| feedback_assessment | Binary, Diagnosis | Tests accepted/rejected numerically; Reasoner diagnoses failure and proposes corrections. ([source](https://arxiv.org/pdf/2608.24212v3), Section 3.2 p.6) |
| feedback_observation | Visual, Structural Scene State, Runtime | Rendered comparison frames, trajectory measurements and script execution failures. ([source](https://arxiv.org/pdf/2608.24212v3), Section 3.2) |
| memory_time | Not Reported | Code reuse and iterative refinement stated but no retained context, memory architecture or lifetime specified. ([source](https://arxiv.org/pdf/2608.24212v3), Entire method pp.4–8; memory/history search) |
| memory_reach | Not Reported | No store-access boundaries or sharing of retained state specified. ([source](https://arxiv.org/pdf/2608.24212v3), Section 3; memory/history search) |
| action_type | Code/Script | Blender Python geometry, articulation and URDF export scripts. ([source](https://arxiv.org/pdf/2608.24212v3), Section 3.2 step 2) |
| graphics_software | General-Purpose | Direct executable Blender Python and standard URDF; no agent-specific authoring operation API reported. ([source](https://arxiv.org/pdf/2608.24212v3), Section 3.2) |
| tools | Graphics Operations, Solver Validator, Execution Utilities | CoACD collision decomposition, Blender execution/rendering, Isaac Sim gravity and actuation rollouts. ([source](https://arxiv.org/pdf/2608.24212v3), Section 3.2) |
| resources | Not Reported | Avoids asset database dependence; no accessed examples or API-document retrieval specified. ([source](https://arxiv.org/pdf/2608.24212v3), Introduction and Section 3; prompt/documentation search) |
| representation | Code, Geometry, Dynamic State, Pixels | Scripts/URDF, generated part geometry, simulated joint trajectories and rendered frames. ([source](https://arxiv.org/pdf/2608.24212v3), Sections 3.1–3.2) |

Events: [{"type": "first_submission", "value": "2026-08-25T08:19:39+00:00", "precision": "timestamp", "timezone": "UTC", "version": "v1", "primary_url": "https://arxiv.org/abs/2608.24212", "authority": "primary", "evidence": "Canonical history.", "prior_event_status": "not_seen_in_supplied_history"}, {"type": "revision", "value": "2026-10-20T01:44:59+00:00", "precision": "timestamp", "timezone": "UTC", "version": "v2", "primary_url": "https://arxiv.org/abs/2608.24212", "authority": "primary", "evidence": "Canonical intermediate history.", "prior_event_status": "not_seen_in_supplied_history"}, {"type": "revision", "value": "2026-11-05T06:32:22+00:00", "precision": "timestamp", "timezone": "UTC", "version": "v3", "local_value": "2026-11-05T00:32:22-06:00", "primary_url": "https://arxiv.org/abs/2608.24212", "authority": "primary", "evidence": "Latest version before cutoff, seven-day revision not same-day.", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: ["A simulator used to validate articulated modeling does not by itself add Simulation as graphics task.", "General-purpose native script interface distinguished from a custom agent-ready tool API."]

### [EvoDesign: Agentic Editable Diagram Creation via Design Expertise Evolution](https://arxiv.org/abs/2604.09568)
core | High | known_discussed_paper
Application: 2D Graphics; operations: Generation, Editing
Canvas-native authoring uses verified local repair traces to accumulate evidence-linked design expertise; 420 held-out tasks and a 36-person perceived-usability study support benefits.
Scope: Agents create and locally modify explicit diagram topology, style and layout in a rendered editable canvas under defect/critique feedback.
Limits: Canvas schema underrepresents dense mathematical/scientific visualizations and art. Reference-derived descriptions simplify topology and selection favors editability. Cold-start and cross-model memory transfer uncertain; multiple calls add latency. User study is self-report without controlled performance comparison; main refinement budget is one pass.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Visualization | Visual diagrams communicate semantic relationships and reduce cognitive load. ([source](https://arxiv.org/pdf/2604.09568v3), Section 1) |
| input_form | Language | Content c and optional natural-language requirements r. ([source](https://arxiv.org/pdf/2604.09568v3), Section 3) |
| output | Structured Specification, Graphics Artifact | D=(G,S,L) manifest renders to interactive object-editable canvas artifact. ([source](https://arxiv.org/pdf/2604.09568v3), Sections 3–4) |
| model_type | VLM | VLM backbones including GPT-5.5 power agent framework. ([source](https://arxiv.org/pdf/2604.09568v3), Section 6.1; Appendix C) |
| model_training | Not Reported | Evolution updates vector-store knowledge; no controller weight-adaptation statement after training/fine-tun searches. ([source](https://arxiv.org/pdf/2604.09568v3), Sections 4.3,6.1; Appendix C) |
| planning | PO-2 | Each role first specifies high-level structure/flow, style principles and layout organization, then instantiates fields. ([source](https://arxiv.org/pdf/2604.09568v3), Section 4.1; Appendix B.2) |
| workflow | Sequential | Structure then style then layout then render/diagnose/refine; one localized pass in main experiment. ([source](https://arxiv.org/pdf/2604.09568v3), Algorithm 1 p.15) |
| update_strategy | Local Patch | Targeted element/style/edge edits, preserving all nine nodes and eleven connections in example. ([source](https://arxiv.org/pdf/2604.09568v3), Section 4.2; Appendix E.2) |
| verifier | Critic, Programmatic | Objective checks and independent VLM-based diagnostic critique. ([source](https://arxiv.org/pdf/2604.09568v3), Section 4.2) |
| feedback_assessment | Score, Diagnosis, Binary | Weighted 0–10 objective/critique score guides refinement; prioritized defects; empty findings terminate. ([source](https://arxiv.org/pdf/2604.09568v3), Section 4.2 Eq.1; Algorithm 1) |
| feedback_observation | Visual, Structural Scene State | Rendered diagram and computed overlap/crossing/overflow/utilization facts. ([source](https://arxiv.org/pdf/2604.09568v3), Section 4.2) |
| memory_time | Short-Term Memory, Long-Term Memory | Current manifest/findings retained across repair; past supported strategies retrieved from maintained hierarchy on future tasks. ([source](https://arxiv.org/pdf/2604.09568v3), Sections 4.2–4.3; Algorithms 1–2) |
| memory_reach | Global Memory | Central M contains role-tagged expertise; structure, style, layout and refiner retrieve relevant subsets. ([source](https://arxiv.org/pdf/2604.09568v3), Section 4.3; Algorithm 1) |
| action_type | Structured Specification | Agents instantiate and update declarative shape, style, coordinates and routing fields. ([source](https://arxiv.org/pdf/2604.09568v3), Section 3; Appendix B.4) |
| graphics_software | Agent-Adapted | Excalidraw canvas wrapped in diagnostic environment, schema generation and size estimation. ([source](https://arxiv.org/pdf/2604.09568v3), Section 6.1; Appendix B.4–B.5) |
| tools | Execution Utilities, Static Validator, Graphics Operations | Renderer, objective defect checks and geometric size estimator for placement. ([source](https://arxiv.org/pdf/2604.09568v3), Sections 4.1–4.2; B.5) |
| resources | Documentation & Rules, Examples & Trajectories | Canvas API docs, design guidelines and trace-grounded sample strategies retrieved by role/context. ([source](https://arxiv.org/pdf/2604.09568v3), Figure 2; Sections 4.1,4.3) |
| representation | Layouts, Pixels | Object-level diagram graph/style/layout and rendered canvas image. ([source](https://arxiv.org/pdf/2604.09568v3), Section 3) |

Events: [{"type": "first_submission", "value": "2026-02-20T11:11:02+00:00", "precision": "timestamp", "timezone": "UTC", "version": "v1", "primary_url": "https://arxiv.org/abs/2604.09568", "authority": "primary", "evidence": "Official Atom published timestamp.", "prior_event_status": "not_seen_in_supplied_history"}, {"type": "revision", "value": "2026-10-05T17:32:59+00:00", "precision": "timestamp", "timezone": "UTC", "version": "v2", "primary_url": "https://arxiv.org/abs/2604.09568", "authority": "primary", "evidence": "Observed canonical intermediate history lines 73–74; current read remains v3.", "prior_event_status": "not_seen_in_supplied_history"}, {"type": "revision", "value": "2026-11-05T18:18:33+00:00", "precision": "timestamp", "timezone": "UTC", "version": "v3", "local_value": "2026-11-05T12:18:33-06:00", "primary_url": "https://arxiv.org/abs/2604.09568", "authority": "primary", "evidence": "Official metadata and canonical latest-version history; catch-up revision of discussed paper.", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: ["Role-tagged shared store is global with filtered retrieval; exact memory access is not uniform.", "Design specifications count as explicit design planning, but LangGraph implementation alone does not change sequential workflow classification."]

### [WorldAct: Activating Monolithic 3D Worlds into Interactive-Ready Object-Centric Scenes](https://arxiv.org/abs/2605.15843)
core | High | known_discussed_paper
Application: Static / Scene, Static / Object; operations: Reconstruction, Editing
Agent selection raises interactable object recall from 23.77% to 78.80% on six Marble scenes and 8.10% to 70.97% on four HY-World scenes, enabling object-level editing and basic simulation.
Scope: VLM decides which objects are extracted/erased and selects reconstruction views, materially controlling conversion of graphics artifacts. Core does not require an unrestricted planner or iterative repair.
Limits: Mass/friction are manually specified; rigid objects only, no articulation. Missed objects remain fused to background. About one hour per scene, ten scenes overall. Human and GPT ratings improve object quality but decrease scene-level quality. Agent lacks demonstrated iterative quality repair; downstream policy adaptations use only two objects.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Modeling | Convert fused scene to independent object assets and repaired background. ([source](https://arxiv.org/pdf/2605.15843v2), Sections 4.1,6) |
| input_form | 3D Representation | Input monolithic 3DGS scene; multi-view images are internally rendered. ([source](https://arxiv.org/pdf/2605.15843v2), Section 4.1) |
| output | Graphics Artifact | Decomposed scene with restored Gaussian background, collision mesh and clean object meshes. ([source](https://arxiv.org/pdf/2605.15843v2), Sections 4.1,4.4) |
| model_type | VLM | Qwen3.6-Plus API parses views and scores crops. ([source](https://arxiv.org/pdf/2605.15843v2), Appendix B.2–B.4) |
| model_training | Not Reported | Prompted API use stated; no controller adaptation description. Fine-tuning belongs to downstream SmolVLA policies. ([source](https://arxiv.org/pdf/2605.15843v2), Appendix B; Section 5.2) |
| planning | Not Applicable | Fixed object inventory→segment→score→select→inpaint procedure; no task-plan representation. ([source](https://arxiv.org/pdf/2605.15843v2), Appendix B Algorithm 1) |
| workflow | Sequential | Parse, initialize state, process each portable object, deduplicate masks, inpaint and return. ([source](https://arxiv.org/pdf/2605.15843v2), Appendix B Algorithm 1) |
| update_strategy | Candidate Selection | Select argmax crop score across available views. ([source](https://arxiv.org/pdf/2605.15843v2), Appendix B.4 Eq.11) |
| verifier | Self | Qwen3.6-Plus grades completeness, clarity and centeredness of candidate crops. ([source](https://arxiv.org/pdf/2605.15843v2), Appendix B.4) |
| feedback_assessment | Score | Integer 0–100 view score used in argmax selection. ([source](https://arxiv.org/pdf/2605.15843v2), Appendix B.4) |
| feedback_observation | Visual | Segmented crop images used for view suitability scoring. ([source](https://arxiv.org/pdf/2605.15843v2), Appendix B.4) |
| memory_time | Short-Term Memory | Stores object name, category, count, recognizability and processing states throughout pipeline. ([source](https://arxiv.org/pdf/2605.15843v2), Appendix B.3) |
| memory_reach | Global Memory | Memory is central representation supplying execution module after vision parses inventory. ([source](https://arxiv.org/pdf/2605.15843v2), Appendix B.3) |
| action_type | Structured Specification | Agent emits structured inventory, object prompt list and selected-view indices consumed by execution module. ([source](https://arxiv.org/pdf/2605.15843v2), Appendix B.1–B.4) |
| graphics_software | Agent-Adapted | Custom agent module connects rendered scene observations to segmentation, inpainting and object generators. ([source](https://arxiv.org/pdf/2605.15843v2), Sections 4.2–4.3; Appendix B) |
| tools | Perception models, Graphics Operations, Execution Utilities | SAM3 segmentation, SAM3D generation, Diffueraser inpainting, mask aggregation/removal and rendering. ([source](https://arxiv.org/pdf/2605.15843v2), Sections 4.2–4.3; Appendix B.4) |
| resources | Documentation & Rules | Prompt rules define portability/recognizability and completeness/clarity/centeredness criteria. ([source](https://arxiv.org/pdf/2605.15843v2), Appendix B.2–B.4) |
| representation | Geometry, Pixels | Explicit Gaussian/mesh scene and rendered views/masks/inpainted images. ([source](https://arxiv.org/pdf/2605.15843v2), Section 4) |

Events: [{"type": "first_submission", "value": "2026-05-15T10:56:23+00:00", "precision": "timestamp", "timezone": "UTC", "version": "v1", "primary_url": "https://arxiv.org/abs/2605.15843", "authority": "primary", "evidence": "Canonical history.", "prior_event_status": "not_seen_in_supplied_history"}, {"type": "revision", "value": "2026-11-05T07:15:15+00:00", "precision": "timestamp", "timezone": "UTC", "version": "v2", "local_value": "2026-11-05T01:15:15-06:00", "primary_url": "https://arxiv.org/abs/2605.15843", "authority": "primary", "evidence": "Latest canonical version before cutoff; seven-day revision of discussed paper.", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: ["Candidate selection is on observations that control generation, not necessarily on completed graphics artifacts.", "Separating agent selection from downstream numerical alignment prevents importing optimization scores as agent feedback."]

### [Composable CAD: Sketch-to-CAD Program Synthesis in Parts](https://arxiv.org/abs/2611.01165)
core | High | new_relative_to_snapshot
Application: Static / CAD; operations: Generation, Reconstruction
Combines agentic CAD elaboration with exact deterministic interface seating; 91.5% of recombined shapes satisfy structural criteria versus 54.1% after VLM-only repair under a three-minute cap.
Scope: VLM executes and visually revises proxy CAD programs, responds to explicit geometric constraint failures, and elaborates component programs; composability is then enforced deterministically.
Limits: Guarantee requires restrictive nonempty connected geometry and single planar interfaces; material budget can reject outputs. Flat segmentation lacks hierarchical exploration. CadQuery weak on freeform surfaces. Thirty-three objects and small internal user studies; design constraints can be overruled and deterministic seating slightly worsens proportions.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Modeling | Sketch-to-CAD design-space construction. ([source](https://arxiv.org/pdf/2611.01165v1), Section 3) |
| input_form | Image | Single concept sketch; text/borrowed 3D edits are separate extensions. ([source](https://arxiv.org/pdf/2611.01165v1), Section 3) |
| output | Program, Graphics Artifact | Per-part CadQuery programs and recombinable shape design space. ([source](https://arxiv.org/pdf/2611.01165v1), Figure 1; Sections 3,5.1) |
| model_type | VLM | Gemini 3.1 Pro sees sketch and rendered proxy views. ([source](https://arxiv.org/pdf/2611.01165v1), Appendices B,E) |
| model_training | Off-the-Shelf | Explicitly off-the-shelf and training-free paradigm. ([source](https://arxiv.org/pdf/2611.01165v1), Abstract; related work p.2) |
| planning | PO-2 | Whole-object proxy explicitly fixes component organization before detailed independent generation. ([source](https://arxiv.org/pdf/2611.01165v1), Sections 3.1–3.2) |
| workflow | Parallel | All parts and all five samples generated in parallel after shared planning stage. ([source](https://arxiv.org/pdf/2611.01165v1), Appendix F p.22) |
| update_strategy | Local Patch | Refine/extend existing operations instead of rewriting; deterministic seating appends transforms/cut/union. ([source](https://arxiv.org/pdf/2611.01165v1), Appendix F; Section 4) |
| verifier | Self, Programmatic, Environment | Same VLM compares renders; relation functions check constraints; execution failures repaired. ([source](https://arxiv.org/pdf/2611.01165v1), Appendices D–E; Section 6.2) |
| feedback_assessment | Binary, Diagnosis | Per-relation pass/fail with residual returned as natural-language feedback. ([source](https://arxiv.org/pdf/2611.01165v1), Appendix D) |
| feedback_observation | Visual, Structural Scene State, Runtime | Four-view renders, evaluated proportion/alignment/attachment residuals, compilation errors. ([source](https://arxiv.org/pdf/2611.01165v1), Appendices D–E; Section 6.2) |
| memory_time | Short-Term Memory | Retains fixed proxy program and interfaces across generation/refinement calls. ([source](https://arxiv.org/pdf/2611.01165v1), Sections 3.1–3.2; Appendix F) |
| memory_reach | Local Memory | Each independent component sees only its own proxy/context, no communication between calls. ([source](https://arxiv.org/pdf/2611.01165v1), Section 3.2) |
| action_type | Code/Script | Return executable CadQuery Python programs. ([source](https://arxiv.org/pdf/2611.01165v1), Appendices E–F) |
| graphics_software | General-Purpose | Native CadQuery scripts; deterministic appender wraps returned solid. ([source](https://arxiv.org/pdf/2611.01165v1), Appendix E; Section 4) |
| tools | Execution Utilities, Static Validator, Graphics Operations, Perception models | Program execution/rendering, relation functions, geometry seating operations, image segmentation API. ([source](https://arxiv.org/pdf/2611.01165v1), Sections 3–4; Appendices B,D,E) |
| resources | Not Reported | Provides fresh sketch, generated proxy and fixed prompts but no reusable asset/example/document retrieval. ([source](https://arxiv.org/pdf/2611.01165v1), Appendices B–F; full documentation/retrieve/examples search) |
| representation | Code, Geometry, Pixels | CadQuery programs, geometric solids/proxies/interfaces and rendered comparisons. ([source](https://arxiv.org/pdf/2611.01165v1), Sections 3–4) |

Events: [{"type": "first_submission", "value": "2026-10-31T18:04:23+00:00", "precision": "timestamp", "timezone": "UTC", "version": "v1", "local_value": "2026-10-31T13:04:23-05:00", "primary_url": "https://arxiv.org/abs/2611.01165", "authority": "primary", "evidence": "Canonical submission history, latest only version before cutoff.", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: ["Coarse geometric blueprint is treated as an explicit construction plan, with fixed scaffold plus generated content.", "Deterministic repair is execution support; its proof does not imply agent reasoning guarantees."]

### [CounterSketch: Physics-Grounded Counterfactual Reasoning for Sketch-to-Video Generation](https://arxiv.org/abs/2611.04244)
core | Medium | new_relative_to_snapshot
Application: 2D Graphics, Dynamic / Animation and temporal scene; operations: Generation, Editing
Couples causal sketch interventions to verified constrained motion; under a fixed MoSketch renderer T2V alignment rises from 0.1682 to 0.2011 and dynamic degree from 0.5625 to 0.7750 against direct VLM guidance.
Scope: VLM causal reasoning changes sketch geometry/scene relations and generates an event plan controlling animated trajectories, with explicit semantic replanning and numerical repair.
Limits: Only 80 questions across 20 scenes, two dynamics interventions and no nonrigid motion. Ambiguous grounding and latent physical properties remain difficult. Main controller identity/training, semantic verifier implementation, repair budgets and memory are not specified. Reported video metrics do not directly quantify constraint satisfaction or isolate repair effectiveness.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Animation | Produce motion guidance for counterfactual sketch animation. ([source](https://arxiv.org/pdf/2611.04244v1), Sections 1,3) |
| input_form | Image, Language | Sketch image S and language counterfactual prompt. ([source](https://arxiv.org/pdf/2611.04244v1), Section 3 Eq.1) |
| output | Structured Specification | Verified object trajectories projected into per-frame bounding boxes passed to downstream renderer. ([source](https://arxiv.org/pdf/2611.04244v1), Section 4.5) |
| model_type | VLM | VLM grounds objects and performs causal reasoning over sketch/relations. ([source](https://arxiv.org/pdf/2611.04244v1), Sections 4.1–4.2 Figures 3–4) |
| model_training | Not Reported | No main reasoner adaptation stated; Gemini 3.8 Flash explicitly names both VLM baselines only. ([source](https://arxiv.org/pdf/2611.04244v1), Sections 4–5; full training/fine-tun search) |
| planning | PO-2 | Ordered events encode affected objects, event type, conditions and updated scene graph, then compile to constraints. ([source](https://arxiv.org/pdf/2611.04244v1), Section 4.2 Eq.5) |
| workflow | Graph-Structured | Verifier routes numerical errors to local parameter repair and semantic errors to event replanning. ([source](https://arxiv.org/pdf/2611.04244v1), Figure 5; Section 4.4) |
| update_strategy | Local Patch, Replanning | Adjust initial state/constraints and re-simulate locally; refine event chain for semantic failures. ([source](https://arxiv.org/pdf/2611.04244v1), Section 4.4; Figure 5) |
| verifier | Programmatic | Computes geometric/physical violations and accepts only violation-reducing changes. ([source](https://arxiv.org/pdf/2611.04244v1), Sections 4.3–4.4) |
| feedback_assessment | Binary, Diagnosis | Per-constraint violation report and acceptance gate route repairs. ([source](https://arxiv.org/pdf/2611.04244v1), Figure 5; Section 4.4) |
| feedback_observation | Structural Scene State | Trajectory positions/velocities, contact gaps and physical/semantic constraints. ([source](https://arxiv.org/pdf/2611.04244v1), Sections 4.3–4.4) |
| memory_time | Not Reported | Evolving graph described as representation but no agent retention/context implementation specified. ([source](https://arxiv.org/pdf/2611.04244v1), Full Sections 4–8; memory search) |
| memory_reach | Not Reported | No shared/local access protocol specified. ([source](https://arxiv.org/pdf/2611.04244v1), Full method; memory search) |
| action_type | Structured Specification | Intervention delta, event tuples and updated constraint graph drive solver. ([source](https://arxiv.org/pdf/2611.04244v1), Section 4.2 Eq.5) |
| graphics_software | Agent-Adapted | Custom constraint compiler and motion-box conditioning connect reasoning to MoSketch renderer. ([source](https://arxiv.org/pdf/2611.04244v1), Sections 4.3–4.5) |
| tools | Solver Validator, Static Validator, Graphics Operations | Apply stroke edits, KKT constrained dynamics rollout and trajectory checks. ([source](https://arxiv.org/pdf/2611.04244v1), Sections 4.2–4.4) |
| resources | Documentation & Rules | Explicit support/contact/gravity/conservation and rolling/pulley rule families compile events. ([source](https://arxiv.org/pdf/2611.04244v1), Figures 4–5; Section 4.3) |
| representation | Geometry, Dynamic State, Pixels | Input sketch pixels, vector polygons/contours, trajectory positions and velocities. ([source](https://arxiv.org/pdf/2611.04244v1), Sections 3–4) |

Events: [{"type": "first_submission", "value": "2026-11-03T03:27:35+00:00", "precision": "timestamp", "timezone": "UTC", "version": "v1", "local_value": "2026-11-02T21:27:35-06:00", "primary_url": "https://arxiv.org/abs/2611.04244", "authority": "primary", "evidence": "Official metadata and canonical v1 history.", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: ["Semantic verification actor is unspecified; Programmatic label is restricted to documented numeric constraints.", "Motion-specification output is for upstream reasoner, not the separate renderer's final video."]

### [An Agentic Framework for Quality-Aware and Scenario-Adaptive Image Compression](https://arxiv.org/abs/2611.04960)
core | High | new_relative_to_snapshot
Application: 2D Graphics; operations: Editing, Other
Training-free agent control adapts VVC and Cheng2020 across standard, perceptual and machine-vision compression; on clean Kodak reports 34.52% matched-LPIPS bitrate saving over Cheng2020.
Scope: VLM selects image restoration operations, ROI compression settings and background resampling, directly modifying image artifacts under measured feedback. This is image-processing agent control, not ordinary codec optimization alone.
Limits: Evaluation is small: 24 Kodak, 102 CLIC and 48 HEVC images with synthetic noise/blur. Runtime, tool-call budgets and overhead not quantified. Pseudo-reference IQA can favor imperfect restorations; detector pseudo-ground truth may bias task measures. No dedicated limitations section or exact plan prompts supplied; these gaps are derived from the complete report.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Not Applicable | Restoration and compression of supplied image, not modeling, animation, simulation or visual explanation. ([source](https://arxiv.org/pdf/2611.04960v1), Sections I,III.A) |
| input_form | Image, Language | Observed image x and user compression intent I. ([source](https://arxiv.org/pdf/2611.04960v1), Section III.A Eq.3) |
| output | Rendered Media | Aggregate coded representation B and reconstructed/restored image. ([source](https://arxiv.org/pdf/2611.04960v1), Section III.B) |
| model_type | VLM | Qwen3-VL-8B-Instruct handles image analysis, planning, tools and feedback across roles. ([source](https://arxiv.org/pdf/2611.04960v1), Section III.E p.10) |
| model_training | Off-the-Shelf | PICA explicitly training-free and uses pretrained models without additional training. ([source](https://arxiv.org/pdf/2611.04960v1), Sections II.A–B,IV.B) |
| planning | PO-2 | Schedules restoration subtasks and ROI/background coding plans in prescribed role architecture. ([source](https://arxiv.org/pdf/2611.04960v1), Sections III.C–D) |
| workflow | Sequential | Perception → pre-restoration → coding → post-restoration; each stage iterates its schedule/execute/reflect path. ([source](https://arxiv.org/pdf/2611.04960v1), Figure 1; Section III.B) |
| update_strategy | Candidate Selection, Replanning | Retain lowest-cost acceptable candidate; reschedule remaining restoration/coding plans if not improved. ([source](https://arxiv.org/pdf/2611.04960v1), Sections III.C–D Eqs.5,6,9) |
| verifier | Self, Critic, Programmatic | Same agent reflects on plan; DepictQA provides qualitative quality diagnosis; SGQR/threshold gates compare candidates. ([source](https://arxiv.org/pdf/2611.04960v1), Sections III.B–E) |
| feedback_assessment | Score, Binary, Diagnosis | SGQR/IQA cost, satisfied/not-satisfied thresholds and actionable messages about excessive rate/quality. ([source](https://arxiv.org/pdf/2611.04960v1), Section III.B Eq.4; Figure 2) |
| feedback_observation | Visual, Structural Scene State | Decoded candidate images plus bitrate, QC settings and ROI information. ([source](https://arxiv.org/pdf/2611.04960v1), Section III.B–D) |
| memory_time | Short-Term Memory | Retains current/best image and global-QC baseline across candidate-plan iterations. ([source](https://arxiv.org/pdf/2611.04960v1), Section III.C–D) |
| memory_reach | Local Memory | Each restoration/coding stage retains its own candidates/reference and passes selected result downstream. ([source](https://arxiv.org/pdf/2611.04960v1), Section III.C–D) |
| action_type | Tool/Function Call | VLM explicitly performs tool invocation; calls restoration and target codecs with chosen settings. ([source](https://arxiv.org/pdf/2611.04960v1), Sections III.D–E) |
| graphics_software | Agent-Adapted | Unified QC abstraction and AROIC region adapter wrap existing black-box codecs. ([source](https://arxiv.org/pdf/2611.04960v1), Sections III.A,III.D) |
| tools | Perception models, Graphics Operations, Execution Utilities, Static Validator | Restoration networks, detector/OCR/IQA; crop/downsample/aggregate; codec execution; quality-rate acceptance gates. ([source](https://arxiv.org/pdf/2611.04960v1), Section III.E; Figure 2) |
| resources | Documentation & Rules | Codec-specific QC knowledge such as QP range and effect on rate/quality. ([source](https://arxiv.org/pdf/2611.04960v1), Section III.D; Figure 2; IV.B) |
| representation | Pixels | Raster images and crops throughout restoration, compression and evaluation. ([source](https://arxiv.org/pdf/2611.04960v1), Section III.A–D) |

Events: [{"type": "first_submission", "value": "2026-11-03T14:19:39+00:00", "precision": "timestamp", "timezone": "UTC", "version": "v1", "local_value": "2026-11-03T08:19:39-06:00", "primary_url": "https://arxiv.org/abs/2611.04960", "authority": "primary", "evidence": "Official metadata and canonical v1 history.", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: ["Image restoration/compression is a demonstrated graphics-artifact action but lacks a precise task-axis label; preserve Not Applicable task and explicit Editing/Other operations."]

## date_unresolved (0)

## unresolved (2)

### [SceneAgent: An Agentic Pipeline from 3D and 4D Captures to Simulation Environments](https://computationalrobotics.seas.harvard.edu/SceneAgent/)
unresolved | Low | new_relative_to_snapshot
Application: Static / Scene; operations: Reconstruction
Converts captures into simulation environments through object reconstruction, physical modeling, simulator visual inspection and repair.
Scope: Plausible direct graphics action from project abstract; no full PDF receipt. Deferred at mandatory harness finalization stop; do not promote to core. Outside seven-day window.
Limits: Full-text method, version, dates as applicable, and taxonomy remain unverified. Metadata/project text only; not one of the 14 completed reads.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Unclear |  |
| input_form | Unclear |  |
| output | Unclear |  |
| model_type | Unclear |  |
| model_training | Unclear |  |
| planning | Unclear |  |
| workflow | Unclear |  |
| update_strategy | Unclear |  |
| verifier | Unclear |  |
| feedback_assessment | Unclear |  |
| feedback_observation | Unclear |  |
| memory_time | Unclear |  |
| memory_reach | Unclear |  |
| action_type | Unclear |  |
| graphics_software | Unclear |  |
| tools | Unclear |  |
| resources | Unclear |  |
| representation | Unclear |  |

Events: [{"type": "first_submission", "value": "2026-10-26T02:45:35+00:00", "precision": "timestamp", "timezone": "UTC", "version": "v1", "primary_url": "https://arxiv.org/abs/2610.34745", "authority": "primary", "evidence": "Official Atom metadata; outside seven-day window.", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: []

### [Agent-Guided Immersive World Generation with Alpha-Textured Proxies](https://immersegen.github.io/)
unresolved | Low | new_relative_to_snapshot
Application: Static / Scene; operations: Generation
VLM asset agents select templates, design prompts and arrange alpha-textured proxies in panoramic worlds.
Scope: Plausible direct graphics action from project abstract; no full PDF receipt. Deferred at mandatory harness finalization stop; do not promote to core. Exact publication date and version unresolved.
Limits: Full-text method, version, dates as applicable, and taxonomy remain unverified. Metadata/project text only; not one of the 14 completed reads.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Unclear |  |
| input_form | Unclear |  |
| output | Unclear |  |
| model_type | Unclear |  |
| model_training | Unclear |  |
| planning | Unclear |  |
| workflow | Unclear |  |
| update_strategy | Unclear |  |
| verifier | Unclear |  |
| feedback_assessment | Unclear |  |
| feedback_observation | Unclear |  |
| memory_time | Unclear |  |
| memory_reach | Unclear |  |
| action_type | Unclear |  |
| graphics_software | Unclear |  |
| tools | Unclear |  |
| resources | Unclear |  |
| representation | Unclear |  |

Events: []
Taxonomy deltas: []

## excluded (0)

## Application index
| Application | Papers |
|---|---|
| 2D Graphics | [ManimCode: Learning Visual Self-Correction for Educational Animation](https://arxiv.org/abs/2611.08294) [late_discovery]; [LongBanana: An Expert-Verified Benchmark for Long-Context Multi-Reference Image Synthesis](https://arxiv.org/abs/2611.06856) [late_discovery]; [EvoDesign: Agentic Editable Diagram Creation via Design Expertise Evolution](https://arxiv.org/abs/2604.09568) [late_discovery]; [CounterSketch: Physics-Grounded Counterfactual Reasoning for Sketch-to-Video Generation](https://arxiv.org/abs/2611.04244) [late_discovery]; [An Agentic Framework for Quality-Aware and Scenario-Adaptive Image Compression](https://arxiv.org/abs/2611.04960) [late_discovery] |
| Static / Object | [WorldAct: Activating Monolithic 3D Worlds into Interactive-Ready Object-Centric Scenes](https://arxiv.org/abs/2605.15843) [late_discovery] |
| Static / CAD | [Parametric CAD Bench v3: Evaluating Agentic Parametric CAD Authoring from Text and Engineering Drawings](https://arxiv.org/abs/2611.02659) [late_discovery]; [CADFather: Autonomous CAD Reconstruction through Coordinated Tool Use](https://arxiv.org/abs/2610.09127) [late_discovery]; [CADForge: Agentic Single-View CAD Reconstruction with Explicit Geometry Reasoning](https://arxiv.org/abs/2610.04262) [late_discovery]; [Composable CAD: Sketch-to-CAD Program Synthesis in Parts](https://arxiv.org/abs/2611.01165) [late_discovery] |
| Static / Scene | [GREP: Grounding Generated Room Evaluation in Principles](https://arxiv.org/abs/2611.05802) [late_discovery]; [WorldAct: Activating Monolithic 3D Worlds into Interactive-Ready Object-Centric Scenes](https://arxiv.org/abs/2605.15843) [late_discovery]; [SceneAgent: An Agentic Pipeline from 3D and 4D Captures to Simulation Environments](https://computationalrobotics.seas.harvard.edu/SceneAgent/) [unresolved]; [Agent-Guided Immersive World Generation with Alpha-Textured Proxies](https://immersegen.github.io/) [unresolved] |
| Dynamic / Articulated assets | [NeoWorld-Pro: Programming Interactive Scenes from Monocular Images for Embodied Simulation](https://arxiv.org/abs/2608.24212) [late_discovery] |
| Dynamic / Animation and temporal scene | [ManimCode: Learning Visual Self-Correction for Educational Animation](https://arxiv.org/abs/2611.08294) [late_discovery]; [AgiWorld: An Agentic Video World Model for Building Persistent Worlds](https://arxiv.org/abs/2611.02341) [late_discovery]; [CounterSketch: Physics-Grounded Counterfactual Reasoning for Sketch-to-Video Generation](https://arxiv.org/abs/2611.04244) [late_discovery] |
| Dynamic / Physical simulation and effects | [Code2Worlds-2: Physically Plausible Agent Harness for Embodied World Simulation](https://arxiv.org/abs/2610.17651) [late_discovery] |
| Datasets and Benchmarks | [Parametric CAD Bench v3: Evaluating Agentic Parametric CAD Authoring from Text and Engineering Drawings](https://arxiv.org/abs/2611.02659) [late_discovery]; [GREP: Grounding Generated Room Evaluation in Principles](https://arxiv.org/abs/2611.05802) [late_discovery]; [LongBanana: An Expert-Verified Benchmark for Long-Context Multi-Reference Image Synthesis](https://arxiv.org/abs/2611.06856) [late_discovery] |
| Cross-category | None verified in this run |

## Source ledger
| Source | Status | Checked pages / queries | Limitations |
|---|---|---|---|
| arxiv | partial | [{"query_or_url": "https://arxiv.org/list/cs.GR/new (max_pages=12; observed full-list URLs in scan receipt)", "checked_at": "2026-11-07T22:32:31.104463+00:00", "outcome": "Observed arxiv_scan result; full provenance in tool-events.jsonl. Complete observed listing pagination only, not field completeness."}, {"query_or_url": "https://arxiv.org/list/cs.GR/recent (max_pages=12; observed full-list URLs in scan receipt)", "checked_at": "2026-11-07T22:32:31.153719+00:00", "outcome": "Observed arxiv_scan result; full provenance in tool-events.jsonl. Complete observed listing pagination only, not field completeness."}, {"query_or_url": "https://arxiv.org/list/cs.CV/new (max_pages=12; observed full-list URLs in scan receipt)", "checked_at": "2026-11-07T22:32:32.362814+00:00", "outcome": "Observed arxiv_scan result; full provenance in tool-events.jsonl. Complete observed listing pagination only, not field completeness."}, {"query_or_url": "https://arxiv.org/list/cs.CV/recent (max_pages=12; observed full-list URLs in scan receipt)", "checked_at": "2026-11-07T22:32:33.195920+00:00", "outcome": "Observed arxiv_scan result; full provenance in tool-events.jsonl. Complete observed listing pagination only, not field completeness."}, {"query_or_url": "https://export.arxiv.org/api/query?id_list=2412.10338%2C2501.14546%2C2502.10259%2C2502.21012%2C2503.13344%2C2507.17892%2C2507.19684%2C2508.19204%2C2509.25549%2C2509.26455%2C2510.01347%2C2510.04066%2C2510.24464%2C2511.00908%2C2511.03212%2C2511.09818%2C2511.18811%2C2512.01707%2C2512.14056%2C2512.17581%2C2601.11063%2C2601.15838%2C2602.00192%2C2602.13780%2C2602.17659%2C2602.18742%2C2603.04314%2C2603.10648%2C2603.10828%2C2603.15834%2C2603.16482%2C2603.21071%2C2603.23481%2C2604.02851%2C2604.03420%2C2604.09568%2C2604.10675%2C2604.19741%2C2604.24317%2C2605.03749%2C2605.06207%2C2605.13675%2C2605.15391%2C2605.15843%2C2605.16797%2C2605.16922%2C2605.19256%2C2605.24011%2C2605.26032%2C2605.30983%2C2605.31572%2C2606.02937%2C2606.06113%2C2606.07642%2C2606.08043%2C2606.15920%2C2606.15992%2C2606.17985%2C2606.26718%2C2606.28780%2C2607.03012%2C2607.26921%2C2607.29586%2C2608.00137%2C2608.01896%2C2608.06886%2C2608.08600%2C2608.14430%2C2608.19540%2C2608.24212%2C2608.28602%2C2608.28699%2C2609.00968%2C2609.08818%2C2609.18279%2C2609.25864%2C2609.27110%2C2609.33928%2C2609.37314%2C2610.00365%2C2610.01279%2C2610.01291%2C2610.07729%2C2610.07925%2C2610.08825%2C2610.09173%2C2610.09502%2C2610.14517%2C2610.16320%2C2610.16621%2C2610.18857%2C2610.20973%2C2610.21569%2C2610.21795%2C2610.25284%2C2610.25395%2C2610.27041%2C2610.31166%2C2610.31835%2C2610.33857&max_results=100", "checked_at": "2026-11-07T22:33:30.642206+00:00", "outcome": "Observed arxiv_metadata result; full provenance in tool-events.jsonl. Lead discovery or primary check; dates require official version metadata."}, {"query_or_url": "https://export.arxiv.org/api/query?id_list=2610.35375%2C2610.35766%2C2610.37019%2C2610.40662%2C2610.40702%2C2610.40752%2C2610.40754%2C2610.40801%2C2610.40832%2C2610.40834%2C2610.40887%2C2610.40900%2C2610.40905%2C2610.40913%2C2610.40914%2C2610.40935%2C2610.40947%2C2610.40949%2C2610.40954%2C2610.40971%2C2610.40972%2C2610.40973%2C2610.40976%2C2610.41011%2C2610.41030%2C2610.41037%2C2610.41063%2C2610.41069%2C2610.41080%2C2610.41111%2C2610.41118%2C2610.41127%2C2610.41130%2C2610.41159%2C2610.41185%2C2610.41190%2C2610.41199%2C2610.41204%2C2610.41210%2C2610.41213%2C2610.41216%2C2610.41231%2C2610.41254%2C2610.41257%2C2610.41258%2C2610.41260%2C2610.41304%2C2610.41310%2C2610.41314%2C2610.41328%2C2610.41337%2C2610.41338%2C2610.41348%2C2610.41352%2C2610.41360%2C2610.41362%2C2610.41373%2C2610.41389%2C2610.41402%2C2610.41408%2C2610.41426%2C2610.41446%2C2610.41485%2C2610.41494%2C2610.41496%2C2610.41501%2C2610.41512%2C2610.41520%2C2610.41556%2C2610.41598%2C2610.41602%2C2610.41618%2C2610.41629%2C2610.41642%2C2610.41651%2C2610.41652%2C2610.41671%2C2610.41673%2C2610.41677%2C2610.41695%2C2610.41705%2C2610.41728%2C2610.41763%2C2610.41772%2C2610.41789%2C2610.41790%2C2610.41814%2C2610.41833%2C2610.41834%2C2610.41835%2C2610.41841%2C2610.41877%2C2610.41924%2C2610.41983%2C2610.41987%2C2610.41992%2C2610.42002%2C2610.42031%2C2610.42036%2C2610.42053&max_results=100", "checked_at": "2026-11-07T22:33:34.166699+00:00", "outcome": "Observed arxiv_metadata result; full provenance in tool-events.jsonl. Lead discovery or primary check; dates require official version metadata."}, {"query_or_url": "https://export.arxiv.org/api/query?id_list=2610.42082%2C2610.42092%2C2610.42111%2C2610.42135%2C2610.42136%2C2610.42141%2C2610.42145%2C2610.42149%2C2610.42152%2C2611.00003%2C2611.00004%2C2611.00017%2C2611.00020%2C2611.00022%2C2611.00023%2C2611.00024%2C2611.00025%2C2611.00026%2C2611.00027%2C2611.00028%2C2611.00029%2C2611.00031%2C2611.00032%2C2611.00033%2C2611.00034%2C2611.00035%2C2611.00036%2C2611.00037%2C2611.00038%2C2611.00039%2C2611.00040%2C2611.00041%2C2611.00042%2C2611.00043%2C2611.00044%2C2611.00045%2C2611.00046%2C2611.00047%2C2611.00048%2C2611.00049%2C2611.00050%2C2611.00053%2C2611.00054%2C2611.00055%2C2611.00056%2C2611.00058%2C2611.00059%2C2611.00061%2C2611.00062%2C2611.00063%2C2611.00064%2C2611.00065%2C2611.00066%2C2611.00067%2C2611.00069%2C2611.00071%2C2611.00072%2C2611.00073%2C2611.00074%2C2611.00076%2C2611.00077%2C2611.00078%2C2611.00079%2C2611.00080%2C2611.00081%2C2611.00084%2C2611.00091%2C2611.00092%2C2611.00097%2C2611.00099%2C2611.00102%2C2611.00105%2C2611.00107%2C2611.00110%2C2611.00111%2C2611.00113%2C2611.00114%2C2611.00120%2C2611.00122%2C2611.00140%2C2611.00150%2C2611.00151%2C2611.00157%2C2611.00175%2C2611.00177%2C2611.00179%2C2611.00180%2C2611.00181%2C2611.00184%2C2611.00191%2C2611.00192%2C2611.00227%2C2611.00238%2C2611.00245%2C2611.00247%2C2611.00253%2C2611.00288%2C2611.00293%2C2611.00328%2C2611.00351&max_results=100", "checked_at": "2026-11-07T22:33:37.474996+00:00", "outcome": "Observed arxiv_metadata result; full provenance in tool-events.jsonl. Lead discovery or primary check; dates require official version metadata."}, {"query_or_url": "https://export.arxiv.org/api/query?id_list=2611.00367%2C2611.00371%2C2611.00375%2C2611.00383%2C2611.00396%2C2611.00406%2C2611.00423%2C2611.00427%2C2611.00430%2C2611.00458%2C2611.00478%2C2611.00482%2C2611.00507%2C2611.00523%2C2611.00527%2C2611.00551%2C2611.00556%2C2611.00566%2C2611.00608%2C2611.00634%2C2611.00653%2C2611.00658%2C2611.00671%2C2611.00676%2C2611.00681%2C2611.00683%2C2611.00684%2C2611.00699%2C2611.00704%2C2611.00715%2C2611.00721%2C2611.00722%2C2611.00756%2C2611.00758%2C2611.00763%2C2611.00768%2C2611.00769%2C2611.00780%2C2611.00784%2C2611.00785%2C2611.00791%2C2611.00794%2C2611.00804%2C2611.00810%2C2611.00819%2C2611.00823%2C2611.00828%2C2611.00833%2C2611.00843%2C2611.00848%2C2611.00859%2C2611.00892%2C2611.00899%2C2611.00908%2C2611.00926%2C2611.00937%2C2611.00953%2C2611.00963%2C2611.00974%2C2611.01018%2C2611.01048%2C2611.01050%2C2611.01074%2C2611.01078%2C2611.01084%2C2611.01095%2C2611.01120%2C2611.01125%2C2611.01141%2C2611.01162%2C2611.01165%2C2611.01215%2C2611.01222%2C2611.01229%2C2611.01230%2C2611.01252%2C2611.01263%2C2611.01283%2C2611.01295%2C2611.01372%2C2611.01391%2C2611.01396%2C2611.01400%2C2611.01414%2C2611.01438%2C2611.01457%2C2611.01460%2C2611.01463%2C2611.01466%2C2611.01467%2C2611.01511%2C2611.01513%2C2611.01517%2C2611.01529%2C2611.01534%2C2611.01536%2C2611.01537%2C2611.01541%2C2611.01543%2C2611.01548&max_results=100", "checked_at": "2026-11-07T22:36:00.031561+00:00", "outcome": "Observed arxiv_metadata result; full provenance in tool-events.jsonl. Lead discovery or primary check; dates require official version metadata."}, {"query_or_url": "https://export.arxiv.org/api/query?id_list=2611.01550%2C2611.01551%2C2611.01558%2C2611.01573%2C2611.01578%2C2611.01600%2C2611.01601%2C2611.01605%2C2611.01607%2C2611.01615%2C2611.01617%2C2611.01626%2C2611.01627%2C2611.01631%2C2611.01635%2C2611.01645%2C2611.01648%2C2611.01663%2C2611.01675%2C2611.01676%2C2611.01682%2C2611.01684%2C2611.01688%2C2611.01696%2C2611.01705%2C2611.01730%2C2611.01736%2C2611.01759%2C2611.01765%2C2611.01783%2C2611.01790%2C2611.01791%2C2611.01815%2C2611.01822%2C2611.01823%2C2611.01846%2C2611.01850%2C2611.01858%2C2611.01860%2C2611.01888%2C2611.01900%2C2611.01902%2C2611.01907%2C2611.01913%2C2611.01921%2C2611.01934%2C2611.01937%2C2611.01939%2C2611.01958%2C2611.01960%2C2611.01962%2C2611.01970%2C2611.01974%2C2611.01978%2C2611.01982%2C2611.01990%2C2611.01992%2C2611.02008%2C2611.02026%2C2611.02034%2C2611.02037%2C2611.02044%2C2611.02051%2C2611.02053%2C2611.02056%2C2611.02076%2C2611.02096%2C2611.02101%2C2611.02114%2C2611.02119%2C2611.02147%2C2611.02197%2C2611.02203%2C2611.02204%2C2611.02211%2C2611.02245%2C2611.02284%2C2611.02305%2C2611.02306%2C2611.02324%2C2611.02327%2C2611.02341%2C2611.02356%2C2611.02363%2C2611.02364%2C2611.02366%2C2611.02393%2C2611.02405%2C2611.02419%2C2611.02433%2C2611.02437%2C2611.02474%2C2611.02488%2C2611.02499%2C2611.02505%2C2611.02506%2C2611.02512%2C2611.02519%2C2611.02526%2C2611.02540&max_results=100", "checked_at": "2026-11-07T22:36:03.311006+00:00", "outcome": "Observed arxiv_metadata result; full provenance in tool-events.jsonl. Lead discovery or primary check; dates require official version metadata."}, {"query_or_url": "https://export.arxiv.org/api/query?id_list=2611.02551%2C2611.02568%2C2611.02578%2C2611.02581%2C2611.02593%2C2611.02599%2C2611.02603%2C2611.02625%2C2611.02631%2C2611.02648%2C2611.02649%2C2611.02651%2C2611.02654%2C2611.02658%2C2611.02659%2C2611.02661%2C2611.02671%2C2611.02685%2C2611.02686%2C2611.02690%2C2611.02695%2C2611.02726%2C2611.02737%2C2611.02744%2C2611.02751%2C2611.02756%2C2611.02759%2C2611.02767%2C2611.02769%2C2611.02775%2C2611.02776%2C2611.02780%2C2611.02782%2C2611.02786%2C2611.02803%2C2611.02822%2C2611.02844%2C2611.02853%2C2611.02854%2C2611.02857%2C2611.02862%2C2611.02877%2C2611.02897%2C2611.02902%2C2611.02921%2C2611.02929%2C2611.02931%2C2611.02941%2C2611.02952%2C2611.02964%2C2611.02995%2C2611.03007%2C2611.03017%2C2611.03023%2C2611.03027%2C2611.03033%2C2611.03042%2C2611.03043%2C2611.03062%2C2611.03067%2C2611.03069%2C2611.03078%2C2611.03080%2C2611.03087%2C2611.03097%2C2611.03098%2C2611.03109%2C2611.03114%2C2611.03120%2C2611.03125%2C2611.03132%2C2611.03136%2C2611.03140%2C2611.03143%2C2611.03189%2C2611.03228%2C2611.03229%2C2611.03232%2C2611.03245%2C2611.03247%2C2611.03283%2C2611.03285%2C2611.03339%2C2611.03360%2C2611.03370%2C2611.03371%2C2611.03377%2C2611.03382%2C2611.03390%2C2611.03393%2C2611.03394%2C2611.03399%2C2611.03404%2C2611.03421%2C2611.03430%2C2611.03438%2C2611.03449%2C2611.03455%2C2611.03465%2C2611.03528&max_results=100", "checked_at": "2026-11-07T22:36:06.603152+00:00", "outcome": "Observed arxiv_metadata result; full provenance in tool-events.jsonl. Lead discovery or primary check; dates require official version metadata."}, {"query_or_url": "https://export.arxiv.org/api/query?id_list=2610.04262%2C2610.09127%2C2610.17651%2C2610.40333%2C2611.01860%2C2611.04277%2C2611.06741%2C2611.07392%2C2611.07909&max_results=9", "checked_at": "2026-11-07T22:36:09.791587+00:00", "outcome": "Observed arxiv_metadata result; full provenance in tool-events.jsonl. Lead discovery or primary check; dates require official version metadata."}, {"query_or_url": "https://export.arxiv.org/api/query?id_list=2611.03533%2C2611.03557%2C2611.03588%2C2611.03597%2C2611.03602%2C2611.03626%2C2611.03646%2C2611.03647%2C2611.03648%2C2611.03685%2C2611.03717%2C2611.03741%2C2611.03765%2C2611.03775%2C2611.03932%2C2611.03936%2C2611.03937%2C2611.03940%2C2611.03942%2C2611.03952%2C2611.03958%2C2611.04002%2C2611.04012%2C2611.04025%2C2611.04028%2C2611.04034%2C2611.04053%2C2611.04084%2C2611.04087%2C2611.04092%2C2611.04102%2C2611.04111%2C2611.04112%2C2611.04123%2C2611.04139%2C2611.04155%2C2611.04164%2C2611.04166%2C2611.04173%2C2611.04193%2C2611.04195%2C2611.04200%2C2611.04216%2C2611.04219%2C2611.04221%2C2611.04233%2C2611.04235%2C2611.04242%2C2611.04244%2C2611.04254%2C2611.04257%2C2611.04262%2C2611.04268%2C2611.04286%2C2611.04300%2C2611.04303%2C2611.04305%2C2611.04317%2C2611.04337%2C2611.04352%2C2611.04358%2C2611.04368%2C2611.04374%2C2611.04379%2C2611.04386%2C2611.04389%2C2611.04397%2C2611.04405%2C2611.04409%2C2611.04414%2C2611.04416%2C2611.04418%2C2611.04422%2C2611.04423%2C2611.04435%2C2611.04438%2C2611.04442%2C2611.04452%2C2611.04467%2C2611.04470%2C2611.04472%2C2611.04476%2C2611.04489%2C2611.04490%2C2611.04491%2C2611.04492%2C2611.04498%2C2611.04524%2C2611.04529%2C2611.04534%2C2611.04537%2C2611.04548%2C2611.04554%2C2611.04583%2C2611.04591%2C2611.04604%2C2611.04616%2C2611.04624%2C2611.04626%2C2611.04633&max_results=100", "checked_at": "2026-11-07T22:36:22.491374+00:00", "outcome": "Observed arxiv_metadata result; full provenance in tool-events.jsonl. Lead discovery or primary check; dates require official version metadata."}, {"query_or_url": "https://export.arxiv.org/api/query?id_list=2611.04645%2C2611.04654%2C2611.04666%2C2611.04709%2C2611.04710%2C2611.04711%2C2611.04712%2C2611.04728%2C2611.04734%2C2611.04754%2C2611.04755%2C2611.04759%2C2611.04764%2C2611.04780%2C2611.04811%2C2611.04822%2C2611.04873%2C2611.04874%2C2611.04894%2C2611.04903%2C2611.04912%2C2611.04913%2C2611.04916%2C2611.04932%2C2611.04939%2C2611.04940%2C2611.04943%2C2611.04946%2C2611.04948%2C2611.04950%2C2611.04959%2C2611.04960%2C2611.04980%2C2611.05004%2C2611.05008%2C2611.05011%2C2611.05024%2C2611.05035%2C2611.05049%2C2611.05058%2C2611.05062%2C2611.05066%2C2611.05072%2C2611.05083%2C2611.05084%2C2611.05102%2C2611.05106%2C2611.05131%2C2611.05145%2C2611.05158%2C2611.05172%2C2611.05181%2C2611.05192%2C2611.05193%2C2611.05197%2C2611.05205%2C2611.05206%2C2611.05223%2C2611.05231%2C2611.05275%2C2611.05279%2C2611.05280%2C2611.05286%2C2611.05291%2C2611.05294%2C2611.05348%2C2611.05359%2C2611.05361%2C2611.05377%2C2611.05380%2C2611.05398%2C2611.05403%2C2611.05404%2C2611.05406%2C2611.05407%2C2611.05408%2C2611.05411%2C2611.05443%2C2611.05449%2C2611.05451%2C2611.05522%2C2611.05539%2C2611.05559%2C2611.05564%2C2611.05565%2C2611.05569%2C2611.05570%2C2611.05578%2C2611.05579%2C2611.05581%2C2611.05593%2C2611.05594%2C2611.05599%2C2611.05618%2C2611.05633%2C2611.05646%2C2611.05648%2C2611.05680%2C2611.05689%2C2611.05693&max_results=100", "checked_at": "2026-11-07T22:36:25.816631+00:00", "outcome": "Observed arxiv_metadata result; full provenance in tool-events.jsonl. Lead discovery or primary check; dates require official version metadata."}, {"query_or_url": "https://export.arxiv.org/api/query?id_list=2611.05697%2C2611.05734%2C2611.05737%2C2611.05738%2C2611.05742%2C2611.05755%2C2611.05766%2C2611.05801%2C2611.05802%2C2611.05811%2C2611.05818%2C2611.05825%2C2611.05843%2C2611.05847%2C2611.05851%2C2611.05859%2C2611.05874%2C2611.05893%2C2611.05909%2C2611.05917%2C2611.05925%2C2611.05927%2C2611.05945%2C2611.05969%2C2611.05974%2C2611.05992%2C2611.05994%2C2611.06000%2C2611.06007%2C2611.06015%2C2611.06020%2C2611.06040%2C2611.06042%2C2611.06046%2C2611.06047%2C2611.06048%2C2611.06061%2C2611.06070%2C2611.06083%2C2611.06085%2C2611.06089%2C2611.06093%2C2611.06096%2C2611.06098%2C2611.06105%2C2611.06113%2C2611.06120%2C2611.06141%2C2611.06143%2C2611.06149%2C2611.06160%2C2611.06168%2C2611.06180%2C2611.06191%2C2611.06195%2C2611.06203%2C2611.06205%2C2611.06221%2C2611.06230%2C2611.06247%2C2611.06255%2C2611.06258%2C2611.06259%2C2611.06270%2C2611.06273%2C2611.06282%2C2611.06302%2C2611.06343%2C2611.06353%2C2611.06355%2C2611.06377%2C2611.06378%2C2611.06412%2C2611.06415%2C2611.06422%2C2611.06430%2C2611.06433%2C2611.06452%2C2611.06453%2C2611.06455%2C2611.06471%2C2611.06484%2C2611.06518%2C2611.06540%2C2611.06544%2C2611.06556%2C2611.06593%2C2611.06594%2C2611.06624%2C2611.06627%2C2611.06631%2C2611.06635%2C2611.06637%2C2611.06652%2C2611.06664%2C2611.06685%2C2611.06701%2C2611.06724%2C2611.06728%2C2611.06738&max_results=100", "checked_at": "2026-11-07T22:36:29.122503+00:00", "outcome": "Observed arxiv_metadata result; full provenance in tool-events.jsonl. Lead discovery or primary check; dates require official version metadata."}, {"query_or_url": "https://export.arxiv.org/api/query?id_list=2610.34745&max_results=1", "checked_at": "2026-11-07T22:36:32.417374+00:00", "outcome": "Observed arxiv_metadata result; full provenance in tool-events.jsonl. Lead discovery or primary check; dates require official version metadata."}, {"query_or_url": "https://export.arxiv.org/api/query?id_list=2611.06748%2C2611.06760%2C2611.06770%2C2611.06781%2C2611.06796%2C2611.06817%2C2611.06838%2C2611.06840%2C2611.06844%2C2611.06849%2C2611.06854%2C2611.06856%2C2611.06864%2C2611.06870%2C2611.06890%2C2611.06899%2C2611.06901%2C2611.06908%2C2611.06918%2C2611.06930%2C2611.06935%2C2611.06954%2C2611.06974%2C2611.06993%2C2611.07009%2C2611.07049%2C2611.07055%2C2611.07061%2C2611.07063%2C2611.07081%2C2611.07132%2C2611.07148%2C2611.07176%2C2611.07188%2C2611.07289%2C2611.07294%2C2611.07301%2C2611.07328%2C2611.07329%2C2611.07354%2C2611.07384%2C2611.07397%2C2611.07398%2C2611.07408%2C2611.07411%2C2611.07417%2C2611.07431%2C2611.07437%2C2611.07443%2C2611.07463%2C2611.07481%2C2611.07498%2C2611.07502%2C2611.07512%2C2611.07513%2C2611.07540%2C2611.07543%2C2611.07551%2C2611.07553%2C2611.07555%2C2611.07566%2C2611.07573%2C2611.07575%2C2611.07580%2C2611.07593%2C2611.07604%2C2611.07613%2C2611.07632%2C2611.07644%2C2611.07647%2C2611.07648%2C2611.07658%2C2611.07662%2C2611.07665%2C2611.07673%2C2611.07677%2C2611.07682%2C2611.07683%2C2611.07702%2C2611.07705%2C2611.07709%2C2611.07711%2C2611.07713%2C2611.07718%2C2611.07730%2C2611.07741%2C2611.07765%2C2611.07775%2C2611.07793%2C2611.07810%2C2611.07811%2C2611.07814%2C2611.07828%2C2611.07836%2C2611.07843%2C2611.07850%2C2611.07865%2C2611.07867%2C2611.07873%2C2611.07883&max_results=100", "checked_at": "2026-11-07T22:36:40.836562+00:00", "outcome": "Observed arxiv_metadata result; full provenance in tool-events.jsonl. Lead discovery or primary check; dates require official version metadata."}, {"query_or_url": "https://export.arxiv.org/api/query?id_list=2611.07900%2C2611.07902%2C2611.07922%2C2611.07929%2C2611.07935%2C2611.07939%2C2611.07941%2C2611.07950%2C2611.07955%2C2611.07961%2C2611.07979%2C2611.07994%2C2611.08003%2C2611.08005%2C2611.08054%2C2611.08080%2C2611.08081%2C2611.08091%2C2611.08095%2C2611.08099%2C2611.08111%2C2611.08125%2C2611.08128%2C2611.08136%2C2611.08138%2C2611.08140%2C2611.08147%2C2611.08148%2C2611.08154%2C2611.08156%2C2611.08157%2C2611.08185%2C2611.08216%2C2611.08236%2C2611.08240%2C2611.08262%2C2611.08264%2C2611.08271%2C2611.08275%2C2611.08286%2C2611.08288%2C2611.08294%2C2611.08301%2C2611.08330%2C2611.08342%2C2611.08352%2C2611.08359%2C2611.08360%2C2611.08368%2C2611.08372%2C2611.08393%2C2611.08407%2C2611.08413%2C2611.08436%2C2611.08441%2C2611.08449%2C2611.08477%2C2611.08485%2C2611.08486&max_results=59", "checked_at": "2026-11-07T22:36:44.125594+00:00", "outcome": "Observed arxiv_metadata result; full provenance in tool-events.jsonl. Lead discovery or primary check; dates require official version metadata."}] | Four required listing paginations completed without unvisited links/errors. All 1062 listing IDs resolved officially; no target-day/history-needed records. Full catchup attention abstracts reviewed (139), plus outside-window title hints reconciled. Most remaining ordinary catalog abstracts unreviewed; other arXiv categories unscanned. Listing snapshot was retrieved after frozen cutoff and is not historical availability proof; retained versions predate cutoff. |
| hugging_face | partial | [{"query_or_url": "https://huggingface.co/papers/date/2026-11-06", "checked_at": "2026-11-07T22:32:32.958559+00:00", "outcome": "Observed hf_daily result; full provenance in tool-events.jsonl. Lead discovery or primary check; dates require official version metadata."}] | One target-date curation page inspected; curation date is not publication. Not all external links resolved; additional-source-leads.json preserves mentions. |
| openreview | partial | [{"query_or_url": "agent animation cutscene temporal world scene cinematography site:openreview.net", "checked_at": "2026-11-07T22:34:52.820622+00:00", "outcome": "Observed web_search result; full provenance in tool-events.jsonl. Lead discovery or primary check; dates require official version metadata."}] | Search-only targeted animation coverage; no full venue-wide enumeration or direct OpenReview metadata API. Candidate dates unverified; deferred source queue. |
| official_venues | partial | [{"query_or_url": "agent CAD generation reconstruction editing constraint solver program repair visual feedback November 6 2026", "checked_at": "2026-11-07T22:33:21.368176+00:00", "outcome": "Observed web_search result; full provenance in tool-events.jsonl. Lead discovery or primary check; dates require official version metadata."}, {"query_or_url": "agent graphics benchmark world auditing verification SIGGRAPH 2026 proceedings", "checked_at": "2026-11-07T22:35:38.106532+00:00", "outcome": "Observed web_search result; full provenance in tool-events.jsonl. Lead discovery or primary check; dates require official version metadata."}] | Hosted search observed ACM/ACL/PMLR/AAAI/IEEE primary venue sources; no complete proceedings sweep or independent publication-date resolution for every hit. |
| project_author_lab | partial | [{"query_or_url": "agent 3D scene layout world generation reconstruction BIM architecture environment spatial arrangement project lab", "checked_at": "2026-11-07T22:34:08.805588+00:00", "outcome": "Observed web_search result; full provenance in tool-events.jsonl. Lead discovery or primary check; dates require official version metadata."}, {"query_or_url": "https://computationalrobotics.seas.harvard.edu/SceneAgent/", "checked_at": "2026-11-07T22:36:06.899108+00:00", "outcome": "Observed open_page result; full provenance in tool-events.jsonl. Lead discovery or primary check; dates require official version metadata."}, {"query_or_url": "https://immersegen.github.io/", "checked_at": "2026-11-07T22:36:07.034887+00:00", "outcome": "Observed open_page result; full provenance in tool-events.jsonl. Lead discovery or primary check; dates require official version metadata."}] | Two official project pages opened; SceneAgent date resolved via official metadata, ImmerseGen exact date unresolved. Other search mentions deferred, not read. |

## Query coverage
- 2d: partial; [{'query_or_url': 'agent 3D object procedural modeling Blender material inverse graphics geometry editing November 2026', 'checked_at': '2026-11-07T22:32:50.119909+00:00', 'outcome': 'Observed web_search result; full provenance in tool-events.jsonl. Lead discovery or primary check; dates require official version metadata.'}]
- object: partial; [{'query_or_url': 'agent SVG diagram chart slide poster editable visual feedback scientific illustration November 6 2026 October 31 2026', 'checked_at': '2026-11-07T22:32:58.192655+00:00', 'outcome': 'Observed web_search result; full provenance in tool-events.jsonl. Lead discovery or primary check; dates require official version metadata.'}]
- cad: partial; [{'query_or_url': 'agent CAD generation reconstruction editing constraint solver program repair visual feedback November 6 2026', 'checked_at': '2026-11-07T22:33:21.368176+00:00', 'outcome': 'Observed web_search result; full provenance in tool-events.jsonl. Lead discovery or primary check; dates require official version metadata.'}]
- scene: partial; [{'query_or_url': 'agent 3D scene layout world generation reconstruction BIM architecture environment spatial arrangement project lab', 'checked_at': '2026-11-07T22:34:08.805588+00:00', 'outcome': 'Observed web_search result; full provenance in tool-events.jsonl. Lead discovery or primary check; dates require official version metadata.'}]
- articulation: partial; [{'query_or_url': 'agent articulated asset joint mechanism rig generation October 31 November 6 2026', 'checked_at': '2026-11-07T22:34:28.067150+00:00', 'outcome': 'Observed web_search result; full provenance in tool-events.jsonl. Lead discovery or primary check; dates require official version metadata.'}]
- animation: partial; [{'query_or_url': 'agent animation cutscene temporal world scene cinematography site:openreview.net', 'checked_at': '2026-11-07T22:34:52.820622+00:00', 'outcome': 'Observed web_search result; full provenance in tool-events.jsonl. Lead discovery or primary check; dates require official version metadata.'}]
- simulation: partial; [{'query_or_url': 'agent physical simulation particle effects deformable world November 2026 research', 'checked_at': '2026-11-07T22:35:17.651511+00:00', 'outcome': 'Observed web_search result; full provenance in tool-events.jsonl. Lead discovery or primary check; dates require official version metadata.'}]
- benchmark: partial; [{'query_or_url': 'agent graphics benchmark world auditing verification SIGGRAPH 2026 proceedings', 'checked_at': '2026-11-07T22:35:38.106532+00:00', 'outcome': 'Observed web_search result; full provenance in tool-events.jsonl. Lead discovery or primary check; dates require official version metadata.'}]
- harness: partial; [{'query_or_url': 'graphics agent memory replanning tool interface feedback program synthesis November 6 2026', 'checked_at': '2026-11-07T22:35:52.693755+00:00', 'outcome': 'Observed web_search result; full provenance in tool-events.jsonl. Lead discovery or primary check; dates require official version metadata.'}]

## Source-derived candidate coverage

Mechanical audit of collected arXiv titles; relevance and semantic correctness require paper evidence.

- Metadata resolved: 1062 / 1062 collected IDs.
- Target-day / history-uncertain candidates: 0.
- Explicit triage decisions: 0; catalog-page delivery: 0.
- Missing source scans: 0; incomplete scans: 0.
- Unresolved metadata: 0; no triage decision: 0.
- Full candidate IDs and remaining gaps: `coverage-audit.json`. Unreviewed entries are not exclusions.
- Other platforms remain governed by the source ledger; this audit is not exhaustive discovery.

## Borderline graphics contributions

These records are not established core agentic systems. They remain visible with their scope uncertainty.

| Paper | Why borderline |
|---|---|
| None recorded | This does not establish that no borderline work exists. |

## Agent-to-graphics evidence

| Paper | Status | Controller | Action / decision | Graphics target | Source |
|---|---|---|---|---|---|
| ManimCode: Learning Visual Self-Correction for Educational Animation | core | Role-conditioned ManimCode Qwen3.5-4B Writer/Reviewer/Reviser | Generate and rewrite executable animation programs; retrieve documentation; retain best rendered candidate | Manim educational animation code and rendered videos | [Sections 3.2, 4.2; Appendix A.3](https://arxiv.org/pdf/2611.08294v1) |
| Parametric CAD Bench v3: Evaluating Agentic Parametric CAD Authoring from Text and Engineering Drawings | core | mini-swe-agent with multimodal Opus 5.5 (one of 13 evaluated model-agent systems) | Write and execute FreeCAD scripts to construct and save native parametric models | FreeCAD PartDesign feature trees, B-rep geometry and FCStd artifacts | [Sections 3.1–3.2, 5.2; Appendices B–C](https://arxiv.org/pdf/2611.02659v1) |
| GREP: Grounding Generated Room Evaluation in Principles | core | GREP VLM discovery/evaluator with camera selector, using GPT-5.6 Sol | Instantiate object/relation checks; measure scene geometry; select and render views to resolve missing evidence | Submitted 3D furnished room and its camera observations; geometry remains fixed | [Section 3.3; Appendix A.1–A.5](https://arxiv.org/pdf/2611.05802v1) |
| CADFather: Autonomous CAD Reconstruction through Coordinated Tool Use | core | Qwen3.8-27B VLM assistant | act(tool,candidate,n) chooses candidate continuation, learned/algorithmic proposals or parameter refinement; finish controls stopping | CadQuery-based CAD program search pool and executed solids | [Sections 3.2–3.6 pp.4–7](https://arxiv.org/pdf/2610.09127v1) |
| Code2Worlds-2: Physically Plausible Agent Harness for Embodied World Simulation | core | Physical scene compiler and Post-Process/refinement model with simulator and visual critics | Emit and correct typed physical plans and dynamics specifications | Embodied World Graph, MuJoCo MJCF scene physical parameters and executable dynamics | [Section 3; Appendix C.5–C.6 pp.20–22](https://arxiv.org/pdf/2610.17651v1) |
| CADForge: Agentic Single-View CAD Reconstruction with Explicit Geometry Reasoning | core | GPT-5.5 planner/geometry/reviewer and code-generation roles | Select ordered components and references, compute geometry parameters, generate and repair component CadQuery scripts | Part-wise B-reps and parametric CAD reconstruction of supplied image | [Sections 3.2–3.5; Appendix G](https://arxiv.org/pdf/2610.04262v1) |
| AgiWorld: An Agentic Video World Model for Building Persistent Worlds | core | One GPT-6-Astra multimodal model in Director and State Update functions | Write world/journey state, waypoints and structured prompts; review generated chunks and replan | Camera-controlled generated video world and shared geometric memory | [Sections 2.2–3.4; Appendix A.1, Algorithm 1](https://arxiv.org/pdf/2611.02341v1) |
| LongBanana: An Expert-Verified Benchmark for Long-Context Multi-Reference Image Synthesis | core | Claude Sonnet 4.6 in OpenClaw RPR harness | Select reference evidence, schedule generation/editing calls, inspect drafts and revise prompts | Multi-reference synthesized raster compositions | [Section 4.1 pp.6–7; Appendix C.1 p.33; D.2 Figure 18](https://arxiv.org/pdf/2611.06856v1) |
| NeoWorld-Pro: Programming Interactive Scenes from Monocular Images for Embodied Simulation | core | MLLM Programmer and Reasoner, exemplified by GPT-5.6-sol | Write Blender geometry/articulation/export scripts and revise structural or physical parameters after failed simulation tests | Articulated object's geometry, joint topology/limits, inertial and friction properties | [Section 3.2 pp.5–6, Figure 3](https://arxiv.org/pdf/2608.24212v3) |
| EvoDesign: Agentic Editable Diagram Creation via Design Expertise Evolution | core | Structure/style/layout VLM agents and localized refiner | Instantiate canvas fields; move nodes, change style, align groups and reroute edges | Editable Excalidraw object manifest and rendered diagram | [Sections 4.1–4.2; Algorithm 1](https://arxiv.org/pdf/2604.09568v3) |
| WorldAct: Activating Monolithic 3D Worlds into Interactive-Ready Object-Centric Scenes | core | Qwen3.6-Plus vision/execution agent | Classify portable objects, supply segmentation prompts and select highest-scored object view for reconstruction | Objects removed from 3DGS scene, reconstruction conditioning and background inpainting masks | [Sections 4.2.1,4.3.2; Appendix B pp.16–17](https://arxiv.org/pdf/2605.15843v2) |
| Composable CAD: Sketch-to-CAD Program Synthesis in Parts | core | Gemini 3.1 Pro VLM | Generate and revise proxy CadQuery code from renders/constraint reports; edit per-part proxy programs into detailed variants | Interchangeable parametric component programs and assembled CAD solids | [Section 3; Appendices D–F pp.21–22](https://arxiv.org/pdf/2611.01165v1) |
| CounterSketch: Physics-Grounded Counterfactual Reasoning for Sketch-to-Video Generation | core | VLM grounding/intervention and causal event-chain reasoner | Change vector strokes and scene graph, infer event sequence, locally replan when constraints fail | Sketch object geometry/relations and animation motion trajectories | [Sections 4.1–4.4 pp.5–7](https://arxiv.org/pdf/2611.04244v1) |
| An Agentic Framework for Quality-Aware and Scenario-Adaptive Image Compression | core | Qwen3-VL-8B-Instruct across four collaborative roles | Schedule restoration tools and regional coding plans; invoke codecs, evaluate and reschedule | Input and decoded image regions, restored raster images and compressed representation | [Sections III.C–E pp.5–10; Figures 1–2](https://arxiv.org/pdf/2611.04960v1) |

## Prior-day memory and carry-over

Frozen history: `knowledge/daily-history/through-20261015-bvb-v11`. Previously unread records now fully read: 3. Prior pending records still without a new full read: 92.

See history-delta.json for per-paper transitions. Historical results remain in the frozen bundle; not repeated is not excluded, and new-to-history does not mean newly published.

## Abstract-first reading queue

Attention pool: 140; abstracts not delivered: 0; priority/triage gaps: 0; unread ranked leads: 20. See reading-plan.json for model-authored priorities and deferred leads. Priority is not an inclusion judgment or recall guarantee.
