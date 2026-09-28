# 02 · Review

**Purpose:** turn the client's numbers into a judgment against the objectives: what worked, what didn't, and what the next month should do more or less of. Also confirm the engagement is live and see what is owed.

## Contract

- **Reads:** `from-client/15-month-review-results-reply.md`; `clients/<client>/strategy.md` (objectives); `clients/<client>/performance.md` (tests running); `clients/<client>/results.md` (earlier months); `clients/<client>/engagement.md` (term); `01 - commercial/ledgers/invoices.md`.
- **Writes:** `15-month-review/02-review.md`.
- **Done when:** every tracked number is logged with its source; each objective has a status; each test running has a result; the engagement term and open invoices are stated.

## Procedure

1. **Resume** the task: `task.py resume <task-id> --note "results reply"`.
2. **Log the numbers** exactly as the client reported them. A number the client didn't give is "not reported", never estimated.
3. **Objectives.** For each objective in `strategy.md`: on track / behind / ahead, by the rule the objective states. No rule → "no rule: strategy to add one" (a lesson).
4. **Tests.** For each test in `performance.md`: which variant won, by the metric the test names, or "inconclusive" when the difference is under the test's threshold.
5. **More / less.** From the objectives, tests and the client's answer to the open question: at most 3 "more of" and 3 "less of", each citing a number or the client's words.
6. **Engagement and money.** The term: continuing, or ends this month (then the operator decides renewal: hold with H2). Open invoices from the ledger: any unpaid past its due date is listed for the operator.

## Output template

    # Month review — <client> · <month>
    ## Numbers
    | Number | Value | Source |
    ## Objectives
    | Objective | Status | Rule | Evidence |
    ## Tests
    | Test | Result | Evidence |
    ## More of / less of
    ## Engagement and money
    Term: … · Open invoices: …

## Self-check

- [ ] Is every number sourced to the client's reply?
- [ ] Does every "more of / less of" cite a number or the client?

## Traps

- **Explaining away a miss.** A behind objective is recorded as behind; the reason goes in "less of" or a lesson.
