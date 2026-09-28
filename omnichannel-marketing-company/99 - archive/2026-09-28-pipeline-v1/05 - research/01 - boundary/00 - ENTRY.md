# 01 · Boundary

**Purpose:** gather everything relevant to the piece's question, from its consensus and live disputes to concrete particulars and the reader's wrong model, with every item traced to a logged source. The spine can only be as good as this stage is wide.

## Contract

- **Reads:** `00-brief.md`; `CONTEXT.md`; `boundary-prompt.md` in this folder; earlier research in `10 - delivery/done/`.
- **Writes:** `05-research/01-sources.md`, `05-research/02-boundary-map.md`, `05-research/03-observations.md`.
- **Done when:** all seven sectors are filled, every claim carries an L-ID or `[VERIFY]`, there are ≥ 5 observations, and the saturation self-check says YES.

## Procedure

1. **Reuse first.** Search `10 - delivery/done/*/09-packaging/pieces/*/05-research/02-boundary-map.md` for the same keyword or question. For each match, copy its source rows into `01-sources.md`. Re-open each URL, update the date read, and drop sources that are gone.
2. **Fill the prompt's slots:**

   | Slot | Value |
   |---|---|
   | `{{TOPIC}}` | The brief's question |
   | `{{ANGLE}}` | The pillar's claim, plus the objection it answers, plus the buyer's stage |
   | `{{DOMAIN}}` | The client's field, plus the buyer (who, where) |

3. **Run the prompt with live research,** and aim wide. Log every source you use as a row in `01-sources.md`, in the same seven-field format as `02 - discovery/02 - research/00 - ENTRY.md` (ID, url, date read, claim, category, confidence, implication). The IDs continue from any reused rows.
4. **Write the boundary map:** the prompt's seven sectors. Every claim ends with its L-ID, or `[VERIFY]`. Sector 5 (concrete particulars) needs at least 12 items; they are the density the draft will spend.
5. **Extract observations.** Write at least 5, numbered O1…. Each one is a pattern across sources, a contradiction between them, or a reusable framework, and each cites its L-IDs. Prefer observations that combine 2+ sources.
6. **Check the keyword.** Confirm the brief's keyword candidate appears in how buyers or sources phrase the topic, citing an L-ID; or propose a better phrase, with its evidence.
7. **Saturation self-check** (the end of the prompt). If the answer is NO, deepen the thin sectors before leaving this stage.

## Output templates

    # Sources — <task id>
    | ID | url / path | date read | claim | category | confidence | implication |

    # Boundary map — <task id>
    ## 1. Core claims   ## 2. Live disputes   ## 3. Adjacent fields   ## 4. Historical arc
    ## 5. Concrete particulars (≥ 12)   ## 6. Contradictions and unknowns   ## 7. The reader's wrong model
    Keyword: <confirmed phrase> [L-…]
    Saturation: YES / NO (thin sectors: …)

    # Observations — <task id>
    | ID | Observation | Type (pattern / contradiction / framework) | Sources |

## Worked example

Gemstone piece `real-or-fake` *(illustrative)*:
- **Sector 2, live dispute:** "Camp A: a lab report is enough proof for a buyer [L-004]. Camp B: buyers don't read lab reports; they trust the seller's name [L-009]."
- **O3 (contradiction):** HR buyers cite authenticity as their top fear [L-003], yet sellers rarely show certificates in their marketing [L-011, L-012].

## Self-check

- [ ] Are all seven sectors filled, and does sector 5 have ≥ 12 particulars?
- [ ] Does every claim end with an L-ID or `[VERIFY]`?
- [ ] Are there ≥ 5 observations, each citing its sources?
- [ ] Does the saturation check say YES?

## Traps

- **Drafting early.** A sentence of article prose here is a failure.
- **"Studies show."** Name the source category and its L-ID, or mark `[VERIFY]`.
- **Narrow search.** Twelve sources all from one category give one voice. Aim for 3+ categories.
