# 03 · Results plan

**Purpose:** fix, before the month runs, exactly when results come back and which numbers, so the next month's review has data. Results are tracked only on retainers.

## Contract

- **Reads:** `clients/<client>/engagement.md` (type); `23-performance/05-tracking.md` (the report list); `26-packaging/02-schedule.md` (the month's dates).
- **Writes:** `28-delivery/03-results-plan.md`.
- **Done when:** a retainer has the date results are asked for and the list of numbers; a one-off says "one-off: results are not tracked".

## Procedure

1. **Type = one-off:** write "one-off: results are not tracked (design lock)". Done.
2. **Type = retainer:** the ask date is day 20 of the month being run (or the engagement's day). The numbers are the tracking stage's report list, unchanged. Name the month task that will ask: the next month task, opened at `01 - commercial/07 - billing-delivery/02 - close/`.

## Output template

    # Results plan — <task id>
    Type: retainer / one-off
    Ask on: <date> · by: the month task for <month>
    Numbers: …

## Self-check

- [ ] Is the list exactly the tracking stage's report list?

## Traps

- **Adding numbers here.** Changing what is measured is performance's job.
