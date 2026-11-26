# Agentic Graphics daily report
Date: 2026-11-26 | Timezone: America/Chicago | As of: 2026-11-26T20:03:44+00:00
browser-based same-day search; documented source coverage
Taxonomy: survey-taxonomy-snapshot-2026-10-15 | Snapshot: bundled_snapshot_not_live_refreshed

## Coverage limits
- Today covers November 26, 2026 midnight through 14:03:44 America/Chicago, frozen at the actual start clock.
- No qualifying same-day Agentic Graphics paper was verified in the browsed source set. Indexing lag, inaccessible pages and selective reading limit this statement.
- One bounded pass reached 10 search batches and 24 attempted primary opens before the approximate six-minute allowance; elapsed time comes from journals, without padding.
- Nine query families and five source families were attempted; coverage is partial. Broad, dated, recent-category and known-alias queries were used.
- Seven arXiv category pages reached; cs.CV recent exposed only entries 1–50 of 1468. Selected excerpts and keyword finds are not an exhaustive category scan.
- HF November 26 dated URL was inaccessible. Root showed Nov 26 and dated-page search returned a result. Curation and announcement dates are not submission dates.
- OpenReview direct search was inaccessible; restricted searches returned older papers and noisy venue pages. SIGGRAPH Asia overview reached; ACM/CVF queries did not establish a same-day event.
- Seven fresh candidate decisions: five with selected full-text passages, one abstract-only relevant record, one abstract-level exclusion. Further leads remain pending.
- November 19–25 is the separate seven-day catch-up lane. SlidesWeaver v1 first date is anomalous and unresolved; v2 revision timestamp is preserved separately.
- Direct main reports and supplied website history are identity/event context only; archived previous-run directories are not recursively used as current evidence.
- No empirical reproduction or revision-content comparison. Unclear cells mean insufficient evidence. Training rewards and offline evaluation are not inferred to be in-loop verifiers.
- Frozen October 15 snapshot remains bundled_snapshot_not_live_refreshed. Tools labels are provisional; source memory wording is inconsistent.
- Source/query ledger batch associations record retrieval intent, not that every result belongs to every associated family.

No qualifying same-day Agentic Graphics paper was verified in the browsed source set.
Coverage is limited to the sources and queries below; unpublished or unindexed papers may be missing.

## Execution and event comparison
Window: 2026-11-26T00:00:00-06:00 through 2026-11-26T14:03:44-06:00. Same-day new: 0; updates: 0. Retrieval: 10 batches / 30 queries / 24 attempted opens in 87 seconds.
The helper groups verified older events under late_discovery; the table separates new-to-us catch-up from previously reported events.

| Paper | Discovery status | Verified Chicago events |
|---|---|---|
| SceneDesigner3D: Agentic Evolutionary Search for Principled Rearrangement of 3D Indoor Scenes | new_to_us_catch_up | v1 first_submission 2026-11-25T11:41:34-06:00 (not_seen_in_supplied_history) |
| PreferenceScene: Personalized Indoor Scene Synthesis from Feedback | new_to_us_catch_up | v1 first_submission 2026-11-24T01:19:27-06:00 (not_seen_in_supplied_history) |
| MAGPIE: Agentic Multi-Reference Image Generation via Executable Scene Construction | new_to_us_catch_up | v1 first_submission 2026-11-24T05:58:12-06:00 (not_seen_in_supplied_history) |
| AdProducer: Towards Agentic Advertising Video Generation | new_to_us_catch_up | v1 first_submission 2026-11-23T13:37:29-06:00 (not_seen_in_supplied_history) |
| Lab2Sim: Agentic Generation of Interactive Laboratory Equipment from Operation Videos | new_to_us_catch_up | v1 first_submission 2026-11-24T21:18:52-06:00 (not_seen_in_supplied_history) |
| Residual Guidance for Real-Time Interactive Video Generation | excluded | v1 first_submission 2026-11-24T09:35:58-06:00 (not_seen_in_supplied_history) |
| Beyond Code and Pixels: Co-Generating Editable and Visually Rich Presentations | new_to_us_catch_up | v2 revision 2026-11-25T08:23:43-06:00 (not_seen_in_supplied_history) |

## already_reported (0)

## same_day_new (0)

## same_day_updates (0)

## late_discovery (6)

