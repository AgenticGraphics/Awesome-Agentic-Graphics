# Agentic Graphics daily report
Date: 2026-11-24 | Timezone: America/Chicago | As of: 2026-11-24T20:05:08+00:00
browser-based same-day search; documented source coverage
Taxonomy: survey-taxonomy-snapshot-2026-10-15 | Snapshot: bundled_snapshot_not_live_refreshed

## Coverage limits
- Today means November 24, 2026 00:00–14:05:08 America/Chicago. Later retrieval times do not extend the frozen as-of cutoff.
- No qualifying same-day event was verified; indexing lag, unpublished work, and uninspected sources prevent a field-wide absence claim.
- The 10 search-batch and 24 attempted page-open caps were reached before the approximate six-minute retrieval allowance. Elapsed retrieval is measured from journals, not padded.
- All nine query families and five source families were attempted. Broad and date-filtered queries are discovery aids, not date evidence.
- arXiv cs.GR new, cs.CV recent, cs.AI/cs.RO/cs.HC/cs.MM/eess.IV new pages were reached. Only returned excerpts and selected keyword matches were inspected; these are not exhaustive category or title screens.
- Hugging Face date URL failed to open; its root page displayed Nov 24 and the date page also appeared in search results. Curation dates do not establish paper events.
- OpenReview search URL was inaccessible; site-restricted searches returned older PDFs. CVPR2026 index returned 403. SIGGRAPH Asia workshop and search results were reached, without a paper-level proceedings sweep.
- Six plausible candidates received fresh screening: five retained relevant/scope-dependent records and one exclusion. Other research leads remain queued. Full texts were inspected selectively, not read exhaustively.
- November 17–23 is a separate catch-up lane. WorldAct was rechecked outside that lane to resolve a prior verification lead. ChatAtom and WorldAct were previously reported, not new discoveries.
- Main daily reports and the supplied website history are compared non-recursively; archived run copies are not current evidence. Historical classifications alone do not verify carried leads.
- No revision-content comparison or empirical reproduction was performed. Unclear cells reflect insufficient inspected evidence; no adaptation or verifier is inferred from model names.
- The bundled October 15 snapshot was not live refreshed. Tools labels remain provisional, and the source memory definition remains internally inconsistent.
- Queries and finds are grouped by invocation for family coverage. A batch association does not mean every returned result belongs to each associated family.

No qualifying same-day Agentic Graphics paper was verified in the browsed source set.
Coverage is limited to the sources and queries below; unpublished or unindexed papers may be missing.

## Execution and event comparison
Window: 2026-11-24T00:00:00-06:00 through 2026-11-24T14:05:08-06:00. Same-day new: 0; updates: 0. Retrieval: 10 batches / 30 queries / 24 attempted opens in 103 seconds.
The helper groups verified older events under late_discovery; the table separates new-to-us catch-up from previously reported events.

| Paper | Discovery status | Verified Chicago events |
|---|---|---|
| 3AGameFactory-Motion: Agentic Rigging and Reliable Complex Motion Generation for Diverse 3D Assets | new_to_us_catch_up | v1 first_submission 2026-11-22T22:16:51-06:00 (not_seen_in_supplied_history) |
| From Point Clouds to Engineering Models: Benchmarking Agentic 3D Reconstruction in the Built Environment | new_to_us_catch_up | v1 first_submission 2026-11-20T10:26:09-06:00 (not_seen_in_supplied_history) |
| AI agents can redesign engineering parts with more than a thousand CAD parameters and nonlinear simulations | new_to_us_catch_up | v1 first_submission 2026-11-19T06:21:21-06:00 (not_seen_in_supplied_history); v2 revision 2026-11-22T10:46:09-06:00 (not_seen_in_supplied_history) |
| ChatAtom: A Multi-Agent LLM System for Molecular Dynamics Simulation and Visualization | previously_reported_event_reverified | v1 first_submission 2026-11-19T14:18:15-06:00 (already_seen) |
| WorldAct: Activating Monolithic 3D Worlds into Interactive-Ready Object-Centric Scenes | previously_reported_event_reverified | v1 first_submission 2026-05-15T05:56:23-05:00 (already_seen); v2 revision 2026-11-05T01:15:15-06:00 (already_seen) |
| Learning the Next Best Move with Visual Diffusion Models | excluded | v1 first_submission 2026-11-23T09:46:19-06:00 (not_seen_in_supplied_history) |

## already_reported (0)

## same_day_new (0)

## same_day_updates (0)

## late_discovery (5)

