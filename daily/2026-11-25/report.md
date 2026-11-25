# Agentic Graphics daily report
Date: 2026-11-25 | Timezone: America/Chicago | As of: 2026-11-25T20:01:38+00:00
browser-based same-day search; documented source coverage
Taxonomy: survey-taxonomy-snapshot-2026-10-15 | Snapshot: bundled_snapshot_not_live_refreshed

## Coverage limits
- Today means November 25, 2026 00:00–14:01:38 America/Chicago; retrieval after cutoff does not extend event eligibility.
- No qualifying same-day Agentic Graphics paper was verified in the browsed source set. Indexing lag, uninspected work and inaccessible sources limit this statement.
- One bounded pass reached 10 search batches and 24 attempted primary-page opens before the approximate six-minute allowance; no padding of elapsed time.
- All nine query families and five source families were attempted with broad and dated searches. Source and query coverage remain partial.
- Seven arXiv category pages were reached; returned excerpts and selected keyword matches were inspected, not all listed papers.
- HF date URL could not open; root Nov 25 heading and search fallback to the dated page were reached. HF curation and announcement days are not submission dates.
- OpenReview direct search was inaccessible; restricted searches returned older papers and noisy venue results. SIGGRAPH Asia technical-paper overview reached; ACM and CVF restricted searches did not yield a verified same-day event.
- Six arXiv candidates and one repository signal received fresh dispositions. Five arXiv full texts were selectively inspected. ShaderAgent remains unresolved without publisher date/history verification.
- November 18–24 is the separate seven-day catch-up lane. Previous pending status alone does not count as a previously verified event.
- Direct main daily histories and supplied website history are used only for identity/event deduplication; previous-run archives were not recursively consulted as current evidence.
- No revision-content comparison or empirical reproduction. Unclear cells preserve missing evidence; offline evaluation is distinct from an in-loop verifier.
- Frozen October 15 snapshot not live refreshed. Tools labels remain provisional; the source memory wording caveat remains.
- Journal family associations describe the batch intent, not a claim that every result belongs to every family.

No qualifying same-day Agentic Graphics paper was verified in the browsed source set.
Coverage is limited to the sources and queries below; unpublished or unindexed papers may be missing.

## Execution and event comparison
Window: 2026-11-25T00:00:00-06:00 through 2026-11-25T14:01:38-06:00. Same-day new: 0; updates: 0. Retrieval: 10 batches / 31 queries / 24 attempted opens in 118.847 seconds.
The helper groups verified older events under late_discovery; the table separates new-to-us catch-up from previously reported events.

| Paper | Discovery status | Verified Chicago events |
|---|---|---|
| Lyris: Layout-Guided Long Video Generation with Persistent 3D Memory | new_to_us_catch_up | v1 first_submission 2026-11-23T12:59:46-06:00 (not_seen_in_supplied_history); v2 revision 2026-11-24T12:46:34-06:00 (not_seen_in_supplied_history) |
| 3DCodeFactory: Scaling Training Data for 3D Code Agents | new_to_us_catch_up | v1 first_submission 2026-11-21T06:58:42-06:00 (not_seen_in_supplied_history) |
| PartAgent: Agentic 3D Part Segmentation via Expert Integration and Closed-Loop Refinement | new_to_us_catch_up | v1 first_submission 2026-11-24T07:07:46-06:00 (not_seen_in_supplied_history) |
| CodeHOI: Code with Agents for Physically Plausible 4D Hand-Object Interaction | new_to_us_catch_up | v1 first_submission 2026-11-23T23:25:36-06:00 (not_seen_in_supplied_history) |
| Plan4D: Generative Plannable 4D Worlds | new_to_us_catch_up | v1 first_submission 2026-11-19T11:59:02-06:00 (not_seen_in_supplied_history) |
| Rethinking Video Agents: When and Why Video Harnesses Work | excluded | v1 first_submission 2026-11-23T21:43:32-06:00 (not_seen_in_supplied_history) |
| ShaderAgent: Self-Evolving Agentic Procedural Material Generation | unresolved |  |

## already_reported (0)

## same_day_new (0)

## same_day_updates (0)

## late_discovery (5)