### [SceneDesigner3D: Agentic Evolutionary Search for Principled Rearrangement of 3D Indoor Scenes](https://arxiv.org/abs/2611.34783)
core | Medium | new_relative_to_snapshot
Application: Static / Scene; operations: Editing
A VLM evolves editable scene-rearrangement programs using physical checks and design feedback.
Scope: A VLM evolves editable scene-rearrangement programs using physical checks and design feedback.
Limits: Selected method passages; training status and memory reach are unverified. No revision comparison or reproduction.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Modeling | Rearranges indoor scenes. ([source](https://arxiv.org/abs/2611.34783), Abstract) |
| input_form | Language, 3D Representation | Takes a scene and prompt. ([source](https://arxiv.org/abs/2611.34783), Abstract) |
| output | Program, Graphics Artifact | Evolves layout programs. ([source](https://arxiv.org/abs/2611.34783), Abstract) |
| model_type | VLM | VLM mutates programs. ([source](https://arxiv.org/abs/2611.34783), Abstract) |
| model_training | Unclear |  |
| planning | PO-2 | Fixed mutation choices with agent selection. ([source](https://arxiv.org/html/2611.34783v1), Section 3.2, lines 160–161) |
| workflow | Graph-Structured | Population search selects parents and children. ([source](https://arxiv.org/html/2611.34783v1), Sections 3.2–3.3) |
| update_strategy | Local Patch, Regeneration, Candidate Selection | Edits, redesigns and selects layouts. ([source](https://arxiv.org/html/2611.34783v1), Sections 3.2–3.4) |
| verifier | Critic, Programmatic | VLM judges; geometry rules check validity. ([source](https://arxiv.org/html/2611.34783v1), Section 3.4; Section 7.3) |
| feedback_assessment | Score, Diagnosis | Fitness and unmet requirements guide mutation. ([source](https://arxiv.org/html/2611.34783v1), Section 3.4, line 168) |
| feedback_observation | Structural Scene State | Checks overlap, supports and doors. ([source](https://arxiv.org/html/2611.34783v1), Section 7.3, line 447) |
| memory_time | Short-Term Memory | Retains a search archive for parent sampling. ([source](https://arxiv.org/html/2611.34783v1), Section 3.4, line 168) |
| memory_reach | Unclear |  |
| action_type | Code/Script | Agent edits and executes Python. ([source](https://arxiv.org/html/2611.34783v1), Section 3.3, line 163) |
| graphics_software | Unclear |  |
| tools | Graphics Operations, Static Validator | Program edits plus geometric validity checks. ([source](https://arxiv.org/html/2611.34783v1), Sections 3.3–3.4; 7.3) |
| resources | Unclear |  |
| representation | Code, Geometry | Programs transform input objects. ([source](https://arxiv.org/html/2611.34783v1), Section 3, Figure 2) |

next_action: "Review full method and survey suitability before corpus inclusion."

Events: [{"type": "first_submission", "value": "2026-11-25T17:41:34+00:00", "precision": "timestamp", "timezone": "UTC", "raw_source_value": "Wed, 25 Nov 2026 17:41:34 UTC", "raw_source_timezone": "UTC", "local_value": "2026-11-25T11:41:34-06:00", "primary_url": "https://arxiv.org/abs/2611.34783", "authority": "primary", "version": "v1", "evidence": "arXiv submission history reports v1 at the preserved UTC timestamp.", "locator": "Submission history, v1", "raw_evidence_archive": "retrieval/04.json", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: []

### [PreferenceScene: Personalized Indoor Scene Synthesis from Feedback](https://arxiv.org/abs/2611.32099)
core | Medium | new_relative_to_snapshot
Application: Static / Scene; operations: Generation, Editing
An LLM updates an explicit room-preference plan from feedback, then instantiates each attribute in a 3D scene.
Scope: An LLM updates an explicit room-preference plan from feedback, then instantiates each attribute in a 3D scene.
Limits: Human feedback is supported by the interaction study; benchmark users are simulated. The offline evaluator is not classified as an in-loop critic.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Modeling | Builds personalized room scenes. ([source](https://arxiv.org/html/2611.32099v1), Section 4.3) |
| input_form | Language | Room instructions and textual feedback. ([source](https://arxiv.org/html/2611.32099v1), Sections 4.1–4.2) |
| output | Structured Specification, Graphics Artifact | Plans become specifications and scenes. ([source](https://arxiv.org/html/2611.32099v1), Sections 4.2–4.3) |
| model_type | LLM | LLM writes and revises plans. ([source](https://arxiv.org/html/2611.32099v1), Sections 4.1–4.2) |
| model_training | Unclear |  |
| planning | PO-2 | LLM plans within fixed attribute machinery. ([source](https://arxiv.org/html/2611.32099v1), Sections 4.1–4.3) |
| workflow | Sequential | Plan, instantiate, feedback, update. ([source](https://arxiv.org/html/2611.32099v1), Section 4, line 225) |
| update_strategy | Replanning | Reconsiders every attribute after feedback. ([source](https://arxiv.org/html/2611.32099v1), Section 4.2, line 242) |
| verifier | Human | Participants review scenes each turn. ([source](https://arxiv.org/html/2611.32099v1), Appendix F, line 1516) |
| feedback_assessment | Score, Diagnosis | Receives satisfaction scores and critiques. ([source](https://arxiv.org/html/2611.32099v1), Appendix F, line 1516) |
| feedback_observation | Structural Scene State | Updates receive descriptions of built scenes. ([source](https://arxiv.org/html/2611.32099v1), Section 4.2, lines 235–241) |
| memory_time | Short-Term Memory | Whole interaction history enters updates. ([source](https://arxiv.org/html/2611.32099v1), Section 4.2, line 235) |
| memory_reach | Unclear |  |
| action_type | Structured Specification | Values translate to object specifications. ([source](https://arxiv.org/html/2611.32099v1), Section 4.3, line 245) |
| graphics_software | Unclear |  |
| tools | Graphics Operations | Instantiates objects, finishes and lighting. ([source](https://arxiv.org/html/2611.32099v1), Section 4.3, lines 245–247) |
| resources | Assets | Retrieves Objaverse objects and ambientCG materials. ([source](https://arxiv.org/html/2611.32099v1), Section 4.3, line 247) |
| representation | Geometry | Specifications instantiate a 3D room. ([source](https://arxiv.org/html/2611.32099v1), Section 4.3) |

next_action: "Review full method and survey suitability before corpus inclusion."

Events: [{"type": "first_submission", "value": "2026-11-24T07:19:27+00:00", "precision": "timestamp", "timezone": "UTC", "raw_source_value": "Tue, 24 Nov 2026 07:19:27 UTC", "raw_source_timezone": "UTC", "local_value": "2026-11-24T01:19:27-06:00", "primary_url": "https://arxiv.org/abs/2611.32099", "authority": "primary", "version": "v1", "evidence": "arXiv submission history reports v1 at the preserved UTC timestamp.", "locator": "Submission history, v1", "raw_evidence_archive": "retrieval/06.json", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: ["Human verifier applies to live interaction; benchmark simulated user is a different evidence source. Offline preference evaluator is not an in-loop critic."]

### [MAGPIE: Agentic Multi-Reference Image Generation via Executable Scene Construction](https://arxiv.org/abs/2611.32462)
core | Medium | new_relative_to_snapshot
Application: 2D Graphics, Static / Scene; operations: Generation, Editing
A multimodal coding harness constructs and refines Blender proxies before reference-grounded image synthesis.
Scope: A multimodal coding harness constructs and refines Blender proxies before reference-grounded image synthesis.
Limits: Generator adaptation does not establish agent-model training. Cross-example harness refinement and memory require further reading.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Modeling | Constructs a 3D composition proxy. ([source](https://arxiv.org/html/2611.32462v1), Section 3.1, line 131) |
| input_form | Language, Image | Reference images and instructions. ([source](https://arxiv.org/html/2611.32462v1), Section 3.1, line 131) |
| output | Program, Rendered Media | Blender program guides image synthesis. ([source](https://arxiv.org/html/2611.32462v1), Section 3.1; Section 3.2) |
| model_type | VLM | Multimodal coding harness handles references. ([source](https://arxiv.org/html/2611.32462v1), Section 3.1, line 131) |
| model_training | Unclear |  |
| planning | PO-2 | Scene planning within fixed construction stages. ([source](https://arxiv.org/html/2611.32462v1), Section 3.1, line 131) |
| workflow | Sequential | Plans, constructs, refines, synthesizes. ([source](https://arxiv.org/html/2611.32462v1), Sections 3.1–3.2) |
| update_strategy | Local Patch, Candidate Selection | Revises code and retains best proxy. ([source](https://arxiv.org/html/2611.32462v1), Appendix refinement study, lines 410, 445) |
| verifier | Programmatic | Geometry verifier checks mesh constraints. ([source](https://arxiv.org/html/2611.32462v1), Section 3.1, lines 145–146) |
| feedback_assessment | Diagnosis | Localized feedback identifies geometric inconsistencies. ([source](https://arxiv.org/html/2611.32462v1), Section 3.1, line 146) |
| feedback_observation | Visual, Structural Scene State | Renders and executed meshes guide refinement. ([source](https://arxiv.org/html/2611.32462v1), Section 3.1, lines 131, 145–146) |
| memory_time | Unclear |  |
| memory_reach | Unclear |  |
| action_type | Code/Script | Writes executable Blender scenes. ([source](https://arxiv.org/html/2611.32462v1), Section 3.1, line 131) |
| graphics_software | Unclear |  |
| tools | Graphics Operations, Static Validator | Scene construction and geometric checks. ([source](https://arxiv.org/html/2611.32462v1), Section 3.1) |
| resources | Unclear |  |
| representation | Code, Geometry, Pixels | Proxy code, meshes and final image. ([source](https://arxiv.org/html/2611.32462v1), Sections 3.1–3.2) |

next_action: "Review full method and survey suitability before corpus inclusion."

Events: [{"type": "first_submission", "value": "2026-11-24T11:58:12+00:00", "precision": "timestamp", "timezone": "UTC", "raw_source_value": "Tue, 24 Nov 2026 11:58:12 UTC", "raw_source_timezone": "UTC", "local_value": "2026-11-24T05:58:12-06:00", "primary_url": "https://arxiv.org/abs/2611.32462", "authority": "primary", "version": "v1", "evidence": "arXiv submission history reports v1 at the preserved UTC timestamp.", "locator": "Submission history, v1", "raw_evidence_archive": "retrieval/06.json", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: []

### [AdProducer: Towards Agentic Advertising Video Generation](https://arxiv.org/abs/2611.31466)
core | Medium | new_relative_to_snapshot
Application: Dynamic / Animation and temporal scene, Datasets and Benchmarks; operations: Generation
A trained multimodal agent researches products and specifies storyboards for a frozen video generator.
Scope: A trained multimodal agent researches products and specifies storyboards for a frozen video generator.
Limits: Training rewards and independent benchmark judges do not establish an inference-time video repair loop; verifier fields remain Unclear.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Animation | Creates multi-shot video advertisements. ([source](https://arxiv.org/html/2611.31466v1), Section 3.1) |
| input_form | Language | Starts from a concise creative brief. ([source](https://arxiv.org/html/2611.31466v1), Section 3.1, line 104) |
| output | Structured Specification, Rendered Media | Storyboard renders into an advertisement. ([source](https://arxiv.org/html/2611.31466v1), Section 3.1, lines 104–105) |
| model_type | VLM | Multimodal agent collects visual references. ([source](https://arxiv.org/html/2611.31466v1), Section 3.1, line 104) |
| model_training | Supervised Fine-Tuning, RL Post-Training | Agent undergoes SFT then RL. ([source](https://arxiv.org/html/2611.31466v1), Section 3.2, line 109) |
| planning | PO-2 | Agent plans shots within research-to-render pipeline. ([source](https://arxiv.org/html/2611.31466v1), Section 3.1, lines 104–106) |
| workflow | Sequential | Research trajectory culminates in storyboard rendering. ([source](https://arxiv.org/html/2611.31466v1), Section 3.1, line 105) |
| update_strategy | Unclear |  |
| verifier | Unclear |  |
| feedback_assessment | Unclear |  |
| feedback_observation | Unclear |  |
| memory_time | Unclear |  |
| memory_reach | Unclear |  |
| action_type | Structured Specification | Specifies shot timing, cameras and references. ([source](https://arxiv.org/html/2611.31466v1), Section 3.1, line 106) |
| graphics_software | Unclear |  |
| tools | Unclear |  |
| resources | Assets | Retrieves product-specific visual references. ([source](https://arxiv.org/html/2611.31466v1), Section 3.1, line 106) |
| representation | Pixels | Frozen generator renders final video. ([source](https://arxiv.org/html/2611.31466v1), Section 3.1, line 105) |

artifact_links: [{"url": "https://lky-ang.github.io/AdProducer-page/", "role": "official project; reached", "raw_evidence_archive": "retrieval/07.json"}]

next_action: "Review full method and survey suitability before corpus inclusion."

Events: [{"type": "first_submission", "value": "2026-11-23T19:37:29+00:00", "precision": "timestamp", "timezone": "UTC", "raw_source_value": "Mon, 23 Nov 2026 19:37:29 UTC", "raw_source_timezone": "UTC", "local_value": "2026-11-23T13:37:29-06:00", "primary_url": "https://arxiv.org/abs/2611.31466", "authority": "primary", "version": "v1", "evidence": "arXiv submission history reports v1 at the preserved UTC timestamp.", "locator": "Submission history, v1", "raw_evidence_archive": "retrieval/07.json", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: ["Product web research tools fall outside the provisional graphics-tools labels. Agent training is distinct from frozen video synthesis."]

### [Lab2Sim: Agentic Generation of Interactive Laboratory Equipment from Operation Videos](https://arxiv.org/abs/2611.33705)
core | Medium | new_relative_to_snapshot
Application: Dynamic / Articulated assets, Dynamic / Physical simulation and effects; operations: Reconstruction, Generation
Agents build editable laboratory equipment from videos, revise assets under independent verification, and adapt them using simulation feedback.
Scope: Agents build editable laboratory equipment from videos, revise assets under independent verification, and adapt them using simulation feedback.
Limits: Selected sections only; model training is unverified. Simulation integration supports articulated behavior, beyond static simulation-ready geometry.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Modeling, Simulation | Constructs assets and simulates equipment behavior. ([source](https://arxiv.org/html/2611.33705v1), Section 3, Figure 2) |
| input_form | Video | Operation videos supply evidence. ([source](https://arxiv.org/html/2611.33705v1), Section 3, Figure 2) |
| output | Program, Graphics Artifact | Delivers code, Blender files and meshes. ([source](https://arxiv.org/html/2611.33705v1), Section 3.2, line 113) |
| model_type | VLM | Role-specific multimodal model sessions. ([source](https://arxiv.org/html/2611.33705v1), Section 3.2, line 100) |
| model_training | Unclear |  |
| planning | PO-2 | Agent build plans within deterministic coordination. ([source](https://arxiv.org/html/2611.33705v1), Section 3.2, lines 100–113) |
| workflow | Sequential | Coordinator processes assets in order. ([source](https://arxiv.org/html/2611.33705v1), Appendix A.1, line 283) |
| update_strategy | Local Patch, Replanning | Revises build plans and affected regions. ([source](https://arxiv.org/html/2611.33705v1), Section 3.2, line 120) |
| verifier | Critic, Environment | Independent verifier and simulation feedback. ([source](https://arxiv.org/html/2611.33705v1), Abstract, line 49; Figure 2) |
| feedback_assessment | Binary, Diagnosis | Checks pass/fail; defects prompt edits. ([source](https://arxiv.org/html/2611.33705v1), Appendix A.5, lines 382–392) |
| feedback_observation | Visual, Structural Scene State, Runtime | Inspects renders, geometry and execution. ([source](https://arxiv.org/html/2611.33705v1), Figure 2; Abstract, line 49) |
| memory_time | Short-Term Memory | Earlier repair records remain retrievable. ([source](https://arxiv.org/html/2611.33705v1), Appendix A.5, line 385) |
| memory_reach | Local Memory | Roles operate separate model sessions. ([source](https://arxiv.org/html/2611.33705v1), Section 3.2, line 100) |
| action_type | Code/Script, Tool/Function Call | Modeling code invokes Blender MCP tools. ([source](https://arxiv.org/html/2611.33705v1), Section 3.2, line 113) |
| graphics_software | Agent-Adapted | MCP exposes Blender to agents. ([source](https://arxiv.org/html/2611.33705v1), Appendix A.3, line 374) |
| tools | Graphics Operations | Tools construct and edit Blender assets. ([source](https://arxiv.org/html/2611.33705v1), Appendix A.3, line 374) |
| resources | Unclear |  |
| representation | Code, Geometry, Dynamic State | Code, meshes and articulated simulation instances. ([source](https://arxiv.org/html/2611.33705v1), Figure 2; Section 3.2) |

next_action: "Review full method and survey suitability before corpus inclusion."

Events: [{"type": "first_submission", "value": "2026-11-25T03:18:52+00:00", "precision": "timestamp", "timezone": "UTC", "raw_source_value": "Wed, 25 Nov 2026 03:18:52 UTC", "raw_source_timezone": "UTC", "local_value": "2026-11-24T21:18:52-06:00", "primary_url": "https://arxiv.org/abs/2611.33705", "authority": "primary", "version": "v1", "evidence": "arXiv submission history reports v1 at the preserved UTC timestamp.", "locator": "Submission history, v1", "raw_evidence_archive": "retrieval/08.json", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: []

### [Beyond Code and Pixels: Co-Generating Editable and Visually Rich Presentations](https://arxiv.org/abs/2611.28010)
core | Medium | new_relative_to_snapshot
Application: 2D Graphics; operations: Generation
SlidesWeaver coordinates language and vision agents through shared presentation states to preserve native text and geometry.
Scope: SlidesWeaver coordinates language and vision agents through shared presentation states to preserve native text and geometry.
Limits: Abstract-only mechanism reading. Source v1 says September 8 under a November identifier: first-submission date is unresolved; only v2 revision is retained as a dated event.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Visualization | Authors structured presentations. ([source](https://arxiv.org/abs/2611.28010), Abstract) |
| input_form | Unclear |  |
| output | Graphics Artifact | Preserves native text and geometry. ([source](https://arxiv.org/abs/2611.28010), Abstract) |
| model_type | Hybrid | Coordinates language and vision agents. ([source](https://arxiv.org/abs/2611.28010), Abstract) |
| model_training | Unclear |  |
| planning | Unclear |  |
| workflow | Unclear |  |
| update_strategy | Unclear |  |
| verifier | Unclear |  |
| feedback_assessment | Unclear |  |
| feedback_observation | Unclear |  |
| memory_time | Short-Term Memory | Shares deck and slide states during generation. ([source](https://arxiv.org/abs/2611.28010), Abstract) |
| memory_reach | Global Memory | Agents coordinate through shared states. ([source](https://arxiv.org/abs/2611.28010), Abstract) |
| action_type | Unclear |  |
| graphics_software | Unclear |  |
| tools | Unclear |  |
| resources | Unclear |  |
| representation | Layouts, Pixels | Combines native geometry with visual composition. ([source](https://arxiv.org/abs/2611.28010), Abstract) |

next_action: "Verify anomalous v1 history and read full method; v2 content changes not assessed."

Events: [{"type": "revision", "value": "2026-11-25T14:23:43+00:00", "precision": "timestamp", "timezone": "UTC", "raw_source_value": "Wed, 25 Nov 2026 14:23:43 UTC", "raw_source_timezone": "UTC", "local_value": "2026-11-25T08:23:43-06:00", "primary_url": "https://arxiv.org/abs/2611.28010", "authority": "primary", "version": "v2", "evidence": "arXiv submission history reports v2 at the preserved UTC timestamp.", "locator": "Submission history, v2", "raw_evidence_archive": "retrieval/09.json", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: []

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

## excluded (1)

### [Residual Guidance for Real-Time Interactive Video Generation](https://arxiv.org/abs/2611.32820)
excluded | Medium | new_relative_to_snapshot
Application: Dynamic / Animation and temporal scene; operations: Generation
E2_NON_AGENTIC: the inspected abstract describes a training-free correction for streaming-video context inertia, without an agentic controller or tool loop.
Scope: E2_NON_AGENTIC: the inspected abstract describes a training-free correction for streaming-video context inertia, without an agentic controller or tool loop.
Limits: Abstract-level scope exclusion; full method not opened. Reconsider if an agentic component is documented.

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

next_action: "Retain exclusion with abstract evidence."

Events: [{"type": "first_submission", "value": "2026-11-24T15:35:58+00:00", "precision": "timestamp", "timezone": "UTC", "raw_source_value": "Tue, 24 Nov 2026 15:35:58 UTC", "raw_source_timezone": "UTC", "local_value": "2026-11-24T09:35:58-06:00", "primary_url": "https://arxiv.org/abs/2611.32820", "authority": "primary", "version": "v1", "evidence": "arXiv submission history reports v1 at the preserved UTC timestamp.", "locator": "Submission history, v1", "raw_evidence_archive": "retrieval/09.json", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: []

## Application index
| Application | Papers |
|---|---|
| 2D Graphics | [MAGPIE: Agentic Multi-Reference Image Generation via Executable Scene Construction](https://arxiv.org/abs/2611.32462) [late_discovery]; [Beyond Code and Pixels: Co-Generating Editable and Visually Rich Presentations](https://arxiv.org/abs/2611.28010) [late_discovery] |
| Static / Object | None verified in this run |
| Static / CAD | None verified in this run |
| Static / Scene | [SceneDesigner3D: Agentic Evolutionary Search for Principled Rearrangement of 3D Indoor Scenes](https://arxiv.org/abs/2611.34783) [late_discovery]; [PreferenceScene: Personalized Indoor Scene Synthesis from Feedback](https://arxiv.org/abs/2611.32099) [late_discovery]; [MAGPIE: Agentic Multi-Reference Image Generation via Executable Scene Construction](https://arxiv.org/abs/2611.32462) [late_discovery] |
| Dynamic / Articulated assets | [Lab2Sim: Agentic Generation of Interactive Laboratory Equipment from Operation Videos](https://arxiv.org/abs/2611.33705) [late_discovery] |
| Dynamic / Animation and temporal scene | [AdProducer: Towards Agentic Advertising Video Generation](https://arxiv.org/abs/2611.31466) [late_discovery] |
| Dynamic / Physical simulation and effects | [Lab2Sim: Agentic Generation of Interactive Laboratory Equipment from Operation Videos](https://arxiv.org/abs/2611.33705) [late_discovery] |
| Datasets and Benchmarks | [AdProducer: Towards Agentic Advertising Video Generation](https://arxiv.org/abs/2611.31466) [late_discovery] |
| Cross-category | [NeoWorld-Pro: Programming Interactive Scenes from Monocular Images for Embodied Simulation](https://arxiv.org/abs/2608.24212) [unresolved]; [PhotoGuider: Composition-Aware Cropping and 360° View Framing with Explainable Photographic Assessments](https://arxiv.org/abs/2611.02897) [unresolved]; [SceneAgent: An Agentic Pipeline from 3D and 4D Captures to Simulation Environments](https://arxiv.org/abs/2610.34745) [unresolved]; [Agentic AI for Scientific Visualization: Tool-Calling Pipelines for Automated Chart and Diagram Generation in Research Writing](https://www.scitepress.org/PublishedPapers/2026/152298/) [unresolved]; [FLASH: A "Generate Once, Synthesize Many" Framework for Synthetic Anomaly Generation in Industrial Anomaly Detection](https://arxiv.org/abs/2609.37314) [unresolved]; [Agent-Guided Immersive World Generation with Alpha-Textured Proxies](https://immersegen.github.io/) [unresolved]; [HiLSVA: Design and Evaluation of a Human-in-the-Loop Agentic System for Scientific Visualization](https://arxiv.org/abs/2606.26614) [unresolved]; [Exploring LLM Agent Designs and Interaction Modalities for Scientific Visualization](https://arxiv.org/abs/2604.27996) [unresolved]; [DramaAgent: Agentic Storytelling Video Generation](https://aclanthology.org/2026.aacl-long.163/) [unresolved]; [ShaderAgent: Self-Evolving Agentic Procedural Material Generation](https://github.com/VAST-AI-Research/ShaderAgent) [unresolved] |

## Source ledger

| Source | Status | Limits |
|---|---|---|
| arxiv | partial | Seven category pages, seven canonical histories and five method pages reached; excerpts only; CV recent limited to first 50 entries. |
| hugging_face | partial | Dated URL inaccessible; root Nov 26 heading and dated-page search fallback reached. Curation is not event evidence. |
| openreview | partial | Direct search inaccessible; restricted queries returned older PDFs and noisy venue pages; no same-day event verified. |
| official_venues | partial | SIGGRAPH Asia technical-paper overview reached; ACM and CVF searches attempted, without proceedings-wide inspection. |
| project_author_lab | partial | AdProducer official project reached; additional project searches attempted; unreviewed signals retained in pending queue. |

## Exact retrieval ledger

Times below are actual post-return recording times; exact per-page retrieval times are not exposed. Full requests, returned evidence and call-start times are in the linked journals.

| Journal | Recorded at (UTC) | Operation | Executed query / URL / find |
|---|---|---|---|
| [01](retrieval/01.json) | 2026-11-26T20:04:25+00:00 | search_query | agent SVG diagram slide poster visual feedback November 2026 |
| [01](retrieval/01.json) | 2026-11-26T20:04:25+00:00 | search_query | agent 3D Blender procedural material "2026-11-26" |
| [01](retrieval/01.json) | 2026-11-26T20:04:25+00:00 | search_query | agent CAD program repair visual feedback November 2026 |
| [01](retrieval/01.json) | 2026-11-26T20:04:25+00:00 | open | https://arxiv.org/list/cs.GR/new |
| [01](retrieval/01.json) | 2026-11-26T20:04:25+00:00 | open | https://arxiv.org/list/cs.CV/recent |
| [01](retrieval/01.json) | 2026-11-26T20:04:25+00:00 | open | https://huggingface.co/papers/date/2026-11-26 |
| [02](retrieval/02.json) | 2026-11-26T20:04:31+00:00 | search_query | agent 3D scene layout generation November 26 2026 arxiv |
| [02](retrieval/02.json) | 2026-11-26T20:04:31+00:00 | search_query | agent articulated assets rig joint generation recent |
| [02](retrieval/02.json) | 2026-11-26T20:04:31+00:00 | search_query | agent animation cinematography temporal scene November 2026 |
| [02](retrieval/02.json) | 2026-11-26T20:04:31+00:00 | open | https://arxiv.org/list/cs.RO/new |
| [02](retrieval/02.json) | 2026-11-26T20:04:31+00:00 | open | https://huggingface.co/papers |
| [02](retrieval/02.json) | 2026-11-26T20:04:31+00:00 | open | https://openreview.net/search?term=graphics%20agent |
| [02](retrieval/02.json) | 2026-11-26T20:04:31+00:00 | find | turn0view0 [find: Title:] |
| [02](retrieval/02.json) | 2026-11-26T20:04:31+00:00 | find | turn0view1 [find: Agent] |
| [03](retrieval/03.json) | 2026-11-26T20:04:38+00:00 | search_query | agent physical simulation particle deformable graphics November 2026 arxiv |
| [03](retrieval/03.json) | 2026-11-26T20:04:38+00:00 | search_query | agent graphics benchmark world auditing verification "2026-11" |
| [03](retrieval/03.json) | 2026-11-26T20:04:38+00:00 | search_query | site:openreview.net graphics agent memory replanning tool feedback 2026 |
| [03](retrieval/03.json) | 2026-11-26T20:04:38+00:00 | open | https://arxiv.org/list/cs.AI/new |
| [03](retrieval/03.json) | 2026-11-26T20:04:38+00:00 | open | https://asia.siggraph.org/2026/program/technical-papers/ |
| [03](retrieval/03.json) | 2026-11-26T20:04:38+00:00 | open | https://arxiv.org/abs/2611.34783 |
| [03](retrieval/03.json) | 2026-11-26T20:04:38+00:00 | find | turn0view0 [find: Agent] |
| [03](retrieval/03.json) | 2026-11-26T20:04:38+00:00 | find | turn1view1 [find: Nov 26] |
| [03](retrieval/03.json) | 2026-11-26T20:04:38+00:00 | find | turn1view1 [find: SceneDesigner] |
| [04](retrieval/04.json) | 2026-11-26T20:04:47+00:00 | search_query | site:arxiv.org "agent" "SVG" "Nov" "2026" |
| [04](retrieval/04.json) | 2026-11-26T20:04:47+00:00 | search_query | site:openreview.net "graphics" "agent" "2026" |
| [04](retrieval/04.json) | 2026-11-26T20:04:47+00:00 | search_query | site:dl.acm.org "agent" "November 2026" graphics |
| [04](retrieval/04.json) | 2026-11-26T20:04:47+00:00 | open | https://arxiv.org/list/cs.HC/new |
| [04](retrieval/04.json) | 2026-11-26T20:04:47+00:00 | open | https://arxiv.org/list/cs.MM/new |
| [04](retrieval/04.json) | 2026-11-26T20:04:47+00:00 | open | https://arxiv.org/list/eess.IV/new |
| [04](retrieval/04.json) | 2026-11-26T20:04:47+00:00 | find | turn1view1 [find: Agent] |
| [04](retrieval/04.json) | 2026-11-26T20:04:47+00:00 | find | turn2view2 [find: Submission history] |
| [04](retrieval/04.json) | 2026-11-26T20:04:47+00:00 | find | turn1view0 [find: generation] |
| [05](retrieval/05.json) | 2026-11-26T20:04:54+00:00 | search_query | "MAGPIE" "Executable Scene Construction" |
| [05](retrieval/05.json) | 2026-11-26T20:04:54+00:00 | search_query | "PreferenceScene" personalized |
| [05](retrieval/05.json) | 2026-11-26T20:04:54+00:00 | search_query | "Lab2Sim" "2611.33705" |
| [05](retrieval/05.json) | 2026-11-26T20:04:54+00:00 | open | https://arxiv.org/html/2611.34783v1 |
| [05](retrieval/05.json) | 2026-11-26T20:04:54+00:00 | open | https://arxiv.org/abs/2611.32099 |
| [05](retrieval/05.json) | 2026-11-26T20:04:54+00:00 | open | https://arxiv.org/abs/2611.32462 |
| [05](retrieval/05.json) | 2026-11-26T20:04:54+00:00 | find | turn3view0 [find: Title:] |
| [05](retrieval/05.json) | 2026-11-26T20:04:54+00:00 | find | turn3view1 [find: Title:] |
| [05](retrieval/05.json) | 2026-11-26T20:04:54+00:00 | find | turn3view2 [find: agent] |
| [06](retrieval/06.json) | 2026-11-26T20:05:03+00:00 | search_query | "AdProducer" "video" project |
| [06](retrieval/06.json) | 2026-11-26T20:05:03+00:00 | search_query | "SceneDesigner3D" project |
| [06](retrieval/06.json) | 2026-11-26T20:05:03+00:00 | search_query | site:arxiv.org "agent" "2026-11-26" graphics Blender |
| [06](retrieval/06.json) | 2026-11-26T20:05:03+00:00 | open | https://arxiv.org/html/2611.32099v1 |
| [06](retrieval/06.json) | 2026-11-26T20:05:03+00:00 | open | https://arxiv.org/html/2611.32462v1 |
| [06](retrieval/06.json) | 2026-11-26T20:05:03+00:00 | open | https://arxiv.org/abs/2611.31466 |
| [06](retrieval/06.json) | 2026-11-26T20:05:03+00:00 | find | turn4view1 [find: Submission history] |
| [06](retrieval/06.json) | 2026-11-26T20:05:03+00:00 | find | turn4view2 [find: Submission history] |
| [06](retrieval/06.json) | 2026-11-26T20:05:03+00:00 | find | turn4view0 [find: 3.] |
| [07](retrieval/07.json) | 2026-11-26T20:05:14+00:00 | search_query | site:huggingface.co/papers/date/2026-11-26 graphics agent |
| [07](retrieval/07.json) | 2026-11-26T20:05:14+00:00 | search_query | site:arxiv.org "agent" "CAD" "Nov 2026" |
| [07](retrieval/07.json) | 2026-11-26T20:05:14+00:00 | search_query | site:openaccess.thecvf.com "agent" "graphics" "2026" |
| [07](retrieval/07.json) | 2026-11-26T20:05:14+00:00 | open | https://arxiv.org/abs/2611.33705 |
| [07](retrieval/07.json) | 2026-11-26T20:05:14+00:00 | open | https://arxiv.org/html/2611.31466v1 |
| [07](retrieval/07.json) | 2026-11-26T20:05:14+00:00 | open | https://lky-ang.github.io/AdProducer-page/ |
| [07](retrieval/07.json) | 2026-11-26T20:05:14+00:00 | find | turn5view2 [find: Submission history] |
| [07](retrieval/07.json) | 2026-11-26T20:05:14+00:00 | find | turn4view0 [find: validity] |
| [07](retrieval/07.json) | 2026-11-26T20:05:14+00:00 | find | turn5view0 [find: ## 3] |
| [07](retrieval/07.json) | 2026-11-26T20:05:14+00:00 | find | turn5view1 [find: ## 3] |
| [08](retrieval/08.json) | 2026-11-26T20:05:23+00:00 | search_query | "ManimAgent" "agent" "November 2026" |
| [08](retrieval/08.json) | 2026-11-26T20:05:23+00:00 | search_query | "SceneSmith" "SceneDesigner3D" |
| [08](retrieval/08.json) | 2026-11-26T20:05:23+00:00 | search_query | "agent" "physical simulation" "November 26, 2026" |
| [08](retrieval/08.json) | 2026-11-26T20:05:23+00:00 | open | https://arxiv.org/html/2611.33705v1 |
| [08](retrieval/08.json) | 2026-11-26T20:05:23+00:00 | open | https://arxiv.org/abs/2611.32820 |
| [08](retrieval/08.json) | 2026-11-26T20:05:23+00:00 | open | https://arxiv.org/abs/2611.28010 |
| [08](retrieval/08.json) | 2026-11-26T20:05:23+00:00 | find | turn6view0 [find: Submission history] |
| [08](retrieval/08.json) | 2026-11-26T20:05:23+00:00 | find | turn5view0 [find: ### 4.1] |
| [08](retrieval/08.json) | 2026-11-26T20:05:23+00:00 | find | turn5view1 [find: verification] |
| [08](retrieval/08.json) | 2026-11-26T20:05:23+00:00 | find | turn6view1 [find: ## 3] |
| [09](retrieval/09.json) | 2026-11-26T20:05:32+00:00 | search_query | site:arxiv.org "agent" "Blender" after:2026-11-19 before:2026-11-27 |
| [09](retrieval/09.json) | 2026-11-26T20:05:32+00:00 | search_query | site:arxiv.org "agent" "CAD" after:2026-11-19 before:2026-11-27 |
| [09](retrieval/09.json) | 2026-11-26T20:05:32+00:00 | search_query | "agent" "graphics" "26 November 2026" |
| [09](retrieval/09.json) | 2026-11-26T20:05:32+00:00 | find | turn7view1 [find: Abstract:] |
| [09](retrieval/09.json) | 2026-11-26T20:05:32+00:00 | find | turn7view1 [find: Submission history] |
| [09](retrieval/09.json) | 2026-11-26T20:05:32+00:00 | find | turn7view2 [find: Abstract:] |
| [09](retrieval/09.json) | 2026-11-26T20:05:32+00:00 | find | turn7view2 [find: Submission history] |
| [09](retrieval/09.json) | 2026-11-26T20:05:32+00:00 | find | turn7view0 [find: ## 3] |
| [09](retrieval/09.json) | 2026-11-26T20:05:32+00:00 | find | turn5view1 [find: ### 3.2] |
| [09](retrieval/09.json) | 2026-11-26T20:05:32+00:00 | find | turn5view0 [find: ### 4.2] |
| [09](retrieval/09.json) | 2026-11-26T20:05:32+00:00 | find | turn4view0 [find: ### 3.4] |
| [10](retrieval/10.json) | 2026-11-26T20:05:42+00:00 | search_query | "agentic" "graphics" "2026-11-26" arxiv |
| [10](retrieval/10.json) | 2026-11-26T20:05:42+00:00 | search_query | "agent" "rig" "Nov" "2026" arxiv |
| [10](retrieval/10.json) | 2026-11-26T20:05:42+00:00 | search_query | "agent" "simulation" "2026-11-26" arxiv |
| [10](retrieval/10.json) | 2026-11-26T20:05:42+00:00 | find | turn7view0 [find: The Asset Agent] |
| [10](retrieval/10.json) | 2026-11-26T20:05:42+00:00 | find | turn7view0 [find: feedback] |
| [10](retrieval/10.json) | 2026-11-26T20:05:42+00:00 | find | turn5view1 [find: ### 3.1] |
| [10](retrieval/10.json) | 2026-11-26T20:05:42+00:00 | find | turn5view1 [find: verifier] |
| [10](retrieval/10.json) | 2026-11-26T20:05:42+00:00 | find | turn5view0 [find: At each turn] |
| [10](retrieval/10.json) | 2026-11-26T20:05:42+00:00 | find | turn5view0 [find: Blender] |
| [10](retrieval/10.json) | 2026-11-26T20:05:42+00:00 | find | turn4view0 [find: ### 3.1] |
| [10](retrieval/10.json) | 2026-11-26T20:05:42+00:00 | find | turn1view1 [find: ###] |
| [11](retrieval/11.json) | 2026-11-26T20:05:50+00:00 | find | turn2view2 [find: Authors:] |
| [11](retrieval/11.json) | 2026-11-26T20:05:50+00:00 | find | turn4view1 [find: Authors:] |
| [11](retrieval/11.json) | 2026-11-26T20:05:50+00:00 | find | turn4view2 [find: Authors:] |
| [11](retrieval/11.json) | 2026-11-26T20:05:50+00:00 | find | turn5view2 [find: Authors:] |
| [11](retrieval/11.json) | 2026-11-26T20:05:50+00:00 | find | turn6view0 [find: Authors:] |
| [11](retrieval/11.json) | 2026-11-26T20:05:50+00:00 | find | turn5view1 [find: The vision] |
| [11](retrieval/11.json) | 2026-11-26T20:05:50+00:00 | find | turn5view1 [find: Cross-Example Harness] |
| [11](retrieval/11.json) | 2026-11-26T20:05:50+00:00 | find | turn4view0 [find: We represent] |
| [11](retrieval/11.json) | 2026-11-26T20:05:50+00:00 | find | turn5view0 [find: The scene instantiation] |

## Query-family coverage

- 2d: partial; journals 01, 04, 08.
- object: partial; journals 01, 04, 05, 06, 09, 10, 11.
- cad: partial; journals 01, 04, 07, 09.
- scene: partial; journals 02, 05, 06, 07, 08, 09, 10, 11.
- articulation: partial; journals 02, 04, 05, 10, 11.
- animation: partial; journals 02, 05, 06, 07, 08, 09, 11.
- simulation: partial; journals 03, 08, 10.
- benchmark: partial; journals 03, 07.
- harness: partial; journals 03, 04, 06, 08, 09, 10, 11.

## Previously reported identity signals

These resurfaced in current searches; prior dates are historical context, not fresh checks.

- 2611.17821: SceneAgent: A Multi-Agent Framework for Portable Game Scene Generation
- 2611.25340: SceneAnything: Agentic Reconstruction of Large-Scale Mesh Scenes from a Single Video
- 2610.34745: SceneAgent: An Agentic Pipeline from 3D and 4D Captures to Simulation Environments
- 2610.39924: PhysAg3D: Bridging 3D Generative and Agentic Models for High-Fidelity and Physically-Interactive Assets

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
- Real2SimLab: A Unified Platform for Real-to-Simulation Transfer: HF listing only; primary identity, history and scope not checked.
- Connecting AI Agents to Live Discrete Element Simulations via the Model Context Protocol: Secondary search identity; primary paper and event not opened within cap.
- Agentic LongLive: Asynchronous Agentic Memory for Long Video Generation: Secondary dated-listing lead; canonical identity, mechanism and history unverified.
- Nemotron-Labs-VisualCreation: Pixel as Code for Agentic Visual Creation: Secondary search lead; primary paper, scope and date unresolved.
- FineDex: Bridging Fine-Grained Human-Object Interaction Generation to Dexterous Humanoid Manipulation: RO listing describes HOI generation and downstream control; authoring boundary/history need primary reading.
- SlidesWeaver first-submission date anomaly: Primary history reports September 8 v1 under a November identifier. Retained v2 revision separately; first event needs versioned metadata confirmation.
- Blueprint procedural house workflow: Secondary repository signal only; no verified research or artifact event.

## Final audit

Structural validation, exact primary-history timestamp/version pairing, Chicago conversions, prior-event comparison, ledger counts and JSONL consistency passed. All 18 fields are present per record; concrete evidence URLs were reached. The 20 daily-helper tests passed in one invocation. These checks do not establish recall. SlidesWeaver v1 remains a pending date anomaly.
