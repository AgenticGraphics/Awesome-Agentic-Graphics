# Agentic Graphics daily report
Date: 2026-11-04 | Timezone: America/Chicago | As of: 2026-11-07T21:44:27+00:00
browser-based same-day search; documented source coverage
Taxonomy: google-doc-taxonomy-v3-2026-10-15 | Snapshot: authorized_live_snapshot_reconciled_and_frozen

## Coverage limits
- Partial bounded research, not field-wide exhaustive discovery. Frozen cutoff and snapshot preserved; later tool retrieval did not extend eligible publication events.
- Harness instructed FINALIZE NOW at turn 38 (elapsed 969 seconds; estimated model cost 36.523 USD), citing time or estimated-cost reserve. Stopped new PDF reads immediately. Eight full papers completed; 12 of maximum 20 slots unused. Wall clock alone did not exhaust 30-minute cap.
- All 1062 listing identities have official metadata; 247 target/uncertain abstracts and 334 catchup attention abstracts were delivered and individually triaged. Catalog records outside reviewed attention remain unreviewed; see unreviewed-catalog.json. Some title hints outside date attention remain unreviewed, not excluded.
- Plausible unread leads persist in reading-plan.json (46 entries), additional-deferred.json (11 outside-plan entries), triage.json and discovery/candidate-catalog.json. Search-only signals remain in search-signals.json.
- Three prior pending backlog slots reserved for CADFather, Reels-RSI and WorldSolver, but none reached before harness finalization. Full authorized INDEX reviewed; details and fresh abstracts checked for these three. See backlog-plan.json for reasons and deviations. No old completed paper imported as newly read.
- NeoWorld-Pro, WorldAct and EvoDesign canonical histories exclude November 4 local revisions: their latest versions are November 5 local. Saved as unresolved later-day leads, not scope exclusions.
- FLASH direct-action revision was read before first-submission enabling papers following shared selected_next; deviation from strict first-submission-first ordering is documented in backlog-plan.json.
- PDF phase began about eight minutes into original 30-minute cap, initially reserving more than 60% for reading; later harness cost reserve curtailed that plan. No claim that all plausible direct-action catchup work was read.
- All five source families and nine query families have executed checks, but OpenReview and official venue coverage is search-limited. No scans of cs.AI/cs.HC/cs.RO/cs.MM/eess.IV; no live taxonomy refresh under frozen experiment instruction.
- Provisional triage rejects are not final exclusions. Authoritative version evidence and full PDF receipt required for every retained classification. No primary-access failure occurred for selected PDFs.

## already_reported (0)

## same_day_new (7)

