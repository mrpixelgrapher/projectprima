# 03 · Gate

**Purpose:** confirm every keyframe is accepted, and advance to motion.

## Contract

- **Reads:** `33-stills/00-still-index.md`.
- **Writes:** the `## 33-stills` section of `CONTEXT.md`; `33-stills/gate.md`.
- **Done when:** the task has advanced.

## Procedure

1. **Checks:** ST1 every keyframe in the continuity list has a prompt (else 01 - prompts); ST2 every keyframe is ACCEPTED (else 02 - check).
2. **Carry forward** (at most 3 bullets): keyframes accepted; revision rounds; anything the operator decided.
3. **Write `gate.md`** (five-line format), then `task.py advance <task-id>`.

## Self-check

- [ ] Is every keyframe accepted?

## Traps

- **Moving on with one still missing.** Its transitions can't be generated.
