# 07 · Gate

**Purpose:** confirm the strategy is complete, approved and consistent; carry it forward; publish it to the client folder; and advance to performance.

## Contract

- **Reads:** every file in `22-strategy/`; `from-client/22-strategy-strategy-reply.md`.
- **Writes:** the `## 22-strategy` section of `CONTEXT.md`; `22-strategy/gate.md`; `clients/<client>/strategy.md`.
- **Done when:** `gate.md` says `VERDICT: PASS`, the strategy is published, and the task has advanced.

## Procedure

1. **Run the checks in order.** Stop at the first failure.

   | # | Check | On failure |
   |---|---|---|
   | T1 | The position statement follows the template, and every difference has proof in hand | 01 - positioning |
   | T2 | 3–5 pillars, each with cited proof, an objection and a buyer stage; aware, considering and deciding all covered | 02 - messages |
   | T3 | One destination by the rule table, one action, a lead magnet or "none" with a reason | 03 - destination |
   | T4 | Every channel in the engagement has a complete row and a link to the destination; every buyer profile is reached | 04 - channels |
   | T5 | Every objective has a metric, baseline, target (client-given or approved), on-track rule and review | 05 - objectives |
   | T6 | `07-approval.md` records APPROVED, or APPROVED WITH CHANGES with the changes applied | 06 - approval |

2. **Write the carry-forward** (at most 10 bullets, each with its source):

       ## 22-strategy
       - Position: "<statement>" [22-strategy/01-positioning.md]
       - Promise: "<line>" [22-strategy/02-messages.md]
       - Pillars: P1 … · P2 … · P3 … [22-strategy/02-messages.md]
       - Destination: … · one action: … · lead magnet: … [22-strategy/03-destination.md]
       - Channels: … (long-form home: …) [22-strategy/04-channel-plan.md]
       - Objectives: O1 …, rule …, read … [22-strategy/05-objectives.md]
       - Approved on <date>; changes: … [client] [22-strategy/07-approval.md]

3. **Publish** the full approved strategy to `clients/<client>/strategy.md` (the old one to `versions/` first): `07-approval.md`, then `01-positioning.md`, `02-messages.md`, `03-destination.md`, `04-channel-plan.md` and `05-objectives.md`, in that order, each under a heading with its file name, with every change the client asked for already applied. Month tasks read their strategy from this file.
4. **Write `gate.md`** (the five-line format in `00 - control/01 - law/TASK_CONTRACT.md` §2), then run `python3 "00 - control/02 - tools/task.py" advance <task-id>`.

## Self-check

- [ ] Is the client's approval on file, verbatim?
- [ ] Does the carry-forward name the destination and every channel?

## Traps

- **Advancing on an implied yes.** T6 needs the reply.
- **A carry-forward without the pillars or the destination.** Performance and planning build from both.
