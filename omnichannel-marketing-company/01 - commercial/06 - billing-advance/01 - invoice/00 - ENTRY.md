# 01 · Invoice

**Purpose:** issue an invoice the client can check line by line against the work they accepted.

## Contract

- **Reads:** `clients/<client>/engagement.md`; `clients/<client>/rates.md`; the accepted proposal's lines (`14-proposal/` and `13-pricing/03-lines.md` in the engagement task, found in the task itself or in `clients/<client>/done/`); `01 - commercial/billing-profile.md`; `01 - commercial/ledgers/invoices.md` (the last number used).
- **Writes:** `16-billing-advance/01-invoice-for-client.md`; an `issued` row in `01 - commercial/ledgers/invoices.md`.
- **Done when:** the invoice carries every required field, re-adds to its total, is sent (H1), and is logged.

## Procedure

1. **Billing profile.** If any row of `billing-profile.md` is "—", hold on H2: write `16-billing-advance/01-billing-profile-for-operator.md` naming the empty rows; `task.py hold <task-id> --on "H2 operator: 01 - commercial/billing-profile.md incomplete"`. Continue when it is filled.
2. **What to bill.**

   | Route | Lines |
   |---|---|
   | engagement | Setup (every setup deliverable, itemised) + 50% of month 1 (base plus accepted add-ons) |
   | month | 50% of this month (base plus add-ons in the current `engagement.md`) |

3. **Number** it `<prefix>-<client>-<nnn>`, the next number for this client in the ledger.
4. **Itemise:** deliverable → sub-tasks (hours × rate) → costs → subtotal; then the 50% line where it applies; then tax per `rates.md`; then the total. Due date: on receipt.
5. **Send and log.** H1 (a rehearsal is not sent). Append an `issued` row to `ledgers/invoices.md`.

## Output template

    # Invoice <number>
    From: <legal name, address, tax registration> · To: <client label>
    Date: … · Due: on receipt · Task: <task id> · Period: <month or setup>
    | Deliverable | Work (sub-task · hours × rate) | Costs | Amount |
    Subtotal · 50% advance (month) · Tax (…) · **Total**
    Pay to: <payment details>

## Self-check

- [ ] Does every line trace to the engagement and the price lines?
- [ ] Does it re-add to the total?
- [ ] Is it logged as issued?

## Traps

- **Billing the whole month in advance.** The terms say 50%.
