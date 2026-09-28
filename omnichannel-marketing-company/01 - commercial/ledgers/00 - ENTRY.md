# ledgers

**Purpose:** the commercial department's memory, one row per event. These rows back every claim the company makes about its clients and money, and the phase ladder (`00 - control/02 - tools/derive_phase.py`) reads them. Tier 2: append rows only; never edit a logged row: add a correcting row instead.

| Ledger | One row per | Written at |
|---|---|---|
| `clients.md` | client (one row when they first accept; a new row when their status changes) | `04 - proposal/` gate; `07 - billing-delivery/` when an engagement ends |
| `proposals.md` | proposal version sent to a client | `04 - proposal/` (on sending) and its gate (on the outcome) |
| `invoices.md` | invoice issued, and one row when it is paid | `06 - billing-advance/`, `07 - billing-delivery/` |
| `upsells.md` | upsell offered | `05 - month-review/` |

Rows from `rehearsal` tasks carry `rehearsal` in the kind column, and never count as clients, revenue or proof.
