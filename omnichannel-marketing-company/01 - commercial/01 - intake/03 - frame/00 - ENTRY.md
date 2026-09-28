# 03 · Frame

**Purpose:** fix what the job must deliver, by making four decisions. Scope (`01 - commercial/02 - scope/`) builds the deliverables list from them, and every open decision becomes a client question at step 4.

## Contract

- **Reads:** `11-intake/01-parse.md`.
- **Writes:** `11-intake/02-frame.md`.
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

   **F3 Outputs.** Which content families to make. The company makes organic content only (no paid ads), built to spread on its own and to convert: every piece drives traffic to one destination online.
   - **Always IN:** the core (research-backed long-form pieces), their channel-native variants, and the destination (the one place online all traffic lands: a newsletter, site or landing page). This is the line's core.
   - **IN:** each other family the request names.
   - **ASK:** every other family. The families are: text social (LinkedIn, X, Threads, Facebook) · visual social (Instagram, Pinterest) · long-form platforms (Substack, Medium, blog) · newsletter · landing page · video (scripts and storyboards through the video factory).
   - A family the request names as the main ask is IN and marked **central**. "Performance marketing" means content engineered for conversion: the performance design (`02 - content/03 - performance/`) is central, and paid ads stay out; say so to the client at step 4.

   **F4 Execution.** Beyond making content, do we publish it? From slot EXECUTION.

   | Value | Rule |
   |---|---|
   | CONTENT-ONLY | The request asks for content, or doesn't mention posting. Recorded as an **assumption**, shown to the client |
   | CONTENT+PUBLISHING | The request asks us to *post*, *run* or *manage* their accounts |
   | UNDECIDED | A verb like "do" could mean making the content or posting it |

   CONTENT+PUBLISHING, or UNDECIDED, puts publishing on the table: its deciding question goes to the client, and the proposal prices it as `includes publishing`.

2. **Look up the package shape** from F1 × F2. Scope turns it into deliverables; the proposal offers it as a one-off or a retainer.

   | F1 \ F2 | LAUNCH | ONGOING |
   |---|---|---|
   | EXISTING | Launch set under the existing brand | Monthly content under the existing brand (retainer) |
   | NEW | Name + positioning, then the launch set | Positioning, then monthly content (retainer) |
   | THIRD-PARTY | Launch set in the third party's voice, delivered to our client | Monthly content in the third party's voice, delivered to our client (retainer) |

   If either F1 or F2 is UNDECIDED, the package shape is **pending** until its deciding question is answered.

3. **Split check.** Split the request only if it names two different brands, or two offers sold to different buyers. If so, list the parts: each becomes its own task through `task.py new` (same client folder, same request file), and this task is closed with `task.py close`, naming the new tasks. Otherwise write "No split".

## Output template

    # Frame — <task id>
    | Decision | Value | Evidence | Deciding question (if UNDECIDED) |
    | F1 Brand mode | … | … | … |
    | F2 Horizon | … | … | … |
    | F3 Outputs | IN: … · ASK: … · central: … | … | — |
    | F4 Execution | … | … | … |
    ## Package shape
    <cell from the lookup, or "pending on F1/F2">
    ## Split
    <No split — reason> or <parts listed>

## Worked example

Gemstone request (parse above):

| Decision | Value | Evidence | Deciding question |
|---|---|---|---|
| F1 | UNDECIDED | I-A vs I-B (S3) | "Current business name, or a new name?" |
| F2 | LAUNCH | S2 "want to like build": not on sale yet | — |
| F3 | IN: core, variants, destination · ASK: text social, visual social, long-form platforms, newsletter, landing page, video | none named | — |
| F4 | CONTENT-ONLY (assumed) | nothing asked beyond content | — |

Package shape: pending on F1 (EXISTING → launch set under the current brand; NEW → name + positioning, then the launch set). Split: no split; one business, one ask.

Performance-marketer request: F1 is UNDECIDED ("for me for xyz" — own business or their client's?). F2 is UNDECIDED (is xyz on sale?). F3 has the performance design IN and **central** ("performance marketing"), with paid ads out and said so. F4 is UNDECIDED ("do performance marketing" could mean making the content or posting it too).

## Self-check

- [ ] Does each of F1–F4 cite a statement, slot or reading?
- [ ] Does every UNDECIDED have a deciding question where each answer maps to one value?
- [ ] Is the package shape the table's cell, or "pending", and not a description of our own?
- [ ] Does the split decision follow the two-brands-or-two-buyers rule?

## Traps

- **Deciding by likelihood.** Choosing EXISTING because it "seems more likely". The rule decides, or the value is UNDECIDED.
- **Scope creep in F3.** Marking families IN because the client would "probably want" them. Unnamed families are ASK.
- **Missing the posting.** Reading "do X for me" as content only. If the verb could mean posting for them, F4 is UNDECIDED.
- **Promising ads.** "Performance marketing" read as paid campaigns. The company does organic content engineered to convert; the client file says so plainly.
