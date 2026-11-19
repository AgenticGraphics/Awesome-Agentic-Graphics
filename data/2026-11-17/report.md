# Agentic Graphics daily report
Date: 2026-11-17 | Timezone: America/Chicago | As of: 2026-11-19T00:48:02+00:00
partial browser-based same-day search; source coverage incomplete
Taxonomy: google-doc-taxonomy-v3-2026-10-15 | Snapshot: authorized_live_snapshot_reconciled_and_frozen

## Coverage limits
- Frozen cutoff is 2026-11-19T00:48:02+00:00; retrieval timestamps after cutoff are ledger observation times and eligibility uses source event timestamps.
- The arXiv catalog covered 1098 collected identities from complete observed cs.GR/cs.CV new/recent listings, with 235 target/uncertain abstracts and 337 catch-up abstracts delivered; all 235 target/uncertain abstracts were reviewed at abstract level, but many catch-up leads remain unranked/unread.
- Only four arXiv source pairs were scanned. cs.AI, cs.HC, cs.RO, cs.MM, eess.IV, HF, OpenReview, official venues, and project/author/lab sources were not fully checked.
- Metadata-only deferred candidates remain in reading-plan.json and candidate-catalog.json; unreviewed/low-priority leads are unresolved, not excluded.
- Triage decisions are in triage.json; selected reading order and ranks are provisional. Five PDFs were fully read and checkpointed: MAVE, CADMAGEDDON, MillBill, CutAgent, ConserveEdit.
- No claim of exhaustive discovery or no-paper result is made.

## already_reported (0)

## same_day_new (5)

