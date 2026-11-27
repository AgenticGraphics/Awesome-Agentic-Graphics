# Agentic Graphics daily report
Date: 2026-11-27 | Timezone: America/Chicago | As of: 2026-11-27T19:58:40+00:00
browser-based same-day search; documented source coverage
Taxonomy: survey-taxonomy-snapshot-2026-10-15 | Snapshot: bundled_snapshot_not_live_refreshed

## Coverage limits
- Today covers November 27, 2026 midnight through 13:58:40 America/Chicago, frozen at the actual start clock.
- No qualifying same-day Agentic Graphics paper was verified in the browsed source set. Indexing lag, inaccessible pages and selective reading limit this statement.
- The 10 search-batch and 24 primary-open caps stopped retrieval before the approximate six-minute allowance; journal elapsed time is not padded.
- All nine query families and five source families were attempted using broad, dated, category and known-alias queries. Coverage is partial.
- Seven arXiv categories reached; new pages showed November 26 listings. CV recent returned entries 1–50 of 1468. Only selected excerpts and keyword matches were inspected.
- HF dated November 27 URL was inaccessible; root showed Nov 27. Dated search fallback returned November 26 and other pages, not a verified November 27 date page.
- OpenReview direct search was inaccessible; site searches returned older papers. SIGGRAPH Asia overview reached, with ACM and CVF searches, without proceedings-wide reading.
- Six candidates freshly screened: five core from selected method passages, one scope-dependent from its abstract. Other plausible leads remain pending.
- November 20–26 is the separate seven-day catch-up lane. First submissions are not public announcement or formal-publication dates.
- Direct earlier main reports and supplied website records are identity/event history only. Previous-run evidence archives were not recursively consulted.
- No empirical reproduction or revision-content comparison. Unclear preserves missing evidence; offline scores and training rewards are not in-loop verification.
- Frozen October 15 snapshot remains bundled_snapshot_not_live_refreshed; Tools labels are provisional and memory wording remains inconsistent.
- Batch family associations describe retrieval intent, not that every result belongs to every associated family.

No qualifying same-day Agentic Graphics paper was verified in the browsed source set.
Coverage is limited to the sources and queries below; unpublished or unindexed papers may be missing.

## Execution and event comparison
Window: 2026-11-27T00:00:00-06:00 through 2026-11-27T13:58:40-06:00. Same-day new: 0; updates: 0. Retrieval: 10 batches / 30 queries / 24 attempted opens in 94 seconds.
The helper groups verified older events under late_discovery; the table separates new-to-us catch-up from previously reported events.

| Paper | Discovery status | Verified Chicago events |
|---|---|---|
| Nemotron-Labs-VisualCreation: Pixel as Code for Agentic Visual Creation | new_to_us_catch_up | v1 first_submission 2026-11-23T12:57:41-06:00 (not_seen_in_supplied_history) |
| Agentic LongLive: Asynchronous Agentic Memory for Long Video Generation | new_to_us_catch_up | v1 first_submission 2026-11-25T12:54:03-06:00 (not_seen_in_supplied_history) |
| SemProxy: Semantic 3D Proxies for Controllable Agentic 3D Modeling | new_to_us_catch_up | v1 first_submission 2026-11-25T08:08:05-06:00 (not_seen_in_supplied_history) |
| Connecting AI Agents to Live Discrete Element Simulations via the Model Context Protocol | new_to_us_catch_up | v1 first_submission 2026-11-25T01:46:35-06:00 (not_seen_in_supplied_history) |
| Real2SimLab: A Unified Platform for Real-to-Simulation Transfer | new_to_us_catch_up | v1 first_submission 2026-11-25T12:23:41-06:00 (not_seen_in_supplied_history) |
| FineDex: Bridging Fine-Grained Human-Object Interaction Generation to Dexterous Humanoid Manipulation | new_to_us_catch_up | v1 first_submission 2026-11-25T12:40:47-06:00 (not_seen_in_supplied_history) |

## already_reported (0)

## same_day_new (0)

## same_day_updates (0)

## late_discovery (6)

