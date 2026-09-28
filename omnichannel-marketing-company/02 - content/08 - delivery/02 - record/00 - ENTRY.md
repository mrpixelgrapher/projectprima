# 02 · Record

**Purpose:** write down what actually happened: what shipped, how long each node took, what came back from the client. The delivery ledger and the effort table rest on these rows, not on memory.

## Contract

- **Reads:** `TASK.md` (History); `26-packaging/01-kit-index.md`; `27-publishing/02-publish-log.md` (if any); `from-client/28-delivery-delivery-note-reply.md`; `12-scope/02-breakdown.md` (engagement) or `clients/<client>/engagement.md` (month); `from-operator/` (hours, if the operator tracked them).
- **Writes:** `28-delivery/02-record.md`; one row in `02 - content/08 - delivery/ledgers/delivery-ledger.md`.
- **Done when:** the record has what shipped, the time per node from History, the client's response, and the ledger row is appended.

## Procedure

1. **What shipped:** pieces × channels, stills, videos; each channel folder COMPLETE or PARTIAL (from the kit index); posts scheduled or live (from the publish log).
2. **Time per node:** from History, the date each node was entered and left, and the days spent, including days on HOLD and what the hold waited for. Where the operator tracked hours, add them (else "—").
3. **Effort against the table:** for each deliverable, the hours the breakdown estimated and the actual hours where tracked. A difference over 25% is flagged for lessons.
4. **Client response:** the receipt, quoted, or "no receipt by <date>".
5. **Ledger:** append the row (a rehearsal task's row says `rehearsal`).

## Output template

    # Record — <task id>
    ## What shipped
    ## Time per node (from History)
    | Node | Entered | Left | Days | Of which on HOLD (waiting for) | Hours (if tracked) |
    ## Effort against the table
    | Deliverable | Estimated h | Actual h | Difference |
    ## Client response

## Self-check

- [ ] Does every time row come from History?
- [ ] Is the ledger row appended with the correct kind?

## Traps

- **"The client seemed happy."** Quote them, or write "no receipt".
