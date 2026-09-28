# 01 · Package

**Purpose:** decide exactly what is offered: the engagement type, a base package that fits the client's budget, the add-ons, and what the route must include (video, publishing).

## Contract

- **Reads:** `CONTEXT.md` (`## 11-intake` to `## 13-pricing`); `12-scope/01-deliverables.md`; `13-pricing/03-lines.md`; `clients/<client>/profile.md`.
- **Writes:** `14-proposal/01-package.md`.
- **Done when:** the type, the base deliverables with their monthly total, the add-ons with prices, the includes, the term and the payment schedule are all stated, and the base fits the budget (or the gap is stated for the operator).

## Procedure

1. **Type.** From the scope's engagement shape: retainer → offer the retainer; one-off → offer the one-off; both → offer the retainer as the main option and the one-off as the alternative.
2. **Base package.** Start from the monthly base. While its total is over the monthly budget, move the monthly deliverable with the lowest priority to the add-ons. Priority (keep first): core pieces → destination pieces → the channel the client already runs → other channels → video → publishing. Never remove the core pieces: if the core alone is over budget, reduce its quantity to the lowest in the cadence table and state the gap for the operator.
3. **Add-ons.** Every add-on candidate from scope, and every deliverable moved out of the base, with its monthly price from `03-lines.md`.
4. **Includes.** `video` if any base deliverable is video; `publishing` if F4 = CONTENT+PUBLISHING and publishing is in the base. Otherwise `—`. (An add-on accepted later changes the includes through `05 - month-review/`.)
5. **Term.** Retainer: rolling monthly, starting the month after acceptance, unless the client named a period. One-off: the setup plus one month.
6. **Payment schedule** from `03-lines.md`: setup on acceptance; each month 50% before work starts, 50% on delivery.

## Output template

    # Package — <task id>
    Type: retainer / one-off / retainer (main) + one-off (alternative)
    Term: … · Includes: … · Currency: …
    ## Base (per month)
    | D | Deliverable | Channel | Qty | Price |
    Monthly base total (incl. tax): … · Budget: … · Fit: within / over by … (operator to decide)
    ## Setup (once)
    | D | Deliverable | Price |
    ## Add-ons (per month)
    | D | Deliverable | Qty | Price |
    ## Payment schedule
    | When | Amount |

## Worked example

*(illustrative)* Budget 40,000 a month; monthly base 52,000 → the LinkedIn variants (lowest priority in the base) move to add-ons → base 38,500, within budget.

## Self-check

- [ ] Were deliverables moved out of the base by the priority order, never the core?
- [ ] Is every price the block total from `03-lines.md`?
- [ ] Are the includes stated?

## Traps

- **Discounting to fit.** Cutting a price instead of moving a deliverable breaks the link between price and work.
- **Silent add-ons.** A channel the client asked for that disappears from the base without appearing as an add-on.
