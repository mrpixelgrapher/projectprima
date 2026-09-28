# 05 · Gate

**Purpose:** gate the hub version and every channel variant, each on its own. A lazy cross-post fails even if the rest is excellent. Then carry the piece forward to the parent waiting at packaging.

## Contract

- **Reads:** everything in `08-shaping/`; the channel ENTRY files in `08 - shaping/03 - channels/`; the Voice section of `00-brief.md`.
- **Writes:** `08-shaping/05-variant-gates.md`; the `## 08 - shaping` section of `CONTEXT.md`; `08-shaping/gate.md`.
- **Done when:** every variant and the hub have passed all their checks, and the task has advanced to `09 - packaging`.

## Procedure

1. **Hub checks:**
   - H1: the metadata is complete, with title and meta description within their limits;
   - H2: the internal links follow the first-piece rule;
   - H3: every graphic marker is a slot with a brief;
   - H4: the audit trail carries SURPLUS.
2. **For each variant, all five checks:**

   | # | Check | Source of the rule |
   |---|---|---|
   | C1 | Every self-check item in that channel's ENTRY is yes | `08 - shaping/03 - channels/<nn - channel>/00 - ENTRY.md` |
   | C2 | V1 read-aloud as the client; V2 no kill-list tells; V3 no monotonous sentence length | `06 - drafting/02 - voice/revoice-prompt.md` |
   | C3 | The variant's own crafted surplus, named in one line | `00 - control/01 - law/PERFECTIONISM_ENFORCEMENT.md` |
   | C4 | Born native: no sentence is copied verbatim from the hub or from another variant | `00 - control/01 - law/OMNICHANNEL_ENFORCEMENT.md` Rule 2 |
   | C5 | Every image slot has a brief (WAITING-ON-PRODUCER counts; a missing brief doesn't) | `04 - visuals/` |

3. **A failure** sends you back to the stage that made the file: seeds (1), hub (2), the channel's sub-folder (3), or visuals (4). Fix it there, then re-run this gate.
4. **Write the carry-forward** (at most 8 bullets):

       ## 08 - shaping
       - Hub: "<title>" [08-shaping/02-hub-metadata.md]
       - Variants: <channel list> — all passed [08-shaping/05-variant-gates.md]
       - Surplus per variant: … [08-shaping/05-variant-gates.md]
       - Images: N briefs, status … [08-shaping/04-visual-index.md]
       - Client to supply: <list, or none> [08-shaping/03-channel-index.md]

5. **Write `gate.md`** (the five-line format in `00 - control/01 - law/TASK_CONTRACT.md` §2), then run `python3 "00 - control/02 - tools/task.py" advance <task-id>`. The child arrives at `09 - packaging`, where its parent waits.

## Output template

    # Variant gates — <task id>
    ## Hub
    | H1 | H2 | H3 | H4 |
    ## Variants
    | Channel | C1 | C2 | C3 surplus | C4 | C5 | Result |

## Self-check

- [ ] Was each variant judged separately, with its own surplus?
- [ ] Did C4 compare every variant against the hub and every other variant?

## Traps

- **Passing the set because the hub is strong.** Every variant stands alone.
- **Images waiting read as failure.** WAITING-ON-PRODUCER passes C5; a missing brief doesn't.
