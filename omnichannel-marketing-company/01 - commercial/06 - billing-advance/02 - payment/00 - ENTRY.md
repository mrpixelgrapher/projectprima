# 02 · Payment

**Purpose:** start content work only once the advance is paid, as the terms say.

## Contract

- **Reads:** `16-billing-advance/01-invoice-for-client.md`; `from-operator/16-billing-advance-payment.md`.
- **Writes:** `16-billing-advance/02-payment-for-operator.md`; a `paid` row in `01 - commercial/ledgers/invoices.md`.
- **Done when:** the operator has confirmed payment (amount and date), and the ledger shows it paid.

## Procedure

1. **Ask:** write `02-payment-for-operator.md`: the invoice number, the amount, "Reply with the date and amount received". Hold: `task.py hold <task-id> --on "H2 operator: payment of <invoice>"`.
2. **When it lands,** resume, and compare the amount received with the invoice total:

   | Received | Action |
   |---|---|
   | the full total | Append a `paid` row to the ledger; go to the gate |
   | less | Record the shortfall; the operator decides (H2) whether work starts |
   | nothing after 7 days | The operator sends a reminder; the task stays on HOLD |

3. **Rehearsal tasks:** the operator writes "rehearsal: no payment"; the ledger row says `rehearsal`.

## Output template

    # Payment check — <invoice>
    Amount due: … · Please reply: date received, amount received.

## Self-check

- [ ] Is the payment confirmed by the operator, not assumed?

## Traps

- **Starting work on a promise.** "They said they'll pay tomorrow" is not a payment.
