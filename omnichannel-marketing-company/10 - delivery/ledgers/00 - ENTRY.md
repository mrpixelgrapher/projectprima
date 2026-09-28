# ledgers

**Purpose:** the company's memory of every job. Each task appends one row per ledger at `10 - delivery/02 - record/` and `03 - lessons/`. These rows are the evidence behind any claim the company makes about what it has delivered. Tier 2: append rows only; never edit a logged row, and add a correcting row instead.

| Ledger | One row per | Written at |
|---|---|---|
| `delivery-ledger.md` | delivered task | 02 - record |
| `client-ledger.md` | task, per client (a client's rows show their history) | 02 - record |
| `proof-index.md` | proof run (the first task of an offer) | 02 - record |
| `lessons-log.md` | task | 03 - lessons |

Rows from `rehearsal` tasks carry `rehearsal` in the kind column, and never count as proof or as delivery.
