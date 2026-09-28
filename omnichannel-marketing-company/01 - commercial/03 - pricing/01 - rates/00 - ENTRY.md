# 01 · Rates

**Purpose:** fix the numbers pricing multiplies by: the client's rate for each kind of work, their currency and tax treatment, and the unit cost of anything paid for outside. Only the operator sets these.

## Contract

- **Reads:** `12-scope/02-breakdown.md` (the kinds of work used); `clients/<client>/rates.md`; `clients/<client>/profile.md` (where the client is); `00 - control/01 - law/HANDOFFS.md` (H2).
- **Writes:** `13-pricing/01-rates-for-operator.md` (when rates are needed); `13-pricing/01-rates.md`.
- **Done when:** `01-rates.md` has a rate for every kind of work in the breakdown, the currency, the tax treatment and every unit cost, each with its source (the operator's file, or the client's `rates.md`).

## Procedure

1. **Reuse or ask.**

   | Situation | Action |
   |---|---|
   | `clients/<client>/rates.md` has a rate for every kind in the breakdown, set within the last 12 months | Reuse it; go to step 3 |
   | Any kind is missing, or the rates are older than 12 months | Ask the operator (step 2) |

2. **Ask the operator** (H2). Write `13-pricing/01-rates-for-operator.md`: the client and where they are; the kinds of work in the breakdown with their total hours (so the operator sees the weight of each); the currency and tax treatment to confirm; the unit costs needed (per still from the image factory, per motion clip, any tool or service the deliverables need); and last time's rates for this client, if any. Then hold:

       python3 "00 - control/02 - tools/task.py" hold <task-id> --on "H2 operator: 13-pricing/01-rates-for-operator.md"

   The operator answers in `from-operator/13-pricing-rates.md`. Resume the task when it lands.
3. **Write `01-rates.md`** from the operator's file or the client's rates, every value with its source.

## Output template

    # Rates — <task id>
    Currency: … · Tax treatment: … (rate …%, applies to …) · Source: [operator: from-operator/13-pricing-rates.md]
    ## Rates per kind of work
    | Kind of work | Rate per hour | Source |
    ## Unit costs
    | Cost | Per | Amount | Source |

## Worked example

*(illustrative; the operator's numbers are never guessed)*

| Kind of work | Rate per hour | Source |
|---|---|---|
| research | 1,500 | [operator: from-operator/13-pricing-rates.md] |
| writing | 1,200 | [operator: from-operator/13-pricing-rates.md] |

Currency: INR · Tax treatment: GST 18% on the total · Unit cost: still (image factory) 40 per still.

## Self-check

- [ ] Does every kind of work in the breakdown have a rate with a source?
- [ ] Are the currency and tax treatment stated, with their source?
- [ ] Does every unit cost the deliverables need have an amount?

## Traps

- **A rate from memory or from another client.** Rates are per client and come from the operator.
- **Tax left for later.** An invoice without its tax treatment can't be issued; fix it here.
