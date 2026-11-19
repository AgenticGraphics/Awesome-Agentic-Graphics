# Agentic Graphics daily report
Date: 2026-11-13 | Timezone: America/Chicago | As of: 2026-11-19T00:11:04+00:00
browser-based same-day search; documented source coverage
Taxonomy: google-doc-taxonomy-v3-2026-10-15 | Snapshot: authorized_live_snapshot_reconciled_and_frozen

## Coverage limits
- Search indexes and public release pages may lag; field-wide completeness is not established.
- Catalog attention pool was fully abstract-read for 210 target_and_uncertain and 258 catch-up routed records, but 64 plausible leads remain ranked unread; 38 delivered graphics/title-hint records still lack provisional ranks.
- One PDF was read (PhysLoop v2) but retained only as unresolved because the checkpoint validator could not bind the downloaded revision to a source-verified timestamp; the raw PDF and failure are preserved.
- No claim of exhaustive discovery; source indexes, HF curation, venue search and metadata API limits remain.

## already_reported (0)

## same_day_new (5)

### [Vision-as-a-Tool: Visual Harness for Multimodal Agentic Coding](https://arxiv.org/abs/2611.17797v1)
core | High | new_relative_to_snapshot
Application: 2D Graphics, Static / Object, Dynamic / Animation and temporal scene; operations: Generation, Editing
Introduces Vision-as-a-Tool and VHarness, a general MCP-based visual utility interface that lets coding agents invoke transcribe, grep, inspect, align and diff during closed-loop visual artifact generation and refinement.
Scope: A coding agent autonomously invokes visual tools, executes code that creates SVG and Blender artifacts, renders them, and uses visual feedback to revise the artifact.
Limits: The experiments focus on static single-page, standalone vector, and individual-object 3D reconstruction tasks; the paper explicitly leaves interactive applications and temporal 3D scenes for future work, and the system substantially increases token/tool usage.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Modeling | The principal task is iterative visual coding for SVG and procedural 3D modeling, with HTML as an additional structured visual artifact. ([source](https://arxiv.org/pdf/2611.17797v1), pp. 1-4) |
| input_form | Image, 3D Representation | Image-to-SVG takes raster target images; Image-to-3D takes four views of a 3D object. ([source](https://arxiv.org/pdf/2611.17797v1), p. 4) |
| output | Program, Graphics Artifact | The agent outputs SVG code, Blender Python code, and rendered artifacts/GLB meshes. ([source](https://arxiv.org/pdf/2611.17797v1), pp. 1, 4, 11) |
| model_type | Hybrid | The agent can be multimodal or text-only while external visual utilities are powered by an MLLM; the deployed system is therefore hybrid. ([source](https://arxiv.org/pdf/2611.17797v1), pp. 1-2, 5) |
| model_training | Off-the-Shelf | Experiments use named pretrained coding agents and Gemini-3.8-Flash as the utility model; no task-specific training of the agentic controller is reported. ([source](https://arxiv.org/pdf/2611.17797v1), pp. 1-2, 5) |
| planning | PO-3 | The agent autonomously chooses tools and iterations rather than following a fixed workflow. ([source](https://arxiv.org/pdf/2611.17797v1), pp. 2-3, 17-20) |
| workflow | Graph-Structured | Code generation, rendering, visual inspection, diagnosis and revision form a loop with alternative callable actions. ([source](https://arxiv.org/pdf/2611.17797v1), pp. 1-3, 6-8) |
| update_strategy | Local Patch, Replanning | The agent makes targeted code updates after diff/inspect feedback and can replan by choosing subsequent utilities and revisions. ([source](https://arxiv.org/pdf/2611.17797v1), pp. 3, 6-8, 17-18) |
| verifier | Critic, Programmatic | External MLLM utilities inspect and compare rendered artifacts; align returns Boolean assertions and diff diagnoses discrepancies. ([source](https://arxiv.org/pdf/2611.17797v1), pp. 3, 6, 15-16) |
| feedback_assessment | Binary, Diagnosis | align returns a Boolean match judgment while diff returns ranked discrepancy diagnoses. ([source](https://arxiv.org/pdf/2611.17797v1), pp. 3, 15-16) |
| feedback_observation | Visual, Structural Scene State | Utilities observe rendered pixels and localized visual/structural discrepancies. ([source](https://arxiv.org/pdf/2611.17797v1), pp. 3, 15-16) |
| memory_time | Working Memory | The formulation conditions later code updates on prior thoughts, code updates, rendered images and utility feedback within one execution. ([source](https://arxiv.org/pdf/2611.17797v1), pp. 2-3) |
| memory_reach | Local Memory | The coding agent uses feedback from its own current artifact trajectory. ([source](https://arxiv.org/pdf/2611.17797v1), pp. 2-3) |
| action_type | Code/Script, Tool/Function Call | The agent writes/edits HTML, SVG and Blender Python and invokes MCP visual tools. ([source](https://arxiv.org/pdf/2611.17797v1), pp. 2-3, 11, 15-20) |
| graphics_software | Agent-Adapted | VHarness adds an MCP adapter exposing graphics perception and verification utilities to existing coding agents and renderers. ([source](https://arxiv.org/pdf/2611.17797v1), pp. 3-5, 11, 18) |
| tools | Graphics Operations, Perception models, Static Validator | Five callable visual utilities perform structure extraction, localization, inspection, assertion checking and image comparison. ([source](https://arxiv.org/pdf/2611.17797v1), pp. 2-3, 11, 15-16) |
| resources | Assets, Documentation & Rules | Image-to-HTML uses provided visual assets; task skills and exact tool prompts supply rules/documentation. ([source](https://arxiv.org/pdf/2611.17797v1), pp. 4, 11, 17-18) |
| representation | Code, Geometry, Layouts, Pixels | The workflow uses HTML/SVG/Blender code, 3D geometry/GLB, layouts and rendered pixels. ([source](https://arxiv.org/pdf/2611.17797v1), pp. 1, 4, 11, 17-18) |

Events: [{"type": "first_submission", "value": "2026-11-13T06:23:19+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2611.17797v1", "authority": "primary", "version": "v1", "evidence": "Official arXiv metadata; target-local time 2026-11-13T00:23:19-06:00.", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: []

### [SceneAgent: A Multi-Agent Framework for Portable Game Scene Generation](https://arxiv.org/abs/2611.17821v1)
core | High | new_relative_to_snapshot
Application: Static / Scene, Dynamic / Animation and temporal scene; operations: Generation, Editing
Provides a portable multi-agent 3D scene-construction protocol separating canonical scene state, task-local reasoning, reusable experience and backend-specific realization.
Scope: Planner and Builder agents directly create and edit a canonical 3D scene state through construction tools, geometry checks and backend adapters.
Limits: Porting still requires backend adapters, compatible assets and capability wrappers; multi-agent coordination adds substantial runtime, human approval limits experience-update scalability, and rendered-view/geometry checks do not establish physical stability, navigability or gameplay success.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Modeling | The system constructs complete 3D game environments and scene layouts. ([source](https://arxiv.org/pdf/2611.17821v1), pp. 1-5) |
| input_form | Language, Image | The method accepts text prompts or reference images. ([source](https://arxiv.org/pdf/2611.17821v1), pp. 1-3) |
| output | Structured Specification, Graphics Artifact | It produces an executable game scene via canonical structured SceneContext and backend export payloads. ([source](https://arxiv.org/pdf/2611.17821v1), pp. 1-4, 16) |
| model_type | LLM | DeepSeek-V4-Flash is used for Orchestrator, Planner and Builder decisions; cross-model experiments use other LLMs. ([source](https://arxiv.org/pdf/2611.17821v1), pp. 5-7, 9) |
| model_training | Off-the-Shelf | The deployed construction agents use named language-model backbones; no task-specific controller fine-tuning is reported. ([source](https://arxiv.org/pdf/2611.17821v1), pp. 6-7) |
| planning | PO-2 | An Orchestrator and Planner create an ordered queue of semantic subtasks, while Builders execute them and refinement may revise the scene. ([source](https://arxiv.org/pdf/2611.17821v1), pp. 2-4, 12-13) |
| workflow | Graph-Structured | Subtasks, fresh Builder sessions, shared state queries, reports, validation and refinement have non-linear dependencies. ([source](https://arxiv.org/pdf/2611.17821v1), pp. 2-4) |
| update_strategy | Local Patch, Replanning, Rollback | Builders perform targeted editing and rollback; Orchestrator can revise the plan and invoke bounded refinement. ([source](https://arxiv.org/pdf/2611.17821v1), pp. 4, 12-13) |
| verifier | Programmatic, Human | Automatic geometry checks diagnose violations; a human quality gate approves or rejects experience updates. ([source](https://arxiv.org/pdf/2611.17821v1), pp. 4-5, 13-18) |
| feedback_assessment | Diagnosis, Binary | Geometry checks produce violation diagnoses; human review makes approve/reject decisions. ([source](https://arxiv.org/pdf/2611.17821v1), pp. 4, 13, 17) |
| feedback_observation | Structural Scene State, Visual | SceneContext exposes actor transforms, bounding boxes, occupancy, provenance and renderings. ([source](https://arxiv.org/pdf/2611.17821v1), pp. 3-5, 13) |
| memory_time | Short-Term Memory, Long-Term Memory | SceneContext persists evolving world state across Builder sessions and skill libraries persist approved experience across generations. ([source](https://arxiv.org/pdf/2611.17821v1), pp. 1-5) |
| memory_reach | Global Memory | SceneContext is shared across Builder sessions and Layout/Content skills are retrieved by future Orchestrator/Planner/Builder runs. ([source](https://arxiv.org/pdf/2611.17821v1), pp. 1-5) |
| action_type | Tool/Function Call, Structured Specification | Agents invoke construction tools and provide structured subtask specifications and reports. ([source](https://arxiv.org/pdf/2611.17821v1), pp. 3-4, 12-13) |
| graphics_software | Agent-Adapted | The agent-facing shared tool interface is adapted across backend engines through adapters and capability wrappers. ([source](https://arxiv.org/pdf/2611.17821v1), pp. 1-4, 16) |
| tools | Graphics Operations, Static Validator, Execution Utilities | Asset retrieval, placement, procedural geometry, scene queries, targeted editing, rollback and collision checks are callable workflow tools. ([source](https://arxiv.org/pdf/2611.17821v1), pp. 4, 12-13) |
| resources | Assets, Examples & Trajectories, Documentation & Rules | Backend asset catalogs, approved Layout/Content traces, construction guides and shared conventions are accessed by the agents. ([source](https://arxiv.org/pdf/2611.17821v1), pp. 1-5, 12) |
| representation | Geometry, Layouts, Code | Canonical geometry and layouts are stored as actor-centric SceneContext, with backend export code/payloads and reusable skills. ([source](https://arxiv.org/pdf/2611.17821v1), pp. 1-4, 16-18) |

Events: [{"type": "first_submission", "value": "2026-11-13T06:57:48+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2611.17821v1", "authority": "primary", "version": "v1", "evidence": "Official arXiv metadata; target-local time 2026-11-13T00:57:48-06:00.", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: []

### [RecurIR: Learning When and How to Revise Restoration Policies via Recursive Self-Improvement](https://arxiv.org/abs/2611.18006v1)
core | High | new_relative_to_snapshot
Application: 2D Graphics, Cross-category; operations: Editing, Auditing
Introduces a recursive self-improvement loop that discovers condition-dependent restoration rules, actively falsifies them with targeted degradation changes, and learns verified revisions to tool selection, order, strength and regions.
Scope: The restoration agent selects and revises image-processing actions that directly modify image artifacts, using visual/quality feedback and programmatic acceptance tests.
Limits: The framework relies on controllable degradation generation, reference-based training supervision and a fixed restoration-tool library; its quality gains and recursive updates are evaluated primarily through image-restoration benchmarks and may not establish general-purpose visual editing beyond restoration.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Modeling | The principal task is adaptive restoration of degraded images. ([source](https://arxiv.org/pdf/2611.18006v1), pp. 1-5) |
| input_form | Image, Language | The agent receives a degraded image and generic restoration instruction, while degradation state is estimated from image observations. ([source](https://arxiv.org/pdf/2611.18006v1), pp. 3, 12) |
| output | Graphics Artifact | The workflow outputs restored images and revised restoration plans. ([source](https://arxiv.org/pdf/2611.18006v1), pp. 3, 5, 6-8) |
| model_type | Hybrid | The system combines learned policy modules, a restoration planner and a library of specialized restoration networks/tools. ([source](https://arxiv.org/pdf/2611.18006v1), pp. 3-5, 12-13) |
| model_training | Supervised Fine-Tuning | PDM and CPRM are optimized with explicit classification/regression objectives; supplementary details describe agent training while restoration tools remain frozen. ([source](https://arxiv.org/pdf/2611.18006v1), pp. 4-5, 12-14) |
| planning | PO-2 | The agent selects tool sequences and parameters, then conditionally revises them based on degradation changes. ([source](https://arxiv.org/pdf/2611.18006v1), pp. 3-5, 12-13) |
| workflow | Sequential | Tool execution follows a selected restoration plan, with regional operations and subsequent revisions in an ordered pipeline. ([source](https://arxiv.org/pdf/2611.18006v1), pp. 3-5, 17) |
| update_strategy | Local Patch, Replanning, Candidate Selection | The controller edits tool selection/order/strength/regions, replans under changed conditions, and selects candidate updates through transfer-retention validation. ([source](https://arxiv.org/pdf/2611.18006v1), pp. 4-5, 8, 14-17) |
| verifier | Programmatic | Quality metrics, severe-artifact detection, transfer validation and retention validation accept or reject candidate policy updates. ([source](https://arxiv.org/pdf/2611.18006v1), pp. 5, 8, 12-14) |
| feedback_assessment | Score, Diagnosis, Binary | PSNR/SSIM and related quality scores provide graded feedback; falsification uses diagnosis of rule contradictions; update acceptance is binary under transfer-retention thresholds. ([source](https://arxiv.org/pdf/2611.18006v1), pp. 4-5, 8, 12-14) |
| feedback_observation | Visual, Structural Scene State | The system observes degraded/restored pixels, degradation severity and spatial distribution, and image-quality/artifact states. ([source](https://arxiv.org/pdf/2611.18006v1), pp. 3-5, 7-8, 17) |
| memory_time | Long-Term Memory | Verified hypotheses, applicability regions and revision evidence are retained and reused across recursive improvement rounds. ([source](https://arxiv.org/pdf/2611.18006v1), pp. 2-5, 13-14) |
| memory_reach | Local Memory | The accumulated hypotheses and revisions are used by the restoration policy and task-generation components; no cross-system shared memory is reported. ([source](https://arxiv.org/pdf/2611.18006v1), pp. 3-5, 13) |
| action_type | Tool/Function Call, Structured Specification | The agent invokes specialized restoration tools and emits structured plans containing tools, order, parameters and regions. ([source](https://arxiv.org/pdf/2611.18006v1), pp. 3-5, 12-13) |
| graphics_software | Agent-Adapted | The agent is built around a shared restoration-tool library and an agent-facing coordination layer rather than direct native GUI authoring. ([source](https://arxiv.org/pdf/2611.18006v1), pp. 2-3, 12-13) |
| tools | Graphics Operations, Perception models, Static Validator | The shared library contains deraining, desnowing, dehazing, deblurring, denoising and all-in-one restoration tools; perception and quality checks guide use. ([source](https://arxiv.org/pdf/2611.18006v1), pp. 12-13) |
| resources | Assets, Documentation & Rules | The agent uses a shared pretrained restoration-tool library, degradation rules and accumulated verified hypotheses/evidence. ([source](https://arxiv.org/pdf/2611.18006v1), pp. 3-5, 12-14) |
| representation | Pixels, Learned State | The workflow operates on image pixels and stores learned condition-dependent hypotheses and revision operators. ([source](https://arxiv.org/pdf/2611.18006v1), pp. 3-5, 13-17) |

Events: [{"type": "first_submission", "value": "2026-11-13T10:33:36+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2611.18006v1", "authority": "primary", "version": "v1", "evidence": "Official arXiv metadata; target-local time 2026-11-13T04:33:36-06:00.", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: []

### [TelePhysica: Agentic Reconstruction of Physically Interactive Scenes](https://arxiv.org/abs/2611.18078v1)
core | High | new_relative_to_snapshot
Application: Static / Scene, Dynamic / Physical simulation and effects, Dynamic / Animation and temporal scene; operations: Reconstruction, Generation, Editing
Introduces a closed-loop agentic reconstruction framework that converts a single photograph into a mechanically verified, executable multi-regime physical world and uses its simulated trajectories to ground video synthesis.
Scope: A vision-language coding agent directly creates and revises 3D graphics and physical scene state, with rendered and solver feedback controlling subsequent scene edits.
Limits: Material parameters are assigned from priors rather than identified online from multi-step visual interaction feedback; the method depends on a fixed solver/model stack and expensive rendering/physics/video components, and its verification is limited to the reported scene regimes and tests.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Simulation, Modeling | The principal purpose is reconstructing and simulating physically interactive 3D scenes, including rigid, articulated and deformable regimes. ([source](https://arxiv.org/pdf/2611.18078v1), pp. 1-5) |
| input_form | Image, Language | The agent receives a single photograph and a scene description. ([source](https://arxiv.org/pdf/2611.18078v1), pp. 1-4) |
| output | Program, Graphics Artifact, Rendered Media | The system emits executable scene programs/physical models, verified 3D worlds and rendered trajectory-conditioned videos. ([source](https://arxiv.org/pdf/2611.18078v1), pp. 1-6) |
| model_type | Hybrid | A vision-language coding agent controls code generation and verification while physics solvers and video diffusion provide downstream execution/rendering. ([source](https://arxiv.org/pdf/2611.18078v1), pp. 1-4, 6) |
| model_training | Off-the-Shelf | The paper uses pretrained coding/video models and reports no task-specific training of the reconstruction controller. ([source](https://arxiv.org/pdf/2611.18078v1), pp. 1-3, 6, 11-13) |
| planning | PO-3 | The agent iteratively proposes scripts, renders, critiques, repairs and re-verifies candidate worlds. ([source](https://arxiv.org/pdf/2611.18078v1), pp. 2, 4-5, 7-8) |
| workflow | Sequential | Stage-1 visual reconstruction precedes Stage-2 equilibrium verification, followed by physics rollout and video conditioning. ([source](https://arxiv.org/pdf/2611.18078v1), pp. 2-6) |
| update_strategy | Local Patch, Replanning, Candidate Selection | The agent locally repairs camera, geometry, poses, roles and colliders; it replans after structured failures and selects only verified scene submissions. ([source](https://arxiv.org/pdf/2611.18078v1), pp. 2, 4, 6-8, 14) |
| verifier | Critic, Programmatic, Environment | Silhouette/edge diagnostics, a deterministic physics solver and equilibrium gates judge candidate worlds; the environment exposes solver health and drift. ([source](https://arxiv.org/pdf/2611.18078v1), pp. 2, 4, 7-8, 14) |
| feedback_assessment | Diagnosis, Binary, Score | Mask/edge metrics provide scores, diagnostic overlays and contact/drift traces provide diagnoses, and threshold gates accept or reject candidates. ([source](https://arxiv.org/pdf/2611.18078v1), pp. 4, 6-8, 14) |
| feedback_observation | Visual, Structural Scene State, Runtime | The loop observes rendered pixels and masks, structural geometry/contact state, and solver runtime/health and drift traces. ([source](https://arxiv.org/pdf/2611.18078v1), pp. 4-6, 14) |
| memory_time | Short-Term Memory | The agent and solver retain scene programs, current state, contact state and checkpoints during reconstruction and rollout. ([source](https://arxiv.org/pdf/2611.18078v1), pp. 4-5, 9-10, 14) |
| memory_reach | Local Memory | State and diagnostics are available to the current reconstruction/rollout controller; no cross-run or multi-agent shared memory is described. ([source](https://arxiv.org/pdf/2611.18078v1), pp. 4-5, 9-10) |
| action_type | Code/Script, Structured Specification, Tool/Function Call | The VLM writes procedural 3D scripts/declarative physical models and invokes rendering, physics and verification execution. ([source](https://arxiv.org/pdf/2611.18078v1), pp. 2, 4-5) |
| graphics_software | Agent-Adapted | The agent-facing interface combines headless rendering, procedural scene compilation and solver adapters. ([source](https://arxiv.org/pdf/2611.18078v1), pp. 2-6, 14) |
| tools | Graphics Operations, Solver Validator, Perception models, Static Validator | Rendering/mask analysis, procedural mesh compilation, rigid and finite-element physics solvers, checkpoint/replay and video conditioning are callable capabilities in the workflow. ([source](https://arxiv.org/pdf/2611.18078v1), pp. 2, 4-6, 14) |
| resources | Assets, Documentation & Rules | The system accesses asset/material priors, declarative physical rules, procedural schemas and pretrained video/renderer components. ([source](https://arxiv.org/pdf/2611.18078v1), pp. 3-6, 14) |
| representation | Code, Geometry, Dynamic State, Pixels | The workflow uses procedural code, explicit meshes/geometry, dynamic mechanical state, simulation trajectories and rendered pixels. ([source](https://arxiv.org/pdf/2611.18078v1), pp. 1-6, 9-10) |

Events: [{"type": "first_submission", "value": "2026-11-13T12:02:43+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2611.18078v1", "authority": "primary", "version": "v1", "evidence": "PDF front matter and official arXiv metadata; target-local time 2026-11-13T06:02:43-06:00.", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: []

### [ImpedanceMimic: Learned Impedance as Action Space for Force-Accurate Motion Imitation](https://arxiv.org/abs/2611.19153v1)
scope_dependent | High | new_relative_to_snapshot
Application: Dynamic / Articulated assets, Dynamic / Physical simulation and effects, Cross-category; operations: Other
Introduces an RL controller that learns state-dependent joint impedance for force-accurate physics-based motion imitation and transfers across human and robot embodiments.
Scope: The paper provides an RL controller for simulated articulated human and humanoid bodies, but its principal target is biomechanical force recovery rather than graphics authoring or a graphics-agent task. It is retained as borderline because the controller acts on an executable dynamic character environment and the paper explicitly connects the setting to physics-based character animation.
Limits: The principal contribution is biomechanics and simulated control rather than graphics authoring; the method depends on motion/force supervision, a fixed biomechanical model and MuJoCo simulation, and uses future reference lookahead in its estimator/observations.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Simulation, Animation | The principal task is physics-based motion imitation and contact-force recovery in articulated body simulation; animation is a secondary graphics interpretation. ([source](https://arxiv.org/pdf/2611.19153v1), pp. 1-5) |
| input_form | 3D Representation, Video | Reference motion trajectories and simulated 3D body state are inputs; the method uses motion data rather than a user graphics-authoring request. ([source](https://arxiv.org/pdf/2611.19153v1), pp. 1-5) |
| output | Graphics Artifact | The controller outputs joint impedance/setpoint actions and produces simulated dynamic states and character motion. ([source](https://arxiv.org/pdf/2611.19153v1), pp. 1-6) |
| model_type | Not Applicable | The decision policy is an MLP actor in an RL controller; no LLM or VLM is used. ([source](https://arxiv.org/pdf/2611.19153v1), pp. 2-5) |
| model_training | RL Post-Training | The actor and critic are trained with PPO for 2 billion simulation steps using motion and force rewards. ([source](https://arxiv.org/pdf/2611.19153v1), pp. 2, 5, 19-22) |
| planning | PO-1 | The policy emits an action at each control step; no explicit multi-step task plan is represented. ([source](https://arxiv.org/pdf/2611.19153v1), pp. 3-5, 19) |
| workflow | Sequential | Reference observations, policy action, PD simulation and reward computation repeat in one ordered control loop. ([source](https://arxiv.org/pdf/2611.19153v1), pp. 2-5, 19-22) |
| update_strategy | Local Patch | The policy continuously changes joint gains and position offsets in response to current simulated state. ([source](https://arxiv.org/pdf/2611.19153v1), pp. 3-5) |
| verifier | Environment, Programmatic | MuJoCo physics executes the controller and computes contact forces; reward and evaluation metrics quantify tracking and force fidelity. ([source](https://arxiv.org/pdf/2611.19153v1), pp. 2, 5-6, 17) |
| feedback_assessment | Score, Diagnosis | Rewards and evaluation metrics provide continuous scores, while termination and numerical-invalid-state checks provide diagnostic/binary outcomes. ([source](https://arxiv.org/pdf/2611.19153v1), pp. 5-10, 17) |
| feedback_observation | Structural Scene State, Runtime | The actor observes proprioception, contact state, lookahead motion/force estimates and foot state; simulator runtime and termination are also used. ([source](https://arxiv.org/pdf/2611.19153v1), pp. 4-5, 19-20) |
| memory_time | Working Memory | The lagged gain state and current simulated state persist within an episode/control rollout, with reset at episode initialization. ([source](https://arxiv.org/pdf/2611.19153v1), pp. 4-5, 21-22) |
| memory_reach | Local Memory | State is available to the single actor/environment loop; no shared or cross-run agent memory is described. ([source](https://arxiv.org/pdf/2611.19153v1), pp. 4-5) |
| action_type | Structured Specification, Tool/Function Call | The policy emits structured numerical impedance parameters and setpoints that are passed to the PD controller/simulator. ([source](https://arxiv.org/pdf/2611.19153v1), pp. 3-5) |
| graphics_software | General-Purpose | The method directly uses MuJoCo Warp and a general-purpose articulated-body simulator without a graphics-specific agent adapter. ([source](https://arxiv.org/pdf/2611.19153v1), pp. 1-5) |
| tools | Solver Validator, Static Validator | MuJoCo Warp, PD control and physical contact computation are callable execution/solver components; kinematic-to-GRF estimation provides observation support. ([source](https://arxiv.org/pdf/2611.19153v1), pp. 2-5, 19-22) |
| resources | Examples & Trajectories, Documentation & Rules | The system uses motion/force trajectories from nine datasets, biomechanical model rules and simulator configurations. ([source](https://arxiv.org/pdf/2611.19153v1), pp. 2, 5, 15-22) |
| representation | Geometry, Dynamic State | The workflow represents articulated geometry, joint/dynamic state, contact forces and learned impedance trajectories. ([source](https://arxiv.org/pdf/2611.19153v1), pp. 1-5) |

Events: [{"type": "first_submission", "value": "2026-11-14T04:44:36+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2611.19153v1", "authority": "primary", "version": "v1", "evidence": "Official arXiv metadata; target-local time 2026-11-13T22:44:36-06:00.", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: []

## same_day_updates (0)

## late_discovery (0)

## date_unresolved (0)

## unresolved (1)

### [PhysLoop: Harnessing LLMs' Physics Awareness for Self-Improving Video Generation Models](https://arxiv.org/abs/2611.16748v2)
unresolved | Low | new_relative_to_snapshot
Application: Dynamic / Physical simulation and effects, Dynamic / Animation and temporal scene, Datasets and Benchmarks; operations: Generation, Editing, Auditing
Introduces a simulator-grounded harness for physically consistent video generation and repair, with controllable data construction and localized correction.
Scope: Full text supports a strong agent-to-graphics relation, but the version-pinned PDF could not be timestamp-validated against the frozen cutoff; preserve as unresolved rather than promote it.
Limits: The exact version event for the read PDF could not be source-validated before the frozen cutoff, so the full-text evidence is not promoted to a final retained classification in this run.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Unclear | The abstract indicates simulation-grounded video generation and repair, but the version receipt is unresolved. ([source](https://arxiv.org/abs/2611.16748), metadata and abstract) |
| input_form | Unclear | Input modalities are not fully attributable to a validated version record. ([source](https://arxiv.org/abs/2611.16748), metadata and abstract) |
| output | Unclear | Output claims are preserved only as unresolved abstract-level evidence. ([source](https://arxiv.org/abs/2611.16748), metadata and abstract) |
| model_type | Unclear | Version binding is unresolved. ([source](https://arxiv.org/abs/2611.16748), metadata and abstract) |
| model_training | Unclear | Version binding is unresolved. ([source](https://arxiv.org/abs/2611.16748), metadata and abstract) |
| planning | Unclear | Version binding is unresolved. ([source](https://arxiv.org/abs/2611.16748), metadata and abstract) |
| workflow | Unclear | Version binding is unresolved. ([source](https://arxiv.org/abs/2611.16748), metadata and abstract) |
| update_strategy | Unclear | Version binding is unresolved. ([source](https://arxiv.org/abs/2611.16748), metadata and abstract) |
| verifier | Unclear | Version binding is unresolved. ([source](https://arxiv.org/abs/2611.16748), metadata and abstract) |
| feedback_assessment | Unclear | Version binding is unresolved. ([source](https://arxiv.org/abs/2611.16748), metadata and abstract) |
| feedback_observation | Unclear | Version binding is unresolved. ([source](https://arxiv.org/abs/2611.16748), metadata and abstract) |
| memory_time | Unclear | Version binding is unresolved. ([source](https://arxiv.org/abs/2611.16748), metadata and abstract) |
| memory_reach | Unclear | Version binding is unresolved. ([source](https://arxiv.org/abs/2611.16748), metadata and abstract) |
| action_type | Unclear | Version binding is unresolved. ([source](https://arxiv.org/abs/2611.16748), metadata and abstract) |
| graphics_software | Unclear | Version binding is unresolved. ([source](https://arxiv.org/abs/2611.16748), metadata and abstract) |
| tools | Unclear | Version binding is unresolved. ([source](https://arxiv.org/abs/2611.16748), metadata and abstract) |
| resources | Unclear | Version binding is unresolved. ([source](https://arxiv.org/abs/2611.16748), metadata and abstract) |
| representation | Unclear | Version binding is unresolved. ([source](https://arxiv.org/abs/2611.16748), metadata and abstract) |

Events: [{"type": "first_submission", "value": "2026-11-12T12:59:35+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2611.16748", "authority": "primary", "evidence": "Official arXiv metadata reports the initial publication timestamp. The precise version history needed to bind the downloaded v2 PDF is not available in the returned metadata.", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: []

## excluded (0)

## Application index
| Application | Papers |
|---|---|
| 2D Graphics | [Vision-as-a-Tool: Visual Harness for Multimodal Agentic Coding](https://arxiv.org/abs/2611.17797v1) [same_day_new]; [RecurIR: Learning When and How to Revise Restoration Policies via Recursive Self-Improvement](https://arxiv.org/abs/2611.18006v1) [same_day_new] |
| Static / Object | [Vision-as-a-Tool: Visual Harness for Multimodal Agentic Coding](https://arxiv.org/abs/2611.17797v1) [same_day_new] |
| Static / CAD | None verified in this run |
| Static / Scene | [SceneAgent: A Multi-Agent Framework for Portable Game Scene Generation](https://arxiv.org/abs/2611.17821v1) [same_day_new]; [TelePhysica: Agentic Reconstruction of Physically Interactive Scenes](https://arxiv.org/abs/2611.18078v1) [same_day_new] |
| Dynamic / Articulated assets | [ImpedanceMimic: Learned Impedance as Action Space for Force-Accurate Motion Imitation](https://arxiv.org/abs/2611.19153v1) [same_day_new] |
| Dynamic / Animation and temporal scene | [Vision-as-a-Tool: Visual Harness for Multimodal Agentic Coding](https://arxiv.org/abs/2611.17797v1) [same_day_new]; [SceneAgent: A Multi-Agent Framework for Portable Game Scene Generation](https://arxiv.org/abs/2611.17821v1) [same_day_new]; [TelePhysica: Agentic Reconstruction of Physically Interactive Scenes](https://arxiv.org/abs/2611.18078v1) [same_day_new]; [PhysLoop: Harnessing LLMs' Physics Awareness for Self-Improving Video Generation Models](https://arxiv.org/abs/2611.16748v2) [unresolved] |
| Dynamic / Physical simulation and effects | [TelePhysica: Agentic Reconstruction of Physically Interactive Scenes](https://arxiv.org/abs/2611.18078v1) [same_day_new]; [ImpedanceMimic: Learned Impedance as Action Space for Force-Accurate Motion Imitation](https://arxiv.org/abs/2611.19153v1) [same_day_new]; [PhysLoop: Harnessing LLMs' Physics Awareness for Self-Improving Video Generation Models](https://arxiv.org/abs/2611.16748v2) [unresolved] |
| Datasets and Benchmarks | [PhysLoop: Harnessing LLMs' Physics Awareness for Self-Improving Video Generation Models](https://arxiv.org/abs/2611.16748v2) [unresolved] |
| Cross-category | [RecurIR: Learning When and How to Revise Restoration Policies via Recursive Self-Improvement](https://arxiv.org/abs/2611.18006v1) [same_day_new]; [ImpedanceMimic: Learned Impedance as Action Space for Force-Accurate Motion Imitation](https://arxiv.org/abs/2611.19153v1) [same_day_new] |

## Source ledger
| Source | Status | Checked pages / queries | Limitations |
|---|---|---|---|
| arxiv | partial | [{"query_or_url": "cs.GR new/recent and cs.CV new/recent via arxiv_scan", "checked_at": "2026-11-19T00:33:00+00:00", "outcome": "Complete observed pagination for all four required pairs; 1098 collected identities resolved; target-day and catch-up abstract pools triaged, but broad relevance recall and remaining title hints are incomplete."}] | Only cs.GR and cs.CV listing pairs were scanned; other arXiv categories in the prepared plan were not reached. 64 plausible leads remain ranked unread and 38 title-hint/graphics-category abstracts lack ranks. |
| hugging_face | partial | [{"query_or_url": "https://huggingface.co/papers/date/2026-11-13", "checked_at": "2026-11-19T00:11:34+00:00", "outcome": "Daily page inspected as a lead source; curation date was not used as publication date."}] | Daily page coverage is a curation snapshot, not publication completeness. |
| openreview | partial | [{"query_or_url": "agent CAD generation reconstruction editing constraint solver November 2026 site:openreview.net", "checked_at": "2026-11-19T00:12:21+00:00", "outcome": "Search returned OpenReview CAD leads; no target-day qualifying paper was verified."}] | Search-limited, not exhaustive venue coverage. |
| official_venues | partial | [{"query_or_url": "agent SVG diagram chart slide poster editable visual feedback November 2026 research; CVF benchmark search", "checked_at": "2026-11-19T00:12:00+00:00", "outcome": "Publisher/project leads inspected; no additional target-day PDF was completed."}] | Only search-returned publisher pages were inspected. |
| project_author_lab | partial | [{"query_or_url": "agent 3D scene/articulation/animation/simulation and graphics harness queries", "checked_at": "2026-11-19T00:15:31+00:00", "outcome": "Project/author links surfaced through search; no additional completed paper beyond catalog cohort."}] | Project/lab coverage was search-result limited. |

## Query coverage
- 2d: partial; [{'query_or_url': '2d', 'checked_at': '2026-11-19T00:33:00+00:00', 'outcome': 'Covered through broad search terms and/or catalog title/abstract triage; not exhaustive.'}]
- object: partial; [{'query_or_url': 'object', 'checked_at': '2026-11-19T00:33:00+00:00', 'outcome': 'Covered through broad search terms and/or catalog title/abstract triage; not exhaustive.'}]
- cad: partial; [{'query_or_url': 'cad', 'checked_at': '2026-11-19T00:33:00+00:00', 'outcome': 'Covered through broad search terms and/or catalog title/abstract triage; not exhaustive.'}]
- scene: partial; [{'query_or_url': 'scene', 'checked_at': '2026-11-19T00:33:00+00:00', 'outcome': 'Covered through broad search terms and/or catalog title/abstract triage; not exhaustive.'}]
- articulation: partial; [{'query_or_url': 'articulation', 'checked_at': '2026-11-19T00:33:00+00:00', 'outcome': 'Covered through broad search terms and/or catalog title/abstract triage; not exhaustive.'}]
- animation: partial; [{'query_or_url': 'animation', 'checked_at': '2026-11-19T00:33:00+00:00', 'outcome': 'Covered through broad search terms and/or catalog title/abstract triage; not exhaustive.'}]
- simulation: partial; [{'query_or_url': 'simulation', 'checked_at': '2026-11-19T00:33:00+00:00', 'outcome': 'Covered through broad search terms and/or catalog title/abstract triage; not exhaustive.'}]
- benchmark: partial; [{'query_or_url': 'benchmark', 'checked_at': '2026-11-19T00:33:00+00:00', 'outcome': 'Covered through broad search terms and/or catalog title/abstract triage; not exhaustive.'}]
- harness: partial; [{'query_or_url': 'harness', 'checked_at': '2026-11-19T00:33:00+00:00', 'outcome': 'Covered through broad search terms and/or catalog title/abstract triage; not exhaustive.'}]

## Source-derived candidate coverage

Mechanical audit of collected arXiv titles; relevance and semantic correctness require paper evidence.

- Metadata resolved: 1098 / 1098 collected IDs.
- Target-day / history-uncertain candidates: 210.
- Explicit triage decisions: 210; catalog-page delivery: 210.
- Missing source scans: 0; incomplete scans: 0.
- Unresolved metadata: 0; no triage decision: 0.
- Full candidate IDs and remaining gaps: `coverage-audit.json`. Unreviewed entries are not exclusions.
- Other platforms remain governed by the source ledger; this audit is not exhaustive discovery.

## Borderline graphics contributions

These records are not established core agentic systems. They remain visible with their scope uncertainty.

| Paper | Why borderline |
|---|---|
| ImpedanceMimic: Learned Impedance as Action Space for Force-Accurate Motion Imitation | The paper provides an RL controller for simulated articulated human and humanoid bodies, but its principal target is biomechanical force recovery rather than graphics authoring or a graphics-agent task. It is retained as borderline because the controller acts on an executable dynamic character environment and the paper explicitly connects the setting to physics-based character animation. |

## Agent-to-graphics evidence

| Paper | Status | Controller | Action / decision | Graphics target | Source |
|---|---|---|---|---|---|
| Vision-as-a-Tool: Visual Harness for Multimodal Agentic Coding | core | The coding agent Pθ, augmented by VHarness callable visual utilities Uϕ | Selects visual tools, writes/edits code, renders, diagnoses discrepancies and decides subsequent revisions | Rendered HTML/SVG images and Blender-generated 3D geometry/GLB artifacts | [pp. 1-4, 11, 15-18](https://arxiv.org/pdf/2611.17797v1) |
| SceneAgent: A Multi-Agent Framework for Portable Game Scene Generation | core | SCENEAGENT Orchestrator, Planner and fresh Builder agents | Decompose prompts, retrieve skills, select assets, place/edit actors, query SceneContext, validate geometry and refine/export the scene | Canonical 3D SceneContext and exported game-engine scene | [pp. 1-5, 12-13](https://arxiv.org/pdf/2611.17821v1) |
| RecurIR: Learning When and How to Revise Restoration Policies via Recursive Self-Improvement | core | RecurIR restoration agent and its PDM/RTEM/CPRM policy modules | Selects restoration tools and sequences, changes operation strength and processing regions, and accepts or rejects revised policies | Degraded image pixels and restored image artifacts | [pp. 1-5, 8, 12-17](https://arxiv.org/pdf/2611.18006v1) |
| TelePhysica: Agentic Reconstruction of Physically Interactive Scenes | core | TelePhysica vision-language coding agent A | Writes procedural meshes and physical models, renders candidates, interprets silhouette/contact/drift diagnostics and revises scene code before executing interventions | Executable 3D visual meshes, colliders, finite-element models and their rendered physical rollouts | [pp. 1-5, 7-8, 14](https://arxiv.org/pdf/2611.18078v1) |
| ImpedanceMimic: Learned Impedance as Action Space for Force-Accurate Motion Imitation | scope_dependent | ImpedanceMimic PPO actor | Modulates per-joint stiffness, damping and position setpoints at each simulation step | Simulated articulated human bodies and a Unitree G1 humanoid dynamic state | [pp. 1-5, 19-27](https://arxiv.org/pdf/2611.19153v1) |
| PhysLoop: Harnessing LLMs' Physics Awareness for Self-Improving Video Generation Models | unresolved | PhysLoop LLM role ensemble | Constructs scenes, invokes simulation/video tools and revises generated video artifacts | Physical scene configurations and rendered videos | [abstract](https://arxiv.org/abs/2611.16748) |

## Prior-day memory and carry-over

Frozen history: `knowledge/daily-history/through-20261015-bvb-v11`. Previously unread records now fully read: 0. Prior pending records still without a new full read: 95.

See history-delta.json for per-paper transitions. Historical results remain in the frozen bundle; not repeated is not excluded, and new-to-history does not mean newly published.

## Abstract-first reading queue

Attention pool: 258; abstracts not delivered: 0; priority/triage gaps: 38; unread ranked leads: 64. See reading-plan.json for model-authored priorities and deferred leads. Priority is not an inclusion judgment or recall guarantee.
