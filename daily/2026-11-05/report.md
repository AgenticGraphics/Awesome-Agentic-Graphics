# Agentic Graphics daily report
Date: 2026-11-05 | Timezone: America/Chicago | As of: 2026-11-07T22:02:47+00:00
browser-based same-day search; documented source coverage
Taxonomy: google-doc-taxonomy-v3-2026-10-15 | Snapshot: authorized_live_snapshot_reconciled_and_frozen

## Coverage limits
- Bounded discovery is not exhaustive. Frozen cutoff and prepared taxonomy/source snapshot preserved; actual retrieval occurred later and all selected PDF versions predate cutoff.
- Four required listing scans covered observed pagination (16/43 cs.GR entries, 258/943 cs.CV entries), deduplicated to 1062 identities, all resolved by official Atom. cs.AI/cs.HC/cs.RO/cs.MM/eess.IV not separately scanned.
- All 179 target-day routed abstracts and all 294 catchup attention abstracts were delivered and individually triaged; overlap deduplicated. 308 individual triage records saved. Remaining 760 catalog records were not abstract-triaged; see unreviewed-catalog-queue.json, not exclusions.
- 17 version-pinned full papers read and checkpointed: three target-day first submissions, four target-day revisions, seven seven-day catch-up papers, and three newly completed older frozen backlog papers. No unchanged completed historical record copied as a new read.
- 42 ranked plausible leads remain unread in reading-plan.json; they are unresolved, including target-day borderline candidates and direct-action catch-up Composable CAD and agentic compression. triage.json preserves provisional rejects, not final excluded records.
- Additional search signals (62) remain in additional-source-deferred.json. Source dates and official abstracts are not verified for all of these. HF curation never establishes publication date.
- OpenReview and official venue coverage is search-only and partial. Project source separately inspected for DyCraft. Nine maintained query families each received one actual hosted search; backend internal queries/open actions are preserved in raw responses but counts use shared tool invocations.
- Finalization reserve reached after 17 full reads; the 20-paper ceiling is not a quota. A further full-paper read/checkpoint could not fit the remaining pre-reserve interval. Reading order deviation is recorded in backlog-plan.json: explicit graphics-action catch-up and three reserved backlog leads were prioritized over speculative target-day transfer-only connections.
- No retained borderline full-text record in this selected direct-action cohort; many provisional borderline leads remain visible in ranked unread queue. This is not a finding that borderline work is irrelevant.
- Taxonomy uncertainties are explicit in field_evidence/taxonomy_delta. Model training is not inferred solely from brand; final scoring separated from action feedback; memory lifetime refers to actual cross-call/cross-run retention.
- No inaccessible PDF or unsaved opened canonical candidate at prevalidation audit. No runtime geometry/code demos executed; results are author-reported, not independently reproduced.

## already_reported (0)

## same_day_new (3)

