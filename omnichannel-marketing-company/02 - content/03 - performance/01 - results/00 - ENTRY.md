# 01 · Results

**Purpose:** fix the starting point the design works from: on a first month, the baseline; on every later month, what last month's numbers and tests showed.

## Contract

- **Reads:** engagement route: `21-discovery/07-client-brief.md` (GOAL, CHANNELS: current numbers), `22-strategy/05-objectives.md`. Month route: `15-month-review/02-review.md`, `clients/<client>/results.md`, `clients/<client>/performance.md`.
- **Writes:** `23-performance/01-results.md`.
- **Done when:** the file states the baseline (or "no baseline: this month establishes it"), and, on a month route, every test's result and the "more of / less of" list carried from the review.

## Procedure

1. **Which route?** Read `route` in `TASK.md`.
2. **Engagement:** copy each objective's baseline with its source. A metric with no baseline is marked "month 1 establishes it", and its target waits for the first review.
3. **Month:** copy from the month review, without re-judging: the numbers vs objectives, each test's result, and the "more of / less of" list. Add the trend across months from `results.md` (up, flat or down per objective, over the last 3 months).
4. **Decisions for this month** (month route), by rule:

   | Result | Decision |
   |---|---|
   | A test variant won by its threshold | Make it the default; retire the loser |
   | A test was inconclusive | Run it one more month with the same variants, or drop it if it was already extended once |
   | An objective is behind 2 months running | The conversion stage must change the weakest link (step 3 there) |
   | An objective is ahead | Keep the design; the upsell was already weighed at the review |

## Output template

    # Results — <task id>
    Route: engagement / month · Month: …
    ## Baseline or last month
    | Objective | Baseline / last month | Target | Status | Trend | Source |
    ## Tests
    | Test | Result | Decision |
    ## More of / less of (from the review)

## Worked example

*(illustrative)* Month 2: O1 enquiries 3 vs a monthly target of 5, behind; test T1 (price-in-headline cover vs question cover): price-in-headline won by 34% saves → default.

## Self-check

- [ ] Is every number sourced to the brief, the review or `results.md`?
- [ ] Does every test have a decision by the rule table?

## Traps

- **Re-judging the review.** The review decided; this stage acts on it.
