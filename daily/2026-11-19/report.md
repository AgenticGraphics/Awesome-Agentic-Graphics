# Agentic Graphics daily report
Date: 2026-11-19 | Timezone: America/Chicago | As of: 2026-11-20T05:00:02+00:00
partial browser-based same-day search; source coverage incomplete
Taxonomy: google-doc-taxonomy-v3-2026-10-15 | Snapshot: authorized_live_snapshot_reconciled_and_frozen

## Coverage limits
- Search indexes and public release pages may lag; field-wide completeness is not established.

No qualifying same-day Agentic Graphics paper was verified in the browsed source set.
Coverage is limited to the sources and queries below; unpublished or unindexed papers may be missing.

## already_reported (0)

## same_day_new (0)

## same_day_updates (0)

## late_discovery (4)

### [MillBill: A Machining Agent with Geometric Feedback](https://arxiv.org/abs/2611.22565v2)
core | High | new_relative_to_snapshot
Application: Static / CAD; operations: Generation, Editing, Auditing
A task-time CAD/CAM agent that delegates numerical geometric execution and verification to a harness while the language model makes process-level machining decisions. It reports 97.4% of target surface within 0.1 mm on 100 simulated parts.
Scope: The language-model agent chooses machining operations, tools, parameters, and revisions for a B-rep CAD artifact; the harness executes toolpaths and simulates the resulting geometry, with deviations returned to the agent.
Limits: Limited to indexed three-axis machining from six principal directions; workholding, travel, collisions, tool deflection, vibration, wear, and thread geometry are incompletely modeled. The evaluation uses simulated machining, one public model collection, and one run per method and part.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Modeling | Turning a B-rep part into a machining program and simulated workpiece is the stated task. ([source](https://arxiv.org/pdf/2611.22565v2), pp. 1-3) |
| input_form | 3D Representation, Document | Inputs are target STEP B-rep, stock, material, and optional drawing notes. ([source](https://arxiv.org/pdf/2611.22565v2), p. 3) |
| output | Program, Graphics Artifact | Output is one G-code program per setup and a machined workpiece after simulation. ([source](https://arxiv.org/pdf/2611.22565v2), p. 3) |
| model_type | Hybrid | A language model is paired with geometric and learned perception components. ([source](https://arxiv.org/pdf/2611.22565v2), pp. 1, 7, 13) |
| model_training | Off-the-Shelf | The paper uses Qwen3.8-27B and contrasts its off-the-shelf decision use with trained machining systems. ([source](https://arxiv.org/pdf/2611.22565v2), pp. 2, 7) |
| planning | PO-2 | Fixed setup/reference planning is combined with ReAct agents revising process and tool plans. ([source](https://arxiv.org/pdf/2611.22565v2), pp. 3-5) |
| workflow | Sequential | Feature recognition, setup selection, planning, execution, simulation, and refinement form an ordered pipeline. ([source](https://arxiv.org/pdf/2611.22565v2), pp. 3-6) |
| update_strategy | Local Patch, Candidate Selection | Harness corrections and model fixes rebuild candidates; the best of at most three builds is retained. ([source](https://arxiv.org/pdf/2611.22565v2), p. 6) |
| verifier | Programmatic, Environment | Safety checks, geometric simulation, and surface-deviation measurement judge programs. ([source](https://arxiv.org/pdf/2611.22565v2), pp. 5-6) |
| feedback_assessment | Score, Diagnosis | Candidates are ranked by safety issues, gouged area, and tolerance score; errors are diagnosed by feature and operation. ([source](https://arxiv.org/pdf/2611.22565v2), p. 6) |
| feedback_observation | Structural Scene State, Runtime | Feedback includes simulated geometry deviations, attributed error regions, and runtime/safety issues. ([source](https://arxiv.org/pdf/2611.22565v2), pp. 3, 5-6) |
| memory_time | Short-Term Memory | Best builds are retained within the iterative task loop. ([source](https://arxiv.org/pdf/2611.22565v2), p. 6) |
| memory_reach | Local Memory | State is passed within the selected planning and verification pipeline; no cross-run shared memory is described. ([source](https://arxiv.org/pdf/2611.22565v2), pp. 3-6) |
| action_type | Tool/Function Call, Structured Specification | Agents call harness tools and return structured JSON plans that become toolpaths/G-code. ([source](https://arxiv.org/pdf/2611.22565v2), pp. 3-5) |
| graphics_software | Agent-Adapted | The method adapts FreeCAD CAM with an agent-facing geometric harness. ([source](https://arxiv.org/pdf/2611.22565v2), p. 5) |
| tools | Graphics Operations, Perception models, Static Validator, Execution Utilities | Feature recognition, reachability, CAM generation, simulation, safety checks, and deviation measurement are used as callable capabilities. ([source](https://arxiv.org/pdf/2611.22565v2), pp. 3-6, S1) |
| resources | Assets, Documentation & Rules | The workflow accesses a B-rep/stock, machining rules and tables, material data, and a cutter library. ([source](https://arxiv.org/pdf/2611.22565v2), pp. 4-5, S1) |
| representation | Code, Geometry | B-rep geometry, structured plans/G-code, toolpaths, and simulated workpiece geometry are central representations. ([source](https://arxiv.org/pdf/2611.22565v2), pp. 1-6) |

Events: [{"type": "first_submission", "version": "v1", "value": "2026-11-17T10:52:45+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2611.22565v1", "authority": "primary", "evidence": "Official arXiv metadata and history record v1 submission on 17 Nov 2026.", "prior_event_status": "not_seen_in_supplied_history"}, {"type": "revision", "version": "v2", "value": "2026-11-18T18:33:02+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2611.22565v2", "authority": "primary", "evidence": "Official arXiv metadata and history record v2 update on 18 Nov 2026.", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: []

### [ConserveEdit: Source-Anchored Transactions for Drift-Bounded Iterative Image Editing](https://arxiv.org/abs/2611.22724v1)
core | High | new_relative_to_snapshot
Application: 2D Graphics; operations: Editing, Auditing
An editor-agnostic transactional controller that anchors iterative image edits to the source, separates authorized change from protected content, and accepts candidates only when progress, drift, and quality tests independently pass. On 1,053 MagicBrush turns, masked commitment keeps outside-support pixels bit-exact; automatic-mask protected-content violations are 2% versus 48% for direct masked editing.
Scope: The transactional controller makes explicit decisions over candidate image edits: it selects authorized supports and candidate commits, evaluates graphics-state feedback, and rolls back or repairs failed edits. The paper evaluates this controller on iterative image-editing artifacts.
Limits: Grounding is the main bottleneck: missed support can make edits incomplete, automatic masks have low overlap, and the system abstains on many turns. The guarantees cover only represented support and descriptors, not semantic completeness or seam quality. Experiments use one frozen editor, MagicBrush, fixed formulas, and no human preference study.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Modeling | The task is iterative instruction-driven image editing under source-preservation constraints. ([source](https://arxiv.org/pdf/2611.22724v1), pp. 1-5) |
| input_form | Language, Image | The controller receives a source image and free-form instruction, and uses masks or grounded image regions. ([source](https://arxiv.org/pdf/2611.22724v1), pp. 1, 3-4) |
| output | Graphics Artifact | The externally returned product is the committed edited image and decision log. ([source](https://arxiv.org/pdf/2611.22724v1), pp. 1, 5-8) |
| model_type | Not Applicable | The paper explicitly states ConserveEdit itself uses no LLM or MLLM; fixed formulas, detectors, and procedural simulation implement its controller. ([source](https://arxiv.org/pdf/2611.22724v1), p. 8) |
| model_training | Not Applicable | The controller is not a trained decision model; frozen Qwen-Image-Edit is the executor under study. ([source](https://arxiv.org/pdf/2611.22724v1), p. 8) |
| planning | PO-1 | The loop follows fixed contract compilation, candidate generation, audit, commit/rollback, and repair rules. ([source](https://arxiv.org/pdf/2611.22724v1), pp. 3-5, Algorithm 1) |
| workflow | Sequential | Iterations operate in an ordered sequential refinement loop. ([source](https://arxiv.org/pdf/2611.22724v1), pp. 3-5, Algorithm 1) |
| update_strategy | Local Patch, Rollback, Candidate Selection | Candidates are masked into local patches, feasible candidates are selected, and failed candidates are rolled back and repaired. ([source](https://arxiv.org/pdf/2611.22724v1), pp. 3-5) |
| verifier | Programmatic | Fixed progress, protected-content drift, change-map, and quality tests programmatically audit each candidate. ([source](https://arxiv.org/pdf/2611.22724v1), pp. 3-5) |
| feedback_assessment | Binary, Score, Diagnosis | The controller uses thresholded feasibility tests, continuous progress/quality scores, and named violated entities/clauses for diagnosis. ([source](https://arxiv.org/pdf/2611.22724v1), pp. 3-5) |
| feedback_observation | Visual, Structural Scene State | Observations include pixels, masks, protected-content descriptors, image quality, and candidate output state. ([source](https://arxiv.org/pdf/2611.22724v1), pp. 3-5) |
| memory_time | Short-Term Memory | The edit contract, cumulative authorized support, current image, and decision log persist across turns within one refinement run. ([source](https://arxiv.org/pdf/2611.22724v1), pp. 3-5) |
| memory_reach | Local Memory | The state is shared by the single controller loop; no cross-run memory is described. ([source](https://arxiv.org/pdf/2611.22724v1), pp. 3-5) |
| action_type | Tool/Function Call | The controller invokes a frozen image editor and applies structured masks/commit operations to candidate images. ([source](https://arxiv.org/pdf/2611.22724v1), pp. 3-5, Algorithm 1) |
| graphics_software | Agent-Adapted | The method wraps frozen general-purpose image editors with a dedicated agent-facing transaction and audit layer. ([source](https://arxiv.org/pdf/2611.22724v1), pp. 1, 5-8) |
| tools | Graphics Operations, Perception models, Static Validator | The workflow uses image editors, masks, Grounding DINO, SAM, CLIP/SigLIP predicates, ArcFace/OCR descriptors, and quality/drift checks. ([source](https://arxiv.org/pdf/2611.22724v1), pp. 3-8) |
| resources | Documentation & Rules | The controller accesses source images, edit contracts, masks, descriptors, thresholds, and documented rules; MagicBrush supplies source/instruction/target data for evaluation. ([source](https://arxiv.org/pdf/2611.22724v1), pp. 4-8, 14-28) |
| representation | Pixels, Layouts | The artifact is represented as pixels and masks; the contract and decision log are structured specifications; the edit support is a 2D layout/region representation. ([source](https://arxiv.org/pdf/2611.22724v1), pp. 1, 3-5) |

Events: [{"type": "first_submission", "version": "v1", "value": "2026-11-17T12:58:37+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2611.22724v1", "authority": "primary", "evidence": "The PDF and arXiv canonical page identify v1 as submitted 17 Nov 2026.", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: []

### [CutAgent: Creative-Gene-Driven Planning and Experience-Guided Self-Refinement for High-CTR E-commerce Advertising Video Creation](https://arxiv.org/abs/2611.22418v1)
core | High | new_relative_to_snapshot
Application: Dynamic / Animation and temporal scene; operations: Generation, Editing, Auditing
A dual-agent Plan–Execute–Self-Evolve system for high-CTR advertising video production. GeneAgent creates a structured creative gene using SFT and CTR-guided GRPO; VideoAgent turns it into a rendered timeline and applies reflection-based local revision plus long-term failure-correction memory. The paper reports 2.21% online CTR and 60.4% forced-choice preference.
Scope: GeneAgent and VideoAgent make explicit planning, retrieval, rendering, revision, and memory-write decisions over advertising video timelines and assets; the reflection loop evaluates rendered graphics and changes subsequent production actions.
Limits: The training data and online evaluation are commercial/product-specific; the CTR reward is a training-time surrogate rather than the reported evaluation metric. The system relies heavily on retrieved clips, fixed schemas, automated multimodal evaluators, and up to three reflection rounds. Generalization beyond e-commerce ads, categories, clip pools, and the reported production stack is not established.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Animation | The task is automated e-commerce advertising video creation with narrative planning, timeline rendering, and iterative production. ([source](https://arxiv.org/pdf/2611.22418v1), pp. 1-4) |
| input_form | Language, Image, Video | Product attributes, review summaries, main/detail product images, and available video assets are inputs. ([source](https://arxiv.org/pdf/2611.22418v1), pp. 1, 3-4) |
| output | Structured Specification, Graphics Artifact, Rendered Media | The system outputs a structured creative gene, executable storyboard, and rendered advertising video. ([source](https://arxiv.org/pdf/2611.22418v1), pp. 3-8, 18-20) |
| model_type | Hybrid | GeneAgent is a vision-language model and VideoAgent uses an LLM with multimodal retrieval and media tools. ([source](https://arxiv.org/pdf/2611.22418v1), pp. 3, 5-7, 14) |
| model_training | Supervised Fine-Tuning, RL Post-Training | GeneAgent receives high-CTR supervised fine-tuning and CTR-guided GRPO; VideoAgent uses a deployed LLM workflow. ([source](https://arxiv.org/pdf/2611.22418v1), pp. 1, 4-7, 12-14) |
| planning | PO-2 | GeneAgent learns an explicit ordered creative gene and VideoAgent expands it into an executable shot storyboard, while fixed production modules execute the plan. ([source](https://arxiv.org/pdf/2611.22418v1), pp. 2-4, 6, 18-19) |
| workflow | Sequential | The workflow orders plan, memory read, shot planning, retrieval, TTS/BGM, rendering, evaluation, diagnosis, revision, verification, and memory write. ([source](https://arxiv.org/pdf/2611.22418v1), pp. 3-6, 14-15) |
| update_strategy | Local Patch, Replanning, Candidate Selection | Reflection revises only affected shots/modules, re-executes them, and accepts verified candidates; the loop can replan deficient production decisions. ([source](https://arxiv.org/pdf/2611.22418v1), pp. 6, 14-15) |
| verifier | Critic, Programmatic | An independent reflection/evaluation module scores six video dimensions and supplies temporally grounded evidence for diagnosis; format and consistency checks are also used. ([source](https://arxiv.org/pdf/2611.22418v1), pp. 6-8, 14-16) |
| feedback_assessment | Score, Diagnosis | The evaluator returns six scalar quality scores and diagnoses localized defects such as missing selling points, repeated clips, mismatched narration, or poor music. ([source](https://arxiv.org/pdf/2611.22418v1), pp. 6-8, 14-16) |
| feedback_observation | Visual, Runtime | Feedback observes rendered frames, shot intervals, text/audio segments, timeline elements, and rendering/production conditions. ([source](https://arxiv.org/pdf/2611.22418v1), pp. 6, 14-16) |
| memory_time | Long-Term Memory | Verified failure-correction experiences are written to E and reused on later products and genes. ([source](https://arxiv.org/pdf/2611.22418v1), pp. 1-3, 6, 14-15) |
| memory_reach | Global Memory | Category shards are retrieved by VideoAgent for subsequent products, and verified corrections are shared across the production workflow. ([source](https://arxiv.org/pdf/2611.22418v1), pp. 6, 14-15) |
| action_type | Structured Specification, Tool/Function Call | Agents emit structured creative genes/storyboards and invoke clip retrieval, TTS, BGM matching, rendering, evaluation, and revision modules. ([source](https://arxiv.org/pdf/2611.22418v1), pp. 3-7, 18-19) |
| graphics_software | Agent-Adapted | The method constructs an agent-facing workbench that adapts retrieval, TTS, audio matching, ffmpeg timeline rendering, and reflection around general media tools. ([source](https://arxiv.org/pdf/2611.22418v1), pp. 3-7, 14, 18-20) |
| tools | Execution Utilities, Graphics Operations, Perception models, Static Validator | Tools include clip retrieval, multimodal embeddings, TTS, subtitle generation, BGM matching, ffmpeg rendering, evaluation, diagnosis, and verification. ([source](https://arxiv.org/pdf/2611.22418v1), pp. 3-7, 14-15) |
| resources | Assets, Examples & Trajectories, Documentation & Rules | The workflow accesses product images/attributes, cleaned clip pools, historical ad examples, CutAgent-70K trajectories/genes/CTR, production rules, and the long-term correction memory. ([source](https://arxiv.org/pdf/2611.22418v1), pp. 1, 4-6, 14-15) |
| representation | Code, Layouts, Pixels, Learned State | Creative genes and storyboards are structured specifications; scripts and ffmpeg timelines are code-like; final videos are pixels/rendered media; learned gene policy is a learned state. ([source](https://arxiv.org/pdf/2611.22418v1), pp. 3-6, 18-20) |

Events: [{"type": "first_submission", "version": "v1", "value": "2026-11-17T08:54:39+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2611.22418v1", "authority": "primary", "evidence": "The canonical arXiv page records submission on 17 Nov 2026.", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: []

### [CodeReel: Accelerating Code-to-Video Agents with Exact Frame Reuse and Blocking-Aware Scheduling](https://arxiv.org/abs/2611.22967v1)
enabling_or_adjacent | High | new_relative_to_snapshot
Application: Dynamic / Animation and temporal scene, Datasets and Benchmarks, Cross-category; operations: Generation, Editing, Auditing
A training-free execution layer behind code-to-video agents. Exact frame reuse cuts redundant rendering while blocking-aware scheduling prioritizes verdicts and useful work-ahead. On EditLoop it reduces agent wait by 36.3% versus Rebuild and 57.9% versus Sequential, with exact frame-level correctness.
Scope: CodeReel is an explicit agent-facing graphics execution and validation layer: coding agents write and refine video programs, while CodeReel executes rendering/checking decisions and preserves exact graphics outputs. The paper does not introduce the agent's creative controller, so it is retained as enabling infrastructure.
Limits: The scope is 2D video programs whose drawing commands can be recorded; 3D scenes, GPU rendering, generative footage, and unsupported interfaces are not reused. Correctness depends on deterministic supported renderers and substantial engineering assumptions. The benchmark is based on replayed and selected real coding-agent sessions and does not make CodeReel the creative decision-maker.

| Taxonomy field | Values | Evidence |
|---|---|---|
| task | Animation | The system supports coding agents that create and refine animated/video graphics programs in a build-inspect-edit loop. ([source](https://arxiv.org/pdf/2611.22967v1), pp. 1-3) |
| input_form | Language, Document | The agent supplies source programs, scene scripts, narration timelines, assets, and edit requests to build commands. ([source](https://arxiv.org/pdf/2611.22967v1), pp. 1-5) |
| output | Graphics Artifact, Rendered Media | Build calls return verdicts/errors or rendered films; CodeReel also materializes exact frame and segment caches. ([source](https://arxiv.org/pdf/2611.22967v1), pp. 1-8) |
| model_type | Not Applicable | CodeReel is training-free and model-agnostic; the study evaluates external coding agents rather than introducing a decision model. ([source](https://arxiv.org/pdf/2611.22967v1), pp. 1-2, 6-8) |
| model_training | Not Applicable | The execution layer is explicitly training-free. ([source](https://arxiv.org/pdf/2611.22967v1), pp. 1-2) |
| planning | PO-1 | Scheduling follows fixed rules based on build dependencies, blocked consumer, pass-rate history, and resource thresholds. ([source](https://arxiv.org/pdf/2611.22967v1), pp. 4-5, Algorithm 1) |
| workflow | Graph-Structured | A build is a DAG of voice, layout, checks, lint, render, film checks, encoding, and work-ahead operations. ([source](https://arxiv.org/pdf/2611.22967v1), pp. 3-5, Algorithm 1) |
| update_strategy | Candidate Selection | The scheduler chooses which cached frames/segments to reuse and which operations to execute, while preserving exact outputs. ([source](https://arxiv.org/pdf/2611.22967v1), pp. 4-5, 12-14) |
| verifier | Programmatic, Environment | Automated lint, timeline, overlap, text, pixel, sound, determinism, and from-scratch correctness checks verify builds and cached frames. ([source](https://arxiv.org/pdf/2611.22967v1), pp. 2-5, 10-13) |
| feedback_assessment | Binary | Build checks return pass/fail verdicts and named errors that determine whether the agent receives a film or correction information. ([source](https://arxiv.org/pdf/2611.22967v1), pp. 1-5) |
| feedback_observation | Runtime, Visual | The layer observes runtime completion/blocking state, check results, source changes, frame keys, rendered pixels, and resource availability. ([source](https://arxiv.org/pdf/2611.22967v1), pp. 1-5, 10-14) |
| memory_time | Short-Term Memory | Frame keys, frame stores, segment stores, and build/check results persist across versions within a session but caches start cold for each session. ([source](https://arxiv.org/pdf/2611.22967v1), pp. 4, 10-13) |
| memory_reach | Local Memory | A single execution layer maintains local stores and a shared resource ledger for agents on one machine; caches are not shared across sessions. ([source](https://arxiv.org/pdf/2611.22967v1), pp. 4-7, 14-15) |
| action_type | Tool/Function Call, Code/Script | CodeReel receives build/tool calls, executes code and rendering operations, schedules checks, and returns verdicts/films. ([source](https://arxiv.org/pdf/2611.22967v1), pp. 1-5, Algorithm 1) |
| graphics_software | Agent-Adapted | The method adapts Canvas 2D/cv.js and Remotion-style rendering into an execution layer designed for coding agents. ([source](https://arxiv.org/pdf/2611.22967v1), pp. 1-8, 11-19) |
| tools | Execution Utilities, Graphics Operations, Static Validator | Tools include program execution, voice/layout, lint, visual checks, rendering, encoding, frame-key evaluation, frame/segment stores, and resource scheduling. ([source](https://arxiv.org/pdf/2611.22967v1), pp. 3-5, 10-14) |
| resources | Examples & Trajectories, Documentation & Rules | EditLoop provides recorded agent sessions, versions, tool calls, source objects, frame traces, and correctness gates; runtime documentation defines frame contracts. ([source](https://arxiv.org/pdf/2611.22967v1), pp. 2-3, 10-12) |
| representation | Code, Pixels, Layouts | Source programs and drawing commands are code; timelines/pages are layouts; frame stores and films are pixels/rendered media. ([source](https://arxiv.org/pdf/2611.22967v1), pp. 1-5, 11-13) |

Events: [{"type": "first_submission", "version": "v1", "value": "2026-11-17T15:52:15+00:00", "precision": "timestamp", "timezone": "UTC", "primary_url": "https://arxiv.org/abs/2611.22967v1", "authority": "primary", "evidence": "The canonical arXiv page and PDF record v1 submission on 17 Nov 2026.", "prior_event_status": "not_seen_in_supplied_history"}]
Taxonomy deltas: []

## date_unresolved (0)

## unresolved (0)

## excluded (0)

## Application index
| Application | Papers |
|---|---|
| 2D Graphics | [ConserveEdit: Source-Anchored Transactions for Drift-Bounded Iterative Image Editing](https://arxiv.org/abs/2611.22724v1) [late_discovery] |
| Static / Object | None verified in this run |
| Static / CAD | [MillBill: A Machining Agent with Geometric Feedback](https://arxiv.org/abs/2611.22565v2) [late_discovery] |
| Static / Scene | None verified in this run |
| Dynamic / Articulated assets | None verified in this run |
| Dynamic / Animation and temporal scene | [CutAgent: Creative-Gene-Driven Planning and Experience-Guided Self-Refinement for High-CTR E-commerce Advertising Video Creation](https://arxiv.org/abs/2611.22418v1) [late_discovery]; [CodeReel: Accelerating Code-to-Video Agents with Exact Frame Reuse and Blocking-Aware Scheduling](https://arxiv.org/abs/2611.22967v1) [late_discovery] |
| Dynamic / Physical simulation and effects | None verified in this run |
| Datasets and Benchmarks | [CodeReel: Accelerating Code-to-Video Agents with Exact Frame Reuse and Blocking-Aware Scheduling](https://arxiv.org/abs/2611.22967v1) [late_discovery] |
| Cross-category | [CodeReel: Accelerating Code-to-Video Agents with Exact Frame Reuse and Blocking-Aware Scheduling](https://arxiv.org/abs/2611.22967v1) [late_discovery] |

## Source ledger
| Source | Status | Checked pages / queries | Limitations |
|---|---|---|---|
| arxiv | not_reached_within_budget | [] | Not yet attempted |
| hugging_face | not_reached_within_budget | [] | Not yet attempted |
| openreview | not_reached_within_budget | [] | Not yet attempted |
| official_venues | not_reached_within_budget | [] | Not yet attempted |
| project_author_lab | not_reached_within_budget | [] | Not yet attempted |

## Query coverage
- 2d: not_reached_within_budget; []
- object: not_reached_within_budget; []
- cad: not_reached_within_budget; []
- scene: not_reached_within_budget; []
- articulation: not_reached_within_budget; []
- animation: not_reached_within_budget; []
- simulation: not_reached_within_budget; []
- benchmark: not_reached_within_budget; []
- harness: not_reached_within_budget; []

## Source-derived candidate coverage

Mechanical audit of collected arXiv titles; relevance and semantic correctness require paper evidence.

- Metadata resolved: 100 / 1163 collected IDs.
- Target-day / history-uncertain candidates: 2.
- Explicit triage decisions: 2; catalog-page delivery: 2.
- Missing source scans: 0; incomplete scans: 0.
- Unresolved metadata: 1063; no triage decision: 0.
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
| MillBill: A Machining Agent with Geometric Feedback | core | ReAct language-model process-sequence and tool-selection agents using Qwen3.8-27B | Select and revise machining operations, setup plans, tool assignments, and cutting parameters | B-rep CAD part, stock, generated toolpaths/G-code, and simulated machined geometry | [pp. 1-6, Fig. 1, Secs. 3.3-3.6](https://arxiv.org/pdf/2611.22565v2) |
| ConserveEdit: Source-Anchored Transactions for Drift-Bounded Iterative Image Editing | core | ConserveEdit transactional controller with fixed contract compiler, mask compositor, drift/progress/quality audits, and repair logic | Select candidate image edits and authorized supports; commit, rollback, abstain, or repair based on graphics-state feedback | Source image, editable regions, protected faces/text/background, and committed pixel image | [pp. 1-8, Algorithm 1](https://arxiv.org/pdf/2611.22724v1) |
| CutAgent: Creative-Gene-Driven Planning and Experience-Guided Self-Refinement for High-CTR E-commerce Advertising Video Creation | core | GeneAgent plus VideoAgent and the independent reflection loop | Generate creative genes and shot scripts; select/retrieve clips; coordinate narration, subtitles, music, timeline rendering; diagnose and revise video components | Product advertising video timeline, clips, audio/subtitle layers, and rendered video | [pp. 1-8, 14-20](https://arxiv.org/pdf/2611.22418v1) |
| CodeReel: Accelerating Code-to-Video Agents with Exact Frame Reuse and Blocking-Aware Scheduling | enabling_or_adjacent | CodeReel execution layer plus the external coding agent issuing build/edit commands | Execute and schedule program builds, checks, renders, frame reuse, and work-ahead; return verdicts or films to the agent | Code-rendered Canvas/Remotion video programs, timelines, frames, audio, and rendered films | [pp. 1-8, Algorithm 1](https://arxiv.org/pdf/2611.22967v1) |

## Prior-day memory and carry-over

Frozen history: `knowledge/daily-history/through-20261015-bvb-v11`. Previously unread records now fully read: 0. Prior pending records still without a new full read: 95.

See history-delta.json for per-paper transitions. Historical results remain in the frozen bundle; not repeated is not excluded, and new-to-history does not mean newly published.

## Abstract-first reading queue

Attention pool: 19; abstracts not delivered: 0; priority/triage gaps: 0; unread ranked leads: 7. See reading-plan.json for model-authored priorities and deferred leads. Priority is not an inclusion judgment or recall guarantee.
