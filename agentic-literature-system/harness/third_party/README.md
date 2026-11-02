# Third-party attribution

`bvb_sandbox/models.py` is based on [Mini-BVB](https://github.com/yunlong10/BVB), commit `fa419e41288b5b9c5e1007fcfbce4e2674bbfe72`, file `sandbox/bvb_sandbox/models.py`. Its [MIT license](BVB-LICENSE) is retained. Only the model adapter needed by this runner is vendored; Blender and the full upstream project are not required.

Local modifications use the installed price table without an import-time network fetch, add caller-configured token prices and rejects unknown pricing instead of silently treating usage as free. `agent.py` adapts the Mini-BVB feedback loop to research tools, evidence checkpoints, recovery, and report validation. `responses_model.py` is the research project's Responses transport. This release does not claim to reproduce a host agent's private prompts or tool runtime.
