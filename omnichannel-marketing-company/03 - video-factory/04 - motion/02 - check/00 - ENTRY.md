# 02 · Check

**Purpose:** accept only clips that move the way the shot says and keep the product and look intact.

## Contract

- **Reads:** `34-motion/motion/` (prompts and clips); the shot lists; `32-shots/01-continuity.md`.
- **Writes:** statuses and notes in `34-motion/00-motion-index.md`; revised prompts `<T-id>.prompt-2.md`.
- **Done when:** every transition is ACCEPTED.

## Procedure

1. **Resume** when the clips have landed.
2. **Check each clip:** M1 it is next to its prompt, named by its T-id; M2 it starts on the start still and ends on the end still; M3 the camera move and subject motion are as written; M4 the duration matches (±0.3 s); M5 nothing warps, appears or changes that continuity fixes; M6 stop-motion reads as stepped, where asked.
3. **Failures:** a revised prompt naming the failed check; resend (H5); hold. After 3 rounds on one transition, ask the operator (H2): simplify the shot, or cut instead of moving.

## Output template

Statuses in the index: RETURNED → ACCEPTED, or REVISED n (check failed).

## Worked example

*(illustrative)* `T-V2a-3 · REVISED 1 · M5: the report's seal melted during the morph`.

## Self-check

- [ ] Is every transition ACCEPTED?

## Traps

- **Accepting a warped product.** The client's product must look like itself in every frame.