### [Nemotron-Labs-VisualCreation: Pixel as Code for Agentic Visual Creation](https://arxiv.org/abs/2611.31358)
core | High | new_relative_to_snapshot
Application: 2D Graphics; operations: Generation, Editing
An authoring harness coordinates raster and structured artifacts with rendered audits and targeted repairs.
Scope: An authoring harness coordinates raster and structured artifacts with rendered audits and targeted repairs.
Limits: Selected method passages only; generator training is separate from planner adaptation.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Visualization | Creates visual designs. ([source](https://arxiv.org/html/2611.31358v1), Section 2, repair examples) |
| input_form | Language, Image | Requests and reference images condition generation. ([source](https://arxiv.org/html/2611.31358v1), Section 3.1–3.2) |
| output | Program, Rendered Media | Editable code and rendered previews. ([source](https://arxiv.org/html/2611.31358v1), Section 2, checkpoint retention) |
| model_type | Hybrid | Language planner and multimodal audit roles. ([source](https://arxiv.org/html/2611.31358v1), Section 3.1; Section 2 visual audit) |
| model_training | Unclear |  |
| planning | PO-2 | Routing constraints coexist with generated plans. ([source](https://arxiv.org/html/2611.31358v1), Section 3.1) |
| workflow | Graph-Structured | Repair branches by causal owner. ([source](https://arxiv.org/html/2611.31358v1), Section 2, targeted repair) |
| update_strategy | Local Patch, Regeneration, Replanning, Candidate Selection | Localized fixes, asset redraws and incumbent comparison. ([source](https://arxiv.org/html/2611.31358v1), Section 2, targeted repair) |
| verifier | Critic, Programmatic | Multimodal review and renderer guards. ([source](https://arxiv.org/html/2611.31358v1), Section 2, visual audit) |
| feedback_assessment | Binary, Ranking, Diagnosis | Pass gates, pairwise choice and causal findings. ([source](https://arxiv.org/html/2611.31358v1), Section 2, visual audit and selection) |
| feedback_observation | Visual, Runtime | Rendered artifacts and execution errors guide repair. ([source](https://arxiv.org/html/2611.31358v1), Section 2, visual audit) |
| memory_time | Short-Term Memory | Checkpoints persist across repair rounds. ([source](https://arxiv.org/html/2611.31358v1), Section 2, checkpoint retention) |
| memory_reach | Unclear |  |
| action_type | Code/Script, Structured Specification | Programs and layout contracts drive rendering. ([source](https://arxiv.org/html/2611.31358v1), Section 3.1; Section 2) |
| graphics_software | Unclear |  |
| tools | Execution Utilities, Perception models, Static Validator | Renderer, multimodal review and fatal guards. ([source](https://arxiv.org/html/2611.31358v1), Section 2, visual audit) |
| resources | Unclear |  |
| representation | Code, Layouts, Pixels, Learned State | Programs, bounded regions, rendered pixels and raster tokens. ([source](https://arxiv.org/html/2611.31358v1), Section 3.1–3.2) |

next_action: "Review full method and survey suitability before corpus inclusion."

Events: [{"type": "first_submission", "value": "2026-11-23T18:57:41+00:00", "precision": "timestamp", "timezone": "UTC", "raw_source_value": "Mon, 23 Nov 2026 18:57:41 UTC", "raw_source_timezone": "UTC", "local_value": "2026-11-23T12:57:41-06:00", "primary_url": "https://arxiv.org/abs/2611.31358", "authority": "primary", "version": "v1", "evidence": "arXiv submission history reports v1 at the preserved UTC timestamp.", "locator": "Submission history, v1", "raw_evidence_archive": "retrieval/04.json", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: ["Generator fine-tuning does not establish planner adaptation. Web retrieval falls outside the provisional graphics tools labels."]

### [Agentic LongLive: Asynchronous Agentic Memory for Long Video Generation](https://arxiv.org/abs/2611.34907)
core | High | new_relative_to_snapshot
Application: Dynamic / Animation and temporal scene; operations: Generation
A memory agent prepares entity state and images alongside video generation, committing them for later shots.
Scope: A memory agent prepares entity state and images alongside video generation, committing them for later shots.
Limits: Main narrative system is open-loop with respect to generated video; observation-based robot variants differ. Training variants are not interchangeable.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Animation | Produces long videos. ([source](https://arxiv.org/html/2611.34907v1), Section 2.2) |
| input_form | Language | Revealed prompts select remembered entities. ([source](https://arxiv.org/html/2611.34907v1), Section 2.2, entity cards) |
| output | Rendered Media | DiT workers generate video. ([source](https://arxiv.org/html/2611.34907v1), Section 2.2, L175) |
| model_type | VLM | Agent ranks host a vision-language model. ([source](https://arxiv.org/html/2611.34907v1), Section 2.2, L175) |
| model_training | Unclear |  |
| planning | Unclear |  |
| workflow | Parallel | Agent, decoder and generator run concurrently. ([source](https://arxiv.org/html/2611.34907v1), Section 2.2, L175) |
| update_strategy | Regeneration, Local Patch | Changed entities redraw or edit prior images. ([source](https://arxiv.org/html/2611.34907v1), Appendix C, entity layer L654–655) |
| verifier | Unclear |  |
| feedback_assessment | Unclear |  |
| feedback_observation | Visual | Entity images are checked before repair. ([source](https://arxiv.org/html/2611.34907v1), Appendix C, entity layer) |
| memory_time | Short-Term Memory | Entity states and location images persist across shots. ([source](https://arxiv.org/html/2611.34907v1), Section 2.2, entity cards and location recall) |
| memory_reach | Unclear |  |
| action_type | Structured Specification | Planner writes structured memory and prompt text. ([source](https://arxiv.org/html/2611.34907v1), Appendix A, asynchronous agents) |
| graphics_software | Unclear |  |
| tools | Perception models | Image model draws memory images. ([source](https://arxiv.org/html/2611.34907v1), Section 2.2, L175) |
| resources | Assets | Previously drawn entity and place images are reused. ([source](https://arxiv.org/html/2611.34907v1), Section 2.2, location recall) |
| representation | Pixels, Learned State | Memory images are encoded into sink K/V. ([source](https://arxiv.org/html/2611.34907v1), Section 2.2, L175) |

artifact_links: [{"url": "https://nvlabs.github.io/LongLive/Agentic-LongLive/", "role": "official project; reached", "raw_evidence_archive": "retrieval/07.json"}]

next_action: "Review full method and survey suitability before corpus inclusion."

Events: [{"type": "first_submission", "value": "2026-11-25T18:54:03+00:00", "precision": "timestamp", "timezone": "UTC", "raw_source_value": "Wed, 25 Nov 2026 18:54:03 UTC", "raw_source_timezone": "UTC", "local_value": "2026-11-25T12:54:03-06:00", "primary_url": "https://arxiv.org/abs/2611.34907", "authority": "primary", "version": "v1", "evidence": "arXiv submission history reports v1 at the preserved UTC timestamp.", "locator": "Submission history, v1", "raw_evidence_archive": "retrieval/06.json", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: ["Cross-shot persistence is within a session, not evidence of cross-run Long-Term Memory. RL reward judges are not automatically inference verifiers. Main and robot-observation variants must remain separate."]

### [SemProxy: Semantic 3D Proxies for Controllable Agentic 3D Modeling](https://arxiv.org/abs/2611.34414)
core | High | new_relative_to_snapshot
Application: Static / Object, Static / Scene; operations: Generation, Editing
Editable semantic bounding boxes provide a shared control interface for users and coding agents constructing Blender models.
Scope: Editable semantic bounding boxes provide a shared control interface for users and coding agents constructing Blender models.
Limits: The representation fixes inputs; planning and geometry strategy depend on the selected harness. User study has seven participants. Continuing a session does not specify whether edits patch or regenerate geometry.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Modeling | Agents construct 3D models. ([source](https://arxiv.org/html/2611.34414v1), Section 3.3) |
| input_form | Language, Image, 3D Representation | Text, images and labeled boxes enter the workspace. ([source](https://arxiv.org/html/2611.34414v1), Section 3.3 L165) |
| output | Program, Graphics Artifact, Rendered Media | Workspace stores scripts, models and renders. ([source](https://arxiv.org/html/2611.34414v1), Section 3.3 L166) |
| model_type | Unclear |  |
| model_training | Off-the-Shelf | Three agents run unmodified. ([source](https://arxiv.org/html/2611.34414v1), Section 4, implementation) |
| planning | Unclear |  |
| workflow | Unclear |  |
| update_strategy | Unclear |  |
| verifier | Human | User reviews and accepts drafted boxes. ([source](https://arxiv.org/html/2611.34414v1), Section 3.4) |
| feedback_assessment | Unclear |  |
| feedback_observation | Visual, Structural Scene State | Proxy renders and box inputs guide refinement. ([source](https://arxiv.org/html/2611.34414v1), Section 3.3–3.4) |
| memory_time | Short-Term Memory | Same agent session continues after user changes. ([source](https://arxiv.org/html/2611.34414v1), Section 3.3 L167) |
| memory_reach | Unclear |  |
| action_type | Code/Script | Blender Python constructs geometry. ([source](https://arxiv.org/html/2611.34414v1), Section 3.3 L168) |
| graphics_software | General-Purpose | Agent drives native Blender Python. ([source](https://arxiv.org/html/2611.34414v1), Section 3.3 L168) |
| tools | Graphics Operations | Blender API constructs geometry. ([source](https://arxiv.org/html/2611.34414v1), Section 3.3 L168) |
| resources | Unclear |  |
| representation | Geometry, Code, Pixels | Boxes, scripts and renders share a workspace. ([source](https://arxiv.org/html/2611.34414v1), Section 3.3) |

next_action: "Review full method and survey suitability before corpus inclusion."

Events: [{"type": "first_submission", "value": "2026-11-25T14:08:05+00:00", "precision": "timestamp", "timezone": "UTC", "raw_source_value": "Wed, 25 Nov 2026 14:08:05 UTC", "raw_source_timezone": "UTC", "local_value": "2026-11-25T08:08:05-06:00", "primary_url": "https://arxiv.org/abs/2611.34414", "authority": "primary", "version": "v1", "evidence": "arXiv submission history reports v1 at the preserved UTC timestamp.", "locator": "Submission history, v1", "raw_evidence_archive": "retrieval/06.json", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: ["Do not assign one planning policy to a deliberately harness-independent input representation."]

### [Connecting AI Agents to Live Discrete Element Simulations via the Model Context Protocol](https://arxiv.org/abs/2611.33926)
core | High | new_relative_to_snapshot
Application: Dynamic / Physical simulation and effects, Cross-category; operations: Generation, Editing
An MCP bridge lets a language agent inspect and modify a running discrete-element simulation shared with a human modeler.
Scope: An MCP bridge lets a language agent inspect and modify a running discrete-element simulation shared with a human modeler.
Limits: Evidence concerns simulation tooling and selected PFC/YADE examples; no claim of visual-effects quality or general benchmark superiority.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Simulation | Operates live particle engines. ([source](https://arxiv.org/html/2611.33926v1), Section 2, agentic loop) |
| input_form | Language | Modeler communicates requests in language. ([source](https://arxiv.org/html/2611.33926v1), Section 2, Figure 1 text) |
| output | Program, Graphics Artifact | Workspace retains scripts and saved models. ([source](https://arxiv.org/html/2611.33926v1), Section 2 L119) |
| model_type | LLM | Language model chooses tools and reads results. ([source](https://arxiv.org/html/2611.33926v1), Section 2 L117–118) |
| model_training | Off-the-Shelf | Existing agent and model are unchanged. ([source](https://arxiv.org/html/2611.33926v1), Section 2 L122) |
| planning | Unclear |  |
| workflow | Unclear |  |
| update_strategy | Local Patch | Agent adjusts engine commands after results. ([source](https://arxiv.org/html/2611.33926v1), Section 2 L122; Table 2) |
| verifier | Human, Environment | Engine rejects commands; modeler accepts results. ([source](https://arxiv.org/html/2611.33926v1), Section 2.1 L157; Table 2) |
| feedback_assessment | Unclear |  |
| feedback_observation | Runtime, Structural Scene State | Engine replies and console history expose state. ([source](https://arxiv.org/html/2611.33926v1), Section 2 L123; Section 2.1 L157) |
| memory_time | Short-Term Memory | Shared engine state and task history persist. ([source](https://arxiv.org/html/2611.33926v1), Section 2; Table 3) |
| memory_reach | Unclear |  |
| action_type | Tool/Function Call, Code/Script | MCP executes snippets and background scripts. ([source](https://arxiv.org/html/2611.33926v1), Section 2.1, Table 3) |
| graphics_software | Agent-Adapted | Bridge adapts existing PFC/YADE engines. ([source](https://arxiv.org/html/2611.33926v1), Section 2 L121–122) |
| tools | Execution Utilities, Graphics Operations | Tools run scripts and modify simulations. ([source](https://arxiv.org/html/2611.33926v1), Section 2.1) |
| resources | Documentation & Rules | Query and browse retrieve engine documentation. ([source](https://arxiv.org/html/2611.33926v1), Section 2.2) |
| representation | Code, Geometry, Dynamic State | Scripts operate particles and evolving engine state. ([source](https://arxiv.org/html/2611.33926v1), Section 2, agentic loop) |

next_action: "Review full method and survey suitability before corpus inclusion."

Events: [{"type": "first_submission", "value": "2026-11-25T07:46:35+00:00", "precision": "timestamp", "timezone": "UTC", "raw_source_value": "Wed, 25 Nov 2026 07:46:35 UTC", "raw_source_timezone": "UTC", "local_value": "2026-11-25T01:46:35-06:00", "primary_url": "https://arxiv.org/abs/2611.33926", "authority": "primary", "version": "v1", "evidence": "arXiv submission history reports v1 at the preserved UTC timestamp.", "locator": "Submission history, v1", "raw_evidence_archive": "retrieval/07.json", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: ["Documentation lookup is a resource operation, not an autonomous correctness verifier. Tool schema checks do not prove physical validity."]

### [Real2SimLab: A Unified Platform for Real-to-Simulation Transfer](https://arxiv.org/abs/2611.34849)
core | High | new_relative_to_snapshot
Application: Datasets and Benchmarks, Dynamic / Physical simulation and effects; operations: Reconstruction, Auditing
An evaluation platform standardizes agent-built simulations, frozen reruns and benchmark scoring.
Scope: An evaluation platform standardizes agent-built simulations, frozen reruns and benchmark scoring.
Limits: Classifications describe the evaluation platform, not every hosted agent. Hidden-data scoring is offline, not an in-loop verifier.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Simulation | Benchmarks real-to-simulation programs. ([source](https://arxiv.org/html/2611.34849v1), Section 3, architecture) |
| input_form | Unclear |  |
| output | Program | Adapters collect executable deliverables. ([source](https://arxiv.org/html/2611.34849v1), Section 3, Figure 4) |
| model_type | Unclear |  |
| model_training | Unclear |  |
| planning | Unclear |  |
| workflow | Sequential | Build, freeze, rerun, then score. ([source](https://arxiv.org/html/2611.34849v1), Section 3, Figure 4) |
| update_strategy | Unclear |  |
| verifier | Unclear |  |
| feedback_assessment | Unclear |  |
| feedback_observation | Unclear |  |
| memory_time | Unclear |  |
| memory_reach | Unclear |  |
| action_type | Code/Script | Methods write programs in sandboxes. ([source](https://arxiv.org/html/2611.34849v1), Section 3, Figure 4) |
| graphics_software | Unclear |  |
| tools | Execution Utilities | Sandboxes and rerunners execute deliverables. ([source](https://arxiv.org/html/2611.34849v1), Section 3, L153–155) |
| resources | Documentation & Rules | Agent skills encode extension procedures. ([source](https://arxiv.org/html/2611.34849v1), Section 3, extending Real2SimLab L183) |
| representation | Code, Pixels | Programs are checked against rendered outputs. ([source](https://arxiv.org/html/2611.34849v1), Section 3, L153–155) |

artifact_links: [{"url": "https://real2simhub.github.io/real2simlab/", "role": "official project; reached", "raw_evidence_archive": "retrieval/08.json"}]

next_action: "Review full method and survey suitability before corpus inclusion."

Events: [{"type": "first_submission", "value": "2026-11-25T18:23:41+00:00", "precision": "timestamp", "timezone": "UTC", "raw_source_value": "Wed, 25 Nov 2026 18:23:41 UTC", "raw_source_timezone": "UTC", "local_value": "2026-11-25T12:23:41-06:00", "primary_url": "https://arxiv.org/abs/2611.34849", "authority": "primary", "version": "v1", "evidence": "arXiv submission history reports v1 at the preserved UTC timestamp.", "locator": "Submission history, v1", "raw_evidence_archive": "retrieval/08.json", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: ["Offline scorer and reproducibility checks do not establish an inference-time verifier, feedback score or agent update policy."]

### [FineDex: Bridging Fine-Grained Human-Object Interaction Generation to Dexterous Humanoid Manipulation](https://arxiv.org/abs/2611.34884)
scope_dependent | Medium | new_relative_to_snapshot
Application: Dynamic / Animation and temporal scene, Cross-category; operations: Generation
Fine-grained motion generation supplies priors for an agent practicing contact strategies in a digital twin; agentic contribution chiefly targets downstream manipulation.
Scope: Fine-grained motion generation supplies priors for an agent practicing contact strategies in a digital twin; agentic contribution chiefly targets downstream manipulation.
Limits: Abstract-only screening. Full method is needed to decide whether any agent authors graphics or only controls the robot.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Animation, Simulation | Generates coordinated motions and practices in a digital twin. ([source](https://arxiv.org/abs/2611.34884), Abstract) |
| input_form | Language | Instructions specify hands, fingers and contacts. ([source](https://arxiv.org/abs/2611.34884), Abstract) |
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
| representation | Dynamic State | Coordinated body, hand and object motion. ([source](https://arxiv.org/abs/2611.34884), Abstract) |

next_action: "Read full method to resolve graphics-authoring versus downstream robot-control scope."

Events: [{"type": "first_submission", "value": "2026-11-25T18:40:47+00:00", "precision": "timestamp", "timezone": "UTC", "raw_source_value": "Wed, 25 Nov 2026 18:40:47 UTC", "raw_source_timezone": "UTC", "local_value": "2026-11-25T12:40:47-06:00", "primary_url": "https://arxiv.org/abs/2611.34884", "authority": "primary", "version": "v1", "evidence": "arXiv submission history reports v1 at the preserved UTC timestamp.", "locator": "Submission history, v1", "raw_evidence_archive": "retrieval/09.json", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: ["Motion synthesis and downstream robot-policy search are distinct; the abstract does not establish an agentic graphics-authoring loop."]

## date_unresolved (0)

## unresolved (10)

### [NeoWorld-Pro: Programming Interactive Scenes from Monocular Images for Embodied Simulation](https://arxiv.org/abs/2608.24212)
unresolved | Low | new_relative_to_snapshot
Application: Cross-category; operations: Unclear
Primary recheck pending.
Scope: Carried from the latest pending queue; historical classifications and dates are not fresh evidence.
Limits: All mechanism fields remain Unclear until a fresh primary check. A prior reported identity may still have unresolved verification work.

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

next_action: "Reopen primary history and method before updating this verification record."

Events: []
Taxonomy deltas: []

### [PhotoGuider: Composition-Aware Cropping and 360° View Framing with Explainable Photographic Assessments](https://arxiv.org/abs/2611.02897)
unresolved | Low | new_relative_to_snapshot
Application: Cross-category; operations: Unclear
Primary recheck pending.
Scope: Carried from the latest pending queue; historical classifications and dates are not fresh evidence.
Limits: All mechanism fields remain Unclear until a fresh primary check. A prior reported identity may still have unresolved verification work.

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

next_action: "Reopen primary history and method before updating this verification record."

Events: []
Taxonomy deltas: []

### [SceneAgent: An Agentic Pipeline from 3D and 4D Captures to Simulation Environments](https://arxiv.org/abs/2610.34745)
unresolved | Low | new_relative_to_snapshot
Application: Cross-category; operations: Unclear
Primary recheck pending.
Scope: Carried from the latest pending queue; historical classifications and dates are not fresh evidence.
Limits: All mechanism fields remain Unclear until a fresh primary check. A prior reported identity may still have unresolved verification work.

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

next_action: "Reopen primary history and method before updating this verification record."

Events: []
Taxonomy deltas: []

### [Agentic AI for Scientific Visualization: Tool-Calling Pipelines for Automated Chart and Diagram Generation in Research Writing](https://www.scitepress.org/PublishedPapers/2026/152298/)
unresolved | Low | new_relative_to_snapshot
Application: Cross-category; operations: Unclear
Primary recheck pending.
Scope: Carried from the latest pending queue; historical classifications and dates are not fresh evidence.
Limits: All mechanism fields remain Unclear until a fresh primary check. A prior reported identity may still have unresolved verification work.

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

next_action: "Reopen primary history and method before updating this verification record."

Events: []
Taxonomy deltas: []

### [FLASH: A "Generate Once, Synthesize Many" Framework for Synthetic Anomaly Generation in Industrial Anomaly Detection](https://arxiv.org/abs/2609.37314)
unresolved | Low | new_relative_to_snapshot
Application: Cross-category; operations: Unclear
Primary recheck pending.
Scope: Carried from the latest pending queue; historical classifications and dates are not fresh evidence.
Limits: All mechanism fields remain Unclear until a fresh primary check. A prior reported identity may still have unresolved verification work.

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

next_action: "Reopen primary history and method before updating this verification record."

Events: []
Taxonomy deltas: []

### [Agent-Guided Immersive World Generation with Alpha-Textured Proxies](https://immersegen.github.io/)
unresolved | Low | new_relative_to_snapshot
Application: Cross-category; operations: Unclear
Primary recheck pending.
Scope: Carried from the latest pending queue; historical classifications and dates are not fresh evidence.
Limits: All mechanism fields remain Unclear until a fresh primary check. A prior reported identity may still have unresolved verification work.

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

next_action: "Reopen primary history and method before updating this verification record."

Events: []
Taxonomy deltas: []

### [HiLSVA: Design and Evaluation of a Human-in-the-Loop Agentic System for Scientific Visualization](https://arxiv.org/abs/2606.26614)
unresolved | Low | new_relative_to_snapshot
Application: Cross-category; operations: Unclear
Primary recheck pending.
Scope: Carried from the latest pending queue; historical classifications and dates are not fresh evidence.
Limits: All mechanism fields remain Unclear until a fresh primary check. A prior reported identity may still have unresolved verification work.

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

next_action: "Reopen primary history and method before updating this verification record."

Events: []
Taxonomy deltas: []

### [Exploring LLM Agent Designs and Interaction Modalities for Scientific Visualization](https://arxiv.org/abs/2604.27996)
unresolved | Low | new_relative_to_snapshot
Application: Cross-category; operations: Unclear
Primary recheck pending.
Scope: Carried from the latest pending queue; historical classifications and dates are not fresh evidence.
Limits: All mechanism fields remain Unclear until a fresh primary check. A prior reported identity may still have unresolved verification work.

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

next_action: "Reopen primary history and method before updating this verification record."

Events: []
Taxonomy deltas: []

### [DramaAgent: Agentic Storytelling Video Generation](https://aclanthology.org/2026.aacl-long.163/)
unresolved | Low | new_relative_to_snapshot
Application: Cross-category; operations: Unclear
Primary recheck pending.
Scope: Carried from the latest pending queue; historical classifications and dates are not fresh evidence.
Limits: All mechanism fields remain Unclear until a fresh primary check. A prior reported identity may still have unresolved verification work.

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

next_action: "Reopen primary history and method before updating this verification record."

Events: []
Taxonomy deltas: []

### [ShaderAgent: Self-Evolving Agentic Procedural Material Generation](https://github.com/VAST-AI-Research/ShaderAgent)
unresolved | Low | new_relative_to_snapshot
Application: Cross-category; operations: Unclear
Primary recheck pending.
Scope: Carried from the latest pending queue; historical classifications and dates are not fresh evidence.
Limits: All mechanism fields remain Unclear until a fresh primary check. A prior reported identity may still have unresolved verification work.

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

next_action: "Reopen primary history and method before updating this verification record."

Events: []
Taxonomy deltas: []

## excluded (0)

## Application index
| Application | Papers |
|---|---|
| 2D Graphics | [Nemotron-Labs-VisualCreation: Pixel as Code for Agentic Visual Creation](https://arxiv.org/abs/2611.31358) [late_discovery] |
| Static / Object | [SemProxy: Semantic 3D Proxies for Controllable Agentic 3D Modeling](https://arxiv.org/abs/2611.34414) [late_discovery] |
| Static / CAD | None verified in this run |
| Static / Scene | [SemProxy: Semantic 3D Proxies for Controllable Agentic 3D Modeling](https://arxiv.org/abs/2611.34414) [late_discovery] |
| Dynamic / Articulated assets | None verified in this run |
| Dynamic / Animation and temporal scene | [Agentic LongLive: Asynchronous Agentic Memory for Long Video Generation](https://arxiv.org/abs/2611.34907) [late_discovery]; [FineDex: Bridging Fine-Grained Human-Object Interaction Generation to Dexterous Humanoid Manipulation](https://arxiv.org/abs/2611.34884) [late_discovery] |
| Dynamic / Physical simulation and effects | [Connecting AI Agents to Live Discrete Element Simulations via the Model Context Protocol](https://arxiv.org/abs/2611.33926) [late_discovery]; [Real2SimLab: A Unified Platform for Real-to-Simulation Transfer](https://arxiv.org/abs/2611.34849) [late_discovery] |
| Datasets and Benchmarks | [Real2SimLab: A Unified Platform for Real-to-Simulation Transfer](https://arxiv.org/abs/2611.34849) [late_discovery] |
| Cross-category | [Connecting AI Agents to Live Discrete Element Simulations via the Model Context Protocol](https://arxiv.org/abs/2611.33926) [late_discovery]; [FineDex: Bridging Fine-Grained Human-Object Interaction Generation to Dexterous Humanoid Manipulation](https://arxiv.org/abs/2611.34884) [late_discovery]; [NeoWorld-Pro: Programming Interactive Scenes from Monocular Images for Embodied Simulation](https://arxiv.org/abs/2608.24212) [unresolved]; [PhotoGuider: Composition-Aware Cropping and 360° View Framing with Explainable Photographic Assessments](https://arxiv.org/abs/2611.02897) [unresolved]; [SceneAgent: An Agentic Pipeline from 3D and 4D Captures to Simulation Environments](https://arxiv.org/abs/2610.34745) [unresolved]; [Agentic AI for Scientific Visualization: Tool-Calling Pipelines for Automated Chart and Diagram Generation in Research Writing](https://www.scitepress.org/PublishedPapers/2026/152298/) [unresolved]; [FLASH: A "Generate Once, Synthesize Many" Framework for Synthetic Anomaly Generation in Industrial Anomaly Detection](https://arxiv.org/abs/2609.37314) [unresolved]; [Agent-Guided Immersive World Generation with Alpha-Textured Proxies](https://immersegen.github.io/) [unresolved]; [HiLSVA: Design and Evaluation of a Human-in-the-Loop Agentic System for Scientific Visualization](https://arxiv.org/abs/2606.26614) [unresolved]; [Exploring LLM Agent Designs and Interaction Modalities for Scientific Visualization](https://arxiv.org/abs/2604.27996) [unresolved]; [DramaAgent: Agentic Storytelling Video Generation](https://aclanthology.org/2026.aacl-long.163/) [unresolved]; [ShaderAgent: Self-Evolving Agentic Procedural Material Generation](https://github.com/VAST-AI-Research/ShaderAgent) [unresolved] |

## Source ledger

| Source | Status | Limits |
|---|---|---|
| arxiv | partial | Seven category pages, six canonical pages and five method pages reached. Only selected excerpts read; CV recent first 50 entries; new category headings remain Nov 26. |
| hugging_face | partial | Nov 27 dated URL blocked. Root reached with Nov 27 heading; search fallback returned Nov 26 and other pages. Curation dates are not event evidence. |
| openreview | partial | Direct search blocked; restricted queries returned older sources, without a verified target-day paper. |
| official_venues | partial | SIGGRAPH Asia overview reached; ACM/CVF queries executed; no proceedings-wide or same-day paper verification. |
| project_author_lab | partial | LongLive and Real2SimLab official projects reached; other project/repository search signals remain unscreened. |

## Exact retrieval ledger

Times below are actual post-return recording times; exact per-page retrieval times are not exposed. Full requests, returned evidence and call-start times are in the linked journals.

| Journal | Recorded at (UTC) | Operation | Executed query / URL / find |
|---|---|---|---|
| [01](retrieval/01.json) | 2026-11-27T19:59:16+00:00 | search_query | agentic graphics 3D scene CAD November 27 2026 |
| [01](retrieval/01.json) | 2026-11-27T19:59:16+00:00 | search_query | "agent" "SVG" "November" "2026" |
| [01](retrieval/01.json) | 2026-11-27T19:59:16+00:00 | search_query | "Nemotron-Labs-VisualCreation" |
| [01](retrieval/01.json) | 2026-11-27T19:59:16+00:00 | open | https://arxiv.org/list/cs.GR/new |
| [01](retrieval/01.json) | 2026-11-27T19:59:16+00:00 | open | https://arxiv.org/list/cs.CV/recent |
| [01](retrieval/01.json) | 2026-11-27T19:59:16+00:00 | open | https://huggingface.co/papers/date/2026-11-27 |
| [02](retrieval/02.json) | 2026-11-27T19:59:24+00:00 | search_query | agentic 3D object modeling procedural materials mesh November 2026 paper |
| [02](retrieval/02.json) | 2026-11-27T19:59:24+00:00 | search_query | agent CAD design November 2026 arxiv |
| [02](retrieval/02.json) | 2026-11-27T19:59:24+00:00 | search_query | "Agentic LongLive" |
| [02](retrieval/02.json) | 2026-11-27T19:59:24+00:00 | open | https://arxiv.org/list/cs.RO/new |
| [02](retrieval/02.json) | 2026-11-27T19:59:24+00:00 | open | https://huggingface.co/papers |
| [02](retrieval/02.json) | 2026-11-27T19:59:24+00:00 | open | https://openreview.net/search?term=graphics%20agent |
| [02](retrieval/02.json) | 2026-11-27T19:59:24+00:00 | find | https://arxiv.org/list/cs.GR/new [find: Title:] |
| [02](retrieval/02.json) | 2026-11-27T19:59:24+00:00 | find | https://arxiv.org/list/cs.CV/recent [find: Agent] |
| [03](retrieval/03.json) | 2026-11-27T19:59:31+00:00 | search_query | agent articulated asset joint rig generation November 2026 |
| [03](retrieval/03.json) | 2026-11-27T19:59:31+00:00 | search_query | agent physical simulation particle effects November 27 2026 |
| [03](retrieval/03.json) | 2026-11-27T19:59:31+00:00 | search_query | site:openreview.net graphics agent 2026 |
| [03](retrieval/03.json) | 2026-11-27T19:59:31+00:00 | open | https://arxiv.org/list/cs.AI/new |
| [03](retrieval/03.json) | 2026-11-27T19:59:31+00:00 | open | https://asia.siggraph.org/2026/program/technical-papers/ |
| [03](retrieval/03.json) | 2026-11-27T19:59:31+00:00 | open | https://arxiv.org/abs/2611.31358 |
| [03](retrieval/03.json) | 2026-11-27T19:59:31+00:00 | find | https://huggingface.co/papers [find: Nov] |
| [03](retrieval/03.json) | 2026-11-27T19:59:31+00:00 | find | https://huggingface.co/papers [find: Real2Sim] |
| [03](retrieval/03.json) | 2026-11-27T19:59:31+00:00 | find | https://arxiv.org/list/cs.RO/new [find: Agent] |
| [04](retrieval/04.json) | 2026-11-27T19:59:38+00:00 | search_query | agent graphics benchmark world auditing verification November 2026 |
| [04](retrieval/04.json) | 2026-11-27T19:59:38+00:00 | search_query | graphics agent memory replanning tool interface feedback program synthesis |
| [04](retrieval/04.json) | 2026-11-27T19:59:38+00:00 | search_query | site:dl.acm.org agent graphics "2026" "November" |
| [04](retrieval/04.json) | 2026-11-27T19:59:38+00:00 | open | https://arxiv.org/list/cs.HC/new |
| [04](retrieval/04.json) | 2026-11-27T19:59:38+00:00 | open | https://arxiv.org/list/cs.MM/new |
| [04](retrieval/04.json) | 2026-11-27T19:59:38+00:00 | open | https://arxiv.org/list/eess.IV/new |
| [04](retrieval/04.json) | 2026-11-27T19:59:38+00:00 | find | https://arxiv.org/abs/2611.31358 [find: Submission history] |
| [04](retrieval/04.json) | 2026-11-27T19:59:38+00:00 | find | https://huggingface.co/papers [find: ###] |
| [04](retrieval/04.json) | 2026-11-27T19:59:38+00:00 | find | https://arxiv.org/list/cs.AI/new [find: simulation] |
| [05](retrieval/05.json) | 2026-11-27T19:59:49+00:00 | search_query | agent 3D scene layout generation November 27 2026 arxiv |
| [05](retrieval/05.json) | 2026-11-27T19:59:49+00:00 | search_query | "Real2SimLab"  |
| [05](retrieval/05.json) | 2026-11-27T19:59:49+00:00 | search_query | site:openreview.net "agent" "graphics" "2026-11" |
| [05](retrieval/05.json) | 2026-11-27T19:59:49+00:00 | open | https://arxiv.org/html/2611.31358v1 |
| [05](retrieval/05.json) | 2026-11-27T19:59:49+00:00 | open | https://arxiv.org/abs/2611.34907 |
| [05](retrieval/05.json) | 2026-11-27T19:59:49+00:00 | open | https://arxiv.org/abs/2611.34414 |
| [05](retrieval/05.json) | 2026-11-27T19:59:49+00:00 | find | https://arxiv.org/list/cs.HC/new [find: Title:] |
| [05](retrieval/05.json) | 2026-11-27T19:59:49+00:00 | find | https://arxiv.org/list/cs.MM/new [find: agent] |
| [05](retrieval/05.json) | 2026-11-27T19:59:49+00:00 | find | https://arxiv.org/list/eess.IV/new [find: agent] |
| [05](retrieval/05.json) | 2026-11-27T19:59:49+00:00 | find | https://huggingface.co/papers [find: Creation] |
| [06](retrieval/06.json) | 2026-11-27T20:00:04+00:00 | search_query | site:arxiv.org agent SVG chart poster slide "27 Nov 2026" |
| [06](retrieval/06.json) | 2026-11-27T20:00:04+00:00 | search_query | site:openaccess.thecvf.com "agent" "graphics" "2026" |
| [06](retrieval/06.json) | 2026-11-27T20:00:04+00:00 | search_query | "Articraft" "2026" "November" |
| [06](retrieval/06.json) | 2026-11-27T20:00:04+00:00 | open | https://arxiv.org/html/2611.34907v1 |
| [06](retrieval/06.json) | 2026-11-27T20:00:04+00:00 | open | https://arxiv.org/html/2611.34414v1 |
| [06](retrieval/06.json) | 2026-11-27T20:00:04+00:00 | open | https://arxiv.org/abs/2611.33926 |
| [06](retrieval/06.json) | 2026-11-27T20:00:04+00:00 | find | https://arxiv.org/abs/2611.34907 [find: Submission history] |
| [06](retrieval/06.json) | 2026-11-27T20:00:04+00:00 | find | https://arxiv.org/abs/2611.34414 [find: Submission history] |
| [06](retrieval/06.json) | 2026-11-27T20:00:04+00:00 | find | https://arxiv.org/html/2611.31358v1 [find: Critic] |
| [06](retrieval/06.json) | 2026-11-27T20:00:04+00:00 | find | https://arxiv.org/html/2611.31358v1 [find: repair] |
| [06](retrieval/06.json) | 2026-11-27T20:00:04+00:00 | find | https://arxiv.org/html/2611.31358v1 [find: memory] |
| [07](retrieval/07.json) | 2026-11-27T20:00:12+00:00 | search_query | site:huggingface.co/papers/date/2026-11-27 |
| [07](retrieval/07.json) | 2026-11-27T20:00:12+00:00 | search_query | agent animation cinematography temporal scene recent paper |
| [07](retrieval/07.json) | 2026-11-27T20:00:12+00:00 | search_query | site:arxiv.org "graphics" "27 Nov 2026" |
| [07](retrieval/07.json) | 2026-11-27T20:00:12+00:00 | open | https://arxiv.org/abs/2611.34849 |
| [07](retrieval/07.json) | 2026-11-27T20:00:12+00:00 | open | https://arxiv.org/html/2611.33926v1 |
| [07](retrieval/07.json) | 2026-11-27T20:00:12+00:00 | open | https://nvlabs.github.io/LongLive/Agentic-LongLive/ |
| [07](retrieval/07.json) | 2026-11-27T20:00:12+00:00 | find | https://arxiv.org/abs/2611.33926 [find: Submission history] |
| [07](retrieval/07.json) | 2026-11-27T20:00:12+00:00 | find | https://arxiv.org/html/2611.34907v1 [find: asynchronous] |
| [07](retrieval/07.json) | 2026-11-27T20:00:12+00:00 | find | https://arxiv.org/html/2611.34907v1 [find: memory bank] |
| [07](retrieval/07.json) | 2026-11-27T20:00:12+00:00 | find | https://arxiv.org/html/2611.34414v1 [find: feedback] |
| [07](retrieval/07.json) | 2026-11-27T20:00:12+00:00 | find | https://arxiv.org/html/2611.34414v1 [find: ProxyStudio] |
| [08](retrieval/08.json) | 2026-11-27T20:00:19+00:00 | search_query | "VibeVideoAgent" |
| [08](retrieval/08.json) | 2026-11-27T20:00:19+00:00 | search_query | site:arxiv.org agent CAD "26 Nov 2026" |
| [08](retrieval/08.json) | 2026-11-27T20:00:19+00:00 | search_query | site:openreview.net "SemProxy" |
| [08](retrieval/08.json) | 2026-11-27T20:00:19+00:00 | open | https://arxiv.org/html/2611.34849v1 |
| [08](retrieval/08.json) | 2026-11-27T20:00:19+00:00 | open | https://arxiv.org/abs/2611.34884 |
| [08](retrieval/08.json) | 2026-11-27T20:00:19+00:00 | open | https://real2simhub.github.io/real2simlab/ |
| [08](retrieval/08.json) | 2026-11-27T20:00:19+00:00 | find | https://arxiv.org/abs/2611.34849 [find: Submission history] |
| [08](retrieval/08.json) | 2026-11-27T20:00:19+00:00 | find | https://arxiv.org/html/2611.34907v1 [find: planner] |
| [08](retrieval/08.json) | 2026-11-27T20:00:19+00:00 | find | https://arxiv.org/html/2611.34414v1 [find: 3.3] |
| [08](retrieval/08.json) | 2026-11-27T20:00:19+00:00 | find | https://arxiv.org/html/2611.33926v1 [find: tools] |
| [08](retrieval/08.json) | 2026-11-27T20:00:19+00:00 | find | https://arxiv.org/html/2611.33926v1 [find: feedback] |
| [09](retrieval/09.json) | 2026-11-27T20:00:28+00:00 | search_query | agent 3D object procedural modeling Blender material |
| [09](retrieval/09.json) | 2026-11-27T20:00:28+00:00 | search_query | agent articulated asset joint mechanism rig generation "27" "November 2026" |
| [09](retrieval/09.json) | 2026-11-27T20:00:28+00:00 | search_query | agent physical simulation effects "November 2026" arxiv |
| [09](retrieval/09.json) | 2026-11-27T20:00:28+00:00 | find | https://arxiv.org/abs/2611.34884 [find: Abstract:] |
| [09](retrieval/09.json) | 2026-11-27T20:00:28+00:00 | find | https://arxiv.org/abs/2611.34884 [find: Submission history] |
| [09](retrieval/09.json) | 2026-11-27T20:00:28+00:00 | find | https://arxiv.org/html/2611.34849v1 [find: offline] |
| [09](retrieval/09.json) | 2026-11-27T20:00:28+00:00 | find | https://arxiv.org/html/2611.34849v1 [find: agent] |
| [09](retrieval/09.json) | 2026-11-27T20:00:28+00:00 | find | https://arxiv.org/html/2611.34907v1 [find: Refinement.] |
| [09](retrieval/09.json) | 2026-11-27T20:00:28+00:00 | find | https://arxiv.org/html/2611.34907v1 [find: 2.2 Asynchronous agentic memory] |
| [09](retrieval/09.json) | 2026-11-27T20:00:28+00:00 | find | https://arxiv.org/html/2611.31358v1 [find: 3 Framework] |
| [09](retrieval/09.json) | 2026-11-27T20:00:28+00:00 | find | https://arxiv.org/html/2611.33926v1 [find: case study] |
| [09](retrieval/09.json) | 2026-11-27T20:00:28+00:00 | find | https://real2simhub.github.io/real2simlab/ [find: offline] |
| [10](retrieval/10.json) | 2026-11-27T20:00:38+00:00 | search_query | agent scientific illustration Manim animation code recent research |
| [10](retrieval/10.json) | 2026-11-27T20:00:38+00:00 | search_query | agent graphics benchmark "November 27" "2026" |
| [10](retrieval/10.json) | 2026-11-27T20:00:38+00:00 | search_query | "SemProxy" "Agentic LongLive" |
| [10](retrieval/10.json) | 2026-11-27T20:00:38+00:00 | find | https://arxiv.org/abs/2611.34884 [find: We] |
| [10](retrieval/10.json) | 2026-11-27T20:00:38+00:00 | find | https://arxiv.org/html/2611.34907v1 [find: We run] |
| [10](retrieval/10.json) | 2026-11-27T20:00:38+00:00 | find | https://arxiv.org/html/2611.34907v1 [find: checks] |
| [10](retrieval/10.json) | 2026-11-27T20:00:38+00:00 | find | https://arxiv.org/html/2611.34907v1 [find: versioned] |
| [10](retrieval/10.json) | 2026-11-27T20:00:38+00:00 | find | https://arxiv.org/html/2611.34849v1 [find: Real2SimLab] |
| [10](retrieval/10.json) | 2026-11-27T20:00:38+00:00 | find | https://arxiv.org/html/2611.31358v1 [find: harness] |
| [10](retrieval/10.json) | 2026-11-27T20:00:38+00:00 | find | https://arxiv.org/html/2611.33926v1 [find: Abstract] |
| [10](retrieval/10.json) | 2026-11-27T20:00:38+00:00 | find | https://arxiv.org/abs/2611.31358 [find: Authors:] |
| [10](retrieval/10.json) | 2026-11-27T20:00:38+00:00 | find | https://arxiv.org/abs/2611.34907 [find: Authors:] |
| [10](retrieval/10.json) | 2026-11-27T20:00:38+00:00 | find | https://arxiv.org/abs/2611.34414 [find: Authors:] |
| [10](retrieval/10.json) | 2026-11-27T20:00:38+00:00 | find | https://arxiv.org/abs/2611.33926 [find: Authors:] |
| [10](retrieval/10.json) | 2026-11-27T20:00:38+00:00 | find | https://arxiv.org/abs/2611.34849 [find: Authors:] |
| [10](retrieval/10.json) | 2026-11-27T20:00:38+00:00 | find | https://arxiv.org/abs/2611.34884 [find: Authors:] |
| [11](retrieval/11.json) | 2026-11-27T20:00:49+00:00 | find | https://arxiv.org/abs/2611.34884 [find: FineDex is] |
| [11](retrieval/11.json) | 2026-11-27T20:00:49+00:00 | find | https://arxiv.org/abs/2611.34884 [find: Abstract] |
| [11](retrieval/11.json) | 2026-11-27T20:00:49+00:00 | find | https://arxiv.org/html/2611.34907v1 [find: entity] |
| [11](retrieval/11.json) | 2026-11-27T20:00:49+00:00 | find | https://arxiv.org/html/2611.34849v1 [find: freeze] |
| [11](retrieval/11.json) | 2026-11-27T20:00:49+00:00 | find | https://arxiv.org/html/2611.34849v1 [find: sandbox] |
| [11](retrieval/11.json) | 2026-11-27T20:00:49+00:00 | find | https://arxiv.org/html/2611.33926v1 [find: modeler] |
| [11](retrieval/11.json) | 2026-11-27T20:00:49+00:00 | find | https://arxiv.org/html/2611.31358v1 [find: planning] |
| [11](retrieval/11.json) | 2026-11-27T20:00:49+00:00 | find | https://arxiv.org/html/2611.34907v1 [find: image model] |

## Query-family coverage

- 2d: partial; journals 01, 05, 06, 10.
- object: partial; journals 02, 09.
- cad: partial; journals 01, 02, 08.
- scene: partial; journals 01, 05, 07.
- articulation: partial; journals 03, 06, 09.
- animation: partial; journals 02, 07, 08, 10, 11.
- simulation: partial; journals 03, 04, 08, 09, 11.
- benchmark: partial; journals 04, 08, 10, 11.
- harness: partial; journals 03, 04, 05, 06, 07, 10, 11.

## Previously reported identity signals

These resurfaced in current searches; prior dates are historical context, not fresh checks.

- 2608.26238: Procedura: Agentic 3D Modeling with Procedural Control
- 2610.39924: PhysAg3D: Bridging 3D Generative and Agentic Models for High-Fidelity and Physically-Interactive Assets
- 2610.21755: DeciCAD: Harness-Grounded Learning of Action Policies for CAD Agents
- 2610.23121: Scene-Designer: Learning Design Intelligence for Agentic 3D Scene Generation
- 2602.10116: SAGE: Scalable Agentic 3D Scene Generation for Embodied AI
- 2606.29395: NaLA: A 3D Native LLM Layout Agent for High-quality 3D Scene Generation
- 2611.25340: SceneAnything: Agentic Reconstruction of Large-Scale Mesh Scenes from a Single Video
- 2501.12909: FilmAgent: A Multi-Agent Framework for End-to-End Film Automation in Virtual 3D Spaces
- 2610.30753: FilmFlow: Agentic System for 3D Virtual Film Cinematography
- 2604.25318: Cutscene Agent: An LLM Agent Framework for Automated 3D Cutscene Generation
- 2607.01766: SimWorlds: A Multi-Agent System for Dynamic 3D Scene Creation
- 2508.08228: LL3M: Large Language 3D Modelers
- 2611.08294: ManimCode: Learning Visual Self-Correction for Educational Animation
- 2604.18364: Training and Agentic Inference Strategies for LLM-based Manim Animation Generation
- 2605.15585: See Before You Code: Learning Visual Priors for Spatially Aware Educational Animation Generation
- 2606.30296: ManimAgent: Self-Evolving Multimodal Agents for Visual Education

## Preserved exclusions

- TaoMate-R1: Temporal Role Specialization for Streaming Multi-Reference Video Generation — historical exclusion; daily/2026-11-10/run.json
- 3A-VLA: Abstraction-Aligned Action Learning for Vision-Language Agents in 3D Game Worlds — historical exclusion; daily/2026-11-10/run.json
- Pose Distance Fields for Humanoid Robots — historical exclusion; daily/2026-11-10/run.json
- DORIS: Polarization Aware Multimodal Degradation Perception for Underwater Image Restoration — historical exclusion; daily/2026-11-10/run.json
- 3D-Agent Blender AI Plugin — historical exclusion; daily/2026-11-16/run.json
- SKILL.PNG: Learning Agent Skills in Pixel Space — historical exclusion; daily/2026-11-20/run.json
- Same Pixels, Different Documents: Measuring Part-Level Editability in Image Vectorization — historical exclusion; daily/2026-11-23/run.json
- Learning the Next Best Move with Visual Diffusion Models — historical exclusion; daily/2026-11-24/run.json
- Rethinking Video Agents: When and Why Video Harnesses Work — historical exclusion; daily/2026-11-25/run.json
- Residual Guidance for Real-Time Interactive Video Generation — historical exclusion; daily/2026-11-26/run.json

## Pending queue

- NeoWorld-Pro: Programming Interactive Scenes from Monocular Images for Embodied Simulation: Historical classifications and timestamps are unverified leads, not fresh primary evidence. All 18 cells remain Unclear.
- PhotoGuider: Composition-Aware Cropping and 360° View Framing with Explainable Photographic Assessments: Historical classifications and timestamps are unverified leads, not fresh primary evidence. All 18 cells remain Unclear.
- SceneAgent: An Agentic Pipeline from 3D and 4D Captures to Simulation Environments: Historical classifications and timestamps are unverified leads, not fresh primary evidence. All 18 cells remain Unclear.
- Agentic AI for Scientific Visualization: Tool-Calling Pipelines for Automated Chart and Diagram Generation in Research Writing: Historical classifications and timestamps are unverified leads, not fresh primary evidence. All 18 cells remain Unclear.
- FLASH: A "Generate Once, Synthesize Many" Framework for Synthetic Anomaly Generation in Industrial Anomaly Detection: Historical classifications and timestamps are unverified leads, not fresh primary evidence. All 18 cells remain Unclear.
- Agent-Guided Immersive World Generation with Alpha-Textured Proxies: Historical classifications and timestamps are unverified leads, not fresh primary evidence. All 18 cells remain Unclear.
- HiLSVA: Design and Evaluation of a Human-in-the-Loop Agentic System for Scientific Visualization: Historical classifications and timestamps are unverified leads, not fresh primary evidence. All 18 cells remain Unclear.
- Exploring LLM Agent Designs and Interaction Modalities for Scientific Visualization: Historical classifications and timestamps are unverified leads, not fresh primary evidence. All 18 cells remain Unclear.
- DramaAgent: Agentic Storytelling Video Generation: Historical classifications and timestamps are unverified leads, not fresh primary evidence. All 18 cells remain Unclear.
- EvoDesign first-submission date anomaly: The primary page reports February 20 first submission under an identifier beginning 2604. Revised method was read, but the first date remains unresolved.
- TRIP event-driven robot harness: Listing passage describes agent-written interrupt programs; candidate paper identity/scope/date not opened within cap.
- QuantiPhy reconstruction-based physical reasoning lead: Selected listing passage describes reconstruction-grounded physical quantities; identity/scope not fully inspected.
- RFW-A: Agentic Procedural Generation of 400K Articulated Assets over 500 Categories: Older search lead outside seven-day catch-up; no new event verified.
- AnyMachine: Secondary lead to machine modeling/rigging workflow; research identity/date unresolved.
- ShaderAgent: Self-Evolving Agentic Procedural Material Generation: Official repository supports a plausible graphics-authoring system, but no publisher date or paper text was verified; retain as unresolved signal.
- RUIBench: What Makes a Good Robot-Use Interface?: Robot interface lead; transferable graphics scope unverified.
- AutoPILOT: A Visual Agent Harness for Real-Time Gameplay: Gameplay harness lead; graphics-authoring relevance unverified.
- GameDojo: Benchmarking Real-Time Interactive Agents in Video Games: Game agent benchmark lead; scope and dates unverified.
- ReWeave: Emergent Physical Task Topologies for Embodied Harness Optimization and Cross-Task Meta-Distillation: HF listing only; primary scope and dates unverified.
- PhyCoVE: Benchmarking Physical Counterfactual Video Editing across Diverse Material Dynamics: HF listing lead; agentic scope and primary date unverified.
- Where is the Interface for the AI Harness?: HC listing lead; transferable graphics scope and canonical history not checked.
- SlidesWeaver first-submission date anomaly: Primary history reports September 8 v1 under a November identifier. Retained v2 revision separately; first event needs versioned metadata confirmation.
- Blueprint procedural house workflow: Secondary repository signal only; no verified research or artifact event.
- VibeVideoAgent: Closing the Perceptual Loop for Code-Driven Video Generation: Primary search abstract only; canonical submission history and full method not opened before cap.
- Unresolved simulation-world construction lead (2611.34457): Secondary search result associates this identifier with world construction; identity and anomalous September submission claim require primary verification.
