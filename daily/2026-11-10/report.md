# Agentic Graphics daily report
Date: 2026-11-10 | Timezone: America/Chicago | As of: 2026-11-11T05:00:02+00:00
browser-based same-day search; documented source coverage
Taxonomy: google-doc-taxonomy-v3-2026-10-15 | Snapshot: authorized_live_snapshot_reconciled_and_frozen

## Coverage limits
- Search indexes and public release pages may lag; field-wide completeness is not established.
- Finalization was explicitly required by harness at elapsed 1366 seconds / estimated model cost 36.338 USD, before 30-minute wall-clock cap; stopped after completing the already-read BlenderFORGE checkpoint. Eight PDF slots remain unused, not a claim all direct-action candidates were read.
- Discovery and metadata retries consumed approximately 12m53s; 60-percent PDF time target was missed. Five metadata errors recovered; no unresolved listing metadata remains.
- Durable reading-plan.json ranked_unread preserves 25 plausible uncompleted candidates with relation priorities and reasons, including stronger direct-action catch-up papers. triage.json holds per-ID decisions, not final exclusions. discovery/candidate-catalog.json preserves all 964 official abstracts and source provenance.
- backlog-plan.json reserves CADFather, CADForge and editable flowchart follow-ups; all remain unread due to finalization reserve. No unchanged prior completed paper imported or reread.
- deferred-sources.json preserves secondary-source/noncatalog signals, source-date uncertainties, and opened-page disposition. Pending prior-day index contains additional leads beyond these three; no claim that all prior abstracts were refreshed.
- Current canonical metadata was acquired after cutoff but publication/revision eligibility remains bounded by frozen as_of. Latest versioned PDFs pinned and histories checked for selected revisions.
- GAGR-Lab canonical abstract and version-pinned PDF disagree materially; PDF evidence is explicitly distinguished and confidence reduced.
- Source listings and public search do not establish field-wide completeness. No scans of cs.AI, cs.HC, cs.RO, cs.MM or eess.IV; cs.AI-only BlenderFORGE found by search.
- additional-deferred.json preserves 4 plausible metadata-only candidate(s) omitted by catalog attention queue: 2611.10771, 2610.09127, 2610.04262, 2610.06852. They remain unread and unresolved, not excluded.
- Final coverage audit inspected: 139/139 target-focused abstracts delivered and individually triaged; no source-pagination, listing-metadata, target-triage or opened/read decision gaps. Remaining untriaged listing records outside reviewed attention pool are not exclusions.

## already_reported (0)

## same_day_new (5)

