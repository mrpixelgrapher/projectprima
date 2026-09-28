# 03 · Gate

**Purpose:** confirm every shot can be rendered and moved, and advance to stills.

## Contract

- **Reads:** `32-shots/*.md`.
- **Writes:** the `## 32-shots` section of `CONTEXT.md`; `32-shots/gate.md`.
- **Done when:** the task has advanced.

## Procedure

1. **Checks:** SH1 every frame has shots with every field, one camera move each, durations adding up (else 01 - shot-list); SH2 every recurring element has a reference and every keyframe is listed (else 02 - continuity).
2. **Carry forward** (at most 4 bullets): shots per video; keyframes to render (count); the look; stop-motion sequences.
3. **Write `gate.md`** (five-line format), then `task.py advance <task-id>`.

## Self-check

- [ ] Is the keyframe list complete?

## Traps

- **A shot with no keyframe.** It can't be rendered.
