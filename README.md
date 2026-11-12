# Nuketape-QA

Griptape Nodes project for QA-testing the Griptape ⇄ Nuke integration (NukeTape): parameter
round-tripping, error propagation through the Nuke host API, and proxy-model workflows.

## Setup

1. **Engine:** Griptape Nodes engine **0.109.0 or later** (the newest workflows here were saved
   with 0.109.0).
2. **Clone this repo** and open it as a project in Griptape Nodes (`griptape-nodes-project.yml`
   at the root — it appears as *Nuke Testing Project*). Libraries inside `libraries/` are picked
   up automatically.

   ```bash
   git clone https://github.com/kieranwestfoundry/Nuketape-QA-.git
   ```
3. **Add the libraries that aren't in this repo** — clone them into `libraries/`:

   ```bash
   cd libraries
   # Required — pinned to the version these workflows were built against
   git clone --branch v0.90.3 https://github.com/griptape-ai/griptape-nodes-library-standard.git
   # Optional — only needed for Griptape Cloud nodes
   git clone https://github.com/griptape-ai/griptape-nodes-library-griptape-cloud.git
   ```

4. Restart the engine (or reload libraries) so the new libraries and their templates register.

## What's in here

### Project workflows (root)

| Workflow | Purpose |
|---|---|
| `errors2log.py` | Nodes that deliberately warn / error — checks what reaches Nuke |
| `test_default_parameters_w_type_enforcing.py` | Start Flow with every parameter type + defaults → End Flow |
| `test_default_parameters_passthrough2artifact.py` | As above, passing values through to artifacts |

### QA library — `libraries/griptape-nodes-library-qa/`

Shared QA helpers. Registered automatically from `libraries/`.

**Node: Emit Warning / Error** (category *QA*)

- `severity` = `WARNING` → writes a warning to the engine log. **Does not reach Nuke** over the
  host API (the protocol has no warning state); visible only in a published gizmo's run log.
- `severity` = `ERROR` → raises, so the node fails. The engine emits `NodeErrorEvent`, which the
  Nuke host API forwards: node state `failed` + message, and the run verdict is `failed`.

**Proxy workflow templates** (`workflows/templates/proxy_*.py`) — 18 templates covering image
edit, text→image/video, video edit, start/end frame, motion transfer, Kling motion control,
Seedance 2.5, WAN animate, splats, and Tripo text→3D. Opening one creates your own copy.

Notes:

- `proxy_tripo_text_to_3d` also needs the **USD Tools** library.
- `proxy_video_start_end_frame` needs your own start/end frame images.
- Source media for the other input-driven templates is in `workflows/inputs/`.

## Known issues

- **Hard-coded input paths.** Some workflows still point at `/Users/kieranwest/...`. Re-point
  their input nodes at your own files (or at `libraries/griptape-nodes-library-qa/workflows/inputs/`).
