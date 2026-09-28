# 01 · Join

**Purpose:** bring every piece's child task inside the parent, so the parent becomes the single, complete record of the job. Then report what each piece carries into the kit.

## Contract

- **Reads:** the parent's `TASK.md` (the `children` field); each child's `08-shaping/` and `07-review/01-review-report.md`.
- **Writes:** `09-packaging/01-join-report.md`, in the parent. The operator moves the children to `09-packaging/pieces/<child-id>/`.
- **Done when:** every child is inside `09-packaging/pieces/`, and the report has one row per piece.

## Procedure

1. **Check readiness:** `python3 "00 - control/02 - tools/task.py" join <parent-id>`.
   - "NOT READY": stop. The parent keeps waiting, and `status` shows where each child is.
   - "READY": continue.
2. **Absorb the children:** `python3 "00 - control/02 - tools/task.py" join <parent-id> --absorb`. Each child folder moves into `09-packaging/pieces/`, and its History is kept.
3. **Write the join report.** One row per piece: the slug, its review round and SURPLUS, its channels, its image slots (and how many are waiting), and any "client to supply" items.
4. **Nothing is edited at packaging.** If a defect is found in a piece, record it in the report, set `gate.md` to HOLD with `waiting on: operator (defect in <piece>)`, and stop. Fixing a piece means sending it back through its nodes, which is the operator's call.

## Output template

    # Join report — <parent id>
    | Piece | Review | SURPLUS | Channels | Image slots (waiting) | Client to supply |

## Self-check

- [ ] Is every child listed in `children` now under `pieces/`?
- [ ] Does every row carry its SURPLUS and image-slot count?

## Traps

- **Joining early.** Joining with a child still in review leaves the package short.
- **Quiet fixes.** Editing a piece's text here breaks its review record.
