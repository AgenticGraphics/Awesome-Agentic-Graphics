# Agentic Graphics daily report
Date: 2026-11-02 | Timezone: America/Chicago | As of: 2026-11-07T21:04:38+00:00
browser-based same-day search; documented source coverage
Taxonomy: google-doc-taxonomy-v3-2026-10-15 | Snapshot: authorized_live_snapshot_reconciled_and_frozen

## Coverage limits
- Partial bounded report, not exhaustive discovery. Harness explicitly instructed FINALIZE NOW at turn 42 (elapsed 1025 seconds, estimated model cost $37.042), citing time or estimated-cost reserve. Stopped new PDF reads, despite remaining nominal 30-minute budget and direct-action queue. PhotoGuider v2 downloaded but not read; three reserved backlog slots not reached.
- Preserved frozen execution frame, cutoff, taxonomy and snapshot_status. Actual source checks were later than cutoff; accepted event/version timestamps remain at or before frozen cutoff.
- Five verified core and two borderline target-day first submissions; no qualifying target-day revision verified. No older catch-up or backlog PDF completed. Do not interpret this as zero relevant older work.
- All 283 target_and_uncertain and 333 catchup_review entries were delivered and individually triaged before first PDF. Source catalog has 1062 identities; metadata complete, but attention pool is not all-source relevance review.
- Reading queue: reading-plan.json ranked_unread; supplementary outside-catalog plausible leads: deferred-extra-queue.json; complete remaining plausible decisions: all-unread-plausible.json. Additional search citations: additional-source-leads.json. Triaged rejection is provisional unless primary content explicitly supports it; no title-only final exclusions created.
- Title hints reviewed individually; later-than-target hints have date-only provisional deferrals, not scope exclusions. Non-hint matched/unmatched full abstracts in attention pool considered. Remaining non-attention source abstracts not claimed screened.
- Prior pending INDEX and selected detail files inspected; three backlog slots reserved in backlog-plan.json but unfilled due harness finalization instruction. No historical record counted as newly read.
- PhotoGuider v2 is downloaded but unread; unresolved record preserves both v1 and v2 dates. EvoDesign, WorldAct and NeoWorld-Pro histories show no event in target/lookback, so they were not substituted for target-day work.
- OpenReview and venue/project searches remain partial; HF curated entries are not fully independently screened. Other arXiv categories not scanned.
- No diagram pixel renders used; taxonomy grounded in delivered full PDF text and targeted mechanism searches. Abstract fields in retained records are concise summaries, not verbatim quotations.
- Final mechanical audit inspected: 4/4 required source pools, 1062/1062 listing metadata records resolved, 283/283 date-focus entries delivered and triaged, no metadata/rank/priority gaps in declared pools. Still 51 plausible unread decisions across linked queues, including 9 supplementary deferred entries; shared ranked_unread reports 45 because its routing also retains saved unresolved leads. Frozen history has 95 pending IDs and 38 previously retained IDs not repeated. All opened arXiv pages have saved decisions; no delivered PDF lacks a saved reading record. These are mechanical coverage facts, not semantic completeness.

## already_reported (0)

## same_day_new (7)

