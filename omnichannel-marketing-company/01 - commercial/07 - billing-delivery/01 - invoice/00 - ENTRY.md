# 01 · Invoice

**Purpose:** bill the second half of the month's work once it has been delivered.

## Contract

- **Reads:** `28-delivery/02-record.md` (what shipped); `16-billing-advance/01-invoice-for-client.md` (what was billed in advance); `clients/<client>/rates.md`; `01 - commercial/billing-profile.md`; `01 - commercial/ledgers/invoices.md`.
- **Writes:** `17-billing-delivery/01-invoice-for-client.md`; an `issued` row in `ledgers/invoices.md`.
- **Done when:** the invoice is complete, re-adds, is sent (H1) and logged.

## Procedure

1. **Bill the remaining 50%** of the month's fee, with the same itemisation as the advance invoice, and reference the advance invoice number.
2. **Adjust only for what didn't ship.** If the record shows a deliverable not delivered (e.g. an image slot still waiting on the image factory at delivery), bill it when it ships, on a later invoice, and say so on this one. Never bill for undelivered work.
3. **Due date:** 7 days from issue, unless the engagement says otherwise.
4. **Send (H1) and log** the `issued` row. Payment of this invoice is not waited on here: `05 - month-review/` checks it next month.

## Output template

Same as `01 - commercial/06 - billing-advance/01 - invoice/00 - ENTRY.md`, with a line "Advance invoiced: <number>" and "Not yet delivered, billed later: …".

## Self-check

- [ ] Does it bill only what the record shows delivered?

## Traps

- **Billing 50% of an unfinished month.** Hold back the lines for what hasn't shipped.
