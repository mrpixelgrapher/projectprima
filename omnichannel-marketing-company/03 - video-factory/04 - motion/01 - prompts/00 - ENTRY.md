# 01 · Prompts

**Purpose:** for every transition, a cinematic prompt that tells the motion model exactly how to get from the start still to the end still: the camera move, what moves in the frame, how fast, and in what style.

## Contract

- **Reads:** `32-shots/<V-id>-shot-list.md` (camera move, transition out, stop-motion, duration); `33-stills/stills/` (the accepted keyframes); `32-shots/01-continuity.md`; `00 - control/01 - law/HANDOFFS.md` (H5).
- **Writes:** `34-motion/motion/<T-id>.prompt.md` (one per transition); `34-motion/00-motion-index.md`.
- **Done when:** every moving shot and every non-cut transition has a prompt, the prompts are handed off, and the task is on HOLD.

## Procedure

1. **List the transitions.** Each moving shot (its -a keyframe → its -b keyframe) is one; each transition out that isn't a plain cut (match cut, whip pan, dissolve, morph) is one, from this shot's last keyframe to the next shot's first. T-id: `T-<V-id>-<n>`. Plain cuts need no motion.
2. **Write each prompt:**

   | Field | Rule |
   |---|---|
   | Start still · end still | The two keyframe files |
   | Duration | From the shot list |
   | Camera | The one move, its direction and speed ("slow push-in, 10% closer over 2 s") |
   | Subject motion | What moves inside the frame, and how ("the left stone lifts 2 cm and rotates a quarter turn") |
   | Transition | For a between-shot transition: how A becomes B ("morph: the stone's outline becomes the lab report's seal") |
   | Stop-motion | If used: frames per second, frame count, and what moves per frame; the clip should look stepped, not smooth |
   | Style | Lighting and look held constant (from continuity); "no new objects, no text, no warping of the product" |
   | Easing | ease-in, ease-out, or linear |

3. **Hand off (H5)** and hold: `task.py hold <task-id> --on "H5 motion: 34-motion/motion/ (<n> transitions)"`. The operator runs each prompt with its two stills and returns the clip next to it (`<T-id>.mp4`). A rehearsal is not sent.

## Output template

    # <T-id> · <V-id> · shot <n> (→ shot <m>)
    start: <keyframe file> · end: <keyframe file> · duration: … s
    camera: … · subject motion: … · transition: … · stop-motion: … · easing: …
    style: … · never: …

## Worked example

*(illustrative)* `T-V2a-1` · start `K-V2a-S1-a` · end `K-V2a-S1-b` · 2.2 s · camera: slow top-down push-in, 15% closer · subject motion: none · easing: ease-out · never: the stones change shape or colour.

## Self-check

- [ ] Does every moving shot and every non-cut transition have a prompt?
- [ ] Does each prompt name one camera move?

## Traps

- **Asking for a story in one clip.** One move, one change. Complex moments are several shots.