### [MAVE: Reconstructing Editable 3D Blockouts from Film Shots](https://arxiv.org/abs/2611.22464)
core | High | new_relative_to_snapshot
Application: Static / Scene, Dynamic / Animation and temporal scene; operations: Reconstruction, Editing, Generation
MAVE combines metric video observation, agentic Blender scene construction, and evidence-based verification for editable 3D blockout reconstruction, with MAVEBench and MAVEData-3K.
Scope: The paper demonstrates an LLM agent operating on an editable Blender graphics environment: it generates edit programs that update a scene, queries evidence, and uses verification feedback to refine the reconstruction.
Limits: The paper relies on recovered camera/human representations and pseudo-depth evidence; verification improves results but does not eliminate reconstruction ambiguity. The agent's explicit planning representation and training/adaptation status are not reported. Full experiments use film-shot blockouts rather than general graphics environments.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Modeling | The task is video-to-editable 3D blockout reconstruction and scene modeling. ([source](https://arxiv.org/pdf/2611.22464v1), Sections 2.1, 3.2, pp.2,5) |
| input_form | Video | Given a film-shot video V, the method reconstructs a blockout scene. ([source](https://arxiv.org/pdf/2611.22464v1), Section 2.1, p.2) |
| output | Graphics Artifact, Rendered Media | Outputs are editable Blender scenes and aligned blockout videos. ([source](https://arxiv.org/pdf/2611.22464v1), Abstract p.1; Section 3.3 p.6) |
| model_type | LLM | An LLM-based agent generates edit programs; multiple LLM agents are evaluated. ([source](https://arxiv.org/pdf/2611.22464v1), Sections 3.2, 4.1, pp.5-6) |
| model_training | Not Reported | The paper reports evaluated agent backends but does not report training or adaptation of the decision-making models for this task. ([source](https://arxiv.org/pdf/2611.22464v1), Section 4.1, p.6; LLM Usage Statement p.10) |
| planning | Unclear | The paper specifies a query-edit-verify policy and operation selection, but does not define an explicit task-plan representation. ([source](https://arxiv.org/pdf/2611.22464v1), Section 3.2, p.6) |
| workflow | Sequential | Scene construction proceeds through repeated query, edit, render/inspect, and verify iterations. ([source](https://arxiv.org/pdf/2611.22464v1), Section 3.2, p.6) |
| update_strategy | Local Patch, Replanning | Agent-generated edit programs update the current scene; verification inconsistencies trigger further edits or explicit justifications. ([source](https://arxiv.org/pdf/2611.22464v1), Sections 3.2-3.3, pp.5-6) |
| verifier | Programmatic | Verification tools evaluate reconstruction against measured video and geometric evidence. ([source](https://arxiv.org/pdf/2611.22464v1), Section 3.3, p.6) |
| feedback_assessment | Diagnosis | Checks report depth conflicts, uncovered evidence, occlusion violations, penetration, support, and completeness issues as diagnostics. ([source](https://arxiv.org/pdf/2611.22464v1), Section 3.3, pp.6-8) |
| feedback_observation | Structural Scene State, Visual | Observations include structural measurements and diagnostic renderings/scene consistency checks. ([source](https://arxiv.org/pdf/2611.22464v1), Figure 3 p.4; Section 3.3 p.6) |
| memory_time | Short-Term Memory | R_{n-1} records previous queries, edits, and verification feedback within the iterative run. ([source](https://arxiv.org/pdf/2611.22464v1), Section 3.2, p.6) |
| memory_reach | Local Memory | The state record conditions the single agent's next operation. ([source](https://arxiv.org/pdf/2611.22464v1), Section 3.2, p.6) |
| action_type | Code/Script | Blender executes agent-generated edit programs. ([source](https://arxiv.org/pdf/2611.22464v1), Section 3.2, p.5) |
| graphics_software | Agent-Adapted | The method adds metric observation, evidence querying, and verification tools around Blender for agentic scene construction. ([source](https://arxiv.org/pdf/2611.22464v1), Sections 3.2, 4.1, pp.5-6) |
| tools | Graphics Operations, Perception models, Static Validator | The workflow uses geometric recovery/perception, Blender graphics edits, and static geometric/video consistency validators. ([source](https://arxiv.org/pdf/2611.22464v1), Sections 3.1-3.3, pp.3-6) |
| resources | Documentation & Rules | The agent receives a task description and tool documentation; no reusable asset library is reported for the principal loop. ([source](https://arxiv.org/pdf/2611.22464v1), Sections 3.2, 4.1, pp.5-6) |
| representation | Code, Geometry, Pixels | Edit programs are code, scene primitives and characters are geometry, and final aligned blockout videos are rendered pixels/media. ([source](https://arxiv.org/pdf/2611.22464v1), Sections 2.1, 3.2-3.3, pp.2,5-6) |

Events: [{"type": "first_submission", "value": "2026-11-17T09:25:47+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2611.22464", "authority": "primary", "evidence": "arXiv metadata records version 1 published on 17 Nov 2026.", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: []

### [CADMAGEDDON: High-Fidelity CAD Reconstruction with Local Inference](https://arxiv.org/abs/2611.22563)
core | High | new_relative_to_snapshot
Application: Static / CAD; operations: Reconstruction, Editing, Generation
CADMAGEDDON separates structural CAD decisions from numerical fitting: a local VLM agent composes feature operations over named fitted geometry, with executable CadQuery/FreeCAD output and residual-driven correction.
Scope: The VLM agent directly operates a CAD environment: it selects named geometric entities and operations, emits executable CAD programs, and uses residual/validity feedback to add, correct, undo, or drop features.
Limits: The method assumes a clean single-part mesh; scan noise, missing regions, assemblies, and design intent beyond literal dimensions remain unresolved. It uses up to 30 or 60 model calls and is slower than single-pass learned models. Benchmark comparisons vary in input modality and subset.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Modeling | Mesh-to-editable-CAD reconstruction and feature modeling. ([source](https://arxiv.org/pdf/2611.22563v1), Section 3, p.4) |
| input_form | 3D Representation | The agent receives a triangle mesh of a single part. ([source](https://arxiv.org/pdf/2611.22563v1), Abstract p.1; Section 3 p.4) |
| output | Program, Graphics Artifact, Structured Specification | The system returns executable CadQuery or native FreeCAD programs and editable CAD geometry. ([source](https://arxiv.org/pdf/2611.22563v1), Sections 3, 4.4, pp.4,10) |
| model_type | VLM | A vision-language model Qwen3.8-27B makes feature decisions from visual/text tool outputs. ([source](https://arxiv.org/pdf/2611.22563v1), Sections 1-3, pp.1-4) |
| model_training | Off-the-Shelf | The paper uses a single open-weight Qwen3.8-27B and states no trained reconstruction model is needed. ([source](https://arxiv.org/pdf/2611.22563v1), Sections 1-3, pp.1-4) |
| planning | PO-3 | The loop is one command per turn with tool selection and feature decisions; no separate plan object is described. ([source](https://arxiv.org/pdf/2611.22563v1), Sections 3.5-3.6, pp.7) |
| workflow | Sequential | It executes a sequential trajectory of inspect, construct, verify, and correct commands. ([source](https://arxiv.org/pdf/2611.22563v1), Sections 3.4-3.5, pp.6-7) |
| update_strategy | Local Patch, Replanning, Rollback | Features can be replaced, undone, dropped, mirrored, or patterned; residuals guide further actions. ([source](https://arxiv.org/pdf/2611.22563v1), Sections 3.4-3.5, pp.6-7) |
| verifier | Programmatic, Environment | The builder checks CAD validity and computes missing/extra residuals; the environment executes operations. ([source](https://arxiv.org/pdf/2611.22563v1), Sections 3.4-3.5, pp.6-7) |
| feedback_assessment | Diagnosis, Score | Residual volume and local surface deviations provide numeric discrepancy/diagnostic evidence. ([source](https://arxiv.org/pdf/2611.22563v1), Figure 1 p.5; Section 3.4 p.6) |
| feedback_observation | Structural Scene State, Visual | Tool reports and renders expose named geometry, current state, residual missing/extra bodies, and visual distance views. ([source](https://arxiv.org/pdf/2611.22563v1), Sections 3.3-3.4, pp.6) |
| memory_time | Short-Term Memory | Recent command outputs, renders, summaries, and saved states persist within a reconstruction run. ([source](https://arxiv.org/pdf/2611.22563v1), Section 3.5, p.7) |
| memory_reach | Local Memory | The retained context is used by the single agent across turns; no cross-agent/global memory is reported. ([source](https://arxiv.org/pdf/2611.22563v1), Section 3.5, p.7) |
| action_type | Tool/Function Call, Code/Script, Structured Specification | The model issues CLI commands and the builder emits/executes CAD code. ([source](https://arxiv.org/pdf/2611.22563v1), Sections 3.3-3.4, pp.6) |
| graphics_software | Agent-Adapted | Agent-facing instruments and DSL wrap CadQuery/FreeCAD for interactive reconstruction. ([source](https://arxiv.org/pdf/2611.22563v1), Sections 1-4, pp.1-10) |
| tools | Graphics Operations, Solver Validator, Static Validator, Perception models | Geometric detectors/fitting, CAD operations, renders, and residual/validity checks are callable workflow tools. ([source](https://arxiv.org/pdf/2611.22563v1), Sections 3.2-3.4, pp.5-6) |
| resources | Documentation & Rules | The system prompt contains a reconstruction guide and command/tool documentation. ([source](https://arxiv.org/pdf/2611.22563v1), Sections 3.5-3.6, p.7) |
| representation | Code, Geometry, Pixels | Executable CAD code and named geometric entities are used; rendered views are observations and editable geometry is the artifact. ([source](https://arxiv.org/pdf/2611.22563v1), Sections 3.2-3.4, pp.5-6) |

Events: [{"type": "first_submission", "value": "2026-11-17T10:48:35+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2611.22563", "authority": "primary", "evidence": "arXiv metadata records version 1 published on 17 Nov 2026.", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: []

### [MillBill: A Machining Agent with Geometric Feedback](https://arxiv.org/abs/2611.22565)
core | High | new_relative_to_snapshot
Application: Static / CAD, Dynamic / Physical simulation and effects; operations: Generation, Reconstruction, Other
MillBill separates machining decisions from their geometric execution and verification: a local language-model controller proposes operation sequences, tools, and parameters, while a geometric harness generates toolpaths, simulates material removal, scores deviations, and feeds corrections back.
Scope: The language-model controller directly selects machining actions on a CAD/CAM graphics representation and receives simulated geometric feedback that changes subsequent plans.
Limits: MillBill is limited to indexed three-axis machining from six principal directions; workholding, machine travel, tool-holder collisions, tool deflection, wear, vibration, thread verification, and real-machine effects are not modeled. It is evaluated on 100 parts from one public library and one run per part.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Simulation | The principal subsystem plans and simulates physical machining of a CAD part; the graphics purpose is physical/CAM simulation. ([source](https://arxiv.org/pdf/2611.22565v1), Abstract p.1; Sections 3.4-3.5 pp.5-6) |
| input_form | 3D Representation | Input is a STEP B-rep target part, stock, material, and optional drawing notes. ([source](https://arxiv.org/pdf/2611.22565v1), Problem definition, p.3) |
| output | Program, Structured Specification, Graphics Artifact | The workflow exposes structured machining plans, G-code programs, and simulated workpiece state. ([source](https://arxiv.org/pdf/2611.22565v1), Sections 3.3-3.5, pp.4-6) |
| model_type | LLM | Qwen3.8-27B language model ReAct agents make process-sequence and tool-selection decisions. ([source](https://arxiv.org/pdf/2611.22565v1), Sections 3.3, S1 pp.4,13) |
| model_training | Off-the-Shelf | The paper explicitly says an off-the-shelf open model makes decisions and no training on machining plans/toolpaths is needed. ([source](https://arxiv.org/pdf/2611.22565v1), Section 2, p.2; S1 p.13) |
| planning | PO-2 | A fixed harness prepares an initial plan; three ReAct sub-agents retrieve knowledge, revise process sequence, and select tools/parameters. ([source](https://arxiv.org/pdf/2611.22565v1), Sections 3.2-3.3, pp.4-5) |
| workflow | Sequential, Parallel | Knowledge retrieval sub-agents run concurrently, while setup-wise plan-execute-verify-refine cycles are sequential. ([source](https://arxiv.org/pdf/2611.22565v1), Sections 3.3-3.6, pp.4-6) |
| update_strategy | Local Patch, Replanning, Candidate Selection | Harness applies direct corrections/rest finishing, model proposes minimal fixes, plan is rebuilt, and best of up to three builds is kept. ([source](https://arxiv.org/pdf/2611.22565v1), Section 3.6, p.6) |
| verifier | Programmatic, Environment | Geometric simulation, gouge/safety checks, and surface deviation measurement verify every program. ([source](https://arxiv.org/pdf/2611.22565v1), Sections 3.4-3.5, pp.5-6) |
| feedback_assessment | Score, Diagnosis, Ranking | Acc_tau is a numeric score; deviations are diagnosed by feature/operation; builds are ranked and the best retained. ([source](https://arxiv.org/pdf/2611.22565v1), Sections 3.5-3.6, pp.6) |
| feedback_observation | Structural Scene State, Runtime | Feedback includes simulated workpiece structural state, excess/gouge regions, and execution/safety issues. ([source](https://arxiv.org/pdf/2611.22565v1), Figure 1 p.3; Sections 3.5-3.6 pp.5-6) |
| memory_time | Short-Term Memory | Agent stages share current plan, operation state, and prior build feedback within one part run. ([source](https://arxiv.org/pdf/2611.22565v1), Sections 3.3, 3.6 pp.4,6) |
| memory_reach | Local Memory | The local planner/harness loop uses the retained state; no global cross-agent memory is reported. ([source](https://arxiv.org/pdf/2611.22565v1), Sections 3.3, 3.6 pp.4,6) |
| action_type | Structured Specification, Tool/Function Call | Agents return structured JSON operation plans and call harness tools; harness emits G-code. ([source](https://arxiv.org/pdf/2611.22565v1), Sections 3.3-3.4 pp.4-5) |
| graphics_software | Agent-Adapted | The method adds an agent/harness layer around FreeCAD CAM and geometric simulation. ([source](https://arxiv.org/pdf/2611.22565v1), Sections 3.4-3.5 pp.5-6) |
| tools | Graphics Operations, Solver Validator, Static Validator, Perception models, Execution Utilities | AAGNet perception, CAM graphics operations, toolpath generation, simulation/solver validation, static safety checks, and execution utilities are used. ([source](https://arxiv.org/pdf/2611.22565v1), Sections 3.1-3.6 pp.3-6) |
| resources | Examples & Trajectories, Documentation & Rules | The workflow retrieves machining guidelines, rules, thread tables, material knowledge, and tool-library data; it also uses reference operation sequences. ([source](https://arxiv.org/pdf/2611.22565v1), Section 3.3 and S1 pp.4-5,13) |
| representation | Code, Geometry, Dynamic State | Plans/G-code are code and structured specifications, B-rep/workpiece are geometry, and simulated removal is dynamic state. ([source](https://arxiv.org/pdf/2611.22565v1), Sections 3.3-3.5 pp.4-6) |

Events: [{"type": "first_submission", "value": "2026-11-17T10:52:45+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2611.22565", "authority": "primary", "evidence": "arXiv metadata records version 1 published on 17 Nov 2026.", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: []

### [CutAgent: Creative-Gene-Driven Planning and Experience-Guided Self-Refinement for High-CTR E-commerce Advertising Video Creation](https://arxiv.org/abs/2611.22418)
core | High | new_relative_to_snapshot
Application: Dynamic / Animation and temporal scene, 2D Graphics; operations: Generation, Editing
CutAgent separates conversion-oriented creative planning from video production using a structured creative gene, then adds reflection-based local revision and category/gene-conditioned long-term experience reuse.
Scope: CutAgent demonstrates agents making structured planning, retrieval, editing, and rendering decisions over advertising video artifacts, with explicit visual/audio evaluation and iterative correction.
Limits: The pipeline depends on retrieved product-specific clip pools and automated multimodal evaluation; the paper notes that VSC is a relative signal because evaluator spatial reasoning is weak. The principal production agent is complex and its learned components are trained on proprietary-scale e-commerce data, limiting direct transferability. Retrieved footage cannot cover a shot when suitable material is absent.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Animation | Principal task is planning and producing short advertising videos with ordered narrative units and temporal shots. ([source](https://arxiv.org/pdf/2611.22418v1), Sections 3.1-3.3, pp.3-7) |
| input_form | Language, Image | Product attributes, review text, and main/detail product images are provided. ([source](https://arxiv.org/pdf/2611.22418v1), Sections 3.1-3.2, pp.3-4) |
| output | Structured Specification, Rendered Media | GeneAgent outputs structured creative genes/storyboards; VideoAgent renders complete advertising videos. ([source](https://arxiv.org/pdf/2611.22418v1), Abstract p.1; Sections 3.2-3.3 pp.3-7) |
| model_type | Hybrid | GeneAgent is a VLM and VideoAgent is an LLM-driven production agent with multimodal retrieval and rendering tools. ([source](https://arxiv.org/pdf/2611.22418v1), Sections 3.2-3.3, pp.3-7) |
| model_training | Supervised Fine-Tuning, RL Post-Training | GeneAgent uses high-CTR supervised fine-tuning and CTR-guided GRPO; VideoAgent's task-time model configuration is separately described. ([source](https://arxiv.org/pdf/2611.22418v1), Sections 3.2.4-3.2.7, pp.4-6) |
| planning | PO-3 | GeneAgent explicitly emits an ordered creative gene before clip selection, and VideoAgent expands it into an executable shot-by-shot storyboard. ([source](https://arxiv.org/pdf/2611.22418v1), Sections 3.1-3.2, pp.3-5) |
| workflow | Sequential | The system follows Plan–Execute–Self-Evolve: gene planning, video production, then reflection and revision. ([source](https://arxiv.org/pdf/2611.22418v1), Sections 3.1, 3.3, pp.3,6-7) |
| update_strategy | Local Patch, Replanning | Reflection revises only affected clips, voice-over, duration, or music and re-executes relevant modules; memory stores verified corrections. ([source](https://arxiv.org/pdf/2611.22418v1), Section B.5, p.15) |
| verifier | Critic, Programmatic | An evaluator produces six-dimensional scores and temporally grounded evidence; verification re-evaluates the revised video. ([source](https://arxiv.org/pdf/2611.22418v1), Section B.5, p.15) |
| feedback_assessment | Score, Diagnosis | NQ, SPC, VSC, MQA, MSS, and TB scores diagnose deficient decisions and determine acceptance. ([source](https://arxiv.org/pdf/2611.22418v1), Sections 4.3.1, B.5, pp.7,15-16) |
| feedback_observation | Visual, Runtime | Feedback is grounded in video frames, shot intervals, audio/subtitle segments, and editing elements; execution failures are localized to production modules. ([source](https://arxiv.org/pdf/2611.22418v1), Section B.5, p.15) |
| memory_time | Long-Term Memory | Verified failure-correction experiences are retained and reused across future products without parameter updates. ([source](https://arxiv.org/pdf/2611.22418v1), Section 3.3.4, p.6) |
| memory_reach | Global Memory | Memory is shared across products through category shards and gene matching, rather than restricted to one shot or one call. ([source](https://arxiv.org/pdf/2611.22418v1), Section 3.3.4, p.6) |
| action_type | Structured Specification, Tool/Function Call | Agents emit structured creative genes/storyboards and invoke retrieval, TTS, BGM, and rendering tools. ([source](https://arxiv.org/pdf/2611.22418v1), Sections 3.2-3.3, pp.3-7) |
| graphics_software | Agent-Adapted | The system adds agent-facing retrieval, TTS, music matching, subtitle, and ffmpeg timeline tooling around general video assets. ([source](https://arxiv.org/pdf/2611.22418v1), Sections 3.3.2, B.1-B.4, pp.6,14-15) |
| tools | Graphics Operations, Perception models, Execution Utilities, Static Validator | Video retrieval/perception, clip/audio/timeline operations, ffmpeg execution, and static/quality checks are callable components. ([source](https://arxiv.org/pdf/2611.22418v1), Sections 3.3.2, B.1-B.4, pp.6,14-15) |
| resources | Assets, Examples & Trajectories, Documentation & Rules | The workflow accesses product clip pools, historical failure-correction examples, production rules, and audio/video assets. ([source](https://arxiv.org/pdf/2611.22418v1), Sections 3.2.2, 3.3.4, B.1-B.3, pp.4,6,14-15) |
| representation | Layouts, Pixels, Learned State | Creative genes/storyboards are structured layouts/specifications; rendered videos are pixels/media; learned state includes the trained GeneAgent policy. ([source](https://arxiv.org/pdf/2611.22418v1), Sections 3.2-3.3, pp.3-7) |

Events: [{"type": "first_submission", "value": "2026-11-17T08:54:39+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2611.22418", "authority": "primary", "evidence": "ArXiv metadata records version 1 published on 17 Nov 2026.", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: []

### [ConserveEdit: Source-Anchored Transactions for Drift-Bounded Iterative Image Editing](https://arxiv.org/abs/2611.22724)
core | High | new_relative_to_snapshot
Application: 2D Graphics; operations: Editing, Auditing
ConserveEdit treats each refinement as a source-anchored transaction with provable invariance and an iteration-independent drift bound, using separate progress, drift, and quality gates plus rollback and logged repair.
Scope: The paper demonstrates a controller that operates on image-editing artifacts at task time: it chooses and commits/rolls back candidate edits against a persistent source contract, with explicit graphics artifact targets and programmatic feedback.
Limits: Guarantees apply only to the grounded support and selected descriptors; poor grounding is the main bottleneck. The paper evaluates one frozen editor and MagicBrush, uses fixed-formula predicates rather than an MLLM judge, and reports abstention/seam failures and no human preference study. The controller can preserve the wrong content if descriptors or masks miss a causal dependency.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Modeling | The task is iterative instruction-based image editing with preservation constraints. ([source](https://arxiv.org/pdf/2611.22724v1), Sections 3.1-3.3, pp.3-5) |
| input_form | Language, Image | A source image and free-form instruction are inputs; MagicBrush also supplies edit masks. ([source](https://arxiv.org/pdf/2611.22724v1), Section 3.1, p.3; Section 4.1 p.5) |
| output | Graphics Artifact, Rendered Media | The controller returns committed edited images or the source after abstention/rollback. ([source](https://arxiv.org/pdf/2611.22724v1), Sections 3.3-4.1, pp.4-6) |
| model_type | Not Applicable | ConserveEdit itself uses no LLM or MLLM; it uses fixed formulas, detectors, segmentation, face, OCR, and frozen image editors. ([source](https://arxiv.org/pdf/2611.22724v1), LLM Usage Statement p.8) |
| model_training | Not Applicable | The controller is not trained; frozen executor and fixed evaluators are used. ([source](https://arxiv.org/pdf/2611.22724v1), LLM Usage Statement p.8) |
| planning | PO-1 | The controller follows a fixed algorithm: choose an unsatisfied clause, propose candidates, audit, commit or repair. ([source](https://arxiv.org/pdf/2611.22724v1), Algorithm 1 p.5) |
| workflow | Sequential | Iterations proceed sequentially over current image state and decision log. ([source](https://arxiv.org/pdf/2611.22724v1), Algorithm 1 p.5) |
| update_strategy | Local Patch, Rollback, Candidate Selection | Masked local commits, rollback on rejection, repair, and lexicographic candidate selection are explicit. ([source](https://arxiv.org/pdf/2611.22724v1), Sections 3.3, Algorithm 1 pp.4-5) |
| verifier | Programmatic | Fixed descriptors, masks, progress predicates, quality score, and drift audits decide feasibility. ([source](https://arxiv.org/pdf/2611.22724v1), Sections 3.2-3.3 pp.3-4) |
| feedback_assessment | Binary, Score, Diagnosis | Drift and quality are numeric scores; clause/progress and feasibility tests diagnose violated conditions and produce binary commit/reject decisions. ([source](https://arxiv.org/pdf/2611.22724v1), Equations 5-8 pp.4-5) |
| feedback_observation | Visual, Structural Scene State | Observations include pixel/feature drift, masks, image quality, and protected-entity/scene state. ([source](https://arxiv.org/pdf/2611.22724v1), Sections 3.2-3.3 pp.3-4) |
| memory_time | Short-Term Memory | Persistent contract, cumulative support, current image, and decision log persist across iterations of one run. ([source](https://arxiv.org/pdf/2611.22724v1), Sections 3.2-3.3 pp.3-5) |
| memory_reach | Local Memory | State is consumed by the single controller loop; no shared multi-agent memory is described. ([source](https://arxiv.org/pdf/2611.22724v1), Sections 3.2-3.3 pp.3-5) |
| action_type | Tool/Function Call | The controller invokes a frozen editor, mask composition, audits, and repair operations. ([source](https://arxiv.org/pdf/2611.22724v1), Sections 3.3-4.1 pp.4-6) |
| graphics_software | Agent-Adapted | The controller wraps frozen Qwen-Image-Edit/FLUX editors with a source-anchored transaction interface. ([source](https://arxiv.org/pdf/2611.22724v1), Sections 3.3, 4.1 pp.4-6) |
| tools | Graphics Operations, Perception models, Static Validator | Frozen image editing is the graphics operation; Grounding DINO/SAM, CLIP/DINO descriptors, face/OCR checks, and quality audits are callable components. ([source](https://arxiv.org/pdf/2611.22724v1), Sections 3.2-4.1 pp.3-6) |
| resources | Documentation & Rules | The controller uses a persistent edit contract and explicit preservation/quality rules. ([source](https://arxiv.org/pdf/2611.22724v1), Sections 3.2-3.3 pp.3-5) |
| representation | Pixels, Layouts | The state and output are image pixels; masks/contracts encode structured 2D layout/support information. ([source](https://arxiv.org/pdf/2611.22724v1), Sections 3.1-3.3 pp.3-5) |

Events: [{"type": "first_submission", "value": "2026-11-17T12:58:37+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2611.22724", "authority": "primary", "evidence": "ArXiv metadata records version 1 published on 17 Nov 2026.", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: []

## same_day_updates (0)

## late_discovery (0)

## date_unresolved (0)

## unresolved (0)

## excluded (0)

## Application index
| Application | Papers |
|---|---|
| 2D Graphics | [CutAgent: Creative-Gene-Driven Planning and Experience-Guided Self-Refinement for High-CTR E-commerce Advertising Video Creation](https://arxiv.org/abs/2611.22418) [same_day_new]; [ConserveEdit: Source-Anchored Transactions for Drift-Bounded Iterative Image Editing](https://arxiv.org/abs/2611.22724) [same_day_new] |
| Static / Object | None verified in this run |
| Static / CAD | [CADMAGEDDON: High-Fidelity CAD Reconstruction with Local Inference](https://arxiv.org/abs/2611.22563) [same_day_new]; [MillBill: A Machining Agent with Geometric Feedback](https://arxiv.org/abs/2611.22565) [same_day_new] |
| Static / Scene | [MAVE: Reconstructing Editable 3D Blockouts from Film Shots](https://arxiv.org/abs/2611.22464) [same_day_new] |
| Dynamic / Articulated assets | None verified in this run |
| Dynamic / Animation and temporal scene | [MAVE: Reconstructing Editable 3D Blockouts from Film Shots](https://arxiv.org/abs/2611.22464) [same_day_new]; [CutAgent: Creative-Gene-Driven Planning and Experience-Guided Self-Refinement for High-CTR E-commerce Advertising Video Creation](https://arxiv.org/abs/2611.22418) [same_day_new] |
| Dynamic / Physical simulation and effects | [MillBill: A Machining Agent with Geometric Feedback](https://arxiv.org/abs/2611.22565) [same_day_new] |
| Datasets and Benchmarks | None verified in this run |
| Cross-category | None verified in this run |

## Source ledger
| Source | Status | Checked pages / queries | Limitations |
|---|---|---|---|
| arxiv | complete | [{"query_or_url": "https://arxiv.org/list/cs.GR/new?skip=0&show=100", "checked_at": "2026-11-19T00:52:50.576696+00:00", "outcome": "complete observed pagination; 16 entries"}, {"query_or_url": "https://arxiv.org/list/cs.GR/recent?skip=0&show=100", "checked_at": "2026-11-19T00:52:50.648719+00:00", "outcome": "complete observed pagination; 42 entries"}, {"query_or_url": "https://arxiv.org/list/cs.CV/new?skip=0&show=2000", "checked_at": "2026-11-19T00:52:55.364270+00:00", "outcome": "complete observed pagination; 322 entries"}, {"query_or_url": "https://arxiv.org/list/cs.CV/recent?skip=0&show=2000", "checked_at": "2026-11-19T00:52:56.333557+00:00", "outcome": "complete observed pagination; 985 entries"}] | Only cs.GR and cs.CV were scanned; other planned arXiv categories were not reached. Coverage is listing-complete for observed pages, not literature-exhaustive. |
| hugging_face | not_reached_within_budget | [] | hf_daily was requested but no usable observation was returned before attention shifted to the arXiv catalog; no HF claims are made. |
| openreview | not_reached_within_budget | [] | No OpenReview search observation was obtained. |
| official_venues | not_reached_within_budget | [] | No official venue/proceedings search observation was obtained. |
| project_author_lab | not_reached_within_budget | [] | No separate project/author/lab search observation was obtained. |

## Query coverage
- 2d: not_reached_within_budget; []
- object: not_reached_within_budget; []
- cad: partial; [{'query_or_url': 'prepared query plan: agent CAD generation reconstruction editing constraint solver', 'checked_at': '2026-11-19T00:53:30.323128+00:00', 'outcome': 'covered by arXiv catalog abstracts; no separate web query'}]
- scene: partial; [{'query_or_url': 'prepared query plan: agent 3D scene layout world generation reconstruction editing', 'checked_at': '2026-11-19T00:53:30.323128+00:00', 'outcome': 'covered by arXiv catalog abstracts; no separate web query'}]
- articulation: not_reached_within_budget; []
- animation: partial; [{'query_or_url': 'prepared query plan: agent animation cutscene temporal world scene cinematography', 'checked_at': '2026-11-19T00:53:30.323128+00:00', 'outcome': 'covered by arXiv catalog abstracts; no separate web query'}]
- simulation: not_reached_within_budget; []
- benchmark: partial; [{'query_or_url': 'prepared query plan: agent graphics benchmark world auditing verification', 'checked_at': '2026-11-19T00:53:30.323128+00:00', 'outcome': 'covered by arXiv catalog abstracts; no separate web query'}]
- harness: partial; [{'query_or_url': 'prepared query plan: graphics agent memory replanning tool interface feedback program synthesis', 'checked_at': '2026-11-19T00:53:30.323128+00:00', 'outcome': 'covered by arXiv catalog abstracts and retained papers; no separate web query'}]

## Source-derived candidate coverage

Mechanical audit of collected arXiv titles; relevance and semantic correctness require paper evidence.

- Metadata resolved: 1098 / 1098 collected IDs.
- Target-day / history-uncertain candidates: 235.
- Explicit triage decisions: 0; catalog-page delivery: 235.
- Missing source scans: 0; incomplete scans: 0.
- Unresolved metadata: 0; no triage decision: 235.
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
| MAVE: Reconstructing Editable 3D Blockouts from Film Shots | core | LLM-based agent evaluated with MAVE's tool and evidence interface | Generates Blender edit programs, queries evidence, and chooses further edits or justifications in a query-edit-verify loop | Editable Blender 3D blockout scene containing camera, geometry, and rigged human proxies | [Sections 3.2-3.3, pp.5-6](https://arxiv.org/pdf/2611.22464v1) |
| CADMAGEDDON: High-Fidelity CAD Reconstruction with Local Inference | core | Qwen3.8-27B vision-language model in the CADMAGEDDON command loop | Selects named planes, profiles, operations, and corrections; issues one CAD command per turn and can undo/drop/replace features | Editable CadQuery or native FreeCAD parametric CAD program and resulting solid | [Sections 3.2-3.5, pp.5-7](https://arxiv.org/pdf/2611.22563v1) |
| MillBill: A Machining Agent with Geometric Feedback | core | Qwen3.8-27B ReAct planning agents | Revises operation sequence, cutter selection, cutting parameters, and minimal corrective fixes through harness tool calls | B-rep CAD part, FreeCAD CAM job, generated toolpaths/G-code, and simulated workpiece | [Sections 3.3-3.6, pp.4-6](https://arxiv.org/pdf/2611.22565v1) |
| CutAgent: Creative-Gene-Driven Planning and Experience-Guided Self-Refinement for High-CTR E-commerce Advertising Video Creation | core | GeneAgent plus VideoAgent collaborative controller | Generates a structured creative gene, expands it into shot scripts, retrieves assets, renders the timeline, and revises affected production modules from temporally grounded evaluation feedback | E-commerce advertising video timeline, including clips, narration, subtitles, music, and transitions | [Sections 3.1-3.3 and B.5, pp.3-7,15](https://arxiv.org/pdf/2611.22418v1) |
| ConserveEdit: Source-Anchored Transactions for Drift-Bounded Iterative Image Editing | core | ConserveEdit transactional controller around frozen Qwen-Image-Edit/FLUX executors | Selects candidate edits, commits feasible masked transactions, or rolls back and repairs based on source-anchored progress/drift/quality audits | 2D image artifact and protected source content | [Sections 3.2-3.3, pp.3-5](https://arxiv.org/pdf/2611.22724v1) |

## Prior-day memory and carry-over

Frozen history: `knowledge/daily-history/through-20261015-bvb-v11`. Previously unread records now fully read: 0. Prior pending records still without a new full read: 95.

See history-delta.json for per-paper transitions. Historical results remain in the frozen bundle; not repeated is not excluded, and new-to-history does not mean newly published.

## Abstract-first reading queue

Attention pool: 337; abstracts not delivered: 102; priority/triage gaps: 337; unread ranked leads: 332. See reading-plan.json for model-authored priorities and deferred leads. Priority is not an inclusion judgment or recall guarantee.
