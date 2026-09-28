# 01 · Results

**Purpose:** get the numbers for the month being run, as the client sees them, so the review and the optimisation rest on data and not on impressions.

## Contract

- **Reads:** `clients/<client>/performance.md` (what to measure, from its tracking section); `clients/<client>/engagement.md`; the previous task in `clients/<client>/done/` (what shipped last); `00 - control/01 - law/HANDOFFS.md` (H1).
- **Writes:** `15-month-review/01-results-for-client.md`.
- **Done when:** the request is sent on its date and the task holds for the reply, or the reply has landed in `from-client/15-month-review-results-reply.md`.

## Procedure

1. **Date.** Results are asked for on day 20 of the month being run (the engagement may name another day). If today is earlier, the request is still written now; the hold names the send date.
2. **Write the request:** the exact numbers to report, copied from the tracking section of `performance.md` (e.g. destination visits, sign-ups or enquiries, the top 3 posts by saves or shares per channel), where each is found, and the period. Keep it to what the client can copy from their dashboards in 10 minutes. Ask one open question: "Anything you want more of, or less of, next month?"
3. **Send and hold** (H1): `task.py hold <task-id> --on "H1 client: 15-month-review/01-results-for-client.md (send on <date>)"`.

## Output template

    # Your numbers for <month>
    Period: <from> – <to>
    | Number | Where to find it | Your number |
    Anything you want more of, or less of, next month?

## Self-check

- [ ] Is every number requested one the tracking plan defines?
- [ ] Does the hold name the send date?

## Traps

- **Asking for everything.** A long request gets no reply. Only the tracked numbers.
