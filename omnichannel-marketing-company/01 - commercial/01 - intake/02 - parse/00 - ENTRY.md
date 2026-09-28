# 02 · Parse

**Purpose:** break the request into what it states, what it could mean, and which brief slots it fills. Step 3 frames the job from this file, and step 4 turns its open items into questions.

## Contract

- **Reads:** `11-intake/00-request.md` and `from-client/` only. No web search, no knowledge of the industry, no memory of similar clients.
- **Writes:** `11-intake/01-parse.md`.
- **Done when:** every clause of the request appears as a statement; every clause with more than one meaning has readings; all 13 slots have a status.

## Procedure

1. **Literal ask.** Write one sentence: what the client asked us to do, using their verbs and nouns.
2. **Statements.** Split the request wherever a new idea starts (usually at "and", a comma, "for", "as"). Number each piece S1, S2 … and write:
   - **Quote:** the exact words.
   - **Establishes:** what those words state, and only that.
   - **Hedge:** any soft words ("like", "want to", "maybe", "into", "kind of") and what they signal (idea not settled, informal, early stage). Otherwise "none".
3. **Readings.** For each statement, ask: *could these words mean two or more things that would change the work?* ("Change the work" means a different brand mode, horizon, buyer or output in step 3.)
   - **If yes**, write the readings I-A, I-B … (2–4). Each gets:
     - **Reading:** one sentence.
     - **Support:** the quote that points to it.
     - **Changes:** which slots or frame decisions it would set.
   - Then write **one deciding question** that covers all the readings of that statement, whose every possible answer points to exactly one reading. "Not sure" is always allowed; it keeps the matter open for a later node.
   - **If no statement is ambiguous**, write "Single reading", and give the reason.
4. **Slots.** For each of the 13 slots in `00 - control/01 - law/BRIEF_SLOTS.md`, in order, set a status. The evidence each status needs:

   | Status | Evidence |
   |---|---|
   | Known | a quote |
   | Partly known | a quote for the known part, and one line for the open part |
   | Assumed | the assumption, plus why a wrong one is cheap, reversible and visible to the client |
   | Unknown | one line naming what is missing |

   A slot fact that depends on how an ambiguous statement is read is Unknown, with a note like "depends on I-A/I-B".

## Output template

    # Parse — <task id>
    ## Literal ask
    <one sentence>
    ## Statements
    | ID | Quote | Establishes | Hedge |
    ## Readings
    ### From S<n>
    | ID | Reading | Support | Changes |
    Deciding question: <question> — <answer> → I-A · <answer> → I-B · not sure → stays open
    ## Slots
    | # | Slot | Status | Evidence / open part |

## Worked example

Request: *I'm into precious gemstones selling and want to like build corporate gifts as a sub branch*

| ID | Quote | Establishes | Hedge |
|---|---|---|---|
| S1 | "I'm into precious gemstones selling" | The speaker sells precious gemstones | "into": informal; says nothing about scale or how long |
| S2 | "want to like build corporate gifts" | They intend to start selling gifts to companies | "want to", "like": an intention, not yet a plan |
| S3 | "as a sub branch" | The gift line would sit under the existing business | none |

Readings from S3:

| ID | Reading | Support | Changes |
|---|---|---|---|
| I-A | A new, separately named sub-brand for corporate gifts | "sub branch" | BRAND = new name; F1 = NEW |
| I-B | A corporate-gifting line under the current business name | "sub branch" | BRAND = current name; F1 = EXISTING |

Deciding question: *Will the corporate gifts be sold under your current business name, or under a new name?* Current → I-B · new → I-A · not sure → stays open.

Slot rows (excerpt):

| # | Slot | Status | Evidence / open part |
|---|---|---|---|
| 1 | SPEAKER | Partly known | "I'm into precious gemstones selling". Open: their role (owner or employee) |
| 3 | OFFER | Partly known | "corporate gifts". Open: what the gifts are, whether they exist yet, the price |
| 4 | BUYER | Partly known | "corporate gifts": the buyers are companies. Open: which companies, and who inside them decides |
| 2 | BRAND | Unknown | depends on I-A/I-B |

## Self-check

- [ ] Does every quote appear word for word in `00-request.md`?
- [ ] Is every clause of the request in the Statements table?
- [ ] Does each deciding question have an answer that points to each reading?
- [ ] Do all 13 slots have a status, with the evidence that status requires?
- [ ] Is there no fact in the file that the request doesn't contain?

## Traps

- **Knowledge leak.** Writing an industry fact (e.g. "gemstones need certification") into a slot. It is not in the request, so it is not Known: it belongs in step 4 as a research question.
- **Premature reading.** Filling BRAND or OFFER from one reading while another reading is still open. Mark the slot Unknown, "depends on I-…".
- **Assuming to avoid asking.** Marking a slot Assumed when a wrong guess would be costly. If it fails any of cheap, reversible or visible, it is Unknown.
- **Paraphrase in quotes.** Quotation marks around words the client didn't write.
