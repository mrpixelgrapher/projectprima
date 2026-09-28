# 02 · Check

**Purpose:** accept only stills that match their shot and the continuity bible, so the motion between them doesn't break.

## Contract

- **Reads:** `33-stills/stills/` (prompts and returned stills); `32-shots/01-continuity.md`; the shot lists.
- **Writes:** statuses and notes in `33-stills/00-still-index.md`; revised prompts `<keyframe>.prompt-2.md` where needed.
- **Done when:** every keyframe is ACCEPTED.

## Procedure

1. **Resume** when the stills have landed.
2. **Check each still** against the 7 checks in `02 - content/05 - writing/08 - visuals/00 - ENTRY.md`, plus: **C8**, it matches the continuity references (same product, palette, light); **C9**, an -a/-b pair frames the same scene so motion can connect them.
3. **Failures:** a revised prompt naming the failed check; resend (H4); hold. After 3 rounds on one keyframe, ask the operator (H2).

## Output template

Statuses in the index: RETURNED → ACCEPTED, or REVISED n (check failed).

## Worked example

*(illustrative)* `K-V2a-S3-a · REVISED 1 · C8: the stone came back emerald-cut; continuity says oval`.

## Self-check

- [ ] Is every keyframe ACCEPTED, with every failure re-prompted?

## Traps

- **Accepting a pair that doesn't connect.** The motion model will warp between them.
