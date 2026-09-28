# 04 · Gate

**Purpose:** confirm every number traces to a rate, an hour and a cost, publish the client's rates, and move to the proposal.

## Contract

- **Reads:** `13-pricing/*.md`.
- **Writes:** the `## 13-pricing` section of `CONTEXT.md`; `13-pricing/gate.md`; `clients/<client>/rates.md`.
- **Done when:** `gate.md` says `VERDICT: PASS`, the rates are published, and the task has advanced.

## Procedure

1. **Checks, in order:**

   | # | Check | On failure |
   |---|---|---|
   | PR1 | Every rate, currency, tax and unit cost has a source | 01 - rates |
   | PR2 | Every costed unit has a line | 02 - costs |
   | PR3 | Every sub-task has a line; blocks re-add; the budget check is written | 03 - lines |

2. **Carry forward** (at most 6 bullets):

       ## 13-pricing
       - Currency · tax: … [13-pricing/01-rates.md]
       - Setup total: … [13-pricing/03-lines.md]
       - Monthly base total: … · budget check: … [13-pricing/03-lines.md]
       - Add-ons per month: <D: total>, … [13-pricing/03-lines.md]
       - Payment: setup on acceptance; month 50% before, 50% on delivery [13-pricing/03-lines.md]

3. **Publish** `clients/<client>/rates.md` from `01-rates.md` (the old one, if any, to `clients/<client>/versions/rates-<YYYY-MM-DD>.md` first).
4. **Write `gate.md`** (the five-line format in `00 - control/01 - law/TASK_CONTRACT.md` §2), then run `python3 "00 - control/02 - tools/task.py" advance <task-id>`.

## Self-check

- [ ] Can every total be traced to lines, and every line to a sub-task?

## Traps

- **Publishing rates the operator hasn't set.** The client file holds only operator-sourced rates.
