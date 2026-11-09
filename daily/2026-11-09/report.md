# Agentic Graphics daily report
Date: 2026-11-09 | Timezone: America/Chicago | As of: 2026-11-09T19:50:25+00:00
browser-based same-day search; documented source coverage
Taxonomy: google-doc-taxonomy-v3-2026-10-15 | Snapshot: authorized_live_snapshot_reconciled_and_frozen

## Coverage limits
- No qualifying same-day Agentic Graphics paper was verified in the browsed source set. This does not prove none exists: listing events all predate target day, while indexing and announcement may lag.
- Frozen window: America/Chicago 2026-11-09 midnight through 2026-11-09T19:50:25+00:00. Later retrieval never extended eligibility. All 16 PDFs explicitly version-pinned and fully delivered, including continuation for 56-page VideoGen-Agent v4.
- Four observed-complete arXiv scans yielded 1054 unique IDs, all metadata-resolved. Zero target_and_uncertain records. All 107 catchup_review abstracts individually triaged. Additional outside-window hints and unmatched graphics-category abstracts reviewed. Remaining 907 catalog abstracts unreviewed, not excluded: unreviewed-catalog-queue.json.
- Nine maintained query families searched in nine calls. All five source families attempted but partial at platform level. cs.AI/cs.HC/cs.RO/cs.MM/eess.IV listings not reached. No exhaustive discovery claim.
- 160 individual triage decisions: triage.json. Title/abstract reject_obvious is provisional, not final excluded. Eleven date-focused unread leads: reading-plan.json. Eighteen additional ranked outside-window leads: deferred-extra-queue.json (two also saved unresolved). Search-only/non-arXiv leads: additional-search-leads.json. Primary abstracts/provenance: discovery/candidate-catalog.json and extra-metadata.json.
- Sixteen completed full papers: thirteen seven-day catch-up papers (including two revised versions) plus three newly completed older pending backlog items. No unchanged prior completed paper reread. See backlog-plan.json and history-delta.json. Remaining historical pending items stay in authorized INDEX.
- No final borderline label inferred from unread abstracts: enabling and borderline candidates remain explicit unresolved queues. Two old scientific-visualization source pages were opened and saved unresolved; prior exclusion of 2604.27996 is not accepted as ground truth.
- Deep reading stopped after all reviewed direct-action seven-day candidates and three reserved backlog slots were completed. At actual clock 20:16:29 UTC, about one minute remained before the three-minute finalization reserve, less than recent complete reading/checkpoint cycles. Four unused PDF slots do not override wall-clock reserve. No additional PDF started.
- Counts: 18 direct primary page opens plus eight hosted-search internal opens = 26; six listing responses, one HF page and 13 official metadata batches tracked separately. All retrieval and PDF reads used shared tools.
- Frozen taxonomy/source snapshot and snapshot_status preserved. Per-paper taxonomy deltas retain ambiguity for raster processing, auditing, non-LLM training and role-shared critics. No peer/current-run answers consulted.
- Concise event-separated summary: overview.md. Final audit confirms all 105 observed title hints have own triage decisions; metadata completeness is not abstract-screening completeness. Frozen frame comparison found no deviations.

No qualifying same-day Agentic Graphics paper was verified in the browsed source set.
Coverage is limited to the sources and queries below; unpublished or unindexed papers may be missing.

## already_reported (0)

## same_day_new (0)

## same_day_updates (0)

## late_discovery (16)

