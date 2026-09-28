# 03 · Upsell

**Purpose:** offer the client more only when the evidence or the client asks for it, priced from their own rates. Otherwise, record why not.

## Contract

- **Reads:** `15-month-review/02-review.md`; `clients/<client>/engagement.md` (add-ons not yet taken, with prices); `clients/<client>/rates.md`; `01 - commercial/02 - scope/02 - breakdown/effort-table.md`.
- **Writes:** `15-month-review/03-upsell.md`; when a trigger fires, `15-month-review/03-upsell-for-operator.md` and `03-upsell-for-client.md`; rows in `01 - commercial/ledgers/upsells.md`.
- **Done when:** no trigger fired (and the file says so), or the offer was signed off, sent and answered.

## Procedure

1. **Triggers** (any one fires an offer):

   | Trigger | Offer |
   |---|---|
   | The client asked for more (in the reply or at any time) | What they asked for, priced |
   | An objective is ahead for 2 months running on a channel | More volume on that channel |
   | A test showed a format that wins on a channel not in the base | That channel or format as an add-on |
   | Publishing is not included and the client reported they didn't post everything delivered | Publishing |

2. **Price it** from the engagement's add-on prices, or, for something new, from the effort table × the client's rates (show the lines).
3. **Sign-off, then offer.** H2 to the operator (`03-upsell-for-operator.md`; hold; `from-operator/15-month-review-upsell.md`), then H1 to the client (`03-upsell-for-client.md`; hold; `from-client/15-month-review-upsell-reply.md`). Log `offered` and the outcome in `ledgers/upsells.md`.
4. **No trigger:** write "No upsell this month", with each trigger and why it didn't fire.

## Output template

    # Upsell — <client> · <month>
    Trigger: … (evidence …) / none
    Offer: … · Price per month: … · Lines: …
    Operator: APPROVED / changes · Client: accepted / declined — "…"

## Self-check

- [ ] Does every offer cite its trigger and evidence?
- [ ] Was the operator's sign-off in place before the client saw it?

## Traps

- **Upselling on a bad month.** No trigger, no offer.
