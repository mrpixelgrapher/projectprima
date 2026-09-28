# 02 · Findings

**Purpose:** turn what came back (the ARENA dossier and the client's answers) into facts anyone can check: a source ledger, a finding per research question with its sources, and the slot board updated with every answer. The brief is built only from these.

## Contract

- **Reads:** `21-discovery/arena-dossier-1/` (as returned); `from-client/21-discovery-questions-round-N-reply.md`; `21-discovery/arena-request-1.md`; `11-intake/06-slot-board.md`.
- **Writes:** `21-discovery/02-slot-board.md`, `21-discovery/03-sources.md` (the source ledger), `21-discovery/04-findings.md`.
- **Done when:** every RQ in the request has a finding or "not found in the dossier"; every source used has a ledger row with all seven fields; every contradiction is listed; every client answer is in the slot board.

## Procedure

1. **Resume** the task once every return in `01-requests.md` has landed: `task.py resume <task-id> --note "dossier 1 and client round N"`. Mark each request "returned <date>" in `01-requests.md`.
2. **Check the dossier is complete.** Every RQ and every sampled channel has a section. A missing section → write `arena-request-2.md` for just the gaps, hold again (H3), and continue with what you have only after it returns.
3. **Log the sources.** One row in `03-sources.md` per source the dossier cites that you use:

   | Field | Rule |
   |---|---|
   | ID | L-001, L-002… (continues across the task and the client) |
   | url / path | Where the source is, as the dossier gives it |
   | date read | The date the dossier gives, or the dossier's date |
   | claim | What the source says: a quote, or a close paraphrase marked (para) |
   | category | survey · official / regulator · platform documentation · company site · practitioner write-up · news · review or forum |
   | confidence | **high:** official, or primary data, or 2+ independent sources agree · **medium:** one credible secondary source · **low:** anecdote, or no stated basis. Set it yourself by this rule, whatever the dossier says |
   | implication | What it means for this client, in one line |

4. **Surface contradictions.** When sources disagree, log both and list the pair: what differs, which is more credible and why, or "unresolved". Never keep only the convenient one.
5. **Write each finding:** 1–3 sentences answering the RQ, citing L-IDs. Nothing credible in the dossier → "not found in the dossier", and route it: a second ARENA request (if strategy needs it) or an open item.
6. **Update the slot board** from intake's: every client answer (quoted, cited [client: 21-discovery-questions-round-N-reply CQn]) and every finding that fills a slot ([src: L-…]). Apply the status rules in `00 - control/01 - law/BRIEF_SLOTS.md`.

## Output templates

`03-sources.md`:

    # Source ledger — <task id>
    | ID | url / path | date read | claim | category | confidence | implication |

`04-findings.md`:

    # Findings — <task id>
    ## Findings
    ### RQn. <question>
    <1–3 sentences> [L-…]
    ## Contradictions
    | Sources | What differs | Resolution |
    ## Not found
    | RQ | Route |

`02-slot-board.md`: the template of `01 - commercial/01 - intake/05 - answers/00 - ENTRY.md`, updated.

## Worked example

Gemstone task *(illustrative)*:

    ### RQ1. How do IT and consulting firms of 50–300 people choose and buy corporate gifts?
    Gifts are usually chosen by HR or the office admin, with finance approving above a per-order limit.
    Festival orders are placed 4–6 weeks ahead. [L-003, L-004, L-007]

Ledger row: `| L-003 | https://example.org/gifting-survey | 2026-10-02 | "61% of HR leads choose festival gifts" | survey | medium | HR is the first reader; pieces should speak to HR needs |`

## Self-check

- [ ] Is every RQ answered or routed, with no finding lacking an L-ID?
- [ ] Does every ledger row have all seven fields, with confidence set by the rule?
- [ ] Is every contradiction listed?
- [ ] Is every client answer quoted into the slot board?

## Traps

- **Copying the dossier's summary as a finding.** A finding cites the sources, not the dossier's conclusion.
- **Trusting the dossier's confidence.** Set it by the rule above.
- **Filling a gap from general knowledge.** If the dossier doesn't say it, it is "not found".
