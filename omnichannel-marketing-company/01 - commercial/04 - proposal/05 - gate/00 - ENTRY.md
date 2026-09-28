# 05 · Gate

**Purpose:** turn an accepted proposal into the client's engagement, fix the route's includes, and move the task to billing. A declined proposal closes the task.

## Contract

- **Reads:** `14-proposal/*.md`; `from-operator/14-proposal-signoff.md`; the client's reply.
- **Writes:** the `## 14-proposal` section of `CONTEXT.md`; `14-proposal/gate.md` (with the `Includes:` line); `clients/<client>/engagement.md`; a row in `01 - commercial/ledgers/clients.md` for a first acceptance.
- **Done when:** the task has advanced with the correct includes, or has been closed.

## Procedure

1. **If DECLINED:** run `python3 "00 - control/02 - tools/task.py" close <task-id> --reason "proposal declined: <client's words>"`. Stop.
2. **Checks, in order:**

   | # | Check | On failure |
   |---|---|---|
   | PP1 | The base fits the budget, or the operator approved the gap | 01 - package |
   | PP2 | The sent document matches the package, number for number | 02 - document |
   | PP3 | The operator's APPROVED is in `from-operator/` | 03 - sign-off |
   | PP4 | The acceptance quotes the client and lists the add-ons chosen | 04 - acceptance |

3. **Publish the engagement.** Fill `clients/<client>/engagement.md`: Type (`retainer` or `one-off`, exactly), Accepted, Term, Includes (e.g. `video, publishing`, or `—`), Payment, the deliverables per month (base plus chosen add-ons) and the add-ons not chosen with their prices. Move any previous version to `versions/` first.
4. **Ledger:** for a client's first acceptance, append a row to `ledgers/clients.md` (status active).
5. **Carry forward** (at most 6 bullets): type, term, deliverables per month in short, includes, monthly total and setup total, the acceptance quote.
6. **Write `gate.md`** in the five-line format (`00 - control/01 - law/TASK_CONTRACT.md` §2) **plus a sixth line**, `Includes: <items or —>`, matching the engagement. `task.py advance` copies it into the task, and the route follows it.
7. **Advance:** `python3 "00 - control/02 - tools/task.py" advance <task-id>`.

## Self-check

- [ ] Does `engagement.md` say `retainer` or `one-off` exactly, so month tasks can open?
- [ ] Does the `Includes:` line match the engagement?

## Traps

- **Includes forgotten.** Without `Includes: video`, the task never visits the video factory, and the videos the client bought are never made.
