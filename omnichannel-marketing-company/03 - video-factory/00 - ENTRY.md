# 03 - video-factory

**Purpose:** turn the writing department's scripts and storyboards into videos, step by step. Refine the script, design every shot (what is in it, how the camera moves, how it cuts or morphs into the next, stop-motion described frame by frame), get every keyframe still from the image generation factory, write the cinematic prompts that make the motion between stills, and hand over an edit plan to assemble the final cut.

**Use when:** a task's engagement includes video: the route sends it here after `02 - content/05 - writing`, and back to `02 - content/06 - packaging` after the edit plan.

## Nodes (each node folder's `00 - ENTRY.md` is its instruction)

| # | Node | One job | Task folder |
|---|---|---|---|
| 1 | `01 - script/` | Refine each script and storyboard into a shooting script: tight, timed, every frame picturable | `31-script/` |
| 2 | `02 - shots/` | Design every shot: scene, framing, lens, camera move, light, transition, stop-motion; one continuity bible | `32-shots/` |
| 3 | `03 - stills/` | One Nano Banana scene prompt per keyframe still → the image factory (H4); check what returns | `33-stills/` |
| 4 | `04 - motion/` | One cinematic motion prompt per transition between two stills → the operator runs it (H5); check the clips | `34-motion/` |
| 5 | `05 - edit-plan/` | The edit decision list: clip order, timings, voice-over, on-screen text, music, sound, captions, exports | `35-edit-plan/` |

## How the factory works with the outside

- **Stills** come from the image generation factory (Nano Banana, custom scene prompting), outside this repo: hand-off H4 in `00 - control/01 - law/HANDOFFS.md`. Every still lands next to its prompt file.
- **Motion** between two stills is generated from our transition and cinematic prompts by the operator in an image-to-video tool: hand-off H5. Every clip lands next to its prompt file.
- **The final cut** is assembled from the edit plan by the operator or the client's team.

## Past material merged here

| From | Became |
|---|---|
| The operator's design lock (`00 - control/04 - source-intent/06 - operator-directives-2026-09-28-design-lock.md`, round 10): "the video department will tell what it wants in the shots, with the transition of camera movement and stop motion everything clearly described… the image generation part goes through the image generation factory… using the transition and cinematic prompting that you create we will get the motion between the shots" | This department: shot design (`02 - shots/`), stills (`03 - stills/`), motion (`04 - motion/`), edit plan (`05 - edit-plan/`) |
