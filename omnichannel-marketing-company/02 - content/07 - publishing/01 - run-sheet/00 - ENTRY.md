# 01 · Run sheet

**Purpose:** give the operator one ordered list that schedules the whole month without opening anything but the kit.

## Contract

- **Reads:** `26-packaging/02-schedule.md`; the kit; `clients/<client>/engagement.md`; `00 - control/01 - law/HANDOFFS.md` (H2).
- **Writes:** `27-publishing/01-run-sheet-for-operator.md`.
- **Done when:** every post in the schedule is a row on the run sheet, and the task is on HOLD for the operator's confirmation.

## Procedure

1. **One row per post,** in date and time order: channel, account, date and time, the kit file, the images or video in order, where the link goes, and the first comment's text if any.
2. **Before the first row:** "Check each account is logged in; check the destination page works (submit it once)."
3. **Hold (H2):** `task.py hold <task-id> --on "H2 operator: schedule every post in 27-publishing/01-run-sheet-for-operator.md"`. The operator replies in `from-operator/27-publishing-run-sheet.md`: for each row, "scheduled" (with the scheduler's confirmation) or "could not" (with why).

## Output template

    # Run sheet — <client> · <month>
    Before you start: …
    | # | Date | Time | Channel · account | Kit file | Media (in order) | Link placement | First comment |
    Reply per row: scheduled / could not — why

## Worked example

*(illustrative)* `| 7 | 2026-11-10 | 12:30 | Instagram · @koragifts | kit/03-instagram/2026-11-10-P2-real-or-fake.md | images/S-P2-instagram-carousel-1…7 | bio | — |`

## Self-check

- [ ] Does every scheduled post appear once, in order?

## Traps

- **Posting now what is dated later.** The schedule is the plan the client approved.