### [3AGameFactory-Motion: Agentic Rigging and Reliable Complex Motion Generation for Diverse 3D Assets](https://arxiv.org/abs/2611.30013)
core | High | new_relative_to_snapshot
Application: Dynamic / Articulated assets, Dynamic / Animation and temporal scene, Datasets and Benchmarks; operations: Generation
Agent-authored skeleton and motion programs drive deterministic rigging and kinematics; DivDynBench evaluates diverse asset morphologies.
Scope: Agent-authored skeleton and motion programs drive deterministic rigging and kinematics; DivDynBench evaluates diverse asset morphologies.
Limits: Selected method passages read; empirical results not reproduced. Evaluation scoring is separate from executor feedback. Repository connection to this exact paper was not confirmed in the opened README.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Modeling, Animation | Builds rigs and motion. ([source](https://arxiv.org/html/2611.30013v1), Section 4) |
| input_form | Language, Image, 3D Representation | Instructions, calibrated views, assets. ([source](https://arxiv.org/html/2611.30013v1), Sections 4.1–4.2) |
| output | Program, Graphics Artifact | Programs yield rigs and animations. ([source](https://arxiv.org/html/2611.30013v1), Section 4, Figure 4) |
| model_type | VLM | Agent annotates parts across views. ([source](https://arxiv.org/html/2611.30013v1), Sections 4.1, 5.2) |
| model_training | Unclear |  |
| planning | PO-2 | Agent sets phases within rig/motion stages. ([source](https://arxiv.org/html/2611.30013v1), Section 4.2) |
| workflow | Sequential | Rigging precedes motion; supplied rigs bypass it. ([source](https://arxiv.org/html/2611.30013v1), Section 4, Figure 4) |
| update_strategy | Local Patch | Executor adjusts motion parameters. ([source](https://arxiv.org/html/2611.30013v1), Section 4.2, Execution and validation) |
| verifier | Programmatic | Executor checks deformations and residuals. ([source](https://arxiv.org/html/2611.30013v1), Sections 4.1–4.2) |
| feedback_assessment | Unclear |  |
| feedback_observation | Structural Scene State | Mesh feedback guides corrections. ([source](https://arxiv.org/html/2611.30013v1), Section 4.2) |
| memory_time | Unclear |  |
| memory_reach | Unclear |  |
| action_type | Code/Script, Tool/Function Call | Agent invokes parameterized Python executor. ([source](https://arxiv.org/html/2611.30013v1), Section 4.2) |
| graphics_software | Unclear |  |
| tools | Graphics Operations, Solver Validator | Rigging and constrained kinematic solving. ([source](https://arxiv.org/html/2611.30013v1), Sections 4.1–4.2) |
| resources | Unclear |  |
| representation | Code, Geometry, Dynamic State | Programs, meshes, evolving joint poses. ([source](https://arxiv.org/html/2611.30013v1), Section 4) |

next_action: "Review full method and survey suitability before corpus inclusion."

Events: [{"type": "first_submission", "value": "2026-11-23T04:16:51+00:00", "precision": "timestamp", "timezone": "UTC", "raw_source_value": "Mon, 23 Nov 2026 04:16:51 UTC", "raw_source_timezone": "UTC", "local_value": "2026-11-22T22:16:51-06:00", "primary_url": "https://arxiv.org/abs/2611.30013", "authority": "primary", "version": "v1", "evidence": "arXiv submission history reports v1 at the preserved UTC timestamp.", "locator": "Submission history, v1", "raw_evidence_archive": "retrieval/06.json", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: []

### [From Point Clouds to Engineering Models: Benchmarking Agentic 3D Reconstruction in the Built Environment](https://arxiv.org/abs/2611.28197)
core | High | new_relative_to_snapshot
Application: Static / CAD, Static / Scene, Datasets and Benchmarks; operations: Reconstruction
Coding agents reconstruct semantic CAD/BIM components from scans using execution, geometry checks and rendered feedback.
Scope: Coding agents reconstruct semantic CAD/BIM components from scans using execution, geometry checks and rendered feedback.
Limits: Selected Sections 3–5 read. Held-out labels and engineering checker are offline evaluation, not in-loop verifiers. No empirical replication.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Modeling | Reconstructs CAD/BIM components. ([source](https://arxiv.org/html/2611.28197v1), Sections 3.1, 4) |
| input_form | 3D Representation, Language | Scans, class vocabulary and task prompt. ([source](https://arxiv.org/html/2611.28197v1), Sections 3.1, 4.1) |
| output | Program, Graphics Artifact | Exports program, native model and IFC. ([source](https://arxiv.org/html/2611.28197v1), Section 3.1) |
| model_type | VLM | Coding agents inspect rendered views. ([source](https://arxiv.org/html/2611.28197v1), Sections 4.1–4.2) |
| model_training | Unclear |  |
| planning | PO-3 | Agent freely interleaves steps and delegation. ([source](https://arxiv.org/html/2611.28197v1), Section 4.2) |
| workflow | Sequential, Parallel | Single-agent loop or asynchronous team. ([source](https://arxiv.org/html/2611.28197v1), Section 4.2) |
| update_strategy | Local Patch | Revises modeling code after measurements. ([source](https://arxiv.org/html/2611.28197v1), Section 4.2) |
| verifier | Programmatic | Automatic checks and validate assertions. ([source](https://arxiv.org/html/2611.28197v1), Section 4.1) |
| feedback_assessment | Diagnosis | Errors and invalid geometry are returned. ([source](https://arxiv.org/html/2611.28197v1), Section 4.1) |
| feedback_observation | Visual, Structural Scene State, Runtime | Views, geometry checks and execution errors. ([source](https://arxiv.org/html/2611.28197v1), Section 4.1) |
| memory_time | Unclear |  |
| memory_reach | Unclear |  |
| action_type | Code/Script | Python measurements and modeling programs. ([source](https://arxiv.org/html/2611.28197v1), Sections 4.1–4.2) |
| graphics_software | Agent-Adapted | Adapters connect harness and Rhino backend. ([source](https://arxiv.org/html/2611.28197v1), Section 4.1) |
| tools | Graphics Operations, Static Validator | Model execution and geometric predicates. ([source](https://arxiv.org/html/2611.28197v1), Section 4.1) |
| resources | Documentation & Rules | Shared API/workflow manual. ([source](https://arxiv.org/html/2611.28197v1), Section 4.1) |
| representation | Code, Geometry | Programs maintain scan-aligned components. ([source](https://arxiv.org/html/2611.28197v1), Sections 3.1, 4.1) |

next_action: "Review full method and survey suitability before corpus inclusion."

Events: [{"type": "first_submission", "value": "2026-11-20T16:26:09+00:00", "precision": "timestamp", "timezone": "UTC", "raw_source_value": "Fri, 20 Nov 2026 16:26:09 UTC", "raw_source_timezone": "UTC", "local_value": "2026-11-20T10:26:09-06:00", "primary_url": "https://arxiv.org/abs/2611.28197", "authority": "primary", "version": "v1", "evidence": "arXiv submission history reports v1 at the preserved UTC timestamp.", "locator": "Submission history, v1", "raw_evidence_archive": "retrieval/07.json", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: []

### [AI agents can redesign engineering parts with more than a thousand CAD parameters and nonlinear simulations](https://arxiv.org/abs/2611.26003)
core | High | new_relative_to_snapshot
Application: Static / CAD; operations: Editing
An LLM changes CAD parameters, receives finite-element scores and feature-level results, and proposes further designs.
Scope: An LLM changes CAD parameters, receives finite-element scores and feature-level results, and proposes further designs.
Limits: Selected protocol passages read; revision differences not compared. Engineering optimization is in scope through CAD editing; this is not a clinical recommendation or independently validated design.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Modeling | Edits engineering geometry. ([source](https://arxiv.org/html/2611.26003v2), Section 3.2) |
| input_form | Language | Opening message specifies problem and constraints. ([source](https://arxiv.org/html/2611.26003v2), Section 3.1) |
| output | Structured Specification, Graphics Artifact | JSON changes compile into CAD solids. ([source](https://arxiv.org/html/2611.26003v2), Section 3.2) |
| model_type | LLM | LLM proposes design files. ([source](https://arxiv.org/html/2611.26003v2), Section 3, Figure 2) |
| model_training | Unclear |  |
| planning | PO-2 | Agent chooses candidates within fixed rounds. ([source](https://arxiv.org/html/2611.26003v2), Section 3.3) |
| workflow | Sequential, Parallel | Rounds; candidates can simulate concurrently. ([source](https://arxiv.org/html/2611.26003v2), Section 3.3) |
| update_strategy | Local Patch, Candidate Selection | Parameter changes; returns best design. ([source](https://arxiv.org/html/2611.26003v2), Sections 3.2–3.3) |
| verifier | Programmatic, Environment | Checks, simulation and scoring judge. ([source](https://arxiv.org/html/2611.26003v2), Sections 3.2–3.4) |
| feedback_assessment | Binary, Score, Diagnosis | Validity, objective and constraint margins. ([source](https://arxiv.org/html/2611.26003v2), Sections 3.1–3.4) |
| feedback_observation | Structural Scene State | Feature-indexed simulation results. ([source](https://arxiv.org/html/2611.26003v2), Section 3.1) |
| memory_time | Short-Term Memory | Retains session messages and results. ([source](https://arxiv.org/html/2611.26003v2), Section 3.1) |
| memory_reach | Unclear |  |
| action_type | Structured Specification, Tool/Function Call | Design JSON and check_design calls. ([source](https://arxiv.org/html/2611.26003v2), Section 3.2; Appendix B tools table) |
| graphics_software | Agent-Adapted | Pipeline builds, meshes and solves designs. ([source](https://arxiv.org/html/2611.26003v2), Section 3.4) |
| tools | Graphics Operations, Solver Validator, Static Validator | CAD builder, simulation and free checks. ([source](https://arxiv.org/html/2611.26003v2), Sections 3.2–3.4) |
| resources | Documentation & Rules | Parameter rules and readable design code. ([source](https://arxiv.org/html/2611.26003v2), Section 3.2) |
| representation | Geometry | Parameterized CAD solids. ([source](https://arxiv.org/html/2611.26003v2), Section 3.2) |

next_action: "Review full method and survey suitability before corpus inclusion."

Events: [{"type": "first_submission", "value": "2026-11-19T12:21:21+00:00", "precision": "timestamp", "timezone": "UTC", "raw_source_value": "Thu, 19 Nov 2026 12:21:21 UTC", "raw_source_timezone": "UTC", "local_value": "2026-11-19T06:21:21-06:00", "primary_url": "https://arxiv.org/abs/2611.26003", "authority": "primary", "version": "v1", "evidence": "arXiv submission history reports v1 at the preserved UTC timestamp.", "locator": "Submission history, v1", "raw_evidence_archive": "retrieval/08.json", "prior_event_status": "not_seen_in_supplied_history"}, {"type": "revision", "value": "2026-11-22T16:46:09+00:00", "precision": "timestamp", "timezone": "UTC", "raw_source_value": "Sun, 22 Nov 2026 16:46:09 UTC", "raw_source_timezone": "UTC", "local_value": "2026-11-22T10:46:09-06:00", "primary_url": "https://arxiv.org/abs/2611.26003", "authority": "primary", "version": "v2", "evidence": "arXiv submission history reports v2 at the preserved UTC timestamp.", "locator": "Submission history, v2", "raw_evidence_archive": "retrieval/08.json", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: []

### [ChatAtom: A Multi-Agent LLM System for Molecular Dynamics Simulation and Visualization](https://arxiv.org/abs/2611.26782)
scope_dependent | High | new_relative_to_snapshot
Application: 2D Graphics, Dynamic / Physical simulation and effects; operations: Generation
Agent-generated OVITO visualization and reviewed simulation scripts support optional scientific visualization scope; materials simulation is the main domain.
Scope: Agent-generated OVITO visualization and reviewed simulation scripts support optional scientific visualization scope; materials simulation is the main domain.
Limits: Selected architecture passages read. Persistent memory is supported, but disabled in the script-generation benchmark. Rendering for the user does not establish agent visual feedback.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Simulation, Visualization | Generates LAMMPS and OVITO workflows. ([source](https://arxiv.org/html/2611.26782v1), Sections 2.2–2.3) |
| input_form | Language | Natural-language requests become plans. ([source](https://arxiv.org/html/2611.26782v1), Section 2.1) |
| output | Program, Rendered Media | Scripts produce streamed trajectory frames. ([source](https://arxiv.org/html/2611.26782v1), Sections 2.2–2.3) |
| model_type | LLM | LLM orchestrator and script agents. ([source](https://arxiv.org/html/2611.26782v1), Abstract; Section 2) |
| model_training | Unclear |  |
| planning | PO-2 | Adaptive orchestrator; deterministic script stages. ([source](https://arxiv.org/html/2611.26782v1), Sections 2.1–2.3) |
| workflow | Sequential | LAMMPS then OVITO; bounded review loops. ([source](https://arxiv.org/html/2611.26782v1), Sections 2.1–2.3) |
| update_strategy | Regeneration | Rejected scripts rewritten with fixes. ([source](https://arxiv.org/html/2611.26782v1), Sections 2.2–2.3) |
| verifier | Critic, Programmatic, Human | Reviewers, code checks and user approval. ([source](https://arxiv.org/html/2611.26782v1), Sections 2.1–2.3) |
| feedback_assessment | Binary, Diagnosis | Review verdicts include errors and fixes. ([source](https://arxiv.org/html/2611.26782v1), Sections 2.2–2.3) |
| feedback_observation | Unclear |  |
| memory_time | Long-Term Memory | Earlier-run failures inform later scripts. ([source](https://arxiv.org/html/2611.26782v1), Sections 2.2–2.3) |
| memory_reach | Unclear |  |
| action_type | Code/Script, Tool/Function Call | Orchestrator calls script-generation tools. ([source](https://arxiv.org/html/2611.26782v1), Sections 2.1–2.3) |
| graphics_software | Agent-Adapted | Reviewed scripts feed OVITO rendering. ([source](https://arxiv.org/html/2611.26782v1), Section 2.3) |
| tools | Execution Utilities, Graphics Operations, Static Validator | Execution, OVITO operations and code checks. ([source](https://arxiv.org/html/2611.26782v1), Sections 2.3–2.4) |
| resources | Documentation & Rules | Curated scripting/modifier rules. ([source](https://arxiv.org/html/2611.26782v1), Sections 2.2–2.3) |
| representation | Code, Dynamic State, Pixels | Scripts, atomic trajectories and frames. ([source](https://arxiv.org/html/2611.26782v1), Sections 2.2–2.3) |

next_action: "Review full method and survey suitability before corpus inclusion."

Events: [{"type": "first_submission", "value": "2026-11-19T20:18:15+00:00", "precision": "timestamp", "timezone": "UTC", "raw_source_value": "Thu, 19 Nov 2026 20:18:15 UTC", "raw_source_timezone": "UTC", "local_value": "2026-11-19T14:18:15-06:00", "primary_url": "https://arxiv.org/abs/2611.26782", "authority": "primary", "version": "v1", "evidence": "arXiv submission history reports v1 at the preserved UTC timestamp.", "locator": "Submission history, v1", "raw_evidence_archive": "retrieval/10.json", "prior_event_status": "already_seen"}]
Taxonomy deltas: []

### [WorldAct: Activating Monolithic 3D Worlds into Interactive-Ready Object-Centric Scenes](https://arxiv.org/abs/2605.15843)
core | Medium | known_discussed_paper
Application: Static / Scene; operations: Reconstruction, Editing
A multimodal agent decomposes generated worlds into editable object meshes and restores scene background.
Scope: A multimodal agent decomposes generated worlds into editable object meshes and restores scene background.
Limits: Prior pending verification resolved at abstract and selected appendix level. Both events precede the seven-day lane; this is a known-paper recheck. Interactive readiness alone is not dynamic authoring.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Modeling | Decomposes and restores 3D scenes. ([source](https://arxiv.org/abs/2605.15843), Abstract) |
| input_form | 3D Representation, Image, Video | Worlds, rendered views or videos. ([source](https://arxiv.org/html/2605.15843v2), Abstract; Appendix B Algorithm 1) |
| output | Graphics Artifact | Editable meshes and restored background. ([source](https://arxiv.org/abs/2605.15843), Abstract) |
| model_type | VLM | Multimodal agent interprets scene observations. ([source](https://arxiv.org/abs/2605.15843), Abstract) |
| model_training | Unclear |  |
| planning | Unclear |  |
| workflow | Unclear |  |
| update_strategy | Unclear |  |
| verifier | Unclear |  |
| feedback_assessment | Unclear |  |
| feedback_observation | Unclear |  |
| memory_time | Short-Term Memory | Inventory tracks processing state within pipeline. ([source](https://arxiv.org/html/2605.15843v2), Appendix B.3) |
| memory_reach | Unclear |  |
| action_type | Unclear |  |
| graphics_software | Unclear |  |
| tools | Perception models | Text-guided segmentation supplies object masks. ([source](https://arxiv.org/html/2605.15843v2), Appendix B overview) |
| resources | Unclear |  |
| representation | Geometry, Pixels | Object meshes, masks and rendered views. ([source](https://arxiv.org/html/2605.15843v2), Abstract; Appendix B overview) |

next_action: "Review full method and survey suitability before corpus inclusion."

Events: [{"type": "first_submission", "value": "2026-05-15T10:56:23+00:00", "precision": "timestamp", "timezone": "UTC", "raw_source_value": "Fri, 15 May 2026 10:56:23 UTC", "raw_source_timezone": "UTC", "local_value": "2026-05-15T05:56:23-05:00", "primary_url": "https://arxiv.org/abs/2605.15843", "authority": "primary", "version": "v1", "evidence": "arXiv submission history reports v1 at the preserved UTC timestamp.", "locator": "Submission history, v1", "raw_evidence_archive": "retrieval/09.json", "prior_event_status": "already_seen"}, {"type": "revision", "value": "2026-11-05T07:15:15+00:00", "precision": "timestamp", "timezone": "UTC", "raw_source_value": "Thu, 5 Nov 2026 07:15:15 UTC", "raw_source_timezone": "UTC", "local_value": "2026-11-05T01:15:15-06:00", "primary_url": "https://arxiv.org/abs/2605.15843", "authority": "primary", "version": "v2", "evidence": "arXiv submission history reports v2 at the preserved UTC timestamp.", "locator": "Submission history, v2", "raw_evidence_archive": "retrieval/09.json", "prior_event_status": "already_seen"}]
Taxonomy deltas: []

## date_unresolved (0)

## unresolved (9)

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

## excluded (1)

### [Learning the Next Best Move with Visual Diffusion Models](https://arxiv.org/abs/2611.30879)
excluded | Medium | new_relative_to_snapshot
Application: Cross-category; operations: Other
E1_DOMAIN: inspected abstract evaluates visual action prediction in chess, pathfinding, Connect Four, Go and billiards; no graphics-authoring or geometric-content system contribution is established.
Scope: E1_DOMAIN: inspected abstract evaluates visual action prediction in chess, pathfinding, Connect Four, Go and billiards; no graphics-authoring or geometric-content system contribution is established.
Limits: Abstract-level exclusion from this graphics-authoring survey pass, not a claim of no broader agent relevance.

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

Events: [{"type": "first_submission", "value": "2026-11-23T15:46:19+00:00", "precision": "timestamp", "timezone": "UTC", "raw_source_value": "Mon, 23 Nov 2026 15:46:19 UTC", "raw_source_timezone": "UTC", "local_value": "2026-11-23T09:46:19-06:00", "primary_url": "https://arxiv.org/abs/2611.30879", "authority": "primary", "version": "v1", "evidence": "arXiv submission history reports v1 at the preserved UTC timestamp.", "locator": "Submission history, v1", "raw_evidence_archive": "retrieval/09.json", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: []

## Application index
| Application | Papers |
|---|---|
| 2D Graphics | [ChatAtom: A Multi-Agent LLM System for Molecular Dynamics Simulation and Visualization](https://arxiv.org/abs/2611.26782) [late_discovery] |
| Static / Object | None verified in this run |
| Static / CAD | [From Point Clouds to Engineering Models: Benchmarking Agentic 3D Reconstruction in the Built Environment](https://arxiv.org/abs/2611.28197) [late_discovery]; [AI agents can redesign engineering parts with more than a thousand CAD parameters and nonlinear simulations](https://arxiv.org/abs/2611.26003) [late_discovery] |
| Static / Scene | [From Point Clouds to Engineering Models: Benchmarking Agentic 3D Reconstruction in the Built Environment](https://arxiv.org/abs/2611.28197) [late_discovery]; [WorldAct: Activating Monolithic 3D Worlds into Interactive-Ready Object-Centric Scenes](https://arxiv.org/abs/2605.15843) [late_discovery] |
| Dynamic / Articulated assets | [3AGameFactory-Motion: Agentic Rigging and Reliable Complex Motion Generation for Diverse 3D Assets](https://arxiv.org/abs/2611.30013) [late_discovery] |
| Dynamic / Animation and temporal scene | [3AGameFactory-Motion: Agentic Rigging and Reliable Complex Motion Generation for Diverse 3D Assets](https://arxiv.org/abs/2611.30013) [late_discovery] |
| Dynamic / Physical simulation and effects | [ChatAtom: A Multi-Agent LLM System for Molecular Dynamics Simulation and Visualization](https://arxiv.org/abs/2611.26782) [late_discovery] |
| Datasets and Benchmarks | [3AGameFactory-Motion: Agentic Rigging and Reliable Complex Motion Generation for Diverse 3D Assets](https://arxiv.org/abs/2611.30013) [late_discovery]; [From Point Clouds to Engineering Models: Benchmarking Agentic 3D Reconstruction in the Built Environment](https://arxiv.org/abs/2611.28197) [late_discovery] |
| Cross-category | [NeoWorld-Pro: Programming Interactive Scenes from Monocular Images for Embodied Simulation](https://arxiv.org/abs/2608.24212) [unresolved]; [PhotoGuider: Composition-Aware Cropping and 360° View Framing with Explainable Photographic Assessments](https://arxiv.org/abs/2611.02897) [unresolved]; [SceneAgent: An Agentic Pipeline from 3D and 4D Captures to Simulation Environments](https://arxiv.org/abs/2610.34745) [unresolved]; [Agentic AI for Scientific Visualization: Tool-Calling Pipelines for Automated Chart and Diagram Generation in Research Writing](https://www.scitepress.org/PublishedPapers/2026/152298/) [unresolved]; [FLASH: A "Generate Once, Synthesize Many" Framework for Synthetic Anomaly Generation in Industrial Anomaly Detection](https://arxiv.org/abs/2609.37314) [unresolved]; [Agent-Guided Immersive World Generation with Alpha-Textured Proxies](https://immersegen.github.io/) [unresolved]; [HiLSVA: Design and Evaluation of a Human-in-the-Loop Agentic System for Scientific Visualization](https://arxiv.org/abs/2606.26614) [unresolved]; [Exploring LLM Agent Designs and Interaction Modalities for Scientific Visualization](https://arxiv.org/abs/2604.27996) [unresolved]; [DramaAgent: Agentic Storytelling Video Generation](https://aclanthology.org/2026.aacl-long.163/) [unresolved] |

## Source ledger

| Source | Status | Limits |
|---|---|---|
| arxiv | partial | Seven category pages reached, selected matches only; histories and selected full-text passages for six candidates. |
| hugging_face | partial | Date URL open blocked; root Nov 24 heading and date-page search fallback reached. |
| openreview | partial | Direct search URL blocked; restricted searches reached older PDF results without same-day primary verification. |
| official_venues | partial | Workshop page reached; CVPR index 403; venue search results do not establish paper-specific publication events. |
| project_author_lab | partial | GameFactory official repository reached; exact motion-paper linkage absent from inspected README. Other repository hits remain signals. |

## Exact retrieval ledger

Times below are actual post-return recording times; exact per-page retrieval times are not exposed. Full requests, returned evidence and call-start times are in the linked journals.

| Journal | Recorded at (UTC) | Operation | Executed query / URL / find |
|---|---|---|---|
| [01](retrieval/01.json) | 2026-11-24T20:05:49+00:00 | search_query | agent SVG diagram slide poster editable visual feedback November 2026 |
| [01](retrieval/01.json) | 2026-11-24T20:05:49+00:00 | search_query | agent 3D object procedural modeling Blender material after:2026-11-23 before:2026-11-25 |
| [01](retrieval/01.json) | 2026-11-24T20:05:49+00:00 | search_query | agent CAD generation repair visual feedback November 24 2026 |
| [01](retrieval/01.json) | 2026-11-24T20:05:49+00:00 | open | https://arxiv.org/list/cs.GR/new |
| [01](retrieval/01.json) | 2026-11-24T20:05:49+00:00 | open | https://arxiv.org/list/cs.CV/recent |
| [01](retrieval/01.json) | 2026-11-24T20:05:49+00:00 | open | https://huggingface.co/papers/date/2026-11-24 |
| [02](retrieval/02.json) | 2026-11-24T20:05:56+00:00 | search_query | site:arxiv.org "agent" "scene" "Nov" "2026" |
| [02](retrieval/02.json) | 2026-11-24T20:05:56+00:00 | search_query | agent articulated asset joint rig generation November 2026 |
| [02](retrieval/02.json) | 2026-11-24T20:05:56+00:00 | search_query | agent animation cutscene cinematography "2026" research |
| [02](retrieval/02.json) | 2026-11-24T20:05:56+00:00 | open | https://arxiv.org/list/cs.RO/new |
| [02](retrieval/02.json) | 2026-11-24T20:05:56+00:00 | open | https://openreview.net/search?term=graphics%20agent |
| [02](retrieval/02.json) | 2026-11-24T20:05:56+00:00 | open | https://huggingface.co/papers |
| [02](retrieval/02.json) | 2026-11-24T20:05:56+00:00 | find | turn0view0 [find: Title:] |
| [02](retrieval/02.json) | 2026-11-24T20:05:56+00:00 | find | turn0view1 [find: agent] |
| [03](retrieval/03.json) | 2026-11-24T20:06:05+00:00 | search_query | site:arxiv.org agent physical simulation particle effects November 2026 |
| [03](retrieval/03.json) | 2026-11-24T20:06:05+00:00 | search_query | site:arxiv.org agent graphics benchmark world auditing "2026" |
| [03](retrieval/03.json) | 2026-11-24T20:06:05+00:00 | search_query | graphics agent memory replanning tool interface feedback program synthesis "November" "2026" |
| [03](retrieval/03.json) | 2026-11-24T20:06:05+00:00 | open | https://arxiv.org/list/cs.AI/new |
| [03](retrieval/03.json) | 2026-11-24T20:06:05+00:00 | open | https://siga26.agentic-graphics.com/ |
| [03](retrieval/03.json) | 2026-11-24T20:06:05+00:00 | open | https://openaccess.thecvf.com/CVPR2026?day=all |
| [03](retrieval/03.json) | 2026-11-24T20:06:05+00:00 | find | turn0view0 [find: Agent] |
| [03](retrieval/03.json) | 2026-11-24T20:06:05+00:00 | find | turn1view2 [find: Nov 24] |
| [03](retrieval/03.json) | 2026-11-24T20:06:05+00:00 | find | turn1view2 [find: 3D] |
| [03](retrieval/03.json) | 2026-11-24T20:06:05+00:00 | find | turn1view0 [find: generation] |
| [04](retrieval/04.json) | 2026-11-24T20:06:13+00:00 | search_query | "3AGameFactory-Motion" |
| [04](retrieval/04.json) | 2026-11-24T20:06:13+00:00 | search_query | site:openreview.net "graphics" "agent" "2026" |
| [04](retrieval/04.json) | 2026-11-24T20:06:13+00:00 | search_query | site:arxiv.org "24 Nov 2026" "agent" graphics |
| [04](retrieval/04.json) | 2026-11-24T20:06:13+00:00 | open | https://arxiv.org/list/cs.HC/new |
| [04](retrieval/04.json) | 2026-11-24T20:06:13+00:00 | open | https://arxiv.org/list/cs.MM/new |
| [04](retrieval/04.json) | 2026-11-24T20:06:13+00:00 | find | turn2view0 [find: 3AGame] |
| [04](retrieval/04.json) | 2026-11-24T20:06:13+00:00 | find | turn2view0 [find: CAD] |
| [04](retrieval/04.json) | 2026-11-24T20:06:13+00:00 | find | turn2view0 [find: visualization] |
| [04](retrieval/04.json) | 2026-11-24T20:06:13+00:00 | find | turn0view0 [find: [1]] |
| [05](retrieval/05.json) | 2026-11-24T20:06:26+00:00 | search_query | "agents" "scans" "CAD/BIM" "2026" |
| [05](retrieval/05.json) | 2026-11-24T20:06:26+00:00 | search_query | site:asia.siggraph.org/2026 agent graphics papers November |
| [05](retrieval/05.json) | 2026-11-24T20:06:26+00:00 | search_query | "WorldAct" "November" "2026" |
| [05](retrieval/05.json) | 2026-11-24T20:06:26+00:00 | open | https://arxiv.org/abs/2611.30013 |
| [05](retrieval/05.json) | 2026-11-24T20:06:26+00:00 | open | https://arxiv.org/html/2611.30013v1 |
| [05](retrieval/05.json) | 2026-11-24T20:06:26+00:00 | open | https://arxiv.org/list/eess.IV/new |
| [05](retrieval/05.json) | 2026-11-24T20:06:26+00:00 | find | turn2view0 [find: shared framework] |
| [05](retrieval/05.json) | 2026-11-24T20:06:26+00:00 | find | turn3view0 [find: graphics] |
| [05](retrieval/05.json) | 2026-11-24T20:06:26+00:00 | find | turn3view1 [find: agent] |
| [06](retrieval/06.json) | 2026-11-24T20:06:36+00:00 | search_query | agent SVG diagram chart slide poster editable visual feedback |
| [06](retrieval/06.json) | 2026-11-24T20:06:36+00:00 | search_query | site:arxiv.org "2026-11-24" "CAD" |
| [06](retrieval/06.json) | 2026-11-24T20:06:36+00:00 | search_query | site:huggingface.co/papers/date/2026-11-24 graphics |
| [06](retrieval/06.json) | 2026-11-24T20:06:36+00:00 | open | https://arxiv.org/abs/2611.28197 |
| [06](retrieval/06.json) | 2026-11-24T20:06:36+00:00 | open | https://arxiv.org/html/2611.28197v1 |
| [06](retrieval/06.json) | 2026-11-24T20:06:36+00:00 | open | https://github.com/wangjazz/gamefactory-3a |
| [06](retrieval/06.json) | 2026-11-24T20:06:36+00:00 | find | turn4view0 [find: Submission history] |
| [06](retrieval/06.json) | 2026-11-24T20:06:36+00:00 | find | turn4view1 [find: 3 Agentic] |
| [06](retrieval/06.json) | 2026-11-24T20:06:36+00:00 | find | turn4view1 [find: feedback] |
| [06](retrieval/06.json) | 2026-11-24T20:06:36+00:00 | find | turn4view2 [find: agent] |
| [07](retrieval/07.json) | 2026-11-24T20:06:44+00:00 | search_query | agent physical simulation deformable world after:2026-11-23 before:2026-11-25 |
| [07](retrieval/07.json) | 2026-11-24T20:06:44+00:00 | search_query | agent animation articulated rig after:2026-11-23 before:2026-11-25 |
| [07](retrieval/07.json) | 2026-11-24T20:06:44+00:00 | search_query | "Articraft" OR "VIGA" "November" "2026" agent |
| [07](retrieval/07.json) | 2026-11-24T20:06:44+00:00 | open | https://arxiv.org/abs/2611.26003 |
| [07](retrieval/07.json) | 2026-11-24T20:06:44+00:00 | open | https://arxiv.org/html/2611.26003v2 |
| [07](retrieval/07.json) | 2026-11-24T20:06:44+00:00 | find | turn5view0 [find: Submission history] |
| [07](retrieval/07.json) | 2026-11-24T20:06:44+00:00 | find | turn5view1 [find: 3.] |
| [07](retrieval/07.json) | 2026-11-24T20:06:44+00:00 | find | turn5view1 [find: feedback] |
| [07](retrieval/07.json) | 2026-11-24T20:06:44+00:00 | find | turn4view1 [find: Agentic Motion Framework] |
| [07](retrieval/07.json) | 2026-11-24T20:06:44+00:00 | find | turn5view2 [find: 2611.30013] |
| [08](retrieval/08.json) | 2026-11-24T20:06:53+00:00 | search_query | site:arxiv.org "agent" "visualization" after:2026-11-17 before:2026-11-25 |
| [08](retrieval/08.json) | 2026-11-24T20:06:53+00:00 | search_query | site:openreview.net "CAD" "2026" "agent" |
| [08](retrieval/08.json) | 2026-11-24T20:06:53+00:00 | search_query | site:arxiv.org "agent" "world auditing" |
| [08](retrieval/08.json) | 2026-11-24T20:06:53+00:00 | open | https://arxiv.org/abs/2605.15843 |
| [08](retrieval/08.json) | 2026-11-24T20:06:53+00:00 | open | https://arxiv.org/abs/2611.30879 |
| [08](retrieval/08.json) | 2026-11-24T20:06:53+00:00 | find | turn6view0 [find: Submission history] |
| [08](retrieval/08.json) | 2026-11-24T20:06:53+00:00 | find | turn6view1 [find: 2.1] |
| [08](retrieval/08.json) | 2026-11-24T20:06:53+00:00 | find | turn6view1 [find: feedback] |
| [08](retrieval/08.json) | 2026-11-24T20:06:53+00:00 | find | turn4view1 [find: Execution and validation.] |
| [08](retrieval/08.json) | 2026-11-24T20:06:53+00:00 | find | turn4view1 [find: Skinning and validation.] |
| [08](retrieval/08.json) | 2026-11-24T20:06:53+00:00 | find | turn5view1 [find: Parallel asynchronous] |
| [09](retrieval/09.json) | 2026-11-24T20:07:02+00:00 | search_query | "ChatAtom" "simulation" "visualization" |
| [09](retrieval/09.json) | 2026-11-24T20:07:02+00:00 | search_query | "agent" "graphics" "24 Nov 2026" |
| [09](retrieval/09.json) | 2026-11-24T20:07:02+00:00 | search_query | site:arxiv.org "Blender" after:2026-11-17 before:2026-11-25 |
| [09](retrieval/09.json) | 2026-11-24T20:07:02+00:00 | open | https://arxiv.org/abs/2611.26782 |
| [09](retrieval/09.json) | 2026-11-24T20:07:02+00:00 | open | https://arxiv.org/html/2611.26782v1 |
| [09](retrieval/09.json) | 2026-11-24T20:07:02+00:00 | find | turn7view1 [find: Abstract] |
| [09](retrieval/09.json) | 2026-11-24T20:07:02+00:00 | find | turn7view1 [find: Submission history] |
| [09](retrieval/09.json) | 2026-11-24T20:07:02+00:00 | find | turn7view0 [find: Abstract] |
| [09](retrieval/09.json) | 2026-11-24T20:07:02+00:00 | find | turn7view0 [find: Submission history] |
| [09](retrieval/09.json) | 2026-11-24T20:07:02+00:00 | find | turn6view1 [find: ## 3] |
| [09](retrieval/09.json) | 2026-11-24T20:07:02+00:00 | find | turn6view1 [find: JSON] |
| [10](retrieval/10.json) | 2026-11-24T20:07:13+00:00 | search_query | site:arxiv.org "agent" "scene" after:2026-11-23 before:2026-11-25 |
| [10](retrieval/10.json) | 2026-11-24T20:07:13+00:00 | search_query | site:arxiv.org "graphics" "benchmark" after:2026-11-23 before:2026-11-25 |
| [10](retrieval/10.json) | 2026-11-24T20:07:13+00:00 | search_query | site:arxiv.org "Manim" OR "PosterMELD" after:2026-11-17 before:2026-11-25 |
| [10](retrieval/10.json) | 2026-11-24T20:07:13+00:00 | open | https://arxiv.org/html/2605.15843v2 |
| [10](retrieval/10.json) | 2026-11-24T20:07:13+00:00 | find | turn8view0 [find: Submission history] |
| [10](retrieval/10.json) | 2026-11-24T20:07:13+00:00 | find | turn8view1 [find: reviewer] |
| [10](retrieval/10.json) | 2026-11-24T20:07:13+00:00 | find | turn8view1 [find: memory] |
| [10](retrieval/10.json) | 2026-11-24T20:07:13+00:00 | find | turn7view1 [find: We evaluate] |
| [10](retrieval/10.json) | 2026-11-24T20:07:13+00:00 | find | turn6view1 [find: 3.1] |
| [10](retrieval/10.json) | 2026-11-24T20:07:13+00:00 | find | turn6view1 [find: fine-tun] |
| [11](retrieval/11.json) | 2026-11-24T20:07:31+00:00 | find | turn9view0 [find: Memory Module] |
| [11](retrieval/11.json) | 2026-11-24T20:07:31+00:00 | find | turn9view0 [find: 4.2.1] |
| [11](retrieval/11.json) | 2026-11-24T20:07:31+00:00 | find | turn9view0 [find: 4.3.2] |
| [11](retrieval/11.json) | 2026-11-24T20:07:31+00:00 | find | turn7view1 [find: demonstrate] |
| [11](retrieval/11.json) | 2026-11-24T20:07:31+00:00 | find | turn4view0 [find: Authors:] |
| [11](retrieval/11.json) | 2026-11-24T20:07:31+00:00 | find | turn5view0 [find: Authors:] |
| [11](retrieval/11.json) | 2026-11-24T20:07:31+00:00 | find | turn6view0 [find: Authors:] |
| [11](retrieval/11.json) | 2026-11-24T20:07:31+00:00 | find | turn8view0 [find: Authors:] |
| [11](retrieval/11.json) | 2026-11-24T20:07:31+00:00 | find | turn4view1 [find: Skeleton construction.] |

## Query-family coverage

- 2d: partial; journals 01, 04, 06, 08, 09, 10.
- object: partial; journals 01, 07, 08, 09, 11.
- cad: partial; journals 01, 04, 05, 06, 08.
- scene: partial; journals 02, 05, 08, 09, 10, 11.
- articulation: partial; journals 02, 04, 05, 06, 07, 11.
- animation: partial; journals 02, 05, 06, 07.
- simulation: partial; journals 03, 07, 09, 10.
- benchmark: partial; journals 03, 06, 08, 10.
- harness: partial; journals 03, 04, 07, 10, 11.

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
- ShaderAgent: Self-Evolving Agentic Procedural Material Generation: Repository mirror search lead; canonical research identity/date not opened.
- Plan4D: Generative Plannable 4D Worlds: HF lead; primary identity, scope and event pending.
- RUIBench: What Makes a Good Robot-Use Interface?: Robot interface lead; transferable graphics scope unverified.
- AutoPILOT: A Visual Agent Harness for Real-Time Gameplay: Gameplay harness lead; graphics-authoring relevance unverified.
- GameDojo: Benchmarking Real-Time Interactive Agents in Video Games: Game agent benchmark lead; scope and dates unverified.
- ReWeave: Emergent Physical Task Topologies for Embodied Harness Optimization and Cross-Task Meta-Distillation: HF listing only; primary scope and dates unverified.
- Lyris: Layout-Guided Long Video Generation with Persistent 3D Memory: HF listing only; agentic mechanism and dates unverified.
