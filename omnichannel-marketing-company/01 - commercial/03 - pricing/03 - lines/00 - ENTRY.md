# 03 · Lines

**Purpose:** compute every priced line and the totals, so the proposal can quote them and invoices can itemise them to the sub-task.

## Contract

- **Reads:** `12-scope/02-breakdown.md`; `13-pricing/01-rates.md`; `13-pricing/02-costs.md`.
- **Writes:** `13-pricing/03-lines.md`.
- **Done when:** every sub-task has a priced line; the setup, monthly base and each add-on have a subtotal, tax and total; the arithmetic checks.

## Procedure

1. **Price each sub-task:** hours × the rate for its kind. Keep the ST number, so an invoice line can be traced to the work.
2. **Group by deliverable,** add the deliverable's costs, and give each deliverable a subtotal.
3. **Block totals:** setup (once), monthly base, and each add-on (per month). Apply the tax treatment from `01-rates.md` to each block total.
4. **Payment schedule** (the company's terms): setup due on acceptance; each month 50% before work starts, 50% on delivery. Write the amounts.
5. **Budget check.** Compare the monthly base total with the client's budget (LIMITS in `clients/<client>/profile.md`). Write "within budget", or "over by X": the proposal then moves deliverables from the base to add-ons until the base fits.
6. **Check the arithmetic** by re-adding every block from its lines. Write "checked" with the date.

## Output template

    # Price lines — <task id>
    Currency: … · Tax: …
    ## Lines
    | ST | D | Sub-task | Kind | Hours | Rate | Amount |
    ## Per deliverable
    | D | Deliverable | Work | Costs | Subtotal |
    ## Blocks
    | Block | Subtotal | Tax | Total |
    | Setup (once) | … |
    | Monthly base | … |
    | Add-on <D> (per month) | … |
    ## Payment schedule
    | When | Amount |
    ## Budget check
    <within budget / over by …>
    Arithmetic: checked <date>

## Worked example

*(illustrative)* ST8 D1 writing 24 h × 1,200 = 28,800. D1 subtotal = research 18,000 + writing 36,000 + visual 5,400 + costs 720 = 60,120.

## Self-check

- [ ] Does every sub-task in the breakdown have a line?
- [ ] Does each block re-add to its lines?
- [ ] Is the budget check written?

## Traps

- **Rounding by feel.** Round only the final block totals, and say how.
- **Hiding costs in rates.** Costs are their own lines; the client sees them.
