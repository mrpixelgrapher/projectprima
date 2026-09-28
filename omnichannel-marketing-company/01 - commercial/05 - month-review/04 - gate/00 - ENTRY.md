# 04 · Gate

**Purpose:** close the review: publish the month's results, update the engagement if an upsell was accepted, and move on to the month's advance invoice.

## Contract

- **Reads:** `15-month-review/*.md`.
- **Writes:** the `## 15-month-review` section of `CONTEXT.md`; `15-month-review/gate.md`; a row in `clients/<client>/results.md`; `clients/<client>/engagement.md` (only if an upsell was accepted).
- **Done when:** the task has advanced.

## Procedure

1. **Checks, in order:**

   | # | Check | On failure |
   |---|---|---|
   | MR1 | The results reply is logged, every number sourced or "not reported" | 02 - review |
   | MR2 | Every objective and test has a status by its rule | 02 - review |
   | MR3 | The upsell file shows a trigger and its outcome, or "no upsell" with reasons | 03 - upsell |
   | MR4 | The engagement continues this month (or the operator's renewal decision is in `from-operator/`) | 02 - review |

2. **Publish:** append the month's row to `clients/<client>/results.md`. If an upsell was accepted: update `engagement.md` (old version to `versions/` first), including its Includes row.
3. **Carry forward** (at most 8 bullets): the month; numbers vs objectives; test results; more of / less of; upsell outcome; open invoices.
4. **Write `gate.md`** (five-line format). If an accepted upsell changes what the route includes, add the sixth line `Includes: <items>` so the task follows it. Then `task.py advance <task-id>`.

## Self-check

- [ ] Does the results row cite this task's reply file?

## Traps

- **An accepted upsell that the route ignores.** Video added this month needs `Includes: video` here.
