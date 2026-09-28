# 02 · Research

**Purpose:** answer, with logged sources, the research questions whose conditions are now met. The brief then states facts about buyers, market, proof standards and rules that anyone can check.

## Contract

- **Reads:** `01-intake/05-research-questions.md`; `02-discovery/01-slot-board.md`, to see which conditions are met; `query-bank.md` in this folder.
- **Writes:** `02-discovery/02-sources.md` (the source ledger) and `02-discovery/03-findings.md`.
- **Done when:** every runnable RQ has a finding, or "not found" with where you searched; every source row has all six fields; every contradiction is listed.

## Procedure

1. **Build the run list.** For each RQ:
   - condition "unconditional", or its CQ answered → **run**;
   - otherwise → **carry**, and name the answer it waits for.

   If the client's answers raised new questions about the outside world, add them as new RQs (numbering continues). Use `query-bank.md` for questions every founder-led client needs.
2. **Write the lane map first,** at the top of `03-findings.md`. Group the runnable RQs into lanes: buyer, market, rules, channels. Lanes may be researched in parallel only after the map is written.
3. **Research each RQ** with the source categories it names. Aim for at least 3 independent categories per lane. Log every source you use as one row in `02-sources.md`:

   | Field | Rule |
   |---|---|
   | ID | L-001, L-002… (continues across the task) |
   | url / path | Where the source is |
   | date read | ISO date |
   | claim | What the source says: a quote, or a close paraphrase marked (para) |
   | category | survey · official / regulator · platform documentation · company site · practitioner write-up · news · review or forum |
   | confidence | **high:** official, or primary data, or 2+ independent sources agree · **medium:** one credible secondary source · **low:** anecdote, or no stated basis |
   | implication | What it means for this client, in one line |

4. **Surface contradictions.** When sources disagree, log both rows and add an entry under Contradictions: the two L-IDs, what differs, which is more credible and why, or "unresolved". Never keep only the convenient one.
5. **Write each finding:** 1–3 sentences answering the RQ, citing L-IDs. If nothing credible was found, write "not found", list where you looked, and mark it [VERIFY].

## Output templates

`02-sources.md`:

    # Source ledger — <task id>
    | ID | url / path | date read | claim | category | confidence | implication |

`03-findings.md`:

    # Findings — <task id>
    ## Lane map
    | Lane | RQs | Runs now / carried (waiting on) |
    ## Findings
    ### RQn. <question>
    <1–3 sentences> [L-…]
    ## Contradictions
    | Sources | What differs | Resolution |
    ## Carried
    | RQ | Waiting on |

## Worked example

Gemstone task. RQ1 was conditional on CQ2, which is now answered, so it runs.

    ### RQ1. How do IT and consulting firms of 50–300 people choose and buy corporate gifts?
    (illustrative) Gifts are usually chosen by HR or the office admin, with finance approving above a
    per-order limit. Festival orders are placed 4–6 weeks ahead. [L-003, L-004, L-007]

`02-sources.md` row *(illustrative)*: `| L-003 | https://example.org/gifting-survey | 2026-10-02 | "61% of HR leads choose festival gifts" | survey | medium | HR is the first reader; pieces should speak to HR needs |`

## Self-check

- [ ] Was the lane map written before any parallel research?
- [ ] Is every runnable RQ answered or marked not found, with where you looked?
- [ ] Does every ledger row have all six fields, and a confidence that follows the rule?
- [ ] Is every contradiction listed, not resolved silently?

## Traps

- **Summary as finding.** A finding with no L-IDs is an opinion.
- **One-source certainty.** Marking a single blog "high".
- **Running conditional RQs early.** Researching "companies" in general before CQ2 named which ones wastes the lane.
