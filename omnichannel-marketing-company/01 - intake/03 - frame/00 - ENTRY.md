# 03 · Frame

**Purpose:** fix what the end of the line must deliver, by making four decisions. The package that `09 - packaging` assembles follows from them, and every open decision becomes a round-1 question at step 4.

## Contract

- **Reads:** `01-intake/01-parse.md`.
- **Writes:** `01-intake/02-frame.md`.
- **Done when:** F1–F4 each have a value with evidence, or are UNDECIDED with a deciding question; the package is looked up; the branch check is answered.

## Procedure

1. **Decide F1–F4 in order** with the rules below. Each value needs evidence: a statement ID, a slot, or a reading. If the rule does not pick exactly one value, write **UNDECIDED** and the deciding question: one question whose every answer maps to exactly one value. Reuse the parse's deciding question when it already covers the decision.

   **F1 Brand mode.** Whose name does the content speak under? From slot BRAND and the readings.

   | Value | Rule |
   |---|---|
   | EXISTING | The request says the content is for a business or brand that already exists, and no new name is mentioned |
   | NEW | The request says a new name, brand or sub-brand will be created |
   | THIRD-PARTY | The speaker asks for work that another party (their client) will use under its own name |
   | UNDECIDED | Readings in the parse point to different values |

   **F2 Horizon.** Is something being brought to market, or kept in market? From slot OFFER and the verbs.

   | Value | Rule |
   |---|---|
   | LAUNCH | The offer is not on sale yet, or is going to a new buyer group. Signals: "build", "start", "launch", "new" |
   | ONGOING | The offer is on sale and the client wants sustained marketing. Signals: "grow", "more customers", "run my marketing" |
   | UNDECIDED | The request doesn't say whether the offer is already on sale |

   **F3 Outputs.** Which content families to make.
   - **Always IN:** the hub piece (long-form article or newsletter) and its channel variants. This is the pipeline's core.
   - **IN:** each other family the request names.
   - **ASK:** every other family. The families are: ad creative and copy · website or landing copy · email · sales collateral (catalogue, deck, one-pager).
   - A family that the request itself names as the main ask (e.g. "performance marketing" → ad creative and copy) is IN and marked **central**.

   **F4 Execution.** Beyond making content, is anything expected of us? From slot EXECUTION.

   | Value | Rule |
   |---|---|
   | CONTENT-ONLY | The request asks for content, or doesn't mention running anything. Recorded as an **assumption**, shown to the client |
   | CONTENT+RUN | The request asks us to *do*, *run* or *manage* an activity (ads, accounts, campaigns) |
   | UNDECIDED | A verb like "do" could mean either making the content or running the activity |

   The pipeline makes content. CONTENT+RUN, or UNDECIDED, puts running on the table, so its deciding question goes to the client in round 1.

2. **Look up the package** from F1 × F2:

   | F1 \ F2 | LAUNCH | ONGOING |
   |---|---|---|
   | EXISTING | Launch set under the existing brand | Recurring content batch for the existing brand |
   | NEW | Name + positioning, then the launch set | Positioning, then the recurring batch |
   | THIRD-PARTY | Launch set in the third party's voice, delivered to our client | Recurring batch in the third party's voice, delivered to our client |

   If either F1 or F2 is UNDECIDED, the package is **pending** until its deciding question is answered.

3. **Branch check.** Split the task now only if the request names two different brands, or two offers sold to different buyers. If so, list the branches: each becomes its own task through `task.py new`, with the same request file. Otherwise write "No branch", and name any split the strategy or planning nodes should consider.

## Output template

    # Frame — <task id>
    | Decision | Value | Evidence | Deciding question (if UNDECIDED) |
    | F1 Brand mode | … | … | … |
    | F2 Horizon | … | … | … |
    | F3 Outputs | IN: … · ASK: … · central: … | … | — |
    | F4 Execution | … | … | … |
    ## Package
    <cell from the lookup, or "pending on F1/F2">
    ## Branch
    <No branch — reason> or <branches listed>

## Worked example

Gemstone request (parse above):

| Decision | Value | Evidence | Deciding question |
|---|---|---|---|
| F1 | UNDECIDED | I-A vs I-B (S3) | "Current business name, or a new name?" |
| F2 | LAUNCH | S2 "want to like build": not on sale yet | — |
| F3 | IN: hub and variants · ASK: sales collateral, email, website copy, ads | none named | — |
| F4 | CONTENT-ONLY (assumed) | nothing asked beyond content | — |

Package: pending on F1 (EXISTING → launch set under the current brand; NEW → name + positioning, then the launch set). Branch: no branch; one business, one ask.

Performance-marketer request: F1 is UNDECIDED ("for me for xyz" — own business or their client's?). F2 is UNDECIDED (is xyz on sale?). F3 has ad creative and copy as IN and **central** ("performance marketing"). F4 is UNDECIDED ("do performance marketing" could mean making the ads or running them).

## Self-check

- [ ] Does each of F1–F4 cite a statement, slot or reading?
- [ ] Does every UNDECIDED have a deciding question where each answer maps to one value?
- [ ] Is the package the table's cell, or "pending", and not a description of our own?
- [ ] Does the branch decision follow the two-brands-or-two-buyers rule?

## Traps

- **Deciding by likelihood.** Choosing EXISTING because it "seems more likely". The rule decides, or the value is UNDECIDED.
- **Scope creep in F3.** Marking families IN because the client would "probably want" them. Unnamed families are ASK.
- **Missing the run.** Reading "do X for me" as content only. If the verb could mean running an activity, F4 is UNDECIDED.
