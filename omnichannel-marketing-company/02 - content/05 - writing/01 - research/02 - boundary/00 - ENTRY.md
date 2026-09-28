# 02 · Boundary

**Purpose:** turn the dossier into everything relevant to the piece's question, from its consensus and live disputes to concrete particulars and the reader's wrong model, with every item traced to a logged source. The spine can only be as good as this stage is wide.

## Contract

- **Reads:** the piece's section of `25-writing/arena-dossier-1/`; the piece brief (`24-planning/briefs/<P>.md`); `CONTEXT.md`; `../01 - request/boundary-prompt.md` (the seven sectors).
- **Writes:** `25-writing/<P>/01-sources.md`, `02-boundary-map.md`, `03-observations.md`.
- **Done when:** all seven sectors are filled, every claim carries an L-ID or `[VERIFY]`, there are ≥ 5 observations, and the saturation self-check says YES.

## Procedure

1. **Resume** the task when the dossier has landed (`task.py resume <task-id> --note "dossier 1"`), and mark each piece "research: dossier in" in `00-piece-index.md`.
2. **Log the sources** the dossier's section cites, one row each in `01-sources.md`, in the seven-field format of `02 - content/01 - discovery/02 - findings/00 - ENTRY.md` (ID, url, date read, claim, category, confidence, implication). IDs continue from the client's earlier ledgers. Set confidence by that rule, whatever the dossier says.
3. **Write the boundary map:** the prompt's seven sectors, from the dossier. Every claim ends with its L-ID, or `[VERIFY]`. Sector 5 (concrete particulars) needs at least 12 items; they are the density the draft will spend. Add the topic's top-post patterns (from the sampling section) under sector 3 or 5 where they matter to the argument, as sourced items.
4. **Extract observations.** Write at least 5, numbered O1…. Each is a pattern across sources, a contradiction between them, or a reusable framework, and each cites its L-IDs. Prefer observations that combine 2+ sources.
5. **Check the keyword.** Confirm the brief's keyword candidate appears in how buyers or sources phrase the topic, citing an L-ID; or propose a better phrase, with its evidence.
6. **Saturation self-check** (the end of the prompt). NO → write `arena-request-2.md` for the thin sectors only, hold (H3), and finish this piece when it returns. Other pieces continue meanwhile only up to this stage.

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

Gemstone piece P2 `real-or-fake` *(illustrative)*:
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
- **Narrow sources.** Twelve sources all from one category give one voice. If the dossier gives fewer than 3 categories, the saturation check is NO.
