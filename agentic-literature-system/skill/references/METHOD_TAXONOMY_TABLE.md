# Current survey taxonomy snapshot

Source: https://github.com/AgenticGraphics/Awesome-Agentic-Graphics
Revision: public-research-snapshot-2026-10-15
Retrieved: 2026-10-15

The tab is named Taxonomy v3; its body says Taxonomy v2. Preserve this mismatch in provenance. Tools contains alternatives and is provisional. The executable codebook is a conservative operationalization, not a change to the source.

Taxonomy v2



User Input
Task
Modeling (Articraft) ·
Animation (ParticleGen) ·
Simulation (SAGE) ·
Visualization (PosterMELD)
Input Form
Language (Articraft) ·
Image (VIGA) ·
Video (SimFoundry) ·
3D Representation (WorldAct) ·
Document (PosterMELD)
Output:
Program: An executable description of how graphics content is created or modified. (Articraft, CADIR, ManimAgent)
Structured Specification: A declarative description of the desired content that requires interpretation or conversion. (ParticleGen, BuildArena)
Graphics Artifact (SimWorlds, SimFoundry, ParticleGen, PosterMELD) ·
Rendered Media (ManimAgent, Code2Worlds, PlotGen)
Base Model
Model Type: The model family or model composition responsible for agentic decision-making.
LLM (SimWorlds)
VLM (VIGA)
Hybrid (SimFoundry)
Model Training: How the decision-making model is used or adapted for the task.
Off-the-Shelf (VIGA) ·
Supervised Fine-Tuning (GIFT) ·
RL Post-Training (BlenderLLM)
Harness
Plan & Act
Planning: Whether a task plan is explicitly represented. Categories by the degree of hard-coding, from high to low:
PO-1: entirely hard-coded/fixed;
PO-2: hybrid;  (e.g. Articrafts)
PO-3: no hard-coded;
Workflow: How execution steps are connected and scheduled.
Sequential: Steps follow one ordered execution path. (Articraft, BannerAgency)
Parallel: Multiple execution paths run concurrently before aggregation. (ParticleGen)
Graph-Structured: Execution follows non-linear dependencies, including hierarchies, branches, search trees, or DAGs. (SceneSmith, BlenderGym, Cutscene Agent)
Update Strategy: How the system responds to feedback.
Regeneration (BlenderGym) ·
Local Patch (Articraft) ·
Replanning (SimWorlds) ·
Rollback (ParticleGen) ·
Candidate Selection (BlenderGym)
Feedback Mechanism
Verifier: The actor or mechanism that judges execution evidence.
Model: Self (VIGA) · Critic (SceneSmith)
Code: Programmatic (Articraft) · Environment (SAGE)
Human(LL3M)
Feedback Signal: Evidence used to guide a subsequent action or update.
Assessment: The judgment returned by the verifier.
Binary (PosterMELD) ·
Score (ParticleGen) ·
Ranking (BlenderGym) ·
Diagnosis (VIGA, Articraft)
Observation from the environment:
Visual (BlenderGym) · Structural Scene State (Articraft) · Runtime (SimWorlds)
Memory:  Information retained beyond one call for later use.
Time
Working Memory: Available only within one model call. (SimWorlds: fresh Coder/Reviewer calls)
Short-Term Memory: Retained across calls within one run, then reset. (VIGA, BlenderGym, SceneSmith, BannerAgency, SimWorlds)
Long-Term Memory: Retained and reused across runs. (MUSE, ManimAgent, SceneCraft, SimWorld Studio, GenRouter)
Reach:
Local Memory: Accessible only to a particular agent, role, or stage. (SceneSmith, SceneConductor, SimWorlds)
Global Memory: Shared across all agents in the system. (BannerAgency, LL3M, PosterMELD, BIMgent)
Graphics Interface & Tooling
Action Type: The form in which an operation is expressed for execution.
Code/Script (Articraft) ·
Structured Specification (ParticleGen) ·
Tool/Function Call (SAGE) ·
GUI Action (BIMgent)
Graphic softwares: ranked by agentic readiness, i.e. whether an agent-oriented interface is already available or must be constructed.
Agent-Ready: The environment provides agent-oriented operations and structured state access. (Articraft, MUSE)
Agent-Adapted: The method adds an agent-facing tool or adapter layer to an existing environment. (SAGE, SimWorlds, PosterMELD, VIGA)
General-Purpose: The agent directly uses native scripts, files, or GUI operations without a dedicated agent abstraction. (BlenderGym, ManimAgent, BIMgent)
Tools: Callable functions that act on or inspect graphics content.
Tools: Callable capabilities used during graphics execution.
Execution Utilities: Support execution and artifact management. (Articraft)
Graphics Operations: Create or modify graphics state (3D). (VIGA)
things that change the 3D scene/objects
authoring tools
Perception models: Analyze or generate graphics content. (SimFoundry)
e.g. SAM 3D, VLM
observation tools
Validators: Compute states satisfying geometric or physical constraints. (Scenethesis)
(optional)change the scene + analysis
Solver Validator: ones that explore alternative states to analyze the scene
Physics simulator
Static Validator: Check correctness or constraint satisfaction. (PosterMELD)
intersection checks? object floating? watertight?
If classified by direction/functionality, we can potentially go with this high level:
ActionAuthoring tools
Hybrid
Non-action tools
Observation tools (doesn’t take the goal/user-input)
Evaluation tools (takes the goal as input?)
Resources: Reusable content accessed or retrieved by the system.
Assets (SceneSmith) ·
Examples & Trajectories (ParticleGen) ·
Documentation & Rules (SimWorlds)
Representation: The form in which graphics content is specified, materialized, or rendered throughout the workflow.
Code(Articraft, CADIR): Executable or declarative descriptions such as scripts, DSLs, and CAD programs
Geometry (SimFoundry, SimWorlds): Explicit 3D content like meshes, scenes, materials, and rigs
Dynamic State (ParticleGen, SAGE): Time-varying state that evolves under simulation
Layouts (PosterMELD, BannerAgency): Structured 2D content such as vector graphics, posters, and slides
Pixels (BlenderFusion, ManimAgent) ·
Learned State (WorldAct, The Scene Language): Neural fields, embeddings, and world-model states