### [CJRR-Net: A Candidate-Joint Reprojection Ranking for Future-View Selection in Human Pose Estimation](https://arxiv.org/abs/2611.13700)
core | High | new_relative_to_snapshot
Application: Dynamic / Animation and temporal scene; operations: Other
Candidate-specific geometry improves future camera selection; a qualitative closed-loop Blender demonstration establishes actual camera control.
Scope: A learned policy issues camera-selection commands that change the active Blender camera; subsequent rendered observations drive the next decision. This is graphics-environment control, although the main quantitative objective is perception rather than authoring.
Limits: Quantitative evaluation uses one held-out subject and fixed camera configurations; potential NLF pretraining overlap. Closed-loop evidence is qualitative and does not establish authoring or continuous camera motion.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Visualization | Discrete camera switching in an animated Blender scene keeps a subject visible. ([source](https://arxiv.org/pdf/2611.13700v1), §4.4 p9) |
| input_form | Image, 3D Representation | Current RGB image and known calibrated camera positions/orientations supply the decision. ([source](https://arxiv.org/pdf/2611.13700v1), §3 pp3–5) |
| output | Structured Specification | Argmax score selects camera index and current-to-selected camera command. ([source](https://arxiv.org/pdf/2611.13700v1), Eq11 p5; Figure4 p8) |
| model_type | Unclear | MLPs, attention pooling and two cross-attention blocks form a non-language ranking network. ([source](https://arxiv.org/pdf/2611.13700v1), §3 pp3–5) |
| model_training | Unclear | Ranker trained with classification, ranking and regret losses; frozen NLF and RootHead. ([source](https://arxiv.org/pdf/2611.13700v1), §4.1 pp5–6) |
| planning | Not Applicable | One next-view argmax; motion planning is future work. ([source](https://arxiv.org/pdf/2611.13700v1), §3.2 p5; §5 p9) |
| workflow | Sequential | Observe, rank, select and acquire next view repeatedly. ([source](https://arxiv.org/pdf/2611.13700v1), Figure4 p8; §4.4 p9) |
| update_strategy | Candidate Selection | Each new observation yields scores and selects one candidate camera. ([source](https://arxiv.org/pdf/2611.13700v1), Eq11 p5; Figure4 p8) |
| verifier | Not Applicable | MPJPE and future ground truth are offline metrics; rollout uses a selector rather than judging a prior action. ([source](https://arxiv.org/pdf/2611.13700v1), §4 pp5–9) |
| feedback_assessment | Not Applicable | Future images and annotations only for supervision/offline evaluation; next observation feeds policy. ([source](https://arxiv.org/pdf/2611.13700v1), §4.1 p6; Figure4 p8) |
| feedback_observation | Visual | Successive input images follow preceding camera commands. ([source](https://arxiv.org/pdf/2611.13700v1), Figure4 p8) |
| memory_time | Not Reported | Current-image selection is described; no retained episodic state is reported. ([source](https://arxiv.org/pdf/2611.13700v1), §3–5 pp3–9; full-text memory search) |
| memory_reach | Not Reported | No agent memory store or access scope described. ([source](https://arxiv.org/pdf/2611.13700v1), §3–5 pp3–9; full-text memory search) |
| action_type | Structured Specification | A selected camera index commands the next active view. ([source](https://arxiv.org/pdf/2611.13700v1), Eq11 p5; Figure4 p8) |
| graphics_software | Agent-Adapted | Blender demonstration routes policy commands into active camera selection and observations. ([source](https://arxiv.org/pdf/2611.13700v1), §4.4 p9; Figure4 p8) |
| tools | Perception models | Frozen NLF-S and ViTPose extract pose and uncertainty from current images. ([source](https://arxiv.org/pdf/2611.13700v1), §3.1 p3 and §4.1 p5) |
| resources | Assets | Renderpeople animated human and FBX dance animation used in the rollout. ([source](https://arxiv.org/pdf/2611.13700v1), §4.4 p9) |
| representation | Geometry, Pixels | Calibrated 3D joints/cameras and rendered RGB observations. ([source](https://arxiv.org/pdf/2611.13700v1), §3 pp3–5 and Figure4 p8) |

Events: [{"type": "first_submission", "value": "2026-11-10T07:46:05+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2611.13700", "authority": "primary", "version": "v1", "local_value": "2026-11-10T01:46:05-06:00", "evidence": "Canonical submission history v1.", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: ["Monitor a non-language learned controller label and supervised training-from-scratch label: current model labels do not cover the reported ranker."]

### [OnlyAct: Extracting Action Representations from Foundation Models for World Models](https://arxiv.org/abs/2611.14420)
enabling_or_adjacent | High | new_relative_to_snapshot
Application: Dynamic / Animation and temporal scene; operations: Generation
Extracts transferable action signals from a pretrained video encoder without a reconstruction bottleneck, enabling action-conditioned video simulation.
Scope: Explicit reusable action interface for interactive video world models, evaluated with camera/game action commands, but no closed-loop task agent is evaluated. Classify the enabling encoder, not a nonexistent planner.
Limits: Offline evaluation only; action labels still required for direct-control alignment. Static-camera flow swaps and small contrastive batches limit adaptation; scene disentanglement is not guaranteed. Single world-model training seeds limit variance claims.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Simulation | Representation enables action-conditioned video world simulators. ([source](https://arxiv.org/pdf/2611.14420v1), §1 p2; §3 p4) |
| input_form | Video | Consecutive demonstration frame pair is encoded as a two-frame video clip. ([source](https://arxiv.org/pdf/2611.14420v1), §3.1 pp4–5) |
| output | Unclear | Single forward pass emits normalized 640-dimensional action embedding. ([source](https://arxiv.org/pdf/2611.14420v1), §3.1 p5; inference p6) |
| model_type | Not Applicable | Main encoder is V-JEPA 2 ViT-L; Qwen embedding ablation is superseded. No agent decision-maker in encoder. ([source](https://arxiv.org/pdf/2611.14420v1), §3 pp4–6; Appendix A.3 pp15–17) |
| model_training | Not Applicable | Encoder receives self-supervised contrastive LoRA adaptation; no task-agent decision model trained. ([source](https://arxiv.org/pdf/2611.14420v1), §3.2 p5; Appendix B pp17–19) |
| planning | Not Applicable | Single forward pass; no prompts or trajectory optimization. ([source](https://arxiv.org/pdf/2611.14420v1), Inference p6) |
| workflow | Sequential | Frame clip encoding, pooling, fixed projection and normalization. ([source](https://arxiv.org/pdf/2611.14420v1), §3.1 p5) |
| update_strategy | Not Applicable | Frozen encoder outputs each action once. ([source](https://arxiv.org/pdf/2611.14420v1), Inference p6) |
| verifier | Not Applicable | Probes, scene reconstruction and action classifiers are offline evaluation. ([source](https://arxiv.org/pdf/2611.14420v1), §4 pp7–10; Appendix B.5 p20) |
| feedback_assessment | Not Applicable | Follow/Control/PSNR used for offline comparisons. ([source](https://arxiv.org/pdf/2611.14420v1), §4 pp7–10; Appendix D p20) |
| feedback_observation | Not Applicable | Supplied frame pair is input, not feedback from an encoder-selected action. ([source](https://arxiv.org/pdf/2611.14420v1), Inference p6) |
| memory_time | Not Applicable | Per-pair encoding; six-frame context belongs to separate world model. ([source](https://arxiv.org/pdf/2611.14420v1), §3.1 p5; §3.3 p6) |
| memory_reach | Not Applicable | No shared agent memory in one-pass encoder. ([source](https://arxiv.org/pdf/2611.14420v1), §3.1 pp4–5) |
| action_type | Unclear | Continuous latent action vector conditions denoiser. ([source](https://arxiv.org/pdf/2611.14420v1), §3.1 p5; §3.3 pp6–7) |
| graphics_software | Agent-Ready | World model explicitly accepts a continuous per-transition action interface. ([source](https://arxiv.org/pdf/2611.14420v1), §3.3 pp6–7) |
| tools | Perception models | Foundation video encoder converts frames into action representations. ([source](https://arxiv.org/pdf/2611.14420v1), §3.1 pp4–5) |
| resources | Examples & Trajectories | Demonstration video supplies action stream transferable to other scenes. ([source](https://arxiv.org/pdf/2611.14420v1), Figure3 p6; action transfer §3.3) |
| representation | Learned State, Pixels | Pixel frame pairs map to learned 640-dimensional normalized embeddings. ([source](https://arxiv.org/pdf/2611.14420v1), §3.1 pp4–5) |

Events: [{"type": "first_submission", "value": "2026-11-10T17:59:19+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2611.14420", "authority": "primary", "version": "v1", "evidence": "Official Atom v1 timestamp.", "local_value": "2026-11-10T11:59:19-06:00", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: ["Monitor latent-action interface/output labels for explicitly agent-facing world-model components; avoid forcing latent vectors into code/specification labels."]

### [UGG: Unified Generative Geometry Model](https://arxiv.org/abs/2611.14440)
scope_dependent | High | new_relative_to_snapshot
Application: Static / Scene; operations: Reconstruction
Joint generative geometry permits candidate diversity and RGB-grounded verification without ground-truth geometry at selection time.
Scope: Hypothesis sampling and geometric verification provide a concrete transferable graphics search mechanism, but no agent chooses graphics tools or acts on an environment. An embodied-agent motivation and best-of-N selection do not establish a deployed graphics agent.
Limits: Reprojection proxy is imperfect, gains uneven, depth and pose may be selected from inconsistent candidates. No graphics-agent demonstration. Fine-tuning is expensive and confidence intervals are not reported.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Modeling | Search selects depth and camera pose estimates. ([source](https://arxiv.org/pdf/2611.14440v1), §3.4 pp5–6) |
| input_form | Video | Full RGB video or first-last video frames condition geometry search. ([source](https://arxiv.org/pdf/2611.14440v1), §4.3–4.5 pp7–9) |
| output | Graphics Artifact | Selected depth and camera geometry may come from independent candidates. ([source](https://arxiv.org/pdf/2611.14440v1), §3.4 p6; B.8 p23) |
| model_type | Not Applicable | Fixed candidate verifier; generative diffusion model supplies hypotheses; no agent decision model. ([source](https://arxiv.org/pdf/2611.14440v1), §3.4; checklist p31) |
| model_training | Not Applicable | Wan transformer fine-tuned for conditional generation; selector uses fixed rules. ([source](https://arxiv.org/pdf/2611.14440v1), §4.1 p6; B.2 p17) |
| planning | Not Applicable | Sample, score, select; no task plan. ([source](https://arxiv.org/pdf/2611.14440v1), §3.4 pp5–6) |
| workflow | Sequential | Generate candidates then calculate residuals and select. ([source](https://arxiv.org/pdf/2611.14440v1), B.5 p20; B.8 pp21–23) |
| update_strategy | Candidate Selection | Select candidate with lowest task-specific verification score. ([source](https://arxiv.org/pdf/2611.14440v1), §3.4 p6) |
| verifier | Programmatic | Numerical reprojection and angular consistency verifier controls selected output. ([source](https://arxiv.org/pdf/2611.14440v1), B.8 pp21–23) |
| feedback_assessment | Score, Ranking | Depth residuals ranked per pair; pose mean angular discrepancy; argmin selects final candidate. ([source](https://arxiv.org/pdf/2611.14440v1), B.8 equations22–23 pp22–23) |
| feedback_observation | Visual | Observed RGB correspondences and photometric evidence verify candidates. ([source](https://arxiv.org/pdf/2611.14440v1), §3.4 p5) |
| memory_time | Not Reported | Candidate pool is transient; agent memory lifetime not defined. History guidance is conditioning, not an agent memory store. ([source](https://arxiv.org/pdf/2611.14440v1), B.5 p20; B.8 pp21–23) |
| memory_reach | Not Reported | No role-scoped or shared agent memory architecture. ([source](https://arxiv.org/pdf/2611.14440v1), B.8 pp21–23) |
| action_type | Not Applicable | Internal numerical selection, no emitted graphics program, tool call or GUI action. ([source](https://arxiv.org/pdf/2611.14440v1), §3.4 pp5–6; checklist p31) |
| graphics_software | Not Applicable | Tensor geometry prediction and OpenCV computations, no agent-adapted authoring environment. ([source](https://arxiv.org/pdf/2611.14440v1), §3; B.8) |
| tools | Perception models, Static Validator | RAFT/DINOv2 extract visual evidence; reprojection residuals check sampled geometry. ([source](https://arxiv.org/pdf/2611.14440v1), B.8 pp21–23) |
| resources | Not Reported | Search uses supplied observations and pretrained models, no retrieved examples/assets/rules resource. ([source](https://arxiv.org/pdf/2611.14440v1), B.5–B.8 pp20–23) |
| representation | Geometry, Pixels, Learned State | Latent tokens decode to RGB, depth and camera rays. ([source](https://arxiv.org/pdf/2611.14440v1), §3.1–3.4 pp3–6) |

Events: [{"type": "first_submission", "value": "2026-11-10T18:11:40+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2611.14440", "authority": "primary", "version": "v1", "evidence": "Canonical v1 history.", "local_value": "2026-11-10T12:11:40-06:00", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: ["Borderline numerical hypothesis search should remain distinct from autonomous agent planning."]

### [Elastic-WAM: Adaptive Spatiotemporal Imagination for Efficient Robot Control](https://arxiv.org/abs/2611.14257)
scope_dependent | High | new_relative_to_snapshot
Application: Cross-category; operations: Other
A learned field jointly controls stopping, denoising progression and spatial refresh, reducing robot-policy inference latency without uniformly refining visual futures.
Scope: Learned state-dependent decisions allocate computation to generated visual futures, a defensible transferable mechanism for graphics agents. Demonstrated outputs/actions are robot controls, not authored graphics or operations in a graphics environment; internal latent refinement alone is not promoted to core.
Limits: Only manipulation evaluation; no graphics-agent demonstration. Robot success and latency do not establish visual fidelity. No explicit task-progress memory; authors' stage-discrimination explanation remains a hypothesis.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Unclear | Latent future refinement supports manipulation rather than an explicit graphics task. ([source](https://arxiv.org/pdf/2611.14257v1), §3–4 pp3–8) |
| input_form | Unclear | Field consumes recurrent state s; backbone accepts language, images and proprioception. ([source](https://arxiv.org/pdf/2611.14257v1), §3.1 pp3–4; A.1 p12) |
| output | Structured Specification | Commit probability, step size and token selection mask. ([source](https://arxiv.org/pdf/2611.14257v1), Eq7–9 p4) |
| model_type | Unclear | Temporal and spatial branches predict field parameters; frozen backbone is joint video-action denoising model. ([source](https://arxiv.org/pdf/2611.14257v1), §3.2 pp4–5; A.1 p12) |
| model_training | Unclear | Three-stage action-grounded supervised learning with frozen WAM. ([source](https://arxiv.org/pdf/2611.14257v1), §3.3 pp4–5) |
| planning | Not Applicable | Local recurrent refinement decisions; no represented task plan in field. ([source](https://arxiv.org/pdf/2611.14257v1), §3.4 p5) |
| workflow | Sequential | Dense initialization, repeated sparse refinement, then commit. ([source](https://arxiv.org/pdf/2611.14257v1), §3.4 pp5–6) |
| update_strategy | Local Patch | Refresh selected future queries, preserve unselected cached states. ([source](https://arxiv.org/pdf/2611.14257v1), §3.4 pp5–6) |
| verifier | Not Applicable | Terminal action error supervises training; inference predicts demand. ([source](https://arxiv.org/pdf/2611.14257v1), §3.3–3.4 pp5–6) |
| feedback_assessment | Not Applicable | Demand probabilities guide action allocation; ground-truth errors only during training. ([source](https://arxiv.org/pdf/2611.14257v1), §3.2 p4; §3.3 p5) |
| feedback_observation | Unclear | Updated recurrent latent state determines subsequent refinement. ([source](https://arxiv.org/pdf/2611.14257v1), §3.4 pp5–6) |
| memory_time | Short-Term Memory | Hidden states, keys, values and last-refresh velocities reused across refinement steps within a replanning cycle. ([source](https://arxiv.org/pdf/2611.14257v1), §3.4 pp5–6) |
| memory_reach | Local Memory | Layer-wise cache retained in the refinement/action denoising process. ([source](https://arxiv.org/pdf/2611.14257v1), §3.4 pp5–6) |
| action_type | Structured Specification | Emit commit, step progression, binary group mask. ([source](https://arxiv.org/pdf/2611.14257v1), Eq7–9 p4) |
| graphics_software | Not Applicable | Internal neural computation, not graphics software control. ([source](https://arxiv.org/pdf/2611.14257v1), §3.4; §4) |
| tools | Not Applicable | Field allocates internal token computation. ([source](https://arxiv.org/pdf/2611.14257v1), §3.4 pp5–6) |
| resources | Not Reported | Demonstrations train policies; no reusable assets/examples/rules accessed by task-time field reported. ([source](https://arxiv.org/pdf/2611.14257v1), §3.4 pp5–6; Appendix A–C) |
| representation | Learned State | Future-video latent tokens and layer-wise caches. ([source](https://arxiv.org/pdf/2611.14257v1), §3.1–3.4 pp3–6) |

Events: [{"type": "first_submission", "value": "2026-11-10T16:04:16+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2611.14257", "authority": "primary", "version": "v1", "evidence": "Canonical history.", "local_value": "2026-11-10T10:04:16-06:00", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: ["Latent-computation control and non-language controllers strain input, model and feedback labels; keep this borderline rather than equating all world-model computation with graphics action."]

### [From Video Frames to Robot Meta-Frames: A Unified Latent Interface for World Action Models](https://arxiv.org/abs/2611.14365)
scope_dependent | High | new_relative_to_snapshot
Application: Cross-category; operations: Other
Distribution-aware spectral packing reduces latent sequence length while preserving jointly predicted robot signals and future visuals.
Scope: Compact structured action/world-model representation could inform graphics-simulator agent interfaces. Demonstrated controller operates a robot, not graphics authoring; numerical latent packing and future-view prediction do not establish agent-to-graphics action.
Limits: Fixed layouts and loss weights may need retuning; limited language grounding and background robustness. No graphics-controller demonstration. Interface gains primarily evaluated through manipulation success.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Unclear | Interface carries proprioception, action and value for joint world/action prediction. ([source](https://arxiv.org/pdf/2611.14365v1), §4.1 p5) |
| input_form | Unclear | Normalized robot variables and one-hot task identifier are packed. ([source](https://arxiv.org/pdf/2611.14365v1), §4.2 p5) |
| output | Unclear | Spatial latent meta-frame and analytic recovery of normalized signals. ([source](https://arxiv.org/pdf/2611.14365v1), Eq2–3 pp5–6) |
| model_type | Not Applicable | Fixed coefficient allocation and analytical DCT/iDCT; no learned interface parameters. ([source](https://arxiv.org/pdf/2611.14365v1), §4.2 pp5–6) |
| model_training | Not Applicable | Packing introduces no learned parameters; full fine-tuning belongs to separate Cosmos backbone. ([source](https://arxiv.org/pdf/2611.14365v1), §4.2 p6; B.2 p14) |
| planning | Not Applicable | Deterministic mask from task type; no plan representation. ([source](https://arxiv.org/pdf/2611.14365v1), §4.4 p6) |
| workflow | Sequential | Normalize/pack, inverse transform, route, then transform/readout. ([source](https://arxiv.org/pdf/2611.14365v1), §4.2–4.4 pp5–6) |
| update_strategy | Not Applicable | Fixed allocation across training/inference. ([source](https://arxiv.org/pdf/2611.14365v1), §4.2 p6) |
| verifier | Not Applicable | Frozen-denoiser compatibility is diagnostic evaluation, not task-time verification. ([source](https://arxiv.org/pdf/2611.14365v1), §3 pp3–4; §5.3 p9) |
| feedback_assessment | Not Applicable | Relative errors, PSNR and action L1 are monitoring/evaluation. ([source](https://arxiv.org/pdf/2611.14365v1), §5.3 p9; C.2 p16) |
| feedback_observation | Not Applicable | Packing/readout is analytical without environment feedback. ([source](https://arxiv.org/pdf/2611.14365v1), §4 pp4–7) |
| memory_time | Not Applicable | Fixed stateless transform of current input signals. ([source](https://arxiv.org/pdf/2611.14365v1), §4.2–4.4 pp5–6) |
| memory_reach | Not Applicable | No memory store or agent access permissions. ([source](https://arxiv.org/pdf/2611.14365v1), §4 pp4–7) |
| action_type | Not Applicable | Mask is deterministically derived; no agent operation emitted. ([source](https://arxiv.org/pdf/2611.14365v1), §4.4 p6) |
| graphics_software | Not Applicable | Video diffusion latent interface; robot simulators only used in task evaluation. ([source](https://arxiv.org/pdf/2611.14365v1), §4; §5) |
| tools | Not Applicable | Analytic mathematical transforms, no graphics tool selection. ([source](https://arxiv.org/pdf/2611.14365v1), §4.2 pp5–6) |
| resources | Documentation & Rules | Predefined channel partition, fixed coefficient slots and task-specific mask rules reused. ([source](https://arxiv.org/pdf/2611.14365v1), §4.2–4.4 pp5–6) |
| representation | Learned State | Signals are carried inside pretrained video latent frame space. ([source](https://arxiv.org/pdf/2611.14365v1), §4.1–4.2 p5) |

Events: [{"type": "first_submission", "value": "2026-11-10T17:21:37+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2611.14365", "authority": "primary", "version": "v1", "evidence": "Official v1 timestamp.", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: ["Dense latent control carriers are underrepresented in input/output labels; monitor without expanding scope to every robot policy."]

## same_day_updates (2)

### [SplatLab: Autonomous Scientific Discovery for 3DGS Research](https://arxiv.org/abs/2610.30468)
core | High | new_relative_to_snapshot
Application: Static / Scene; operations: Generation, Editing
Execution-grounded evolutionary graphics research uses verified program substrates, metric-weighted selection and adversarial falsification to develop 3DGS methods.
Scope: Implementation and evolutionary controllers edit executable neural-rendering programs, train and render them, and use observed metrics/build failures to change subsequent code. Graphics algorithm development is a concrete graphics-program action, not merely generic scientific discussion.
Limits: Sixteen reported runs are not equalized-budget comparisons; reproducibility details and LLM stack refer to a supplement absent from this 14-page v3 PDF. Paper reports qualified/marginal/negative results despite broad headline gains. Embedded generated-paper results are not independent validation.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Modeling | Programs implement scene reconstruction/radiance-field modeling through 3DGS hooks. ([source](https://arxiv.org/pdf/2610.30468v3), §3 p4; Stage3 p5) |
| input_form | Language, Document | Candidate mechanism, L-ID/B-ID thesis and cited implementations/papers condition Implementer. ([source](https://arxiv.org/pdf/2610.30468v3), §3 pp4–5) |
| output | Program | Returns C codebase with structured plugin diffs. ([source](https://arxiv.org/pdf/2610.30468v3), §3 p4; Stage3 p5) |
| model_type | LLM | LLM implementation reasoning and LLM rationale/verbal gradients guide mutations. ([source](https://arxiv.org/pdf/2610.30468v3), Stage3–4 p5) |
| model_training | Not Reported | LLM stack deferred to supplementary; retrieved 14-page v3 ends in references without that supplement. No decision-model adaptation statement found. ([source](https://arxiv.org/pdf/2610.30468v3), §4 p6; pp1–14; full-PDF model-term search) |
| planning | PO-2 | Graph-of-Thoughts generation/aggregation/refinement nodes operate within fixed hook contracts and cascade stages; hierarchy can revisit phases. ([source](https://arxiv.org/pdf/2610.30468v3), §3 pp4–5) |
| workflow | Graph-Structured | Revisitable reasoning branches, islands, crossover, hierarchy and return paths. ([source](https://arxiv.org/pdf/2610.30468v3), §3 p4; Stages3–4 pp5–6) |
| update_strategy | Local Patch, Regeneration, Candidate Selection | Structured local diffs, Rewrite full-block regeneration, and Elo/Pareto survivor selection. ([source](https://arxiv.org/pdf/2610.30468v3), Stages3–4 pp5–6) |
| verifier | Critic, Programmatic | Compile/smoke checks and measured metrics; standing falsifier and LLM causal rationales. ([source](https://arxiv.org/pdf/2610.30468v3), Stages3–4 pp5–6) |
| feedback_assessment | Binary, Score, Ranking, Diagnosis | Pass/fail smoke contract, PSNR, Elo/Pareto comparison and build-log verbal-gradient diagnoses. ([source](https://arxiv.org/pdf/2610.30468v3), Stages3–4 pp5–6) |
| feedback_observation | Runtime | Compilation/build logs and measured training performance return to agents. ([source](https://arxiv.org/pdf/2610.30468v3), Stage3–4 p5) |
| memory_time | Short-Term Memory, Long-Term Memory | Lessons File accumulates rationales within tournament; build-failure negatives stored cross-run and saturation checks consult logged negatives. ([source](https://arxiv.org/pdf/2610.30468v3), Stages1–4 pp4–5) |
| memory_reach | Local Memory | Lessons fed to Ideator; failure store used by implementation/search roles. ([source](https://arxiv.org/pdf/2610.30468v3), Stages3–4 p5) |
| action_type | Code/Script | Agents emit structured code diffs in EVOLVE-BLOCKs. ([source](https://arxiv.org/pdf/2610.30468v3), Stage3 p5) |
| graphics_software | Agent-Adapted | Hook mapper, grammar and agent modification scaffolds wrap existing 3DGS libraries. ([source](https://arxiv.org/pdf/2610.30468v3), §3 pp4–5) |
| tools | Execution Utilities, Graphics Operations, Static Validator | Diff application/compilation, ns-train renderer/training experiments, smoke and metric checks. ([source](https://arxiv.org/pdf/2610.30468v3), Stages3–4 pp5–6) |
| resources | Examples & Trajectories, Documentation & Rules | Reference implementations, literature citations and constrained grammar/hooks guide edits. ([source](https://arxiv.org/pdf/2610.30468v3), Stages3–4 p5) |
| representation | Code, Learned State, Pixels | Plugin code trains radiance-field models and renders scene images. ([source](https://arxiv.org/pdf/2610.30468v3), Stages3–4 pp5–6) |

Events: [{"type": "first_submission", "value": "2026-10-21T21:30:32+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2610.30468", "authority": "primary", "version": "v1", "evidence": "Canonical history.", "prior_event_status": "not_seen_in_supplied_history"}, {"type": "revision", "value": "2026-11-08T04:37:54+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2610.30468", "authority": "primary", "version": "v2", "evidence": "Canonical history.", "prior_event_status": "not_seen_in_supplied_history"}, {"type": "revision", "value": "2026-11-10T12:24:58+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2610.30468", "authority": "primary", "version": "v3", "evidence": "Latest version before frozen cutoff.", "local_value": "2026-11-10T06:24:58-06:00", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: ["Graphics research-code evolution is a distinct application phase worth monitoring; do not merge its program edits with generated manuscript figure workflows."]

### [GAGR-Lab: Evaluating Joint Spatial-Geometric and Analytic Function Reasoning](https://arxiv.org/abs/2610.10201)
core | Medium | new_relative_to_snapshot
Application: 2D Graphics, Datasets and Benchmarks; operations: Generation
Source-bound geometric-action audit separates formalization from construction and exposes input leakage, local counterexamples and shared-solution benchmark shortcuts.
Scope: Models emit executable mathematical curves that are rendered and evaluated against scene obstacles and target geometry. Native episodes expose resulting paths to subsequent turns, establishing a direct code-to-geometric-artifact action, unlike generic game locomotion. Narrow geometric construction benchmark, not general 3D authoring.
Limits: Canonical abstract/PDF contents disagree. Retrospective incomplete archive; dependent repeated requests; missing old pilot logs and pending permanent accession. No hidden reasoning or broad model ranking established.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Modeling | Construct continuous symbolic curve satisfying geometric constraints. ([source](https://arxiv.org/pdf/2610.10201v2), p1; Methods p9) |
| input_form | Image, Language | Original scene screenshots and operation-specific prompts accompany each native request. ([source](https://arxiv.org/pdf/2610.10201v2), pp6,9–10; SI p17) |
| output | Program | Raw expressions such as 0.235*x are executed. ([source](https://arxiv.org/pdf/2610.10201v2), TablesS4–S6 p30) |
| model_type | Unclear | Provider labels Minimax/Kimi, Muse/Gemma; serving snapshots not fully established. ([source](https://arxiv.org/pdf/2610.10201v2), p2; TableS3 p29) |
| model_training | Not Reported | Archived requested profiles and serving parameters, no adaptation protocol for native controllers. ([source](https://arxiv.org/pdf/2610.10201v2), p2; Methods p9; full-text search) |
| planning | Not Reported | Visible responses are behavioral observations, not internal reasoning; chained workflow is prospective. ([source](https://arxiv.org/pdf/2610.10201v2), Discussion p8; SI p17) |
| workflow | Sequential | Native episodes consist of chronologically executed actor turns. ([source](https://arxiv.org/pdf/2610.10201v2), FiguresS1–S5 pp19–23) |
| update_strategy | Regeneration | Successive turns emit complete replacement expressions. ([source](https://arxiv.org/pdf/2610.10201v2), TableS5 p30) |
| verifier | Environment | Native engine executes paths and records world exit, terrain impact and target hits. ([source](https://arxiv.org/pdf/2610.10201v2), Methods p10; pp17,30) |
| feedback_assessment | Not Reported | Outcome fields archived, but exact scalar/status payload returned to each next actor not established. ([source](https://arxiv.org/pdf/2610.10201v2), Methods p10; SI p17) |
| feedback_observation | Visual | Historical screenshots contain previous trajectory, remaining original visible input. ([source](https://arxiv.org/pdf/2610.10201v2), SI p17; FiguresS1–S5) |
| memory_time | Short-Term Memory | Prior curve paths remain on scene screenshots over turns. ([source](https://arxiv.org/pdf/2610.10201v2), SI p17) |
| memory_reach | Global Memory | Alternating actors see original shared scene containing historical paths. ([source](https://arxiv.org/pdf/2610.10201v2), FiguresS1–S2 pp19–20; SI p17) |
| action_type | Code/Script | Mathematical function strings are extracted and executed. ([source](https://arxiv.org/pdf/2610.10201v2), Methods p9; TablesS4–S6) |
| graphics_software | Agent-Adapted | Graphwar-derived Rust implementation with model response extraction and archived execution. ([source](https://arxiv.org/pdf/2610.10201v2), Methods p10; code availability) |
| tools | Execution Utilities, Graphics Operations | Expression extraction/execution and native trajectory materialization. ([source](https://arxiv.org/pdf/2610.10201v2), Methods pp9–10) |
| resources | Documentation & Rules | Public mathematical contracts and historical anchoring conventions govern actions. ([source](https://arxiv.org/pdf/2610.10201v2), Methods p9) |
| representation | Code, Geometry, Pixels | Expression code, dense CSV curve coordinates and original screenshots. ([source](https://arxiv.org/pdf/2610.10201v2), Methods pp9–10) |

Events: [{"type": "first_submission", "value": "2026-10-07T15:01:54+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2610.10201", "authority": "primary", "version": "v1", "evidence": "Canonical history.", "prior_event_status": "not_seen_in_supplied_history"}, {"type": "revision", "value": "2026-11-10T13:12:55+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2610.10201", "authority": "primary", "version": "v2", "evidence": "Canonical history; retrieved PDF explicitly marks v2 on p1.", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: ["External graphical traces can provide within-episode shared memory without an LLM memory store; preserve distinction."]

## late_discovery (1)

### [BlenderFORGE: Framework for Optimizing Reactive 3D-Graphics Editing Ability of MLLMs](https://arxiv.org/abs/2611.10768)
core | High | new_relative_to_snapshot
Application: Static / Scene, Static / Object, Datasets and Benchmarks; operations: Editing
A reproducible executable editing substrate enables SFT and multi-turn RL to amortize graphics-editing experience into open-weight agents, complementing BlenderGym's inference-time scaling.
Scope: The trained VLM explicitly chooses code-execution and rendering tools, edits live Blender state, and uses returned renderings/errors for further edits. Training substrate is a principal contribution, with task-time execution directly demonstrated.
Limits: Four bounded editing families only; partial shape-key base-mesh overlap; highest camera-transfer valid rate 35%; no significance intervals for main comparisons and incomplete compute accounting. Terminal reward proxies do not guarantee semantic correctness; some specialists outperform generalists.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Modeling | Object pose, shape-key coefficients, illumination and shader parameter editing; animation explicitly future work. ([source](https://arxiv.org/pdf/2611.10768v1), §3.1 pp3–4; F p27) |
| input_form | Language, Image, 3D Representation | Instructions, start/goal multiview images and initial scene information or bpy initialization script. ([source](https://arxiv.org/pdf/2611.10768v1), §3.4 p5; B.1 pp16–17) |
| output | Graphics Artifact | Final modified Blender scene is evaluated/exported. ([source](https://arxiv.org/pdf/2611.10768v1), §3.1 pp3–4; Algorithm1 p16) |
| model_type | VLM | Qwen3-VL-8B and Qwen3.5-9B consume images and generate action text. ([source](https://arxiv.org/pdf/2611.10768v1), §4.1 p7) |
| model_training | Supervised Fine-Tuning, RL Post-Training | Teacher-trajectory and general-data SFT followed by GSPO AgentLoop-RL. ([source](https://arxiv.org/pdf/2611.10768v1), §3.5 pp6–7; §4.1 p7) |
| planning | Not Reported | ReAct tool choice and reasoning traces; no explicit separate represented multi-step plan for trained agent specified. Baseline plan failure examples do not establish its planner. ([source](https://arxiv.org/pdf/2611.10768v1), A.2 pp15–16; C pp19–23; full-text plan search) |
| workflow | Sequential | Generate calls, execute each in order, append responses and repeat. ([source](https://arxiv.org/pdf/2611.10768v1), Algorithm1 p16) |
| update_strategy | Local Patch | bpy updates current scene attributes and previews for next modification. ([source](https://arxiv.org/pdf/2611.10768v1), §3.1 p4; A.2 p15) |
| verifier | Self, Environment | Agent interprets previews; executor returns success flag and traceback. ([source](https://arxiv.org/pdf/2611.10768v1), §4.5 p10; A.2 p15) |
| feedback_assessment | Binary, Diagnosis | Success flag or traceback; agent reasons about remaining visual discrepancies. ([source](https://arxiv.org/pdf/2611.10768v1), A.2 p15; C p20) |
| feedback_observation | Visual, Runtime | Preview images and stdout/stderr returned through two agent tools. ([source](https://arxiv.org/pdf/2611.10768v1), A.2 pp15–16) |
| memory_time | Short-Term Memory | ctx is extended with each generated message and tool response; isolated scene destroyed after episode. ([source](https://arxiv.org/pdf/2611.10768v1), §3.5 p7; Algorithm1 p16) |
| memory_reach | Local Memory | Each episode's agent context and scene are isolated from others. ([source](https://arxiv.org/pdf/2611.10768v1), §3.3 p5; Algorithm1 p16) |
| action_type | Code/Script, Tool/Function Call | Hermes JSON tool calls carry bpy scripts or camera-preview requests. ([source](https://arxiv.org/pdf/2611.10768v1), A.2 p15; B.1 p17) |
| graphics_software | Agent-Adapted | BlenderHTTP addon and proxy manager expose code, preview and scene export. ([source](https://arxiv.org/pdf/2611.10768v1), A.1–A.2 pp14–15) |
| tools | Execution Utilities, Graphics Operations | blender_code_executor and blender_preview_renderer. ([source](https://arxiv.org/pdf/2611.10768v1), A.2 p15) |
| resources | Assets, Documentation & Rules | Existing asset scene loaded; provided function schemas and Infinigen setup code guide edits. ([source](https://arxiv.org/pdf/2611.10768v1), B.1 pp16–17; §3.3 p5) |
| representation | Code, Geometry, Pixels | bpy scripts modify explicit scenes observed through Cycles images. ([source](https://arxiv.org/pdf/2611.10768v1), §3.1–3.3 pp3–5; A.2) |

Events: [{"type": "first_submission", "value": "2026-11-07T14:56:41+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2611.10768", "authority": "primary", "version": "v1", "evidence": "Official metadata/canonical history.", "local_value": "2026-11-07T08:56:41-06:00", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: ["Preserve distinction between training-time verifiable reward and task-time visual/runtime feedback, even when both share a sandbox."]

## date_unresolved (0)

## unresolved (1)

### [DramaAgent: Agentic Storytelling Video Generation](https://aclanthology.org/2026.aacl-long.163/)
unresolved | Low | new_relative_to_snapshot
Application: Dynamic / Animation and temporal scene; operations: Generation, Editing
Potential multi-scene audiovisual generation and localized agent repair.
Scope: Primary abstract establishes a strong potential video-agent lead, but full PDF and precise date not reached before harness finalization reserve. Not included as verified retained work.
Limits: Abstract-only; publication day and full method remain unverified.

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

Events: [{"type": "formal_publication", "value": "2026-11", "precision": "unknown", "timezone": "unknown", "primary_url": "https://aclanthology.org/2026.aacl-long.163/", "authority": "primary", "evidence": "Proceedings metadata gives November 2026, not an exact release day; conference date range cannot establish same-day publication.", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: []

## excluded (4)

### [TaoMate-R1: Temporal Role Specialization for Streaming Multi-Reference Video Generation](https://arxiv.org/abs/2611.14307)
excluded | High | new_relative_to_snapshot
Application: Dynamic / Animation and temporal scene; operations: Generation
Temporal rather than operation-based LoRA sharing reduces instruction-boundary luminance jumps in streaming video.
Scope: E2_NON_AGENTIC. Full text resolves the provisional streaming-state lead as generator parameter sharing, not agentic control. Absolute chunk index alone selects opening/continuation adapters; external instructions condition synthesis. No material agent-facing interface or controller contribution beyond ordinary conditional video generation is established.
Limits: 32 cases, ten long streams with cached teacher audio and end-frame conditions; external baselines concatenate independently generated clips. No task agent evaluated. Not all text alignment/audio metrics improve.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Not Applicable |  |
| input_form | Not Applicable |  |
| output | Not Applicable |  |
| model_type | Not Applicable |  |
| model_training | Not Applicable |  |
| planning | Not Applicable |  |
| workflow | Not Applicable |  |
| update_strategy | Not Applicable |  |
| verifier | Not Applicable |  |
| feedback_assessment | Not Applicable |  |
| feedback_observation | Not Applicable |  |
| memory_time | Not Applicable |  |
| memory_reach | Not Applicable |  |
| action_type | Not Applicable |  |
| graphics_software | Not Applicable |  |
| tools | Not Applicable |  |
| resources | Not Applicable |  |
| representation | Not Applicable |  |

Events: [{"type": "first_submission", "value": "2026-11-10T16:38:37+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2611.14307", "authority": "primary", "version": "v1", "evidence": "Canonical v1 history.", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: []

### [3A-VLA: Abstraction-Aligned Action Learning for Vision-Language Agents in 3D Game Worlds](https://arxiv.org/abs/2602.02212)
excluded | High | new_relative_to_snapshot
Application: Cross-category; operations: Other
Task-agnostic sparse training abstractions improve reactive VLA game control and facilitate token pruning.
Scope: E1_DOMAIN/E7_OUTSIDE_TASK_BOUNDARY. Full text demonstrates game-playing, combat and navigation, not graphics authoring, scene construction or world auditing. The fact that actions affect a rendered game does not alone establish a graphics research target; generic abstraction supervision is not a material graphics-specific enabling component.
Limits: No long-horizon planning or explicit temporal memory; ESA lacks terrain/collision geometry. Cross-game results concern short-horizon combat, not general completion or graphics tasks.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Not Applicable |  |
| input_form | Not Applicable |  |
| output | Not Applicable |  |
| model_type | Not Applicable |  |
| model_training | Not Applicable |  |
| planning | Not Applicable |  |
| workflow | Not Applicable |  |
| update_strategy | Not Applicable |  |
| verifier | Not Applicable |  |
| feedback_assessment | Not Applicable |  |
| feedback_observation | Not Applicable |  |
| memory_time | Not Applicable |  |
| memory_reach | Not Applicable |  |
| action_type | Not Applicable |  |
| graphics_software | Not Applicable |  |
| tools | Not Applicable |  |
| resources | Not Applicable |  |
| representation | Not Applicable |  |

Events: [{"type": "first_submission", "value": "2026-02-02T15:17:49+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2602.02212", "authority": "primary", "version": "v1", "evidence": "Canonical history.", "prior_event_status": "not_seen_in_supplied_history"}, {"type": "revision", "value": "2026-11-10T12:27:03+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2602.02212", "authority": "primary", "version": "v2", "evidence": "Official metadata and canonical v2 history.", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: []

### [Pose Distance Fields for Humanoid Robots](https://arxiv.org/abs/2602.04851)
excluded | Medium | new_relative_to_snapshot
Application: Cross-category; operations: Other
Lightweight pose-distance reward improves humanoid policy sample efficiency and regularizes retargeting.
Scope: Full text establishes a robot pose regularizer and humanoid tracking reward, not an agent controlling graphics authoring or an explicitly graphics-agent-facing component. Related physics-based character-control methods motivate it, but experiments target Unitree G1 behavior and physical deployment. The initially plausible animation connection remains generic motion-prior transfer, insufficient material graphics-agent evidence.
Limits: Some tracking accuracy regresses, style mimicry can collapse, retargeting can be slower and jitterier, and retargeted training poses may be physically infeasible. Single primary robot morphology.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Not Applicable |  |
| input_form | Not Applicable |  |
| output | Not Applicable |  |
| model_type | Not Applicable |  |
| model_training | Not Applicable |  |
| planning | Not Applicable |  |
| workflow | Not Applicable |  |
| update_strategy | Not Applicable |  |
| verifier | Not Applicable |  |
| feedback_assessment | Not Applicable |  |
| feedback_observation | Not Applicable |  |
| memory_time | Not Applicable |  |
| memory_reach | Not Applicable |  |
| action_type | Not Applicable |  |
| graphics_software | Not Applicable |  |
| tools | Not Applicable |  |
| resources | Not Applicable |  |
| representation | Not Applicable |  |

Events: [{"type": "first_submission", "value": "2026-02-04T18:38:51+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2602.04851", "authority": "primary", "version": "v1", "evidence": "Canonical history.", "prior_event_status": "not_seen_in_supplied_history"}, {"type": "revision", "value": "2026-11-10T10:57:26+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2602.04851", "authority": "primary", "version": "v2", "evidence": "Canonical history.", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: []

### [DORIS: Polarization Aware Multimodal Degradation Perception for Underwater Image Restoration](https://arxiv.org/abs/2610.17991)
excluded | High | new_relative_to_snapshot
Application: 2D Graphics; operations: Reconstruction
Polarization-aware degradation descriptions and local RGB/polarization alignment improve single-step underwater restoration.
Scope: E2_NON_AGENTIC/E3_ONE_SHOT. Diagnostic language hidden states provide conditioning to a single forward-pass restoration network, not a tool/action decision, agent-facing component or feedback controller. Provisional controller possibility resolved by explicit architecture. ChatGPT code assistance is authoring support, not an experimental graphics agent.
Limits: Outdoor no-reference evaluation only; several small downstream gains and tradeoffs in SSIM/DISTS. Supplementary hyperparameter material referenced but not present in retrieved PDF.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Not Applicable |  |
| input_form | Not Applicable |  |
| output | Not Applicable |  |
| model_type | Not Applicable |  |
| model_training | Not Applicable |  |
| planning | Not Applicable |  |
| workflow | Not Applicable |  |
| update_strategy | Not Applicable |  |
| verifier | Not Applicable |  |
| feedback_assessment | Not Applicable |  |
| feedback_observation | Not Applicable |  |
| memory_time | Not Applicable |  |
| memory_reach | Not Applicable |  |
| action_type | Not Applicable |  |
| graphics_software | Not Applicable |  |
| tools | Not Applicable |  |
| resources | Not Applicable |  |
| representation | Not Applicable |  |

Events: [{"type": "first_submission", "value": "2026-10-13T08:55:27+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2610.17991", "authority": "primary", "version": "v1", "evidence": "Canonical history.", "prior_event_status": "not_seen_in_supplied_history"}, {"type": "revision", "value": "2026-11-10T12:33:35+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2610.17991", "authority": "primary", "version": "v2", "evidence": "Canonical history.", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: []

## Application index
| Application | Papers |
|---|---|
| 2D Graphics | [GAGR-Lab: Evaluating Joint Spatial-Geometric and Analytic Function Reasoning](https://arxiv.org/abs/2610.10201) [same_day_updates] |
| Static / Object | [BlenderFORGE: Framework for Optimizing Reactive 3D-Graphics Editing Ability of MLLMs](https://arxiv.org/abs/2611.10768) [late_discovery] |
| Static / CAD | None verified in this run |
| Static / Scene | [UGG: Unified Generative Geometry Model](https://arxiv.org/abs/2611.14440) [same_day_new]; [SplatLab: Autonomous Scientific Discovery for 3DGS Research](https://arxiv.org/abs/2610.30468) [same_day_updates]; [BlenderFORGE: Framework for Optimizing Reactive 3D-Graphics Editing Ability of MLLMs](https://arxiv.org/abs/2611.10768) [late_discovery] |
| Dynamic / Articulated assets | None verified in this run |
| Dynamic / Animation and temporal scene | [CJRR-Net: A Candidate-Joint Reprojection Ranking for Future-View Selection in Human Pose Estimation](https://arxiv.org/abs/2611.13700) [same_day_new]; [OnlyAct: Extracting Action Representations from Foundation Models for World Models](https://arxiv.org/abs/2611.14420) [same_day_new]; [DramaAgent: Agentic Storytelling Video Generation](https://aclanthology.org/2026.aacl-long.163/) [unresolved] |
| Dynamic / Physical simulation and effects | None verified in this run |
| Datasets and Benchmarks | [GAGR-Lab: Evaluating Joint Spatial-Geometric and Analytic Function Reasoning](https://arxiv.org/abs/2610.10201) [same_day_updates]; [BlenderFORGE: Framework for Optimizing Reactive 3D-Graphics Editing Ability of MLLMs](https://arxiv.org/abs/2611.10768) [late_discovery] |
| Cross-category | [Elastic-WAM: Adaptive Spatiotemporal Imagination for Efficient Robot Control](https://arxiv.org/abs/2611.14257) [same_day_new]; [From Video Frames to Robot Meta-Frames: A Unified Latent Interface for World Action Models](https://arxiv.org/abs/2611.14365) [same_day_new] |

## Source ledger
| Source | Status | Checked pages / queries | Limitations |
|---|---|---|---|
| arxiv | partial | [{"query_or_url": "https://arxiv.org/list/cs.GR/new?skip=0&show=100", "checked_at": "2026-11-11T05:00:38.442429+00:00", "outcome": "Observed 9 entries; complete observed pagination, no unvisited links or listing errors. Publication dates resolved separately."}, {"query_or_url": "https://arxiv.org/list/cs.GR/recent?skip=0&show=100", "checked_at": "2026-11-11T05:00:38.564811+00:00", "outcome": "Observed 45 entries; complete observed pagination, no unvisited links or listing errors. Publication dates resolved separately."}, {"query_or_url": "https://arxiv.org/list/cs.CV/new?skip=0&show=100", "checked_at": "2026-11-11T05:00:38.804254+00:00", "outcome": "Observed 100 entries; complete observed pagination, no unvisited links or listing errors. Publication dates resolved separately."}, {"query_or_url": "https://arxiv.org/list/cs.CV/new?skip=0&show=2000", "checked_at": "2026-11-11T05:00:39.235663+00:00", "outcome": "Observed 239 entries; complete observed pagination, no unvisited links or listing errors. Publication dates resolved separately."}, {"query_or_url": "https://arxiv.org/list/cs.CV/recent?skip=0&show=100", "checked_at": "2026-11-11T05:00:38.989851+00:00", "outcome": "Observed 100 entries; complete observed pagination, no unvisited links or listing errors. Publication dates resolved separately."}, {"query_or_url": "https://arxiv.org/list/cs.CV/recent?skip=0&show=2000", "checked_at": "2026-11-11T05:00:40.473995+00:00", "outcome": "Observed 869 entries; complete observed pagination, no unvisited links or listing errors. Publication dates resolved separately."}, {"query_or_url": "official Atom metadata batch 2205.01188,2503.00868,2504.09341,2505.20858,2507.01835,2507.22953,2510.18218,2510.21615,2511.03212,2511.06365,2511.14521,2511.14613,2511.21098,2512.08991,2512.20113,2512.24340,2601.02126,2601.11475,2601.16759,2602.02212,2602.02977,2602.04851,2602.13414,2602.23872,2603.02337,2603.05947,2603.06639,2603.12751,2603.13652,2603.15507,2603.29630,2604.14560,2604.23195,2604.23546,2605.00496,2605.04574,2605.09288,2605.14201,2605.20436,2605.21139,2605.21489,2605.22715,2605.24001,2605.26368,2606.02357,2606.03148,2606.03971,2606.12601,2606.12635,2606.14700,2606.24548,2606.26969,2606.27385,2606.32012,2607.00033,2607.10796,2607.16319,2607.16826,2608.03185,2608.04971,2608.09928,2608.10864,2609.04698,2609.08155,2609.12731,2610.09841,2610.10201,2610.11302,2610.17991,2610.18039,2610.23966,2610.24395,2610.27947,2610.28856,2610.30468,2610.33484,2610.36672,2611.05197,2611.05380,2611.05398,2611.05400,2611.05403,2611.05404,2611.05406,2611.05407,2611.05408,2611.05411,2611.05443,2611.05449,2611.05451,2611.05522,2611.05539,2611.05559,2611.05564,2611.05565,2611.05569,2611.05570,2611.05578,2611.05579,2611.05581", "checked_at": "2026-11-11T05:00:54.787731+00:00", "outcome": "HTTPStatusError: Client error '429 Unknown Error' for url 'https://export.arxiv.org/api/query?id_list=2205.01188%2C2503.00868%2C2504.09341%2C2505.20858%2C2507.01835%2C2507.22953%2C2510.18218%2C2510.21615%2C2511.03212%2C2511.06365%2C2511.14521%2C2511.14613%2C2511.21098%2C2512.08991%2C2512.20113%2C2512.24340%2C2601.02126%2C2601.11475%2C2601.16759%2C2602.02212%2C2602.02977%2C2602.04851%2C2602.13414%2C2602.23872%2C2603.02337%2C2603.05947%2C2603.06639%2C2603.12751%2C2603.13652%2C2603.15507%2C2603.29630%2C2604.14560%2C2604.23195%2C2604.23546%2C2605.00496%2C2605.04574%2C2605.09288%2C2605.14201%2C2605.20436%2C2605.21139%2C2605.21489%2C2605.22715%2C2605.24001%2C2605.26368%2C2606.02357%2C2606.03148%2C2606.03971%2C2606.12601%2C2606.12635%2C2606.14700%2C2606.24548%2C2606.26969%2C2606.27385%2C2606.32012%2C2607.00033%2C2607.10796%2C2607.16319%2C2607.16826%2C2608.03185%2C2608.04971%2C2608.09928%2C2608.10864%2C2609.04698%2C2609.08155%2C2609.12731%2C2610.09841%2C2610.10201%2C2610.11302%2C2610.17991%2C2610.18039%2C2610.23966%2C2610.24395%2C2610.27947%2C2610.28856%2C2610.30468%2C2610.33484%2C2610.36672%2C2611.05197%2C2611.05380%2C2611.05398%2C2611.05400%2C2611.05403%2C2611.05404%2C2611.05406%2C2611.05407%2C2611.05408%2C2611.05411%2C2611.05443%2C2611.05449%2C2611.05451%2C2611.05522%2C2611.05539%2C2611.05559%2C2611.05564%2C2611.05565%2C2611.05569%2C2611.05570%2C2611.05578%2C2611.05579%2C2611.05581&max_results=100'\nFor more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429"}, {"query_or_url": "official Atom metadata batch 2611.05593,2611.05594,2611.05599,2611.05618,2611.05633,2611.05646,2611.05648,2611.05680,2611.05689,2611.05693,2611.05697,2611.05734,2611.05737,2611.05738,2611.05742,2611.05755,2611.05766,2611.05801,2611.05802,2611.05811,2611.05818,2611.05825,2611.05843,2611.05847,2611.05851,2611.05859,2611.05874,2611.05893,2611.05909,2611.05917,2611.05925,2611.05927,2611.05945,2611.05969,2611.05974,2611.05992,2611.05994,2611.06000,2611.06007,2611.06015,2611.06020,2611.06040,2611.06042,2611.06046,2611.06047,2611.06048,2611.06061,2611.06070,2611.06083,2611.06085,2611.06089,2611.06093,2611.06096,2611.06098,2611.06105,2611.06113,2611.06120,2611.06141,2611.06143,2611.06149,2611.06160,2611.06168,2611.06180,2611.06191,2611.06195,2611.06203,2611.06205,2611.06221,2611.06230,2611.06247,2611.06255,2611.06258,2611.06259,2611.06270,2611.06273,2611.06282,2611.06302,2611.06343,2611.06353,2611.06355,2611.06377,2611.06378,2611.06412,2611.06415,2611.06422,2611.06430,2611.06433,2611.06452,2611.06453,2611.06455,2611.06471,2611.06484,2611.06518,2611.06540,2611.06544,2611.06556,2611.06593,2611.06594,2611.06624,2611.06627", "checked_at": "2026-11-11T05:01:59.531914+00:00", "outcome": "ReadTimeout: The read operation timed out"}, {"query_or_url": "official Atom metadata batch 2611.06631,2611.06635,2611.06637,2611.06652,2611.06664,2611.06685,2611.06701,2611.06724,2611.06728,2611.06738,2611.06741,2611.06748,2611.06760,2611.06770,2611.06781,2611.06796,2611.06817,2611.06838,2611.06840,2611.06844,2611.06849,2611.06854,2611.06856,2611.06864,2611.06870,2611.06890,2611.06899,2611.06901,2611.06908,2611.06918,2611.06930,2611.06935,2611.06954,2611.06974,2611.06993,2611.07009,2611.07049,2611.07055,2611.07061,2611.07063,2611.07081,2611.07132,2611.07148,2611.07176,2611.07188,2611.07289,2611.07294,2611.07301,2611.07328,2611.07329,2611.07354,2611.07384,2611.07392,2611.07397,2611.07398,2611.07408,2611.07411,2611.07417,2611.07431,2611.07437,2611.07443,2611.07463,2611.07481,2611.07498,2611.07502,2611.07512,2611.07513,2611.07540,2611.07543,2611.07551,2611.07553,2611.07555,2611.07566,2611.07573,2611.07575,2611.07580,2611.07593,2611.07604,2611.07613,2611.07632,2611.07644,2611.07647,2611.07648,2611.07658,2611.07662,2611.07665,2611.07673,2611.07677,2611.07682,2611.07683,2611.07702,2611.07705,2611.07709,2611.07711,2611.07713,2611.07718,2611.07730,2611.07741,2611.07765,2611.07775", "checked_at": "2026-11-11T05:02:08.990006+00:00", "outcome": "HTTPStatusError: Client error '429 Unknown Error' for url 'https://export.arxiv.org/api/query?id_list=2611.06631%2C2611.06635%2C2611.06637%2C2611.06652%2C2611.06664%2C2611.06685%2C2611.06701%2C2611.06724%2C2611.06728%2C2611.06738%2C2611.06741%2C2611.06748%2C2611.06760%2C2611.06770%2C2611.06781%2C2611.06796%2C2611.06817%2C2611.06838%2C2611.06840%2C2611.06844%2C2611.06849%2C2611.06854%2C2611.06856%2C2611.06864%2C2611.06870%2C2611.06890%2C2611.06899%2C2611.06901%2C2611.06908%2C2611.06918%2C2611.06930%2C2611.06935%2C2611.06954%2C2611.06974%2C2611.06993%2C2611.07009%2C2611.07049%2C2611.07055%2C2611.07061%2C2611.07063%2C2611.07081%2C2611.07132%2C2611.07148%2C2611.07176%2C2611.07188%2C2611.07289%2C2611.07294%2C2611.07301%2C2611.07328%2C2611.07329%2C2611.07354%2C2611.07384%2C2611.07392%2C2611.07397%2C2611.07398%2C2611.07408%2C2611.07411%2C2611.07417%2C2611.07431%2C2611.07437%2C2611.07443%2C2611.07463%2C2611.07481%2C2611.07498%2C2611.07502%2C2611.07512%2C2611.07513%2C2611.07540%2C2611.07543%2C2611.07551%2C2611.07553%2C2611.07555%2C2611.07566%2C2611.07573%2C2611.07575%2C2611.07580%2C2611.07593%2C2611.07604%2C2611.07613%2C2611.07632%2C2611.07644%2C2611.07647%2C2611.07648%2C2611.07658%2C2611.07662%2C2611.07665%2C2611.07673%2C2611.07677%2C2611.07682%2C2611.07683%2C2611.07702%2C2611.07705%2C2611.07709%2C2611.07711%2C2611.07713%2C2611.07718%2C2611.07730%2C2611.07741%2C2611.07765%2C2611.07775&max_results=100'\nFor more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429"}, {"query_or_url": "official Atom metadata batch 2611.07793,2611.07810,2611.07811,2611.07814,2611.07828,2611.07836,2611.07843,2611.07850,2611.07865,2611.07867,2611.07873,2611.07883,2611.07900,2611.07902,2611.07909,2611.07922,2611.07929,2611.07935,2611.07939,2611.07941,2611.07950,2611.07955,2611.07961,2611.07979,2611.07994,2611.08003,2611.08005,2611.08054,2611.08080,2611.08081,2611.08091,2611.08095,2611.08099,2611.08111,2611.08125,2611.08128,2611.08136,2611.08138,2611.08140,2611.08147,2611.08148,2611.08154,2611.08156,2611.08157,2611.08185,2611.08216,2611.08236,2611.08240,2611.08262,2611.08264,2611.08271,2611.08275,2611.08286,2611.08288,2611.08294,2611.08301,2611.08330,2611.08342,2611.08352,2611.08359,2611.08360,2611.08368,2611.08372,2611.08393,2611.08407,2611.08413,2611.08436,2611.08441,2611.08449,2611.08477,2611.08485,2611.08486,2611.08538,2611.08561,2611.08577,2611.08578,2611.08610,2611.08631,2611.08645,2611.08649,2611.08651,2611.08652,2611.08655,2611.08657,2611.08665,2611.08731,2611.08732,2611.08754,2611.08755,2611.08763,2611.08771,2611.08782,2611.08800,2611.08802,2611.08808,2611.08831,2611.08838,2611.08861,2611.08879,2611.08886", "checked_at": "2026-11-11T05:05:14.267940+00:00", "outcome": "HTTPStatusError: Client error '429 Unknown Error' for url 'https://export.arxiv.org/api/query?id_list=2611.07793%2C2611.07810%2C2611.07811%2C2611.07814%2C2611.07828%2C2611.07836%2C2611.07843%2C2611.07850%2C2611.07865%2C2611.07867%2C2611.07873%2C2611.07883%2C2611.07900%2C2611.07902%2C2611.07909%2C2611.07922%2C2611.07929%2C2611.07935%2C2611.07939%2C2611.07941%2C2611.07950%2C2611.07955%2C2611.07961%2C2611.07979%2C2611.07994%2C2611.08003%2C2611.08005%2C2611.08054%2C2611.08080%2C2611.08081%2C2611.08091%2C2611.08095%2C2611.08099%2C2611.08111%2C2611.08125%2C2611.08128%2C2611.08136%2C2611.08138%2C2611.08140%2C2611.08147%2C2611.08148%2C2611.08154%2C2611.08156%2C2611.08157%2C2611.08185%2C2611.08216%2C2611.08236%2C2611.08240%2C2611.08262%2C2611.08264%2C2611.08271%2C2611.08275%2C2611.08286%2C2611.08288%2C2611.08294%2C2611.08301%2C2611.08330%2C2611.08342%2C2611.08352%2C2611.08359%2C2611.08360%2C2611.08368%2C2611.08372%2C2611.08393%2C2611.08407%2C2611.08413%2C2611.08436%2C2611.08441%2C2611.08449%2C2611.08477%2C2611.08485%2C2611.08486%2C2611.08538%2C2611.08561%2C2611.08577%2C2611.08578%2C2611.08610%2C2611.08631%2C2611.08645%2C2611.08649%2C2611.08651%2C2611.08652%2C2611.08655%2C2611.08657%2C2611.08665%2C2611.08731%2C2611.08732%2C2611.08754%2C2611.08755%2C2611.08763%2C2611.08771%2C2611.08782%2C2611.08800%2C2611.08802%2C2611.08808%2C2611.08831%2C2611.08838%2C2611.08861%2C2611.08879%2C2611.08886&max_results=100'\nFor more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429"}, {"query_or_url": "official Atom metadata batch 2611.08887,2611.08897,2611.08904,2611.08923,2611.08928,2611.08943,2611.08946,2611.08954,2611.08962,2611.08976,2611.08989,2611.08994,2611.08996,2611.08998,2611.09014,2611.09017,2611.09041,2611.09047,2611.09055,2611.09058,2611.09069,2611.09074,2611.09077,2611.09084,2611.09089,2611.09092,2611.09096,2611.09100,2611.09117,2611.09118,2611.09120,2611.09121,2611.09123,2611.09129,2611.09133,2611.09170,2611.09175,2611.09191,2611.09195,2611.09224,2611.09238,2611.09302,2611.09304,2611.09309,2611.09316,2611.09336,2611.09355,2611.09380,2611.09387,2611.09436,2611.09455,2611.09458,2611.09493,2611.09505,2611.09511,2611.09521,2611.09524,2611.09527,2611.09536,2611.09570,2611.09583,2611.09599,2611.09617,2611.09625,2611.09652,2611.09655,2611.09661,2611.09664,2611.09692,2611.09693,2611.09714,2611.09717,2611.09724,2611.09725,2611.09740,2611.09745,2611.09756,2611.09769,2611.09770,2611.09794,2611.09795,2611.09816,2611.09845,2611.09851,2611.09854,2611.09863,2611.09866,2611.09878,2611.09880,2611.09882,2611.09892,2611.09894,2611.09897,2611.09913,2611.09916,2611.09939,2611.09949,2611.09951,2611.09953,2611.09954", "checked_at": "2026-11-11T05:06:37.326603+00:00", "outcome": "ReadTimeout: The read operation timed out"}, {"query_or_url": "https://export.arxiv.org/api/query?id_list=2611.09955%2C2611.09956%2C2611.09957%2C2611.09958%2C2611.09959%2C2611.09960%2C2611.09964%2C2611.09971%2C2611.09973%2C2611.09977%2C2611.09980%2C2611.09982%2C2611.09987%2C2611.09993%2C2611.09997%2C2611.09998%2C2611.10000%2C2611.10001%2C2611.10003%2C2611.10004%2C2611.10005%2C2611.10007%2C2611.10013%2C2611.10014%2C2611.10028%2C2611.10032%2C2611.10033%2C2611.10043%2C2611.10061%2C2611.10062%2C2611.10066%2C2611.10070%2C2611.10073%2C2611.10088%2C2611.10091%2C2611.10092%2C2611.10093%2C2611.10097%2C2611.10106%2C2611.10144%2C2611.10148%2C2611.10160%2C2611.10174%2C2611.10182%2C2611.10199%2C2611.10228%2C2611.10236%2C2611.10241%2C2611.10245%2C2611.10249%2C2611.10260%2C2611.10262%2C2611.10263%2C2611.10297%2C2611.10318%2C2611.10321%2C2611.10331%2C2611.10337%2C2611.10338%2C2611.10344%2C2611.10347%2C2611.10348%2C2611.10349%2C2611.10353%2C2611.10370%2C2611.10376%2C2611.10377%2C2611.10379%2C2611.10382%2C2611.10392%2C2611.10413%2C2611.10416%2C2611.10423%2C2611.10441%2C2611.10448%2C2611.10475%2C2611.10483%2C2611.10484%2C2611.10485%2C2611.10497%2C2611.10498%2C2611.10503%2C2611.10506%2C2611.10509%2C2611.10518%2C2611.10523%2C2611.10528%2C2611.10544%2C2611.10547%2C2611.10552%2C2611.10559%2C2611.10562%2C2611.10571%2C2611.10575%2C2611.10578%2C2611.10592%2C2611.10599%2C2611.10609%2C2611.10626%2C2611.10632&max_results=100", "checked_at": "2026-11-11T05:06:53.110997+00:00", "outcome": "Observed source response; scope/date require primary verification."}, {"query_or_url": "https://export.arxiv.org/api/query?id_list=2611.10637%2C2611.10642%2C2611.10644%2C2611.10652%2C2611.10653%2C2611.10655%2C2611.10660%2C2611.10664%2C2611.10665%2C2611.10672%2C2611.10678%2C2611.10690%2C2611.10694%2C2611.10699%2C2611.10713%2C2611.10714%2C2611.10717%2C2611.10720%2C2611.10728%2C2611.10729%2C2611.10734%2C2611.10740%2C2611.10744%2C2611.10746%2C2611.10751%2C2611.10758%2C2611.10764%2C2611.10770%2C2611.10771%2C2611.10774%2C2611.10811%2C2611.10819%2C2611.10821%2C2611.10840%2C2611.10847%2C2611.10858%2C2611.10869%2C2611.10875%2C2611.10908%2C2611.10917%2C2611.10940%2C2611.10960%2C2611.10991%2C2611.11001%2C2611.11007%2C2611.11041%2C2611.11058%2C2611.11062%2C2611.11071%2C2611.11076%2C2611.11087%2C2611.11093%2C2611.11115%2C2611.11116%2C2611.11122%2C2611.11123%2C2611.11131%2C2611.11132%2C2611.11136%2C2611.11139%2C2611.11140%2C2611.11147%2C2611.11152%2C2611.11169%2C2611.11200%2C2611.11209%2C2611.11210%2C2611.11214%2C2611.11218%2C2611.11258%2C2611.11261%2C2611.11265%2C2611.11272%2C2611.11289%2C2611.11291%2C2611.11296%2C2611.11304%2C2611.11320%2C2611.11326%2C2611.11334%2C2611.11359%2C2611.11378%2C2611.11391%2C2611.11398%2C2611.11421%2C2611.11427%2C2611.11433%2C2611.11437%2C2611.11452%2C2611.11464%2C2611.11500%2C2611.11503%2C2611.11510%2C2611.11517%2C2611.11547%2C2611.11554%2C2611.11561%2C2611.11583%2C2611.11586%2C2611.11602&max_results=100", "checked_at": "2026-11-11T05:08:57.276319+00:00", "outcome": "Observed source response; scope/date require primary verification."}, {"query_or_url": "https://export.arxiv.org/api/query?id_list=2611.11607%2C2611.11640%2C2611.11644%2C2611.11678%2C2611.11692%2C2611.11697%2C2611.11735%2C2611.11738%2C2611.11751%2C2611.11753%2C2611.11757%2C2611.11763%2C2611.11770%2C2611.11790%2C2611.11793%2C2611.11809%2C2611.11821%2C2611.11824%2C2611.11831%2C2611.11833%2C2611.11836%2C2611.11843%2C2611.11873%2C2611.11875%2C2611.11887%2C2611.11890%2C2611.11893%2C2611.11906%2C2611.11912%2C2611.11926%2C2611.11934%2C2611.11949%2C2611.11951%2C2611.11962%2C2611.11964%2C2611.11980%2C2611.11989%2C2611.11994%2C2611.12011%2C2611.12023%2C2611.12025%2C2611.12037%2C2611.12038%2C2611.12040%2C2611.12042%2C2611.12044%2C2611.12051%2C2611.12066%2C2611.12069%2C2611.12070%2C2611.12075%2C2611.12077%2C2611.12087%2C2611.12102%2C2611.12103%2C2611.12129%2C2611.12136%2C2611.12144%2C2611.12149%2C2611.12162%2C2611.12187%2C2611.12242%2C2611.12243%2C2611.12259%2C2611.12286%2C2611.12305%2C2611.12319%2C2611.12324%2C2611.12334%2C2611.12345%2C2611.12346%2C2611.12353%2C2611.12364%2C2611.12382%2C2611.12405%2C2611.12411%2C2611.12426%2C2611.12437%2C2611.12443%2C2611.12445%2C2611.12452%2C2611.12477%2C2611.12508%2C2611.12524%2C2611.12557%2C2611.12564%2C2611.12574%2C2611.12603%2C2611.12624%2C2611.12650%2C2611.12657%2C2611.12668%2C2611.12674%2C2611.12681%2C2611.12682%2C2611.12686%2C2611.12699%2C2611.12716%2C2611.12727%2C2611.12739&max_results=100", "checked_at": "2026-11-11T05:09:05.452525+00:00", "outcome": "Observed source response; scope/date require primary verification."}, {"query_or_url": "https://export.arxiv.org/api/query?id_list=2611.12777%2C2611.12798%2C2611.12805%2C2611.12852%2C2611.12855%2C2611.12870%2C2611.12875%2C2611.12879%2C2611.12883%2C2611.12884%2C2611.12885%2C2611.12886%2C2611.12894%2C2611.12911%2C2611.12912%2C2611.12930%2C2611.12932%2C2611.12934%2C2611.12969%2C2611.12975%2C2611.12976%2C2611.12977%2C2611.12978%2C2611.12981%2C2611.12997%2C2611.13000%2C2611.13004%2C2611.13006%2C2611.13009%2C2611.13010%2C2611.13014%2C2611.13027%2C2611.13028%2C2611.13045%2C2611.13046%2C2611.13120%2C2611.13150%2C2611.13172%2C2611.13177%2C2611.13178%2C2611.13180%2C2611.13191%2C2611.13192%2C2611.13198%2C2611.13200%2C2611.13213%2C2611.13245%2C2611.13262%2C2611.13271%2C2611.13280%2C2611.13296%2C2611.13297%2C2611.13304%2C2611.13308%2C2611.13310%2C2611.13316%2C2611.13324%2C2611.13330%2C2611.13384%2C2611.13425%2C2611.13453%2C2611.13486%2C2611.13488%2C2611.13496%2C2611.13504%2C2611.13510%2C2611.13511%2C2611.13513%2C2611.13514%2C2611.13528%2C2611.13530%2C2611.13540%2C2611.13576%2C2611.13581%2C2611.13596%2C2611.13609%2C2611.13620%2C2611.13621%2C2611.13626%2C2611.13628%2C2611.13638%2C2611.13649%2C2611.13654%2C2611.13677%2C2611.13685%2C2611.13700%2C2611.13711%2C2611.13739%2C2611.13752%2C2611.13759%2C2611.13766%2C2611.13769%2C2611.13772%2C2611.13776%2C2611.13784%2C2611.13785%2C2611.13807%2C2611.13808%2C2611.13820%2C2611.13849&max_results=100", "checked_at": "2026-11-11T05:09:09.966067+00:00", "outcome": "Observed source response; scope/date require primary verification."}, {"query_or_url": "https://export.arxiv.org/api/query?id_list=2610.04262%2C2610.06852%2C2610.09127%2C2611.10592%2C2611.10644%2C2611.10768%2C2611.10771%2C2611.11344&max_results=8", "checked_at": "2026-11-11T05:09:16.855812+00:00", "outcome": "Observed source response; scope/date require primary verification."}, {"query_or_url": "https://export.arxiv.org/api/query?id_list=2205.01188%2C2503.00868%2C2504.09341%2C2505.20858%2C2507.01835%2C2507.22953%2C2510.18218%2C2510.21615%2C2511.03212%2C2511.06365%2C2511.14521%2C2511.14613%2C2511.21098%2C2512.08991%2C2512.20113%2C2512.24340%2C2601.02126%2C2601.11475%2C2601.16759%2C2602.02212%2C2602.02977%2C2602.04851%2C2602.13414%2C2602.23872%2C2603.02337%2C2603.05947%2C2603.06639%2C2603.12751%2C2603.13652%2C2603.15507%2C2603.29630%2C2604.14560%2C2604.23195%2C2604.23546%2C2605.00496%2C2605.04574%2C2611.13851%2C2611.13868%2C2611.13870%2C2611.13883%2C2611.13884%2C2611.13890%2C2611.13892%2C2611.13903%2C2611.13907%2C2611.13911%2C2611.13912%2C2611.13920%2C2611.13933%2C2611.13935%2C2611.13955%2C2611.13970%2C2611.13971%2C2611.13992%2C2611.13995%2C2611.13997%2C2611.14013%2C2611.14018%2C2611.14025%2C2611.14033%2C2611.14046%2C2611.14058%2C2611.14060%2C2611.14074%2C2611.14076%2C2611.14097%2C2611.14113%2C2611.14116%2C2611.14118%2C2611.14124%2C2611.14129%2C2611.14135%2C2611.14136%2C2611.14143%2C2611.14176%2C2611.14207%2C2611.14218%2C2611.14254%2C2611.14257%2C2611.14279%2C2611.14281%2C2611.14286%2C2611.14307%2C2611.14311%2C2611.14365%2C2611.14380%2C2611.14420%2C2611.14430%2C2611.14432%2C2611.14436%2C2611.14440%2C2611.14451%2C2611.14469%2C2611.14470%2C2611.14476%2C2611.14483%2C2611.14496%2C2611.14498%2C2611.14518%2C2611.14519&max_results=100", "checked_at": "2026-11-11T05:09:26.551457+00:00", "outcome": "Observed source response; scope/date require primary verification."}, {"query_or_url": "https://export.arxiv.org/api/query?id_list=2605.09288%2C2605.14201%2C2605.20436%2C2605.21139%2C2605.21489%2C2605.22715%2C2605.24001%2C2605.26368%2C2606.02357%2C2606.03148%2C2606.03971%2C2606.12601%2C2606.12635%2C2606.14700%2C2606.24548%2C2606.26969%2C2606.27385%2C2606.32012%2C2607.00033%2C2607.10796%2C2607.16319%2C2607.16826%2C2608.03185%2C2608.04971%2C2608.09928%2C2608.10864%2C2609.04698%2C2609.08155%2C2609.12731%2C2610.09841%2C2610.10201%2C2610.11302%2C2610.17991%2C2610.18039%2C2610.23966%2C2610.24395%2C2610.27947%2C2610.28856%2C2610.30468%2C2610.33484%2C2610.36672%2C2611.05197%2C2611.05380%2C2611.05398%2C2611.05400%2C2611.05403%2C2611.05404%2C2611.05406%2C2611.05407%2C2611.05408%2C2611.05411%2C2611.05443%2C2611.05449%2C2611.05451%2C2611.05522%2C2611.05539%2C2611.05559%2C2611.05564%2C2611.05565%2C2611.05569%2C2611.05570%2C2611.05578%2C2611.05579%2C2611.05581%2C2611.05593%2C2611.05594%2C2611.05599%2C2611.05618%2C2611.05633%2C2611.05646%2C2611.05648%2C2611.05680%2C2611.05689%2C2611.05693%2C2611.05697%2C2611.05734%2C2611.05737%2C2611.05738%2C2611.05742%2C2611.05755%2C2611.05766%2C2611.05801%2C2611.05802%2C2611.05811%2C2611.05818%2C2611.05825%2C2611.05843%2C2611.05847%2C2611.05851%2C2611.05859%2C2611.05874%2C2611.05893%2C2611.05909%2C2611.05917%2C2611.05925%2C2611.05927%2C2611.05945%2C2611.05969%2C2611.05974%2C2611.05992&max_results=100", "checked_at": "2026-11-11T05:09:29.885190+00:00", "outcome": "Observed source response; scope/date require primary verification."}, {"query_or_url": "https://export.arxiv.org/api/query?id_list=2611.05994%2C2611.06000%2C2611.06007%2C2611.06015%2C2611.06020%2C2611.06040%2C2611.06042%2C2611.06046%2C2611.06047%2C2611.06048%2C2611.06061%2C2611.06070%2C2611.06083%2C2611.06085%2C2611.06089%2C2611.06093%2C2611.06096%2C2611.06098%2C2611.06105%2C2611.06113%2C2611.06120%2C2611.06141%2C2611.06143%2C2611.06149%2C2611.06160%2C2611.06168%2C2611.06180%2C2611.06191%2C2611.06195%2C2611.06203%2C2611.06205%2C2611.06221%2C2611.06230%2C2611.06247%2C2611.06255%2C2611.06258%2C2611.06259%2C2611.06270%2C2611.06273%2C2611.06282%2C2611.06302%2C2611.06343%2C2611.06353%2C2611.06355%2C2611.06377%2C2611.06378%2C2611.06412%2C2611.06415%2C2611.06422%2C2611.06430%2C2611.06433%2C2611.06452%2C2611.06453%2C2611.06455%2C2611.06471%2C2611.06484%2C2611.06518%2C2611.06540%2C2611.06544%2C2611.06556%2C2611.06593%2C2611.06594%2C2611.06624%2C2611.06627%2C2611.06631%2C2611.06635%2C2611.06637%2C2611.06652%2C2611.06664%2C2611.06685%2C2611.06701%2C2611.06724%2C2611.06728%2C2611.06738%2C2611.06741%2C2611.06748%2C2611.06760%2C2611.06770%2C2611.06781%2C2611.06796%2C2611.06817%2C2611.06838%2C2611.06840%2C2611.06844%2C2611.06849%2C2611.06854%2C2611.06856%2C2611.06864%2C2611.06870%2C2611.06890%2C2611.06899%2C2611.06901%2C2611.06908%2C2611.06918%2C2611.06930%2C2611.06935%2C2611.06954%2C2611.06974%2C2611.06993%2C2611.07009&max_results=100", "checked_at": "2026-11-11T05:09:33.387897+00:00", "outcome": "Observed source response; scope/date require primary verification."}, {"query_or_url": "https://export.arxiv.org/api/query?id_list=2611.07049%2C2611.07055%2C2611.07061%2C2611.07063%2C2611.07081%2C2611.07132%2C2611.07148%2C2611.07176%2C2611.07188%2C2611.07289%2C2611.07294%2C2611.07301%2C2611.07328%2C2611.07329%2C2611.07354%2C2611.07384%2C2611.07392%2C2611.07397%2C2611.07398%2C2611.07408%2C2611.07411%2C2611.07417%2C2611.07431%2C2611.07437%2C2611.07443%2C2611.07463%2C2611.07481%2C2611.07498%2C2611.07502%2C2611.07512%2C2611.07513%2C2611.07540%2C2611.07543%2C2611.07551%2C2611.07553%2C2611.07555%2C2611.07566%2C2611.07573%2C2611.07575%2C2611.07580%2C2611.07593%2C2611.07604%2C2611.07613%2C2611.07632%2C2611.07644%2C2611.07647%2C2611.07648%2C2611.07658%2C2611.07662%2C2611.07665%2C2611.07673%2C2611.07677%2C2611.07682%2C2611.07683%2C2611.07702%2C2611.07705%2C2611.07709%2C2611.07711%2C2611.07713%2C2611.07718%2C2611.07730%2C2611.07741%2C2611.07765%2C2611.07775%2C2611.07793%2C2611.07810%2C2611.07811%2C2611.07814%2C2611.07828%2C2611.07836%2C2611.07843%2C2611.07850%2C2611.07865%2C2611.07867%2C2611.07873%2C2611.07883%2C2611.07900%2C2611.07902%2C2611.07909%2C2611.07922%2C2611.07929%2C2611.07935%2C2611.07939%2C2611.07941%2C2611.07950%2C2611.07955%2C2611.07961%2C2611.07979%2C2611.07994%2C2611.08003%2C2611.08005%2C2611.08054%2C2611.08080%2C2611.08081%2C2611.08091%2C2611.08095%2C2611.08099%2C2611.08111%2C2611.08125%2C2611.08128&max_results=100", "checked_at": "2026-11-11T05:10:04.549979+00:00", "outcome": "Observed source response; scope/date require primary verification."}, {"query_or_url": "https://export.arxiv.org/api/query?id_list=2611.08136%2C2611.08138%2C2611.08140%2C2611.08147%2C2611.08148%2C2611.08154%2C2611.08156%2C2611.08157%2C2611.08185%2C2611.08216%2C2611.08236%2C2611.08240%2C2611.08262%2C2611.08264%2C2611.08271%2C2611.08275%2C2611.08286%2C2611.08288%2C2611.08294%2C2611.08301%2C2611.08330%2C2611.08342%2C2611.08352%2C2611.08359%2C2611.08360%2C2611.08368%2C2611.08372%2C2611.08393%2C2611.08407%2C2611.08413%2C2611.08436%2C2611.08441%2C2611.08449%2C2611.08477%2C2611.08485%2C2611.08486%2C2611.08538%2C2611.08561%2C2611.08577%2C2611.08578%2C2611.08610%2C2611.08631%2C2611.08645%2C2611.08649%2C2611.08651%2C2611.08652%2C2611.08655%2C2611.08657%2C2611.08665%2C2611.08731%2C2611.08732%2C2611.08754%2C2611.08755%2C2611.08763%2C2611.08771%2C2611.08782%2C2611.08800%2C2611.08802%2C2611.08808%2C2611.08831%2C2611.08838%2C2611.08861%2C2611.08879%2C2611.08886%2C2611.08887%2C2611.08897%2C2611.08904%2C2611.08923%2C2611.08928%2C2611.08943%2C2611.08946%2C2611.08954%2C2611.08962%2C2611.08976%2C2611.08989%2C2611.08994%2C2611.08996%2C2611.08998%2C2611.09014%2C2611.09017%2C2611.09041%2C2611.09047%2C2611.09055%2C2611.09058%2C2611.09069%2C2611.09074%2C2611.09077%2C2611.09084%2C2611.09089%2C2611.09092%2C2611.09096%2C2611.09100%2C2611.09117%2C2611.09118%2C2611.09120%2C2611.09121%2C2611.09123%2C2611.09129%2C2611.09133%2C2611.09170&max_results=100", "checked_at": "2026-11-11T05:10:08.043440+00:00", "outcome": "Observed source response; scope/date require primary verification."}, {"query_or_url": "https://export.arxiv.org/api/query?id_list=2611.09175%2C2611.09191%2C2611.09195%2C2611.09224%2C2611.09238%2C2611.09302%2C2611.09304%2C2611.09309%2C2611.09316%2C2611.09336%2C2611.09355%2C2611.09380%2C2611.09387%2C2611.09436%2C2611.09455%2C2611.09458%2C2611.09493%2C2611.09505%2C2611.09511%2C2611.09521%2C2611.09524%2C2611.09527%2C2611.09536%2C2611.09570%2C2611.09583%2C2611.09599%2C2611.09617%2C2611.09625%2C2611.09652%2C2611.09655%2C2611.09661%2C2611.09664%2C2611.09692%2C2611.09693%2C2611.09714%2C2611.09717%2C2611.09724%2C2611.09725%2C2611.09740%2C2611.09745%2C2611.09756%2C2611.09769%2C2611.09770%2C2611.09794%2C2611.09795%2C2611.09816%2C2611.09845%2C2611.09851%2C2611.09854%2C2611.09863%2C2611.09866%2C2611.09878%2C2611.09880%2C2611.09882%2C2611.09892%2C2611.09894%2C2611.09897%2C2611.09913%2C2611.09916%2C2611.09939%2C2611.09949%2C2611.09951%2C2611.09953%2C2611.09954&max_results=64", "checked_at": "2026-11-11T05:10:11.305194+00:00", "outcome": "Observed source response; scope/date require primary verification."}, {"query_or_url": "https://arxiv.org/abs/2611.13700", "checked_at": "2026-11-11T05:12:53.976537+00:00", "outcome": "Observed source response; scope/date require primary verification."}, {"query_or_url": "https://arxiv.org/abs/2611.14420", "checked_at": "2026-11-11T05:14:23.224384+00:00", "outcome": "Observed source response; scope/date require primary verification."}, {"query_or_url": "https://arxiv.org/abs/2611.14440", "checked_at": "2026-11-11T05:15:25.186204+00:00", "outcome": "Observed source response; scope/date require primary verification."}, {"query_or_url": "https://arxiv.org/abs/2611.14307", "checked_at": "2026-11-11T05:16:23.720229+00:00", "outcome": "Observed source response; scope/date require primary verification."}, {"query_or_url": "https://arxiv.org/abs/2611.14257", "checked_at": "2026-11-11T05:16:51.359910+00:00", "outcome": "Observed source response; scope/date require primary verification."}, {"query_or_url": "https://arxiv.org/abs/2611.14365", "checked_at": "2026-11-11T05:17:52.043070+00:00", "outcome": "Observed source response; scope/date require primary verification."}, {"query_or_url": "https://arxiv.org/abs/2610.30468", "checked_at": "2026-11-11T05:18:47.935049+00:00", "outcome": "Observed source response; scope/date require primary verification."}, {"query_or_url": "https://arxiv.org/abs/2610.30468", "checked_at": "2026-11-11T05:18:47.935049+00:00", "outcome": "Observed source response; scope/date require primary verification."}, {"query_or_url": "https://arxiv.org/abs/2602.02212", "checked_at": "2026-11-11T05:20:04.602302+00:00", "outcome": "Observed source response; scope/date require primary verification."}, {"query_or_url": "https://arxiv.org/abs/2610.10201", "checked_at": "2026-11-11T05:20:37.255713+00:00", "outcome": "Observed source response; scope/date require primary verification."}, {"query_or_url": "https://arxiv.org/abs/2602.04851", "checked_at": "2026-11-11T05:21:39.913132+00:00", "outcome": "Observed source response; scope/date require primary verification."}, {"query_or_url": "https://arxiv.org/abs/2610.17991", "checked_at": "2026-11-11T05:22:13.022872+00:00", "outcome": "Observed source response; scope/date require primary verification."}, {"query_or_url": "https://arxiv.org/abs/2611.10768", "checked_at": "2026-11-11T05:22:42.849657+00:00", "outcome": "Observed source response; scope/date require primary verification."}] | All four required listings fully paginated; 964 listing identities resolved after five transient metadata failures. Only 276 attention-pool abstracts plus selected extras triaged. Other categories unscanned; intermediate histories not inspected for deferred records. |
| hugging_face | partial | [{"query_or_url": "https://huggingface.co/papers/date/2026-11-10", "checked_at": "2026-11-11T05:00:40.350996+00:00", "outcome": "Observed source response; scope/date require primary verification."}] | Daily curation page inspected; curation date not publication date. Unresolved additional signals retained in deferred-sources.json. |
| openreview | partial | [{"query_or_url": "agent CAD generation reconstruction editing constraint solver program repair visual feedback November 2026 site:openreview.net", "checked_at": "2026-11-11T05:03:20.726843+00:00", "outcome": "Observed source response; scope/date require primary verification."}] | Site-restricted public search only, not full OpenReview inventory or canonical forum-date verification. |
| official_venues | partial | [{"query_or_url": "agent animation cutscene temporal scene cinematography research November 3 November 10 2026", "checked_at": "2026-11-11T05:07:40.421973+00:00", "outcome": "Observed source response; scope/date require primary verification."}, {"query_or_url": "agent graphics benchmark world auditing verification SIGGRAPH 2026 proceedings", "checked_at": "2026-11-11T05:08:29.715972+00:00", "outcome": "Observed source response; scope/date require primary verification."}, {"query_or_url": "https://aclanthology.org/2026.aacl-long.163/", "checked_at": "2026-11-11T05:09:17.144651+00:00", "outcome": "Observed source response; scope/date require primary verification."}] | ACL venue paper page and venue-oriented searches only. DramaAgent exact publication day and PDF unresolved. |
| project_author_lab | partial | [{"query_or_url": "agent 3D scene layout world generation BIM architecture November 2026 research project", "checked_at": "2026-11-11T05:03:49.605388+00:00", "outcome": "Observed source response; scope/date require primary verification."}, {"query_or_url": "graphics agent memory replanning tool interface feedback program synthesis project lab November 10 2026", "checked_at": "2026-11-11T05:08:49.130825+00:00", "outcome": "Observed source response; scope/date require primary verification."}, {"query_or_url": "https://news.mit.edu/2026/single-ai-model-simulates-many-substances-behavior-1109", "checked_at": "2026-11-11T05:09:17.307916+00:00", "outcome": "Observed source response; scope/date require primary verification."}] | MIT lab news is a research signal, not a new paper candidate/event. Other projects surfaced through search not exhaustively checked. |

## Query coverage
- 2d: partial; [{'query_or_url': 'agent SVG diagram chart slide poster editable visual feedback research November 3 10 2026', 'checked_at': '2026-11-11T05:02:35.042307+00:00', 'outcome': 'Observed source response; scope/date require primary verification.'}]
- object: partial; [{'query_or_url': 'agent 3D object procedural modeling Blender material inverse graphics shape editing research November 2026', 'checked_at': '2026-11-11T05:02:56.825855+00:00', 'outcome': 'Observed source response; scope/date require primary verification.'}]
- cad: partial; [{'query_or_url': 'agent CAD generation reconstruction editing constraint solver program repair visual feedback November 2026 site:openreview.net', 'checked_at': '2026-11-11T05:03:20.726843+00:00', 'outcome': 'Observed source response; scope/date require primary verification.'}]
- scene: partial; [{'query_or_url': 'agent 3D scene layout world generation BIM architecture November 2026 research project', 'checked_at': '2026-11-11T05:03:49.605388+00:00', 'outcome': 'Observed source response; scope/date require primary verification.'}]
- articulation: partial; [{'query_or_url': 'agent articulated asset joint mechanism rig generation research', 'checked_at': '2026-11-11T05:07:14.843118+00:00', 'outcome': 'Observed source response; scope/date require primary verification.'}]
- animation: partial; [{'query_or_url': 'agent animation cutscene temporal scene cinematography research November 3 November 10 2026', 'checked_at': '2026-11-11T05:07:40.421973+00:00', 'outcome': 'Observed source response; scope/date require primary verification.'}]
- simulation: partial; [{'query_or_url': 'agent physical simulation particle effects deformable world research November 2026', 'checked_at': '2026-11-11T05:08:12.276311+00:00', 'outcome': 'Observed source response; scope/date require primary verification.'}]
- benchmark: partial; [{'query_or_url': 'agent graphics benchmark world auditing verification SIGGRAPH 2026 proceedings', 'checked_at': '2026-11-11T05:08:29.715972+00:00', 'outcome': 'Observed source response; scope/date require primary verification.'}]
- harness: partial; [{'query_or_url': 'graphics agent memory replanning tool interface feedback program synthesis project lab November 10 2026', 'checked_at': '2026-11-11T05:08:49.130825+00:00', 'outcome': 'Observed source response; scope/date require primary verification.'}]

## Source-derived candidate coverage

Mechanical audit of collected arXiv titles; relevance and semantic correctness require paper evidence.

- Metadata resolved: 964 / 964 collected IDs.
- Target-day / history-uncertain candidates: 139.
- Explicit triage decisions: 139; catalog-page delivery: 139.
- Missing source scans: 0; incomplete scans: 0.
- Unresolved metadata: 0; no triage decision: 0.
- Full candidate IDs and remaining gaps: `coverage-audit.json`. Unreviewed entries are not exclusions.
- Other platforms remain governed by the source ledger; this audit is not exhaustive discovery.

## Borderline graphics contributions

These records are not established core agentic systems. They remain visible with their scope uncertainty.

| Paper | Why borderline |
|---|---|
| UGG: Unified Generative Geometry Model | Hypothesis sampling and geometric verification provide a concrete transferable graphics search mechanism, but no agent chooses graphics tools or acts on an environment. An embodied-agent motivation and best-of-N selection do not establish a deployed graphics agent. |
| Elastic-WAM: Adaptive Spatiotemporal Imagination for Efficient Robot Control | Learned state-dependent decisions allocate computation to generated visual futures, a defensible transferable mechanism for graphics agents. Demonstrated outputs/actions are robot controls, not authored graphics or operations in a graphics environment; internal latent refinement alone is not promoted to core. |
| From Video Frames to Robot Meta-Frames: A Unified Latent Interface for World Action Models | Compact structured action/world-model representation could inform graphics-simulator agent interfaces. Demonstrated controller operates a robot, not graphics authoring; numerical latent packing and future-view prediction do not establish agent-to-graphics action. |

## Agent-to-graphics evidence

| Paper | Status | Controller | Action / decision | Graphics target | Source |
|---|---|---|---|---|---|
| CJRR-Net: A Candidate-Joint Reprojection Ranking for Future-View Selection in Human Pose Estimation | core | CJRR-Net learned candidate-camera ranker | Select one of eight cameras; activate it for the next observation | Active camera in Blender 5.0.1 animated scene | [§4.4 p9 and Figure 4 p8](https://arxiv.org/pdf/2611.13700v1) |
| OnlyAct: Extracting Action Representations from Foundation Models for World Models | enabling_or_adjacent | External agent/camera action stream, or supplied demonstration; no task-time autonomous controller evaluated | Map demonstrated or real actions into a reusable latent action interface | Action-conditioned autoregressive video world simulator | [§3 pp4–7; Figure3; Appendix D p20](https://arxiv.org/pdf/2611.14420v1) |
| UGG: Unified Generative Geometry Model | scope_dependent | Fixed numerical candidate selector; no demonstrated agent controller | Rank independent depth/pose hypotheses using reprojection evidence | Reconstructed scene depth and camera geometry | [§3.4 pp5–6; B.8 pp21–23; checklist p31](https://arxiv.org/pdf/2611.14440v1) |
| Elastic-WAM: Adaptive Spatiotemporal Imagination for Efficient Robot Control | scope_dependent | Learned spatiotemporal refinement-demand field | Stop or continue latent video refinement; choose denoising progression and exact-budget token mask | Internal future-video representations used for robot control; no exposed graphics artifact | [§3.2–3.4 pp4–6](https://arxiv.org/pdf/2611.14257v1) |
| From Video Frames to Robot Meta-Frames: A Unified Latent Interface for World Action Models | scope_dependent | MetaWAM robot policy; analytical interface itself has no autonomous controller | Pack robot action/state/value signals and route their conditioning/target roles | Video diffusion latent world representation; no authored graphics target demonstrated | [§4 pp4–7; §5 pp7–9](https://arxiv.org/pdf/2611.14365v1) |
| SplatLab: Autonomous Scientific Discovery for 3DGS Research | core | Implementer, Graph-of-Thoughts controller, tournament mutation operators and debugger agents | Emit/apply structured code diffs to 3DGS plugin hooks; execute and select/refine candidates | SPLATIFY/NERFIFY/gsplat neural-rendering program code and rendered scene experiments | [§3 Stage3–4 pp5–6](https://arxiv.org/pdf/2610.30468v3) |
| GAGR-Lab: Evaluating Joint Spatial-Geometric and Analytic Function Reasoning | core | Hosted language/vision model actors in archived native episodes | Emit mathematical expression executed as a curve through a shooter location | 2D geometric trajectory in Rust Graphwar arena with obstacles | [Methods pp9–10; Figures5/S1–S5; TablesS4–S6 p30](https://arxiv.org/pdf/2610.10201v2) |
| BlenderFORGE: Framework for Optimizing Reactive 3D-Graphics Editing Ability of MLLMs | core | SFT+GSPO-trained Qwen visual language editing agent | Autonomously choose bpy execution or preview tool; emit scene edits | Explicit Blender object transforms, shape keys, materials and lights | [§3.1 pp3–4; A.2 pp15–16](https://arxiv.org/pdf/2611.10768v1) |

## Prior-day memory and carry-over

Frozen history: `knowledge/daily-history/through-20261015-bvb-v11`. Previously unread records now fully read: 0. Prior pending records still without a new full read: 95.

See history-delta.json for per-paper transitions. Historical results remain in the frozen bundle; not repeated is not excluded, and new-to-history does not mean newly published.

## Abstract-first reading queue

Attention pool: 278; abstracts not delivered: 0; priority/triage gaps: 0; unread ranked leads: 25. See reading-plan.json for model-authored priorities and deferred leads. Priority is not an inclusion judgment or recall guarantee.