### [LongBanana: An Expert-Verified Benchmark for Long-Context Multi-Reference Image Synthesis](https://arxiv.org/abs/2611.06856)
core | High | new_relative_to_snapshot
Application: 2D Graphics, Datasets and Benchmarks; operations: Generation
Separates privileged static composition schedules from adaptive evidence-grounded synthesis; OpenClaw + RPR obtains 78.4 checklist average versus 74.6 for PD-Direct.
Scope: Evaluated agent harness selects references, plans image generation and revises drafts using visual feedback.
Limits: Only 90 high-density image tasks; no 3D or video coverage. RPR gains depend on harness and can induce drift. Reproduction commands, runtime and API cost are omitted. Checklist release declarations conflict with linked project availability; not independently reproduced.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Visualization | Composes reference-grounded advertisements, posters and visual compositions. ([source](https://arxiv.org/pdf/2611.06856v1), pp.1,4,25) |
| input_form | Language, Image | User instruction and approximately 32 reference images. ([source](https://arxiv.org/pdf/2611.06856v1), p.36 Fig.18) |
| output | Rendered Media | Final output: synthesized image. ([source](https://arxiv.org/pdf/2611.06856v1), p.36) |
| model_type | VLM | Claude Sonnet 4.6 plans and inspects drafts and references. ([source](https://arxiv.org/pdf/2611.06856v1), pp.7,33,36) |
| model_training | Not Reported | Shared agent model and harness versions identified, but controller adaptation explicitly neither specified nor denied. ([source](https://arxiv.org/pdf/2611.06856v1), Appendix C.1 and full-text training search) |
| planning | PO-2 | Fixed ReAct/Plan–Exec/Reflect stages; agent builds subgoals and prompt schedule. ([source](https://arxiv.org/pdf/2611.06856v1), pp.7,36) |
| workflow | Sequential | RPR is a serial workflow. ([source](https://arxiv.org/pdf/2611.06856v1), p.3) |
| update_strategy | Local Patch | Detect missing content or wrong bindings and revise prompts and repair drafts. ([source](https://arxiv.org/pdf/2611.06856v1), p.36) |
| verifier | Self | Reflect lets the agent inspect drafts and decide revision. ([source](https://arxiv.org/pdf/2611.06856v1), pp.7,36) |
| feedback_assessment | Diagnosis | Missing content and wrong bindings drive repair. ([source](https://arxiv.org/pdf/2611.06856v1), p.36) |
| feedback_observation | Visual | Agent-directed draft review. ([source](https://arxiv.org/pdf/2611.06856v1), p.36) |
| memory_time | Short-Term Memory | Harness maintains reference state and records revisions across generation steps. ([source](https://arxiv.org/pdf/2611.06856v1), pp.7,36) |
| memory_reach | Global Memory | Shared agent state connects ReAct, Plan–Exec and Reflect. ([source](https://arxiv.org/pdf/2611.06856v1), p.36 Fig.18) |
| action_type | Tool/Function Call | Harness calls reference browsing and image-generation tools. ([source](https://arxiv.org/pdf/2611.06856v1), p.33 C.1) |
| graphics_software | Agent-Adapted | Harness wraps fixed image generator and tool inventory. ([source](https://arxiv.org/pdf/2611.06856v1), pp.3,33) |
| tools | Execution Utilities, Perception models | Image-generation, OCR/count/layout, file or prompt-management tools. ([source](https://arxiv.org/pdf/2611.06856v1), p.33) |
| resources | Assets | Reference image inventory is retrieved during synthesis. ([source](https://arxiv.org/pdf/2611.06856v1), pp.7,36) |
| representation | Pixels | Draft and final images materialize generation state. ([source](https://arxiv.org/pdf/2611.06856v1), pp.7,36) |

Events: [{"type": "first_submission", "value": "2026-11-04T18:11:56+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2611.06856", "authority": "primary", "version": "v1", "evidence": "Canonical submission history; 12:11:56 America/Chicago.", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: ["Visualization versus general raster modeling remains a task-boundary ambiguity; classify the visual communication setting, not every generation task as Visualization."]

### [EvoWorld: Towards Out-of-Sight World Evolution in Generative Video Models](https://arxiv.org/abs/2611.06748)
core | High | new_relative_to_snapshot
Application: Dynamic / Animation and temporal scene; operations: Generation
Brain-generated event-aware prompts plus trained anchored renderer yield 90.8% core success on 120 cases; removing reasoning prompts substantially reduces success.
Scope: World brain's observed-event reasoning directly specifies subsequent video state; not merely a transferable world model.
Limits: Single event and subject reaction, mostly horizontal camera pans; no systematic complex 6-DoF or multi-event test. Controlled I2V uses first frame rather than demonstrating adaptive retrieval in main evaluation. VLM-based assessment may bias results.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Animation | Render event and off-screen subject reaction. ([source](https://arxiv.org/pdf/2611.06748v2), §3.1) |
| input_form | Language, Image | Controlled I2V benchmark supplies initial frame and switched prompts. ([source](https://arxiv.org/pdf/2611.06748v2), pp.16-17) |
| output | Rendered Media | 896x512 video at 24fps. ([source](https://arxiv.org/pdf/2611.06748v2), §4.2) |
| model_type | VLM | VLM brain instantiated with Qwen3.8-27B. ([source](https://arxiv.org/pdf/2611.06748v2), §4.2) |
| model_training | Not Reported | LoRA training explicitly describes renderer; brain adaptation is not specified. ([source](https://arxiv.org/pdf/2611.06748v2), §4.2, Appendices B-D; full-text frozen/brain search) |
| planning | Not Reported | Brain produces a next-segment prompt; no explicit multi-step task plan reported. ([source](https://arxiv.org/pdf/2611.06748v2), Appendix D; full-text plan search) |
| workflow | Sequential | Each completed segment is observed then next segment generated. ([source](https://arxiv.org/pdf/2611.06748v2), §3.3.5) |
| update_strategy | Not Applicable | Continuation follows realized event; prior segments are not repaired or regenerated. ([source](https://arxiv.org/pdf/2611.06748v2), Appendix D and repair search) |
| verifier | Self | Brain assesses realized threat and checks resultant response. ([source](https://arxiv.org/pdf/2611.06748v2), Appendix D Fig.7) |
| feedback_assessment | Diagnosis | Threat assessment: DANGEROUS; observed charging changes response. ([source](https://arxiv.org/pdf/2611.06748v2), p.18 Fig.7) |
| feedback_observation | Visual | Temporally sampled frames from new segment are observed. ([source](https://arxiv.org/pdf/2611.06748v2), Appendix D) |
| memory_time | Short-Term Memory | Accumulated textual world record supplied at each call. ([source](https://arxiv.org/pdf/2611.06748v2), Appendix D) |
| memory_reach | Local Memory | World record provided to brain, renderer gets inferred prompt and anchors. ([source](https://arxiv.org/pdf/2611.06748v2), Appendix D) |
| action_type | Tool/Function Call | Concrete generation prompt conditions next renderer segment. ([source](https://arxiv.org/pdf/2611.06748v2), §3.3.5) |
| graphics_software | Agent-Adapted | Brain and anchors integrated with LTX conditioning path. ([source](https://arxiv.org/pdf/2611.06748v2), §3.3, Appendix E) |
| tools | Perception models | Segment-autoregressive video renderer called with inferred instruction. ([source](https://arxiv.org/pdf/2611.06748v2), §3.3) |
| resources | Assets | Opening frame used as persistent entity reference in evaluated configuration. ([source](https://arxiv.org/pdf/2611.06748v2), pp.17-18) |
| representation | Pixels, Learned State | Decoded frames and reference/temporal latents condition generation. ([source](https://arxiv.org/pdf/2611.06748v2), §3.3.2) |

Events: [{"type": "first_submission", "value": "2026-11-04T16:26:45+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2611.06748", "authority": "primary", "version": "v1", "evidence": "Official metadata published; Chicago November 4.", "prior_event_status": "not_seen_in_supplied_history"}, {"type": "revision", "value": "2026-11-05T04:27:21+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2611.06748", "authority": "primary", "version": "v2", "evidence": "Official updated; Chicago November 4 22:27:21; latest available before cutoff.", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: ["Forward evolution from observations is not well captured by corrective update labels; no corrective update asserted."]

### [DreamRealm: Exploring and Materializing Hallucination Worlds for Trustworthy Vision-Language Models](https://arxiv.org/abs/2611.06433)
core | High | new_relative_to_snapshot
Application: 2D Graphics, Datasets and Benchmarks; operations: Editing
Constructs 28,960 human-approved hallucination-guided image edits; matched Qwen training improves HallusionBench by 7.26 points.
Scope: Data-generation planner selects image-edit type, preservation regions and candidate prompts; verified quality gates control retries and redraw fallback.
Limits: Only 30.07% editing yield after human review; closed-source generation and annotation costs; planner adaptation and conversational memory unspecified. Minimality is judged, not globally optimized.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Modeling | Controlled content and structure edits materialize counterfactual scenes. ([source](https://arxiv.org/pdf/2611.06433v2), §3.2) |
| input_form | Image, Language | Original image, question, ground truth and target answer. ([source](https://arxiv.org/pdf/2611.06433v2), Alg.1) |
| output | Rendered Media | Curated edited image with QA metadata. ([source](https://arxiv.org/pdf/2611.06433v2), Alg.1) |
| model_type | VLM | Gemini verifier observes images and plans edits. ([source](https://arxiv.org/pdf/2611.06433v2), p.21) |
| model_training | Not Reported | Gemini API version named; adaptation not stated. Qwen training is separate. ([source](https://arxiv.org/pdf/2611.06433v2), Appendices E-F; training search) |
| planning | PO-2 | Model chooses edit type and ordered instructions within bounded loops. ([source](https://arxiv.org/pdf/2611.06433v2), Alg.1 lines 6-12) |
| workflow | Graph-Structured | Strict/relaxed/skip verification branches, retries and redraw fallback. ([source](https://arxiv.org/pdf/2611.06433v2), Alg.1) |
| update_strategy | Regeneration, Candidate Selection | Failed synthesis retries; quality failure advances edit type or instruction; redraw fallback. ([source](https://arxiv.org/pdf/2611.06433v2), pp.13-14) |
| verifier | Self, Human | Same V plans and verifies; human rejects final samples. ([source](https://arxiv.org/pdf/2611.06433v2), Alg.1, Appendix D.2) |
| feedback_assessment | Binary, Score | Three 1-5 scores plus semantic-equivalence and human approval gates. ([source](https://arxiv.org/pdf/2611.06433v2), Alg.1 lines 14-28) |
| feedback_observation | Visual | V compares original and edited images and answers blind questions. ([source](https://arxiv.org/pdf/2611.06433v2), §3.2) |
| memory_time | Short-Term Memory | Preservation regions and instruction list retained through subsequent calls. ([source](https://arxiv.org/pdf/2611.06433v2), Alg.1) |
| memory_reach | Local Memory | Local per-edit plan and retry counters. ([source](https://arxiv.org/pdf/2611.06433v2), Alg.1) |
| action_type | Tool/Function Call | Invoke editor with wrapped instruction and chosen edit mode. ([source](https://arxiv.org/pdf/2611.06433v2), Alg.1 Synth) |
| graphics_software | Agent-Adapted | Pipeline wraps editor modes and verification. ([source](https://arxiv.org/pdf/2611.06433v2), Alg.1) |
| tools | Perception models, Execution Utilities | GPT-Image-2 synthesis; UploadOSS storage. ([source](https://arxiv.org/pdf/2611.06433v2), Alg.1) |
| resources | Assets | VisCoR original images supply edit material. ([source](https://arxiv.org/pdf/2611.06433v2), Appendix D) |
| representation | Pixels | Original and edited raster images. ([source](https://arxiv.org/pdf/2611.06433v2), §3.2) |

Events: [{"type": "first_submission", "value": "2026-11-04T12:34:12+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2611.06433", "authority": "primary", "version": "v1", "evidence": "Official published timestamp, November 4 Chicago.", "prior_event_status": "not_seen_in_supplied_history"}, {"type": "revision", "value": "2026-11-05T06:45:33+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2611.06433", "authority": "primary", "version": "v2", "evidence": "Latest before frozen cutoff; November 5 Chicago, not a target-day update.", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: ["Generic raster content editing straddles Modeling/Visualization; Modeling here describes scene-content alteration rather than visual communication."]

### [ArtiVidRM: Verifiable Artifact-as-Rubric Reward Modeling for Explicit Quality Articulation in Video Generation](https://arxiv.org/abs/2611.07301)
core | Medium | new_relative_to_snapshot
Application: Dynamic / Animation and temporal scene; operations: Generation
Observable artifact lists support interpretable reward learning and two-round prompt repair; humans prefer refined Veo videos in 71% of comparisons, with 18% ties.
Scope: In the demonstrated two-round refinement application, model-chosen visual defects determine prompt feedback that changes subsequent video generation; simple fixed control rather than autonomous planning.
Limits: Only one feedback-conditioned regeneration demonstrated, not long-horizon agent planning. Fresh generation can introduce defects; small human evaluation. Principal paper contribution is the critic, so a narrower agent definition could treat this as enabling rather than core.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Animation | Refines generated video motion, rendering and temporal quality. ([source](https://arxiv.org/pdf/2611.07301v1), §4.3) |
| input_form | Language, Video | Initial generated video and original text prompt supplied to refinement. ([source](https://arxiv.org/pdf/2611.07301v1), §4.3) |
| output | Rendered Media | Second-round refined video. ([source](https://arxiv.org/pdf/2611.07301v1), §4.3) |
| model_type | VLM | Qwen3-VL-8B-Instruct backbone. ([source](https://arxiv.org/pdf/2611.07301v1), §4 p.6) |
| model_training | Supervised Fine-Tuning, RL Post-Training | Stage I supervised artifact training; Stage II GRPO with artifact and preference rewards. ([source](https://arxiv.org/pdf/2611.07301v1), §3.2) |
| planning | Not Applicable | Fixed two-round generation with no explicit task plan. ([source](https://arxiv.org/pdf/2611.07301v1), §4.3; full-text plan search) |
| workflow | Sequential | Initial video, critique, append feedback, regenerate. ([source](https://arxiv.org/pdf/2611.07301v1), §4.3) |
| update_strategy | Regeneration | Refined video is a fresh generation rather than edit. ([source](https://arxiv.org/pdf/2611.07301v1), p.9) |
| verifier | Critic | ArtiVidRM critiques separate Veo output. ([source](https://arxiv.org/pdf/2611.07301v1), §4.3) |
| feedback_assessment | Diagnosis | Artifact list becomes feedback; scalar reward use pertains to separate training. ([source](https://arxiv.org/pdf/2611.07301v1), §4.3) |
| feedback_observation | Visual | Visible generated-video defects inspected. ([source](https://arxiv.org/pdf/2611.07301v1), §4.3) |
| memory_time | Short-Term Memory | Original prompt and returned artifact list carried to next generation. ([source](https://arxiv.org/pdf/2611.07301v1), §4.3) |
| memory_reach | Local Memory | Feedback retained for local second-generation invocation. ([source](https://arxiv.org/pdf/2611.07301v1), §4.3) |
| action_type | Tool/Function Call | Invoke Veo with appended critique. ([source](https://arxiv.org/pdf/2611.07301v1), §4.3) |
| graphics_software | Agent-Adapted | Feedback loop wraps closed-source generator. ([source](https://arxiv.org/pdf/2611.07301v1), §4.3) |
| tools | Perception models | Veo-3.1 generation and ArtiVidRM diagnosis. ([source](https://arxiv.org/pdf/2611.07301v1), §4.3) |
| resources | Not Reported | No retrieved reusable resource specified for task-time loop. ([source](https://arxiv.org/pdf/2611.07301v1), §4.3, Appendices A-D; memory search) |
| representation | Pixels | Raster video input/output; no explicit 3D state. ([source](https://arxiv.org/pdf/2611.07301v1), §4.3) |

Events: [{"type": "first_submission", "value": "2026-11-05T01:37:25+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2611.07301", "authority": "primary", "version": "v1", "evidence": "Official timestamp converts to November 4 19:37:25 Chicago.", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: ["Core decision rests on demonstrated critique-conditioned generator action, not on reward-model training alone; preserve local-loop versus autonomous-planner distinction."]

### [Procedural Adversarial Learning](https://arxiv.org/abs/2611.06890)
scope_dependent | Medium | new_relative_to_snapshot
Application: Static / Scene, Datasets and Benchmarks; operations: Generation
Simple-PAT reduces cross-model worst-case error by geometric mean 3.15x over uniform training while exposing failures of foundation perception models.
Scope: Adaptive adversarial scene generation is a defensible transferable graphics-auditing mechanism, but actual controller is numerical CMA-ES, not an established agent system. Do not equate minimax optimization with agency.
Limits: Simplified 13–69-dimensional generators; finite search cannot certify true worst case, discontinuities hide failures, typical-case error can worsen. Transfer to actual graphics agents is untested.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Modeling | Procedurally configure objects, layout, lighting and static poses. ([source](https://arxiv.org/pdf/2611.06890v1), §3) |
| input_form | Not Applicable | Input is generator function, numeric losses and sampler hyperparameters. ([source](https://arxiv.org/pdf/2611.06890v1), Alg.1) |
| output | Rendered Media | Generator yields rendered image and ground-truth label. ([source](https://arxiv.org/pdf/2611.06890v1), §3) |
| model_type | Not Applicable | CMA-ES is zeroth-order optimizer; trained UNet is learner, not controller. ([source](https://arxiv.org/pdf/2611.06890v1), §4, Appendix A) |
| model_training | Not Applicable | Numerical sampler updates are CMA-ES; gradient training concerns learner. ([source](https://arxiv.org/pdf/2611.06890v1), §4) |
| planning | Not Applicable | Fixed optimization iteration without task plan. ([source](https://arxiv.org/pdf/2611.06890v1), Alg.1) |
| workflow | Parallel | 16 CMA-ES instances contribute samples to one batch before aggregate updates. ([source](https://arxiv.org/pdf/2611.06890v1), §4, Appendix A) |
| update_strategy | Candidate Selection | Fitness selects sampling distributions; least-fit instances replaced. ([source](https://arxiv.org/pdf/2611.06890v1), §4) |
| verifier | Programmatic | Compute numeric prediction error against procedural labels. ([source](https://arxiv.org/pdf/2611.06890v1), Alg.1 FITNESS) |
| feedback_assessment | Score | Task error plus separation fitness controls sampler updates. ([source](https://arxiv.org/pdf/2611.06890v1), pp.6-7) |
| feedback_observation | Structural Scene State | Prediction and label discrepancies and parameter-space distances. ([source](https://arxiv.org/pdf/2611.06890v1), Alg.1) |
| memory_time | Short-Term Memory | Mean/covariance and pooled two-generation fitness retained until reset. ([source](https://arxiv.org/pdf/2611.06890v1), §4) |
| memory_reach | Local Memory | Each sampler maintains its distribution. ([source](https://arxiv.org/pdf/2611.06890v1), §4) |
| action_type | Structured Specification | Parameter vector specifies procedural scene. ([source](https://arxiv.org/pdf/2611.06890v1), §3) |
| graphics_software | General-Purpose | Custom fast backend adapted from ProcFunc, not an agent interface. ([source](https://arxiv.org/pdf/2611.06890v1), §3.2) |
| tools | Graphics Operations | Generator creates objects and renders selected scene parameters. ([source](https://arxiv.org/pdf/2611.06890v1), §3, Alg.1) |
| resources | Assets | Anny human model, MakeHuman clothing and CMU pose archetypes. ([source](https://arxiv.org/pdf/2611.06890v1), §3.3) |
| representation | Geometry, Pixels | Explicit room/object/pose geometry rendered as images. ([source](https://arxiv.org/pdf/2611.06890v1), §3) |

Events: [{"type": "first_submission", "value": "2026-11-04T18:42:28+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2611.06890", "authority": "primary", "version": "v1", "evidence": "Canonical history; November 4 Chicago.", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: ["Numerical optimizer falls outside LLM/VLM model labels; sentinel does not imply absence of adaptive feedback. Preserve borderline rather than labeling every black-box search an agent."]

### [Interactive World Simulation with Cosmos for Physical AI](https://arxiv.org/abs/2611.06627)
enabling_or_adjacent | High | new_relative_to_snapshot
Application: Dynamic / Physical simulation and effects; operations: Generation
Unified streaming rendering recipe with measured latency boundaries and actual closed-loop policy experiment; calibrated apple-task success 27/32 versus native RTX 22/32.
Scope: Principal contribution is an explicit agent-facing observation renderer, not a new graphics action planner. Actual GR00T closed-loop simulator evaluation supports enabling scope beyond speculative transfer.
Limits: Policy comparison is calibration-set only, not held-out generalization; several checkpoints/appearance variants worsen. Transfer throughput often below real-time playback, and startup is expensive. Long rollouts hallucinate objects, deform geometry and drift. Camera/AV prerecorded controls do not alone demonstrate adaptive agent use.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Simulation | Generate observations for simulated robot policy experience. ([source](https://arxiv.org/pdf/2611.06627v1), §6) |
| input_form | Language, Video | Language appearance prompt and streaming depth/segmentation/edge/blur control frames. ([source](https://arxiv.org/pdf/2611.06627v1), §6.1) |
| output | Rendered Media | Four RGB observations per update. ([source](https://arxiv.org/pdf/2611.06627v1), p.38) |
| model_type | Not Applicable | Cosmos renders supplied controls; external policy chooses actions. ([source](https://arxiv.org/pdf/2611.06627v1), §6.1) |
| model_training | Not Applicable | Renderer undergoes RF/teacher-forcing/consistency/DMD training; policy separately fine-tuned. ([source](https://arxiv.org/pdf/2611.06627v1), §6.3) |
| planning | Not Applicable | Predict next chunk under supplied controls. ([source](https://arxiv.org/pdf/2611.06627v1), §4.1, §6.1; planner search) |
| workflow | Sequential | Encode controls, denoise chunk, refresh cache, decode and continue. ([source](https://arxiv.org/pdf/2611.06627v1), §6.4) |
| update_strategy | Not Applicable | Continues next chunk; no judge-driven repair. ([source](https://arxiv.org/pdf/2611.06627v1), §6.4) |
| verifier | Not Applicable | Quality and task-success metrics are final evaluation, not renderer critique. ([source](https://arxiv.org/pdf/2611.06627v1), §6.5) |
| feedback_assessment | Not Applicable | No per-chunk judgment changes rendering; completed output becomes history. ([source](https://arxiv.org/pdf/2611.06627v1), §6.4-6.5) |
| feedback_observation | Not Applicable | Depth is an input control, not verifier evidence. ([source](https://arxiv.org/pdf/2611.06627v1), §6.1) |
| memory_time | Short-Term Memory | 30-latent-frame cache, three sinks and decoder state persist within rollout. ([source](https://arxiv.org/pdf/2611.06627v1), pp.17-18,38) |
| memory_reach | Local Memory | Generator history and decoder state internal to renderer. ([source](https://arxiv.org/pdf/2611.06627v1), §4.1) |
| action_type | Not Applicable | Renderer consumes conditions and emits observations, not commands. ([source](https://arxiv.org/pdf/2611.06627v1), §6.1) |
| graphics_software | Agent-Adapted | Cosmos wrapper connects Isaac depth controls to policy RGB interface. ([source](https://arxiv.org/pdf/2611.06627v1), §6.5 Appendix C.4) |
| tools | Perception models | Causal Wan2.2 encoder/decoder and Cosmos generator. ([source](https://arxiv.org/pdf/2611.06627v1), §6.4) |
| resources | Not Reported | No asset/example/document retrieval inside renderer reported. ([source](https://arxiv.org/pdf/2611.06627v1), §6.4, Appendix C.4) |
| representation | Pixels, Learned State | Spatial control frames, RGB output, VAE latents and cached keys/values. ([source](https://arxiv.org/pdf/2611.06627v1), §6.1,6.4) |

Events: [{"type": "first_submission", "value": "2026-11-04T15:11:04+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2611.06627", "authority": "primary", "version": "v1", "evidence": "Official metadata; November 4 Chicago.", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: ["Enabling components should not inherit external policy taxonomy. Cache memory is represented, but renderer conditioning is not automatically verifier feedback."]

### [EmoReward: Self-Evolving Reward Calibration for Emotional Video Generation RL](https://arxiv.org/abs/2611.06518)
scope_dependent | Medium | new_relative_to_snapshot
Application: Dynamic / Animation and temporal scene; operations: Auditing
Between-run bounded reliability multipliers and instance validity gating improve selected video-quality metrics and ordinal human ratings without updating reward providers.
Scope: Useful experience-calibrated graphics reward mechanism, but paper expressly says Act does not generate or revise video. Numeric provider allocation and generator RL do not alone establish agent action on graphics; actual planner implementation is underspecified.
Limits: VideoAlign is both outcome/calibration target and reported metric; macro partly shares evaluator information. Only one reference-to-calibrated transition tested, not sustained evolution. Three channels constant in analyzed traces; image transfers and unequal training budgets show trade-offs. Planner identity unspecified.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Animation | Evaluates emotional gesture, expression and temporal motion in video generation. ([source](https://arxiv.org/pdf/2611.06518v1), §3) |
| input_form | Language, Video | Prompt p and generated video x. ([source](https://arxiv.org/pdf/2611.06518v1), Alg.1) |
| output | Not Applicable | Returns scalar total reward. ([source](https://arxiv.org/pdf/2611.06518v1), Alg.1 line 15) |
| model_type | Not Reported | Planner converts prompt to EmoScript but model or algorithm unspecified; named VLMs are scoring providers. ([source](https://arxiv.org/pdf/2611.06518v1), §3.3, Appendix C; planner/GPT/Qwen searches) |
| model_training | Not Reported | Providers frozen; generator RL specified; planner training not stated. ([source](https://arxiv.org/pdf/2611.06518v1), §3.3-3.5; full-text mechanism search) |
| planning | Unclear | Called Plan but EmoScript specifies affect targets and expression windows, not clear task steps. ([source](https://arxiv.org/pdf/2611.06518v1), §3.3) |
| workflow | Sequential | Ground, score, gate, look up and fuse; export table after completed reference run. ([source](https://arxiv.org/pdf/2611.06518v1), Algorithms 1-2) |
| update_strategy | Not Applicable | No video revisions; table remains frozen during subsequent run. ([source](https://arxiv.org/pdf/2611.06518v1), §3.3,3.5) |
| verifier | Programmatic | Correlation computes provider reliability against outcomes. ([source](https://arxiv.org/pdf/2611.06518v1), Algorithm 2) |
| feedback_assessment | Score | Correlations and centered reliability advantages tilt weights. ([source](https://arxiv.org/pdf/2611.06518v1), Eq.9-10) |
| feedback_observation | Structural Scene State | Recorded context, provider scores, gates and outcome y. ([source](https://arxiv.org/pdf/2611.06518v1), §3.5) |
| memory_time | Long-Term Memory | 3,232 completed-run traces create table reused in subsequent training. ([source](https://arxiv.org/pdf/2611.06518v1), §3.5 Appendix E) |
| memory_reach | Local Memory | Only fusion lookup consumes memory; providers remain unchanged and Plan independent. ([source](https://arxiv.org/pdf/2611.06518v1), Algorithm 1) |
| action_type | Not Applicable | Act does not generate or revise video; only scores. ([source](https://arxiv.org/pdf/2611.06518v1), §3.3) |
| graphics_software | Not Applicable | Returns reward to separate generator optimizer. ([source](https://arxiv.org/pdf/2611.06518v1), §3.2) |
| tools | Perception models | AU head, temporal vision-language encoder, R1-Omni, optical flow and VideoAlign. ([source](https://arxiv.org/pdf/2611.06518v1), Appendix C) |
| resources | Examples & Trajectories | Completed-run rollout traces calibrate reusable table. ([source](https://arxiv.org/pdf/2611.06518v1), Appendix E) |
| representation | Pixels | Videos scored as frames and clips. ([source](https://arxiv.org/pdf/2611.06518v1), Appendix C) |

Events: [{"type": "first_submission", "value": "2026-11-04T13:43:09+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2611.06518", "authority": "primary", "version": "v1", "evidence": "Official submission timestamp; November 4 Chicago.", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: ["Provider weighting called policy/action in paper is not automatically graphics agency. Numeric reward output lacks a dedicated taxonomy output label."]

## same_day_updates (1)

### [FLASH: A "Generate Once, Synthesize Many" Framework for Synthetic Anomaly Generation in Industrial Anomaly Detection](https://arxiv.org/abs/2609.37314)
core | High | new_relative_to_snapshot
Application: 2D Graphics; operations: Generation, Editing
Amortizes expensive generation by validated patch reuse; 78.1 image F1 versus 83.6 real-defect oracle on SuperADD.
Scope: VLM selects concrete defect, target and placement instructions that control image generation; schema/semantic rejection retries modify its specification. Validated images are selected for graphics reuse.
Limits: Full text reports estimated 13.8x speedup excluding VLM and extraction costs, unlike abstract-page 11.95x. Human rescue of rejected crops appears in supplement despite main text annotation-free wording. No cross-dataset validation; several simpler ablations improve pixel F1.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Modeling | Material-specific controlled content alteration of industrial images. ([source](https://arxiv.org/pdf/2609.37314v2), §3.1) |
| input_form | Image, Document | Normal image plus Config File with dataset context and constraints. ([source](https://arxiv.org/pdf/2609.37314v2), p.3) |
| output | Graphics Artifact | Reusable RGB crop, soft alpha mask and scale metadata. ([source](https://arxiv.org/pdf/2609.37314v2), Appendix G Storage) |
| model_type | VLM | Both VLM roles use Qwen2.5-VL-7B-Instruct. ([source](https://arxiv.org/pdf/2609.37314v2), pp.3-4) |
| model_training | Not Reported | Inference and frozen templates described, but no explicit controller adaptation statement. ([source](https://arxiv.org/pdf/2609.37314v2), Appendices A-B, G; fine-tun/frozen search) |
| planning | Not Applicable | Single defect specification, no represented multistep plan. ([source](https://arxiv.org/pdf/2609.37314v2), Appendix B) |
| workflow | Sequential | Generate, extract, validate, store. ([source](https://arxiv.org/pdf/2609.37314v2), Fig.1) |
| update_strategy | Regeneration, Candidate Selection | Rejected specs retried; accepted crops enter bank; invalid crops rejected. ([source](https://arxiv.org/pdf/2609.37314v2), pp.12,18-19) |
| verifier | Programmatic, Critic, Human | Schema/contrast checks; VLM-2 semantic check; human review of rejected crops. ([source](https://arxiv.org/pdf/2609.37314v2), Appendices B,G) |
| feedback_assessment | Binary, Diagnosis | Rejection reasons appended to retry; defect true/false gates storage. ([source](https://arxiv.org/pdf/2609.37314v2), pp.12,18-19) |
| feedback_observation | Visual, Structural Scene State | Normal/anomaly crops inspected; specification schema, contrast and category validity checked. ([source](https://arxiv.org/pdf/2609.37314v2), Appendices B,G) |
| memory_time | Short-Term Memory | Used defect names and rejection reasons retained for subsequent attempts. ([source](https://arxiv.org/pdf/2609.37314v2), p.12) |
| memory_reach | Local Memory | Specification role tracks duplicate names and rejection reasons. ([source](https://arxiv.org/pdf/2609.37314v2), Appendix B) |
| action_type | Structured Specification | Four structured fields inserted into generation template. ([source](https://arxiv.org/pdf/2609.37314v2), Appendix B) |
| graphics_software | Agent-Adapted | Custom template/config wrapper around image model. ([source](https://arxiv.org/pdf/2609.37314v2), §3.1) |
| tools | Perception models, Static Validator, Graphics Operations | Image model; schema/contrast validators; registration and crop extraction. ([source](https://arxiv.org/pdf/2609.37314v2), §3.1-3.3) |
| resources | Documentation & Rules, Assets | Config defect vocabulary and frozen rules; three normal donor images/category. ([source](https://arxiv.org/pdf/2609.37314v2), Appendix B) |
| representation | Pixels | Normal/anomaly RGB frames, masks and crops. ([source](https://arxiv.org/pdf/2609.37314v2), §3) |

Events: [{"type": "first_submission", "value": "2026-09-29T11:50:01+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2609.37314", "authority": "primary", "version": "v1", "evidence": "Official published.", "prior_event_status": "not_seen_in_supplied_history"}, {"type": "revision", "value": "2026-11-04T21:21:33+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2609.37314", "authority": "primary", "version": "v2", "evidence": "Canonical latest revision, November 4 Chicago.", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: ["Stored reusable defects are graphics resources, not automatically long-term agent memory."]

## late_discovery (0)

## date_unresolved (0)

## unresolved (3)

### [NeoWorld-Pro: Programming Interactive Scenes from Monocular Images for Embodied Simulation](https://arxiv.org/abs/2608.24212)
unresolved | Low | new_relative_to_snapshot
Application: Cross-category; operations: Unclear
Full text not read in this run; defer verified later-day revision.
Scope: Temporal routing only: canonical full history shows no November 4 Chicago or seven-day lookback event. Latest revision is November 5 local, before retrieval cutoff but after target day. Plausible graphics action remains unread; not a scope exclusion.
Limits: No scope/taxonomy decision from abstract alone.

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

Events: [{"type": "first_submission", "value": "2026-08-25T08:19:39+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2608.24212", "authority": "primary", "version": "v1", "evidence": "Canonical full submission history inspected.", "prior_event_status": "not_seen_in_supplied_history"}, {"type": "revision", "value": "2026-10-20T01:44:59+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2608.24212", "authority": "primary", "version": "v2", "evidence": "Canonical full submission history inspected.", "prior_event_status": "not_seen_in_supplied_history"}, {"type": "revision", "value": "2026-11-05T06:32:22+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2608.24212", "authority": "primary", "version": "v3", "evidence": "Canonical full submission history inspected.", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: []

### [WorldAct: Activating Monolithic 3D Worlds into Interactive-Ready Object-Centric Scenes](https://arxiv.org/abs/2605.15843)
unresolved | Low | known_discussed_paper
Application: Cross-category; operations: Unclear
Full text not read in this run; defer verified later-day revision.
Scope: Temporal routing only: canonical full history shows no November 4 Chicago or seven-day lookback event. Latest revision is November 5 local, before retrieval cutoff but after target day. Plausible graphics action remains unread; not a scope exclusion.
Limits: No scope/taxonomy decision from abstract alone.

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

Events: [{"type": "first_submission", "value": "2026-05-15T10:56:23+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2605.15843", "authority": "primary", "version": "v1", "evidence": "Canonical full submission history inspected.", "prior_event_status": "not_seen_in_supplied_history"}, {"type": "revision", "value": "2026-11-05T07:15:15+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2605.15843", "authority": "primary", "version": "v2", "evidence": "Canonical full submission history inspected.", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: []

### [EvoDesign: Agentic Editable Diagram Creation via Design Expertise Evolution](https://arxiv.org/abs/2604.09568)
unresolved | Low | known_discussed_paper
Application: Cross-category; operations: Unclear
Full text not read in this run; defer verified later-day revision.
Scope: Temporal routing only: canonical full history shows no November 4 Chicago or seven-day lookback event. Latest revision is November 5 local, before retrieval cutoff but after target day. Plausible graphics action remains unread; not a scope exclusion.
Limits: No scope/taxonomy decision from abstract alone.

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

Events: [{"type": "first_submission", "value": "2026-02-20T11:11:02+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2604.09568", "authority": "primary", "version": "v1", "evidence": "Canonical full submission history inspected.", "prior_event_status": "not_seen_in_supplied_history"}, {"type": "revision", "value": "2026-10-05T17:32:59+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2604.09568", "authority": "primary", "version": "v2", "evidence": "Canonical full submission history inspected.", "prior_event_status": "not_seen_in_supplied_history"}, {"type": "revision", "value": "2026-11-05T18:18:33+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2604.09568", "authority": "primary", "version": "v3", "evidence": "Canonical full submission history inspected.", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: []

## excluded (0)

## Application index
| Application | Papers |
|---|---|
| 2D Graphics | [LongBanana: An Expert-Verified Benchmark for Long-Context Multi-Reference Image Synthesis](https://arxiv.org/abs/2611.06856) [same_day_new]; [DreamRealm: Exploring and Materializing Hallucination Worlds for Trustworthy Vision-Language Models](https://arxiv.org/abs/2611.06433) [same_day_new]; [FLASH: A "Generate Once, Synthesize Many" Framework for Synthetic Anomaly Generation in Industrial Anomaly Detection](https://arxiv.org/abs/2609.37314) [same_day_updates] |
| Static / Object | None verified in this run |
| Static / CAD | None verified in this run |
| Static / Scene | [Procedural Adversarial Learning](https://arxiv.org/abs/2611.06890) [same_day_new] |
| Dynamic / Articulated assets | None verified in this run |
| Dynamic / Animation and temporal scene | [EvoWorld: Towards Out-of-Sight World Evolution in Generative Video Models](https://arxiv.org/abs/2611.06748) [same_day_new]; [ArtiVidRM: Verifiable Artifact-as-Rubric Reward Modeling for Explicit Quality Articulation in Video Generation](https://arxiv.org/abs/2611.07301) [same_day_new]; [EmoReward: Self-Evolving Reward Calibration for Emotional Video Generation RL](https://arxiv.org/abs/2611.06518) [same_day_new] |
| Dynamic / Physical simulation and effects | [Interactive World Simulation with Cosmos for Physical AI](https://arxiv.org/abs/2611.06627) [same_day_new] |
| Datasets and Benchmarks | [LongBanana: An Expert-Verified Benchmark for Long-Context Multi-Reference Image Synthesis](https://arxiv.org/abs/2611.06856) [same_day_new]; [DreamRealm: Exploring and Materializing Hallucination Worlds for Trustworthy Vision-Language Models](https://arxiv.org/abs/2611.06433) [same_day_new]; [Procedural Adversarial Learning](https://arxiv.org/abs/2611.06890) [same_day_new] |
| Cross-category | [NeoWorld-Pro: Programming Interactive Scenes from Monocular Images for Embodied Simulation](https://arxiv.org/abs/2608.24212) [unresolved]; [WorldAct: Activating Monolithic 3D Worlds into Interactive-Ready Object-Centric Scenes](https://arxiv.org/abs/2605.15843) [unresolved]; [EvoDesign: Agentic Editable Diagram Creation via Design Expertise Evolution](https://arxiv.org/abs/2604.09568) [unresolved] |

## Source ledger
| Source | Status | Checked pages / queries | Limitations |
|---|---|---|---|
| arxiv | partial | [{"query_or_url": "https://arxiv.org/list/cs.GR/new?skip=0&show=100", "checked_at": "2026-11-07T21:44:52.746867+00:00", "outcome": "16 entries; scan observed pagination complete=True; errors=[]; unvisited=[]"}, {"query_or_url": "https://arxiv.org/list/cs.GR/recent?skip=0&show=100", "checked_at": "2026-11-07T21:44:52.816084+00:00", "outcome": "43 entries; scan observed pagination complete=True; errors=[]; unvisited=[]"}, {"query_or_url": "https://arxiv.org/list/cs.CV/new?skip=0&show=100", "checked_at": "2026-11-07T21:44:53.079809+00:00", "outcome": "100 entries; scan observed pagination complete=True; errors=[]; unvisited=[]"}, {"query_or_url": "https://arxiv.org/list/cs.CV/new?skip=0&show=2000", "checked_at": "2026-11-07T21:44:53.331347+00:00", "outcome": "258 entries; scan observed pagination complete=True; errors=[]; unvisited=[]"}, {"query_or_url": "https://arxiv.org/list/cs.CV/recent?skip=0&show=100", "checked_at": "2026-11-07T21:44:53.460116+00:00", "outcome": "100 entries; scan observed pagination complete=True; errors=[]; unvisited=[]"}, {"query_or_url": "https://arxiv.org/list/cs.CV/recent?skip=0&show=2000", "checked_at": "2026-11-07T21:44:54.497228+00:00", "outcome": "943 entries; scan observed pagination complete=True; errors=[]; unvisited=[]"}, {"query_or_url": "https://arxiv.org/abs/2611.06856", "checked_at": "2026-11-07T21:52:44.292078+00:00", "outcome": "Canonical paper/history or official project inspected; stored observation available."}, {"query_or_url": "https://arxiv.org/abs/2611.06748", "checked_at": "2026-11-07T21:53:49.356340+00:00", "outcome": "Canonical paper/history or official project inspected; stored observation available."}, {"query_or_url": "https://arxiv.org/abs/2611.06433", "checked_at": "2026-11-07T21:54:52.983448+00:00", "outcome": "Canonical paper/history or official project inspected; stored observation available."}, {"query_or_url": "https://arxiv.org/abs/2611.07301", "checked_at": "2026-11-07T21:55:48.965317+00:00", "outcome": "Canonical paper/history or official project inspected; stored observation available."}, {"query_or_url": "https://arxiv.org/abs/2611.06890", "checked_at": "2026-11-07T21:56:43.574074+00:00", "outcome": "Canonical paper/history or official project inspected; stored observation available."}, {"query_or_url": "https://arxiv.org/abs/2609.37314", "checked_at": "2026-11-07T21:57:38.168457+00:00", "outcome": "Canonical paper/history or official project inspected; stored observation available."}, {"query_or_url": "https://arxiv.org/abs/2608.24212", "checked_at": "2026-11-07T21:58:35.823137+00:00", "outcome": "Canonical paper/history or official project inspected; stored observation available."}, {"query_or_url": "https://arxiv.org/abs/2605.15843", "checked_at": "2026-11-07T21:58:51.990810+00:00", "outcome": "Canonical paper/history or official project inspected; stored observation available."}, {"query_or_url": "https://arxiv.org/abs/2604.09568", "checked_at": "2026-11-07T21:58:52.084536+00:00", "outcome": "Canonical paper/history or official project inspected; stored observation available."}, {"query_or_url": "https://arxiv.org/abs/2611.06627", "checked_at": "2026-11-07T21:59:15.550556+00:00", "outcome": "Canonical paper/history or official project inspected; stored observation available."}, {"query_or_url": "https://arxiv.org/abs/2611.06518", "checked_at": "2026-11-07T22:00:29.717005+00:00", "outcome": "Canonical paper/history or official project inspected; stored observation available."}] | Four required listing pagination chains completed with no errors or unvisited links. All 1062 listing IDs resolved. Target/uncertain 247 and catchup attention 334 abstracts delivered and triaged. Other categories not scanned; remaining catalog records and some outside-window title hints not fully reviewed. Listings are current observations, not historical availability proof. |
| hugging_face | partial | [{"query_or_url": "https://huggingface.co/papers/date/2026-11-04", "checked_at": "2026-11-07T21:44:54.821837+00:00", "outcome": "Daily page inspected as lead source; curation date is not publication date. Selected leads batch-resolved."}] | One daily page only; not an exhaustive feed history. Selected image/world/curation leads resolved, others remain source signals. |
| openreview | partial | [{"query_or_url": "agent CAD generation reconstruction editing constraint solver program repair November 2026 site:openreview.net", "checked_at": "2026-11-07T21:46:02.964525+00:00", "outcome": "Search returned grounded leads; dates and scope are not established from snippets. See tool-events.jsonl."}] | One hosted site-restricted search; no exhaustive venue/API enumeration or new OpenReview PDF reads. |
| official_venues | partial | [{"query_or_url": "agent graphics benchmark world auditing verification 2026 site:openaccess.thecvf.com", "checked_at": "2026-11-07T21:48:25.046150+00:00", "outcome": "Search returned grounded leads; dates and scope are not established from snippets. See tool-events.jsonl."}, {"query_or_url": "agent 3D object procedural modeling Blender material inverse graphics geometry editing 2026 November", "checked_at": "2026-11-07T21:45:31.706039+00:00", "outcome": "Search returned grounded leads; dates and scope are not established from snippets. See tool-events.jsonl."}] | Hosted CVF/proceedings search and observed citations only; no exhaustive official conference release calendar checked. |
| project_author_lab | partial | [{"query_or_url": "https://long-banana.com/", "checked_at": "2026-11-07T21:52:50.370371+00:00", "outcome": "Canonical paper/history or official project inspected; stored observation available."}, {"query_or_url": "agent 3D scene layout world generation BIM architecture October November 2026 project", "checked_at": "2026-11-07T21:46:24.230736+00:00", "outcome": "Search returned grounded leads; dates and scope are not established from snippets. See tool-events.jsonl."}, {"query_or_url": "agent physical simulation particle effects deformable world generation research project lab 2026", "checked_at": "2026-11-07T21:48:03.104382+00:00", "outcome": "Search returned grounded leads; dates and scope are not established from snippets. See tool-events.jsonl."}, {"query_or_url": "graphics agent memory replanning tool interface feedback program synthesis November 2026 github project", "checked_at": "2026-11-07T21:48:50.584066+00:00", "outcome": "Search returned grounded leads; dates and scope are not established from snippets. See tool-events.jsonl."}] | Broad hosted searches and LongBanana project page only; other labs and repositories not exhaustively checked. |

## Query coverage
- 2d: partial; [{'query_or_url': 'agent SVG diagram chart slide poster editable visual feedback November 4 2026 October 29 2026', 'checked_at': '2026-11-07T21:45:15.367634+00:00', 'outcome': 'Search returned grounded leads; dates and scope are not established from snippets. See tool-events.jsonl.'}]
- object: partial; [{'query_or_url': 'agent 3D object procedural modeling Blender material inverse graphics geometry editing 2026 November', 'checked_at': '2026-11-07T21:45:31.706039+00:00', 'outcome': 'Search returned grounded leads; dates and scope are not established from snippets. See tool-events.jsonl.'}]
- cad: partial; [{'query_or_url': 'agent CAD generation reconstruction editing constraint solver program repair November 2026 site:openreview.net', 'checked_at': '2026-11-07T21:46:02.964525+00:00', 'outcome': 'Search returned grounded leads; dates and scope are not established from snippets. See tool-events.jsonl.'}]
- scene: partial; [{'query_or_url': 'agent 3D scene layout world generation BIM architecture October November 2026 project', 'checked_at': '2026-11-07T21:46:24.230736+00:00', 'outcome': 'Search returned grounded leads; dates and scope are not established from snippets. See tool-events.jsonl.'}]
- articulation: partial; [{'query_or_url': 'agent articulated asset joint mechanism rig generation research', 'checked_at': '2026-11-07T21:47:26.535363+00:00', 'outcome': 'Search returned grounded leads; dates and scope are not established from snippets. See tool-events.jsonl.'}]
- animation: partial; [{'query_or_url': 'agent animation cutscene temporal scene cinematography November 4 2026 October 29 2026', 'checked_at': '2026-11-07T21:47:44.518832+00:00', 'outcome': 'Search returned grounded leads; dates and scope are not established from snippets. See tool-events.jsonl.'}]
- simulation: partial; [{'query_or_url': 'agent physical simulation particle effects deformable world generation research project lab 2026', 'checked_at': '2026-11-07T21:48:03.104382+00:00', 'outcome': 'Search returned grounded leads; dates and scope are not established from snippets. See tool-events.jsonl.'}]
- benchmark: partial; [{'query_or_url': 'agent graphics benchmark world auditing verification 2026 site:openaccess.thecvf.com', 'checked_at': '2026-11-07T21:48:25.046150+00:00', 'outcome': 'Search returned grounded leads; dates and scope are not established from snippets. See tool-events.jsonl.'}]
- harness: partial; [{'query_or_url': 'graphics agent memory replanning tool interface feedback program synthesis November 2026 github project', 'checked_at': '2026-11-07T21:48:50.584066+00:00', 'outcome': 'Search returned grounded leads; dates and scope are not established from snippets. See tool-events.jsonl.'}]

## Source-derived candidate coverage

Mechanical audit of collected arXiv titles; relevance and semantic correctness require paper evidence.

- Metadata resolved: 1062 / 1062 collected IDs.
- Target-day / history-uncertain candidates: 247.
- Explicit triage decisions: 247; catalog-page delivery: 247.
- Missing source scans: 0; incomplete scans: 0.
- Unresolved metadata: 0; no triage decision: 0.
- Full candidate IDs and remaining gaps: `coverage-audit.json`. Unreviewed entries are not exclusions.
- Other platforms remain governed by the source ledger; this audit is not exhaustive discovery.

## Borderline graphics contributions

These records are not established core agentic systems. They remain visible with their scope uncertainty.

| Paper | Why borderline |
|---|---|
| Procedural Adversarial Learning | Adaptive adversarial scene generation is a defensible transferable graphics-auditing mechanism, but actual controller is numerical CMA-ES, not an established agent system. Do not equate minimax optimization with agency. |
| EmoReward: Self-Evolving Reward Calibration for Emotional Video Generation RL | Useful experience-calibrated graphics reward mechanism, but paper expressly says Act does not generate or revise video. Numeric provider allocation and generator RL do not alone establish agent action on graphics; actual planner implementation is underspecified. |

## Agent-to-graphics evidence

| Paper | Status | Controller | Action / decision | Graphics target | Source |
|---|---|---|---|---|---|
| LongBanana: An Expert-Verified Benchmark for Long-Context Multi-Reference Image Synthesis | core | Claude Sonnet 4.6 in OpenClaw + RPR | Select reference evidence, schedule generation/editing calls, inspect and repair drafts | Multi-reference composite raster image | [pp.7,33,36](https://arxiv.org/pdf/2611.06856v1) |
| EvoWorld: Towards Out-of-Sight World Evolution in Generative Video Models | core | Qwen3.8-27B world brain | Infer reaction and issue concrete next-segment prompt from observed event | Rendered temporal scene and off-screen character state | [pp.8,17-18](https://arxiv.org/pdf/2611.06748v2) |
| DreamRealm: Exploring and Materializing Hallucination Worlds for Trustworthy Vision-Language Models | core | Gemini 2.5 Pro planner/verifier in bounded orchestration | Select local/global editing or redraw, generate three ordered edit instructions, gate attempts using image checks | Original and counterfactual raster images | [pp.13-14,21](https://arxiv.org/pdf/2611.06433v2) |
| ArtiVidRM: Verifiable Artifact-as-Rubric Reward Modeling for Explicit Quality Articulation in Video Generation | core | ArtiVidRM critic within fixed feedback-appending controller | Choose visible defects to condition next generation | Veo-generated video | [§4.3 p.9](https://arxiv.org/pdf/2611.07301v1) |
| Procedural Adversarial Learning | scope_dependent | Numerical CMA-ES adversary; agent status unestablished | Select generator parameter vectors from loss feedback | PAL-Dojo scene geometry, lighting, poses and resulting images | [§4 p.6](https://arxiv.org/pdf/2611.06890v1) |
| FLASH: A "Generate Once, Synthesize Many" Framework for Synthetic Anomaly Generation in Industrial Anomaly Detection | core | Qwen2.5-VL-7B-Instruct specification and validation roles | Choose defect and where to introduce it; revise rejected specification; admit or reject generated crops | Counterfactual industrial image defects and reusable crop bank | [§3.1, Appendix B](https://arxiv.org/pdf/2609.37314v2) |
| Interactive World Simulation with Cosmos for Physical AI | enabling_or_adjacent | External GR00T N1.7 policy; Cosmos is enabling observation component | Robot actions advance Isaac physics, whose depth controls condition new RGB observations for next policy action | Simulated scene appearance rendered as video observations | [pp.36,38,75-77](https://arxiv.org/pdf/2611.06627v1) |
| EmoReward: Self-Evolving Reward Calibration for Emotional Video Generation RL | scope_dependent | Rule-based Reflect/Evolve allocator and unspecified EmoScript planner | Gate and reweight quality evidence; emit scalar reward to external RL optimizer | Emotional quality of generated video | [§§3.3-3.5, Appendix A](https://arxiv.org/pdf/2611.06518v1) |

## Prior-day memory and carry-over

Frozen history: `knowledge/daily-history/through-20261015-bvb-v11`. Previously unread records now fully read: 0. Prior pending records still without a new full read: 95.

See history-delta.json for per-paper transitions. Historical results remain in the frozen bundle; not repeated is not excluded, and new-to-history does not mean newly published.

## Abstract-first reading queue

Attention pool: 337; abstracts not delivered: 0; priority/triage gaps: 0; unread ranked leads: 46. See reading-plan.json for model-authored priorities and deferred leads. Priority is not an inclusion judgment or recall guarantee.