### [Frontier3DBench: Benchmarking Coding Agents for 3D Creation across Objects, Scenes, and Interactive Open Worlds](https://arxiv.org/abs/2611.09017)
core | High | new_relative_to_snapshot
Application: Datasets and Benchmarks, Static / Object, Static / Scene; operations: Generation, Reconstruction, Editing
A unified 145-task benchmark distinguishes appearance, structure and coordinated behavior in executable 3D creation; best reported overall score is 66.02/100.
Scope: Demonstrated coding agents create and edit executable Blender/Unreal artifacts; benchmark directly evaluates graphics action outcomes.
Limits: Only 11 coupled model-harness configurations are evaluated, so model and harness effects are confounded. Public errors but not quality scores enter retries. API cost accounting omits infrastructure and has partial usage records for some systems. Internal planning, adaptation and memory are insufficiently specified; L3 scoring exposes poor motion clearance and stateful workflow completion.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Modeling | Object and scene construction, reconstruction and editing. ([source](https://arxiv.org/pdf/2611.09017v1), §2.1–2.2 pp3–4) |
| input_form | Language, Image, 3D Representation | Input contains written instruction, optional reference images, and initial scene/assets for editing. ([source](https://arxiv.org/pdf/2611.09017v1), §2.1 p3) |
| output | Program, Graphics Artifact | Blender projects and executable construction/editing code are required deliverables. ([source](https://arxiv.org/pdf/2611.09017v1), §2.1 p3) |
| model_type | VLM | Coding agents combine visual understanding with program execution and handle image-conditioned tasks. ([source](https://arxiv.org/pdf/2611.09017v1), Abstract p1; §3.1 p6) |
| model_training | Not Reported | Developer models/harnesses and reasoning settings are listed; adaptation/training status is not explicitly specified. ([source](https://arxiv.org/pdf/2611.09017v1), §3.1; Appendix B pp17–18; full-text search training) |
| planning | Not Reported | Agents decide submission readiness, but no explicit internal plan representation is described. ([source](https://arxiv.org/pdf/2611.09017v1), §3.1 and Appendix B.1; plan search) |
| workflow | Sequential | Submit, run public checks, retry on failures within at most six attempts. ([source](https://arxiv.org/pdf/2611.09017v1), Appendix B.1 p17) |
| update_strategy | Regeneration | A new attempt starts after timeout, transport error or failed public check. ([source](https://arxiv.org/pdf/2611.09017v1), Appendix B.1 p17) |
| verifier | Programmatic | Public execution/delivery checks control retries. ([source](https://arxiv.org/pdf/2611.09017v1), §3.1 p7; Appendix B.1 p17) |
| feedback_assessment | Binary, Diagnosis | Failed checks return execution errors; no score feedback. ([source](https://arxiv.org/pdf/2611.09017v1), §3.1 p7; Appendix B.1 p17) |
| feedback_observation | Runtime | Execution errors are passed into a new attempt. ([source](https://arxiv.org/pdf/2611.09017v1), Appendix B.1 p17) |
| memory_time | Not Reported | L1/L2 agent memory lifetimes are not described. L3 workspace persistence and world state are distinct. ([source](https://arxiv.org/pdf/2611.09017v1), §3.1; Appendix B; memory/persistent searches) |
| memory_reach | Not Reported | No agent/role access scope for retained memory is reported. ([source](https://arxiv.org/pdf/2611.09017v1), §3.1; Appendix B; memory search) |
| action_type | Code/Script | Construction/editing code is executed in headless Blender. ([source](https://arxiv.org/pdf/2611.09017v1), §2.1 p3; Appendix B.1 p17) |
| graphics_software | General-Purpose | Submitted source bundles execute in headless Blender 5.2.1. ([source](https://arxiv.org/pdf/2611.09017v1), Appendix B.1 p17) |
| tools | Execution Utilities, Graphics Operations | Isolated execution containers run programs constructing/editing Blender artifacts. ([source](https://arxiv.org/pdf/2611.09017v1), §2.1 p3; Appendix B.1 p17) |
| resources | Assets | Public task assets and supplied initial scenes are agent-visible. ([source](https://arxiv.org/pdf/2611.09017v1), §2.1 p3; Appendix B.1 p17) |
| representation | Code, Geometry, Pixels | Executable code, native editable geometry and rendered images. ([source](https://arxiv.org/pdf/2611.09017v1), §2.1 p3; Appendix B.1 p17) |

Events: [{"type": "first_submission", "value": "2026-11-06T05:45:31+00:00", "precision": "timestamp", "timezone": "UTC", "local_value": "2026-11-05T23:45:31-06:00", "primary_url": "https://arxiv.org/abs/2611.09017", "authority": "primary", "version": "v1", "evidence": "Canonical submission history v1; latest available before cutoff.", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: ["Monitor a separate evaluation-protocol descriptor: final judges and runtime probes must not be conflated with generative-agent loop feedback."]

### [Video-Coder: Reinforcing Agentic Coding for Video Generation](https://arxiv.org/abs/2611.09894)
core | High | new_relative_to_snapshot
Application: Dynamic / Animation and temporal scene; operations: Generation
Trains a multimodal code-driven video agent through SFT and agentic RL with an annealed execution/video reward balance; draft animations improve structure and motion of downstream videos.
Scope: The multimodal agent writes, executes and repairs Blender programs controlling scene geometry, motion and camera; direct graphics action is demonstrated.
Limits: Training-set counts conflict: abstract/method name SFT-6k and RL-2k, whereas experiment/conclusion name 10k and 4k. Reported PhyGenBench arithmetic also conflicts (table 0.61 to 0.67 versus approximately seven points in abstract; OmniWeaving text mismatches table). Material phenomena remain limited by untextured drafts. No standalone limitations section was found; these are observed reporting and experimental limits.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Animation | Construct dynamic 3D scenes with keyframes, drivers, constraints or physics, rendered as animation. ([source](https://arxiv.org/pdf/2611.09894v1), §3.2 p5; Appendix A p12) |
| input_form | Language | Given a text prompt c, the model writes Blender Python. ([source](https://arxiv.org/pdf/2611.09894v1), §3.2 p5) |
| output | Program, Rendered Media | Self-contained script and final re-rendered white-model video; no .blend files allowed. ([source](https://arxiv.org/pdf/2611.09894v1), §3.2 p5; Appendix A p12) |
| model_type | VLM | Multimodal coding agent initialized from Qwen3.5-9B and observes rendered frames. ([source](https://arxiv.org/pdf/2611.09894v1), §3.3 p5) |
| model_training | Supervised Fine-Tuning, RL Post-Training | SFT followed by harness-native GRPO agentic reinforcement learning optimizes only the coding policy. ([source](https://arxiv.org/pdf/2611.09894v1), §3.3 pp5–6) |
| planning | PO-2 | Fixed Think & Plan/write/check/run workflow asks the model to reason explicitly about objects, dimensions, positions, timing and camera before writing code. ([source](https://arxiv.org/pdf/2611.09894v1), Appendix A Figure 6 p13) |
| workflow | Sequential | Write, static check, render, inspect, revise and repeat before final submission. ([source](https://arxiv.org/pdf/2611.09894v1), §3.2 p5; Appendix A p13) |
| update_strategy | Local Patch, Regeneration | Fix concrete problems in script; prompt supports rewrite or sed -i. ([source](https://arxiv.org/pdf/2611.09894v1), Appendix A pp13–14) |
| verifier | Self, Programmatic | Static checks and harness content checks flag failures; policy inspects frames against description. ([source](https://arxiv.org/pdf/2611.09894v1), §3.2 p5; Appendix A pp13–14) |
| feedback_assessment | Binary, Diagnosis | RUN OK/errors, tracebacks, content problems and model-written concrete visual issues. ([source](https://arxiv.org/pdf/2611.09894v1), §3.2 p5; Appendix A p13) |
| feedback_observation | Visual, Structural Scene State, Runtime | Returned frames, tracebacks, object counts and moving mesh positions/timing/framing. ([source](https://arxiv.org/pdf/2611.09894v1), Appendix A Figure 6 p13) |
| memory_time | Short-Term Memory | Current policy conditions on previous programs, execution feedback and rendered videos across turns. ([source](https://arxiv.org/pdf/2611.09894v1), §3.2 equation 2 p5) |
| memory_reach | Local Memory | One coding policy retains its episode code/observations in isolated sandbox. ([source](https://arxiv.org/pdf/2611.09894v1), §3.2 p5) |
| action_type | Code/Script, Tool/Function Call | Shell writes Python scripts and calls check_script/run_blender. ([source](https://arxiv.org/pdf/2611.09894v1), §3.2 p5; Appendix A pp13–14) |
| graphics_software | Agent-Adapted | Dedicated harness wraps Blender execution/rendering with structured feedback. ([source](https://arxiv.org/pdf/2611.09894v1), §3.2 p5) |
| tools | Execution Utilities, Graphics Operations, Static Validator | Shell/file commands, Blender construction/rendering, and check_script syntax/contract checker. ([source](https://arxiv.org/pdf/2611.09894v1), §3.2 p5; Appendix A p13) |
| resources | Documentation & Rules | System prompt gives script contract, rendering rules and API constraints; external assets/files/add-ons forbidden. ([source](https://arxiv.org/pdf/2611.09894v1), Appendix A pp12–14) |
| representation | Code, Geometry, Dynamic State, Pixels | Python programs build meshes, time-varying motions and rendered frames. ([source](https://arxiv.org/pdf/2611.09894v1), §3.2 p5; Appendix A pp12–13) |

Events: [{"type": "first_submission", "value": "2026-11-06T18:59:57+00:00", "precision": "timestamp", "timezone": "UTC", "local_value": "2026-11-06T12:59:57-06:00", "primary_url": "https://arxiv.org/abs/2611.09894", "authority": "primary", "version": "v1", "evidence": "Canonical history v1, before cutoff.", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: ["Keep RL optimization scores distinct from task-time Binary/Diagnosis feedback."]

### [Parametric CAD Bench v3: Evaluating Agentic Parametric CAD Authoring from Text and Engineering Drawings](https://arxiv.org/abs/2611.02659)
core | High | new_relative_to_snapshot
Application: Static / CAD, Datasets and Benchmarks; operations: Generation, Reconstruction, Editing
Separates native CAD geometry and engineering specification consistency in a versioned 100-task suite; best overall mean continuous reward is 61.03%, not a success rate.
Scope: Evaluates actual agent executions that write FreeCAD scripts and native editable CAD documents. Artifact generation is direct graphics action, despite underspecified internal harness mechanics.
Limits: Curated single-body tasks exclude assembly mating, FEM/FEA and manufacturing qualification. Geometric/parameter rewards are heuristic and can penalize alternative valid constructions. Create-and-edit does not establish history preservation. One final outcome per task and model/harness/provider confounds limit causal comparisons and robustness claims. Internal planning, memory and feedback are largely unspecified.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Modeling | Mechanical CAD creation, editing and reconstruction. ([source](https://arxiv.org/pdf/2611.02659v1), §3.1 p4) |
| input_form | Language, Image | Text descriptions and dimensions, or engineering drawings; no externally supplied starting FCStd. ([source](https://arxiv.org/pdf/2611.02659v1), Table 1 p4; §3.2 p8) |
| output | Program, Graphics Artifact | answer.py and answer.FCStd; base/edit FCStd pair in edit tasks. ([source](https://arxiv.org/pdf/2611.02659v1), §3.2 p8; Appendix B p19) |
| model_type | VLM | Multimodal observation channel sends complete image payloads to the model before CAD construction. ([source](https://arxiv.org/pdf/2611.02659v1), §5.2 pp12–13) |
| model_training | Not Reported | Configurations and provider models are listed; task-specific adaptation status is not reported. ([source](https://arxiv.org/pdf/2611.02659v1), §5–6; Appendix A; training search) |
| planning | Not Reported | No explicit plan representation or degree described. ([source](https://arxiv.org/pdf/2611.02659v1), §4–5; appendices; planning search) |
| workflow | Sequential | Drawing must be observed before proceeding; create-and-edit builds base then target. ([source](https://arxiv.org/pdf/2611.02659v1), §3.1 p4; §5.2 pp12–13) |
| update_strategy | Not Reported | Interactive workflows and failure recovery are mentioned but specific feedback-driven update mechanism is absent. ([source](https://arxiv.org/pdf/2611.02659v1), §4–6; Appendix A–C; retry/feedback searches) |
| verifier | Not Reported | Programmatic verifier and held-out assets are isolated from agent environment; no loop judge is specified. ([source](https://arxiv.org/pdf/2611.02659v1), §4.1–4.2 pp9–12; feedback search) |
| feedback_assessment | Not Reported | Continuous task reward is final scoring; no returned assessment guiding subsequent action is established. ([source](https://arxiv.org/pdf/2611.02659v1), §4.2 pp9–12; full-text feedback search) |
| feedback_observation | Not Reported | Task drawing observation is explicit, but feedback observations used for repairs are not specified. ([source](https://arxiv.org/pdf/2611.02659v1), §4–5; feedback/tool searches) |
| memory_time | Not Reported | No retained agent state lifetime reported. ([source](https://arxiv.org/pdf/2611.02659v1), §4–6; Appendix A; memory search) |
| memory_reach | Not Reported | No role/agent memory accessibility described. ([source](https://arxiv.org/pdf/2611.02659v1), §4–6; Appendix A; memory search) |
| action_type | Code/Script | Write FreeCAD 1.1.0 script that builds native feature trees. ([source](https://arxiv.org/pdf/2611.02659v1), Appendix B p19; Appendix C p24) |
| graphics_software | General-Purpose | Native FreeCAD Python scripts operate in pinned runtime; multimodal transport bridge is not a CAD operation abstraction. ([source](https://arxiv.org/pdf/2611.02659v1), §4.1 p9; Appendix B p19) |
| tools | Execution Utilities, Graphics Operations | Shell transport/execution and FreeCAD feature construction are used. ([source](https://arxiv.org/pdf/2611.02659v1), §4.1 p9; §5.2 p13; Appendix B p19) |
| resources | Documentation & Rules | Shared native-feature output contract and execution requirements supplied to agents. ([source](https://arxiv.org/pdf/2611.02659v1), Appendix B p19 and C p24) |
| representation | Code, Geometry | Python programs and B-rep solids with native feature-tree dependencies. ([source](https://arxiv.org/pdf/2611.02659v1), §1 p1; Appendix B p19) |

Events: [{"type": "first_submission", "value": "2026-11-02T07:19:55+00:00", "precision": "timestamp", "timezone": "UTC", "local_value": "2026-11-02T01:19:55-06:00", "primary_url": "https://arxiv.org/abs/2611.02659", "authority": "primary", "version": "v1", "evidence": "Canonical v1 history. September 24 is results snapshot, not paper submission.", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: ["Benchmark final reward and agent-loop feedback need separate representation; absence of internal harness reporting should remain visible."]

### [CADFather: Autonomous CAD Reconstruction through Coordinated Tool Use](https://arxiv.org/abs/2610.09127)
core | High | new_relative_to_snapshot
Application: Static / CAD; operations: Reconstruction
Coordinates heterogeneous reconstruction tools and protected candidate-pool search without additional training; reported DeepCAD/Fusion360/MCB mean IoUs are 0.987/0.976/0.913 with zero invalid outputs under its protocol.
Scope: Visual assistant explicitly selects CAD candidates, tools, proposal counts and stopping using executed geometry feedback.
Limits: Operation library restricts attainable shape and optimizer cannot repair wrong topology. Pool retention cannot recover ungenerated alternatives. Compute limits and incomplete visual evidence cause premature termination. Baseline validity rules, input modalities and subsets differ; ablations do not isolate assistant selection policy or matched consumed compute. No assembly, tolerance or manufacturing-intent validation.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Modeling | Mesh-to-parametric CAD reconstruction. ([source](https://arxiv.org/pdf/2610.09127v1), §3.1 p3) |
| input_form | 3D Representation | Input target mesh M*. ([source](https://arxiv.org/pdf/2610.09127v1), §3.1 p3) |
| output | Program, Graphics Artifact | Final protected-best CAD program and mesh. ([source](https://arxiv.org/pdf/2610.09127v1), Fig1 p4; §3.5 p7) |
| model_type | VLM | Qwen3.8-27B visual assistant consumes renders, scores and history. ([source](https://arxiv.org/pdf/2610.09127v1), §3.3 p5; §4.1 p8) |
| model_training | Off-the-Shelf | Both assistant and generation models are frozen; no additional training. ([source](https://arxiv.org/pdf/2610.09127v1), §4.1 p8; abstract) |
| planning | Not Reported | One-sentence current-step intent and up to four action calls; no multi-step plan representation reported. ([source](https://arxiv.org/pdf/2610.09127v1), §3.3 p5; plan/rationale search across full PDF) |
| workflow | Graph-Structured | Parent/child program pool preserves alternative branches; assistant can extend earlier candidates or root. ([source](https://arxiv.org/pdf/2610.09127v1), §3.2–3.3 pp4–5) |
| update_strategy | Local Patch, Candidate Selection | Append operations or refine numerical parameters; protect best valid score and choose alternative candidates. ([source](https://arxiv.org/pdf/2610.09127v1), §3.2,3.4–3.5 pp4–7) |
| verifier | Self, Programmatic | Assistant visually accepts proposals after programmatic validity/measurement. ([source](https://arxiv.org/pdf/2610.09127v1), §3.5 p6) |
| feedback_assessment | Binary, Score, Diagnosis | Validity and visual acceptance, IoU/GMS scores, failure/budget reasons are returned. ([source](https://arxiv.org/pdf/2610.09127v1), §3.5–3.6 pp6–7) |
| feedback_observation | Visual, Structural Scene State, Runtime | Renders, candidate operation/validity/measurement table, build and timeout outcomes. ([source](https://arxiv.org/pdf/2610.09127v1), §3.3–3.6 pp5–7) |
| memory_time | Short-Term Memory | Per-part pool and transcript retain previous executed requests and rationales; prior renders are not retained. ([source](https://arxiv.org/pdf/2610.09127v1), §3.2–3.3 pp4–5) |
| memory_reach | Local Memory | Assistant receives bounded pool table and transcript for that part; proposal tools receive selected parents. ([source](https://arxiv.org/pdf/2610.09127v1), §3.3 p5) |
| action_type | Tool/Function Call | act(tool,candidate,n) and finish calls. ([source](https://arxiv.org/pdf/2610.09127v1), §3.3 p5) |
| graphics_software | Agent-Adapted | Shared CadQuery DSL exposed through proposal/refinement tools and candidate table. ([source](https://arxiv.org/pdf/2610.09127v1), §3.1–3.4 pp3–6) |
| tools | Graphics Operations, Execution Utilities, Static Validator, Solver Validator, Perception models | Learned CAD proposal model, geometric construction, numerical distance-fitting optimizer, execution, watertightness checks and rendering. ([source](https://arxiv.org/pdf/2610.09127v1), §3.4–3.5 p6) |
| resources | Documentation & Rules | Reusable rule description provides objective, tool costs and response format each step. ([source](https://arxiv.org/pdf/2610.09127v1), §3.3 p5) |
| representation | Code, Geometry, Pixels | Executable DSL programs, candidate meshes and renders. ([source](https://arxiv.org/pdf/2610.09127v1), §3.1–3.3 pp3–5) |

Events: [{"type": "first_submission", "value": "2026-10-06T21:20:59+00:00", "precision": "timestamp", "timezone": "UTC", "local_value": "2026-10-06T16:20:59-05:00", "primary_url": "https://arxiv.org/abs/2610.09127", "authority": "primary", "version": "v1", "evidence": "Canonical history; unchanged v1, newly completed authorized prior unresolved backlog, not seven-day catch-up.", "prior_event_status": "already_seen"}]
Taxonomy deltas: ["Candidate retention is not automatically Rollback; preserve the distinction between immutable search branches and reverting mutable artifact state."]

### [GATOR: Generative and Agentic 3D Object Reconstruction From Casual Images](https://arxiv.org/abs/2610.11215)
core | High | new_relative_to_snapshot
Application: Static / Object; operations: Reconstruction, Editing
Combines generative instance-specific initialization with localized agent repair; refinement improves appearance and repairs supports/openings without remaking complete objects.
Scope: GPT-6-Astra autonomously edits generated 3D geometry and materials via Blender and retains/reverts changes from matched render comparisons.
Limits: Upstream mask/depth errors remain harmful. Proprietary agent costs up to ten minutes per object. Refinement does not uniformly improve geometric metrics and worsens several HANDAL measures. Final rigid-body comparison covers one room and is not in-loop simulation feedback. The controller adaptation status is not explicit.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Modeling | Repair topology, geometry, UVs and materials. ([source](https://arxiv.org/pdf/2610.11215v1), §3.5 p6) |
| input_form | Image, 3D Representation | Generated mesh plus input images, masks, cameras and depth. ([source](https://arxiv.org/pdf/2610.11215v1), A.4 p19) |
| output | Graphics Artifact | Deliverable is selected GLB, not report or gallery. ([source](https://arxiv.org/pdf/2610.11215v1), A.4 p19) |
| model_type | VLM | Multimodal GPT-6-Astra judges image/render agreement. ([source](https://arxiv.org/pdf/2610.11215v1), §3.5 p6) |
| model_training | Not Reported | Prompted Codex configuration is given; explicit no-retraining statement applies to generator, not controller. ([source](https://arxiv.org/pdf/2610.11215v1), A.4–A.5 pp19–22; training/frozen/fine-tun search) |
| planning | PO-2 | Scope before scheduling: identify highest-value repairs, allocate effort, record concise notes; fixed review/checkpoint obligations. ([source](https://arxiv.org/pdf/2610.11215v1), A.4 Prompt1 p19) |
| workflow | Sequential | Inspect, edit, render, review, checkpoint and repeat. ([source](https://arxiv.org/pdf/2610.11215v1), §3.5 p6; A.4 pp19–21) |
| update_strategy | Local Patch, Rollback, Candidate Selection | Target local components, revert degraded edits and select best inspected snapshot. ([source](https://arxiv.org/pdf/2610.11215v1), A.4 pp19–21) |
| verifier | Self, Programmatic | Agent inspects comparisons; review helper checks import/materials before further edits. ([source](https://arxiv.org/pdf/2610.11215v1), A.4 pp20–21) |
| feedback_assessment | Binary, Diagnosis | Retain/revert candidate; identify remaining geometry, texture and pose defects. ([source](https://arxiv.org/pdf/2610.11215v1), A.4 pp19–21) |
| feedback_observation | Visual, Structural Scene State | Matched comparison/detail images, native-frame anchor statistics and material checks. ([source](https://arxiv.org/pdf/2610.11215v1), A.4 p20) |
| memory_time | Short-Term Memory | Save packed scene after improvements; retain inspected checkpoint and outstanding defects for later revision/recovery. ([source](https://arxiv.org/pdf/2610.11215v1), A.4 pp19–21) |
| memory_reach | Local Memory | Single object-refinement worker retains its snapshots. ([source](https://arxiv.org/pdf/2610.11215v1), A.4 pp19–21) |
| action_type | Code/Script, Tool/Function Call | Write Blender scripts and invoke review, export, checkpoint and finish helpers. ([source](https://arxiv.org/pdf/2610.11215v1), §3.5 p6; A.4 pp19–21) |
| graphics_software | Agent-Adapted | Prebuilt review/export tools wrap Blender with receipts, matched views and checks. ([source](https://arxiv.org/pdf/2610.11215v1), A.4 pp19–20) |
| tools | Execution Utilities, Graphics Operations, Static Validator | Scene edits/rendering, export/checkpoint helpers, import/material validator. ([source](https://arxiv.org/pdf/2610.11215v1), A.4 pp19–21) |
| resources | Documentation & Rules | Prompt supplies geometry/material rules and coordinate conventions. ([source](https://arxiv.org/pdf/2610.11215v1), A.4 pp19–21) |
| representation | Code, Geometry, Pixels | Scripts edit mesh/material state and compare renders. ([source](https://arxiv.org/pdf/2610.11215v1), §3.5 p6; A.4 pp19–21) |

Events: [{"type": "first_submission", "value": "2026-10-08T04:13:04+00:00", "precision": "timestamp", "timezone": "UTC", "local_value": "2026-10-07T23:13:04-05:00", "primary_url": "https://arxiv.org/abs/2610.11215", "authority": "primary", "version": "v1", "evidence": "Canonical v1 history; newly completed prior unresolved backlog, outside seven-day lookback.", "prior_event_status": "already_seen"}]
Taxonomy deltas: []

### [Reels-RSI: Program-Level Self-Improvement for Code-Rendered Explainer Videos](https://arxiv.org/abs/2610.14495)
core | High | new_relative_to_snapshot
Application: 2D Graphics, Dynamic / Animation and temporal scene; operations: Generation, Editing
Makes explainer programs auditable across runs: tested rules discovered four latent defects in earlier reels; weaker-director violations fell from thirty unguarded to five guarded in the reported small study.
Scope: Director and frame workers create and revise editable animation programs through a graphics CLI; reusable tested memory feeds subsequent authoring.
Limits: Only 111 reels, one model family, small ablation cells and no human preference study. Only one newly learned rule was compiled. Position bias invalidated the apparent 11–1 evolution win; lessons did not yield compounding quality gains and visual preferences missed omitted facts. Human curation cost is unmeasured. Auto-accept learning-curve arm explicitly departs from default human gating.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Animation, Visualization | Explanatory diagrams and timed visual sequences deliver worked geometry/science/history content. ([source](https://arxiv.org/pdf/2610.14495v1), §1–2 pp1–3) |
| input_form | Language, Image | One-sentence topics and geometry task from textbook photo. ([source](https://arxiv.org/pdf/2610.14495v1), Table2 p6; Appendix B p19) |
| output | Program, Rendered Media | Editable script, storyboard/frame programs and MP4. ([source](https://arxiv.org/pdf/2610.14495v1), §2 p2; Fig1 p3) |
| model_type | VLM | Claude director transcribes text and geometry from photo and supports visual review. ([source](https://arxiv.org/pdf/2610.14495v1), §5.1 p6; Appendix B p19) |
| model_training | Off-the-Shelf | Self-improvement happens in programs rather than weights; interchangeable existing agent CLIs follow Markdown skill. ([source](https://arxiv.org/pdf/2610.14495v1), Abstract p1; §1–3 pp2–4) |
| planning | PO-2 | Ten-step handbook guides model-created storyboard with per-frame scene, duration, transition and route. ([source](https://arxiv.org/pdf/2610.14495v1), §2–3 pp2–4) |
| workflow | Graph-Structured | Director produces briefs for frame workers, whose frame programs are assembled before review. ([source](https://arxiv.org/pdf/2610.14495v1), §3 p4; §4.2 pp4–5) |
| update_strategy | Local Patch | Change one program value/frame; recorded diffs link defects to fixes. ([source](https://arxiv.org/pdf/2610.14495v1), Table1 p3; §4.1–4.2 p4) |
| verifier | Programmatic, Human | Finalize checks lint/runtime/layout/contrast; reviewed reels use human gates at plan/look-dev/final. ([source](https://arxiv.org/pdf/2610.14495v1), §4.1 p4; §5.1–5.2 p6) |
| feedback_assessment | Binary, Diagnosis | Errors block rendering; findings carry codes, lines/messages and recommended fixes. ([source](https://arxiv.org/pdf/2610.14495v1), §4.1 p4; Appendix A pp18–19) |
| feedback_observation | Runtime, Structural Scene State, Visual | Runtime errors, layout/contrast/animation-structure checks and viewed render defects. ([source](https://arxiv.org/pdf/2610.14495v1), §3–4 pp3–4; §5.1–5.2 p6) |
| memory_time | Short-Term Memory, Long-Term Memory | Per-pass logs/snapshots persist during revisions; accepted lessons/rules are injected into future reels. ([source](https://arxiv.org/pdf/2610.14495v1), §4.1–4.3 pp4–5) |
| memory_reach | Local Memory | Lessons have director/frame/solve/history scopes and conditional injection into matching worker briefs. ([source](https://arxiv.org/pdf/2610.14495v1), §4.2–4.3 pp4–5; Appendix B) |
| action_type | Code/Script, Tool/Function Call | Agent writes frame code and invokes reels CLI commands. ([source](https://arxiv.org/pdf/2610.14495v1), Fig1 p3; §3 p4) |
| graphics_software | Agent-Adapted | Purpose-built CLI adapts headless browser/GSAP/FFmpeg rendering for agent skill execution. ([source](https://arxiv.org/pdf/2610.14495v1), §2–3 pp3–4) |
| tools | Execution Utilities, Graphics Operations, Static Validator | CLI assembles/renders, manages snapshots/assets, checks source/runtime/layout. ([source](https://arxiv.org/pdf/2610.14495v1), §3–4 pp4–5) |
| resources | Assets, Documentation & Rules | Map layers, credited images, fonts, chalk kits, presets and handbook references. ([source](https://arxiv.org/pdf/2610.14495v1), §3 p4) |
| representation | Code, Layouts, Pixels | HTML/SVG/Canvas/Three.js frame programs, diagram layouts and rendered MP4. ([source](https://arxiv.org/pdf/2610.14495v1), §2 pp2–3) |

Events: [{"type": "first_submission", "value": "2026-10-10T02:46:44+00:00", "precision": "timestamp", "timezone": "UTC", "local_value": "2026-10-09T21:46:44-05:00", "primary_url": "https://arxiv.org/abs/2610.14495", "authority": "primary", "version": "v1", "evidence": "Official Atom v1 and canonical history; newly completed prior backlog, not target-day or seven-day item.", "prior_event_status": "already_seen"}]
Taxonomy deltas: ["Monitor memory provenance/admission: executable tested rules, human-gated lessons and self-rewritten playbooks differ substantially despite sharing Long-Term Memory."]

### [ManimCode: Learning Visual Self-Correction for Educational Animation](https://arxiv.org/abs/2611.08294)
core | High | new_relative_to_snapshot
Application: 2D Graphics, Dynamic / Animation and temporal scene; operations: Generation, Editing
Learns visual correction rather than only final-program generation; render success reaches 96.6%/97.0% on two benchmarks, with improved long-form completion when substituted as scene module.
Scope: Learned role-conditioned controller writes and rewrites executable animation programs in response to runtime, layout and rendered-video evidence.
Limits: RL primarily improves render success, not quality. Candidate retention cannot fix oscillating/remaining layout defects. Human validation uses one team annotator and only 98 pairs; agreement is poor for small judge gaps. Single-pass baselines differ in retrieval/budget. Knowledge-base overlap required masking on ManimBench. No standalone limitations section; these limits are explicit in evaluation and appendices.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Animation, Visualization | Educational animations show mathematical relationships, diagrams and evolving processes. ([source](https://arxiv.org/pdf/2611.08294v1), §1 p2; §3 p4) |
| input_form | Language | Each inference request starts with a newly generated program; no target code/video required. ([source](https://arxiv.org/pdf/2611.08294v1), §4.2 p7) |
| output | Program, Rendered Media | Selected executable program and rendered animation video. ([source](https://arxiv.org/pdf/2611.08294v1), §3.2 p5; §4.2 p7) |
| model_type | VLM | Single Qwen3.5-4B receives sampled frames for reviewing. ([source](https://arxiv.org/pdf/2611.08294v1), §4.1 p6) |
| model_training | Supervised Fine-Tuning, RL Post-Training | Role-conditioned LoRA SFT followed by Reviser RLOO RL. ([source](https://arxiv.org/pdf/2611.08294v1), §4.1–4.2 pp6–7; B.2 p16) |
| planning | PO-1 | Fixed retrieval/write/render/review/rewrite protocol with hard-coded acceptance and stopping. ([source](https://arxiv.org/pdf/2611.08294v1), §4.2 p7; Table7 p15) |
| workflow | Sequential | Ordered render–review–revise loop with up to ten renders. ([source](https://arxiv.org/pdf/2611.08294v1), Fig3 p6; Table7 p15) |
| update_strategy | Regeneration, Candidate Selection, Rollback | Reviser rewrites full program, retains best-scored candidate and resets revision base to best if alignment/completeness fall >0.5. ([source](https://arxiv.org/pdf/2611.08294v1), §3.2 p5; Table7 p15) |
| verifier | Critic, Programmatic | Dedicated Reviewer role critiques sampled frames; renderer and layout checker provide additional evidence. ([source](https://arxiv.org/pdf/2611.08294v1), §3.2 p5; §4 p7) |
| feedback_assessment | Binary, Score, Diagnosis | Render success/failure, four 1–5 review scores and specific defect critique. ([source](https://arxiv.org/pdf/2611.08294v1), §3.2 p5; Table7 p15) |
| feedback_observation | Visual, Structural Scene State, Runtime | Eight video frames, object positions at animation pauses, execution errors. ([source](https://arxiv.org/pdf/2611.08294v1), §3.2 p5) |
| memory_time | Short-Term Memory | Latest candidate and best candidate retained across revision rounds. ([source](https://arxiv.org/pdf/2611.08294v1), Table7 p15) |
| memory_reach | Local Memory | Each role receives a prescribed subset of code, critique, errors, frames and API cards. ([source](https://arxiv.org/pdf/2611.08294v1), §4.1 p6; Table8 p16) |
| action_type | Code/Script | Writer/Reviser emits full executable Manim program. ([source](https://arxiv.org/pdf/2611.08294v1), §4 p6) |
| graphics_software | Agent-Adapted | Harness wraps ManimCE and plugins with layout feedback and visual review. ([source](https://arxiv.org/pdf/2611.08294v1), §3.2 p5; A.3 p15) |
| tools | Execution Utilities, Graphics Operations, Static Validator | Manim rendering/execution and pause-state layout checker. ([source](https://arxiv.org/pdf/2611.08294v1), §3.2 p5; A.3 p15) |
| resources | Documentation & Rules, Examples & Trajectories | Retrieved API docs, plugin recipes, best-practice rules and example scenes. ([source](https://arxiv.org/pdf/2611.08294v1), §3.1 p5; A.2 p15) |
| representation | Code, Layouts, Pixels | Manim programs, structured diagram layout positions and rendered video frames. ([source](https://arxiv.org/pdf/2611.08294v1), Fig1 p4; §3.2 p5) |

Events: [{"type": "first_submission", "value": "2026-11-05T16:55:44+00:00", "precision": "timestamp", "timezone": "UTC", "local_value": "2026-11-05T10:55:44-06:00", "primary_url": "https://arxiv.org/abs/2611.08294", "authority": "primary", "version": "v1", "evidence": "Canonical v1 history; PDF cover date October31 is not submission authority.", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: ["Reviewer-role Critic versus same-backbone Self is ambiguous in the codebook; role-separated Critic is used and shared weights are disclosed."]

### [CrowdDirector: Runtime Orchestration of Crowd Simulation through Natural-Language Directives](https://arxiv.org/abs/2611.08763)
core | Medium | new_relative_to_snapshot
Application: Dynamic / Animation and temporal scene; operations: Editing
Separates language-time authoring from cheap local crowd control: 20-agent updates take 20.5 ms versus 3,880 ms for recurrent LLM, while response agreement improves over rules.
Scope: Controller directly changes simulated crowd state and selects character actions in an animated Unity environment; no LLM-only requirement applies.
Limits: Only 2D environments, finite operation library, 15 participants, and training crowds of 8–40. Large-crowd tests establish computation scaling rather than behavioral generalization. Per-tick LLM remains better on most response metrics. Model-family/training labels are imperfect fits to the frozen taxonomy.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Animation | Runtime behavioral crowd authoring drives Unity movement, interaction and animation. ([source](https://arxiv.org/pdf/2611.08763v1), §1 p2; §3.6 p7) |
| input_form | Language | User supplies natural-language directive while scene state is read internally from the running Unity environment. ([source](https://arxiv.org/pdf/2611.08763v1), §3.2–3.3 pp3–5) |
| output | Structured Specification | Validated directive patches and action-target assignments sent to engine. ([source](https://arxiv.org/pdf/2611.08763v1), §3.2 p4; §3.6 p7) |
| model_type | Hybrid | LLM interprets directives; relational GNN chooses all recurrent actions without text encoder. ([source](https://arxiv.org/pdf/2611.08763v1), §3.1–3.4 pp3–5) |
| model_training | Unclear | GNN trained with KL to rollout/LLM targets; no pretrained GNN or fine-tuning described; interpreter adaptation unstated. ([source](https://arxiv.org/pdf/2611.08763v1), §3.5 pp5–6; full-text fine/pretrain search) |
| planning | Not Applicable | Controller selects one available action, retains until completion/failure, and chooses again; route planning delegated to Unity. ([source](https://arxiv.org/pdf/2611.08763v1), §3.2–3.6 pp3–7; plan search) |
| workflow | Sequential | Interpret, validate, build graph/candidates, select, execute. ([source](https://arxiv.org/pdf/2611.08763v1), §3.1 p3) |
| update_strategy | Candidate Selection, Replanning, Local Patch | Directive applies scene patches; policy selects candidates; execution failure or changed directive triggers new action choice. ([source](https://arxiv.org/pdf/2611.08763v1), §3.2 p4; §3.4 p5; §3.6 p7) |
| verifier | Programmatic, Environment, Human | Validator gates operations, user must accept partial instructions, Unity reports action completion/failure. ([source](https://arxiv.org/pdf/2611.08763v1), §3.2 pp3–4; §3.6 p7) |
| feedback_assessment | Binary, Diagnosis | Five-state feasibility verdict; completed/failed action flags. ([source](https://arxiv.org/pdf/2611.08763v1), §3.2 p3; §3.6 p7) |
| feedback_observation | Structural Scene State, Runtime | Live objects/zones/reachability and execution outcome messages. ([source](https://arxiv.org/pdf/2611.08763v1), §3.3 p4; §3.6 p7) |
| memory_time | Short-Term Memory | Active directives retain lifetimes and resume after temporary overrides; action held until completion. ([source](https://arxiv.org/pdf/2611.08763v1), §3.2 p4; §3.6 p7) |
| memory_reach | Global Memory | Candidate generator and graph policy read all active directives every update across crowd. ([source](https://arxiv.org/pdf/2611.08763v1), §3.2 p4) |
| action_type | Structured Specification | JSON operation directives and selected action-target records. ([source](https://arxiv.org/pdf/2611.08763v1), §3.2 p4; §3.4 p5) |
| graphics_software | Agent-Adapted | Python policy process communicates with Unity scene client via WebSocket. ([source](https://arxiv.org/pdf/2611.08763v1), §3.6 pp6–7) |
| tools | Graphics Operations, Static Validator | Scene validator checks supported actions; Unity performs navigation/animation/interactions. ([source](https://arxiv.org/pdf/2611.08763v1), §3.2 p3; §3.6 p7) |
| resources | Documentation & Rules | Fixed supported operation vocabulary and nine-needs tier rules guide behavior. ([source](https://arxiv.org/pdf/2611.08763v1), §3.2–3.3 pp3–5) |
| representation | Dynamic State, Layouts | 2D scene geometry and time-varying character needs/actions/directives. ([source](https://arxiv.org/pdf/2611.08763v1), §3.3 p4; §3.6 p7) |

Events: [{"type": "first_submission", "value": "2026-11-05T22:18:10+00:00", "precision": "timestamp", "timezone": "UTC", "local_value": "2026-11-05T16:18:10-06:00", "primary_url": "https://arxiv.org/abs/2611.08763", "authority": "primary", "version": "v1", "evidence": "Canonical v1 history; December MIG conference date not treated as already published event.", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: ["Add/monitor non-foundation-policy training distinctions: GNN supervised distillation from scratch is not SFT or RL post-training.", "Replanning label covers reactive reselection here; explicit multi-step plan is not present."]

### [GREP: Grounding Generated Room Evaluation in Principles](https://arxiv.org/abs/2611.05802)
core | High | new_relative_to_snapshot
Application: Static / Scene, Datasets and Benchmarks; operations: Auditing
Principled, evidence-adaptive auditing reaches 13/15 agreement with human majority preferences; diagnostic feedback supports five-scene layout refinement beyond score-only feedback.
Scope: The inspection agent operates on a 3D graphics environment by choosing measurements and camera views, rendering additional observations and auditing scene defects. Auditing need not mutate object geometry.
Limits: Human comparison uses only six scenes and dependent pairwise samples, with unequal evidence access across evaluators. Judge may favor its own family. Discovery coverage is not exhaustive. Forced binary/default-valid judgments may hide missing evidence. Repeatability varies up to 7.3 score SD; refinement uses a different scoring protocol and discards incomplete attempts.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Not Applicable | Evaluation inspects a fixed submitted room without authoring it. ([source](https://arxiv.org/pdf/2611.05802v1), §3 p3) |
| input_form | 3D Representation | Assets, positions, orientations, scales and boundaries of generated rooms. ([source](https://arxiv.org/pdf/2611.05802v1), §3 p3) |
| output | Structured Specification | Structured per-check verdict/reason/evidence records and score reports. ([source](https://arxiv.org/pdf/2611.05802v1), §3.4 p5; A.5 p15) |
| model_type | VLM | GPT-5.6 Sol VLM inspects views and makes judgments. ([source](https://arxiv.org/pdf/2611.05802v1), §3.1 p3; §4.1 p5) |
| model_training | Not Reported | Model and settings specified, but adaptation status is not. ([source](https://arxiv.org/pdf/2611.05802v1), §4.1; Appendix C; training/fine-tun/off-the-shelf search) |
| planning | PO-2 | VLM instantiates scoped checks/observation goals from fixed types; fixed budgets govern camera scheduling. ([source](https://arxiv.org/pdf/2611.05802v1), A.2–A.4 pp14–15) |
| workflow | Graph-Structured | Different metric branches bypass/enter screen, acquisition and adjudication; groups share evidence. ([source](https://arxiv.org/pdf/2611.05802v1), Fig7 p13; Table4 p14) |
| update_strategy | Replanning, Candidate Selection | Missing evidence triggers new observation goals; camera candidates filtered and selected. ([source](https://arxiv.org/pdf/2611.05802v1), A.3–A.4 p15) |
| verifier | Self, Programmatic | Deterministic gate checks image availability; metric evaluator judges whether view answers the current question. ([source](https://arxiv.org/pdf/2611.05802v1), A.3–A.5 p15) |
| feedback_assessment | Binary, Diagnosis | Evidence sufficient/insufficient with unmet requirements, then request more views. ([source](https://arxiv.org/pdf/2611.05802v1), A.3–A.4 p15) |
| feedback_observation | Visual, Structural Scene State | Rendered views plus distances, angles, overlaps and clearance. ([source](https://arxiv.org/pdf/2611.05802v1), §3.3 pp4–5) |
| memory_time | Short-Term Memory | Acquired views retained in group evidence bank for subsequent checks. ([source](https://arxiv.org/pdf/2611.05802v1), A.3–A.4 p15) |
| memory_reach | Local Memory | Function checks share bank only inside object group; other metrics have own scopes. ([source](https://arxiv.org/pdf/2611.05802v1), Table4 p14; A.3 p15) |
| action_type | Tool/Function Call | Callable measure, view retrieval and render operations. ([source](https://arxiv.org/pdf/2611.05802v1), §3.3 pp4–5) |
| graphics_software | Agent-Adapted | Custom evidence acquisition wraps Blender EEVEE rendering. ([source](https://arxiv.org/pdf/2611.05802v1), C.3 p19) |
| tools | Graphics Operations, Static Validator | Camera rendering and deterministic geometry/contact/boundary checks. ([source](https://arxiv.org/pdf/2611.05802v1), §3.3 p4; A.5 p15) |
| resources | Assets, Documentation & Rules | Asset catalog supplies usable-side references/previews; predefined check requirements and tolerances guide inspection. ([source](https://arxiv.org/pdf/2611.05802v1), A.3 p15; Table4 p14) |
| representation | Geometry, Pixels | Mesh/transform geometry and rendered evidence frames. ([source](https://arxiv.org/pdf/2611.05802v1), §3 pp3–5) |

Events: [{"type": "first_submission", "value": "2026-11-04T01:19:12+00:00", "precision": "timestamp", "timezone": "UTC", "local_value": "2026-11-03T19:19:12-06:00", "primary_url": "https://arxiv.org/abs/2611.05802", "authority": "primary", "version": "v1", "evidence": "Canonical v1 submission history before cutoff.", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: ["Task taxonomy lacks an auditing task and output vocabulary lacks diagnostic reports; use Not Applicable task and explicitly derived Structured Specification output instead of claiming scene creation.", "Maintain output scores separately from evidence-sufficiency feedback."]

### [AnimWeb-Bench: Benchmarking Animated Webpage Code Generation from Videos](https://arxiv.org/abs/2611.09769)
core | High | new_relative_to_snapshot
Application: 2D Graphics, Dynamic / Animation and temporal scene, Datasets and Benchmarks; operations: Reconstruction
Separates static and animation fidelity on 124 real webpages; render feedback adds 4–7% on animation metrics beyond frame inspection.
Scope: Render-feedback coding agent actively edits HTML/CSS/JS controlling temporal visual composition, beyond generic website automation.
Limits: Small curated Awwwards set excludes interaction-triggered sequences. Evaluation depends on detection/tracking and matching heuristics. FI/RF interventions were developed from benchmark traces and are diagnostic, not held-out tuned-method claims. Proprietary agents and underspecified budgets limit reproduction. PDF contains unfilled venue/date placeholders.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Animation | Recover time-driven webpage motion, timing, easing and synchronization. ([source](https://arxiv.org/pdf/2611.09769v1), §2.1 p2) |
| input_form | Video, Image | Reference video and composite images of static assets in workspace. ([source](https://arxiv.org/pdf/2611.09769v1), §4.1 p6) |
| output | Program | Return one self-contained HTML file with inline CSS and JavaScript. ([source](https://arxiv.org/pdf/2611.09769v1), §2.1 p2; §4.1 p6) |
| model_type | VLM | Multimodal GPT-5.6 Sol inspects full-resolution frames. ([source](https://arxiv.org/pdf/2611.09769v1), §4.1 p6; §4.3 p8) |
| model_training | Not Reported | Provider defaults and reasoning effort reported; no adaptation statement. ([source](https://arxiv.org/pdf/2611.09769v1), §4.1 p6; full-PDF training/fine-tun search) |
| planning | PO-2 | Agent describes timed animation sequence before coding; fixed prompts require full-frame inspection and render feedback. ([source](https://arxiv.org/pdf/2611.09769v1), Fig8 p13) |
| workflow | Sequential | Record, extract frames, edit, repeat. ([source](https://arxiv.org/pdf/2611.09769v1), Fig8 p13) |
| update_strategy | Local Patch | edit index.html after comparing generated preview. ([source](https://arxiv.org/pdf/2611.09769v1), Fig8 lines11–14 p13) |
| verifier | Self | Codex compares own video to reference and revises code. ([source](https://arxiv.org/pdf/2611.09769v1), §4.3 p8; Fig8 p13) |
| feedback_assessment | Diagnosis | Timing/motion mismatches and failed montage command lead to edits/fallback. ([source](https://arxiv.org/pdf/2611.09769v1), Appendix F p13) |
| feedback_observation | Visual, Runtime | Own animation frames and command-not-found error are observed. ([source](https://arxiv.org/pdf/2611.09769v1), Fig8 p13) |
| memory_time | Short-Term Memory | Current index.html and generated comparison frames remain through multiple rounds. ([source](https://arxiv.org/pdf/2611.09769v1), Fig8 p13) |
| memory_reach | Local Memory | Single agent has isolated task workspace; outside workspace/network prohibited. ([source](https://arxiv.org/pdf/2611.09769v1), §4.1 p6) |
| action_type | Code/Script, Tool/Function Call | Writes/edits HTML and invokes ffmpeg/record.sh. ([source](https://arxiv.org/pdf/2611.09769v1), Fig8 p13) |
| graphics_software | Agent-Adapted | Added recording tool renders generated page to video for agent comparison. ([source](https://arxiv.org/pdf/2611.09769v1), §4.3 p8; Fig8 p13) |
| tools | Execution Utilities, Graphics Operations | Shell file operations, frame extraction and browser animation recording. ([source](https://arxiv.org/pdf/2611.09769v1), Fig8 p13) |
| resources | Assets, Documentation & Rules | Original page assets and tools/README.md recorder instructions. ([source](https://arxiv.org/pdf/2611.09769v1), §4.1 p6; Fig8 p13) |
| representation | Code, Layouts, Pixels | HTML/CSS/JS specifies DOM layouts and pixel animation previews. ([source](https://arxiv.org/pdf/2611.09769v1), §2.1 p2; Fig8 p13) |

Events: [{"type": "first_submission", "value": "2026-11-06T17:31:09+00:00", "precision": "timestamp", "timezone": "UTC", "local_value": "2026-11-06T11:31:09-06:00", "primary_url": "https://arxiv.org/abs/2611.09769", "authority": "primary", "version": "v1", "evidence": "Canonical history; PDF ACM 2018 and received/accepted dates are unfilled template artifacts, not publication evidence.", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: []

### [PCBRouteAgent: How Close Are LLM Agents to Becoming PCB Routing Engineers?](https://arxiv.org/abs/2611.08175)
core | High | new_relative_to_snapshot
Application: Static / CAD; operations: Generation, Editing
On 247 boards, planned native-engine routing improves clean-pass rates with approximately 131× fewer model calls than the same-Haiku interactive baseline.
Scope: The agent modifies geometric PCB layout in a native CAD environment, not just symbolic electronics reasoning; engineering CAD is included by the user scope.
Limits: D3-B includes unscored response-failure retries and guarded angle repair, not strict first-attempt comparison. Only ten large boards; six remain incomplete with Opus. No component ablation isolates LLM replanning from strong deterministic routing. Initial images remain fixed; text carries evolving state. Scope includes geometric EDA as engineering CAD, which may differ from a narrower mechanical-only survey.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Modeling | Construct copper geometry satisfying design rules. ([source](https://arxiv.org/pdf/2611.08175v1), §3.1 p5) |
| input_form | Image, Language | Planner receives board images and serialized textual electrical/geometric sidecar. ([source](https://arxiv.org/pdf/2611.08175v1), §3.2.1 p6) |
| output | Graphics Artifact | Routed traces/vias saved in native KiCad PCB file. ([source](https://arxiv.org/pdf/2611.08175v1), §3.1 p5; §3.3 p9) |
| model_type | VLM | Multimodal LLM consumes board views and text to produce guide patch. ([source](https://arxiv.org/pdf/2611.08175v1), §3.2.4 p7) |
| model_training | Not Reported | Prompt/API settings given; no controller training/adaptation statement. ([source](https://arxiv.org/pdf/2611.08175v1), §4 pp10–11; Appendix B; training/fine-tun search) |
| planning | PO-2 | MST/order/corridors initialized heuristically; model revises explicit guide topology and layer plan. ([source](https://arxiv.org/pdf/2611.08175v1), §3.2 pp6–8) |
| workflow | Graph-Structured | Nested connection tasks, recovery branches, conditional rollback and batched escalation to planner. ([source](https://arxiv.org/pdf/2611.08175v1), Algorithm1 p18) |
| update_strategy | Local Patch, Replanning, Rollback, Candidate Selection | Patch affected guide, replan corridors/layers, choose waypoint alternatives, restore checkpoints after failures. ([source](https://arxiv.org/pdf/2611.08175v1), §3.2.4–3.3 pp7–9) |
| verifier | Programmatic, Environment | Schema/ID checks gate patches and KiCad execution/connectivity checks gate routes. ([source](https://arxiv.org/pdf/2611.08175v1), §3.2.4 p8; §3.3 p9) |
| feedback_assessment | Binary, Diagnosis | Pass/fail plus blocker, reached position, invalid-reference and failed-route reasons. ([source](https://arxiv.org/pdf/2611.08175v1), §3.3.2 p9; B.2 p21) |
| feedback_observation | Structural Scene State, Runtime | Initial images fixed; evolving connectivity and execution feedback provide state changes. ([source](https://arxiv.org/pdf/2611.08175v1), §3.2.4 p7) |
| memory_time | Short-Term Memory | Previous guides, failed edge history and stable board checkpoints retained across rounds. ([source](https://arxiv.org/pdf/2611.08175v1), B.1.2 p20) |
| memory_reach | Global Memory | Planner and executor exchange revisioned guide and committed board/connectivity state. ([source](https://arxiv.org/pdf/2611.08175v1), §3.2.4 p7; Algorithm1 p18) |
| action_type | Structured Specification | Model outputs JSON GlobalGuidePatch, not copper-drawing code. ([source](https://arxiv.org/pdf/2611.08175v1), B.1 pp19–20) |
| graphics_software | Agent-Adapted | PCBWorld engine interface exposes native KiCad PNS to agent harness. ([source](https://arxiv.org/pdf/2611.08175v1), §3 p5) |
| tools | Graphics Operations, Solver Validator, Static Validator, Execution Utilities | PNS construction/walkaround/shove, A* detour, consistency validators and checkpoint operations. ([source](https://arxiv.org/pdf/2611.08175v1), §3.3 pp8–9) |
| resources | Documentation & Rules, Examples & Trajectories | Schemas, routing constraints and example patch shape inserted into prompts. ([source](https://arxiv.org/pdf/2611.08175v1), B.1–B.2 pp19–21) |
| representation | Layouts, Geometry, Pixels | Layerwise corridor layout, physical trace/via geometry and board images. ([source](https://arxiv.org/pdf/2611.08175v1), §3.1–3.2 pp5–7) |

Events: [{"type": "first_submission", "value": "2026-11-05T15:31:15+00:00", "precision": "timestamp", "timezone": "UTC", "local_value": "2026-11-05T09:31:15-06:00", "primary_url": "https://arxiv.org/abs/2611.08175", "authority": "primary", "version": "v1", "evidence": "Canonical v1 history.", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: ["Explicitly retain geometric EDA inclusion rationale; this is demonstrated CAD-state control, not a merely transferable electronics mechanism."]

### [CounterSketch: Physics-Grounded Counterfactual Reasoning for Sketch-to-Video Generation](https://arxiv.org/abs/2611.04244)
core | Medium | new_relative_to_snapshot
Application: 2D Graphics, Dynamic / Animation and temporal scene; operations: Generation, Editing
An 80-question counterfactual sketch benchmark and explicit physics-event pipeline improve text alignment and dynamic degree over direct VLM motion prediction under a fixed MoSketch renderer.
Scope: VLM intervention and event-chain decisions explicitly modify vector sketch scene state and govern constrained motion; semantic conflicts trigger local replanning. Control is fixed-harness rather than autonomous tool discovery.
Limits: Only 20 base scenes and 80 questions; comparisons largely measure video alignment, not physical accuracy directly. Ambiguous sketches and hidden mass/friction undermine grounding. Controller identity/training, repair budgets, semantic verifier and implementation are insufficiently documented. Non-rigid motion is future work.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Animation, Simulation | Constrained physical rollout supplies counterfactual animated motion. ([source](https://arxiv.org/pdf/2611.04244v1), §4.3 p6; §4.5 p7) |
| input_form | Image, Language | Sketch image S and natural-language counterfactual prompt. ([source](https://arxiv.org/pdf/2611.04244v1), §3 p4) |
| output | Structured Specification | Verified trajectories projected to per-frame motion bounding boxes for downstream video synthesis. ([source](https://arxiv.org/pdf/2611.04244v1), §4.5 p7) |
| model_type | VLM | VLM scene grounding and causal reasoning operate on sketch and prompt. ([source](https://arxiv.org/pdf/2611.04244v1), Fig3 p5; Fig4 p6) |
| model_training | Not Reported | Gemini 3.8 Flash named for baselines; selected planner adaptation not specified. ([source](https://arxiv.org/pdf/2611.04244v1), §5.2 p8; full-PDF training search) |
| planning | PO-2 | Explicit event chain contains affected objects, event type, conditions and updated graph; fixed compiler then rolls out constraints. ([source](https://arxiv.org/pdf/2611.04244v1), §4.2–4.3 pp5–6) |
| workflow | Graph-Structured | Verification branches to numerical repair or semantic replan then back into rollout. ([source](https://arxiv.org/pdf/2611.04244v1), Fig5 p7) |
| update_strategy | Local Patch, Replanning | Numerical violations adjust parameters/constraints; semantic conflicts refine event chain. ([source](https://arxiv.org/pdf/2611.04244v1), §4.4 p7) |
| verifier | Programmatic | Trajectory checks physical/geometric constraints and only accepts violation-reducing updates. ([source](https://arxiv.org/pdf/2611.04244v1), §4.4 p7) |
| feedback_assessment | Binary, Diagnosis | Per-constraint violation report; accept only improvements. ([source](https://arxiv.org/pdf/2611.04244v1), Fig3 p5; §4.4 p7) |
| feedback_observation | Structural Scene State | Trajectory states and geometric/physical violations inform repair. ([source](https://arxiv.org/pdf/2611.04244v1), §4.3–4.4 pp6–7) |
| memory_time | Not Reported | Scene states evolve, but model-call retention or explicit memory interface not described. ([source](https://arxiv.org/pdf/2611.04244v1), §4; full-PDF memory/implementation search) |
| memory_reach | Not Reported | No scope/access model for retained controller context. ([source](https://arxiv.org/pdf/2611.04244v1), §4; memory search) |
| action_type | Structured Specification | Intervention and event tuples modify objects, geometry and relations. ([source](https://arxiv.org/pdf/2611.04244v1), §4.2 p6) |
| graphics_software | Not Reported | Equations and MoSketch backbone stated, but agent-to-software adapter details not reported. ([source](https://arxiv.org/pdf/2611.04244v1), §4–5; implementation/library search) |
| tools | Solver Validator, Static Validator, Graphics Operations | Vector intervention, constrained rollout and trajectory checks. ([source](https://arxiv.org/pdf/2611.04244v1), §4.2–4.4 pp6–7) |
| resources | Not Reported | No accessed example bank, asset library or documentation retrieval specified. ([source](https://arxiv.org/pdf/2611.04244v1), §4–5; library/implementation search) |
| representation | Layouts, Dynamic State | Vector strokes/bounds and object motion trajectories. ([source](https://arxiv.org/pdf/2611.04244v1), §4.1–4.5 pp5–7) |

Events: [{"type": "first_submission", "value": "2026-11-03T03:27:35+00:00", "precision": "timestamp", "timezone": "UTC", "local_value": "2026-11-02T21:27:35-06:00", "primary_url": "https://arxiv.org/abs/2611.04244", "authority": "primary", "version": "v1", "evidence": "Canonical v1 history.", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: ["Preserve partially specified controller details even with demonstrated structured graphics actions; do not infer a fully autonomous tool agent."]

### [LongBanana: An Expert-Verified Benchmark for Long-Context Multi-Reference Image Synthesis](https://arxiv.org/abs/2611.06856)
core | High | new_relative_to_snapshot
Application: 2D Graphics, Datasets and Benchmarks; operations: Generation, Editing
Dense reference-binding benchmark with human-audited labels; OpenClaw+RPR improves average checklist score from 76.1 to 78.4, but workflow gains depend on harness and backend.
Scope: LongBanana-Gen orchestrator explicitly selects reference evidence, image-generation/editing calls and repairs based on observed drafts.
Limits: Only 90 tasks; costly annotation and model/tool-dependent evaluation. No video or 3D tasks. RPR lowers task pass rate for two harnesses and can over-revise temporal state. Reproduction commands, compute and API costs are missing; checklist release statements conflict with linked public project. Some figure model identifiers remain pending.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Modeling | Construct coherent static visual compositions from multiple entity/appearance references. ([source](https://arxiv.org/pdf/2611.06856v1), §2 p3; D.2 p36) |
| input_form | Language, Image | User instruction and roughly 32 reference images with distractors. ([source](https://arxiv.org/pdf/2611.06856v1), Figure18 p36) |
| output | Rendered Media | One final synthesized image. ([source](https://arxiv.org/pdf/2611.06856v1), §2.1 p3) |
| model_type | VLM | Sonnet agent observes references and draft images; generator separately makes pixels. ([source](https://arxiv.org/pdf/2611.06856v1), C.1 p33; Figure18 p36) |
| model_training | Not Reported | Shared model and versioned harnesses specified, not adaptation status. ([source](https://arxiv.org/pdf/2611.06856v1), C.1 p33; training/fine-tun search) |
| planning | PO-2 | Model decomposes subgoals and builds scene plan/prompt schedule within three fixed stages. ([source](https://arxiv.org/pdf/2611.06856v1), D.2 Figure18 p36) |
| workflow | Sequential | RPR is explicitly a serial workflow with repair/requery loop. ([source](https://arxiv.org/pdf/2611.06856v1), §1 p3; D.2 p36) |
| update_strategy | Local Patch, Replanning | Adjust prompts/schedule and repair missing content or wrong bindings while preserving satisfied constraints. ([source](https://arxiv.org/pdf/2611.06856v1), §4.3 p10; D.2 p36) |
| verifier | Self | Agent-directed draft review, not access to evaluation graph/checklist. ([source](https://arxiv.org/pdf/2611.06856v1), §4.1 p7; Figure18 p36) |
| feedback_assessment | Diagnosis | Detect missing content and wrong bindings then revise prompts. ([source](https://arxiv.org/pdf/2611.06856v1), Figure18 p36) |
| feedback_observation | Visual | Agent inspects generated drafts and reference evidence. ([source](https://arxiv.org/pdf/2611.06856v1), §4.1 p7) |
| memory_time | Short-Term Memory | Reference state, prompt schedule and revisions retained during synthesis. ([source](https://arxiv.org/pdf/2611.06856v1), §1 p3; Figure18 p36) |
| memory_reach | Local Memory | One shared orchestrator state across its serial stages. ([source](https://arxiv.org/pdf/2611.06856v1), C.1 p33; Figure18 p36) |
| action_type | Tool/Function Call | Reference browsing, generation, editing and file/prompt management tool calls. ([source](https://arxiv.org/pdf/2611.06856v1), C.1 p33) |
| graphics_software | Agent-Adapted | Harness wraps fixed image generator with explicit tool calls and maintained reference state. ([source](https://arxiv.org/pdf/2611.06856v1), §1 p3; C.1 p33) |
| tools | Perception models, Execution Utilities, Static Validator | Generation harness calls OCR/count/layout, image generation and file/prompt management tools. ([source](https://arxiv.org/pdf/2611.06856v1), C.1 p33) |
| resources | Assets | Reference inventory browsed/retrieved as synthesis evidence. ([source](https://arxiv.org/pdf/2611.06856v1), §4.1 p7) |
| representation | Pixels | Reference images and evolving draft/final images. ([source](https://arxiv.org/pdf/2611.06856v1), §4.1 p7; Figure18 p36) |

Events: [{"type": "first_submission", "value": "2026-11-04T18:11:56+00:00", "precision": "timestamp", "timezone": "UTC", "local_value": "2026-11-04T12:11:56-06:00", "primary_url": "https://arxiv.org/abs/2611.06856", "authority": "primary", "version": "v1", "evidence": "Official Atom v1 timestamp and canonical page; NeurIPS label does not establish separate publication event.", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: ["Static raster synthesis has no exact task label in frozen taxonomy; Modeling is a broad 2D composition mapping, not a claim of geometric output."]

### [VideoGen-Agent: Reinforcing Video Generation Agents](https://arxiv.org/abs/2609.24997)
core | High | new_relative_to_snapshot
Application: Dynamic / Animation and temporal scene, Dynamic / Physical simulation and effects; operations: Generation
Multitask learned tool use improves base generation from 56.5 to 75.6 on VABench; upgrading generators yields 86.1 without policy retraining.
Scope: Learned controller selects generation/verification tools and regenerates video segments from observations, with direct graphics output control.
Limits: Same VLM rubric is used for RL reward and final evaluation. Specialized procedural judge agreement is only 72%. Fixed-workflow comparison is not generation-call matched; unseen-combination gain over composed workflow is only 0.8 points. Physics limited to planar collisions/drops; projected momentum checks are not calibrated 3D conservation. Tool failures are retried, affecting cost/robustness interpretation.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Animation, Simulation | Generate motion/multishot videos; collision/drop branch specifies physical bodies and computes motion. ([source](https://arxiv.org/pdf/2609.24997v4), §2.1 pp3–4; B.4 p20) |
| input_form | Language | User text prompt initiates six-task policy. ([source](https://arxiv.org/pdf/2609.24997v4), §2.1 p3) |
| output | Rendered Media | Return latest complete video sequence. ([source](https://arxiv.org/pdf/2609.24997v4), Algorithm1 p15) |
| model_type | VLM | Qwen3-VL-8B-Instruct shared multimodal policy. ([source](https://arxiv.org/pdf/2609.24997v4), §3.1 p6) |
| model_training | Supervised Fine-Tuning, RL Post-Training | 16K teacher trajectories SFT then 8K prompt GRPO. ([source](https://arxiv.org/pdf/2609.24997v4), §2.3–2.4 pp5–6) |
| planning | PO-2 | Prompt supplies reference workflows and hard tool constraints; policy composes calls and parses ordered shot plans adaptively. ([source](https://arxiv.org/pdf/2609.24997v4), B.3 pp19–20) |
| workflow | Sequential | Exactly one tool call per turn, wait for response; multi-shot segments executed in order. ([source](https://arxiv.org/pdf/2609.24997v4), B.3 p16) |
| update_strategy | Regeneration | Every regeneration replaces prior segment, without ranking/reverting older candidates. ([source](https://arxiv.org/pdf/2609.24997v4), B.1 p15; B.3 p17) |
| verifier | Self, Programmatic | Detection/depth measurements inform policy acceptance; environment checks missing segments and invalid calls. ([source](https://arxiv.org/pdf/2609.24997v4), B.1–B.2 pp15–16) |
| feedback_assessment | Binary, Score, Diagnosis | Found flags, detection ratio/coverage reward and missing/ambiguous object status govern regeneration. ([source](https://arxiv.org/pdf/2609.24997v4), B.2 p16; B.3 pp18–19) |
| feedback_observation | Structural Scene State, Runtime | Bounding boxes, subject depth ordering and tool errors retained as observations. ([source](https://arxiv.org/pdf/2609.24997v4), B.1–B.3 pp15–19) |
| memory_time | Short-Term Memory | Ht appends every action/output/error; current segment map persists until final assembly. ([source](https://arxiv.org/pdf/2609.24997v4), Algorithm1 p15) |
| memory_reach | Local Memory | One policy owns interaction history and current sequence. ([source](https://arxiv.org/pdf/2609.24997v4), §2.1 p3; Algorithm1 p15) |
| action_type | Tool/Function Call | JSON named-tool calls with typed arguments. ([source](https://arxiv.org/pdf/2609.24997v4), B.3 pp16–20) |
| graphics_software | Agent-Adapted | Common interface wraps multiple generators, verifier models and simulator. ([source](https://arxiv.org/pdf/2609.24997v4), §2.1 p4; Table2 p7) |
| tools | Perception models, Solver Validator, Execution Utilities | Video generators/detection/depth, rigid simulator, frame extraction and sequence assembly. ([source](https://arxiv.org/pdf/2609.24997v4), Table2 p7; B.4 p20) |
| resources | Assets, Documentation & Rules, Examples & Trajectories | Retrieved reference images and factual descriptions, tool schemas and example workflow patterns. ([source](https://arxiv.org/pdf/2609.24997v4), B.3 pp17–20) |
| representation | Pixels, Dynamic State | Video/frame pixels, optical flow and simulated body positions/velocities. ([source](https://arxiv.org/pdf/2609.24997v4), B.3–B.4 pp17–23) |

Events: [{"type": "first_submission", "value": "2026-09-21T17:58:56+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2609.24997", "authority": "primary", "version": "v1", "evidence": "Canonical history.", "prior_event_status": "not_seen_in_supplied_history"}, {"type": "revision", "value": "2026-11-06T08:24:41+00:00", "precision": "timestamp", "timezone": "UTC", "local_value": "2026-11-06T02:24:41-06:00", "primary_url": "https://arxiv.org/abs/2609.24997", "authority": "primary", "version": "v4", "evidence": "Official updated timestamp and canonical history; latest before frozen cutoff, seven-day revision catch-up.", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: ["Returned detector coverage reward is inference feedback Score; terminal Gemini reward is training/final evaluation only.", "Latest-only retention explicitly rules out Candidate Selection and Rollback for generated videos."]

### [An Agentic Framework for Quality-Aware and Scenario-Adaptive Image Compression](https://arxiv.org/abs/2611.04960)
core | High | new_relative_to_snapshot
Application: 2D Graphics; operations: Editing
Training-free black-box codec adaptation improves rate-quality curves across clean, noise and blur settings, including 28.96% matched-LPIPS bitrate savings over VVC on clean Kodak.
Scope: VLM decisions directly modify raster artifacts through restoration selection, regional quality allocation and crop/recomposition, not merely abstract compression policy.
Limits: Only two codecs and two synthetic degradations are evaluated. Latency, number of candidates and iteration ceilings are not fully quantified. Pseudo-reference selection may bias quality optimization. No standalone limitations section; these are evaluation/reporting limits. Restoration/compression sits outside the four task labels despite explicit graphics-artifact actions.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Not Applicable | Task is compression and restoration, not modeling, animation, simulation or visualization. ([source](https://arxiv.org/pdf/2611.04960v2), §III-A–B pp3–4) |
| input_form | Image, Language | Image and user instruction for compression scenario/target. ([source](https://arxiv.org/pdf/2611.04960v2), §III-B p4) |
| output | Graphics Artifact, Rendered Media | Aggregate coded representation with metadata plus final reconstructed image. ([source](https://arxiv.org/pdf/2611.04960v2), §III-A Eq3 p4; Eq8 p8) |
| model_type | VLM | Qwen3-VL supports interpretation, planning, tool calls and feedback refinement across roles. ([source](https://arxiv.org/pdf/2611.04960v2), §III-E p10) |
| model_training | Off-the-Shelf | Training-free framework coordinates pretrained models without additional training. ([source](https://arxiv.org/pdf/2611.04960v2), §II pp3; §III-E p10) |
| planning | PO-2 | Model schedules restoration subtasks and candidate QC/downsample plans within fixed four-role process. ([source](https://arxiv.org/pdf/2611.04960v2), §III-C–D pp5–8) |
| workflow | Sequential | Perception→pre-restoration→coding→post-restoration with local iterative loops. ([source](https://arxiv.org/pdf/2611.04960v2), Fig1 p4) |
| update_strategy | Replanning, Candidate Selection, Local Patch | Reschedule unsuccessful plans, retain best candidate and adjust ROI/background controls. ([source](https://arxiv.org/pdf/2611.04960v2), §III-C–D pp5–8) |
| verifier | Critic, Programmatic, Self | DepictQA diagnoses distortions; SGQR metrics gate candidates; planner reflects on unmet targets. ([source](https://arxiv.org/pdf/2611.04960v2), §III-B–E pp4–10) |
| feedback_assessment | Binary, Score, Diagnosis | Scores select candidates; target satisfaction gates updates; feedback explains bitrate/quality deficit. ([source](https://arxiv.org/pdf/2611.04960v2), Fig2 p5; Eq5,9 pp5,8) |
| feedback_observation | Visual, Structural Scene State | VLM reassesses decoded image; ROI locations, bitrate and measured quality enter reflection. ([source](https://arxiv.org/pdf/2611.04960v2), §III-C p6; §III-D pp6–8) |
| memory_time | Short-Term Memory | Current and best image/control candidates retained across iterations. ([source](https://arxiv.org/pdf/2611.04960v2), §III-C–D pp5–8) |
| memory_reach | Local Memory | Each stage maintains candidate set and passes selected image/configuration onward. ([source](https://arxiv.org/pdf/2611.04960v2), §III-B–D pp4–8) |
| action_type | Tool/Function Call, Structured Specification | Candidate plans specify ROI/QC/downsample decisions; agents invoke target codec/restoration tools. ([source](https://arxiv.org/pdf/2611.04960v2), §III-D–E pp7–10) |
| graphics_software | Agent-Adapted | Codec-agnostic agent layer wraps native QC interfaces without changing codec internals. ([source](https://arxiv.org/pdf/2611.04960v2), §III-A p3; §III-D p7) |
| tools | Perception models, Graphics Operations, Static Validator | Restoration/detection/IQA models, crop/downsample/aggregate operations, bitrate/quality checks. ([source](https://arxiv.org/pdf/2611.04960v2), §III-D–E pp7–10) |
| resources | Documentation & Rules | Codec QC range/meaning provided as prior knowledge. ([source](https://arxiv.org/pdf/2611.04960v2), Fig2 p5; §IV-B p10) |
| representation | Pixels, Layouts | Image crops/reconstruction and ROI coordinate/scaling metadata. ([source](https://arxiv.org/pdf/2611.04960v2), Eq7–8 pp7–8) |

Events: [{"type": "first_submission", "value": "2026-11-03T14:19:39+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2611.04960", "authority": "primary", "version": "v1", "evidence": "Official Atom published timestamp.", "prior_event_status": "not_seen_in_supplied_history"}, {"type": "revision", "value": "2026-11-06T03:13:32+00:00", "precision": "timestamp", "timezone": "UTC", "local_value": "2026-11-05T21:13:32-06:00", "primary_url": "https://arxiv.org/abs/2611.04960", "authority": "primary", "version": "v2", "evidence": "Official updated timestamp and canonical latest-version history; before cutoff.", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: ["Add/monitor a raster processing task label; direct editing scope should not force restoration into Modeling."]

### [Seeing Beyond the Next Step: World-Model-Guided Human-Like Navigation in Multi-Agent Scenes](https://arxiv.org/abs/2611.07730)
core | High | new_relative_to_snapshot
Application: Dynamic / Animation and temporal scene; operations: Generation
Distills two consequence predictors into a fast visual policy: 65 ms decisions recover most online-planner quality while improving crowd motion realism over reactive baselines.
Scope: Paper explicitly treats navigation as crowd-behavior graphics, demonstrating VLM policy actions controlling animated pedestrians in Unity and evaluating perceived motion realism; not merely downstream robot control.
Limits: Fixed 100-anchor vocabulary and short-horizon oracles cannot capture rare motion or delayed negotiation. Unit-weighted score lacks explicit conflict arbitration. All closed-loop evaluation uses Unity reconstructions with nonredistributable commercial assets; no real robot validation. Twenty-person study and five scenes limit generalization.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Animation | Crowd-behavior simulation assessed for motion quality, naturalness and smoothness. ([source](https://arxiv.org/pdf/2611.07730v1), §2 p2; Appendix G pp21–22) |
| input_form | Language, Image | Third-person RGB plus formatted text goals/current state. ([source](https://arxiv.org/pdf/2611.07730v1), Appendix K pp24–25) |
| output | Structured Specification | One integer indexing executable anchor vocabulary. ([source](https://arxiv.org/pdf/2611.07730v1), Appendix K p25) |
| model_type | VLM | Qwen3-VL-2B-Instruct backbone with LoRA. ([source](https://arxiv.org/pdf/2611.07730v1), Appendix A p15) |
| model_training | Supervised Fine-Tuning, RL Post-Training | Supervised anchor classification followed by GRPO policy refinement. ([source](https://arxiv.org/pdf/2611.07730v1), Appendix A p15) |
| planning | Not Applicable | World models, candidate grouping and scoring removed; one forward action-selection pass. ([source](https://arxiv.org/pdf/2611.07730v1), §3.3 p6; Appendix J p24) |
| workflow | Sequential | Observe, classify anchor, execute, observe next state. ([source](https://arxiv.org/pdf/2611.07730v1), §3 pp3–6) |
| update_strategy | Candidate Selection | Categorical policy selects next motion from fixed vocabulary at each observation. ([source](https://arxiv.org/pdf/2611.07730v1), §3.3 p6) |
| verifier | Not Applicable | No world-model prediction or consequence scoring at inference. ([source](https://arxiv.org/pdf/2611.07730v1), §3.3 p6; Appendix J p24) |
| feedback_assessment | Not Applicable | Score function discarded for deployment. ([source](https://arxiv.org/pdf/2611.07730v1), §3.3 p6) |
| feedback_observation | Visual, Structural Scene State | RGB plus current/previous velocity, relative pedestrians/objects and goal. ([source](https://arxiv.org/pdf/2611.07730v1), Eq1 pp3–4) |
| memory_time | Short-Term Memory | Previous ego velocity retained in next-step input. ([source](https://arxiv.org/pdf/2611.07730v1), Eq1 p3; Appendix K p25) |
| memory_reach | Local Memory | Observation/state are expressed in each controlled agent's ego frame. ([source](https://arxiv.org/pdf/2611.07730v1), Eq1 pp3–4) |
| action_type | Structured Specification | Output constrained to one anchor index. ([source](https://arxiv.org/pdf/2611.07730v1), Appendix K p25) |
| graphics_software | Agent-Adapted | Unity reconstructed scenes expose state and execute anchor-classifier output. ([source](https://arxiv.org/pdf/2611.07730v1), §4.1 p6; Appendix K p24) |
| tools | Graphics Operations | Simulation executes selected motion primitive in Unity. ([source](https://arxiv.org/pdf/2611.07730v1), §3.3 p6; §4.1 p6) |
| resources | Examples & Trajectories, Documentation & Rules | 100 trajectory-derived motion anchors and fixed coordinate/action prompt contract. ([source](https://arxiv.org/pdf/2611.07730v1), §3.1 p4; Appendix K pp24–25) |
| representation | Dynamic State, Pixels | Animated motion state and third-person RGB observations. ([source](https://arxiv.org/pdf/2611.07730v1), Eq1 p3; §3.1 p4) |

Events: [{"type": "first_submission", "value": "2026-11-05T09:42:12+00:00", "precision": "timestamp", "timezone": "UTC", "local_value": "2026-11-05T03:42:12-06:00", "primary_url": "https://arxiv.org/abs/2611.07730", "authority": "primary", "version": "v1", "evidence": "Official Atom published timestamp; canonical v1.", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: ["Training-time world-model verification must remain separate from deployed reactive control; method is core through crowd animation, not merely agent terminology."]

## date_unresolved (0)

## unresolved (2)

### [HiLSVA: Design and Evaluation of a Human-in-the-Loop Agentic System for Scientific Visualization](https://arxiv.org/abs/2606.26614)
unresolved | Low | new_relative_to_snapshot
Application: 2D Graphics; operations: Generation
Primary abstract describes agent-assisted scientific visualization; full method classification deferred.
Scope: Official primary abstract demonstrates plausible visualization-agent activity but full PDF not reached. Outside date window and not one of three reserved pending backlog slots. Historical exclusion of 2604.27996 is not adopted as ground truth; contradiction remains queued.
Limits: Unread primary PDF; taxonomy placeholders express unresolved evidence, not absence of mechanism.

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

Events: [{"type": "first_submission", "value": "2026-06-25T05:19:07+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2606.26614", "authority": "primary", "version": "v1", "evidence": "Official Atom metadata; old event outside seven-day window.", "prior_event_status": "not_seen_in_supplied_history"}, {"type": "revision", "value": "2026-07-16T18:32:05+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2606.26614", "authority": "primary", "version": "v2", "evidence": "Official latest update predates target window.", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: []

### [Exploring LLM Agent Designs and Interaction Modalities for Scientific Visualization](https://arxiv.org/abs/2604.27996)
unresolved | Low | new_relative_to_snapshot
Application: 2D Graphics; operations: Generation
Primary abstract describes agent-assisted scientific visualization; full method classification deferred.
Scope: Official primary abstract demonstrates plausible visualization-agent activity but full PDF not reached. Outside date window and not one of three reserved pending backlog slots. Historical exclusion of 2604.27996 is not adopted as ground truth; contradiction remains queued.
Limits: Unread primary PDF; taxonomy placeholders express unresolved evidence, not absence of mechanism.

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

Events: [{"type": "first_submission", "value": "2026-04-30T15:22:28+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2604.27996", "authority": "primary", "version": "v1", "evidence": "Official Atom metadata; old event outside seven-day window.", "prior_event_status": "already_seen"}, {"type": "revision", "value": "2026-06-26T20:31:32+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2604.27996", "authority": "primary", "version": "v3", "evidence": "Official latest update predates target window.", "prior_event_status": "already_seen"}]
Taxonomy deltas: []

## excluded (0)

## Application index
| Application | Papers |
|---|---|
| 2D Graphics | [Reels-RSI: Program-Level Self-Improvement for Code-Rendered Explainer Videos](https://arxiv.org/abs/2610.14495) [late_discovery]; [ManimCode: Learning Visual Self-Correction for Educational Animation](https://arxiv.org/abs/2611.08294) [late_discovery]; [AnimWeb-Bench: Benchmarking Animated Webpage Code Generation from Videos](https://arxiv.org/abs/2611.09769) [late_discovery]; [CounterSketch: Physics-Grounded Counterfactual Reasoning for Sketch-to-Video Generation](https://arxiv.org/abs/2611.04244) [late_discovery]; [LongBanana: An Expert-Verified Benchmark for Long-Context Multi-Reference Image Synthesis](https://arxiv.org/abs/2611.06856) [late_discovery]; [An Agentic Framework for Quality-Aware and Scenario-Adaptive Image Compression](https://arxiv.org/abs/2611.04960) [late_discovery]; [HiLSVA: Design and Evaluation of a Human-in-the-Loop Agentic System for Scientific Visualization](https://arxiv.org/abs/2606.26614) [unresolved]; [Exploring LLM Agent Designs and Interaction Modalities for Scientific Visualization](https://arxiv.org/abs/2604.27996) [unresolved] |
| Static / Object | [Frontier3DBench: Benchmarking Coding Agents for 3D Creation across Objects, Scenes, and Interactive Open Worlds](https://arxiv.org/abs/2611.09017) [late_discovery]; [GATOR: Generative and Agentic 3D Object Reconstruction From Casual Images](https://arxiv.org/abs/2610.11215) [late_discovery] |
| Static / CAD | [Parametric CAD Bench v3: Evaluating Agentic Parametric CAD Authoring from Text and Engineering Drawings](https://arxiv.org/abs/2611.02659) [late_discovery]; [CADFather: Autonomous CAD Reconstruction through Coordinated Tool Use](https://arxiv.org/abs/2610.09127) [late_discovery]; [PCBRouteAgent: How Close Are LLM Agents to Becoming PCB Routing Engineers?](https://arxiv.org/abs/2611.08175) [late_discovery] |
| Static / Scene | [Frontier3DBench: Benchmarking Coding Agents for 3D Creation across Objects, Scenes, and Interactive Open Worlds](https://arxiv.org/abs/2611.09017) [late_discovery]; [GREP: Grounding Generated Room Evaluation in Principles](https://arxiv.org/abs/2611.05802) [late_discovery] |
| Dynamic / Articulated assets | None verified in this run |
| Dynamic / Animation and temporal scene | [Video-Coder: Reinforcing Agentic Coding for Video Generation](https://arxiv.org/abs/2611.09894) [late_discovery]; [Reels-RSI: Program-Level Self-Improvement for Code-Rendered Explainer Videos](https://arxiv.org/abs/2610.14495) [late_discovery]; [ManimCode: Learning Visual Self-Correction for Educational Animation](https://arxiv.org/abs/2611.08294) [late_discovery]; [CrowdDirector: Runtime Orchestration of Crowd Simulation through Natural-Language Directives](https://arxiv.org/abs/2611.08763) [late_discovery]; [AnimWeb-Bench: Benchmarking Animated Webpage Code Generation from Videos](https://arxiv.org/abs/2611.09769) [late_discovery]; [CounterSketch: Physics-Grounded Counterfactual Reasoning for Sketch-to-Video Generation](https://arxiv.org/abs/2611.04244) [late_discovery]; [VideoGen-Agent: Reinforcing Video Generation Agents](https://arxiv.org/abs/2609.24997) [late_discovery]; [Seeing Beyond the Next Step: World-Model-Guided Human-Like Navigation in Multi-Agent Scenes](https://arxiv.org/abs/2611.07730) [late_discovery] |
| Dynamic / Physical simulation and effects | [VideoGen-Agent: Reinforcing Video Generation Agents](https://arxiv.org/abs/2609.24997) [late_discovery] |
| Datasets and Benchmarks | [Frontier3DBench: Benchmarking Coding Agents for 3D Creation across Objects, Scenes, and Interactive Open Worlds](https://arxiv.org/abs/2611.09017) [late_discovery]; [Parametric CAD Bench v3: Evaluating Agentic Parametric CAD Authoring from Text and Engineering Drawings](https://arxiv.org/abs/2611.02659) [late_discovery]; [GREP: Grounding Generated Room Evaluation in Principles](https://arxiv.org/abs/2611.05802) [late_discovery]; [AnimWeb-Bench: Benchmarking Animated Webpage Code Generation from Videos](https://arxiv.org/abs/2611.09769) [late_discovery]; [LongBanana: An Expert-Verified Benchmark for Long-Context Multi-Reference Image Synthesis](https://arxiv.org/abs/2611.06856) [late_discovery] |
| Cross-category | None verified in this run |

## Source ledger
| Source | Status | Checked pages / queries | Limitations |
|---|---|---|---|
| arxiv | partial | [{"query_or_url": "https://arxiv.org/list/cs.GR/new?skip=0&show=100", "checked_at": "2026-11-09T19:50:53.124406+00:00", "outcome": "8 entries; observed pagination complete=True; unvisited=[]; errors=[]"}, {"query_or_url": "https://arxiv.org/list/cs.GR/recent?skip=0&show=100", "checked_at": "2026-11-09T19:50:54.901321+00:00", "outcome": "46 entries; observed pagination complete=True; unvisited=[]; errors=[]"}, {"query_or_url": "https://arxiv.org/list/cs.CV/new?skip=0&show=100", "checked_at": "2026-11-09T19:50:55.233106+00:00", "outcome": "100 entries; observed pagination complete=True; unvisited=[]; errors=[]"}, {"query_or_url": "https://arxiv.org/list/cs.CV/new?skip=0&show=2000", "checked_at": "2026-11-09T19:50:55.446289+00:00", "outcome": "210 entries; observed pagination complete=True; unvisited=[]; errors=[]"}, {"query_or_url": "https://arxiv.org/list/cs.CV/recent?skip=0&show=100", "checked_at": "2026-11-09T19:50:55.565704+00:00", "outcome": "100 entries; observed pagination complete=True; unvisited=[]; errors=[]"}, {"query_or_url": "https://arxiv.org/list/cs.CV/recent?skip=0&show=2000", "checked_at": "2026-11-09T19:50:56.517336+00:00", "outcome": "958 entries; observed pagination complete=True; unvisited=[]; errors=[]"}, {"query_or_url": "https://export.arxiv.org/api/query?id_list=2306.13275%2C2310.07801%2C2410.05557%2C2412.01203%2C2412.12737%2C2505.24030%2C2506.09661%2C2507.09608%2C2510.02789%2C2510.16822%2C2511.03212%2C2511.18127%2C2512.02458%2C2512.07976%2C2512.18563%2C2601.02126%2C2602.04908%2C2602.17310%2C2602.23903%2C2603.02337%2C2603.02865%2C2603.04399%2C2603.23975%2C2604.03203%2C2604.08410%2C2604.08711%2C2604.17748%2C2605.00722%2C2605.05026%2C2605.09196%2C2605.09319%2C2605.10180%2C2605.11651%2C2605.12678%2C2605.16396%2C2605.16732%2C2605.16981%2C2605.18190%2C2605.20079%2C2605.20479%2C2605.20496%2C2605.24371%2C2605.28137%2C2605.31557%2C2606.10147%2C2606.15104%2C2606.17241%2C2606.25478%2C2606.30058%2C2607.05319%2C2607.13460%2C2607.19120%2C2607.24409%2C2607.24852%2C2608.13660%2C2608.15058%2C2609.00525%2C2609.00634%2C2609.03080%2C2609.24997%2C2609.31780%2C2609.38377%2C2610.02946%2C2610.12407%2C2610.13549%2C2610.15660%2C2610.18030%2C2610.19683%2C2610.20585%2C2610.22457%2C2610.23287%2C2610.26165%2C2610.30320%2C2610.31282%2C2610.33798%2C2610.33877%2C2610.34855%2C2610.39701%2C2610.40702%2C2610.42111%2C2611.00003%2C2611.00004%2C2611.00017%2C2611.00020%2C2611.00022%2C2611.00023%2C2611.00024%2C2611.00025%2C2611.00026%2C2611.00027%2C2611.00028%2C2611.00029%2C2611.00031%2C2611.00032%2C2611.00033%2C2611.00034%2C2611.00035%2C2611.00036%2C2611.00037%2C2611.00038&max_results=100", "checked_at": "2026-11-09T19:51:02.297660+00:00", "outcome": "Batch identity/abstract/published/updated provenance preserved; intermediate versions not inferred."}, {"query_or_url": "https://export.arxiv.org/api/query?id_list=2611.00039%2C2611.00040%2C2611.00041%2C2611.00042%2C2611.00043%2C2611.00044%2C2611.00045%2C2611.00046%2C2611.00047%2C2611.00048%2C2611.00049%2C2611.00050%2C2611.00053%2C2611.00054%2C2611.00055%2C2611.00056%2C2611.00058%2C2611.00059%2C2611.00061%2C2611.00062%2C2611.00063%2C2611.00064%2C2611.00065%2C2611.00066%2C2611.00067%2C2611.00069%2C2611.00071%2C2611.00072%2C2611.00073%2C2611.00074%2C2611.00076%2C2611.00077%2C2611.00078%2C2611.00079%2C2611.00080%2C2611.00081%2C2611.00084%2C2611.00091%2C2611.00092%2C2611.00097%2C2611.00099%2C2611.00102%2C2611.00105%2C2611.00107%2C2611.00110%2C2611.00111%2C2611.00113%2C2611.00114%2C2611.00120%2C2611.00122%2C2611.00140%2C2611.00150%2C2611.00151%2C2611.00157%2C2611.00175%2C2611.00177%2C2611.00179%2C2611.00180%2C2611.00181%2C2611.00184%2C2611.00191%2C2611.00192%2C2611.00227%2C2611.00238%2C2611.00245%2C2611.00247%2C2611.00253%2C2611.00288%2C2611.00293%2C2611.00328%2C2611.00351%2C2611.00367%2C2611.00371%2C2611.00375%2C2611.00383%2C2611.00396%2C2611.00406%2C2611.00423%2C2611.00427%2C2611.00430%2C2611.00458%2C2611.00478%2C2611.00482%2C2611.00507%2C2611.00523%2C2611.00527%2C2611.00551%2C2611.00556%2C2611.00566%2C2611.00608%2C2611.00634%2C2611.00653%2C2611.00658%2C2611.00671%2C2611.00676%2C2611.00681%2C2611.00683%2C2611.00684%2C2611.00699%2C2611.00704&max_results=100", "checked_at": "2026-11-09T19:51:05.592994+00:00", "outcome": "Batch identity/abstract/published/updated provenance preserved; intermediate versions not inferred."}, {"query_or_url": "https://export.arxiv.org/api/query?id_list=2611.00715%2C2611.00721%2C2611.00722%2C2611.00756%2C2611.00758%2C2611.00763%2C2611.00768%2C2611.00769%2C2611.00780%2C2611.00784%2C2611.00785%2C2611.00791%2C2611.00794%2C2611.00804%2C2611.00810%2C2611.00819%2C2611.00823%2C2611.00828%2C2611.00833%2C2611.00843%2C2611.00848%2C2611.00859%2C2611.00892%2C2611.00899%2C2611.00908%2C2611.00926%2C2611.00937%2C2611.00953%2C2611.00963%2C2611.00974%2C2611.01018%2C2611.01048%2C2611.01050%2C2611.01074%2C2611.01078%2C2611.01084%2C2611.01095%2C2611.01120%2C2611.01125%2C2611.01141%2C2611.01162%2C2611.01165%2C2611.01215%2C2611.01222%2C2611.01229%2C2611.01230%2C2611.01252%2C2611.01263%2C2611.01283%2C2611.01295%2C2611.01372%2C2611.01391%2C2611.01396%2C2611.01400%2C2611.01414%2C2611.01438%2C2611.01457%2C2611.01460%2C2611.01463%2C2611.01466%2C2611.01467%2C2611.01511%2C2611.01513%2C2611.01517%2C2611.01529%2C2611.01534%2C2611.01536%2C2611.01537%2C2611.01541%2C2611.01543%2C2611.01548%2C2611.01550%2C2611.01551%2C2611.01558%2C2611.01573%2C2611.01578%2C2611.01600%2C2611.01601%2C2611.01605%2C2611.01607%2C2611.01615%2C2611.01617%2C2611.01626%2C2611.01627%2C2611.01631%2C2611.01635%2C2611.01645%2C2611.01648%2C2611.01663%2C2611.01675%2C2611.01676%2C2611.01682%2C2611.01684%2C2611.01688%2C2611.01696%2C2611.01705%2C2611.01730%2C2611.01736%2C2611.01759%2C2611.01765&max_results=100", "checked_at": "2026-11-09T19:51:09.212048+00:00", "outcome": "Batch identity/abstract/published/updated provenance preserved; intermediate versions not inferred."}, {"query_or_url": "https://export.arxiv.org/api/query?id_list=2611.01783%2C2611.01790%2C2611.01791%2C2611.01815%2C2611.01822%2C2611.01823%2C2611.01846%2C2611.01850%2C2611.01858%2C2611.01860%2C2611.01888%2C2611.01900%2C2611.01902%2C2611.01907%2C2611.01913%2C2611.01921%2C2611.01934%2C2611.01937%2C2611.01939%2C2611.01958%2C2611.01960%2C2611.01962%2C2611.01970%2C2611.01974%2C2611.01978%2C2611.01982%2C2611.01990%2C2611.01992%2C2611.02008%2C2611.02026%2C2611.02034%2C2611.02037%2C2611.02044%2C2611.02051%2C2611.02053%2C2611.02056%2C2611.02076%2C2611.02096%2C2611.02101%2C2611.02114%2C2611.02119%2C2611.02147%2C2611.02197%2C2611.02203%2C2611.02204%2C2611.02211%2C2611.02245%2C2611.02284%2C2611.02305%2C2611.02306%2C2611.02324%2C2611.02327%2C2611.02341%2C2611.02356%2C2611.02363%2C2611.02364%2C2611.02366%2C2611.02393%2C2611.02405%2C2611.02419%2C2611.02433%2C2611.02437%2C2611.02474%2C2611.02488%2C2611.02499%2C2611.02505%2C2611.02506%2C2611.02512%2C2611.02519%2C2611.02526%2C2611.02540%2C2611.02551%2C2611.02568%2C2611.02578%2C2611.02581%2C2611.02593%2C2611.02599%2C2611.02603%2C2611.02625%2C2611.02631%2C2611.02648%2C2611.02649%2C2611.02651%2C2611.02654%2C2611.02658%2C2611.02659%2C2611.02661%2C2611.02671%2C2611.02685%2C2611.02686%2C2611.02690%2C2611.02695%2C2611.02726%2C2611.02737%2C2611.02744%2C2611.02751%2C2611.02756%2C2611.02759%2C2611.02767%2C2611.02769&max_results=100", "checked_at": "2026-11-09T19:52:24.963629+00:00", "outcome": "Batch identity/abstract/published/updated provenance preserved; intermediate versions not inferred."}, {"query_or_url": "https://export.arxiv.org/api/query?id_list=2611.02775%2C2611.02776%2C2611.02780%2C2611.02782%2C2611.02786%2C2611.02803%2C2611.02822%2C2611.02844%2C2611.02853%2C2611.02854%2C2611.02857%2C2611.02862%2C2611.02877%2C2611.02897%2C2611.02902%2C2611.02921%2C2611.02929%2C2611.02931%2C2611.02941%2C2611.02952%2C2611.02964%2C2611.02995%2C2611.03007%2C2611.03017%2C2611.03023%2C2611.03027%2C2611.03033%2C2611.03042%2C2611.03043%2C2611.03062%2C2611.03067%2C2611.03069%2C2611.03078%2C2611.03080%2C2611.03087%2C2611.03097%2C2611.03098%2C2611.03109%2C2611.03114%2C2611.03120%2C2611.03125%2C2611.03132%2C2611.03136%2C2611.03140%2C2611.03143%2C2611.03189%2C2611.03228%2C2611.03229%2C2611.03232%2C2611.03245%2C2611.03247%2C2611.03283%2C2611.03285%2C2611.03339%2C2611.03360%2C2611.03370%2C2611.03371%2C2611.03377%2C2611.03382%2C2611.03390%2C2611.03393%2C2611.03394%2C2611.03399%2C2611.03404%2C2611.03421%2C2611.03430%2C2611.03438%2C2611.03449%2C2611.03455%2C2611.03465%2C2611.03528%2C2611.03533%2C2611.03557%2C2611.03588%2C2611.03597%2C2611.03602%2C2611.03626%2C2611.03646%2C2611.03647%2C2611.03648%2C2611.03685%2C2611.03717%2C2611.03741%2C2611.03765%2C2611.03775%2C2611.03932%2C2611.03936%2C2611.03937%2C2611.03940%2C2611.03942%2C2611.03952%2C2611.03958%2C2611.04002%2C2611.04012%2C2611.04025%2C2611.04028%2C2611.04034%2C2611.04053%2C2611.04084%2C2611.04087&max_results=100", "checked_at": "2026-11-09T19:52:28.369572+00:00", "outcome": "Batch identity/abstract/published/updated provenance preserved; intermediate versions not inferred."}, {"query_or_url": "https://export.arxiv.org/api/query?id_list=2611.04092%2C2611.04102%2C2611.04111%2C2611.04112%2C2611.04123%2C2611.04139%2C2611.04155%2C2611.04164%2C2611.04166%2C2611.04173%2C2611.04193%2C2611.04195%2C2611.04200%2C2611.04216%2C2611.04219%2C2611.04221%2C2611.04233%2C2611.04235%2C2611.04242%2C2611.04244%2C2611.04254%2C2611.04257%2C2611.04262%2C2611.04268%2C2611.04286%2C2611.04300%2C2611.04303%2C2611.04305%2C2611.04317%2C2611.04337%2C2611.04352%2C2611.04358%2C2611.04368%2C2611.04374%2C2611.04379%2C2611.04386%2C2611.04389%2C2611.04397%2C2611.04405%2C2611.04409%2C2611.04414%2C2611.04416%2C2611.04418%2C2611.04422%2C2611.04423%2C2611.04435%2C2611.04438%2C2611.04442%2C2611.04452%2C2611.04467%2C2611.04470%2C2611.04472%2C2611.04476%2C2611.04489%2C2611.04490%2C2611.04491%2C2611.04492%2C2611.04498%2C2611.04524%2C2611.04529%2C2611.04534%2C2611.04537%2C2611.04548%2C2611.04554%2C2611.04583%2C2611.04591%2C2611.04604%2C2611.04616%2C2611.04624%2C2611.04626%2C2611.04633%2C2611.04645%2C2611.04654%2C2611.04666%2C2611.04709%2C2611.04710%2C2611.04711%2C2611.04712%2C2611.04728%2C2611.04734%2C2611.04754%2C2611.04755%2C2611.04759%2C2611.04764%2C2611.04780%2C2611.04811%2C2611.04822%2C2611.04873%2C2611.04874%2C2611.04894%2C2611.04903%2C2611.04912%2C2611.04913%2C2611.04916%2C2611.04932%2C2611.04939%2C2611.04940%2C2611.04943%2C2611.04946%2C2611.04948&max_results=100", "checked_at": "2026-11-09T19:52:31.744379+00:00", "outcome": "Batch identity/abstract/published/updated provenance preserved; intermediate versions not inferred."}, {"query_or_url": "https://export.arxiv.org/api/query?id_list=2611.04950%2C2611.04959%2C2611.04960%2C2611.04980%2C2611.05004%2C2611.05008%2C2611.05011%2C2611.05024%2C2611.05035%2C2611.05049%2C2611.05058%2C2611.05062%2C2611.05066%2C2611.05072%2C2611.05083%2C2611.05084%2C2611.05102%2C2611.05106%2C2611.05131%2C2611.05145%2C2611.05158%2C2611.05172%2C2611.05181%2C2611.05192%2C2611.05193%2C2611.05197%2C2611.05205%2C2611.05206%2C2611.05223%2C2611.05231%2C2611.05275%2C2611.05279%2C2611.05280%2C2611.05286%2C2611.05291%2C2611.05294%2C2611.05348%2C2611.05359%2C2611.05361%2C2611.05377%2C2611.05380%2C2611.05398%2C2611.05400%2C2611.05403%2C2611.05404%2C2611.05406%2C2611.05407%2C2611.05408%2C2611.05411%2C2611.05443%2C2611.05449%2C2611.05451%2C2611.05522%2C2611.05539%2C2611.05559%2C2611.05564%2C2611.05565%2C2611.05569%2C2611.05570%2C2611.05578%2C2611.05579%2C2611.05581%2C2611.05593%2C2611.05594%2C2611.05599%2C2611.05618%2C2611.05633%2C2611.05646%2C2611.05648%2C2611.05680%2C2611.05689%2C2611.05693%2C2611.05697%2C2611.05734%2C2611.05737%2C2611.05738%2C2611.05742%2C2611.05755%2C2611.05766%2C2611.05801%2C2611.05802%2C2611.05811%2C2611.05818%2C2611.05825%2C2611.05843%2C2611.05847%2C2611.05851%2C2611.05859%2C2611.05874%2C2611.05893%2C2611.05909%2C2611.05917%2C2611.05925%2C2611.05927%2C2611.05945%2C2611.05969%2C2611.05974%2C2611.05992%2C2611.05994%2C2611.06000&max_results=100", "checked_at": "2026-11-09T19:53:29.917003+00:00", "outcome": "Batch identity/abstract/published/updated provenance preserved; intermediate versions not inferred."}, {"query_or_url": "https://export.arxiv.org/api/query?id_list=2611.06007%2C2611.06015%2C2611.06020%2C2611.06040%2C2611.06042%2C2611.06046%2C2611.06047%2C2611.06048%2C2611.06061%2C2611.06070%2C2611.06083%2C2611.06085%2C2611.06089%2C2611.06093%2C2611.06096%2C2611.06098%2C2611.06105%2C2611.06113%2C2611.06120%2C2611.06141%2C2611.06143%2C2611.06149%2C2611.06160%2C2611.06168%2C2611.06180%2C2611.06191%2C2611.06195%2C2611.06203%2C2611.06205%2C2611.06221%2C2611.06230%2C2611.06247%2C2611.06255%2C2611.06258%2C2611.06259%2C2611.06270%2C2611.06273%2C2611.06282%2C2611.06302%2C2611.06343%2C2611.06353%2C2611.06355%2C2611.06377%2C2611.06378%2C2611.06412%2C2611.06415%2C2611.06422%2C2611.06430%2C2611.06433%2C2611.06452%2C2611.06453%2C2611.06455%2C2611.06471%2C2611.06484%2C2611.06518%2C2611.06540%2C2611.06544%2C2611.06556%2C2611.06593%2C2611.06594%2C2611.06624%2C2611.06627%2C2611.06631%2C2611.06635%2C2611.06637%2C2611.06652%2C2611.06664%2C2611.06685%2C2611.06701%2C2611.06724%2C2611.06728%2C2611.06738%2C2611.06741%2C2611.06748%2C2611.06760%2C2611.06770%2C2611.06781%2C2611.06796%2C2611.06817%2C2611.06838%2C2611.06840%2C2611.06844%2C2611.06849%2C2611.06854%2C2611.06856%2C2611.06864%2C2611.06870%2C2611.06890%2C2611.06899%2C2611.06901%2C2611.06908%2C2611.06918%2C2611.06930%2C2611.06935%2C2611.06954%2C2611.06974%2C2611.06993%2C2611.07009%2C2611.07049%2C2611.07055&max_results=100", "checked_at": "2026-11-09T19:53:33.322467+00:00", "outcome": "Batch identity/abstract/published/updated provenance preserved; intermediate versions not inferred."}, {"query_or_url": "https://export.arxiv.org/api/query?id_list=2611.07061%2C2611.07063%2C2611.07081%2C2611.07132%2C2611.07148%2C2611.07176%2C2611.07188%2C2611.07289%2C2611.07294%2C2611.07301%2C2611.07328%2C2611.07329%2C2611.07354%2C2611.07384%2C2611.07392%2C2611.07397%2C2611.07398%2C2611.07408%2C2611.07411%2C2611.07417%2C2611.07431%2C2611.07437%2C2611.07443%2C2611.07463%2C2611.07481%2C2611.07498%2C2611.07502%2C2611.07512%2C2611.07513%2C2611.07540%2C2611.07543%2C2611.07551%2C2611.07553%2C2611.07555%2C2611.07566%2C2611.07573%2C2611.07575%2C2611.07580%2C2611.07593%2C2611.07604%2C2611.07613%2C2611.07632%2C2611.07644%2C2611.07647%2C2611.07648%2C2611.07658%2C2611.07662%2C2611.07665%2C2611.07673%2C2611.07677%2C2611.07682%2C2611.07683%2C2611.07702%2C2611.07705%2C2611.07709%2C2611.07711%2C2611.07713%2C2611.07718%2C2611.07730%2C2611.07741%2C2611.07765%2C2611.07775%2C2611.07793%2C2611.07810%2C2611.07811%2C2611.07814%2C2611.07828%2C2611.07836%2C2611.07843%2C2611.07850%2C2611.07865%2C2611.07867%2C2611.07873%2C2611.07883%2C2611.07900%2C2611.07902%2C2611.07909%2C2611.07922%2C2611.07929%2C2611.07935%2C2611.07939%2C2611.07941%2C2611.07950%2C2611.07955%2C2611.07961%2C2611.07979%2C2611.07994%2C2611.08003%2C2611.08005%2C2611.08054%2C2611.08080%2C2611.08081%2C2611.08091%2C2611.08095%2C2611.08099%2C2611.08111%2C2611.08125%2C2611.08128%2C2611.08136%2C2611.08138&max_results=100", "checked_at": "2026-11-09T19:53:37.640503+00:00", "outcome": "Batch identity/abstract/published/updated provenance preserved; intermediate versions not inferred."}, {"query_or_url": "https://export.arxiv.org/api/query?id_list=2611.08140%2C2611.08147%2C2611.08148%2C2611.08154%2C2611.08156%2C2611.08157%2C2611.08185%2C2611.08216%2C2611.08236%2C2611.08240%2C2611.08262%2C2611.08264%2C2611.08271%2C2611.08275%2C2611.08286%2C2611.08288%2C2611.08294%2C2611.08301%2C2611.08330%2C2611.08342%2C2611.08352%2C2611.08359%2C2611.08360%2C2611.08368%2C2611.08372%2C2611.08393%2C2611.08407%2C2611.08413%2C2611.08436%2C2611.08441%2C2611.08449%2C2611.08477%2C2611.08485%2C2611.08486%2C2611.08538%2C2611.08561%2C2611.08577%2C2611.08578%2C2611.08610%2C2611.08631%2C2611.08645%2C2611.08649%2C2611.08651%2C2611.08652%2C2611.08655%2C2611.08657%2C2611.08665%2C2611.08731%2C2611.08732%2C2611.08754%2C2611.08755%2C2611.08763%2C2611.08771%2C2611.08782%2C2611.08800%2C2611.08802%2C2611.08808%2C2611.08831%2C2611.08838%2C2611.08861%2C2611.08879%2C2611.08886%2C2611.08887%2C2611.08897%2C2611.08904%2C2611.08923%2C2611.08928%2C2611.08943%2C2611.08946%2C2611.08954%2C2611.08962%2C2611.08976%2C2611.08989%2C2611.08994%2C2611.08996%2C2611.08998%2C2611.09014%2C2611.09017%2C2611.09041%2C2611.09047%2C2611.09055%2C2611.09058%2C2611.09069%2C2611.09074%2C2611.09077%2C2611.09084%2C2611.09089%2C2611.09092%2C2611.09096%2C2611.09100%2C2611.09117%2C2611.09118%2C2611.09120%2C2611.09121%2C2611.09123%2C2611.09129%2C2611.09133%2C2611.09170%2C2611.09175%2C2611.09191&max_results=100", "checked_at": "2026-11-09T19:54:50.308133+00:00", "outcome": "Batch identity/abstract/published/updated provenance preserved; intermediate versions not inferred."}, {"query_or_url": "https://export.arxiv.org/api/query?id_list=2611.09195%2C2611.09224%2C2611.09238%2C2611.09302%2C2611.09304%2C2611.09309%2C2611.09316%2C2611.09336%2C2611.09355%2C2611.09380%2C2611.09387%2C2611.09436%2C2611.09455%2C2611.09458%2C2611.09493%2C2611.09505%2C2611.09511%2C2611.09521%2C2611.09524%2C2611.09527%2C2611.09536%2C2611.09570%2C2611.09583%2C2611.09599%2C2611.09617%2C2611.09625%2C2611.09652%2C2611.09655%2C2611.09661%2C2611.09664%2C2611.09692%2C2611.09693%2C2611.09714%2C2611.09717%2C2611.09724%2C2611.09725%2C2611.09740%2C2611.09745%2C2611.09756%2C2611.09769%2C2611.09770%2C2611.09794%2C2611.09795%2C2611.09816%2C2611.09845%2C2611.09851%2C2611.09854%2C2611.09863%2C2611.09866%2C2611.09878%2C2611.09880%2C2611.09882%2C2611.09892%2C2611.09894&max_results=54", "checked_at": "2026-11-09T19:54:53.489093+00:00", "outcome": "Batch identity/abstract/published/updated provenance preserved; intermediate versions not inferred."}, {"query_or_url": "https://export.arxiv.org/api/query?id_list=2604.27996%2C2606.26614%2C2610.30753%2C2610.33060%2C2610.38468%2C2610.40333%2C2611.07461%2C2611.08175&max_results=8", "checked_at": "2026-11-09T19:54:59.009861+00:00", "outcome": "Batch identity/abstract/published/updated provenance preserved; intermediate versions not inferred."}, {"query_or_url": "https://export.arxiv.org/api/query?id_list=2610.04262%2C2610.09127%2C2610.11215%2C2610.13502%2C2610.14495&max_results=5", "checked_at": "2026-11-09T19:56:44.071892+00:00", "outcome": "Batch identity/abstract/published/updated provenance preserved; intermediate versions not inferred."}, {"query_or_url": "https://arxiv.org/abs/2611.09017", "checked_at": "2026-11-09T19:58:09.713499+00:00", "outcome": "Primary page retrieved; selected arXiv PDFs checkpointed, older project/venue papers saved unresolved."}, {"query_or_url": "https://arxiv.org/abs/2611.09894", "checked_at": "2026-11-09T19:59:17.500209+00:00", "outcome": "Primary page retrieved; selected arXiv PDFs checkpointed, older project/venue papers saved unresolved."}, {"query_or_url": "https://arxiv.org/abs/2611.02659", "checked_at": "2026-11-09T20:00:19.866898+00:00", "outcome": "Primary page retrieved; selected arXiv PDFs checkpointed, older project/venue papers saved unresolved."}, {"query_or_url": "https://arxiv.org/abs/2610.09127", "checked_at": "2026-11-09T20:01:24.445257+00:00", "outcome": "Primary page retrieved; selected arXiv PDFs checkpointed, older project/venue papers saved unresolved."}, {"query_or_url": "https://arxiv.org/abs/2610.11215", "checked_at": "2026-11-09T20:02:33.737583+00:00", "outcome": "Primary page retrieved; selected arXiv PDFs checkpointed, older project/venue papers saved unresolved."}, {"query_or_url": "https://arxiv.org/abs/2610.14495", "checked_at": "2026-11-09T20:03:37.813541+00:00", "outcome": "Primary page retrieved; selected arXiv PDFs checkpointed, older project/venue papers saved unresolved."}, {"query_or_url": "https://arxiv.org/abs/2611.08294", "checked_at": "2026-11-09T20:04:46.763291+00:00", "outcome": "Primary page retrieved; selected arXiv PDFs checkpointed, older project/venue papers saved unresolved."}, {"query_or_url": "https://arxiv.org/abs/2611.08763", "checked_at": "2026-11-09T20:05:46.410546+00:00", "outcome": "Primary page retrieved; selected arXiv PDFs checkpointed, older project/venue papers saved unresolved."}, {"query_or_url": "https://arxiv.org/abs/2611.05802", "checked_at": "2026-11-09T20:07:10.145626+00:00", "outcome": "Primary page retrieved; selected arXiv PDFs checkpointed, older project/venue papers saved unresolved."}, {"query_or_url": "https://arxiv.org/abs/2611.09769", "checked_at": "2026-11-09T20:08:21.341820+00:00", "outcome": "Primary page retrieved; selected arXiv PDFs checkpointed, older project/venue papers saved unresolved."}, {"query_or_url": "https://arxiv.org/abs/2611.08175", "checked_at": "2026-11-09T20:09:27.841079+00:00", "outcome": "Primary page retrieved; selected arXiv PDFs checkpointed, older project/venue papers saved unresolved."}, {"query_or_url": "https://arxiv.org/abs/2611.04244", "checked_at": "2026-11-09T20:10:40.860506+00:00", "outcome": "Primary page retrieved; selected arXiv PDFs checkpointed, older project/venue papers saved unresolved."}, {"query_or_url": "https://arxiv.org/abs/2611.06856", "checked_at": "2026-11-09T20:11:46.317840+00:00", "outcome": "Primary page retrieved; selected arXiv PDFs checkpointed, older project/venue papers saved unresolved."}, {"query_or_url": "https://arxiv.org/abs/2609.24997", "checked_at": "2026-11-09T20:12:53.448851+00:00", "outcome": "Primary page retrieved; selected arXiv PDFs checkpointed, older project/venue papers saved unresolved."}, {"query_or_url": "https://arxiv.org/abs/2611.04960", "checked_at": "2026-11-09T20:14:25.271121+00:00", "outcome": "Primary page retrieved; selected arXiv PDFs checkpointed, older project/venue papers saved unresolved."}, {"query_or_url": "https://arxiv.org/abs/2611.07730", "checked_at": "2026-11-09T20:15:24.610273+00:00", "outcome": "Primary page retrieved; selected arXiv PDFs checkpointed, older project/venue papers saved unresolved."}] | All four requested cs.GR/cs.CV new/recent paginations complete in six responses; 1054 deduplicated listing IDs resolved. Zero target_and_uncertain records. Only 147 listing identities individually abstract-triaged; 907 unreviewed. Other categories not scanned. |
| hugging_face | partial | [{"query_or_url": "https://huggingface.co/papers/date/2026-11-09", "checked_at": "2026-11-09T19:50:56.829349+00:00", "outcome": "Target daily curation page retrieved; selected leads resolved in official metadata. Curation is not publication date."}] | Single target-date curated page; selected leads pursued, other secondary entries not exhaustively screened. |
| openreview | partial | [{"query_or_url": "site:openreview.net agent CAD generation reconstruction program repair visual feedback 2026", "checked_at": "2026-11-09T19:52:17.332471+00:00", "outcome": "Executed hosted search; citations and deferred leads preserved in additional-search-leads.json; search dates not publication evidence."}] | One site-restricted hosted search; no API traversal or OpenReview PDF reads; remaining leads preserved. |
| official_venues | partial | [{"query_or_url": "agent physical simulation particle effects deformable world November 2026 research SIGGRAPH Asia", "checked_at": "2026-11-09T19:54:00.288320+00:00", "outcome": "Executed hosted search; citations and deferred leads preserved in additional-search-leads.json; search dates not publication evidence."}, {"query_or_url": "https://ns60.ieeevis.org/year/2026/program/content/3121c4fc-2fc3-4c4c-a716-fc64018061ec/", "checked_at": "2026-11-09T19:54:54.053878+00:00", "outcome": "Primary page retrieved; selected arXiv PDFs checkpointed, older project/venue papers saved unresolved."}] | IEEE VIS primary page and venue-related searches; no exhaustive proceedings traversal. Presentation timing not publication evidence. |
| project_author_lab | partial | [{"query_or_url": "agent SVG diagram slide poster editable visual feedback November 2026 November 9 research", "checked_at": "2026-11-09T19:51:29.963379+00:00", "outcome": "Executed hosted search; citations and deferred leads preserved in additional-search-leads.json; search dates not publication evidence."}, {"query_or_url": "agent 3D object procedural modeling Blender inverse graphics geometry editing research", "checked_at": "2026-11-09T19:51:53.250210+00:00", "outcome": "Executed hosted search; citations and deferred leads preserved in additional-search-leads.json; search dates not publication evidence."}, {"query_or_url": "agent 3D scene layout BIM world generation reconstruction November 2 November 9 2026 project", "checked_at": "2026-11-09T19:52:53.841027+00:00", "outcome": "Executed hosted search; citations and deferred leads preserved in additional-search-leads.json; search dates not publication evidence."}, {"query_or_url": "agent articulated asset joint mechanism rig generation 2026 research project", "checked_at": "2026-11-09T19:53:12.099075+00:00", "outcome": "Executed hosted search; citations and deferred leads preserved in additional-search-leads.json; search dates not publication evidence."}, {"query_or_url": "agent animation cutscene cinematography temporal scene November 2026 research", "checked_at": "2026-11-09T19:53:24.969874+00:00", "outcome": "Executed hosted search; citations and deferred leads preserved in additional-search-leads.json; search dates not publication evidence."}, {"query_or_url": "agent graphics benchmark world auditing verification November 9 2026 November 2 2026", "checked_at": "2026-11-09T19:54:13.135299+00:00", "outcome": "Executed hosted search; citations and deferred leads preserved in additional-search-leads.json; search dates not publication evidence."}, {"query_or_url": "graphics agent memory replanning tool interface feedback program synthesis 2026 project lab", "checked_at": "2026-11-09T19:54:42.462942+00:00", "outcome": "Executed hosted search; citations and deferred leads preserved in additional-search-leads.json; search dates not publication evidence."}, {"query_or_url": "https://hilsva.github.io/", "checked_at": "2026-11-09T19:54:53.720856+00:00", "outcome": "Primary page retrieved; selected arXiv PDFs checkpointed, older project/venue papers saved unresolved."}] | HiLSVA directly inspected; other project/lab evidence mostly search retrieval. Prepared source snapshot remains frozen as required, without live Google Doc refresh. |

## Query coverage
- 2d: complete; [{'query_or_url': 'agent SVG diagram slide poster editable visual feedback November 2026 November 9 research', 'checked_at': '2026-11-09T19:51:29.963379+00:00', 'outcome': 'Declared query executed. Complete denotes query completion only, not topic completeness.'}]
- object: complete; [{'query_or_url': 'agent 3D object procedural modeling Blender inverse graphics geometry editing research', 'checked_at': '2026-11-09T19:51:53.250210+00:00', 'outcome': 'Declared query executed. Complete denotes query completion only, not topic completeness.'}]
- cad: complete; [{'query_or_url': 'site:openreview.net agent CAD generation reconstruction program repair visual feedback 2026', 'checked_at': '2026-11-09T19:52:17.332471+00:00', 'outcome': 'Declared query executed. Complete denotes query completion only, not topic completeness.'}]
- scene: complete; [{'query_or_url': 'agent 3D scene layout BIM world generation reconstruction November 2 November 9 2026 project', 'checked_at': '2026-11-09T19:52:53.841027+00:00', 'outcome': 'Declared query executed. Complete denotes query completion only, not topic completeness.'}]
- articulation: complete; [{'query_or_url': 'agent articulated asset joint mechanism rig generation 2026 research project', 'checked_at': '2026-11-09T19:53:12.099075+00:00', 'outcome': 'Declared query executed. Complete denotes query completion only, not topic completeness.'}]
- animation: complete; [{'query_or_url': 'agent animation cutscene cinematography temporal scene November 2026 research', 'checked_at': '2026-11-09T19:53:24.969874+00:00', 'outcome': 'Declared query executed. Complete denotes query completion only, not topic completeness.'}]
- simulation: complete; [{'query_or_url': 'agent physical simulation particle effects deformable world November 2026 research SIGGRAPH Asia', 'checked_at': '2026-11-09T19:54:00.288320+00:00', 'outcome': 'Declared query executed. Complete denotes query completion only, not topic completeness.'}]
- benchmark: complete; [{'query_or_url': 'agent graphics benchmark world auditing verification November 9 2026 November 2 2026', 'checked_at': '2026-11-09T19:54:13.135299+00:00', 'outcome': 'Declared query executed. Complete denotes query completion only, not topic completeness.'}]
- harness: complete; [{'query_or_url': 'graphics agent memory replanning tool interface feedback program synthesis 2026 project lab', 'checked_at': '2026-11-09T19:54:42.462942+00:00', 'outcome': 'Declared query executed. Complete denotes query completion only, not topic completeness.'}]

## Source-derived candidate coverage

Mechanical audit of collected arXiv titles; relevance and semantic correctness require paper evidence.

- Metadata resolved: 1054 / 1054 collected IDs.
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
| Frontier3DBench: Benchmarking Coding Agents for 3D Creation across Objects, Scenes, and Interactive Open Worlds | core | Evaluated developer coding-agent model/harness configurations | Write/execute construction or editing programs and retry after execution/delivery errors | Editable Blender object and scene artifacts; extended Unreal projects | [§2.1 p3; §3.1 pp6–7; Appendix B.1 p17](https://arxiv.org/pdf/2611.09017v1) |
| Video-Coder: Reinforcing Agentic Coding for Video Generation | core | Qwen3.5-9B-derived Video-Coder multimodal policy | Plan scene, write/revise Blender script, choose check_script/run_blender and submit | Dynamic 3D scene and animated white-model video | [§3.2–3.3 p5; Appendix A pp12–14](https://arxiv.org/pdf/2611.09894v1) |
| Parametric CAD Bench v3: Evaluating Agentic Parametric CAD Authoring from Text and Engineering Drawings | core | Evaluated coding agents, including multimodal mini-swe-agent with Claude Opus 5.5 | Write/execute FreeCAD scripts constructing native PartDesign features and save base/edited documents | Editable native parametric CAD solids and feature trees | [§3 pp4–8; §5.2 pp12–13; Appendix B p19](https://arxiv.org/pdf/2611.02659v1) |
| CADFather: Autonomous CAD Reconstruction through Coordinated Tool Use | core | Frozen Qwen3.8-27B visual assistant | Select candidate, proposal tool and sample count; accept/reject proposals or finish | CadQuery-based DSL programs and executable CAD solids reconstructed from target mesh | [§3.1–3.6 pp3–7](https://arxiv.org/pdf/2610.09127v1) |
| GATOR: Generative and Agentic 3D Object Reconstruction From Casual Images | core | GPT-6-Astra through Codex CLI | Choose repairs, script Blender changes, inspect matched renders and revert regressions | Generated object mesh, topology, UVs, PBR textures and materials | [§3.5 p6; A.4 pp19–21](https://arxiv.org/pdf/2610.11215v1) |
| Reels-RSI: Program-Level Self-Improvement for Code-Rendered Explainer Videos | core | Claude Code director and frame workers following Reels-RSI skill | Create script/storyboard and HTML/SVG/Canvas/Three.js animation programs; revise from finalize checks | Editable explainer reel compositions and rendered MP4 | [§2–4 pp2–5; §5.2 p6](https://arxiv.org/pdf/2610.14495v1) |
| ManimCode: Learning Visual Self-Correction for Educational Animation | core | SFT+RL Qwen3.5-4B with role-conditioned writing, review and revision | Generate retrieval queries and animation programs; rewrite from error/critique; select best rendered candidate | Manim educational animation programs and rendered videos | [§4 pp5–7; Appendix A.3 p15](https://arxiv.org/pdf/2611.08294v1) |
| CrowdDirector: Runtime Orchestration of Crowd Simulation through Natural-Language Directives | core | Claude Haiku directive interpreter plus relational GNN crowd policy | Apply validated scene directives and select available action/target for each character | Running animated crowd scene in Unity 2D | [§3.1 p3; §3.6 pp6–7](https://arxiv.org/pdf/2611.08763v1) |
| GREP: Grounding Generated Room Evaluation in Principles | core | GPT-5.6 Sol evaluation agent with scoped metric evaluators | Instantiate scene checks, select measurements/views, request new camera renders and resolve sufficiency | Submitted 3D room geometry, transforms and rendered views | [§3.3 pp4–5; Appendix A.3–A.5 p15](https://arxiv.org/pdf/2611.05802v1) |
| AnimWeb-Bench: Benchmarking Animated Webpage Code Generation from Videos | core | Codex with GPT-5.6 Sol | Inspect source frames, write HTML/CSS/JS, record animation and revise timing/motion code | Animated webpage composition and temporal behavior | [§4.3 p8; Fig8 p13](https://arxiv.org/pdf/2611.09769v1) |
| PCBRouteAgent: How Close Are LLM Agents to Becoming PCB Routing Engineers? | core | Claude Opus 5.5 or Haiku 5.5 global routing planner | Patch route topology, corridor geometry, layer transitions and order | Physical copper traces and vias in KiCad board layout | [§3.2.4–3.3 pp7–9](https://arxiv.org/pdf/2611.08175v1) |
| CounterSketch: Physics-Grounded Counterfactual Reasoning for Sketch-to-Video Generation | core | VLM-guided intervention/event-chain reasoner with bounded repair coordinator | Modify vector scene graph, choose causal event sequence and replan conflicting constraints | Sketch object geometry/relations and animation motion trajectories | [§4.2–4.4 pp5–7](https://arxiv.org/pdf/2611.04244v1) |
| LongBanana: An Expert-Verified Benchmark for Long-Context Multi-Reference Image Synthesis | core | Claude Sonnet 4.6 via OpenClaw+RPR | Retrieve references, plan prompts, call generation/editing backend, inspect draft and revise | Composite raster image grounded in reference identities/relations | [§4.1 p7; C.1 p33; Figure18 p36](https://arxiv.org/pdf/2611.06856v1) |
| VideoGen-Agent: Reinforcing Video Generation Agents | core | Qwen3-VL-8B-Instruct trained by SFT and GRPO | Select retrieval, simulation, generation and verification calls; revise prompts and regenerate dependent segments | Generated videos and rigid-motion guidance | [§2.1 p3; Algorithm1 p15; B.3 pp16–20](https://arxiv.org/pdf/2609.24997v4) |
| An Agentic Framework for Quality-Aware and Scenario-Adaptive Image Compression | core | Qwen3-VL-8B-Instruct across four collaborating roles | Plan restoration and ROI/background quality settings, execute tools, select candidates and reschedule | Input/decoded raster image regions and compressed image artifact | [§III-C–E pp5–10](https://arxiv.org/pdf/2611.04960v2) |
| Seeing Beyond the Next Step: World-Model-Guided Human-Like Navigation in Multi-Agent Scenes | core | SFT+GRPO Qwen3-VL-2B+LoRA policy | Select one of 100 executable short-horizon motion anchors from live observations | Animated pedestrian trajectory in reconstructed Unity crowd scenes | [§3.1 pp3–4; §3.3 p6; §4.1 p6](https://arxiv.org/pdf/2611.07730v1) |

## Prior-day memory and carry-over

Frozen history: `knowledge/daily-history/through-20261015-bvb-v11`. Previously unread records now fully read: 3. Prior pending records still without a new full read: 92.

See history-delta.json for per-paper transitions. Historical results remain in the frozen bundle; not repeated is not excluded, and new-to-history does not mean newly published.

## Abstract-first reading queue

Attention pool: 109; abstracts not delivered: 0; priority/triage gaps: 0; unread ranked leads: 11. See reading-plan.json for model-authored priorities and deferred leads. Priority is not an inclusion judgment or recall guarantee.
