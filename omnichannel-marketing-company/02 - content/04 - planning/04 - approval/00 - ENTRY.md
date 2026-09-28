# 04 · Approval

**Purpose:** get the client's yes on the month before anything is written: the topics, the pieces and the dated calendar.

## Contract

- **Reads:** `24-planning/01-month-plan.md`, `02-calendar.md`; `00 - control/01 - law/HANDOFFS.md` (H1).
- **Writes:** `24-planning/04-plan-for-client.md` (the send unit); after the reply, `24-planning/05-approval.md`.
- **Done when:** the reply is in `from-client/24-planning-plan-reply.md`, and `05-approval.md` records APPROVED, or APPROVED WITH CHANGES with the changes applied to the plan, calendar and briefs.

## Procedure

1. **Write the plan for the client,** in their language, without internal IDs: the month; what we learned last month (month route: 3 lines, with the numbers); the topics; each piece as its question and where it leads; the calendar as a simple table (date, channel, what posts); what we need from them (assets, facts to check, a date that matters); "reply 'approved', or tell us what to change".
2. **Send and hold** (H1): `task.py hold <task-id> --on "H1 client: 24-planning/04-plan-for-client.md"`. A rehearsal is not sent.
3. **When the reply lands,** resume and apply it:

   | Reply | Action |
   |---|---|
   | APPROVED | Record it; go to the gate |
   | Changes | Apply each to the plan, calendar and the affected briefs; log each with the client's quote; if a piece changes its question, its brief is rewritten |
   | No reply after 5 days | The operator sends one reminder; the task stays on HOLD |

## Output template

`05-approval.md`:

    # Plan approval — <task id>
    Reply: <date> · Outcome: APPROVED / APPROVED WITH CHANGES
    | Change | The client's words | Applied to |

## Worked example

*(illustrative)* Reply: "approved, but move the ordering post before the 5th, our HR contacts plan early" → P3's first date moved to 2026-11-04 in the calendar and its brief.

## Self-check

- [ ] Is every change applied to every file it touches?

## Traps

- **Writing before the yes.** Writing starts only after `05-approval.md` says APPROVED.