### [ManimCode: Learning Visual Self-Correction for Educational Animation](https://arxiv.org/abs/2611.08294)
core | High | new_relative_to_snapshot
Application: 2D Graphics, Dynamic / Animation and temporal scene; operations: Generation
Small-model visual self-correction trained from 24,034 verified animation records; achieves 96.6%/97.0% render success on two benchmarks.
Scope: A trained multimodal controller writes and revises executable animation programs from render errors, layout diagnostics and its own visual critiques.
Limits: Ten-render budget; visual revisions can oscillate or preserve clipped content. Automatic judge agreement is weak for small score gaps and human evaluation uses one blinded team member. Training primarily improves executability; RL adds little visual-quality gain.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Animation | Creates educational animations explaining processes over time. ([source](https://arxiv.org/pdf/2611.08294v1), §1 p.2) |
| input_form | Language | Each inference request starts from a newly generated program; no reference image required. ([source](https://arxiv.org/pdf/2611.08294v1), §4.2 p.7) |
| output | Program, Rendered Media | Generates animation programs and returns best rendered video. ([source](https://arxiv.org/pdf/2611.08294v1), §4.2 p.7; Fig.3) |
| model_type | VLM | Same 4B model reviews sampled frames and generates code. ([source](https://arxiv.org/pdf/2611.08294v1), §4.1 pp.5–6) |
| model_training | Supervised Fine-Tuning, RL Post-Training | Role-conditioned SFT followed by Reviser RLOO RL, both LoRA trained. ([source](https://arxiv.org/pdf/2611.08294v1), §4; Appendix B.2 p.16) |
| planning | Not Reported | Scene loop specifies roles and stopping rules, not a represented task plan. Lecture plans belong to external long-form systems. ([source](https://arxiv.org/pdf/2611.08294v1), §4.2; Appendix A.3, C.3) |
| workflow | Sequential | Write, render, review, revise repeatedly. ([source](https://arxiv.org/pdf/2611.08294v1), Fig.3; §4.2) |
| update_strategy | Regeneration, Candidate Selection, Rollback | Reviser rewrites full program; retains best; revision base reverts to best if alignment/completeness drop exceeds 0.5. ([source](https://arxiv.org/pdf/2611.08294v1), §3.2 p.5; Table 7 p.15) |
| verifier | Self, Programmatic, Environment | Same model critiques frames; geometric checker reports layout defects; renderer reports crashes. ([source](https://arxiv.org/pdf/2611.08294v1), §3.2; §4.2; A.3) |
| feedback_assessment | Score, Diagnosis, Binary | Four 1–5 review scores, specific defects and render success/error change revision and acceptance. ([source](https://arxiv.org/pdf/2611.08294v1), §3.2; Table 7) |
| feedback_observation | Visual, Structural Scene State, Runtime | Eight frames, object positions at pauses, and execution errors. ([source](https://arxiv.org/pdf/2611.08294v1), §3.2 p.5) |
| memory_time | Short-Term Memory | Current program and best program persist across revision rounds. ([source](https://arxiv.org/pdf/2611.08294v1), §3.2; Table 7) |
| memory_reach | Global Memory | Role contexts pass current program, review and selected revision base through shared loop. ([source](https://arxiv.org/pdf/2611.08294v1), §4.1 pp.5–6; Table 7) |
| action_type | Code/Script | Writes complete Python Manim program. ([source](https://arxiv.org/pdf/2611.08294v1), §3.2) |
| graphics_software | General-Purpose | Native ManimCE v0.19.1 scripts and eight plugins. ([source](https://arxiv.org/pdf/2611.08294v1), A.2–A.3 p.15) |
| tools | Execution Utilities, Graphics Operations, Static Validator | Program execution/rendering and geometric layout checks. ([source](https://arxiv.org/pdf/2611.08294v1), §3.2; A.3) |
| resources | Documentation & Rules, Examples & Trajectories | Retrieves API documentation, best-practice rules and verified example scenes. ([source](https://arxiv.org/pdf/2611.08294v1), A.2 p.15) |
| representation | Code, Layouts, Pixels | Programs, positioned text/diagram objects and rendered frames. ([source](https://arxiv.org/pdf/2611.08294v1), §3.2; Fig.5) |

next_action: "Review/add evidence-grounded record; retain stated taxonomy uncertainties. No survey source mutation authorized."

Events: [{"type": "first_submission", "value": "2026-11-05T16:55:44+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2611.08294", "authority": "primary", "version": "v1", "evidence": "Canonical history v1; 2026-11-05 10:55:44 America/Chicago.", "local_value": "2026-11-05T10:55:44-06:00", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: ["Planning is not inferred from the fixed loop; external lecture planning excluded.", "Tools remain provisional; native scripting classified General-Purpose despite added checking/retrieval."]

### [Deformable Contact-Aware 3D Object Placement](https://arxiv.org/abs/2611.08005)
core | High | new_relative_to_snapshot
Application: Static / Scene; operations: Editing
Separates semantic release planning from deformable settling; reports 72.3% lower penetration than strongest raw rigid baseline on 2,063 placement cases.
Scope: GPT-5.2 selects support, scale, orientation, anchor and material IDs that instantiate a simulated 3D placement. Fixed orchestration still contains explicit model decisions on graphics state.
Limits: Simplified isotropic material parameters and reconstruction quality bound fidelity; simulated feasibility is not real-world safety. Mean runtime 107.5 seconds. Final diagnostics do not establish a model replanning loop.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Modeling | Output is settled object placement and deformed geometry. ([source](https://arxiv.org/pdf/2611.08005v1), §3 p.3) |
| input_form | Language, 3D Representation | Scene mesh S, prompt p and object mesh MO. ([source](https://arxiv.org/pdf/2611.08005v1), §3) |
| output | Graphics Artifact, Structured Specification | Returns settled geometries, rotation/translation, feasibility flag and diagnostic measurements. ([source](https://arxiv.org/pdf/2611.08005v1), §3 equation y) |
| model_type | VLM | GPT-5.2 handles JSON parsing and rendered orientation selection. ([source](https://arxiv.org/pdf/2611.08005v1), Table 6 p.13) |
| model_training | Off-the-Shelf | Planner parameters comprise fixed prompts, perception modules and geometric rules; cloud API configuration with deterministic decoding. ([source](https://arxiv.org/pdf/2611.08005v1), §4; Appendix A) |
| planning | PO-1 | Fixed release-state planner stages construct z0 then simulator executes it. ([source](https://arxiv.org/pdf/2611.08005v1), §4 Eq.1, Table 1) |
| workflow | Sequential | Synchronous model calls, staged release construction then rollout. ([source](https://arxiv.org/pdf/2611.08005v1), §4; Table 14) |
| update_strategy | Candidate Selection, Local Patch, Regeneration | Select one of three orientations; clamp scale/change invalid anchors; retry malformed JSON twice. ([source](https://arxiv.org/pdf/2611.08005v1), B.3; Table 10) |
| verifier | Self, Programmatic | Model confidence gates fallbacks; parser/schema and geometry checks trigger repair. ([source](https://arxiv.org/pdf/2611.08005v1), Appendix B and Table 10) |
| feedback_assessment | Score, Diagnosis | Confidence thresholds and parser errors drive retry/fallback. ([source](https://arxiv.org/pdf/2611.08005v1), Table 10) |
| feedback_observation | Visual, Structural Scene State, Runtime | Orientation images, support/part availability, parser error messages. ([source](https://arxiv.org/pdf/2611.08005v1), B.3; Table 10) |
| memory_time | Short-Term Memory | Each stage estimates part of z0 and passes state onward with uncertainty. ([source](https://arxiv.org/pdf/2611.08005v1), §4 p.4) |
| memory_reach | Global Memory | All modules fill common release-state components used by simulator. ([source](https://arxiv.org/pdf/2611.08005v1), §4 Table 1) |
| action_type | Structured Specification | JSON support/size, target/anchor, best_view and material IDs. ([source](https://arxiv.org/pdf/2611.08005v1), Appendix B) |
| graphics_software | Agent-Adapted | JSON planner fields are translated through custom grounding and Genesis rigid–MPM coupling. ([source](https://arxiv.org/pdf/2611.08005v1), §4; Appendix A) |
| tools | Graphics Operations, Perception models, Solver Validator, Static Validator | Ray casting/rendering, segmentation models, coupled simulation, schema and geometry checking. ([source](https://arxiv.org/pdf/2611.08005v1), Table 6; §4) |
| resources | Documentation & Rules | Curated material library, synonym dictionary and category scale ranges accessed during placement. ([source](https://arxiv.org/pdf/2611.08005v1), Appendices B–D) |
| representation | Geometry, Dynamic State, Pixels | Meshes, particles with evolving state and rendered orientation candidates. ([source](https://arxiv.org/pdf/2611.08005v1), §3–4) |

next_action: "Review/add evidence-grounded record; retain stated taxonomy uncertainties. No survey source mutation authorized."

Events: [{"type": "first_submission", "value": "2026-11-05T13:28:51+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2611.08005", "authority": "primary", "version": "v1", "evidence": "Canonical history; 07:28:51 Chicago target day.", "local_value": "2026-11-05T07:28:51-06:00", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: ["Simulation is a tool for static placement, not automatically a Simulation task label.", "The model planner uses fixed release-state stages; PO-1 versus absent multi-step plan is a definitional boundary."]

### [Seeing Beyond the Next Step: World-Model-Guided Human-Like Navigation in Multi-Agent Scenes](https://arxiv.org/abs/2611.07730)
core | High | new_relative_to_snapshot
Application: Dynamic / Animation and temporal scene; operations: Generation
Distills two task-aligned future predictors into real-time crowd steering; 65 ms deployed decisions versus 1.2 s online world-model planning.
Scope: The policy controls executable motion anchors of virtual pedestrians in Unity crowd simulations, explicitly evaluated for crowd motion naturalness rather than only robot navigation.
Limits: 100-anchor vocabulary and one-anchor future horizons restrict rare or delayed behavior. Unity scenes rely on nonredistributable commercial assets; no real robot validation. User study has 20 observers.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Animation | Generates perceptually human-like virtual crowd trajectories. ([source](https://arxiv.org/pdf/2611.07730v1), §2, §4) |
| input_form | Image, Language | Third-person RGB with structured textual ego/goal/entity context. ([source](https://arxiv.org/pdf/2611.07730v1), §3 Eq.1; Appendix K) |
| output | Structured Specification | Single integer indexes a predefined executable motion trajectory. ([source](https://arxiv.org/pdf/2611.07730v1), Appendix K) |
| model_type | VLM | Qwen3-VL-2B-Instruct backbone. ([source](https://arxiv.org/pdf/2611.07730v1), Appendix A) |
| model_training | Supervised Fine-Tuning, RL Post-Training | Supervised anchor classification followed by GRPO, LoRA updated. ([source](https://arxiv.org/pdf/2611.07730v1), §3.1,3.3; Appendix A) |
| planning | Not Applicable | World models are preference oracles, not planners; selected anchor is action abstraction. ([source](https://arxiv.org/pdf/2611.07730v1), §3.3 p.6; Appendix J) |
| workflow | Sequential | Construct ten candidates, predict outcomes, compute scores, update GRPO policy. ([source](https://arxiv.org/pdf/2611.07730v1), §3.3) |
| update_strategy | Not Applicable | Scores change policy weights via GRPO rather than regenerate/patch an artifact or select a retained best graphics candidate. ([source](https://arxiv.org/pdf/2611.07730v1), §3.3) |
| verifier | Programmatic | Fixed formulas score progress, smoothness, risk and semantic validity from predicted consequences. ([source](https://arxiv.org/pdf/2611.07730v1), Eq.6; Appendix B) |
| feedback_assessment | Score | Scalar score and group-relative advantages guide policy refinement. ([source](https://arxiv.org/pdf/2611.07730v1), Eq.6) |
| feedback_observation | Visual, Structural Scene State | Predicted segmentation maps and position/velocity consequences determine rewards. ([source](https://arxiv.org/pdf/2611.07730v1), §3.2–3.3) |
| memory_time | Short-Term Memory | Predictors take three history frames plus current RGB; previous ego velocity retained. ([source](https://arxiv.org/pdf/2611.07730v1), §3.2 p.5; Appendix A) |
| memory_reach | Local Memory | Each controlled agent uses its own ego-centered temporal context. ([source](https://arxiv.org/pdf/2611.07730v1), §3.2 Eq.ht) |
| action_type | Structured Specification | One anchor index selects trajectory from vocabulary. ([source](https://arxiv.org/pdf/2611.07730v1), Appendix K) |
| graphics_software | Agent-Adapted | Unity reconstructed scenes provide ego-frame state and anchor execution. ([source](https://arxiv.org/pdf/2611.07730v1), §4.1; Appendix K) |
| tools | Perception models | Frozen state and semantic predictors queried for candidate consequences. ([source](https://arxiv.org/pdf/2611.07730v1), §3.2–3.3) |
| resources | Examples & Trajectories, Documentation & Rules | 100 demonstration-derived anchors and explicit semantic scoring rules reused. ([source](https://arxiv.org/pdf/2611.07730v1), §3.1; Appendix B–D) |
| representation | Dynamic State, Pixels, Learned State | Positions/velocities, RGB/segmentation images, learned consequence models. ([source](https://arxiv.org/pdf/2611.07730v1), §3) |

next_action: "Review/add evidence-grounded record; retain stated taxonomy uncertainties. No survey source mutation authorized."

Events: [{"type": "first_submission", "value": "2026-11-05T09:42:12+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2611.07730", "authority": "primary", "version": "v1", "evidence": "Canonical v1 history; Chicago 03:42:12.", "local_value": "2026-11-05T03:42:12-06:00", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: ["Gradient policy refinement is not represented by artifact update-strategy labels.", "Crowd animation demonstrated in Unity makes this core despite robotics applications; not a generic robot-control inclusion."]

## same_day_updates (4)

### [DreamRealm: Exploring and Materializing Hallucination Worlds for Trustworthy Vision-Language Models](https://arxiv.org/abs/2611.06433)
core | High | new_relative_to_snapshot
Application: 2D Graphics; operations: Editing, Generation
Hallucination-conditioned verified image editing yields 28,960 human-approved examples; resulting correspondence training improves HallusionBench by 7.26 points.
Scope: Gemini planner determines local/global edits, preservation regions and fallback image-generation actions; quality feedback changes subsequent synthesis attempts.
Limits: Only 30.07% of editing candidates survive human review. Commercial editing and human annotation incur cost; minimality is subjective score-constrained, not guaranteed. Worked trace lacks human result and is not final admission proof.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Modeling | Changes object counts, attributes and scene content in raster images. ([source](https://arxiv.org/pdf/2611.06433v2), §3.2) |
| input_form | Image, Language | Original image, question, true answer and target response. ([source](https://arxiv.org/pdf/2611.06433v2), Algorithm 1) |
| output | Rendered Media | Curated edited image with QA metadata. ([source](https://arxiv.org/pdf/2611.06433v2), Algorithm 1 Ensure) |
| model_type | VLM | Gemini 2.5 Pro examines image, plans edits and scores outputs. ([source](https://arxiv.org/pdf/2611.06433v2), Appendix E) |
| model_training | Off-the-Shelf | Named API versions used for editing/planning; training is separately specified for Qwen target model. ([source](https://arxiv.org/pdf/2611.06433v2), Appendices D–F) |
| planning | PO-2 | Model produces t0, preservation/change regions and three ordered instructions inside fixed retry scaffold. ([source](https://arxiv.org/pdf/2611.06433v2), Algorithm 1 line 6) |
| workflow | Graph-Structured | Nested instruction/type/attempt loops; strict, relaxed and skip verification branches. ([source](https://arxiv.org/pdf/2611.06433v2), Algorithm 1) |
| update_strategy | Local Patch, Regeneration | Minimal local edit preferred, full-image redraw fallback permitted. ([source](https://arxiv.org/pdf/2611.06433v2), Appendix A) |
| verifier | Self, Human | Same V plans and verifies; annotators decide final acceptance. ([source](https://arxiv.org/pdf/2611.06433v2), Algorithm 1; D.2) |
| feedback_assessment | Score, Binary | Edit success/plausibility/minimality scores; blind YES/equivalence checks control retry. ([source](https://arxiv.org/pdf/2611.06433v2), Algorithm 1 lines 14–33) |
| feedback_observation | Visual | Original and edited images supplied to visual checks. ([source](https://arxiv.org/pdf/2611.06433v2), §3.2) |
| memory_time | Short-Term Memory | Ordered instructions, regions and retry indices retained through per-edit execution. ([source](https://arxiv.org/pdf/2611.06433v2), Algorithm 1) |
| memory_reach | Global Memory | Plan and original-target record are reused by synthesis and verification calls. ([source](https://arxiv.org/pdf/2611.06433v2), Algorithm 1) |
| action_type | Tool/Function Call | Synth invokes GPT-Image-2 with model-planned edit instruction and type. ([source](https://arxiv.org/pdf/2611.06433v2), Algorithm 1 line 12; Appendix E) |
| graphics_software | Agent-Adapted | Wrap/Synth adapts instructions and selected edit modes to image generator. ([source](https://arxiv.org/pdf/2611.06433v2), Algorithm 1) |
| tools | Perception models, Execution Utilities | Image generator and UploadOSS/curation utilities. ([source](https://arxiv.org/pdf/2611.06433v2), Algorithm 1; D.1) |
| resources | Documentation & Rules | Minimal-edit rules and question-dependent verification modes are reused. ([source](https://arxiv.org/pdf/2611.06433v2), Appendix A) |
| representation | Pixels | Original and edited raster images. ([source](https://arxiv.org/pdf/2611.06433v2), §3.2; Figures 6–8) |

next_action: "Review/add evidence-grounded record; retain stated taxonomy uncertainties. No survey source mutation authorized."

Events: [{"type": "first_submission", "value": "2026-11-04T12:34:12+00:00", "precision": "timestamp", "timezone": "UTC", "authority": "primary", "primary_url": "https://arxiv.org/abs/2611.06433", "version": "v1", "evidence": "Official Atom published; prior day Chicago.", "local_value": "2026-11-04T06:34:12-06:00", "prior_event_status": "not_seen_in_supplied_history"}, {"type": "revision", "value": "2026-11-05T06:45:33+00:00", "precision": "timestamp", "timezone": "UTC", "authority": "primary", "primary_url": "https://arxiv.org/abs/2611.06433", "version": "v2", "evidence": "Official Atom updated and canonical v2 history; Chicago 00:45:33.", "local_value": "2026-11-05T00:45:33-06:00", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: ["Modeling for raster counterfactual editing is a coarse task mapping; no new taxonomy label proposed.", "Human acceptance is a curation gate, not human-guided iterative repair."]

### [NeoWorld-Pro: Programming Interactive Scenes from Monocular Images for Embodied Simulation](https://arxiv.org/abs/2608.24212)
core | High | new_relative_to_snapshot
Application: Dynamic / Articulated assets, Static / Scene; operations: Reconstruction
Physics-in-the-loop procedural reconstruction reaches 216 matched joints out of 245 and improves closed-loop scene task success over open-loop baseline.
Scope: MLLM agents produce and refine explicit Blender/URDF graphics programs from rendered and simulated physical failures.
Limits: Rigid/articulated quasi-static assets only; evaluation fewer than ten objects and 30 scenes. Referenced Appendix A.1 is absent from delivered 13-page PDF, limiting reproduction details. Scene CEM and manipulation-policy extensions are not mixed into object-level taxonomy.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Modeling | Reconstruct geometry and articulation of assets. ([source](https://arxiv.org/pdf/2608.24212v3), §3.2) |
| input_form | Image | Single RGB scene image, segmented into object crops. ([source](https://arxiv.org/pdf/2608.24212v3), §3.1) |
| output | Program, Graphics Artifact | Executable Blender Python programs and compiled URDF assets. ([source](https://arxiv.org/pdf/2608.24212v3), §3.1–3.2) |
| model_type | VLM | MLLM reasoner uses images, simulation frames and code. ([source](https://arxiv.org/pdf/2608.24212v3), §3.2) |
| model_training | Off-the-Shelf | Zero-shot code synthesis without dataset-specific training. ([source](https://arxiv.org/pdf/2608.24212v3), §1 p.2) |
| planning | Not Reported | Fixed generation stages and scene hierarchy are described; no explicit task-plan representation. No plan/prompt matches. ([source](https://arxiv.org/pdf/2608.24212v3), §3.2; full text search) |
| workflow | Sequential | Sequential geometry, articulation, export, then physical refinement. ([source](https://arxiv.org/pdf/2608.24212v3), §3.2 steps 1–3) |
| update_strategy | Local Patch | Iterative code editing and specific friction, damping, mass changes. ([source](https://arxiv.org/pdf/2608.24212v3), §3.2; Fig.3) |
| verifier | Critic, Environment, Programmatic | MLLM-Critic checks outputs; engine executes tests; numerical criteria accept trajectories. ([source](https://arxiv.org/pdf/2608.24212v3), §3.2 pp.5–6) |
| feedback_assessment | Diagnosis, Binary | Wrong axis/missing joint diagnoses and pass/fail physical acceptance. ([source](https://arxiv.org/pdf/2608.24212v3), §3.2; Fig.2) |
| feedback_observation | Visual, Structural Scene State, Runtime | Rendered outputs, trajectory measurements and execution failures. ([source](https://arxiv.org/pdf/2608.24212v3), §3.2) |
| memory_time | Short-Term Memory | Generated code reused across stages and iteratively modified. ([source](https://arxiv.org/pdf/2608.24212v3), §3.2 p.5) |
| memory_reach | Global Memory | Reasoner, Programmer and Critic inspect/refine common object program. ([source](https://arxiv.org/pdf/2608.24212v3), Fig.2; §3.2) |
| action_type | Code/Script | MLLM writes Blender Python and export scripts. ([source](https://arxiv.org/pdf/2608.24212v3), §3.2) |
| graphics_software | General-Purpose | Direct executable Blender Python programs and URDF export. ([source](https://arxiv.org/pdf/2608.24212v3), §3.2) |
| tools | Graphics Operations, Execution Utilities, Solver Validator | Blender construction/rendering, runtime execution, CoACD collision geometry and Isaac Sim tests. ([source](https://arxiv.org/pdf/2608.24212v3), §3.2) |
| resources | Not Reported | Avoids curated asset libraries; no documentation/example retrieval described; no documentation or prompt matches. ([source](https://arxiv.org/pdf/2608.24212v3), §1–3; full PDF search) |
| representation | Code, Geometry, Dynamic State, Pixels | Scripts, URDF meshes/joints, simulated trajectories and render frames. ([source](https://arxiv.org/pdf/2608.24212v3), §3.2) |

next_action: "Review/add evidence-grounded record; retain stated taxonomy uncertainties. No survey source mutation authorized."

Events: [{"type": "first_submission", "value": "2026-08-25T08:19:39+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2608.24212", "authority": "primary", "version": "v1", "evidence": "Canonical history.", "local_value": "2026-08-25T03:19:39-05:00", "prior_event_status": "not_seen_in_supplied_history"}, {"type": "revision", "value": "2026-10-20T01:44:59+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2608.24212", "authority": "primary", "version": "v2", "evidence": "Canonical history.", "local_value": "2026-10-19T20:44:59-05:00", "prior_event_status": "not_seen_in_supplied_history"}, {"type": "revision", "value": "2026-11-05T06:32:22+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2608.24212", "authority": "primary", "version": "v3", "evidence": "Canonical history latest before cutoff; Chicago 00:32:22.", "local_value": "2026-11-05T00:32:22-06:00", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: ["Explicit scene hierarchy is not automatically an agent task plan.", "Final scene CEM uses score/ranking and candidate selection but is outside the selected object-level subsystem."]

### [EvoDesign: Agentic Editable Diagram Creation via Design Expertise Evolution](https://arxiv.org/abs/2604.09568)
core | High | known_discussed_paper
Application: 2D Graphics; operations: Generation, Editing
Editable schema plus local verification and evidence-linked expertise memory; 6,273-case CanvasBench and 36-person user study.
Scope: Structure/style/layout agents emit canvas objects; refiner applies localized manifest operations from rendered verification.
Limits: Restricted canvas expressivity, cold-start memory and model transfer unresolved. Reference-derived benchmark inputs favor structured diagrams; multistage latency and judge-dependent evaluation limit conclusions.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Visualization | Diagrams communicate semantic topology and reduce cognitive load. ([source](https://arxiv.org/pdf/2604.09568v3), §1) |
| input_form | Language | Semantic content c and optional textual requirements r. ([source](https://arxiv.org/pdf/2604.09568v3), §3) |
| output | Structured Specification, Graphics Artifact | Manifest D and directly editable canvas artifact exposed to users. ([source](https://arxiv.org/pdf/2604.09568v3), §3, Appendix F) |
| model_type | VLM | VLM backbones including GPT-5.5 and Gemini-3.1-Pro used across roles. ([source](https://arxiv.org/pdf/2604.09568v3), §6.1; Appendix C) |
| model_training | Not Reported | Backbones and temperature specified; no fine-tuning/weight-update statement. Training split supports memory evolution. ([source](https://arxiv.org/pdf/2604.09568v3), §6.1, Appendix C; full-text searches) |
| planning | PO-2 | Each role first produces high-level design specification then instantiates fields. ([source](https://arxiv.org/pdf/2604.09568v3), §4.1; B.2) |
| workflow | Sequential | Structure then style then layout then diagnose/refine; main experiments one pass. ([source](https://arxiv.org/pdf/2604.09568v3), Algorithm 1) |
| update_strategy | Local Patch | Targeted edits instead of whole diagram regeneration. ([source](https://arxiv.org/pdf/2604.09568v3), §4.2) |
| verifier | Critic, Programmatic | Objective overlap/crossing checks plus VLM critique. ([source](https://arxiv.org/pdf/2604.09568v3), §4.2) |
| feedback_assessment | Score, Diagnosis | Prioritized defect findings and 0–10 weighted diagnostic score guide repair. ([source](https://arxiv.org/pdf/2604.09568v3), §4.2 Eq.1) |
| feedback_observation | Visual, Structural Scene State | Rendered diagram and element-level geometry checked. ([source](https://arxiv.org/pdf/2604.09568v3), §4.2) |
| memory_time | Short-Term Memory, Long-Term Memory | Current manifest and refinement trace retained; design knowledge retrieved across future tasks. ([source](https://arxiv.org/pdf/2604.09568v3), §4.3; Algorithm 1) |
| memory_reach | Global Memory | Agents query same M with role/context filters. ([source](https://arxiv.org/pdf/2604.09568v3), §4.3 p.6) |
| action_type | Structured Specification | Agents instantiate and update canvas schema fields. ([source](https://arxiv.org/pdf/2604.09568v3), §4.1–4.2) |
| graphics_software | Agent-Adapted | LangGraph plus schema/diagnostic adapter around Excalidraw. ([source](https://arxiv.org/pdf/2604.09568v3), §6.1; B.4–5) |
| tools | Graphics Operations, Static Validator | Rendering and geometric size estimator plus overlap/overflow checks. ([source](https://arxiv.org/pdf/2604.09568v3), §4.2; B.5) |
| resources | Documentation & Rules, Examples & Trajectories | Canvas API knowledge, design rules and trace-grounded sample strategies retrieved. ([source](https://arxiv.org/pdf/2604.09568v3), Fig.2; §4.3) |
| representation | Layouts, Pixels | Object-level layouts and rendered images. ([source](https://arxiv.org/pdf/2604.09568v3), §3–4) |

next_action: "Review/add evidence-grounded record; retain stated taxonomy uncertainties. No survey source mutation authorized."

Events: [{"type": "first_submission", "value": "2026-02-20T11:11:02+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2604.09568", "authority": "primary", "version": "v1", "evidence": "Canonical history.", "local_value": "2026-02-20T05:11:02-06:00", "prior_event_status": "not_seen_in_supplied_history"}, {"type": "revision", "value": "2026-10-05T17:32:59+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2604.09568", "authority": "primary", "version": "v2", "evidence": "Canonical history.", "local_value": "2026-10-05T12:32:59-05:00", "prior_event_status": "not_seen_in_supplied_history"}, {"type": "revision", "value": "2026-11-05T18:18:33+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2604.09568", "authority": "primary", "version": "v3", "evidence": "Latest history at cutoff; Chicago 12:18:33.", "local_value": "2026-11-05T12:18:33-06:00", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: ["Task-time workflow separated from graph-like cross-task expertise promotion.", "Memory evolution is not model-training evidence; model_training remains Not Reported."]

### [WorldAct: Activating Monolithic 3D Worlds into Interactive-Ready Object-Centric Scenes](https://arxiv.org/abs/2605.15843)
core | High | known_discussed_paper
Application: Static / Scene; operations: Editing, Reconstruction
Agent guidance raises interactable object recall from 23.77% to 78.80% on Marble and 8.10% to 70.97% on HY-World.
Scope: VLM object and viewpoint decisions directly control removal/reconstruction of graphics content.
Limits: Ten evaluated scenes; approximately one hour conversion. Physical parameters manually assigned, rigid objects only. Regenerated object quality improves while scene-level human naturalness decreases from 4.20 to 3.78.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Modeling | Creates decomposed editable 3D scene assets. ([source](https://arxiv.org/pdf/2605.15843v2), §4.1) |
| input_form | 3D Representation | Input monolithic 3DGS G; observations rendered internally. ([source](https://arxiv.org/pdf/2605.15843v2), §4.1) |
| output | Graphics Artifact | Completed background/collision mesh and aligned object assets. ([source](https://arxiv.org/pdf/2605.15843v2), §4.4) |
| model_type | VLM | Qwen3.6-Plus vision-language model. ([source](https://arxiv.org/pdf/2605.15843v2), B.2) |
| model_training | Off-the-Shelf | Vision and scoring modules use prompted Qwen3.6-Plus API; adaptation only described for downstream robot. ([source](https://arxiv.org/pdf/2605.15843v2), B.2–4) |
| planning | Not Reported | Object inventory and fixed processing order, no explicit agent task plan. ([source](https://arxiv.org/pdf/2605.15843v2), Algorithm 1; full-text plan search) |
| workflow | Sequential | Parse, initialize memory, segment/score/select per object, deduplicate, inpaint. ([source](https://arxiv.org/pdf/2605.15843v2), Algorithm 1) |
| update_strategy | Candidate Selection | Argmax view scores and highest DINO pose similarity select candidates. ([source](https://arxiv.org/pdf/2605.15843v2), B.4; §4.4) |
| verifier | Self, Programmatic | Same Qwen assesses crops; DINO similarity chooses initial pose. ([source](https://arxiv.org/pdf/2605.15843v2), B.4; §4.4) |
| feedback_assessment | Score | 0–100 crop score controls best-view choice. ([source](https://arxiv.org/pdf/2605.15843v2), B.4) |
| feedback_observation | Visual | Candidate crops and rendered object views. ([source](https://arxiv.org/pdf/2605.15843v2), B.4; §4.4) |
| memory_time | Short-Term Memory | Inventory dictionary and processing states retained across pipeline. ([source](https://arxiv.org/pdf/2605.15843v2), B.3) |
| memory_reach | Global Memory | Central memory supplies execution module object prompts. ([source](https://arxiv.org/pdf/2605.15843v2), B.3) |
| action_type | Tool/Function Call | Agent invokes SAM3 with selected text prompts and passes selected view to SAM3D. ([source](https://arxiv.org/pdf/2605.15843v2), B.1,B.4) |
| graphics_software | Agent-Adapted | Custom selection/memory/execution wrapper orchestrates existing segmenter and reconstruction tools. ([source](https://arxiv.org/pdf/2605.15843v2), B.5; §4) |
| tools | Perception models, Graphics Operations | SAM3, SAM3D, Diffueraser, DepthLab and DINO; rendering, mask lifting, ICP and Poisson reconstruction. ([source](https://arxiv.org/pdf/2605.15843v2), §4) |
| resources | Documentation & Rules | Portable/fixed taxonomy and explicit completeness/clarity/centeredness scoring criteria. ([source](https://arxiv.org/pdf/2605.15843v2), B.2,B.4) |
| representation | Geometry, Learned State, Pixels | Gaussian scene, learned Gaussian appearance, meshes and rendered/inpainted frames. ([source](https://arxiv.org/pdf/2605.15843v2), §3–4) |

next_action: "Review/add evidence-grounded record; retain stated taxonomy uncertainties. No survey source mutation authorized."

Events: [{"type": "first_submission", "value": "2026-05-15T10:56:23+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2605.15843", "authority": "primary", "version": "v1", "evidence": "Canonical history.", "local_value": "2026-05-15T05:56:23-05:00", "prior_event_status": "not_seen_in_supplied_history"}, {"type": "revision", "value": "2026-11-05T07:15:15+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2605.15843", "authority": "primary", "version": "v2", "evidence": "Canonical history latest at cutoff; Chicago 01:15:15.", "local_value": "2026-11-05T01:15:15-06:00", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: ["Core does not require an iterative repair loop: object selection causally controls graphics operations.", "Prompt criteria counted as Documentation & Rules; no retrieved asset library claimed."]

## late_discovery (10)

### [CADFather: Autonomous CAD Reconstruction through Coordinated Tool Use](https://arxiv.org/abs/2610.09127)
core | High | new_relative_to_snapshot
Application: Static / CAD; operations: Reconstruction
Coordinates complementary CAD proposal tools without retraining; reports zero invalid outputs on full DeepCAD, Fusion360 and MCB and higher IoU than published CADENA sampling.
Scope: Assistant chooses candidates, CAD tools, sample counts and stopping from executed geometry feedback.
Limits: Comparisons mix input modalities, subsets and validity protocols. Tool ablations do not isolate assistant selection or match consumed compute. Fixed DSL cannot recover arbitrary engineering intent; wrong initial topology and resource limits remain failure modes.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Modeling | Editable parametric CAD reconstruction. ([source](https://arxiv.org/pdf/2610.09127v1), §1) |
| input_form | 3D Representation | Target mesh M*. Renders generated internally. ([source](https://arxiv.org/pdf/2610.09127v1), §3.1) |
| output | Program, Graphics Artifact | Final CAD program and mesh. ([source](https://arxiv.org/pdf/2610.09127v1), Fig.1) |
| model_type | VLM | Qwen3.8-27B vision-language assistant. ([source](https://arxiv.org/pdf/2610.09127v1), §4.1) |
| model_training | Off-the-Shelf | Both generator and assistant models frozen; no additional training. ([source](https://arxiv.org/pdf/2610.09127v1), §4.1 p.8) |
| planning | Not Reported | One-sentence rationale and up to four current act calls, not an explicit multistep task plan. ([source](https://arxiv.org/pdf/2610.09127v1), §3.3; full-text plan search) |
| workflow | Graph-Structured | Parent-child candidate branches can be revisited; agent operates several candidates per step. ([source](https://arxiv.org/pdf/2610.09127v1), §3.2) |
| update_strategy | Local Patch, Candidate Selection, Rollback | Parameter adjustment, best-result selection and return to earlier valid/root candidates. ([source](https://arxiv.org/pdf/2610.09127v1), §3.2,3.4–5) |
| verifier | Self, Programmatic, Environment | Assistant visual admission; numerical geometry checks; CAD execution outcomes. ([source](https://arxiv.org/pdf/2610.09127v1), §3.5) |
| feedback_assessment | Score, Binary, Diagnosis | IoU/GMS score, validity/acceptance and failure reasons inform next step. ([source](https://arxiv.org/pdf/2610.09127v1), §3.5–6) |
| feedback_observation | Visual, Structural Scene State, Runtime | Renders, geometric scores/operation counts and failed execution reports. ([source](https://arxiv.org/pdf/2610.09127v1), §3.3,3.5) |
| memory_time | Short-Term Memory | Candidate pool and executed-action transcript retained per part. ([source](https://arxiv.org/pdf/2610.09127v1), §3.2–3.3) |
| memory_reach | Global Memory | Shared pool tracks programs, metrics, tool histories used by assistant/executor. ([source](https://arxiv.org/pdf/2610.09127v1), §3.2–3.3) |
| action_type | Tool/Function Call | Function calls act and finish. ([source](https://arxiv.org/pdf/2610.09127v1), §3.3) |
| graphics_software | Agent-Adapted | Common CadQuery DSL and custom tools expose geometry proposals/refinement. ([source](https://arxiv.org/pdf/2610.09127v1), §3.1–3.4) |
| tools | Graphics Operations, Perception models, Solver Validator, Static Validator, Execution Utilities | Algorithmic CAD construction, learned proposal model, parameter solver, validity checks, build/measure orchestration. ([source](https://arxiv.org/pdf/2610.09127v1), §3.4–3.5) |
| resources | Documentation & Rules | Fixed task/tool descriptions, cost and answer format supplied every step. ([source](https://arxiv.org/pdf/2610.09127v1), §3.3) |
| representation | Code, Geometry, Pixels | DSL programs, generated solids/meshes and rendered target/candidates. ([source](https://arxiv.org/pdf/2610.09127v1), §3.1–3.3) |

next_action: "Review/add evidence-grounded record; retain stated taxonomy uncertainties. No survey source mutation authorized."

Events: [{"type": "first_submission", "value": "2026-10-06T21:20:59+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2610.09127", "authority": "primary", "version": "v1", "evidence": "Canonical history; newly completed authorized older backlog, not seven-day catch-up or target event.", "local_value": "2026-10-06T16:20:59-05:00", "prior_event_status": "already_seen"}]
Taxonomy deltas: ["Policy selects actions without explicit multistep plan; do not infer PO-3 from autonomy.", "Shared candidate retention is within-part memory, not cross-run persistence."]

### [Reels-RSI: Program-Level Self-Improvement for Code-Rendered Explainer Videos](https://arxiv.org/abs/2610.14495)
core | High | new_relative_to_snapshot
Application: 2D Graphics, Dynamic / Animation and temporal scene; operations: Generation, Editing, Auditing
Program-level memory makes learned checks retroactively auditable; one new rule found four latent defects in older reels, and rules reduced weak-director violations from 30 to 5.
Scope: Director writes and repairs HTML/SVG animation programs through executable checks; rules learned from edits can audit old graphics programs.
Limits: One model family, small ablation cells, no human preference study. L1 accumulation did not compound; pairwise judge favored second-shown video 62–81%. First evolution has no statistically supported improvement, and preferred scripts dropped thirteen facts. Static checks cannot enforce missing topic facts.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Animation | Time-based explanatory animations synchronized to narration. ([source](https://arxiv.org/pdf/2610.14495v1), §2) |
| input_form | Language, Image | Sentence topics and reviewed geometry problem from photograph. ([source](https://arxiv.org/pdf/2610.14495v1), Table 2; Appendix B) |
| output | Program, Rendered Media | Reel directory includes source animation code and MP4. ([source](https://arxiv.org/pdf/2610.14495v1), §2; Fig.1) |
| model_type | VLM | Reviewed director transcribes and interprets photograph, constructs code. ([source](https://arxiv.org/pdf/2610.14495v1), §5.1; Appendix B) |
| model_training | Off-the-Shelf | Interchangeable existing agent CLIs; improvement in programs rather than model weights. ([source](https://arxiv.org/pdf/2610.14495v1), Abstract; §3) |
| planning | PO-2 | Ten-step handbook; agent creates script and per-frame storyboard with scene/duration/route/status; plan reviewed at gate. ([source](https://arxiv.org/pdf/2610.14495v1), §2–3; §5.1) |
| workflow | Sequential | Script, storyboard, frame construction, finalize/repair and render. ([source](https://arxiv.org/pdf/2610.14495v1), Fig.1; §3–4.1) |
| update_strategy | Local Patch | One-property animation fix and targeted code diffs. ([source](https://arxiv.org/pdf/2610.14495v1), §2; §5.4) |
| verifier | Programmatic, Environment, Human | Static rules, renderer runtime/layout checks and human plan/look-dev/final gates. ([source](https://arxiv.org/pdf/2610.14495v1), §2; §5.1–5.2) |
| feedback_assessment | Diagnosis, Binary | Findings have codes/lines/messages; error severity blocks rendering. ([source](https://arxiv.org/pdf/2610.14495v1), §4.1; Appendix A) |
| feedback_observation | Visual, Structural Scene State, Runtime | Viewer sees rendered frames; checker sees layout/contrast; runtime failures logged. ([source](https://arxiv.org/pdf/2610.14495v1), §2–4.1) |
| memory_time | Short-Term Memory, Long-Term Memory | Per-pass source snapshots; accepted lessons/rules reused on future reels. ([source](https://arxiv.org/pdf/2610.14495v1), §4.1–4.3) |
| memory_reach | Global Memory | Shared ~/.reels store supplies director and future frame-worker briefs. ([source](https://arxiv.org/pdf/2610.14495v1), Fig.1; §4.2) |
| action_type | Code/Script, Tool/Function Call | Director writes frame HTML/SVG/Canvas/Three.js and calls reels CLI. ([source](https://arxiv.org/pdf/2610.14495v1), §2–3) |
| graphics_software | Agent-Adapted | Dedicated agent handbook/CLI wraps browser/GSAP/FFmpeg. ([source](https://arxiv.org/pdf/2610.14495v1), §3) |
| tools | Graphics Operations, Execution Utilities, Static Validator | Render, assemble, fonts, captions, geometry helpers and static rules. ([source](https://arxiv.org/pdf/2610.14495v1), §3–4.1) |
| resources | Assets, Documentation & Rules | Map layers, Commons images, fonts/presets and scoped accepted lessons/handbook. ([source](https://arxiv.org/pdf/2610.14495v1), §3; §4.2) |
| representation | Code, Layouts, Pixels | Source programs, structured frame layouts and rendered pixels. ([source](https://arxiv.org/pdf/2610.14495v1), §2) |

next_action: "Review/add evidence-grounded record; retain stated taxonomy uncertainties. No survey source mutation authorized."

Events: [{"type": "first_submission", "value": "2026-10-10T02:46:44+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2610.14495", "authority": "primary", "version": "v1", "evidence": "Official Atom and canonical v1; Chicago Oct 9. Newly completed frozen pending backlog.", "local_value": "2026-10-09T21:46:44-05:00", "prior_event_status": "already_seen"}]
Taxonomy deltas: ["L3 uses ranking and human-gated candidate playbook selection, excluded from task-time update cells.", "Human feedback applies to reviewed configuration; most headless evaluations use deterministic checks only."]

### [CADForge: Agentic Single-View CAD Reconstruction with Explicit Geometry Reasoning](https://arxiv.org/abs/2610.04262)
core | High | new_relative_to_snapshot
Application: Static / CAD; operations: Reconstruction
Reports 8.35% better CD-L1 than Procedura with 75.4% lower tokens; parameter memory reduces tokens per component from 45,696 to 27,225 with comparable geometry.
Scope: Agents choose component construction plans, synthesize and repair CAD geometry against rendered evidence.
Limits: 200-case evaluation, five human judges and single-view ambiguity. CPVR denominators follow native workflows rather than a fully matched attempt protocol. Extreme side/rear views remain difficult; final CAD validity does not guarantee correct engineering design.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Modeling | Constructs editable CAD model from image. ([source](https://arxiv.org/pdf/2610.04262v1), §3.1) |
| input_form | Image | Single RGB image. ([source](https://arxiv.org/pdf/2610.04262v1), §3.1) |
| output | Program, Graphics Artifact | CadQuery programs plus B-Reps exported STEP/STL/GLB. ([source](https://arxiv.org/pdf/2610.04262v1), §3.1; C.2 p.18) |
| model_type | VLM | Same GPT-5.5 backbone used as visual agents and text-only code agent. ([source](https://arxiv.org/pdf/2610.04262v1), §4.1; G.4) |
| model_training | Off-the-Shelf | Training-free without specialized fine-tuning. ([source](https://arxiv.org/pdf/2610.04262v1), §2 pp.2–3) |
| planning | PO-2 | Ordered component inventory follows dependency-aware CAD construction blueprint. ([source](https://arxiv.org/pdf/2610.04262v1), §3.2; G.1) |
| workflow | Graph-Structured | Review selects geometry, modeling or mixed-error branch. ([source](https://arxiv.org/pdf/2610.04262v1), §3.4; G.6) |
| update_strategy | Regeneration, Local Patch, Rollback | Complete replacement observation/code on review; smallest technical code repair; safe_fillet returns original solid on failure. ([source](https://arxiv.org/pdf/2610.04262v1), G.2–G.5; C.3) |
| verifier | Critic, Programmatic, Environment | Distinct review agent, static validity and execution checks. ([source](https://arxiv.org/pdf/2610.04262v1), §3.4; G.5–G.6) |
| feedback_assessment | Binary, Diagnosis | pass/error type with one-to-three corrective sentences. ([source](https://arxiv.org/pdf/2610.04262v1), G.6 p.32) |
| feedback_observation | Visual, Runtime | Two renders alongside reference; execution/static-validation error messages. ([source](https://arxiv.org/pdf/2610.04262v1), C.2 p.18; G.5) |
| memory_time | Short-Term Memory | Nested dictionary retains accepted component parameters through run. ([source](https://arxiv.org/pdf/2610.04262v1), §3.5) |
| memory_reach | Global Memory | Geometry and code stages retrieve same component dictionary. ([source](https://arxiv.org/pdf/2610.04262v1), §3.5) |
| action_type | Code/Script | Python solvers and complete component CadQuery scripts. ([source](https://arxiv.org/pdf/2610.04262v1), G.3–G.5) |
| graphics_software | Agent-Adapted | Custom ten-helper API manifest and wrapped CadQuery execution namespace. ([source](https://arxiv.org/pdf/2610.04262v1), C.3 pp.18–19) |
| tools | Graphics Operations, Execution Utilities, Static Validator | Geometric math helpers, CadQuery operations, renderer, execution and validity checker. ([source](https://arxiv.org/pdf/2610.04262v1), §3.3–3.4; C.2–3) |
| resources | Documentation & Rules, Examples & Trajectories | API manifest contains signatures, functionality, concise usage examples and selection guidance. ([source](https://arxiv.org/pdf/2610.04262v1), C.3 pp.18–19) |
| representation | Code, Geometry, Pixels | Programs, B-Reps and review renders. ([source](https://arxiv.org/pdf/2610.04262v1), §3.1; C.2) |

next_action: "Review/add evidence-grounded record; retain stated taxonomy uncertainties. No survey source mutation authorized."

Events: [{"type": "first_submission", "value": "2026-10-03T03:39:54+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2610.04262", "authority": "primary", "version": "v1", "evidence": "Canonical history; Chicago Oct 2. Newly completed authorized backlog, not target-day discovery.", "local_value": "2026-10-02T22:39:54-05:00", "prior_event_status": "already_seen"}]
Taxonomy deltas: ["Task-time memory distinct from offline helper construction.", "Math parameter-solving utilities are not automatically Solver Validator under the state-exploration definition."]

### [DyCraft: An Agentic System for Long-Horizon 4D Scene Generation](https://arxiv.org/abs/2610.40754)
core | High | new_relative_to_snapshot
Application: Dynamic / Animation and temporal scene, Dynamic / Physical simulation and effects; operations: Generation
On 24 minute-scale animation tasks, lowers penetration from 80.1% to 13.0% and floating from 15.7% to 2.7% versus bare agent; 72.3% human preference.
Scope: Coding agent authors and repairs explicit animated Blender scene state using per-frame numerical validators and visual inspection.
Limits: Residual contact/character errors remain; validation is geometric rather than a universal physical proof. Only 24 prompts, same proprietary model and mainly qualitative ablations. Per-task preferences sometimes favor the baseline, especially mechanisms. No dedicated limitations section.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Animation, Simulation | Authored character motion and baked fluid/rigid-body dynamics. ([source](https://arxiv.org/pdf/2610.40754v1), §3.3; Fig.5) |
| input_form | Language, 3D Representation | Text task; robot tasks explicitly supply G1 articulated asset to reuse. ([source](https://arxiv.org/pdf/2610.40754v1), §3.1; Appendix C.2) |
| output | Program, Graphics Artifact, Rendered Media | Entirely code-based generation delivers editable Blender project and final film. ([source](https://arxiv.org/pdf/2610.40754v1), §3.1; Fig.1) |
| model_type | VLM | GPT-6-Astra views rendered frame grids and writes code. ([source](https://arxiv.org/pdf/2610.40754v1), §3.3 Visual Inspection; §4) |
| model_training | Off-the-Shelf | Extends existing Codex with system prompt/operations; same underlying GPT-6-Astra for all comparisons. ([source](https://arxiv.org/pdf/2610.40754v1), §3.1; §4 p.7) |
| planning | PO-2 | Agent plans full action/shot sequence from two rewritten briefs; required storyboard verification stages. ([source](https://arxiv.org/pdf/2610.40754v1), §3.2–3.3) |
| workflow | Graph-Structured, Parallel | Can delegate object/scene/motion tasks in parallel; main agent integrates contributions. ([source](https://arxiv.org/pdf/2610.40754v1), §3.3 Delegation p.6) |
| update_strategy | Local Patch | Locally revise layout, pose, camera and connecting motion before rendering. ([source](https://arxiv.org/pdf/2610.40754v1), Fig.3; §3.3) |
| verifier | Self, Programmatic | Author visually inspects frames and numerical verifiers check geometry. ([source](https://arxiv.org/pdf/2610.40754v1), §3.3–3.4) |
| feedback_assessment | Binary, Diagnosis | Pass/fail gates with penetration depth and separating-axis diagnostics. ([source](https://arxiv.org/pdf/2610.40754v1), §3.4) |
| feedback_observation | Visual, Structural Scene State | Rendered views and per-frame collisions/support/joint limits. ([source](https://arxiv.org/pdf/2610.40754v1), §3.3–3.4) |
| memory_time | Short-Term Memory | scene.txt, motion.txt, persistent project and verified storyboard used later. ([source](https://arxiv.org/pdf/2610.40754v1), §3.2–3.3) |
| memory_reach | Global Memory | Main integrates subagent contributions into common film state. ([source](https://arxiv.org/pdf/2610.40754v1), §3.3 Delegation) |
| action_type | Code/Script, Tool/Function Call | Native file editing, shell/Python and custom harness operations. ([source](https://arxiv.org/pdf/2610.40754v1), §3.1) |
| graphics_software | Agent-Adapted | Custom build123d parts/joints/pose interface and Blender motion/check helpers. ([source](https://arxiv.org/pdf/2610.40754v1), §3.2 p.5) |
| tools | Execution Utilities, Graphics Operations, Solver Validator, Static Validator | File/shell execution; CAD/render authoring; IK and simulation; collision/support checks. ([source](https://arxiv.org/pdf/2610.40754v1), §3.1–3.4) |
| resources | Assets, Examples & Trajectories, Documentation & Rules | Rigged character library; CMU and dog motion capture; staged skills/API instructions. ([source](https://arxiv.org/pdf/2610.40754v1), Appendix A.1–A.2 pp.17–19) |
| representation | Code, Geometry, Dynamic State, Pixels | Python/CAD code, meshes/rigs, motion/simulation states and rendered images. ([source](https://arxiv.org/pdf/2610.40754v1), §3) |

next_action: "Review/add evidence-grounded record; retain stated taxonomy uncertainties. No survey source mutation authorized."

Events: [{"type": "first_submission", "value": "2026-10-29T16:42:04+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2610.40754", "authority": "primary", "version": "v1", "evidence": "Canonical history; Chicago Oct 29 11:42:04, seven-day catch-up.", "local_value": "2026-10-29T11:42:04-05:00", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: ["Parallel denotes supported delegation, not a measured per-run schedule.", "Memory inferred from explicit files and shared project, not agent brand."]

### [GREP: Grounding Generated Room Evaluation in Principles](https://arxiv.org/abs/2611.05802)
core | High | new_relative_to_snapshot
Application: Static / Scene, Datasets and Benchmarks; operations: Auditing
Evidence-adaptive room audit agrees with 13/15 human pair preferences; reports enable targeted revisions in a separate five-scene refinement study.
Scope: Evaluation agent actively selects and changes cameras in a 3D graphics environment to audit scene-specific defects; auditing is explicitly in scope even without changing object geometry.
Limits: Fifteen pairs come from only six scenes and are not independent. Single-judge bias, incomplete discovered-check coverage, forced binary verdicts and default-valid outcomes remain. Repeatability can obscure mean differences below four points; refinement uses a different scoring protocol.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Not Applicable | Audits fixed scenes; no artifact Modeling, Animation, Simulation or visual communication task. ([source](https://arxiv.org/pdf/2611.05802v1), §3) |
| input_form | 3D Representation, Language | Asset geometry, transforms, boundaries and intended room-use context. ([source](https://arxiv.org/pdf/2611.05802v1), §3; A.1) |
| output | Not Applicable | Scores and inspection reports, not graphics content or declarative specification of desired content. ([source](https://arxiv.org/pdf/2611.05802v1), §3.4) |
| model_type | VLM | GPT-5.6 Sol visual evaluator. ([source](https://arxiv.org/pdf/2611.05802v1), §4.1; C.3) |
| model_training | Not Reported | Judge identity and configuration reported but no explicit adaptation/frozen status; training matches only future work and references. ([source](https://arxiv.org/pdf/2611.05802v1), C.3; full-text searches) |
| planning | PO-2 | Scene-specific checks fix targets and required observations within fixed vocabulary. ([source](https://arxiv.org/pdf/2611.05802v1), A.2–A.3) |
| workflow | Graph-Structured | Metric-specific branches, conclusive early exits and evidence-request loops. ([source](https://arxiv.org/pdf/2611.05802v1), Fig.7; Table 4) |
| update_strategy | Candidate Selection, Local Patch | Select feasible camera candidates; up to three VLM camera repair proposals. ([source](https://arxiv.org/pdf/2611.05802v1), A.4; Table 7) |
| verifier | Critic, Programmatic | Metric evaluator judges evidence sufficiency, distinct from camera selector; deterministic gate validates decodable nonblank views. ([source](https://arxiv.org/pdf/2611.05802v1), A.3–A.4) |
| feedback_assessment | Binary, Diagnosis | Sufficient/insufficient evidence and unmet observation requirements guide additional acquisition. ([source](https://arxiv.org/pdf/2611.05802v1), A.3–A.5) |
| feedback_observation | Visual, Structural Scene State | Views plus distance, angle, clearance measurements. ([source](https://arxiv.org/pdf/2611.05802v1), §3.3; A.3) |
| memory_time | Short-Term Memory | Acquired views retained for later checks in same scope. ([source](https://arxiv.org/pdf/2611.05802v1), §3.3; A.3) |
| memory_reach | Local Memory | Function group shares evidence bank; others keep own scopes. ([source](https://arxiv.org/pdf/2611.05802v1), Table 4; A.3) |
| action_type | Tool/Function Call | Measure, retrieve-view and render-new-view operations. ([source](https://arxiv.org/pdf/2611.05802v1), §3.3) |
| graphics_software | Agent-Adapted | Custom camera/measurement interface around Blender EEVEE. ([source](https://arxiv.org/pdf/2611.05802v1), C.3) |
| tools | Graphics Operations, Static Validator | Rendering/camera operations and geometric validity/visibility screening. ([source](https://arxiv.org/pdf/2611.05802v1), §3.3; A.1–A.4) |
| resources | Documentation & Rules | Fixed check types, evidence requirements and severity rules; catalog-side affordance references. ([source](https://arxiv.org/pdf/2611.05802v1), A.2–A.3; B) |
| representation | Geometry, Pixels | Explicit geometry/transforms and rendered views. ([source](https://arxiv.org/pdf/2611.05802v1), §3; A.3) |

next_action: "Review/add evidence-grounded record; retain stated taxonomy uncertainties. No survey source mutation authorized."

Events: [{"type": "first_submission", "value": "2026-11-04T01:19:12+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2611.05802", "authority": "primary", "version": "v1", "evidence": "Canonical v1; Chicago Nov 3 19:19:12, seven-day catch-up.", "local_value": "2026-11-03T19:19:12-06:00", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: ["Auditing lacks a direct task/output label; preserve Not Applicable rather than relabel reports as graphics specifications.", "Final scene scores distinguished from internal evidence-sufficiency feedback."]

### [Parametric CAD Bench v3: Evaluating Agentic Parametric CAD Authoring from Text and Engineering Drawings](https://arxiv.org/abs/2611.02659)
core | High | new_relative_to_snapshot
Application: Static / CAD, Datasets and Benchmarks; operations: Generation, Editing, Reconstruction
Native feature-tree and dimension-sensitive evaluation across 100 tasks; best overall point estimate 61.03% mean reward, not success rate. Create-and-edit remains hardest.
Scope: Benchmark directly evaluates agent-executed FreeCAD authoring, not one-shot geometry predictions alone.
Limits: Single final trial per system/task, small curated suite, potential contamination and platform differences. Geometry and spec checks do not certify design intent, editability or manufacturing. Valid alternate topology may be penalized. Internal agent mechanisms incompletely reported.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Modeling | Native parametric mechanical CAD authoring. ([source](https://arxiv.org/pdf/2611.02659v1), §3.1) |
| input_form | Language, Image | Text description/edit instructions or engineering drawing. ([source](https://arxiv.org/pdf/2611.02659v1), Table 1) |
| output | Program, Graphics Artifact | answer.py and native FCStd files required. ([source](https://arxiv.org/pdf/2611.02659v1), Appendix B p.19; C p.24) |
| model_type | VLM | Opus 5.5 receives actual image content via base64 bridge, not text-only image paths. ([source](https://arxiv.org/pdf/2611.02659v1), §5.2) |
| model_training | Not Reported | Model/agent version specified, providers' training undisclosed; no fine-tuning statement. ([source](https://arxiv.org/pdf/2611.02659v1), §5.2,6; full PDF searches) |
| planning | Not Reported | No explicit task plan or planning degree described. ([source](https://arxiv.org/pdf/2611.02659v1), §4–5, Appendix A; search planning) |
| workflow | Not Reported | Image ingestion requirement and job versions reported; internal scheduling not specified. ([source](https://arxiv.org/pdf/2611.02659v1), §5.2, Appendix A) |
| update_strategy | Not Reported | Two saved edit artifacts do not prove reuse of base; no repair strategy described. ([source](https://arxiv.org/pdf/2611.02659v1), §3.1,6; full-text repair search) |
| verifier | Not Reported | Separate verifier measures submitted artifacts; no task-time verifier interaction established. ([source](https://arxiv.org/pdf/2611.02659v1), §4.1–4.2) |
| feedback_assessment | Not Reported | Continuous reward is final held-out score, not a feedback signal delivered to agent. ([source](https://arxiv.org/pdf/2611.02659v1), §4.2; search feedback) |
| feedback_observation | Not Reported | Input drawing transport described; subsequent evidence used to revise actions not documented. ([source](https://arxiv.org/pdf/2611.02659v1), §5.2) |
| memory_time | Not Reported | Logs exist but no retained-state memory mechanism described. ([source](https://arxiv.org/pdf/2611.02659v1), §4–6, Appendix A; memory search) |
| memory_reach | Not Reported | No access/reach architecture described. ([source](https://arxiv.org/pdf/2611.02659v1), §4–6, Appendix A; memory search) |
| action_type | Code/Script | Write executable FreeCAD Python script. ([source](https://arxiv.org/pdf/2611.02659v1), Appendices B–C) |
| graphics_software | General-Purpose | Native FreeCAD Python API; sandbox pins 1.1.0. ([source](https://arxiv.org/pdf/2611.02659v1), §1,4.1; Appendix B) |
| tools | Graphics Operations, Execution Utilities | Shell bridge and FreeCAD execution/modeling API. ([source](https://arxiv.org/pdf/2611.02659v1), §5.2; Appendix B) |
| resources | Documentation & Rules | System image-inspection rule and common artifact/feature-tree contract. ([source](https://arxiv.org/pdf/2611.02659v1), §5.2, Appendix B) |
| representation | Code, Geometry, Pixels | Python scripts, native feature/B-Rep geometry and engineering drawing pixels. ([source](https://arxiv.org/pdf/2611.02659v1), §1,3; Appendix B) |

next_action: "Review/add evidence-grounded record; retain stated taxonomy uncertainties. No survey source mutation authorized."

Events: [{"type": "first_submission", "value": "2026-11-02T07:19:55+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2611.02659", "authority": "primary", "version": "v1", "evidence": "Canonical v1 submission; Chicago Nov 2 01:19:55. September leaderboard snapshot is not paper submission date.", "local_value": "2026-11-02T01:19:55-06:00", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: ["Benchmark final verifier excluded from task-time feedback cells.", "Create-and-edit operation retained as task definition while patch/reuse strategy stays unreported."]

### [SketchDirector: Complex Scene Sketching via Agentic Layout Reasoning and Detail Refinement](https://arxiv.org/abs/2610.41260)
core | High | new_relative_to_snapshot
Application: 2D Graphics; operations: Generation, Editing
Editable six-action layout interface and scoped failure/experience memory; 30-prompt evaluation and 68-person preference study support improved composition.
Scope: Agent explicitly moves, rescales, rotates, relayers, deletes and regenerates editable vector objects from feedback.
Limits: Complex interactions remain difficult; downstream refinement can duplicate objects. Roughly six minutes per sketch and 21 with refinement. Model adaptation and several verification thresholds are not fully specified; 64×64 cells at 12 pixels conflicts with claimed 780-pixel canvas resolution.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Modeling | Constructs multi-object scene sketches with explicit editable object geometry. ([source](https://arxiv.org/pdf/2610.41260v1), §3 p.3) |
| input_form | Language | Scene textual description T; object drafts generated internally. ([source](https://arxiv.org/pdf/2610.41260v1), §3.1) |
| output | Program, Graphics Artifact | Independent SVG assets and executable layouts enable subsequent editing. ([source](https://arxiv.org/pdf/2610.41260v1), §4.1 p.6) |
| model_type | VLM | GPT-5.5 reasons jointly over geometry, rendered canvas and layout history. ([source](https://arxiv.org/pdf/2610.41260v1), §3.3 p.4; §4.1) |
| model_training | Not Reported | Default backbone and rendering optimization given, but no adaptation status; training mentions are related work. ([source](https://arxiv.org/pdf/2610.41260v1), §4.1; full-text training search) |
| planning | PO-2 | Model predicts action program inside fixed Plan–Execute–Verify–Correct cycle. ([source](https://arxiv.org/pdf/2610.41260v1), §3.3) |
| workflow | Sequential | Operations sequentially executed and verification follows. ([source](https://arxiv.org/pdf/2610.41260v1), §3.3 p.4) |
| update_strategy | Local Patch, Replanning, Regeneration | move/scale/layer update existing state; modify regenerates object; memory informs revised action plan. ([source](https://arxiv.org/pdf/2610.41260v1), §3.2–3.3) |
| verifier | Critic, Programmatic | Boundary/size checks and explicitly VLM critic with canvas/collage. ([source](https://arxiv.org/pdf/2610.41260v1), §3.3 pp.4–5) |
| feedback_assessment | Binary, Score, Diagnosis | Weighted five-aspect score, conjunction pass/fail and violation/failure analysis guide next plan. ([source](https://arxiv.org/pdf/2610.41260v1), Eqs.1–2; Fig.4) |
| feedback_observation | Visual, Structural Scene State | Bounding boxes/scales and rendered canvas/object collage. ([source](https://arxiv.org/pdf/2610.41260v1), §3.3) |
| memory_time | Short-Term Memory, Long-Term Memory | Failure records discarded after current scene succeeds; successful cross-scene experiences persist. ([source](https://arxiv.org/pdf/2610.41260v1), §3.3 pp.5–6) |
| memory_reach | Local Memory | Retrieved experience and failure feedback provided to layout planner. ([source](https://arxiv.org/pdf/2610.41260v1), §3.3 p.6) |
| action_type | Code/Script, Tool/Function Call | Executable programs composed of six functional tools. ([source](https://arxiv.org/pdf/2610.41260v1), §3.2–3.3) |
| graphics_software | Agent-Adapted | Custom six-operation canvas wrapper with pydiffvg rendering. ([source](https://arxiv.org/pdf/2610.41260v1), §3.2; §4.1) |
| tools | Graphics Operations, Static Validator, Perception models | Canvas transforms/rendering, geometric checks and SketchAgent object regeneration. ([source](https://arxiv.org/pdf/2610.41260v1), §3.1–3.3) |
| resources | Examples & Trajectories | Retrieves prior successful scene experiences via object-set Jaccard similarity. ([source](https://arxiv.org/pdf/2610.41260v1), §3.3 Eq.3) |
| representation | Code, Layouts, Pixels | Action programs, object SVG canvas layouts and rendered scenes. ([source](https://arxiv.org/pdf/2610.41260v1), §3; Figs.3–5) |

next_action: "Review/add evidence-grounded record; retain stated taxonomy uncertainties. No survey source mutation authorized."

Events: [{"type": "first_submission", "value": "2026-10-30T05:05:12+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2610.41260", "authority": "primary", "version": "v1", "evidence": "Canonical history; Chicago Oct 30 00:05:12, seven-day catch-up.", "local_value": "2026-10-30T00:05:12-05:00", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: ["Modeling versus Visualization remains coarse for scene sketches; choose content construction purpose.", "Do not merge diffusion refinement gradients into controller model_training."]

### [CounterSketch: Physics-Grounded Counterfactual Reasoning for Sketch-to-Video Generation](https://arxiv.org/abs/2611.04244)
core | Medium | new_relative_to_snapshot
Application: 2D Graphics, Dynamic / Animation and temporal scene; operations: Generation, Editing
80-question benchmark; physics-grounded rollout improves T2V alignment from 0.1729 to 0.2011 versus direct VLM trajectories under same downstream renderer.
Scope: VLM causal reasoning chooses interventions and event-chain updates on vector scene state; verifier failures cause semantic replanning before animation synthesis.
Limits: Ambiguous sketch grounding and latent physical parameters limit fidelity. Only 20 base scenes; no quantitative physical violation or repair-count reporting. Controller backbone and training omitted; numerical/semantic acceptance thresholds and implementation details underspecified.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Animation | Transforms static sketches into counterfactual animations. ([source](https://arxiv.org/pdf/2611.04244v1), §3) |
| input_form | Image, Language | Sketch image and What-if prompt. ([source](https://arxiv.org/pdf/2611.04244v1), §3 Eq.1) |
| output | Rendered Media | Final sketch video Vcf. ([source](https://arxiv.org/pdf/2611.04244v1), §3 Eq.3) |
| model_type | VLM | VLM scene grounding and causal reasoning. ([source](https://arxiv.org/pdf/2611.04244v1), §4.1; Fig.4) |
| model_training | Not Reported | No controller adaptation details; Gemini 3.8 Flash named specifically for baselines, not clearly own controller. ([source](https://arxiv.org/pdf/2611.04244v1), §4–5; full-text searches) |
| planning | PO-2 | VLM generates ordered events with affected objects, conditions and updated graph; fixed five-stage scaffold. ([source](https://arxiv.org/pdf/2611.04244v1), §4.2 Eq.5) |
| workflow | Graph-Structured | Violations route to numerical repair or semantic replan and re-rollout. ([source](https://arxiv.org/pdf/2611.04244v1), Fig.5; §4.4) |
| update_strategy | Local Patch, Replanning | Adjust initial state/constraints locally or refine semantic event chain. ([source](https://arxiv.org/pdf/2611.04244v1), §4.4) |
| verifier | Programmatic | Checks trajectories against physical/geometric constraints and accepts only reduced violations. ([source](https://arxiv.org/pdf/2611.04244v1), §4.4) |
| feedback_assessment | Binary, Diagnosis | Per-constraint violation reports and acceptance test determine repair route. ([source](https://arxiv.org/pdf/2611.04244v1), §4.4; Fig.5) |
| feedback_observation | Structural Scene State | Contact gaps, constraints, trajectories and semantic intervention state. ([source](https://arxiv.org/pdf/2611.04244v1), §4.3–4.4) |
| memory_time | Short-Term Memory | Updated scene graph and active event constraints carried forward and repaired locally. ([source](https://arxiv.org/pdf/2611.04244v1), §4.2–4.4) |
| memory_reach | Global Memory | First four stages operate on common explicit physical scene representation. ([source](https://arxiv.org/pdf/2611.04244v1), §4 overview) |
| action_type | Structured Specification | Reasoner emits intervention and event/constraint records, not executable script. ([source](https://arxiv.org/pdf/2611.04244v1), §4.2 Eq.5) |
| graphics_software | Agent-Adapted | Verified dynamics projected to bounding-box controls for MoSketch. ([source](https://arxiv.org/pdf/2611.04244v1), §4.5; §5.2) |
| tools | Solver Validator, Static Validator, Graphics Operations | KKT constrained rollout, violation checks, vector intervention and trajectory projection. ([source](https://arxiv.org/pdf/2611.04244v1), §4.3–4.5) |
| resources | Not Reported | No reusable retrieved examples, assets or documentation resource described. ([source](https://arxiv.org/pdf/2611.04244v1), Entire 11-page paper; searches memory/API/documentation) |
| representation | Layouts, Dynamic State, Pixels | Vector objects and bounding boxes, dynamic trajectories, final video pixels. ([source](https://arxiv.org/pdf/2611.04244v1), §4) |

next_action: "Review/add evidence-grounded record; retain stated taxonomy uncertainties. No survey source mutation authorized."

Events: [{"type": "first_submission", "value": "2026-11-03T03:27:35+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2611.04244", "authority": "primary", "version": "v1", "evidence": "Canonical history; Chicago Nov 2 21:27:35, catch-up.", "local_value": "2026-11-02T21:27:35-06:00", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: ["Core based on explicit VLM decisions modifying vector state and semantic replanning, not merely constrained optimization.", "Simulation is means to sketch animation; no separate Simulation task label."]

### [AgiWorld: An Agentic Video World Model for Building Persistent Worlds](https://arxiv.org/abs/2611.02341)
core | High | new_relative_to_snapshot
Application: Dynamic / Animation and temporal scene; operations: Generation
Couples semantic world planning to reliable geometric video memory; WM reduces World Explore translation error from 1.32m to 1.05m and FID from 42.73 to 35.37 versus strongest baseline; agent benefits shown qualitatively.
Scope: Agent controls video-world camera trajectories/content prompts and explicitly rolls back, regenerates and replans after geometric/visual failures.
Limits: Agent evaluation mainly qualitative two-example ablations; quantitative metrics predominantly test WM alone. Paths accepted after three failed repairs and repeated faults eventually only reported. Static scenes only; internal collection limits reproducibility. No dedicated limitations section.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Animation | Builds continuous long video journey through generated world. ([source](https://arxiv.org/pdf/2611.02341v1), §2.1) |
| input_form | Image, Language | Initial image and free-form instruction. ([source](https://arxiv.org/pdf/2611.02341v1), §2.1) |
| output | Rendered Media | Output explicitly defined as long video; world state is retained internal control. ([source](https://arxiv.org/pdf/2611.02341v1), §2.1) |
| model_type | VLM | One multimodal language model performs both director and update, GPT-6-Astra. ([source](https://arxiv.org/pdf/2611.02341v1), A.1 p.19) |
| model_training | Not Reported | Guidelines and schemas specified for controller; no explicit fine-tuning/frozen controller statement. Training described only for Wan-based WM. ([source](https://arxiv.org/pdf/2611.02341v1), A.1; §5; targeted searches) |
| planning | PO-2 | Ordered journey stages and 60-second waypoint plan within fixed triggers/checks. ([source](https://arxiv.org/pdf/2611.02341v1), §3.1–3.3; A.4) |
| workflow | Graph-Structured | Conditional regeneration, revision, refresh and replan branches. ([source](https://arxiv.org/pdf/2611.02341v1), Algorithm 1 p.22) |
| update_strategy | Local Patch, Regeneration, Replanning, Rollback | Small state edits; chunk regenerated with new seed; route redesigned; prior memory/world state restored before retry. ([source](https://arxiv.org/pdf/2611.02341v1), A.6–A.7) |
| verifier | Self, Programmatic | Same director reviews content; deterministic tools check schema, path bounds and generated geometry. ([source](https://arxiv.org/pdf/2611.02341v1), §3.3; A.1,A.6) |
| feedback_assessment | Binary, Diagnosis | Present/absent/different and ok/minor/major diagnoses; threshold pass/fail triggers retry. ([source](https://arxiv.org/pdf/2611.02341v1), A.6 p.23) |
| feedback_observation | Visual, Structural Scene State | Frames, projected layout, point-cloud floorplan and camera clearance/height. ([source](https://arxiv.org/pdf/2611.02341v1), Table 5 p.24) |
| memory_time | Short-Term Memory | All generated chunks, geometry and retired elements persist for current rollout. ([source](https://arxiv.org/pdf/2611.02341v1), §2.2,3.4) |
| memory_reach | Global Memory | Shared spatial memory read by WM and agent; world state serves director/update. ([source](https://arxiv.org/pdf/2611.02341v1), §2.2; Fig.2) |
| action_type | Structured Specification | JSON layouts, waypoints, stage records and structured prompts interpreted by tools. ([source](https://arxiv.org/pdf/2611.02341v1), A.1; Tables 3–4) |
| graphics_software | Agent-Ready | Agent and WM co-designed around metric control and shared structured state. ([source](https://arxiv.org/pdf/2611.02341v1), §2.2; §3.2) |
| tools | Graphics Operations, Static Validator, Perception models | Project/render world geometry and interpolate paths; schema/clearance validators; learned depth and video generator. ([source](https://arxiv.org/pdf/2611.02341v1), §3.2; Table 5) |
| resources | Documentation & Rules | Shared WM capability/practice specification and step guidelines. ([source](https://arxiv.org/pdf/2611.02341v1), A.4 Table 6) |
| representation | Geometry, Dynamic State, Pixels, Learned State | Point clouds/coarse world geometry, time-indexed camera states, generated pixels and retained WM latents. ([source](https://arxiv.org/pdf/2611.02341v1), §2–4) |

next_action: "Review/add evidence-grounded record; retain stated taxonomy uncertainties. No survey source mutation authorized."

Events: [{"type": "first_submission", "value": "2026-11-02T00:39:40+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2611.02341", "authority": "primary", "version": "v1", "evidence": "Official Atom published; canonical v1 date. Chicago Nov 1 18:39:40, catch-up.", "local_value": "2026-11-01T18:39:40-06:00", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: ["Within-rollout spatial memory is Short-Term Memory, not Long-Term Memory merely due minute-scale duration.", "Video-model adaptation excluded from decision-model training cell."]

### [LongBanana: An Expert-Verified Benchmark for Long-Context Multi-Reference Image Synthesis](https://arxiv.org/abs/2611.06856)
core | High | new_relative_to_snapshot
Application: 2D Graphics, Datasets and Benchmarks; operations: Generation, Editing
Expert-audited long-context image benchmark; OpenClaw+RPR scores 78.4 versus 76.1 minimal and 74.6 privileged graph-direct baseline; 47.8% weighted task pass rate.
Scope: RPR controller chooses visual references, schedules image generator calls and revises prompts from inspected drafts, directly changing generated images.
Limits: RPR gains depend on harness and may induce drift; not compute-matched and runtime/API cost absent. Figure captions retain pending identifiers despite C.1 model declarations. Release claims conflict with checklist noting missing public executable instructions. 90 cases exclude 3D/video.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Modeling | Constructs image composition from entities, appearances and relations. ([source](https://arxiv.org/pdf/2611.06856v1), §2.1; Fig.1) |
| input_form | Image, Language | Approximately 32 reference images and synthesis instruction. ([source](https://arxiv.org/pdf/2611.06856v1), §2.1) |
| output | Rendered Media | One coherent synthesized final image. ([source](https://arxiv.org/pdf/2611.06856v1), §2.1; Fig.18) |
| model_type | VLM | Sonnet 4.6 observes references and reviews visual drafts. ([source](https://arxiv.org/pdf/2611.06856v1), C.1; Fig.18) |
| model_training | Not Reported | Shared agent backbone/version reported; no adaptation/frozen-agent statement. Image backend fixed. ([source](https://arxiv.org/pdf/2611.06856v1), C.1; full-text searches) |
| planning | PO-2 | Agent decomposes into subgoals and builds scene plan/prompt schedule inside RPR sequence. ([source](https://arxiv.org/pdf/2611.06856v1), D.2 Fig.18) |
| workflow | Sequential | RPR described as serial ReAct–Plan–Exec–Reflect workflow. ([source](https://arxiv.org/pdf/2611.06856v1), §1 p.3) |
| update_strategy | Local Patch, Replanning | Target unmet bindings with image edits; feedback adjusts execution schedule/retrieves new evidence. ([source](https://arxiv.org/pdf/2611.06856v1), D.2; §4.3) |
| verifier | Self | Agent-directed draft review in Reflect. ([source](https://arxiv.org/pdf/2611.06856v1), §4.1; Fig.18) |
| feedback_assessment | Diagnosis | Identifies missing content and wrong bindings for prompt repair. ([source](https://arxiv.org/pdf/2611.06856v1), Fig.18) |
| feedback_observation | Visual | Inspects draft and reference images before revisions. ([source](https://arxiv.org/pdf/2611.06856v1), §4.1) |
| memory_time | Short-Term Memory | Harness maintains reference state and records revisions throughout synthesis. ([source](https://arxiv.org/pdf/2611.06856v1), §1 p.3; Fig.18) |
| memory_reach | Global Memory | Shared agent state connects grounding, execution and reflection. ([source](https://arxiv.org/pdf/2611.06856v1), Fig.18) |
| action_type | Tool/Function Call | Harness calls reference browsing, image generation and file/prompt management tools. ([source](https://arxiv.org/pdf/2611.06856v1), C.1) |
| graphics_software | Agent-Adapted | RPR harness wraps existing fixed image generator with state/prompt control. ([source](https://arxiv.org/pdf/2611.06856v1), §1; C.1) |
| tools | Perception models, Execution Utilities, Static Validator | Generation harness explicitly calls image backend, OCR/count/layout and file/prompt tools. ([source](https://arxiv.org/pdf/2611.06856v1), C.1 p.33) |
| resources | Assets | Agent retrieves selected references from provided visual inventory. ([source](https://arxiv.org/pdf/2611.06856v1), §4.1; Fig.18) |
| representation | Pixels | References and intermediate/final raster composites; semantic plan not an editable geometry/layout artifact. ([source](https://arxiv.org/pdf/2611.06856v1), §4.1; D.2) |

next_action: "Review/add evidence-grounded record; retain stated taxonomy uncertainties. No survey source mutation authorized."

Events: [{"type": "first_submission", "value": "2026-11-04T18:11:56+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2611.06856", "authority": "primary", "version": "v1", "evidence": "Official Atom published and canonical v1; Chicago Nov 4 12:11:56.", "local_value": "2026-11-04T12:11:56-06:00", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: ["Final agentic checklist judge is a distinct subsystem; its Score/Critic feedback labels are not transferred to generation loop.", "Source task mapping Modeling is coarse for mixed raster composition; preserves purpose rather than equating images with Visualization."]

## date_unresolved (0)

## unresolved (0)

## excluded (0)

## Application index
| Application | Papers |
|---|---|
| 2D Graphics | [ManimCode: Learning Visual Self-Correction for Educational Animation](https://arxiv.org/abs/2611.08294) [same_day_new]; [DreamRealm: Exploring and Materializing Hallucination Worlds for Trustworthy Vision-Language Models](https://arxiv.org/abs/2611.06433) [same_day_updates]; [EvoDesign: Agentic Editable Diagram Creation via Design Expertise Evolution](https://arxiv.org/abs/2604.09568) [same_day_updates]; [Reels-RSI: Program-Level Self-Improvement for Code-Rendered Explainer Videos](https://arxiv.org/abs/2610.14495) [late_discovery]; [SketchDirector: Complex Scene Sketching via Agentic Layout Reasoning and Detail Refinement](https://arxiv.org/abs/2610.41260) [late_discovery]; [CounterSketch: Physics-Grounded Counterfactual Reasoning for Sketch-to-Video Generation](https://arxiv.org/abs/2611.04244) [late_discovery]; [LongBanana: An Expert-Verified Benchmark for Long-Context Multi-Reference Image Synthesis](https://arxiv.org/abs/2611.06856) [late_discovery] |
| Static / Object | None verified in this run |
| Static / CAD | [CADFather: Autonomous CAD Reconstruction through Coordinated Tool Use](https://arxiv.org/abs/2610.09127) [late_discovery]; [CADForge: Agentic Single-View CAD Reconstruction with Explicit Geometry Reasoning](https://arxiv.org/abs/2610.04262) [late_discovery]; [Parametric CAD Bench v3: Evaluating Agentic Parametric CAD Authoring from Text and Engineering Drawings](https://arxiv.org/abs/2611.02659) [late_discovery] |
| Static / Scene | [Deformable Contact-Aware 3D Object Placement](https://arxiv.org/abs/2611.08005) [same_day_new]; [NeoWorld-Pro: Programming Interactive Scenes from Monocular Images for Embodied Simulation](https://arxiv.org/abs/2608.24212) [same_day_updates]; [WorldAct: Activating Monolithic 3D Worlds into Interactive-Ready Object-Centric Scenes](https://arxiv.org/abs/2605.15843) [same_day_updates]; [GREP: Grounding Generated Room Evaluation in Principles](https://arxiv.org/abs/2611.05802) [late_discovery] |
| Dynamic / Articulated assets | [NeoWorld-Pro: Programming Interactive Scenes from Monocular Images for Embodied Simulation](https://arxiv.org/abs/2608.24212) [same_day_updates] |
| Dynamic / Animation and temporal scene | [ManimCode: Learning Visual Self-Correction for Educational Animation](https://arxiv.org/abs/2611.08294) [same_day_new]; [Seeing Beyond the Next Step: World-Model-Guided Human-Like Navigation in Multi-Agent Scenes](https://arxiv.org/abs/2611.07730) [same_day_new]; [Reels-RSI: Program-Level Self-Improvement for Code-Rendered Explainer Videos](https://arxiv.org/abs/2610.14495) [late_discovery]; [DyCraft: An Agentic System for Long-Horizon 4D Scene Generation](https://arxiv.org/abs/2610.40754) [late_discovery]; [CounterSketch: Physics-Grounded Counterfactual Reasoning for Sketch-to-Video Generation](https://arxiv.org/abs/2611.04244) [late_discovery]; [AgiWorld: An Agentic Video World Model for Building Persistent Worlds](https://arxiv.org/abs/2611.02341) [late_discovery] |
| Dynamic / Physical simulation and effects | [DyCraft: An Agentic System for Long-Horizon 4D Scene Generation](https://arxiv.org/abs/2610.40754) [late_discovery] |
| Datasets and Benchmarks | [GREP: Grounding Generated Room Evaluation in Principles](https://arxiv.org/abs/2611.05802) [late_discovery]; [Parametric CAD Bench v3: Evaluating Agentic Parametric CAD Authoring from Text and Engineering Drawings](https://arxiv.org/abs/2611.02659) [late_discovery]; [LongBanana: An Expert-Verified Benchmark for Long-Context Multi-Reference Image Synthesis](https://arxiv.org/abs/2611.06856) [late_discovery] |
| Cross-category | None verified in this run |

## Source ledger
| Source | Status | Checked pages / queries | Limitations |
|---|---|---|---|
| arxiv | partial | [{"query_or_url": "https://arxiv.org/list/cs.GR/new?skip=0&show=100", "checked_at": "2026-11-07T22:03:10.358621+00:00", "outcome": "Retrieved 16 entries; scan complete_observed_pagination=True; no claim of field completeness."}, {"query_or_url": "https://arxiv.org/list/cs.GR/recent?skip=0&show=100", "checked_at": "2026-11-07T22:03:10.432862+00:00", "outcome": "Retrieved 43 entries; scan complete_observed_pagination=True; no claim of field completeness."}, {"query_or_url": "https://arxiv.org/list/cs.CV/new?skip=0&show=100", "checked_at": "2026-11-07T22:03:10.675749+00:00", "outcome": "Retrieved 100 entries; scan complete_observed_pagination=True; no claim of field completeness."}, {"query_or_url": "https://arxiv.org/list/cs.CV/new?skip=0&show=2000", "checked_at": "2026-11-07T22:03:10.921151+00:00", "outcome": "Retrieved 258 entries; scan complete_observed_pagination=True; no claim of field completeness."}, {"query_or_url": "https://arxiv.org/list/cs.CV/recent?skip=0&show=100", "checked_at": "2026-11-07T22:03:11.051725+00:00", "outcome": "Retrieved 100 entries; scan complete_observed_pagination=True; no claim of field completeness."}, {"query_or_url": "https://arxiv.org/list/cs.CV/recent?skip=0&show=2000", "checked_at": "2026-11-07T22:03:11.975936+00:00", "outcome": "Retrieved 943 entries; scan complete_observed_pagination=True; no claim of field completeness."}, {"query_or_url": "https://arxiv.org/abs/2611.08294", "checked_at": "2026-11-07T22:11:59.719325+00:00", "outcome": "Canonical history/evidence inspected."}, {"query_or_url": "https://arxiv.org/abs/2611.08005", "checked_at": "2026-11-07T22:13:03.272852+00:00", "outcome": "Canonical history/evidence inspected."}, {"query_or_url": "https://arxiv.org/abs/2611.07730", "checked_at": "2026-11-07T22:14:06.129281+00:00", "outcome": "Canonical history/evidence inspected."}, {"query_or_url": "https://arxiv.org/abs/2611.07730", "checked_at": "2026-11-07T22:14:06.129281+00:00", "outcome": "Canonical history/evidence inspected."}, {"query_or_url": "https://arxiv.org/abs/2611.06433", "checked_at": "2026-11-07T22:15:06.483163+00:00", "outcome": "Canonical history/evidence inspected."}, {"query_or_url": "https://arxiv.org/abs/2608.24212", "checked_at": "2026-11-07T22:16:07.464849+00:00", "outcome": "Canonical history/evidence inspected."}, {"query_or_url": "https://arxiv.org/abs/2604.09568", "checked_at": "2026-11-07T22:17:06.100809+00:00", "outcome": "Canonical history/evidence inspected."}, {"query_or_url": "https://arxiv.org/abs/2604.09568", "checked_at": "2026-11-07T22:17:06.100809+00:00", "outcome": "Canonical history/evidence inspected."}, {"query_or_url": "https://arxiv.org/abs/2605.15843", "checked_at": "2026-11-07T22:18:06.597045+00:00", "outcome": "Canonical history/evidence inspected."}, {"query_or_url": "https://arxiv.org/abs/2610.09127", "checked_at": "2026-11-07T22:19:08.838498+00:00", "outcome": "Canonical history/evidence inspected."}, {"query_or_url": "https://arxiv.org/abs/2610.14495", "checked_at": "2026-11-07T22:20:06.165794+00:00", "outcome": "Canonical history/evidence inspected."}, {"query_or_url": "https://arxiv.org/abs/2610.04262", "checked_at": "2026-11-07T22:21:03.039761+00:00", "outcome": "Canonical history/evidence inspected."}, {"query_or_url": "https://arxiv.org/abs/2610.40754", "checked_at": "2026-11-07T22:21:56.473589+00:00", "outcome": "Canonical history/evidence inspected."}, {"query_or_url": "https://arxiv.org/abs/2611.05802", "checked_at": "2026-11-07T22:22:55.378511+00:00", "outcome": "Canonical history/evidence inspected."}, {"query_or_url": "https://arxiv.org/abs/2611.02659", "checked_at": "2026-11-07T22:23:57.166828+00:00", "outcome": "Canonical history/evidence inspected."}, {"query_or_url": "https://arxiv.org/abs/2610.41260", "checked_at": "2026-11-07T22:24:59.585334+00:00", "outcome": "Canonical history/evidence inspected."}, {"query_or_url": "https://arxiv.org/abs/2611.04244", "checked_at": "2026-11-07T22:26:00.873397+00:00", "outcome": "Canonical history/evidence inspected."}, {"query_or_url": "https://arxiv.org/abs/2611.02341", "checked_at": "2026-11-07T22:27:06.066146+00:00", "outcome": "Canonical history/evidence inspected."}, {"query_or_url": "https://arxiv.org/abs/2611.06856", "checked_at": "2026-11-07T22:28:09.621488+00:00", "outcome": "Canonical history/evidence inspected."}, {"query_or_url": "agent 3D object procedural modeling Blender material inverse graphics geometry editing October November 2026", "checked_at": "2026-11-07T22:04:07.698006+00:00", "outcome": "Hosted search executed; grounded response and citations preserved. This is a bounded query, not source completeness."}, {"query_or_url": "agent physical simulation particle effects deformable world research November 5 2026", "checked_at": "2026-11-07T22:06:27.029904+00:00", "outcome": "Hosted search executed; grounded response and citations preserved. This is a bounded query, not source completeness."}] | Four required cs.GR/cs.CV new/recent listings exhausted observed pagination with no errors; all 1062 unique listing IDs resolved. Other arXiv categories not scanned. Listing dates not publication dates; selected revision histories inspected, deferred histories remain pending. |
| hugging_face | partial | [{"query_or_url": "https://huggingface.co/papers/date/2026-11-05", "checked_at": "2026-11-07T22:03:12.324890+00:00", "outcome": "Target curation page retrieved; curation is not submission date. Selected plausible leads resolved with official metadata; remaining page leads not fully reviewed."}] | One target-day curation page; not all linked abstracts opened. HF date is not an event date. |
| openreview | partial | [{"query_or_url": "agent CAD generation reconstruction editing constraint solver program repair November 2026 site:openreview.net", "checked_at": "2026-11-07T22:04:42.180512+00:00", "outcome": "Hosted search executed; grounded response and citations preserved. This is a bounded query, not source completeness."}] | One OpenReview-targeted hosted search; no systematic venue traversal or date-verified new release. |
| official_venues | partial | [{"query_or_url": "agent SVG diagram chart slide poster editable visual feedback scientific illustration Manim November 5 2026 research", "checked_at": "2026-11-07T22:03:51.120085+00:00", "outcome": "Hosted search executed; grounded response and citations preserved. This is a bounded query, not source completeness."}, {"query_or_url": "agent animation cutscene temporal scene cinematography generation 2026 research", "checked_at": "2026-11-07T22:06:01.816653+00:00", "outcome": "Hosted search executed; grounded response and citations preserved. This is a bounded query, not source completeness."}, {"query_or_url": "agent graphics benchmark world auditing verification 2026 site:openaccess.thecvf.com", "checked_at": "2026-11-07T22:06:48.926143+00:00", "outcome": "Hosted search executed; grounded response and citations preserved. This is a bounded query, not source completeness."}] | CVF-targeted and other hosted searches returned proceedings leads; no primary proceedings page separately fetched in this run. No day-level publication event inferred. |
| project_author_lab | partial | [{"query_or_url": "https://dy-craft.github.io/", "checked_at": "2026-11-07T22:22:01.128155+00:00", "outcome": "Official DyCraft project supports animation-control relation; date authority remains arXiv."}, {"query_or_url": "agent 3D scene layout world generation BIM architecture spatial arrangement November 2026 project", "checked_at": "2026-11-07T22:05:07.383252+00:00", "outcome": "Hosted search executed; grounded response and citations preserved. This is a bounded query, not source completeness."}, {"query_or_url": "agent articulated asset joint mechanism rig generation research October 30 November 5 2026", "checked_at": "2026-11-07T22:05:35.501566+00:00", "outcome": "Hosted search executed; grounded response and citations preserved. This is a bounded query, not source completeness."}, {"query_or_url": "graphics agent memory replanning tool interface feedback program synthesis 2026 project lab", "checked_at": "2026-11-07T22:07:19.421090+00:00", "outcome": "Hosted search executed; grounded response and citations preserved. This is a bounded query, not source completeness."}] | Bounded searches, not an exhaustive release review. |

## Query coverage
- 2d: partial; [{'query_or_url': 'agent SVG diagram chart slide poster editable visual feedback scientific illustration Manim November 5 2026 research', 'checked_at': '2026-11-07T22:03:51.120085+00:00', 'outcome': 'Hosted search executed; grounded response and citations preserved. This is a bounded query, not source completeness.'}]
- object: partial; [{'query_or_url': 'agent 3D object procedural modeling Blender material inverse graphics geometry editing October November 2026', 'checked_at': '2026-11-07T22:04:07.698006+00:00', 'outcome': 'Hosted search executed; grounded response and citations preserved. This is a bounded query, not source completeness.'}]
- cad: partial; [{'query_or_url': 'agent CAD generation reconstruction editing constraint solver program repair November 2026 site:openreview.net', 'checked_at': '2026-11-07T22:04:42.180512+00:00', 'outcome': 'Hosted search executed; grounded response and citations preserved. This is a bounded query, not source completeness.'}]
- scene: partial; [{'query_or_url': 'agent 3D scene layout world generation BIM architecture spatial arrangement November 2026 project', 'checked_at': '2026-11-07T22:05:07.383252+00:00', 'outcome': 'Hosted search executed; grounded response and citations preserved. This is a bounded query, not source completeness.'}]
- articulation: partial; [{'query_or_url': 'agent articulated asset joint mechanism rig generation research October 30 November 5 2026', 'checked_at': '2026-11-07T22:05:35.501566+00:00', 'outcome': 'Hosted search executed; grounded response and citations preserved. This is a bounded query, not source completeness.'}]
- animation: partial; [{'query_or_url': 'agent animation cutscene temporal scene cinematography generation 2026 research', 'checked_at': '2026-11-07T22:06:01.816653+00:00', 'outcome': 'Hosted search executed; grounded response and citations preserved. This is a bounded query, not source completeness.'}]
- simulation: partial; [{'query_or_url': 'agent physical simulation particle effects deformable world research November 5 2026', 'checked_at': '2026-11-07T22:06:27.029904+00:00', 'outcome': 'Hosted search executed; grounded response and citations preserved. This is a bounded query, not source completeness.'}]
- benchmark: partial; [{'query_or_url': 'agent graphics benchmark world auditing verification 2026 site:openaccess.thecvf.com', 'checked_at': '2026-11-07T22:06:48.926143+00:00', 'outcome': 'Hosted search executed; grounded response and citations preserved. This is a bounded query, not source completeness.'}]
- harness: partial; [{'query_or_url': 'graphics agent memory replanning tool interface feedback program synthesis 2026 project lab', 'checked_at': '2026-11-07T22:07:19.421090+00:00', 'outcome': 'Hosted search executed; grounded response and citations preserved. This is a bounded query, not source completeness.'}]

## Source-derived candidate coverage

Mechanical audit of collected arXiv titles; relevance and semantic correctness require paper evidence.

- Metadata resolved: 1062 / 1062 collected IDs.
- Target-day / history-uncertain candidates: 179.
- Explicit triage decisions: 179; catalog-page delivery: 179.
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
| ManimCode: Learning Visual Self-Correction for Educational Animation | core | Role-conditioned Qwen3.5-4B ManimCode | Writes and rewrites full Manim programs and selects best rendered candidate | Educational animation code and rendered video | [Sections 4.1–4.2, pp.5–7; Appendix A.3 p.15](https://arxiv.org/pdf/2611.08294v1) |
| Deformable Contact-Aware 3D Object Placement | core | GPT-5.2 language/vision placement modules | Select support, size, orientation, target anchor and material mapping | Inserted object and deformable support geometry in reconstructed indoor scene | [§4 pp.4–6; Appendices A–B pp.13–14](https://arxiv.org/pdf/2611.08005v1) |
| Seeing Beyond the Next Step: World-Model-Guided Human-Like Navigation in Multi-Agent Scenes | core | Qwen3-VL-2B-Instruct with LoRA crowd-motion policy | Chooses executable short motion anchors | Virtual pedestrian positions and trajectories in Unity scenes | [§3–4 pp.3–6; Appendix K p.25](https://arxiv.org/pdf/2611.07730v1) |
| DreamRealm: Exploring and Materializing Hallucination Worlds for Trustworthy Vision-Language Models | core | Gemini 2.5 Pro planner/verifier V | Plans three ordered edit instructions and selects edit type; failed verification changes retry/fallback | Original raster image edited to support a counterfactual response | [Algorithm 1 p.14; worked example p.21](https://arxiv.org/pdf/2611.06433v2) |
| NeoWorld-Pro: Programming Interactive Scenes from Monocular Images for Embodied Simulation | core | MLLM Reasoner/Programmer/Critic roles | Generate Blender programs, articulation definitions and URDF export scripts; revise code and physical parameters | Articulated object assets reconstructed from scene crops | [§3.2 pp.5–6](https://arxiv.org/pdf/2608.24212v3) |
| EvoDesign: Agentic Editable Diagram Creation via Design Expertise Evolution | core | Structure, style, layout and refiner VLM agents | Instantiate and modify node/edge style, positions, grouping and routing | Editable Excalidraw canvas manifest | [§4.1–4.2 pp.4–5](https://arxiv.org/pdf/2604.09568v3) |
| WorldAct: Activating Monolithic 3D Worlds into Interactive-Ready Object-Centric Scenes | core | Qwen3.6-Plus object/view-selection agent | Select portable objects, issue SAM3 prompts and choose regeneration views | Monolithic 3DGS scene decomposed into background and object meshes | [§4 pp.4–6; Appendix B pp.16–17](https://arxiv.org/pdf/2605.15843v2) |
| CADFather: Autonomous CAD Reconstruction through Coordinated Tool Use | core | Qwen3.8-27B visual assistant | act(tool,candidate,n), visual proposal admission and finish decisions | CadQuery-based DSL program candidates and their solids | [§3.3 p.5; Fig.2](https://arxiv.org/pdf/2610.09127v1) |
| Reels-RSI: Program-Level Self-Improvement for Code-Rendered Explainer Videos | core | Claude Code director (Opus reviewed, Sonnet headless) | Writes script/storyboard/frame programs and repairs check findings | Executable explainer reel source and rendered animation | [§2–4 pp.2–5; §5.2 p.6](https://arxiv.org/pdf/2610.14495v1) |
| CADForge: Agentic Single-View CAD Reconstruction with Explicit Geometry Reasoning | core | GPT-5.5 planner, geometry observer/programmer, code and review agents | Ordered decomposition, geometry-solving scripts, component CadQuery generation and routed revisions | Part-aware editable B-Rep reconstruction | [§3 pp.3–6](https://arxiv.org/pdf/2610.04262v1) |
| DyCraft: An Agentic System for Long-Horizon 4D Scene Generation | core | GPT-6-Astra coding agent | Writes geometry, storyboards, motion and simulation code; repairs failed contact/joint/support states | Editable animated 3D Blender project and rendered film | [§3.1–3.4 pp.3–6](https://arxiv.org/pdf/2610.40754v1) |
| GREP: Grounding Generated Room Evaluation in Principles | core | GPT-5.6 Sol discovery/evaluator with camera selector | Formulates checks and requests/selects new render viewpoints when evidence insufficient | Submitted 3D rooms and rendered camera observations | [§3.3 pp.4–5; Appendix A.4 p.15](https://arxiv.org/pdf/2611.05802v1) |
| Parametric CAD Bench v3: Evaluating Agentic Parametric CAD Authoring from Text and Engineering Drawings | core | mini-swe-agent with Claude Opus 5.5 | Uses shell/code execution to author FreeCAD Python scripts and native feature trees | FCStd CAD documents for mechanical tasks | [§5.2 pp.12–13; Appendix B p.19](https://arxiv.org/pdf/2611.02659v1) |
| SketchDirector: Complex Scene Sketching via Agentic Layout Reasoning and Detail Refinement | core | GPT-5.5 layout reasoning agent | Emits executable object-level editing programs, replans after failed geometric/semantic verification | Bézier SVG object canvas | [§3.2–3.3; Figures 3–5](https://arxiv.org/pdf/2610.41260v1) |
| CounterSketch: Physics-Grounded Counterfactual Reasoning for Sketch-to-Video Generation | core | VLM intervention parser and causal reasoner | Changes vector objects/relations, infers event chain and locally replans violated semantic constraints | Vector scene graph and object animation trajectories | [§4.2–4.4 pp.6–7](https://arxiv.org/pdf/2611.04244v1) |
| AgiWorld: An Agentic Video World Model for Building Persistent Worlds | core | GPT-6-Astra director and state updater | Emits world layout, waypoints and structured prompts; revises them based on generated content | Camera-controlled video world and shared geometric/semantic state | [§3 pp.4–6; A.1 p.19](https://arxiv.org/pdf/2611.02341v1) |
| LongBanana: An Expert-Verified Benchmark for Long-Context Multi-Reference Image Synthesis | core | Claude Sonnet 4.6 RPR agent | Retrieves references, plans composition schedule, calls image tool, diagnoses and repairs drafts | Reference-grounded composite raster image | [§4.1 p.7; C.1 p.33; Fig.18 p.36](https://arxiv.org/pdf/2611.06856v1) |

## Prior-day memory and carry-over

Frozen history: `knowledge/daily-history/through-20261015-bvb-v11`. Previously unread records now fully read: 3. Prior pending records still without a new full read: 92.

See history-delta.json for per-paper transitions. Historical results remain in the frozen bundle; not repeated is not excluded, and new-to-history does not mean newly published.

## Abstract-first reading queue

Attention pool: 297; abstracts not delivered: 0; priority/triage gaps: 0; unread ranked leads: 42. See reading-plan.json for model-authored priorities and deferred leads. Priority is not an inclusion judgment or recall guarantee.
