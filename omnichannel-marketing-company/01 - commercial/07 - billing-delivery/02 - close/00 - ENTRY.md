# 02 · Close

**Purpose:** make the client's history complete, and keep a retainer moving: next month's task opens here.

## Contract

- **Reads:** `TASK.md`; `28-delivery/02-record.md`; `clients/<client>/engagement.md`; the invoices of this task.
- **Writes:** `17-billing-delivery/02-close.md`; a row in `clients/<client>/history.md`; for a continuing retainer, a new month task (through `task.py new`).
- **Done when:** the history row is written, and either next month's task exists or the reason there is none is stated.

## Procedure

1. **History row:** task, route, opened, closed (today), shipped (from the record), invoices (numbers), outcome.
2. **Next month.**

   | `engagement.md` | Action |
   |---|---|
   | Type = retainer and the term continues | Open the next month: `python3 "00 - control/02 - tools/task.py" new --route month --client <client> --month <YYYY-MM> --kind <this task's kind>`, where `<YYYY-MM>` is the month after the one this task delivered. The month task starts at `05 - month-review/` |
   | Type = one-off, or the term has ended | No next task. If the term ended, append a row to `ledgers/clients.md` (status ended) |

## Output template

    # Close — <task id>
    History row written: yes
    Next: T-… opened for <month> / none — <reason>

## Self-check

- [ ] Is the next month the one after the month this task delivered?

## Traps

- **Opening the same month twice.** The tool refuses a duplicate id; check `task.py status` first.
