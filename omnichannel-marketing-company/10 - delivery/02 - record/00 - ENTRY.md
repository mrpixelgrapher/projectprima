# 02 · Record

**Purpose:** write down what actually happened (what shipped, what it cost, how the client responded) and, for a proof run, whether the offer is proven. Then append the company ledgers, so the company's claims rest on rows, not memory.

## Contract

- **Reads:** `TASK.md` (History); `09-packaging/02-kit-index.md`; `client/receipt.md` (if any); `03-strategy/04-objectives.md`; `10 - delivery/ledgers/*.md`.
- **Writes:** `10-delivery/02-record.md`; one row each in `10 - delivery/ledgers/delivery-ledger.md` and `client-ledger.md`; and, for a proof run, a row in `proof-index.md`.
- **Done when:** the record is written and the ledger rows are appended.

## Procedure

1. **What shipped:** pieces × channels, and COMPLETE or PARTIAL per piece (from the kit index).
2. **Cost:** from History, the date each node was entered and left, and the days spent per node. Add effort notes (research depth, review rounds, returns) where the History shows them.
3. **Client response:** a quote from `client/receipt.md`, or "no response by <date>". Wait up to 14 days after sending before writing "no response".
4. **Is this a proof run?** It is if `10 - delivery/ledgers/proof-index.md` has no row for this offer (the frame's package type) yet.
5. **Disposition** (proof runs only):

   | Disposition | Rule |
   |---|---|
   | PROVEN | Every piece passed review; the package was delivered (PARTIAL only because images are waiting counts); the client confirmed receipt and that they can use it |
   | PARTIAL | Delivered, but some pieces or channels can't be used as delivered, or the client's response is missing |
   | NOT PROVEN | Not delivered, or the client rejected it |

6. **Objectives:** note the review date. Results are added to the record when the client reports them.
7. **Append the ledger rows,** using the formats in `10 - delivery/ledgers/00 - ENTRY.md`. For `rehearsal` tasks, the rows carry `kind: rehearsal` and never count as proof.

## Output template

    # Record — <task id>
    ## What shipped
    ## Cost (per node, from History)
    | Node | Entered | Left | Days | Notes |
    ## Client response
    ## Disposition (proof run only): PROVEN | PARTIAL | NOT PROVEN — reason
    ## Objectives: review on …

## Self-check

- [ ] Does every cost row come from History?
- [ ] Does the disposition follow the table?
- [ ] Are the ledger rows appended, with the correct kind?

## Traps

- **"The client seemed happy."** Quote them, or write "no response".
- **A rehearsal counted as proof.**