### [Lyris: Layout-Guided Long Video Generation with Persistent 3D Memory](https://arxiv.org/abs/2611.31239)
core | Medium | new_relative_to_snapshot
Application: Static / Scene, Dynamic / Animation and temporal scene; operations: Generation, Editing
A VLM authors scene boxes; geometric checks revise them, while reconstructed video chunks update shared scene memory.
Scope: A VLM authors scene boxes; geometric checks revise them, while reconstructed video chunks update shared scene memory.
Limits: Selected v1 method read; v2 history verified without a revision-content comparison. Video-model tuning is distinct from planner adaptation.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Modeling, Animation | Plans scenes and generates walkthroughs. ([source](https://arxiv.org/html/2611.31239v1), Section 3, lines 103–107) |
| input_form | Image, Language | Input views and optional descriptions. ([source](https://arxiv.org/html/2611.31239v1), Section 3, line 103) |
| output | Structured Specification, Rendered Media | Labeled boxes guide generated video. ([source](https://arxiv.org/html/2611.31239v1), Section 3, line 103) |
| model_type | VLM | Vision-language model plans layouts. ([source](https://arxiv.org/html/2611.31239v1), Section 3, line 103) |
| model_training | Off-the-Shelf | Planner queried without fine-tuning. ([source](https://arxiv.org/html/2611.31239v1), Appendix B.1, line 502) |
| planning | PO-2 | Fixed chunk pipeline; model proposes boxes. ([source](https://arxiv.org/html/2611.31239v1), Section 3; Appendix B.1) |
| workflow | Sequential | Each completed chunk informs the next. ([source](https://arxiv.org/html/2611.31239v1), Section 3.2, lines 118–123) |
| update_strategy | Local Patch, Candidate Selection | Selects proposals and repairs flagged boxes. ([source](https://arxiv.org/html/2611.31239v1), Appendix B.1, line 513) |
| verifier | Programmatic | Six geometric checks verify proposals. ([source](https://arxiv.org/html/2611.31239v1), Appendix B.1, Table 11) |
| feedback_assessment | Binary, Diagnosis | Checks flag violations for repair. ([source](https://arxiv.org/html/2611.31239v1), Appendix B.1, lines 504–513) |
| feedback_observation | Visual, Structural Scene State | Planner receives rendered memory and boxes. ([source](https://arxiv.org/html/2611.31239v1), Appendix B.1, line 503) |
| memory_time | Short-Term Memory | Scene memory persists across video chunks. ([source](https://arxiv.org/html/2611.31239v1), Section 3.2) |
| memory_reach | Global Memory | Planner and generator consume scene memory. ([source](https://arxiv.org/html/2611.31239v1), Figure 2; Section 3.2) |
| action_type | Structured Specification | Planner emits labeled metric boxes. ([source](https://arxiv.org/html/2611.31239v1), Appendix B.1, lines 491–502) |
| graphics_software | Unclear |  |
| tools | Static Validator, Perception models | Geometric checks and chunk reconstruction. ([source](https://arxiv.org/html/2611.31239v1), Appendix B.1; Section 3.2) |
| resources | Examples & Trajectories | Retrieves two annotated layout examples. ([source](https://arxiv.org/html/2611.31239v1), Appendix B.1, line 503) |
| representation | Geometry, Pixels | Point clouds, boxes and video frames. ([source](https://arxiv.org/html/2611.31239v1), Section 3.2) |

next_action: "Review full method and survey suitability before corpus inclusion."

Events: [{"type": "first_submission", "value": "2026-11-23T18:59:46+00:00", "precision": "timestamp", "timezone": "UTC", "raw_source_value": "Mon, 23 Nov 2026 18:59:46 UTC", "raw_source_timezone": "UTC", "local_value": "2026-11-23T12:59:46-06:00", "primary_url": "https://arxiv.org/abs/2611.31239", "authority": "primary", "version": "v1", "evidence": "arXiv submission history reports v1 at the preserved UTC timestamp.", "locator": "Submission history, v1", "raw_evidence_archive": "retrieval/06.json", "prior_event_status": "not_seen_in_supplied_history"}, {"type": "revision", "value": "2026-11-24T18:46:34+00:00", "precision": "timestamp", "timezone": "UTC", "raw_source_value": "Tue, 24 Nov 2026 18:46:34 UTC", "raw_source_timezone": "UTC", "local_value": "2026-11-24T12:46:34-06:00", "primary_url": "https://arxiv.org/abs/2611.31239", "authority": "primary", "version": "v2", "evidence": "arXiv submission history reports v2 at the preserved UTC timestamp.", "locator": "Submission history, v2", "raw_evidence_archive": "retrieval/06.json", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: []

### [3DCodeFactory: Scaling Training Data for 3D Code Agents](https://arxiv.org/abs/2611.28783)
core | Medium | new_relative_to_snapshot
Application: Static / Object, Static / Scene, Datasets and Benchmarks; operations: Generation, Reconstruction
Synthesizes 3D tasks and multi-turn coding trajectories with rendered self-inspection, then filters artifacts for training.
Scope: Synthesizes 3D tasks and multi-turn coding trajectories with rendered self-inspection, then filters artifacts for training.
Limits: Post-rollout rubric filtering is not coded as an in-loop verifier. Student SFT and data-collection agents are distinct; selected passages only.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Modeling | Agents write 3D artifacts. ([source](https://arxiv.org/html/2611.28783v1), Section 3.1, line 109) |
| input_form | Language, Image | Text-derived tasks use reference images. ([source](https://arxiv.org/html/2611.28783v1), Section 3.3, line 127) |
| output | Program, Graphics Artifact | Code rollouts produce 3D artifacts. ([source](https://arxiv.org/html/2611.28783v1), Section 3.1, line 109) |
| model_type | VLM | Student uses multimodal interleaved training. ([source](https://arxiv.org/html/2611.28783v1), Appendix B, line 263) |
| model_training | Supervised Fine-Tuning | Full-parameter multimodal SFT trains students. ([source](https://arxiv.org/html/2611.28783v1), Appendix B, line 263) |
| planning | Unclear |  |
| workflow | Sequential | Multi-turn write, render, inspect cycle. ([source](https://arxiv.org/html/2611.28783v1), Section 3.1, line 109) |
| update_strategy | Unclear |  |
| verifier | Self | Agent performs render-based self-inspection. ([source](https://arxiv.org/html/2611.28783v1), Section 3.4, Figure 4) |
| feedback_assessment | Unclear |  |
| feedback_observation | Visual, Runtime, Structural Scene State | Renders, errors and scene queries. ([source](https://arxiv.org/html/2611.28783v1), Appendix B.1, line 254) |
| memory_time | Short-Term Memory | Interaction trajectory spans task turns. ([source](https://arxiv.org/html/2611.28783v1), Section 3.1, line 109) |
| memory_reach | Unclear |  |
| action_type | Code/Script, Tool/Function Call | Python execution and rendering tools. ([source](https://arxiv.org/html/2611.28783v1), Appendix B.1, line 254) |
| graphics_software | Agent-Adapted | Blender-MCP exposes agent tools. ([source](https://arxiv.org/html/2611.28783v1), Appendix B.1, line 254) |
| tools | Execution Utilities, Graphics Operations | Script execution and multi-view rendering. ([source](https://arxiv.org/html/2611.28783v1), Appendix B.1, line 254) |
| resources | Unclear |  |
| representation | Code, Geometry, Pixels | Scripts, 3D scenes and screenshots. ([source](https://arxiv.org/html/2611.28783v1), Appendix B.1, line 254) |

next_action: "Review full method and survey suitability before corpus inclusion."

Events: [{"type": "first_submission", "value": "2026-11-21T12:58:42+00:00", "precision": "timestamp", "timezone": "UTC", "raw_source_value": "Sat, 21 Nov 2026 12:58:42 UTC", "raw_source_timezone": "UTC", "local_value": "2026-11-21T06:58:42-06:00", "primary_url": "https://arxiv.org/abs/2611.28783", "authority": "primary", "version": "v1", "evidence": "arXiv submission history reports v1 at the preserved UTC timestamp.", "locator": "Submission history, v1", "raw_evidence_archive": "retrieval/06.json", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: []

### [PartAgent: Agentic 3D Part Segmentation via Expert Integration and Closed-Loop Refinement](https://arxiv.org/abs/2611.32554)
enabling_or_adjacent | Medium | new_relative_to_snapshot
Application: Static / Object; operations: Editing
An observation-driven VLM refines object part partitions and verifies proposed changes before updating the segmentation.
Scope: An observation-driven VLM refines object part partitions and verifies proposed changes before updating the segmentation.
Limits: Segmentation enables editable object structure; it does not establish asset creation. Verifier identity and software interface remain unclear in inspected passages.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Modeling | Refines semantic partitions of object meshes. ([source](https://arxiv.org/html/2611.32554v1), Introduction, lines 68–80) |
| input_form | 3D Representation | Maps evidence onto the original mesh. ([source](https://arxiv.org/html/2611.32554v1), Introduction, line 69) |
| output | Graphics Artifact | Produces refined object segmentation. ([source](https://arxiv.org/html/2611.32554v1), Conclusion, line 274) |
| model_type | VLM | VLM chooses targeted refinement actions. ([source](https://arxiv.org/html/2611.32554v1), Section 3.3, line 167) |
| model_training | Off-the-Shelf | Training-free; frozen expert models. ([source](https://arxiv.org/html/2611.32554v1), Introduction, lines 75–80) |
| planning | Unclear |  |
| workflow | Sequential | Action outcomes guide subsequent decisions. ([source](https://arxiv.org/html/2611.32554v1), Section 3.3, line 167) |
| update_strategy | Local Patch, Candidate Selection | Repairs evidence, regroups or reselects partitions. ([source](https://arxiv.org/html/2611.32554v1), Section 3.3, line 167) |
| verifier | Unclear |  |
| feedback_assessment | Unclear |  |
| feedback_observation | Visual, Structural Scene State | Observes partitions and original renders. ([source](https://arxiv.org/html/2611.32554v1), Figure 4; Section 3.3, line 201) |
| memory_time | Short-Term Memory | Updated state guides the next inspection. ([source](https://arxiv.org/html/2611.32554v1), Figure 4, line 100) |
| memory_reach | Unclear |  |
| action_type | Unclear |  |
| graphics_software | Unclear |  |
| tools | Perception models | Integrates frozen 2D and 3D experts. ([source](https://arxiv.org/html/2611.32554v1), Introduction, lines 75–80) |
| resources | Unclear |  |
| representation | Geometry, Pixels | Mesh regions and multiview image evidence. ([source](https://arxiv.org/html/2611.32554v1), Introduction, line 69) |

next_action: "Review full method and survey suitability before corpus inclusion."

Events: [{"type": "first_submission", "value": "2026-11-24T13:07:46+00:00", "precision": "timestamp", "timezone": "UTC", "raw_source_value": "Tue, 24 Nov 2026 13:07:46 UTC", "raw_source_timezone": "UTC", "local_value": "2026-11-24T07:07:46-06:00", "primary_url": "https://arxiv.org/abs/2611.32554", "authority": "primary", "version": "v1", "evidence": "arXiv submission history reports v1 at the preserved UTC timestamp.", "locator": "Submission history, v1", "raw_evidence_archive": "retrieval/09.json", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: ["Part segmentation is mapped provisionally to Modeling/Editing; it is enabling structure processing rather than demonstrated asset authoring."]

### [CodeHOI: Code with Agents for Physically Plausible 4D Hand-Object Interaction](https://arxiv.org/abs/2611.31976)
core | Medium | new_relative_to_snapshot
Application: Dynamic / Articulated assets, Dynamic / Animation and temporal scene, Dynamic / Physical simulation and effects, Datasets and Benchmarks; operations: Generation, Reconstruction
Object and interaction agents write physics-grounded hand-object programs; a checker and critic return violations for revision.
Scope: Object and interaction agents write physics-grounded hand-object programs; a checker and critic return violations for revision.
Limits: Selected method evidence only. Benchmark success metrics remain distinct from the in-loop checker. No memory persistence or software readiness inferred.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Modeling, Animation, Simulation | Builds objects and simulates hand interactions. ([source](https://arxiv.org/html/2611.31976v1), Section 3, line 120) |
| input_form | Unclear |  |
| output | Program, Graphics Artifact | Procedural programs produce articulated scenes. ([source](https://arxiv.org/html/2611.31976v1), Section 3.1, lines 127–130) |
| model_type | VLM | Critic inspects input overlays and renders. ([source](https://arxiv.org/html/2611.31976v1), Implementation, line 402) |
| model_training | Off-the-Shelf | Uses off-the-shelf frontier models. ([source](https://arxiv.org/html/2611.31976v1), Abstract, line 70) |
| planning | PO-2 | Fixed stages; agent plans hand contacts. ([source](https://arxiv.org/html/2611.31976v1), Section 3, line 120) |
| workflow | Sequential | Object stage precedes interaction stage. ([source](https://arxiv.org/html/2611.31976v1), Section 3, line 120) |
| update_strategy | Unclear |  |
| verifier | Programmatic, Critic | Deterministic checker and critic assess results. ([source](https://arxiv.org/html/2611.31976v1), Section 3.3, line 145) |
| feedback_assessment | Binary, Diagnosis | Accepts or returns violation review. ([source](https://arxiv.org/html/2611.31976v1), Figure 2; Section 3.3) |
| feedback_observation | Visual, Structural Scene State | Inspects renders and measured violations. ([source](https://arxiv.org/html/2611.31976v1), Section 3, line 121; Section 3.3) |
| memory_time | Unclear |  |
| memory_reach | Unclear |  |
| action_type | Code/Script | Agents write procedural modeling programs. ([source](https://arxiv.org/html/2611.31976v1), Section 3.1, line 127) |
| graphics_software | Unclear |  |
| tools | Solver Validator, Static Validator, Perception models | Physics solvers, checker, depth and masks. ([source](https://arxiv.org/html/2611.31976v1), Abstract; Section 3.3; Implementation line 402) |
| resources | Unclear |  |
| representation | Code, Geometry, Dynamic State, Pixels | Programs, meshes, simulations and renders. ([source](https://arxiv.org/html/2611.31976v1), Sections 3–3.3) |

next_action: "Review full method and survey suitability before corpus inclusion."

Events: [{"type": "first_submission", "value": "2026-11-24T05:25:36+00:00", "precision": "timestamp", "timezone": "UTC", "raw_source_value": "Tue, 24 Nov 2026 05:25:36 UTC", "raw_source_timezone": "UTC", "local_value": "2026-11-23T23:25:36-06:00", "primary_url": "https://arxiv.org/abs/2611.31976", "authority": "primary", "version": "v1", "evidence": "arXiv submission history reports v1 at the preserved UTC timestamp.", "locator": "Submission history, v1", "raw_evidence_archive": "retrieval/10.json", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: []

### [Plan4D: Generative Plannable 4D Worlds](https://arxiv.org/abs/2611.26516)
enabling_or_adjacent | Medium | new_relative_to_snapshot
Application: Dynamic / Animation and temporal scene; operations: Generation
A feed-forward model predicts RGB and dense 4D geometry from scene context and actions; it is a possible agent substrate.
Scope: A feed-forward model predicts RGB and dense 4D geometry from scene context and actions; it is a possible agent substrate.
Limits: No inference-time agentic feedback loop established. Training-time geometry critic is not an in-loop verifier.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Unclear |  |
| input_form | Language, Image | Observed scene and text-specified actions. ([source](https://arxiv.org/html/2611.26516v1), Introduction, line 82) |
| output | Rendered Media, Graphics Artifact | Outputs RGB and dense 4D geometry. ([source](https://arxiv.org/html/2611.26516v1), Introduction, lines 82–98) |
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
| representation | Pixels, Geometry, Dynamic State | RGB, depth, points and scene flow. ([source](https://arxiv.org/html/2611.26516v1), Conclusion, line 269) |

next_action: "Review full method and survey suitability before corpus inclusion."

Events: [{"type": "first_submission", "value": "2026-11-19T17:59:02+00:00", "precision": "timestamp", "timezone": "UTC", "raw_source_value": "Thu, 19 Nov 2026 17:59:02 UTC", "raw_source_timezone": "UTC", "local_value": "2026-11-19T11:59:02-06:00", "primary_url": "https://arxiv.org/abs/2611.26516", "authority": "primary", "version": "v1", "evidence": "arXiv submission history reports v1 at the preserved UTC timestamp.", "locator": "Submission history, v1", "raw_evidence_archive": "retrieval/07.json", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: ["Feed-forward world-model substrate; no decision-making model or inference-time verifier established."]

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
Application: Static / Object; operations: Generation
Potential procedural-material authoring system.
Scope: Official repository supports a plausible graphics-authoring system, but no publisher date or paper text was verified; retain as unresolved signal.
Limits: Repository-only reading; paper mechanism and publication event require fresh primary verification.

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

next_action: "Open publisher paper and history; do not infer release date from repository activity."

Events: []
Taxonomy deltas: []

## excluded (1)

### [Rethinking Video Agents: When and Why Video Harnesses Work](https://arxiv.org/abs/2611.31883)
excluded | High | new_relative_to_snapshot
Application: Cross-category; operations: Other
Studies adaptive observations for video understanding, rather than graphics authoring or world auditing.
Scope: Studies adaptive observations for video understanding, rather than graphics authoring or world auditing.
Limits: Abstract-level scope exclusion; no full-method taxonomy asserted.

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

Events: [{"type": "first_submission", "value": "2026-11-24T03:43:32+00:00", "precision": "timestamp", "timezone": "UTC", "raw_source_value": "Tue, 24 Nov 2026 03:43:32 UTC", "raw_source_timezone": "UTC", "local_value": "2026-11-23T21:43:32-06:00", "primary_url": "https://arxiv.org/abs/2611.31883", "authority": "primary", "version": "v1", "evidence": "arXiv submission history reports v1 at the preserved UTC timestamp.", "locator": "Submission history, v1", "raw_evidence_archive": "retrieval/08.json", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: []

## Application index
| Application | Papers |
|---|---|
| 2D Graphics | None verified in this run |
| Static / Object | [3DCodeFactory: Scaling Training Data for 3D Code Agents](https://arxiv.org/abs/2611.28783) [late_discovery]; [PartAgent: Agentic 3D Part Segmentation via Expert Integration and Closed-Loop Refinement](https://arxiv.org/abs/2611.32554) [late_discovery]; [ShaderAgent: Self-Evolving Agentic Procedural Material Generation](https://github.com/VAST-AI-Research/ShaderAgent) [unresolved] |
| Static / CAD | None verified in this run |
| Static / Scene | [Lyris: Layout-Guided Long Video Generation with Persistent 3D Memory](https://arxiv.org/abs/2611.31239) [late_discovery]; [3DCodeFactory: Scaling Training Data for 3D Code Agents](https://arxiv.org/abs/2611.28783) [late_discovery] |
| Dynamic / Articulated assets | [CodeHOI: Code with Agents for Physically Plausible 4D Hand-Object Interaction](https://arxiv.org/abs/2611.31976) [late_discovery] |
| Dynamic / Animation and temporal scene | [Lyris: Layout-Guided Long Video Generation with Persistent 3D Memory](https://arxiv.org/abs/2611.31239) [late_discovery]; [CodeHOI: Code with Agents for Physically Plausible 4D Hand-Object Interaction](https://arxiv.org/abs/2611.31976) [late_discovery]; [Plan4D: Generative Plannable 4D Worlds](https://arxiv.org/abs/2611.26516) [late_discovery] |
| Dynamic / Physical simulation and effects | [CodeHOI: Code with Agents for Physically Plausible 4D Hand-Object Interaction](https://arxiv.org/abs/2611.31976) [late_discovery] |
| Datasets and Benchmarks | [3DCodeFactory: Scaling Training Data for 3D Code Agents](https://arxiv.org/abs/2611.28783) [late_discovery]; [CodeHOI: Code with Agents for Physically Plausible 4D Hand-Object Interaction](https://arxiv.org/abs/2611.31976) [late_discovery] |
| Cross-category | [NeoWorld-Pro: Programming Interactive Scenes from Monocular Images for Embodied Simulation](https://arxiv.org/abs/2608.24212) [unresolved]; [PhotoGuider: Composition-Aware Cropping and 360° View Framing with Explainable Photographic Assessments](https://arxiv.org/abs/2611.02897) [unresolved]; [SceneAgent: An Agentic Pipeline from 3D and 4D Captures to Simulation Environments](https://arxiv.org/abs/2610.34745) [unresolved]; [Agentic AI for Scientific Visualization: Tool-Calling Pipelines for Automated Chart and Diagram Generation in Research Writing](https://www.scitepress.org/PublishedPapers/2026/152298/) [unresolved]; [FLASH: A "Generate Once, Synthesize Many" Framework for Synthetic Anomaly Generation in Industrial Anomaly Detection](https://arxiv.org/abs/2609.37314) [unresolved]; [Agent-Guided Immersive World Generation with Alpha-Textured Proxies](https://immersegen.github.io/) [unresolved]; [HiLSVA: Design and Evaluation of a Human-in-the-Loop Agentic System for Scientific Visualization](https://arxiv.org/abs/2606.26614) [unresolved]; [Exploring LLM Agent Designs and Interaction Modalities for Scientific Visualization](https://arxiv.org/abs/2604.27996) [unresolved]; [DramaAgent: Agentic Storytelling Video Generation](https://aclanthology.org/2026.aacl-long.163/) [unresolved] |

## Source ledger

| Source | Status | Limits |
|---|---|---|
| arxiv | partial | Seven category pages reached; selected listings, six histories and five method pages inspected. |
| hugging_face | partial | Dated URL open inaccessible; root Nov 25 and dated-page search fallback reached. Curation dates do not verify events. |
| openreview | partial | Direct search inaccessible; restricted queries reached older paper/profile and noisy venue results; no same-day paper verified. |
| official_venues | partial | SIGGRAPH Asia overview reached; ACM/CVF restricted searches attempted, no paper-level proceedings sweep. |
| project_author_lab | partial | ShaderAgent repository reached; PartAgent project open inaccessible despite search evidence. Project searches reached further leads. |

## Exact retrieval ledger

Times below are actual post-return recording times; exact per-page retrieval times are not exposed. Full requests, returned evidence and call-start times are in the linked journals.

| Journal | Recorded at (UTC) | Operation | Executed query / URL / find |
|---|---|---|---|
| [01](retrieval/01.json) | 2026-11-25T20:02:18.587Z | search_query | agent SVG diagram poster slide visual feedback November 2026 |
| [01](retrieval/01.json) | 2026-11-25T20:02:18.587Z | search_query | agent procedural 3D modeling material ShaderAgent November 2026 |
| [01](retrieval/01.json) | 2026-11-25T20:02:18.587Z | search_query | agent CAD geometry editing "2026-11-25" |
| [01](retrieval/01.json) | 2026-11-25T20:02:18.587Z | open | https://arxiv.org/list/cs.GR/new |
| [01](retrieval/01.json) | 2026-11-25T20:02:18.587Z | open | https://arxiv.org/list/cs.CV/recent |
| [01](retrieval/01.json) | 2026-11-25T20:02:18.587Z | open | https://huggingface.co/papers/date/2026-11-25 |
| [02](retrieval/02.json) | 2026-11-25T20:02:31.576Z | search_query | agent 3D scene generation reconstruction November 2026 arxiv |
| [02](retrieval/02.json) | 2026-11-25T20:02:31.576Z | search_query | agent rig articulated asset animation November 2026 |
| [02](retrieval/02.json) | 2026-11-25T20:02:31.576Z | search_query | "Plan4D" "ReWeave" |
| [02](retrieval/02.json) | 2026-11-25T20:02:31.576Z | open | https://arxiv.org/list/cs.RO/new |
| [02](retrieval/02.json) | 2026-11-25T20:02:31.576Z | open | https://huggingface.co/papers |
| [02](retrieval/02.json) | 2026-11-25T20:02:31.576Z | open | https://openreview.net/search?term=graphics%20agent |
| [02](retrieval/02.json) | 2026-11-25T20:02:31.576Z | find | turn0view0 [find: Title:] |
| [02](retrieval/02.json) | 2026-11-25T20:02:31.576Z | find | turn0view1 [find: Agent] |
| [03](retrieval/03.json) | 2026-11-25T20:02:44.740Z | search_query | site:arxiv.org agent physical simulation particle effects November 2026 |
| [03](retrieval/03.json) | 2026-11-25T20:02:44.740Z | search_query | site:arxiv.org agent graphics benchmark harness feedback "Nov" "2026" |
| [03](retrieval/03.json) | 2026-11-25T20:02:44.740Z | search_query | site:openreview.net graphics agent 2026 memory planning |
| [03](retrieval/03.json) | 2026-11-25T20:02:44.740Z | open | https://arxiv.org/list/cs.AI/new |
| [03](retrieval/03.json) | 2026-11-25T20:02:44.740Z | open | https://asia.siggraph.org/2026/program/technical-papers/ |
| [03](retrieval/03.json) | 2026-11-25T20:02:44.740Z | open | https://github.com/VAST-AI-Research/ShaderAgent |
| [03](retrieval/03.json) | 2026-11-25T20:02:44.740Z | find | turn1view1 [find: Nov 25] |
| [03](retrieval/03.json) | 2026-11-25T20:02:44.740Z | find | turn0view0 [find: Agent] |
| [03](retrieval/03.json) | 2026-11-25T20:02:44.740Z | find | turn1view1 [find: Plan4D] |
| [04](retrieval/04.json) | 2026-11-25T20:02:54.645Z | search_query | "Plan4D: Generative Plannable 4D Worlds" |
| [04](retrieval/04.json) | 2026-11-25T20:02:54.645Z | search_query | "Lyris" "Layout-Guided" |
| [04](retrieval/04.json) | 2026-11-25T20:02:54.645Z | search_query | site:arxiv.org "agent" "Nov 24, 2026" graphics |
| [04](retrieval/04.json) | 2026-11-25T20:02:54.645Z | search_query | site:openaccess.thecvf.com 2026 agent graphics generation |
| [04](retrieval/04.json) | 2026-11-25T20:02:54.645Z | open | https://arxiv.org/list/cs.HC/new |
| [04](retrieval/04.json) | 2026-11-25T20:02:54.645Z | open | https://arxiv.org/list/cs.MM/new |
| [04](retrieval/04.json) | 2026-11-25T20:02:54.645Z | open | https://arxiv.org/list/eess.IV/new |
| [04](retrieval/04.json) | 2026-11-25T20:02:54.645Z | find | turn2view2 [find: arxiv] |
| [04](retrieval/04.json) | 2026-11-25T20:02:54.645Z | find | turn1view1 [find: 3D] |
| [04](retrieval/04.json) | 2026-11-25T20:02:54.645Z | find | turn2view0 [find: graphics] |
| [05](retrieval/05.json) | 2026-11-25T20:03:10.364Z | search_query | "PartAgent" "3D Part Segmentation" |
| [05](retrieval/05.json) | 2026-11-25T20:03:10.364Z | search_query | "3DCodeFactory" agent |
| [05](retrieval/05.json) | 2026-11-25T20:03:10.364Z | search_query | "ShaderAgent" paper SIGGRAPH 2026 |
| [05](retrieval/05.json) | 2026-11-25T20:03:10.364Z | open | https://arxiv.org/abs/2611.31239 |
| [05](retrieval/05.json) | 2026-11-25T20:03:10.364Z | open | https://arxiv.org/html/2611.31239v1 |
| [05](retrieval/05.json) | 2026-11-25T20:03:10.364Z | open | https://arxiv.org/abs/2611.28783 |
| [05](retrieval/05.json) | 2026-11-25T20:03:10.364Z | find | turn3view0 [find: Title:] |
| [05](retrieval/05.json) | 2026-11-25T20:03:10.364Z | find | turn3view1 [find: Title:] |
| [05](retrieval/05.json) | 2026-11-25T20:03:10.364Z | find | turn2view2 [find: Designer] |
| [06](retrieval/06.json) | 2026-11-25T20:03:21.279Z | search_query | site:arxiv.org "PartAgent" |
| [06](retrieval/06.json) | 2026-11-25T20:03:21.279Z | search_query | site:arxiv.org agent graphics CAD SVG after:2026-11-24 before:2026-11-26 |
| [06](retrieval/06.json) | 2026-11-25T20:03:21.279Z | search_query | site:openreview.net "graphics" "Nov 2026" |
| [06](retrieval/06.json) | 2026-11-25T20:03:21.279Z | open | https://arxiv.org/html/2611.28783v1 |
| [06](retrieval/06.json) | 2026-11-25T20:03:21.279Z | open | https://arxiv.org/abs/2611.26516 |
| [06](retrieval/06.json) | 2026-11-25T20:03:21.279Z | open | https://arxiv.org/html/2611.26516v1 |
| [06](retrieval/06.json) | 2026-11-25T20:03:21.279Z | find | turn4view0 [find: Submission history] |
| [06](retrieval/06.json) | 2026-11-25T20:03:21.279Z | find | turn4view2 [find: Submission history] |
| [06](retrieval/06.json) | 2026-11-25T20:03:21.279Z | find | turn4view1 [find: planner] |
| [06](retrieval/06.json) | 2026-11-25T20:03:21.279Z | find | turn4view1 [find: memory] |
| [07](retrieval/07.json) | 2026-11-25T20:03:31.446Z | search_query | "PartAgent" arxiv segmentation 2026 |
| [07](retrieval/07.json) | 2026-11-25T20:03:31.446Z | search_query | agent animation simulation "2026-11-25" |
| [07](retrieval/07.json) | 2026-11-25T20:03:31.446Z | search_query | ManimAgent PosterMELD VIGA agent recent November 2026 |
| [07](retrieval/07.json) | 2026-11-25T20:03:31.446Z | open | https://yangcaoai.github.io/PartAgent_ProjectPage/ |
| [07](retrieval/07.json) | 2026-11-25T20:03:31.446Z | open | https://arxiv.org/abs/2611.31883 |
| [07](retrieval/07.json) | 2026-11-25T20:03:31.446Z | find | turn5view0 [find: rollout] |
| [07](retrieval/07.json) | 2026-11-25T20:03:31.446Z | find | turn5view1 [find: Submission history] |
| [07](retrieval/07.json) | 2026-11-25T20:03:31.446Z | find | turn5view2 [find: feed-forward] |
| [07](retrieval/07.json) | 2026-11-25T20:03:31.446Z | find | turn0view0 [find: PreferenceScene] |
| [08](retrieval/08.json) | 2026-11-25T20:03:41.481Z | search_query | "CodeHOI" agent |
| [08](retrieval/08.json) | 2026-11-25T20:03:41.481Z | search_query | site:dl.acm.org "ShaderAgent" |
| [08](retrieval/08.json) | 2026-11-25T20:03:41.481Z | search_query | site:arxiv.org "agent" "25 Nov 2026" CAD graphics |
| [08](retrieval/08.json) | 2026-11-25T20:03:41.481Z | open | https://arxiv.org/abs/2611.32554 |
| [08](retrieval/08.json) | 2026-11-25T20:03:41.481Z | open | https://arxiv.org/html/2611.32554v1 |
| [08](retrieval/08.json) | 2026-11-25T20:03:41.481Z | find | turn5view0 [find: feedback] |
| [08](retrieval/08.json) | 2026-11-25T20:03:41.481Z | find | turn6view1 [find: Abstract] |
| [08](retrieval/08.json) | 2026-11-25T20:03:41.481Z | find | turn6view1 [find: Submission history] |
| [08](retrieval/08.json) | 2026-11-25T20:03:41.481Z | find | turn2view2 [find: Citation] |
| [09](retrieval/09.json) | 2026-11-25T20:03:53.581Z | search_query | site:huggingface.co/papers/date/2026-11-25 graphics agent |
| [09](retrieval/09.json) | 2026-11-25T20:03:53.581Z | search_query | site:dl.acm.org agent graphics "November 2026" |
| [09](retrieval/09.json) | 2026-11-25T20:03:53.581Z | search_query | site:arxiv.org agent CAD constraint solver November 2026 |
| [09](retrieval/09.json) | 2026-11-25T20:03:53.581Z | open | https://arxiv.org/abs/2611.31976 |
| [09](retrieval/09.json) | 2026-11-25T20:03:53.581Z | open | https://arxiv.org/html/2611.31976v1 |
| [09](retrieval/09.json) | 2026-11-25T20:03:53.581Z | find | turn7view0 [find: Submission history] |
| [09](retrieval/09.json) | 2026-11-25T20:03:53.581Z | find | turn7view1 [find: refinement] |
| [09](retrieval/09.json) | 2026-11-25T20:03:53.581Z | find | turn5view0 [find: 3.2] |
| [09](retrieval/09.json) | 2026-11-25T20:03:53.581Z | find | turn4view0 [find: Authors:] |
| [09](retrieval/09.json) | 2026-11-25T20:03:53.581Z | find | turn4view2 [find: Authors:] |
| [09](retrieval/09.json) | 2026-11-25T20:03:53.581Z | find | turn7view0 [find: Authors:] |
| [09](retrieval/09.json) | 2026-11-25T20:03:53.581Z | find | turn5view1 [find: Authors:] |
| [10](retrieval/10.json) | 2026-11-25T20:04:04.106Z | search_query | "MAGPIE: Agentic Multi-Reference Image Generation" |
| [10](retrieval/10.json) | 2026-11-25T20:04:04.106Z | search_query | "AdProducer: Towards Agentic Advertising Video Generation" |
| [10](retrieval/10.json) | 2026-11-25T20:04:04.106Z | search_query | agent CAD SVG scene simulation "November 25, 2026" |
| [10](retrieval/10.json) | 2026-11-25T20:04:04.106Z | find | turn8view0 [find: Submission history] |
| [10](retrieval/10.json) | 2026-11-25T20:04:04.106Z | find | turn8view0 [find: Authors:] |
| [10](retrieval/10.json) | 2026-11-25T20:04:04.106Z | find | turn8view1 [find: Evaluator Agent] |
| [10](retrieval/10.json) | 2026-11-25T20:04:04.106Z | find | turn7view1 [find: Verification] |
| [10](retrieval/10.json) | 2026-11-25T20:04:04.106Z | find | turn7view1 [find: state] |
| [10](retrieval/10.json) | 2026-11-25T20:04:04.106Z | find | turn5view0 [find: 3.4 Artifact] |
| [10](retrieval/10.json) | 2026-11-25T20:04:04.106Z | find | turn3view2 [find: Title:] |
| [10](retrieval/10.json) | 2026-11-25T20:04:04.106Z | find | turn1view0 [find: CodeHOI] |
| [11](retrieval/11.json) | 2026-11-25T20:04:16.111Z | find | turn7view1 [find: Agent state] |
| [11](retrieval/11.json) | 2026-11-25T20:04:16.111Z | find | turn7view1 [find: Action space] |
| [11](retrieval/11.json) | 2026-11-25T20:04:16.111Z | find | turn7view1 [find: Partition verification] |
| [11](retrieval/11.json) | 2026-11-25T20:04:16.111Z | find | turn7view1 [find: training-free] |
| [11](retrieval/11.json) | 2026-11-25T20:04:16.111Z | find | turn8view1 [find: Deterministic checker] |
| [11](retrieval/11.json) | 2026-11-25T20:04:16.111Z | find | turn8view1 [find: Off-the-shelf] |
| [11](retrieval/11.json) | 2026-11-25T20:04:16.111Z | find | turn8view1 [find: 3.1 Object] |
| [11](retrieval/11.json) | 2026-11-25T20:04:16.111Z | find | turn8view1 [find: memory] |
| [11](retrieval/11.json) | 2026-11-25T20:04:16.111Z | find | turn5view0 [find: Trajectory] |
| [11](retrieval/11.json) | 2026-11-25T20:04:16.111Z | find | turn4view1 [find: 3.1 Layout] |

## Query-family coverage

- 2d: partial; journals 01, 04, 05, 06, 07, 10.
- object: partial; journals 01, 03, 05, 06, 07, 08, 09, 10, 11.
- cad: partial; journals 01, 06, 08, 09, 10.
- scene: partial; journals 02, 04, 07, 10, 11.
- articulation: partial; journals 02, 08, 09, 10, 11.
- animation: partial; journals 02, 04, 05, 06, 07, 08, 10, 11.
- simulation: partial; journals 03, 07, 08, 09, 10, 11.
- benchmark: partial; journals 03, 04, 07, 09.
- harness: partial; journals 03, 05, 06, 07, 08, 09, 10, 11.

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
- PreferenceScene: Personalized Indoor Scene Synthesis from Feedback: Primary category abstract reached; canonical history and full method deferred at open cap.
- MAGPIE: Agentic Multi-Reference Image Generation via Executable Scene Construction: HF and search identity lead; primary history and mechanism not opened.
- AdProducer: Towards Agentic Advertising Video Generation: HF and project search lead; primary history and full method not opened.
- PhyCoVE: Benchmarking Physical Counterfactual Video Editing across Diverse Material Dynamics: HF listing lead; agentic scope and primary date unverified.
- Where is the Interface for the AI Harness?: HC listing lead; transferable graphics scope and canonical history not checked.
- Residual Guidance for Real-Time Interactive Video Generation: MM listing lead; primary history and agentic scope not checked.
