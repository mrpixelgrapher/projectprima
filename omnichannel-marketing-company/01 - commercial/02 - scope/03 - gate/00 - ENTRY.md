# 03 · Gate

**Purpose:** confirm the scope is complete and countable, carry it forward, and move the task to pricing (or, on the direct route, publish the engagement and move straight to discovery).

## Contract

- **Reads:** `12-scope/01-deliverables.md`, `12-scope/02-breakdown.md`; `TASK.md` (`route`); `11-intake/06-slot-board.md` (F4).
- **Writes:** the `## 12-scope` section of `CONTEXT.md`; `12-scope/gate.md`; on the direct route, `clients/<client>/engagement.md`.
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

3. **Direct route only** (`route` in `TASK.md` is `direct`: no pricing, proposal or billing). Do here what the proposal gate does on the engagement route:
   - Publish `clients/<client>/engagement.md` (old one to `versions/` first): Type (`one-off`, or `retainer` if the shape is retainer), Accepted (today, "direct: no commercial terms, operator directive I-013"), Term, Includes, Payment ("none: direct route"), and the deliverables per month from `01-deliverables.md` (setup and monthly; add-on candidates listed as not included).
   - Includes: `video` if a video deliverable is in the monthly list; `publishing` if F4 = CONTENT+PUBLISHING. Otherwise `—`.
4. **Write `gate.md`** (the five-line format in `00 - control/01 - law/TASK_CONTRACT.md` §2; on the direct route, add the sixth line `Includes: <items or —>`), then run `python3 "00 - control/02 - tools/task.py" advance <task-id>`.

## Self-check

- [ ] Were the checks run in order?
- [ ] Does the carry-forward give hours, not prices? (Prices belong to pricing.)

## Traps

- **Pricing here.** A number with a currency in scope skips the client's rates.
