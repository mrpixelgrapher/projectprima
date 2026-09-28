# 03 · Gate

**Purpose:** confirm the scope is complete and countable, carry it forward, and move the task to pricing.

## Contract

- **Reads:** `12-scope/01-deliverables.md`, `12-scope/02-breakdown.md`.
- **Writes:** the `## 12-scope` section of `CONTEXT.md`; `12-scope/gate.md`.
- **Done when:** `gate.md` says `VERDICT: PASS` and the task has advanced.

## Procedure

1. **Run the checks in order.** Stop at the first failure and go back to the stage named.

   | # | Check | On failure |
   |---|---|---|
   | SC1 | Every F3 IN family has deliverables; every ASK family has an add-on row; paid ads are excluded | 01 - deliverables |
   | SC2 | Every quantity follows the cadence table or a matching change rule | 01 - deliverables |
   | SC3 | Every deliverable has sub-tasks, each with one kind and hours from the effort table or an adjustment rule | 02 - breakdown |
   | SC4 | The totals add up | 02 - breakdown |

2. **Write the carry-forward** (at most 6 bullets, each with its source):

       ## 12-scope
       - Shape: one-off / retainer / both offered [12-scope/01-deliverables.md]
       - Setup: D-S… (<names>) · <hours> h [12-scope/02-breakdown.md]
       - Monthly base: <deliverables in short> · <hours> h [12-scope/02-breakdown.md]
       - Add-ons: <list> [12-scope/01-deliverables.md]
       - Excluded: paid ads; … [12-scope/01-deliverables.md]

3. **Write `gate.md`** (the five-line format in `00 - control/01 - law/TASK_CONTRACT.md` §2), then run `python3 "00 - control/02 - tools/task.py" advance <task-id>`.

## Self-check

- [ ] Were the checks run in order?
- [ ] Does the carry-forward give hours, not prices? (Prices belong to pricing.)

## Traps

- **Pricing here.** A number with a currency in scope skips the client's rates.