### [Parametric CAD Bench v3: Evaluating Agentic Parametric CAD Authoring from Text and Engineering Drawings](https://arxiv.org/abs/2611.02659)
core | High | new_relative_to_snapshot
Application: Static / CAD, Datasets and Benchmarks; operations: Generation, Reconstruction, Editing
Native parametric artifact evaluation separates geometric similarity from CAD specification compliance across 100 tasks and 13 systems; top overall mean reward is 61.03%, not a success rate.
Scope: Evaluates agents executing native FreeCAD authoring scripts, not merely predicting CAD descriptions.
Limits: Single final trials, curated single-body tasks, heuristic scores and reference-construction sensitivity limit generalization. Artifact scoring does not certify preserved edit history or arbitrary future editability. Agent internals are sparsely reported.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Modeling | Creation, create-and-edit and drawing-to-CAD tasks. ([source](https://arxiv.org/pdf/2611.02659v1), §3.1 p.4) |
| input_form | Language, Image | Part descriptions and edit instructions; engineering drawings are geometry input. ([source](https://arxiv.org/pdf/2611.02659v1), Table 1 p.4; p.8) |
| output | Program, Graphics Artifact | Output contract requires answer.py and answer.FCStd with native editable features. ([source](https://arxiv.org/pdf/2611.02659v1), Appendix B p.19) |
| model_type | VLM | Opus 5.5 mini-swe-agent receives full image payloads through a multimodal channel. ([source](https://arxiv.org/pdf/2611.02659v1), §5.2 pp.12–13) |
| model_training | Not Reported | Provider configurations and unknown training data are discussed; task adaptation regime is not specified. ([source](https://arxiv.org/pdf/2611.02659v1), §5–6 pp.12–17, Appendix A p.19) |
| planning | Not Reported | Agent configurations reported without plan representation. ([source](https://arxiv.org/pdf/2611.02659v1), §4–5; Appendix A) |
| workflow | Not Reported | Image transport is described, not the agent's internal dependency topology. ([source](https://arxiv.org/pdf/2611.02659v1), §5.2 pp.12–13) |
| update_strategy | Not Reported | Saved base and target do not establish actual reuse; repair policy not described. ([source](https://arxiv.org/pdf/2611.02659v1), §3–5 pp.4–16) |
| verifier | Not Reported | Separate held-out programmatic scorer evaluates final artifacts. ([source](https://arxiv.org/pdf/2611.02659v1), §4 pp.9–12) |
| feedback_assessment | Not Reported | Continuous scores are final evaluation rewards. ([source](https://arxiv.org/pdf/2611.02659v1), §4.2 pp.9–12) |
| feedback_observation | Not Reported | Task-image input transport reported; corrective observation stream not specified. ([source](https://arxiv.org/pdf/2611.02659v1), §5.2 pp.12–13) |
| memory_time | Not Reported | No retained controller-state lifetime described; memory search returned no matches. ([source](https://arxiv.org/pdf/2611.02659v1), Full text including Appendix A) |
| memory_reach | Not Reported | No memory sharing scope described. ([source](https://arxiv.org/pdf/2611.02659v1), Full text including Appendix A) |
| action_type | Code/Script | Write executable FreeCAD Python script. ([source](https://arxiv.org/pdf/2611.02659v1), p.8; Appendix B p.19) |
| graphics_software | General-Purpose | Native FreeCAD Python API and documents, no CAD-specific action abstraction required. ([source](https://arxiv.org/pdf/2611.02659v1), pp.3,8,19) |
| tools | Execution Utilities, Graphics Operations | Shell image bridge and executable native FreeCAD construction. ([source](https://arxiv.org/pdf/2611.02659v1), pp.8,12–13,19) |
| resources | Documentation & Rules | Shared output contract specifies native PartDesign modeling and file conventions. ([source](https://arxiv.org/pdf/2611.02659v1), Appendices B–C pp.19–25) |
| representation | Code, Geometry | Python programs and native B-rep geometry/feature histories. ([source](https://arxiv.org/pdf/2611.02659v1), pp.1,8,19) |

Events: [{"type": "first_submission", "value": "2026-11-02T07:19:55+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2611.02659", "authority": "primary", "version": "v1", "evidence": "Canonical submission history; Chicago 2026-11-02 01:19:55-06:00.", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: ["Benchmark verifier must be distinguished from agent-loop feedback; task create-and-edit does not imply local-patch strategy."]

### [Visual-to-Executable Procedural Reconstruction of Buildings](https://arxiv.org/abs/2611.03143)
core | High | new_relative_to_snapshot
Application: Static / Scene; operations: Reconstruction
Render-guided refinement reduces expert tree repair cost from 4.32 to 1.47 after two iterations; structured component prediction and deterministic compilation preserve editability.
Scope: A fine-tuned VLM revises executable facade structure from its rendered output; demonstrated graphics artifact action despite not branded an agent.
Limits: Only approximately planar visible facades are recovered; unseen sides use simple completion. Complex ornaments and severe occlusion remain difficult. No released code/checkpoints/training assets at submission; qualitative FaçAID comparisons are not identical-input benchmarks.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Modeling | Recover facade descriptions and instantiate building assets. ([source](https://arxiv.org/pdf/2611.03143v1), §3 p.3) |
| input_form | Image | Input is an in-the-wild building image. ([source](https://arxiv.org/pdf/2611.03143v1), §3 p.3) |
| output | Program, Graphics Artifact | Executable CGA program and instantiated editable 3D building asset. ([source](https://arxiv.org/pdf/2611.03143v1), §3 p.5; §4.1 p.6) |
| model_type | VLM | Qwen-VL-7B consumes RGB/mask and rendered schematic with YAML. ([source](https://arxiv.org/pdf/2611.03143v1), §3 pp.4–5) |
| model_training | Supervised Fine-Tuning | Two-stage supervised fine-tuning with LoRA, induction and repair examples. ([source](https://arxiv.org/pdf/2611.03143v1), Appendix D pp.16–17) |
| planning | Not Reported | Fixed reconstruction stages but no explicit task-plan representation; plan search only matches facade plane. ([source](https://arxiv.org/pdf/2611.03143v1), §3; Appendix D) |
| workflow | Sequential | Induction then render/rewrite iterations then component prediction and compilation. ([source](https://arxiv.org/pdf/2611.03143v1), §3 pp.4–5) |
| update_strategy | Regeneration | Reflection rewrites current YAML into revised symbolic program. ([source](https://arxiv.org/pdf/2611.03143v1), §3 p.5) |
| verifier | Self | Same fine-tuned model compares schematic and reference evidence. ([source](https://arxiv.org/pdf/2611.03143v1), §3 p.5) |
| feedback_assessment | Not Reported | Direct rewrite and sufficient agreement described; no emitted score, diagnosis or binary judgment specified. ([source](https://arxiv.org/pdf/2611.03143v1), §3 p.5; Appendix D) |
| feedback_observation | Visual, Structural Scene State | Reflection receives current YAML layout plus rendered schematic and RGB-mask overlay. ([source](https://arxiv.org/pdf/2611.03143v1), §3 p.5) |
| memory_time | Short-Term Memory | Yt retained and passed to next reflection call, up to two iterations. ([source](https://arxiv.org/pdf/2611.03143v1), §3 p.5) |
| memory_reach | Local Memory | Current layout is input to global reflection module. ([source](https://arxiv.org/pdf/2611.03143v1), §3 p.5) |
| action_type | Structured Specification | VLM emits schema-constrained YAML rather than low-level CGA. ([source](https://arxiv.org/pdf/2611.03143v1), §3 pp.4–5; Appendix B) |
| graphics_software | Agent-Adapted | Custom compiler maps layout and component schemas into CGA engine rules. ([source](https://arxiv.org/pdf/2611.03143v1), §3 p.5) |
| tools | Graphics Operations, Perception models | SAM3 segmentation; deterministic layout renderer and CGA compiler. ([source](https://arxiv.org/pdf/2611.03143v1), §3 pp.4–5) |
| resources | Documentation & Rules | Architectural regularity, grammar-validity priors and constrained schemas guide reflection. ([source](https://arxiv.org/pdf/2611.03143v1), §3 p.5; Appendix B) |
| representation | Code, Layouts, Pixels, Geometry | YAML/CGA, facade layouts, schematic images, instantiated building geometry. ([source](https://arxiv.org/pdf/2611.03143v1), §3 pp.4–5) |

Events: [{"type": "first_submission", "value": "2026-11-02T13:52:45+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2611.03143", "authority": "primary", "version": "v1", "evidence": "Canonical history; local 2026-11-02T07:52:45-06:00.", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: ["An artifact hierarchy is not a plan or graph workflow; direct YAML rewrite should not be conflated with evaluator node-edit operations."]

### [CounterSketch: Physics-Grounded Counterfactual Reasoning for Sketch-to-Video Generation](https://arxiv.org/abs/2611.04244)
core | Medium | new_relative_to_snapshot
Application: 2D Graphics, Dynamic / Animation and temporal scene; operations: Generation, Editing
Separates causal intervention reasoning from video synthesis; on 80 questions raises text-video alignment from 0.1682 to 0.2011 with fixed MoSketch renderer.
Scope: VLM intervention reasoning modifies vector sketches and physical scene graphs, then constraint violations trigger trajectory repair and semantic replanning.
Limits: Ambiguous grounding and unobservable mass/friction challenge physical validity. Implementation, controller adaptation and semantic verifier details are sparse; benchmark has only 20 base scenes.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Animation | Generate physically plausible sketch motion. ([source](https://arxiv.org/pdf/2611.04244v1), §3–4 p.4) |
| input_form | Image, Language | Sketch image and natural-language what-if prompt. ([source](https://arxiv.org/pdf/2611.04244v1), §3 p.4) |
| output | Structured Specification | Verified trajectories projected to per-frame motion bounding boxes for downstream synthesis. ([source](https://arxiv.org/pdf/2611.04244v1), §4.5 p.7) |
| model_type | VLM | VLM grounds sketch and reasons about causal interventions. ([source](https://arxiv.org/pdf/2611.04244v1), §4.1–4.2 p.5) |
| model_training | Not Reported | Gemini 3.8 Flash named for baselines, but proposed controller training regime not stated; no implementation appendix. ([source](https://arxiv.org/pdf/2611.04244v1), §4–5 pp.5–9; complete text) |
| planning | PO-2 | VLM generates explicit causal event sequence; fixed compiler/solver implements it. ([source](https://arxiv.org/pdf/2611.04244v1), §4.2–4.3 pp.5–6) |
| workflow | Graph-Structured | Numerical failures branch to local repair; semantic failures to event replanning. ([source](https://arxiv.org/pdf/2611.04244v1), §4.4/Fig.5 p.7) |
| update_strategy | Local Patch, Replanning | Parameter/constraint adjustments and local semantic replanning. ([source](https://arxiv.org/pdf/2611.04244v1), §4.4 p.7) |
| verifier | Programmatic | Checks geometric/physical constraints; updates accepted only if violations decrease. ([source](https://arxiv.org/pdf/2611.04244v1), §4.4/Fig.5 p.7) |
| feedback_assessment | Binary, Diagnosis | Per-constraint violation report; accept versus repair/replan. ([source](https://arxiv.org/pdf/2611.04244v1), Figs.3,5 pp.5,7) |
| feedback_observation | Structural Scene State | Checks generated trajectories against constraints and intervention compliance. ([source](https://arxiv.org/pdf/2611.04244v1), §4.4 p.7) |
| memory_time | Short-Term Memory | Evolving scene graph and event state retained during rollout and repair. ([source](https://arxiv.org/pdf/2611.04244v1), §4.2–4.4 pp.5–7) |
| memory_reach | Local Memory | Physical reasoning layer maintains graph and event state. ([source](https://arxiv.org/pdf/2611.04244v1), §4 pp.5–7) |
| action_type | Structured Specification | Events encode affected objects, event type, conditions and updated scene graph. ([source](https://arxiv.org/pdf/2611.04244v1), §4.2 p.5) |
| graphics_software | Agent-Adapted | Custom trajectory controls condition existing MoSketch renderer. ([source](https://arxiv.org/pdf/2611.04244v1), §4.5–5.2 p.7) |
| tools | Graphics Operations, Solver Validator, Static Validator | Vector intervention, constrained dynamics solve, trajectory verification. ([source](https://arxiv.org/pdf/2611.04244v1), §4.2–4.4 pp.6–7) |
| resources | Documentation & Rules | Physical rules for support, gravity, contact and conservation. ([source](https://arxiv.org/pdf/2611.04244v1), Fig.4; §4.3 p.6) |
| representation | Layouts, Dynamic State | Vector strokes, scene layouts and time-indexed positions/velocities. ([source](https://arxiv.org/pdf/2611.04244v1), §4.1–4.5 pp.5–7) |

Events: [{"type": "first_submission", "value": "2026-11-03T03:27:35+00:00", "precision": "timestamp", "timezone": "UTC", "authority": "primary", "primary_url": "https://arxiv.org/abs/2611.04244", "version": "v1", "evidence": "Canonical history; Chicago 2026-11-02T21:27:35-06:00.", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: ["Model-based semantic verifier identity is unspecified; only explicit constraint checks classified. Upstream structured outputs distinguished from downstream rendered video."]

### [ScienceVision: Can AI Observe and Reason Like a Scientist?](https://arxiv.org/abs/2611.04087)
core | High | new_relative_to_snapshot
Application: Datasets and Benchmarks, Static / CAD, Static / Scene, Cross-category; operations: Auditing
Cross-domain 3D inspection benchmark separates native computation from fixed images and optional viewer tools; native-artifact configurations outperform fixed images, while MCP effects are small and mixed.
Scope: Actual trajectories show agents selecting and measuring native 3D scene objects and changing viewer state, including CAD/architecture inspection. Scope is auditing rather than content creation.
Limits: Incomplete execution logs, changed tasks and score conventions prevent causal claims about model/harness effects. Eight CAD questions have target/counting ambiguity; scores grade answers, not verified evidence acquisition. No human success baseline.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Visualization | View control, isolation, slices and measurement for structural inspection. ([source](https://arxiv.org/pdf/2611.04087v1), §2–3; Appendix C p.23) |
| input_form | Language, 3D Representation | Question and native 3D artifact supplied. ([source](https://arxiv.org/pdf/2611.04087v1), §3.1 p.5) |
| output | Not Applicable | Final product is requested textual/numeric answer, not graphics content. ([source](https://arxiv.org/pdf/2611.04087v1), §2.1,3.3 pp.3,5) |
| model_type | VLM | Multimodal models inspect viewer images and native data through tools. ([source](https://arxiv.org/pdf/2611.04087v1), §3 p.5; Appendix C) |
| model_training | Not Reported | Model release names, efforts and incomplete snapshot records; no adaptation procedure specified. ([source](https://arxiv.org/pdf/2611.04087v1), Appendix D pp.23–25) |
| planning | Not Reported | Action trajectories described but no explicit controller plan representation. ([source](https://arxiv.org/pdf/2611.04087v1), Appendices D,F) |
| workflow | Sequential | Open, select, measure, interpret and answer in successive recorded calls. ([source](https://arxiv.org/pdf/2611.04087v1), Appendix D.3 p.24; F.6 p.39) |
| update_strategy | Not Reported | Alternative data reading follows failed library load; no artifact patch or explicit plan rewrite reported. ([source](https://arxiv.org/pdf/2611.04087v1), Appendix D.3 p.24) |
| verifier | Self | Agent interprets failed access and changes method. ([source](https://arxiv.org/pdf/2611.04087v1), Appendix D.3 p.24; F.6) |
| feedback_assessment | Diagnosis | Failure to load molecular library leads to alternative atom-record inspection. ([source](https://arxiv.org/pdf/2611.04087v1), Appendix D.3 p.24) |
| feedback_observation | Visual, Structural Scene State, Runtime | Viewer states, measured geometry and failed scene/library loads guide investigation. ([source](https://arxiv.org/pdf/2611.04087v1), Appendix C p.23; D.3 p.24; F.6 pp.39–40) |
| memory_time | Not Reported | Trajectories retained for analysis, but controller state retention protocol is not described; memory/history searches empty. ([source](https://arxiv.org/pdf/2611.04087v1), Appendices C–F, full text) |
| memory_reach | Not Reported | No controller-memory access model reported. ([source](https://arxiv.org/pdf/2611.04087v1), Appendices C–F) |
| action_type | Tool/Function Call, Code/Script | MCP inspection calls and generated source-analysis scripts. ([source](https://arxiv.org/pdf/2611.04087v1), §3.1 p.5; Appendix F.6) |
| graphics_software | Agent-Adapted | Viewer-specific MCP operations exposed to agents. ([source](https://arxiv.org/pdf/2611.04087v1), Appendix C p.23) |
| tools | Execution Utilities, Graphics Operations | File/code execution; camera, isolation, slices and geometric measurements. ([source](https://arxiv.org/pdf/2611.04087v1), Appendix C,D.3,F.6) |
| resources | Not Reported | Native artifact is task input, expert traces are annotation records; task-time reusable resource retrieval not established. ([source](https://arxiv.org/pdf/2611.04087v1), Appendices A–F) |
| representation | Geometry, Pixels, Code | Native 3D objects, viewer renders and generated analysis scripts. ([source](https://arxiv.org/pdf/2611.04087v1), §3; Appendix C,D.3) |

Events: [{"type": "first_submission", "value": "2026-11-02T23:55:01+00:00", "precision": "timestamp", "timezone": "UTC", "authority": "primary", "primary_url": "https://arxiv.org/abs/2611.04087", "version": "v1", "evidence": "Official metadata; Chicago 2026-11-02T17:55:01-06:00.", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: ["Auditing can act on graphics viewer state without producing a graphics output; answer-only output is Not Applicable. Benchmark grading is not loop feedback."]

### [ProtoFusion: Protocol-Guided Prompt Refinement for Generative Infrared and Visible Image Fusion](https://arxiv.org/abs/2611.02877)
core | High | new_relative_to_snapshot
Application: 2D Graphics; operations: Generation, Editing
Frozen-model, slot-constrained prompt optimization improves source-grounded fusion; full PGPR raises UniPercept overall from 38.13 to 47.78 on FMB, with optional SBC raising it to 49.18.
Scope: Offline VLM controller chooses validated protocol edits that change generated fusion images using source-grounded visual critique and best-so-far selection.
Limits: Proxy-score monotonicity does not guarantee fidelity. Full system retains 19.64% image-level source inconsistencies. Prompt-local changes need not be image-local; base generation takes about 188 seconds, excluding optional correction.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Visualization | Fusion targets natural visible appearance for human inspection and visual interpretation. ([source](https://arxiv.org/pdf/2611.02877v1), §1 p.1; §4.8 p.13) |
| input_form | Image | Offline episode takes infrared and visible training pair. ([source](https://arxiv.org/pdf/2611.02877v1), §3.1 p.4) |
| output | Structured Specification | Optimized protocol fixed and reused during inference. ([source](https://arxiv.org/pdf/2611.02877v1), §4.1 p.6) |
| model_type | VLM | Qwen3-VL-8B-Instruct implements initialization, composition, diagnosis and edit prediction. ([source](https://arxiv.org/pdf/2611.02877v1), §4.1 p.7) |
| model_training | Off-the-Shelf | All model parameters remain frozen; only protocol slots updated. ([source](https://arxiv.org/pdf/2611.02877v1), §4.1 pp.6–7) |
| planning | PO-2 | Fixed perception/decision/style/assembly template; VLM writes final prompt as operational plan with steps and constraints. ([source](https://arxiv.org/pdf/2611.02877v1), Appendix A.3 p.19) |
| workflow | Sequential | Compose, generate, diagnose, edit and validate repeat in one cycle. ([source](https://arxiv.org/pdf/2611.02877v1), Eq.1 p.4) |
| update_strategy | Local Patch, Candidate Selection | Only specified slot changes; best non-fatal candidate retained. ([source](https://arxiv.org/pdf/2611.02877v1), §3.1 p.5) |
| verifier | Critic, Programmatic | Diagnostic role judges image; deterministic validator rejects malformed/repeated/ineffective edits. ([source](https://arxiv.org/pdf/2611.02877v1), §3.1 p.5; A.2 p.18) |
| feedback_assessment | Binary, Score, Diagnosis | Text critique, nine binary checks and weighted scalar score control candidate inheritance. ([source](https://arxiv.org/pdf/2611.02877v1), §3.1 p.5; A.2 p.18) |
| feedback_observation | Visual | Source pair and generated fusion image used for diagnosis. ([source](https://arxiv.org/pdf/2611.02877v1), Eq.4–5 p.5) |
| memory_time | Short-Term Memory | Incumbent protocol, image and score inherited across six rounds. ([source](https://arxiv.org/pdf/2611.02877v1), §3.1 p.5) |
| memory_reach | Global Memory | Same current protocol and candidate shared by composition, diagnosis and editor roles. ([source](https://arxiv.org/pdf/2611.02877v1), Eq.1,4,5 pp.4–5) |
| action_type | Structured Specification | Three constrained protocol-slot edit actions. ([source](https://arxiv.org/pdf/2611.02877v1), Eq.5 p.5) |
| graphics_software | Agent-Adapted | Custom protocol composer and validator wrap black-box paired-image generator. ([source](https://arxiv.org/pdf/2611.02877v1), §3.1 pp.4–5) |
| tools | Perception models, Static Validator | Qwen-Image-Edit generator and deterministic edit validator invoked in loop. ([source](https://arxiv.org/pdf/2611.02877v1), §3.1 p.5; §4.1 p.7) |
| resources | Documentation & Rules | Reusable initial protocol, fusion principles and validation rules. ([source](https://arxiv.org/pdf/2611.02877v1), A.2–A.3 pp.18–19) |
| representation | Pixels | Fusion artifacts are raster images; protocol is semantic instruction rather than geometric program. ([source](https://arxiv.org/pdf/2611.02877v1), §3.1 p.5) |

Events: [{"type": "first_submission", "value": "2026-11-02T10:13:54+00:00", "precision": "timestamp", "timezone": "UTC", "authority": "primary", "primary_url": "https://arxiv.org/abs/2611.02877", "version": "v1", "evidence": "Canonical v1; local 2026-11-02T04:13:54-06:00.", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: ["Offline protocol learning is not model fine-tuning. Separate reusable learned specification from controller memory and fixed inference from optimization loop."]

### [Balancing Representations by Identifying and Generating Under-represented Data](https://arxiv.org/abs/2611.02952)
scope_dependent | Medium | new_relative_to_snapshot
Application: 2D Graphics; operations: Generation
Label-free generation allocation improves transfer across five source regimes; fixed-encoder analysis finds roughly twice the neighborhood shrinkage at selected anchors versus matched controls.
Scope: Adaptive acquisition changes which image variants are generated, a potentially useful agentic data-generation mechanism. Full text establishes a fixed statistical SSL loop, not a separately demonstrated graphics agent; retain this boundary rather than promote generic feedback to agency.
Limits: Main comparisons have about 1.5 times baseline gradient updates; controlled paired tests partly address this. Fidelity is not measured, synthetic anchors accumulate without filtering, and web-scale budgets are untested.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Not Applicable | Generate augmentation variants for representation training, not modeling, animation, simulation or visualization. ([source](https://arxiv.org/pdf/2611.02952v1), §1,4 pp.2,4–5) |
| input_form | Image | Unlabeled source image corpus. ([source](https://arxiv.org/pdf/2611.02952v1), §4.1 p.4) |
| output | Rendered Media | Generated raster variants added to source set. ([source](https://arxiv.org/pdf/2611.02952v1), §4.3 p.5) |
| model_type | Not Applicable | ResNet/ViT SSL embeddings and fixed acquisition rule; no LLM/VLM controller. ([source](https://arxiv.org/pdf/2611.02952v1), §4.1,5 pp.4–5) |
| model_training | Unclear | SSL encoder is continuously trained; generator frozen. ([source](https://arxiv.org/pdf/2611.02952v1), §4.1 p.4; Appendix D pp.16–17) |
| planning | Not Applicable | Fixed acquisition loop without plan object; planning search empty. ([source](https://arxiv.org/pdf/2611.02952v1), Algorithm 1 p.21) |
| workflow | Sequential | Train, embed, score, select, generate and augment sequentially. ([source](https://arxiv.org/pdf/2611.02952v1), Algorithm 1 p.21) |
| update_strategy | Candidate Selection | Recomputed scores choose next sparse-anchor subset. ([source](https://arxiv.org/pdf/2611.02952v1), §4.2 p.5) |
| verifier | Programmatic | kNN distances determine low-support regions. ([source](https://arxiv.org/pdf/2611.02952v1), §4.1–4.2 p.5) |
| feedback_assessment | Score | Mean squared neighbor distance sets acquisition score. ([source](https://arxiv.org/pdf/2611.02952v1), Eq.4 p.5) |
| feedback_observation | Not Applicable | Selector observes embedding-space distances, not rendered inspections, scene geometry or runtime. ([source](https://arxiv.org/pdf/2611.02952v1), Eq.4 p.5) |
| memory_time | Short-Term Memory | Encoder warm-started and all earlier images retained over cycles. ([source](https://arxiv.org/pdf/2611.02952v1), §4.1; Appendix D p.16) |
| memory_reach | Local Memory | Single loop retains source dataset and encoder state. ([source](https://arxiv.org/pdf/2611.02952v1), Algorithm 1 p.21) |
| action_type | Tool/Function Call | Calls frozen image-to-image generator on chosen anchor with empty prompt. ([source](https://arxiv.org/pdf/2611.02952v1), §4.3 p.5) |
| graphics_software | General-Purpose | Standard SD3 Medium image-to-image parameters. ([source](https://arxiv.org/pdf/2611.02952v1), Appendix D p.17) |
| tools | Perception models | Frozen image-to-image diffusion generator. ([source](https://arxiv.org/pdf/2611.02952v1), §4.3 p.5) |
| resources | Assets | Accumulating image corpus provides reusable generation anchors. ([source](https://arxiv.org/pdf/2611.02952v1), §4.1–4.3 pp.4–5) |
| representation | Pixels, Learned State | Image variants and normalized learned embeddings. ([source](https://arxiv.org/pdf/2611.02952v1), §4 pp.4–5) |

Events: [{"type": "first_submission", "value": "2026-11-02T11:17:31+00:00", "precision": "timestamp", "timezone": "UTC", "authority": "primary", "primary_url": "https://arxiv.org/abs/2611.02952", "version": "v1", "evidence": "Official metadata; local 2026-11-02T05:17:31-06:00.", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: ["Statistical adaptive acquisition is a defensible borderline, not automatically an agent. Codebook lacks self-supervised controller training and learned-feature feedback labels."]

### [FlowTranslator: Training-Free In-Image Machine Translation with Flow-Based Editing](https://arxiv.org/abs/2611.04303)
scope_dependent | High | new_relative_to_snapshot
Application: 2D Graphics; operations: Editing
Region coupling release and displacement expansion improve PRIM mean BLEU from 16.88 to 20.57 and ScenePair text exact match from 33.44% to 40.08%.
Scope: Image-conditioned LLM specifies semantic text replacements, but the principal contribution is fixed diffusion trajectory control. No autonomous tool choice, model-level feedback or agent-facing deployment is established; the localized editor could materially support graphics agents.
Limits: Cyrillic rendering remains poor; OCR errors depress measured quality. ScenePair fixes translations and boxes, so it tests rendering rather than full upstream translation. TTV SSIM is lower than trained systems.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Visualization | Localizes signage and product imagery while preserving typography and context. ([source](https://arxiv.org/pdf/2611.04303v1), §1 p.1) |
| input_form | Image, Language | Prompt contains image, numbered OCR strings and requested target language. ([source](https://arxiv.org/pdf/2611.04303v1), §4.1 p.7) |
| output | Rendered Media | Final latent decoded into translated image. ([source](https://arxiv.org/pdf/2611.04303v1), Fig.2 p.4) |
| model_type | VLM | Commercial LLM receives image and numbered text. ([source](https://arxiv.org/pdf/2611.04303v1), §4.1 p.7) |
| model_training | Off-the-Shelf | Every module frozen, no IIMT parameter training or fine-tuning. ([source](https://arxiv.org/pdf/2611.04303v1), p.3; §3 p.4) |
| planning | Not Applicable | Single prescribed translation/caption call, no task-plan representation. ([source](https://arxiv.org/pdf/2611.04303v1), §3.1; §4.1 pp.5,7) |
| workflow | Sequential | OCR then translation then flow rendering. ([source](https://arxiv.org/pdf/2611.04303v1), Figs.1–2 pp.2,4) |
| update_strategy | Not Applicable | Fixed ODE controls, no feedback-driven semantic update. ([source](https://arxiv.org/pdf/2611.04303v1), §3 pp.5–6) |
| verifier | Not Applicable | OCR read-back and trajectory probes used only in evaluation. ([source](https://arxiv.org/pdf/2611.04303v1), §4.1 pp.6–7; Appendix A) |
| feedback_assessment | Not Applicable | Positive feedback means latent displacement arithmetic, not judgment. ([source](https://arxiv.org/pdf/2611.04303v1), §3.3 p.6; §4.1) |
| feedback_observation | Not Applicable | Single LLM call does not observe edited result. ([source](https://arxiv.org/pdf/2611.04303v1), §3.3 p.6; §4.1 p.7) |
| memory_time | Working Memory | One call per image with image and OCR lines. ([source](https://arxiv.org/pdf/2611.04303v1), §4.1 p.7) |
| memory_reach | Local Memory | Translator prompt context belongs to one component. ([source](https://arxiv.org/pdf/2611.04303v1), §4.1 p.7) |
| action_type | Structured Specification | Strict JSON translation pairs and source/target captions. ([source](https://arxiv.org/pdf/2611.04303v1), §4.1 p.7) |
| graphics_software | Agent-Adapted | Custom caption-to-mask flow-editing pipeline wraps frozen T2I model. ([source](https://arxiv.org/pdf/2611.04303v1), §3.1 p.5) |
| tools | Perception models | PP-OCRv5 and Z-Image-Turbo invoked in cascade. ([source](https://arxiv.org/pdf/2611.04303v1), §4.1 p.7) |
| resources | Documentation & Rules | Reusable prompt requires preserved line order and unchanged non-text scene description. ([source](https://arxiv.org/pdf/2611.04303v1), §4.1 p.7) |
| representation | Pixels, Learned State | Raster input/output and VAE edit latent. ([source](https://arxiv.org/pdf/2611.04303v1), Fig.2; §3.1 pp.4–5) |

Events: [{"type": "first_submission", "value": "2026-11-03T04:33:47+00:00", "precision": "timestamp", "timezone": "UTC", "authority": "primary", "primary_url": "https://arxiv.org/abs/2611.04303", "version": "v1", "evidence": "Canonical history; Chicago 2026-11-02T22:33:47-06:00.", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: ["Numerical diffusion feedback is not an agent verification loop. Single-call structured translation is retained as borderline rather than automatically core."]

## same_day_updates (0)

## late_discovery (0)

## date_unresolved (0)

## unresolved (6)

### [EvoDesign: Agentic Editable Diagram Creation via Design Expertise Evolution](https://arxiv.org/abs/2604.09568)
unresolved | Low | known_discussed_paper
Application: Cross-category; operations: Unclear
Full-text assessment deferred; no final inclusion decision.
Scope: Canonical v1 Feb 20, v2 Oct 5, v3 Nov 5: no target-day or seven-day event. Relevant known lead deferred, not a scope exclusion.
Limits: No PDF reading receipt in this run; taxonomy intentionally unclassified.

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

Events: [{"type": "first_submission", "value": "2026-02-20T11:11:02+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2604.09568", "authority": "primary", "version": "v1", "evidence": "Official metadata; local 2026-02-20T05:11:02-06:00. Canonical history inspected where stated.", "prior_event_status": "not_seen_in_supplied_history"}, {"type": "revision", "value": "2026-11-05T18:18:33+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2604.09568", "authority": "primary", "version": "v3", "evidence": "Official metadata; local 2026-11-05T12:18:33-06:00. Canonical history inspected where stated.", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: []

### [WorldAct: Activating Monolithic 3D Worlds into Interactive-Ready Object-Centric Scenes](https://arxiv.org/abs/2605.15843)
unresolved | Low | known_discussed_paper
Application: Cross-category; operations: Unclear
Full-text assessment deferred; no final inclusion decision.
Scope: Canonical v1 May 15 and v2 Nov 5: no target-day or seven-day event. Relevant known lead deferred, not a scope exclusion.
Limits: No PDF reading receipt in this run; taxonomy intentionally unclassified.

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

Events: [{"type": "first_submission", "value": "2026-05-15T10:56:23+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2605.15843", "authority": "primary", "version": "v1", "evidence": "Official metadata; local 2026-05-15T05:56:23-05:00. Canonical history inspected where stated.", "prior_event_status": "not_seen_in_supplied_history"}, {"type": "revision", "value": "2026-11-05T07:15:15+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2605.15843", "authority": "primary", "version": "v2", "evidence": "Official metadata; local 2026-11-05T01:15:15-06:00. Canonical history inspected where stated.", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: []

### [NeoWorld-Pro: Programming Interactive Scenes from Monocular Images for Embodied Simulation](https://arxiv.org/abs/2608.24212)
unresolved | Low | new_relative_to_snapshot
Application: Cross-category; operations: Unclear
Full-text assessment deferred; no final inclusion decision.
Scope: Canonical v1 Aug 25, v2 Oct 20, v3 Nov 5: no target-day or seven-day event. Relevant known lead deferred, not a scope exclusion.
Limits: No PDF reading receipt in this run; taxonomy intentionally unclassified.

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

Events: [{"type": "first_submission", "value": "2026-08-25T08:19:39+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2608.24212", "authority": "primary", "version": "v1", "evidence": "Official metadata; local 2026-08-25T03:19:39-05:00. Canonical history inspected where stated.", "prior_event_status": "not_seen_in_supplied_history"}, {"type": "revision", "value": "2026-11-05T06:32:22+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2608.24212", "authority": "primary", "version": "v3", "evidence": "Official metadata; local 2026-11-05T00:32:22-06:00. Canonical history inspected where stated.", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: []

### [PhotoGuider: Composition-Aware Cropping and 360° View Framing with Explainable Photographic Assessments](https://arxiv.org/abs/2611.02897)
unresolved | Low | new_relative_to_snapshot
Application: Cross-category; operations: Unclear
Full-text assessment deferred; no final inclusion decision.
Scope: Target-day v1 verified; latest cutoff-available v2 Nov 4 downloaded (sha256 79b8e8ac2fbfb0f5bef959a688c66c38910366d2ebb60cd395bb340765a6fe9d) but NOT read before harness finalization instruction. Learned framing controller relation remains provisional.
Limits: No PDF reading receipt in this run; taxonomy intentionally unclassified.

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

Events: [{"type": "first_submission", "value": "2026-11-02T10:31:22+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2611.02897", "authority": "primary", "version": "v1", "evidence": "Official metadata; local 2026-11-02T04:31:22-06:00. Canonical history inspected where stated.", "prior_event_status": "not_seen_in_supplied_history"}, {"type": "revision", "value": "2026-11-04T14:00:35+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2611.02897", "authority": "primary", "version": "v2", "evidence": "Official metadata; local 2026-11-04T08:00:35-06:00. Canonical history inspected where stated.", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: []

### [SceneAgent: An Agentic Pipeline from 3D and 4D Captures to Simulation Environments](https://arxiv.org/abs/2610.34745)
unresolved | Low | new_relative_to_snapshot
Application: Cross-category; operations: Unclear
Full-text assessment deferred; no final inclusion decision.
Scope: Official project abstract supports simulator-based repair; official v1 is Oct 26 02:45 UTC = Oct 25 Chicago, outside seven-day lookback. Nov 1 project news is acceptance, not verified publication. Unread.
Limits: No PDF reading receipt in this run; taxonomy intentionally unclassified.

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

Events: [{"type": "first_submission", "value": "2026-10-26T02:45:35+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2610.34745", "authority": "primary", "version": "v1", "evidence": "Official metadata; local 2026-10-25T21:45:35-05:00. Canonical history inspected where stated.", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: []

### [Agentic AI for Scientific Visualization: Tool-Calling Pipelines for Automated Chart and Diagram Generation in Research Writing](https://www.scitepress.org/PublishedPapers/2026/152298/)
unresolved | Low | new_relative_to_snapshot
Application: 2D Graphics; operations: Unclear
Lead only; full reading pending.
Scope: Explicit graphics tool-calling pipeline, but exact publication date and full text not established within bounded run.
Limits: No exact primary date or full PDF receipt.

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
| 2D Graphics | [CounterSketch: Physics-Grounded Counterfactual Reasoning for Sketch-to-Video Generation](https://arxiv.org/abs/2611.04244) [same_day_new]; [ProtoFusion: Protocol-Guided Prompt Refinement for Generative Infrared and Visible Image Fusion](https://arxiv.org/abs/2611.02877) [same_day_new]; [Balancing Representations by Identifying and Generating Under-represented Data](https://arxiv.org/abs/2611.02952) [same_day_new]; [FlowTranslator: Training-Free In-Image Machine Translation with Flow-Based Editing](https://arxiv.org/abs/2611.04303) [same_day_new]; [Agentic AI for Scientific Visualization: Tool-Calling Pipelines for Automated Chart and Diagram Generation in Research Writing](https://www.scitepress.org/PublishedPapers/2026/152298/) [unresolved] |
| Static / Object | None verified in this run |
| Static / CAD | [Parametric CAD Bench v3: Evaluating Agentic Parametric CAD Authoring from Text and Engineering Drawings](https://arxiv.org/abs/2611.02659) [same_day_new]; [ScienceVision: Can AI Observe and Reason Like a Scientist?](https://arxiv.org/abs/2611.04087) [same_day_new] |
| Static / Scene | [Visual-to-Executable Procedural Reconstruction of Buildings](https://arxiv.org/abs/2611.03143) [same_day_new]; [ScienceVision: Can AI Observe and Reason Like a Scientist?](https://arxiv.org/abs/2611.04087) [same_day_new] |
| Dynamic / Articulated assets | None verified in this run |
| Dynamic / Animation and temporal scene | [CounterSketch: Physics-Grounded Counterfactual Reasoning for Sketch-to-Video Generation](https://arxiv.org/abs/2611.04244) [same_day_new] |
| Dynamic / Physical simulation and effects | None verified in this run |
| Datasets and Benchmarks | [Parametric CAD Bench v3: Evaluating Agentic Parametric CAD Authoring from Text and Engineering Drawings](https://arxiv.org/abs/2611.02659) [same_day_new]; [ScienceVision: Can AI Observe and Reason Like a Scientist?](https://arxiv.org/abs/2611.04087) [same_day_new] |
| Cross-category | [ScienceVision: Can AI Observe and Reason Like a Scientist?](https://arxiv.org/abs/2611.04087) [same_day_new]; [EvoDesign: Agentic Editable Diagram Creation via Design Expertise Evolution](https://arxiv.org/abs/2604.09568) [unresolved]; [WorldAct: Activating Monolithic 3D Worlds into Interactive-Ready Object-Centric Scenes](https://arxiv.org/abs/2605.15843) [unresolved]; [NeoWorld-Pro: Programming Interactive Scenes from Monocular Images for Embodied Simulation](https://arxiv.org/abs/2608.24212) [unresolved]; [PhotoGuider: Composition-Aware Cropping and 360° View Framing with Explainable Photographic Assessments](https://arxiv.org/abs/2611.02897) [unresolved]; [SceneAgent: An Agentic Pipeline from 3D and 4D Captures to Simulation Environments](https://arxiv.org/abs/2610.34745) [unresolved] |

## Source ledger
| Source | Status | Checked pages / queries | Limitations |
|---|---|---|---|
| arxiv | partial | [{"query_or_url": "https://arxiv.org/list/cs.GR/new?skip=0&show=100", "checked_at": "2026-11-07T21:05:06.881758+00:00", "outcome": "Observed listing page fetched; 16 entries. Complete observed pagination=True. Not field completeness."}, {"query_or_url": "https://arxiv.org/list/cs.GR/recent?skip=0&show=100", "checked_at": "2026-11-07T21:05:06.916791+00:00", "outcome": "Observed listing page fetched; 43 entries. Complete observed pagination=True. Not field completeness."}, {"query_or_url": "https://arxiv.org/list/cs.CV/recent?skip=0&show=100", "checked_at": "2026-11-07T21:05:07.108708+00:00", "outcome": "Observed listing page fetched; 100 entries. Complete observed pagination=True. Not field completeness."}, {"query_or_url": "https://arxiv.org/list/cs.CV/recent?skip=0&show=2000", "checked_at": "2026-11-07T21:05:08.404628+00:00", "outcome": "Observed listing page fetched; 943 entries. Complete observed pagination=True. Not field completeness."}, {"query_or_url": "https://arxiv.org/list/cs.CV/new?skip=0&show=100", "checked_at": "2026-11-07T21:05:07.207611+00:00", "outcome": "Observed listing page fetched; 100 entries. Complete observed pagination=True. Not field completeness."}, {"query_or_url": "https://arxiv.org/list/cs.CV/new?skip=0&show=2000", "checked_at": "2026-11-07T21:05:08.878589+00:00", "outcome": "Observed listing page fetched; 258 entries. Complete observed pagination=True. Not field completeness."}, {"query_or_url": "https://export.arxiv.org/api/query?id_list=2412.10338%2C2501.14546%2C2502.10259%2C2502.21012%2C2503.13344%2C2507.17892%2C2507.19684%2C2508.19204%2C2509.25549%2C2509.26455%2C2510.01347%2C2510.04066%2C2510.24464%2C2511.00908%2C2511.03212%2C2511.09818%2C2511.18811%2C2512.01707%2C2512.14056%2C2512.17581%2C2601.11063%2C2601.15838%2C2602.00192%2C2602.13780%2C2602.17659%2C2602.18742%2C2603.04314%2C2603.10648%2C2603.10828%2C2603.15834%2C2603.16482%2C2603.21071%2C2603.23481%2C2604.02851%2C2604.03420%2C2604.09568%2C2604.10675%2C2604.19741%2C2604.24317%2C2605.03749%2C2605.06207%2C2605.13675%2C2605.15391%2C2605.15843%2C2605.16797%2C2605.16922%2C2605.19256%2C2605.24011%2C2605.26032%2C2605.30983%2C2605.31572%2C2606.02937%2C2606.06113%2C2606.07642%2C2606.08043%2C2606.15920%2C2606.15992%2C2606.17985%2C2606.26718%2C2606.28780%2C2607.03012%2C2607.26921%2C2607.29586%2C2608.00137%2C2608.01896%2C2608.06886%2C2608.08600%2C2608.14430%2C2608.19540%2C2608.24212%2C2608.28602%2C2608.28699%2C2609.00968%2C2609.08818%2C2609.18279%2C2609.25864%2C2609.27110%2C2609.33928%2C2609.37314%2C2610.00365%2C2610.01279%2C2610.01291%2C2610.07729%2C2610.07925%2C2610.08825%2C2610.09173%2C2610.09502%2C2610.14517%2C2610.16320%2C2610.16621%2C2610.18857%2C2610.20973%2C2610.21569%2C2610.21795%2C2610.25284%2C2610.25395%2C2610.27041%2C2610.31166%2C2610.31835%2C2610.33857&max_results=100", "checked_at": "2026-11-07T21:08:47.556451+00:00", "outcome": "Official Atom identities and timestamps resolved; raw provenance retained."}, {"query_or_url": "https://export.arxiv.org/api/query?id_list=2610.35375%2C2610.35766%2C2610.37019%2C2610.40662%2C2610.40702%2C2610.40752%2C2610.40754%2C2610.40801%2C2610.40832%2C2610.40834%2C2610.40887%2C2610.40900%2C2610.40905%2C2610.40913%2C2610.40914%2C2610.40935%2C2610.40947%2C2610.40949%2C2610.40954%2C2610.40971%2C2610.40972%2C2610.40973%2C2610.40976%2C2610.41011%2C2610.41030%2C2610.41037%2C2610.41063%2C2610.41069%2C2610.41080%2C2610.41111%2C2610.41118%2C2610.41127%2C2610.41130%2C2610.41159%2C2610.41185%2C2610.41190%2C2610.41199%2C2610.41204%2C2610.41210%2C2610.41213%2C2610.41216%2C2610.41231%2C2610.41254%2C2610.41257%2C2610.41258%2C2610.41260%2C2610.41304%2C2610.41310%2C2610.41314%2C2610.41328%2C2610.41337%2C2610.41338%2C2610.41348%2C2610.41352%2C2610.41360%2C2610.41362%2C2610.41373%2C2610.41389%2C2610.41402%2C2610.41408%2C2610.41426%2C2610.41446%2C2610.41485%2C2610.41494%2C2610.41496%2C2610.41501%2C2610.41512%2C2610.41520%2C2610.41556%2C2610.41598%2C2610.41602%2C2610.41618%2C2610.41629%2C2610.41642%2C2610.41651%2C2610.41652%2C2610.41671%2C2610.41673%2C2610.41677%2C2610.41695%2C2610.41705%2C2610.41728%2C2610.41763%2C2610.41772%2C2610.41789%2C2610.41790%2C2610.41814%2C2610.41833%2C2610.41834%2C2610.41835%2C2610.41841%2C2610.41877%2C2610.41924%2C2610.41983%2C2610.41987%2C2610.41992%2C2610.42002%2C2610.42031%2C2610.42036%2C2610.42053&max_results=100", "checked_at": "2026-11-07T21:08:51.154339+00:00", "outcome": "Official Atom identities and timestamps resolved; raw provenance retained."}, {"query_or_url": "https://export.arxiv.org/api/query?id_list=2610.42082%2C2610.42092%2C2610.42111%2C2610.42135%2C2610.42136%2C2610.42141%2C2610.42145%2C2610.42149%2C2610.42152%2C2611.00003%2C2611.00004%2C2611.00017%2C2611.00020%2C2611.00022%2C2611.00023%2C2611.00024%2C2611.00025%2C2611.00026%2C2611.00027%2C2611.00028%2C2611.00029%2C2611.00031%2C2611.00032%2C2611.00033%2C2611.00034%2C2611.00035%2C2611.00036%2C2611.00037%2C2611.00038%2C2611.00039%2C2611.00040%2C2611.00041%2C2611.00042%2C2611.00043%2C2611.00044%2C2611.00045%2C2611.00046%2C2611.00047%2C2611.00048%2C2611.00049%2C2611.00050%2C2611.00053%2C2611.00054%2C2611.00055%2C2611.00056%2C2611.00058%2C2611.00059%2C2611.00061%2C2611.00062%2C2611.00063%2C2611.00064%2C2611.00065%2C2611.00066%2C2611.00067%2C2611.00069%2C2611.00071%2C2611.00072%2C2611.00073%2C2611.00074%2C2611.00076%2C2611.00077%2C2611.00078%2C2611.00079%2C2611.00080%2C2611.00081%2C2611.00084%2C2611.00091%2C2611.00092%2C2611.00097%2C2611.00099%2C2611.00102%2C2611.00105%2C2611.00107%2C2611.00110%2C2611.00111%2C2611.00113%2C2611.00114%2C2611.00120%2C2611.00122%2C2611.00140%2C2611.00150%2C2611.00151%2C2611.00157%2C2611.00175%2C2611.00177%2C2611.00179%2C2611.00180%2C2611.00181%2C2611.00184%2C2611.00191%2C2611.00192%2C2611.00227%2C2611.00238%2C2611.00245%2C2611.00247%2C2611.00253%2C2611.00288%2C2611.00293%2C2611.00328%2C2611.00351&max_results=100", "checked_at": "2026-11-07T21:08:54.521050+00:00", "outcome": "Official Atom identities and timestamps resolved; raw provenance retained."}, {"query_or_url": "{\"max_batches\": 3, \"operation\": \"resolve\"}", "checked_at": "2026-11-07T21:08:54.554244+00:00", "outcome": "Batch catalog metadata resolution: 300 resolved; 762 pending."}, {"query_or_url": "https://export.arxiv.org/api/query?id_list=2611.00367%2C2611.00371%2C2611.00375%2C2611.00383%2C2611.00396%2C2611.00406%2C2611.00423%2C2611.00427%2C2611.00430%2C2611.00458%2C2611.00478%2C2611.00482%2C2611.00507%2C2611.00523%2C2611.00527%2C2611.00551%2C2611.00556%2C2611.00566%2C2611.00608%2C2611.00634%2C2611.00653%2C2611.00658%2C2611.00671%2C2611.00676%2C2611.00681%2C2611.00683%2C2611.00684%2C2611.00699%2C2611.00704%2C2611.00715%2C2611.00721%2C2611.00722%2C2611.00756%2C2611.00758%2C2611.00763%2C2611.00768%2C2611.00769%2C2611.00780%2C2611.00784%2C2611.00785%2C2611.00791%2C2611.00794%2C2611.00804%2C2611.00810%2C2611.00819%2C2611.00823%2C2611.00828%2C2611.00833%2C2611.00843%2C2611.00848%2C2611.00859%2C2611.00892%2C2611.00899%2C2611.00908%2C2611.00926%2C2611.00937%2C2611.00953%2C2611.00963%2C2611.00974%2C2611.01018%2C2611.01048%2C2611.01050%2C2611.01074%2C2611.01078%2C2611.01084%2C2611.01095%2C2611.01120%2C2611.01125%2C2611.01141%2C2611.01162%2C2611.01165%2C2611.01215%2C2611.01222%2C2611.01229%2C2611.01230%2C2611.01252%2C2611.01263%2C2611.01283%2C2611.01295%2C2611.01372%2C2611.01391%2C2611.01396%2C2611.01400%2C2611.01414%2C2611.01438%2C2611.01457%2C2611.01460%2C2611.01463%2C2611.01466%2C2611.01467%2C2611.01511%2C2611.01513%2C2611.01517%2C2611.01529%2C2611.01534%2C2611.01536%2C2611.01537%2C2611.01541%2C2611.01543%2C2611.01548&max_results=100", "checked_at": "2026-11-07T21:09:03.954861+00:00", "outcome": "Official Atom identities and timestamps resolved; raw provenance retained."}, {"query_or_url": "https://export.arxiv.org/api/query?id_list=2611.01550%2C2611.01551%2C2611.01558%2C2611.01573%2C2611.01578%2C2611.01600%2C2611.01601%2C2611.01605%2C2611.01607%2C2611.01615%2C2611.01617%2C2611.01626%2C2611.01627%2C2611.01631%2C2611.01635%2C2611.01645%2C2611.01648%2C2611.01663%2C2611.01675%2C2611.01676%2C2611.01682%2C2611.01684%2C2611.01688%2C2611.01696%2C2611.01705%2C2611.01730%2C2611.01736%2C2611.01759%2C2611.01765%2C2611.01783%2C2611.01790%2C2611.01791%2C2611.01815%2C2611.01822%2C2611.01823%2C2611.01846%2C2611.01850%2C2611.01858%2C2611.01860%2C2611.01888%2C2611.01900%2C2611.01902%2C2611.01907%2C2611.01913%2C2611.01921%2C2611.01934%2C2611.01937%2C2611.01939%2C2611.01958%2C2611.01960%2C2611.01962%2C2611.01970%2C2611.01974%2C2611.01978%2C2611.01982%2C2611.01990%2C2611.01992%2C2611.02008%2C2611.02026%2C2611.02034%2C2611.02037%2C2611.02044%2C2611.02051%2C2611.02053%2C2611.02056%2C2611.02076%2C2611.02096%2C2611.02101%2C2611.02114%2C2611.02119%2C2611.02147%2C2611.02197%2C2611.02203%2C2611.02204%2C2611.02211%2C2611.02245%2C2611.02284%2C2611.02305%2C2611.02306%2C2611.02324%2C2611.02327%2C2611.02341%2C2611.02356%2C2611.02363%2C2611.02364%2C2611.02366%2C2611.02393%2C2611.02405%2C2611.02419%2C2611.02433%2C2611.02437%2C2611.02474%2C2611.02488%2C2611.02499%2C2611.02505%2C2611.02506%2C2611.02512%2C2611.02519%2C2611.02526%2C2611.02540&max_results=100", "checked_at": "2026-11-07T21:09:07.456002+00:00", "outcome": "Official Atom identities and timestamps resolved; raw provenance retained."}, {"query_or_url": "https://export.arxiv.org/api/query?id_list=2611.02551%2C2611.02568%2C2611.02578%2C2611.02581%2C2611.02593%2C2611.02599%2C2611.02603%2C2611.02625%2C2611.02631%2C2611.02648%2C2611.02649%2C2611.02651%2C2611.02654%2C2611.02658%2C2611.02659%2C2611.02661%2C2611.02671%2C2611.02685%2C2611.02686%2C2611.02690%2C2611.02695%2C2611.02726%2C2611.02737%2C2611.02744%2C2611.02751%2C2611.02756%2C2611.02759%2C2611.02767%2C2611.02769%2C2611.02775%2C2611.02776%2C2611.02780%2C2611.02782%2C2611.02786%2C2611.02803%2C2611.02822%2C2611.02844%2C2611.02853%2C2611.02854%2C2611.02857%2C2611.02862%2C2611.02877%2C2611.02897%2C2611.02902%2C2611.02921%2C2611.02929%2C2611.02931%2C2611.02941%2C2611.02952%2C2611.02964%2C2611.02995%2C2611.03007%2C2611.03017%2C2611.03023%2C2611.03027%2C2611.03033%2C2611.03042%2C2611.03043%2C2611.03062%2C2611.03067%2C2611.03069%2C2611.03078%2C2611.03080%2C2611.03087%2C2611.03097%2C2611.03098%2C2611.03109%2C2611.03114%2C2611.03120%2C2611.03125%2C2611.03132%2C2611.03136%2C2611.03140%2C2611.03143%2C2611.03189%2C2611.03228%2C2611.03229%2C2611.03232%2C2611.03245%2C2611.03247%2C2611.03283%2C2611.03285%2C2611.03339%2C2611.03360%2C2611.03370%2C2611.03371%2C2611.03377%2C2611.03382%2C2611.03390%2C2611.03393%2C2611.03394%2C2611.03399%2C2611.03404%2C2611.03421%2C2611.03430%2C2611.03438%2C2611.03449%2C2611.03455%2C2611.03465%2C2611.03528&max_results=100", "checked_at": "2026-11-07T21:09:10.821562+00:00", "outcome": "Official Atom identities and timestamps resolved; raw provenance retained."}, {"query_or_url": "{\"max_batches\": 3, \"operation\": \"resolve\"}", "checked_at": "2026-11-07T21:09:10.872394+00:00", "outcome": "Batch catalog metadata resolution: 600 resolved; 462 pending."}, {"query_or_url": "https://export.arxiv.org/api/query?id_list=2610.04262%2C2610.06852%2C2610.09127%2C2610.17651%2C2610.28679%2C2610.30753%2C2610.33060%2C2610.38468%2C2610.40333%2C2610.40339%2C2610.41260%2C2610.42141%2C2611.00097%2C2611.03939&max_results=14", "checked_at": "2026-11-07T21:09:14.012545+00:00", "outcome": "Official Atom identities and timestamps resolved; raw provenance retained."}, {"query_or_url": "https://export.arxiv.org/api/query?id_list=2611.03533%2C2611.03557%2C2611.03588%2C2611.03597%2C2611.03602%2C2611.03626%2C2611.03646%2C2611.03647%2C2611.03648%2C2611.03685%2C2611.03717%2C2611.03741%2C2611.03765%2C2611.03775%2C2611.03932%2C2611.03936%2C2611.03937%2C2611.03940%2C2611.03942%2C2611.03952%2C2611.03958%2C2611.04002%2C2611.04012%2C2611.04025%2C2611.04028%2C2611.04034%2C2611.04053%2C2611.04084%2C2611.04087%2C2611.04092%2C2611.04102%2C2611.04111%2C2611.04112%2C2611.04123%2C2611.04139%2C2611.04155%2C2611.04164%2C2611.04166%2C2611.04173%2C2611.04193%2C2611.04195%2C2611.04200%2C2611.04216%2C2611.04219%2C2611.04221%2C2611.04233%2C2611.04235%2C2611.04242%2C2611.04244%2C2611.04254%2C2611.04257%2C2611.04262%2C2611.04268%2C2611.04286%2C2611.04300%2C2611.04303%2C2611.04305%2C2611.04317%2C2611.04337%2C2611.04352%2C2611.04358%2C2611.04368%2C2611.04374%2C2611.04379%2C2611.04386%2C2611.04389%2C2611.04397%2C2611.04405%2C2611.04409%2C2611.04414%2C2611.04416%2C2611.04418%2C2611.04422%2C2611.04423%2C2611.04435%2C2611.04438%2C2611.04442%2C2611.04452%2C2611.04467%2C2611.04470%2C2611.04472%2C2611.04476%2C2611.04489%2C2611.04490%2C2611.04491%2C2611.04492%2C2611.04498%2C2611.04524%2C2611.04529%2C2611.04534%2C2611.04537%2C2611.04548%2C2611.04554%2C2611.04583%2C2611.04591%2C2611.04604%2C2611.04616%2C2611.04624%2C2611.04626%2C2611.04633&max_results=100", "checked_at": "2026-11-07T21:09:19.799533+00:00", "outcome": "Official Atom identities and timestamps resolved; raw provenance retained."}, {"query_or_url": "https://export.arxiv.org/api/query?id_list=2611.04645%2C2611.04654%2C2611.04666%2C2611.04709%2C2611.04710%2C2611.04711%2C2611.04712%2C2611.04728%2C2611.04734%2C2611.04754%2C2611.04755%2C2611.04759%2C2611.04764%2C2611.04780%2C2611.04811%2C2611.04822%2C2611.04873%2C2611.04874%2C2611.04894%2C2611.04903%2C2611.04912%2C2611.04913%2C2611.04916%2C2611.04932%2C2611.04939%2C2611.04940%2C2611.04943%2C2611.04946%2C2611.04948%2C2611.04950%2C2611.04959%2C2611.04960%2C2611.04980%2C2611.05004%2C2611.05008%2C2611.05011%2C2611.05024%2C2611.05035%2C2611.05049%2C2611.05058%2C2611.05062%2C2611.05066%2C2611.05072%2C2611.05083%2C2611.05084%2C2611.05102%2C2611.05106%2C2611.05131%2C2611.05145%2C2611.05158%2C2611.05172%2C2611.05181%2C2611.05192%2C2611.05193%2C2611.05197%2C2611.05205%2C2611.05206%2C2611.05223%2C2611.05231%2C2611.05275%2C2611.05279%2C2611.05280%2C2611.05286%2C2611.05291%2C2611.05294%2C2611.05348%2C2611.05359%2C2611.05361%2C2611.05377%2C2611.05380%2C2611.05398%2C2611.05403%2C2611.05404%2C2611.05406%2C2611.05407%2C2611.05408%2C2611.05411%2C2611.05443%2C2611.05449%2C2611.05451%2C2611.05522%2C2611.05539%2C2611.05559%2C2611.05564%2C2611.05565%2C2611.05569%2C2611.05570%2C2611.05578%2C2611.05579%2C2611.05581%2C2611.05593%2C2611.05594%2C2611.05599%2C2611.05618%2C2611.05633%2C2611.05646%2C2611.05648%2C2611.05680%2C2611.05689%2C2611.05693&max_results=100", "checked_at": "2026-11-07T21:09:23.150276+00:00", "outcome": "Official Atom identities and timestamps resolved; raw provenance retained."}, {"query_or_url": "https://export.arxiv.org/api/query?id_list=2611.05697%2C2611.05734%2C2611.05737%2C2611.05738%2C2611.05742%2C2611.05755%2C2611.05766%2C2611.05801%2C2611.05802%2C2611.05811%2C2611.05818%2C2611.05825%2C2611.05843%2C2611.05847%2C2611.05851%2C2611.05859%2C2611.05874%2C2611.05893%2C2611.05909%2C2611.05917%2C2611.05925%2C2611.05927%2C2611.05945%2C2611.05969%2C2611.05974%2C2611.05992%2C2611.05994%2C2611.06000%2C2611.06007%2C2611.06015%2C2611.06020%2C2611.06040%2C2611.06042%2C2611.06046%2C2611.06047%2C2611.06048%2C2611.06061%2C2611.06070%2C2611.06083%2C2611.06085%2C2611.06089%2C2611.06093%2C2611.06096%2C2611.06098%2C2611.06105%2C2611.06113%2C2611.06120%2C2611.06141%2C2611.06143%2C2611.06149%2C2611.06160%2C2611.06168%2C2611.06180%2C2611.06191%2C2611.06195%2C2611.06203%2C2611.06205%2C2611.06221%2C2611.06230%2C2611.06247%2C2611.06255%2C2611.06258%2C2611.06259%2C2611.06270%2C2611.06273%2C2611.06282%2C2611.06302%2C2611.06343%2C2611.06353%2C2611.06355%2C2611.06377%2C2611.06378%2C2611.06412%2C2611.06415%2C2611.06422%2C2611.06430%2C2611.06433%2C2611.06452%2C2611.06453%2C2611.06455%2C2611.06471%2C2611.06484%2C2611.06518%2C2611.06540%2C2611.06544%2C2611.06556%2C2611.06593%2C2611.06594%2C2611.06624%2C2611.06627%2C2611.06631%2C2611.06635%2C2611.06637%2C2611.06652%2C2611.06664%2C2611.06685%2C2611.06701%2C2611.06724%2C2611.06728%2C2611.06738&max_results=100", "checked_at": "2026-11-07T21:09:26.450870+00:00", "outcome": "Official Atom identities and timestamps resolved; raw provenance retained."}, {"query_or_url": "{\"max_batches\": 3, \"operation\": \"resolve\"}", "checked_at": "2026-11-07T21:09:26.529738+00:00", "outcome": "Batch catalog metadata resolution: 900 resolved; 162 pending."}, {"query_or_url": "https://export.arxiv.org/api/query?id_list=2610.34745&max_results=1", "checked_at": "2026-11-07T21:09:29.676788+00:00", "outcome": "Official Atom identities and timestamps resolved; raw provenance retained."}, {"query_or_url": "https://export.arxiv.org/api/query?id_list=2611.06741%2C2611.06748%2C2611.06760%2C2611.06770%2C2611.06781%2C2611.06796%2C2611.06817%2C2611.06838%2C2611.06840%2C2611.06844%2C2611.06849%2C2611.06854%2C2611.06856%2C2611.06864%2C2611.06870%2C2611.06890%2C2611.06899%2C2611.06901%2C2611.06908%2C2611.06918%2C2611.06930%2C2611.06935%2C2611.06954%2C2611.06974%2C2611.06993%2C2611.07009%2C2611.07049%2C2611.07055%2C2611.07061%2C2611.07063%2C2611.07081%2C2611.07132%2C2611.07148%2C2611.07176%2C2611.07188%2C2611.07289%2C2611.07294%2C2611.07301%2C2611.07328%2C2611.07329%2C2611.07354%2C2611.07384%2C2611.07392%2C2611.07397%2C2611.07398%2C2611.07408%2C2611.07411%2C2611.07417%2C2611.07431%2C2611.07437%2C2611.07443%2C2611.07463%2C2611.07481%2C2611.07498%2C2611.07502%2C2611.07512%2C2611.07513%2C2611.07540%2C2611.07543%2C2611.07551%2C2611.07553%2C2611.07555%2C2611.07566%2C2611.07573%2C2611.07575%2C2611.07580%2C2611.07593%2C2611.07604%2C2611.07613%2C2611.07632%2C2611.07644%2C2611.07647%2C2611.07648%2C2611.07658%2C2611.07662%2C2611.07665%2C2611.07673%2C2611.07677%2C2611.07682%2C2611.07683%2C2611.07702%2C2611.07705%2C2611.07709%2C2611.07711%2C2611.07713%2C2611.07718%2C2611.07730%2C2611.07741%2C2611.07765%2C2611.07775%2C2611.07793%2C2611.07810%2C2611.07811%2C2611.07814%2C2611.07828%2C2611.07836%2C2611.07843%2C2611.07850%2C2611.07865%2C2611.07867&max_results=100", "checked_at": "2026-11-07T21:09:34.581526+00:00", "outcome": "Official Atom identities and timestamps resolved; raw provenance retained."}, {"query_or_url": "https://export.arxiv.org/api/query?id_list=2611.07873%2C2611.07883%2C2611.07900%2C2611.07902%2C2611.07909%2C2611.07922%2C2611.07929%2C2611.07935%2C2611.07939%2C2611.07941%2C2611.07950%2C2611.07955%2C2611.07961%2C2611.07979%2C2611.07994%2C2611.08003%2C2611.08005%2C2611.08054%2C2611.08080%2C2611.08081%2C2611.08091%2C2611.08095%2C2611.08099%2C2611.08111%2C2611.08125%2C2611.08128%2C2611.08136%2C2611.08138%2C2611.08140%2C2611.08147%2C2611.08148%2C2611.08154%2C2611.08156%2C2611.08157%2C2611.08185%2C2611.08216%2C2611.08236%2C2611.08240%2C2611.08262%2C2611.08264%2C2611.08271%2C2611.08275%2C2611.08286%2C2611.08288%2C2611.08294%2C2611.08301%2C2611.08330%2C2611.08342%2C2611.08352%2C2611.08359%2C2611.08360%2C2611.08368%2C2611.08372%2C2611.08393%2C2611.08407%2C2611.08413%2C2611.08436%2C2611.08441%2C2611.08449%2C2611.08477%2C2611.08485%2C2611.08486&max_results=62", "checked_at": "2026-11-07T21:09:37.891195+00:00", "outcome": "Official Atom identities and timestamps resolved; raw provenance retained."}, {"query_or_url": "{\"max_batches\": 3, \"operation\": \"resolve\"}", "checked_at": "2026-11-07T21:09:37.972601+00:00", "outcome": "Batch catalog metadata resolution: 1062 resolved; 0 pending."}, {"query_or_url": "https://arxiv.org/abs/2604.09568", "checked_at": "2026-11-07T21:13:28.617270+00:00", "outcome": "Primary page retrieved; dates/abstract or version history inspected. See paper record or deferred lead."}, {"query_or_url": "https://arxiv.org/abs/2605.15843", "checked_at": "2026-11-07T21:13:28.741661+00:00", "outcome": "Primary page retrieved; dates/abstract or version history inspected. See paper record or deferred lead."}, {"query_or_url": "https://arxiv.org/abs/2608.24212", "checked_at": "2026-11-07T21:13:28.835624+00:00", "outcome": "Primary page retrieved; dates/abstract or version history inspected. See paper record or deferred lead."}, {"query_or_url": "https://arxiv.org/abs/2611.02659", "checked_at": "2026-11-07T21:14:30.607880+00:00", "outcome": "Primary page retrieved; dates/abstract or version history inspected. See paper record or deferred lead."}, {"query_or_url": "https://arxiv.org/abs/2611.03143", "checked_at": "2026-11-07T21:15:30.148426+00:00", "outcome": "Primary page retrieved; dates/abstract or version history inspected. See paper record or deferred lead."}, {"query_or_url": "https://arxiv.org/abs/2611.04244", "checked_at": "2026-11-07T21:16:33.093415+00:00", "outcome": "Primary page retrieved; dates/abstract or version history inspected. See paper record or deferred lead."}, {"query_or_url": "https://arxiv.org/abs/2611.04087", "checked_at": "2026-11-07T21:17:35.241116+00:00", "outcome": "Primary page retrieved; dates/abstract or version history inspected. See paper record or deferred lead."}, {"query_or_url": "https://arxiv.org/abs/2611.02877", "checked_at": "2026-11-07T21:18:43.015999+00:00", "outcome": "Primary page retrieved; dates/abstract or version history inspected. See paper record or deferred lead."}, {"query_or_url": "https://arxiv.org/abs/2611.02952", "checked_at": "2026-11-07T21:19:44.163798+00:00", "outcome": "Primary page retrieved; dates/abstract or version history inspected. See paper record or deferred lead."}, {"query_or_url": "https://arxiv.org/abs/2611.04303", "checked_at": "2026-11-07T21:20:47.223810+00:00", "outcome": "Primary page retrieved; dates/abstract or version history inspected. See paper record or deferred lead."}, {"query_or_url": "https://arxiv.org/abs/2611.02897", "checked_at": "2026-11-07T21:21:47.873518+00:00", "outcome": "Primary page retrieved; dates/abstract or version history inspected. See paper record or deferred lead."}, {"query_or_url": "https://arxiv.org/abs/2604.09568", "checked_at": "2026-11-07T21:13:28.617270+00:00", "outcome": "Primary page retrieved; dates/abstract or version history inspected. See paper record or deferred lead."}] | Four required GR/CV new/recent scans completed observed pagination with no errors/unvisited links; all 1062 listing IDs resolved. 283 target/uncertain and 333 catchup-review abstracts delivered and individually triaged. Other categories not separately scanned; many non-attention lookback abstracts remain unreviewed; older intermediate version histories unresolved except three inspected leads. |
| hugging_face | partial | [{"query_or_url": "https://huggingface.co/papers/date/2026-11-02", "checked_at": "2026-11-07T21:05:18.411565+00:00", "outcome": "Target-day curation page inspected as discovery lead, not publication authority; Wizard lead retained. Full independent identity/abstract screening of all curated entries not completed."}] | Daily curation is not submission date; not every curated paper independently resolved. Bounded page inspection only. |
| openreview | partial | [{"query_or_url": "agent CAD generation reconstruction editing constraint solver November 2026 site:openreview.net", "checked_at": "2026-11-07T21:06:27.701715+00:00", "outcome": "Hosted web search returned cited leads; not exhaustive coverage. Search dates are not accepted without primary verification."}] | One site-targeted hosted search; no exhaustive note API walk and no selected OpenReview PDF. |
| official_venues | partial | [{"query_or_url": "agent physical simulation particle effects deformable world 2026 research SIGGRAPH", "checked_at": "2026-11-07T21:07:58.330233+00:00", "outcome": "Hosted web search returned cited leads; not exhaustive coverage. Search dates are not accepted without primary verification."}, {"query_or_url": "https://www.scitepress.org/PublishedPapers/2026/152298/", "checked_at": "2026-11-07T21:09:11.751379+00:00", "outcome": "Primary page retrieved; dates/abstract or version history inspected. See paper record or deferred lead."}] | Publisher abstract plus SIGGRAPH-related search; no complete proceedings walk; exact dates missing for publisher lead. |
| project_author_lab | partial | [{"query_or_url": "agent SVG diagram chart slide poster editable visual feedback research November 2 2026 October 27 2026", "checked_at": "2026-11-07T21:05:42.267818+00:00", "outcome": "Hosted web search returned cited leads; not exhaustive coverage. Search dates are not accepted without primary verification."}, {"query_or_url": "agent 3D object procedural modeling Blender material inverse graphics research 2026 project", "checked_at": "2026-11-07T21:06:06.384851+00:00", "outcome": "Hosted web search returned cited leads; not exhaustive coverage. Search dates are not accepted without primary verification."}, {"query_or_url": "agent 3D scene layout world generation BIM architecture October 2026 November 2 2026", "checked_at": "2026-11-07T21:06:53.806263+00:00", "outcome": "Hosted web search returned cited leads; not exhaustive coverage. Search dates are not accepted without primary verification."}, {"query_or_url": "agent articulated asset joint mechanism rig generation research 2026", "checked_at": "2026-11-07T21:07:12.415108+00:00", "outcome": "Hosted web search returned cited leads; not exhaustive coverage. Search dates are not accepted without primary verification."}, {"query_or_url": "agent animation cutscene temporal scene cinematography research November 2026", "checked_at": "2026-11-07T21:07:29.536500+00:00", "outcome": "Hosted web search returned cited leads; not exhaustive coverage. Search dates are not accepted without primary verification."}, {"query_or_url": "agent graphics benchmark world auditing verification November 2026 October 27 2026", "checked_at": "2026-11-07T21:08:17.309217+00:00", "outcome": "Hosted web search returned cited leads; not exhaustive coverage. Search dates are not accepted without primary verification."}, {"query_or_url": "graphics agent memory replanning tool interface feedback program synthesis 2026 project lab", "checked_at": "2026-11-07T21:08:47.195201+00:00", "outcome": "Hosted web search returned cited leads; not exhaustive coverage. Search dates are not accepted without primary verification."}, {"query_or_url": "https://computationalrobotics.seas.harvard.edu/SceneAgent/", "checked_at": "2026-11-07T21:09:11.456875+00:00", "outcome": "Primary page retrieved; dates/abstract or version history inspected. See paper record or deferred lead."}] | SceneAgent project page and cited project/lab leads; no comprehensive lab coverage. Acceptance announcement not treated as publication. |

## Query coverage
- 2d: complete; [{'query_or_url': 'agent SVG diagram chart slide poster editable visual feedback research November 2 2026 October 27 2026', 'checked_at': '2026-11-07T21:05:42.267818+00:00', 'outcome': 'Maintained family search executed; this denotes query completion only, not paper completeness.'}]
- object: complete; [{'query_or_url': 'agent 3D object procedural modeling Blender material inverse graphics research 2026 project', 'checked_at': '2026-11-07T21:06:06.384851+00:00', 'outcome': 'Maintained family search executed; this denotes query completion only, not paper completeness.'}]
- cad: complete; [{'query_or_url': 'agent CAD generation reconstruction editing constraint solver November 2026 site:openreview.net', 'checked_at': '2026-11-07T21:06:27.701715+00:00', 'outcome': 'Maintained family search executed; this denotes query completion only, not paper completeness.'}]
- scene: complete; [{'query_or_url': 'agent 3D scene layout world generation BIM architecture October 2026 November 2 2026', 'checked_at': '2026-11-07T21:06:53.806263+00:00', 'outcome': 'Maintained family search executed; this denotes query completion only, not paper completeness.'}]
- articulation: complete; [{'query_or_url': 'agent articulated asset joint mechanism rig generation research 2026', 'checked_at': '2026-11-07T21:07:12.415108+00:00', 'outcome': 'Maintained family search executed; this denotes query completion only, not paper completeness.'}]
- animation: complete; [{'query_or_url': 'agent animation cutscene temporal scene cinematography research November 2026', 'checked_at': '2026-11-07T21:07:29.536500+00:00', 'outcome': 'Maintained family search executed; this denotes query completion only, not paper completeness.'}]
- simulation: complete; [{'query_or_url': 'agent physical simulation particle effects deformable world 2026 research SIGGRAPH', 'checked_at': '2026-11-07T21:07:58.330233+00:00', 'outcome': 'Maintained family search executed; this denotes query completion only, not paper completeness.'}]
- benchmark: complete; [{'query_or_url': 'agent graphics benchmark world auditing verification November 2026 October 27 2026', 'checked_at': '2026-11-07T21:08:17.309217+00:00', 'outcome': 'Maintained family search executed; this denotes query completion only, not paper completeness.'}]
- harness: complete; [{'query_or_url': 'graphics agent memory replanning tool interface feedback program synthesis 2026 project lab', 'checked_at': '2026-11-07T21:08:47.195201+00:00', 'outcome': 'Maintained family search executed; this denotes query completion only, not paper completeness.'}]

## Source-derived candidate coverage

Mechanical audit of collected arXiv titles; relevance and semantic correctness require paper evidence.

- Metadata resolved: 1062 / 1062 collected IDs.
- Target-day / history-uncertain candidates: 283.
- Explicit triage decisions: 283; catalog-page delivery: 283.
- Missing source scans: 0; incomplete scans: 0.
- Unresolved metadata: 0; no triage decision: 0.
- Full candidate IDs and remaining gaps: `coverage-audit.json`. Unreviewed entries are not exclusions.
- Other platforms remain governed by the source ledger; this audit is not exhaustive discovery.

## Borderline graphics contributions

These records are not established core agentic systems. They remain visible with their scope uncertainty.

| Paper | Why borderline |
|---|---|
| Balancing Representations by Identifying and Generating Under-represented Data | Adaptive acquisition changes which image variants are generated, a potentially useful agentic data-generation mechanism. Full text establishes a fixed statistical SSL loop, not a separately demonstrated graphics agent; retain this boundary rather than promote generic feedback to agency. |
| FlowTranslator: Training-Free In-Image Machine Translation with Flow-Based Editing | Image-conditioned LLM specifies semantic text replacements, but the principal contribution is fixed diffusion trajectory control. No autonomous tool choice, model-level feedback or agent-facing deployment is established; the localized editor could materially support graphics agents. |

## Agent-to-graphics evidence

| Paper | Status | Controller | Action / decision | Graphics target | Source |
|---|---|---|---|---|---|
| Parametric CAD Bench v3: Evaluating Agentic Parametric CAD Authoring from Text and Engineering Drawings | core | Model-agent systems, including mini-swe-agent with multimodal Opus 5.5 | Write and execute FreeCAD Python to construct native parametric feature trees | FreeCAD single-body parametric CAD documents | [Sections 3.1–3.2, 5.2; Appendix B, pp.4,8,12–13,19](https://arxiv.org/pdf/2611.02659v1) |
| Visual-to-Executable Procedural Reconstruction of Buildings | core | Fine-tuned Qwen-VL-7B in induction/reflection modes | Rewrite YAML split-and-repeat facade layout based on rendered schematic and image-mask evidence | Procedural facade structure compiled into CGA building assets | [§3 pp.4–5](https://arxiv.org/pdf/2611.03143v1) |
| CounterSketch: Physics-Grounded Counterfactual Reasoning for Sketch-to-Video Generation | core | VLM-guided counterfactual event-chain reasoner | Modify vector geometry/relations and replan physical event chains after constraint failures | Sketch scene graph and object trajectories for animation | [§4 pp.5–7](https://arxiv.org/pdf/2611.04244v1) |
| ScienceVision: Can AI Observe and Reason Like a Scientist? | core | Evaluated model–harness agents, including Astra/Codex | Choose scene targets, viewer inspection and geometric measurements | Native 3D scientific artifacts, CAD assemblies and architectural models | [§3; Appendix F.6 pp.39–40](https://arxiv.org/pdf/2611.04087v1) |
| ProtoFusion: Protocol-Guided Prompt Refinement for Generative Infrared and Visible Image Fusion | core | Frozen Qwen3-VL-8B-Instruct protocol editor | Add environment item, revise principle or add principle controlling paired-image generation | Fusion image content, target saliency and appearance via structured protocol | [§3.1 pp.4–5; §4.1 pp.6–7](https://arxiv.org/pdf/2611.02877v1) |
| Balancing Representations by Identifying and Generating Under-represented Data | scope_dependent | Changing SSL encoder plus fixed percentile/farthest-point acquisition rule | Select 500 anchors and request five frozen diffusion variants per anchor each cycle | Synthetic raster images augmenting training corpus | [§4 pp.4–5; Algorithm 1 p.21](https://arxiv.org/pdf/2611.02952v1) |
| FlowTranslator: Training-Free In-Image Machine Translation with Flow-Based Editing | scope_dependent | Frozen image-conditioned Doubao-Seed-2.0-lite translator, followed by fixed flow-control schedule | Emit source/target captions and translation pairs as JSON, used to condition localized rendering | Raster text regions in scene images | [§3.1 p.5; §4.1 p.7](https://arxiv.org/pdf/2611.04303v1) |

## Prior-day memory and carry-over

Frozen history: `knowledge/daily-history/through-20261015-bvb-v11`. Previously unread records now fully read: 0. Prior pending records still without a new full read: 95.

See history-delta.json for per-paper transitions. Historical results remain in the frozen bundle; not repeated is not excluded, and new-to-history does not mean newly published.

## Abstract-first reading queue

Attention pool: 338; abstracts not delivered: 0; priority/triage gaps: 0; unread ranked leads: 45. See reading-plan.json for model-authored priorities and deferred leads. Priority is not an inclusion judgment or recall guarantee.
