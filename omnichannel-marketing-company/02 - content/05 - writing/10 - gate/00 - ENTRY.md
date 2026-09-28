# 10 · Gate

**Purpose:** confirm every piece is complete, passed, human-checked and shaped for every channel with every still accepted. Then carry the month's writing forward and advance.

## Contract

- **Reads:** everything in `25-writing/`; the piece briefs; `from-operator/25-writing-human-check.md`; the channel ENTRYs in `06 - channels/`.
- **Writes:** the `## 25-writing` section of `CONTEXT.md`; `25-writing/gate.md`.
- **Done when:** `gate.md` says `VERDICT: PASS` and the task has advanced.

## Procedure

1. **Per piece, in order:**

   | # | Check | On failure |
   |---|---|---|
   | W1 | `01-sources.md` to `04-spine.md` exist; the saturation check says YES; the originality check says NONE | 01 - research |
   | W2 | `05-draft.md` and `06-article.md` exist; the voice note is present | 02 - draft / 03 - voice |
   | W3 | `07-review.md`'s last round is PASS, with a SURPLUS line | 04 - review |
   | W4 | `08-seeds.md` has six seeds, each assigned | 05 - seeds |
   | W5 | A variant exists for every channel in the plan | 06 - channels |

2. **Per variant, all five:**

   | # | Check | Source of the rule |
   |---|---|---|
   | C1 | Every self-check item in that channel's ENTRY is yes | `06 - channels/<nn - channel>/00 - ENTRY.md` |
   | C2 | V1 read-aloud as the client; V2 no kill-list tells; V3 no monotonous sentence length | `03 - voice/revoice-prompt.md` |
   | C3 | The variant's own crafted surplus, named in one line | `00 - control/01 - law/PERFECTIONISM_ENFORCEMENT.md` |
   | C4 | Born native: no sentence copied from the article or another variant | `00 - control/01 - law/OMNICHANNEL_ENFORCEMENT.md` Rule 2 |
   | C5 | Its date, tagged link and test variant match the calendar | `24-planning/02-calendar.md` |

3. **Across the month:**

   | # | Check | On failure |
   |---|---|---|
   | W6 | Every video in the plan has a script and storyboard | 07 - scripts |
   | W7 | Every still is ACCEPTED in `stills/00-still-index.md` | 08 - visuals |
   | W8 | The operator's human check says PASS for every piece | 09 - human-check |

4. **Write the carry-forward** (at most 10 bullets):

       ## 25-writing
       - Pieces: P1 "<title>" · P2 … — all passed review and the human check [25-writing/00-piece-index.md]
       - Surplus per piece: … [25-writing/<P>/07-review.md]
       - Variants: N across <channels> [25-writing/00-piece-index.md]
       - Stills: N accepted [25-writing/stills/00-still-index.md]
       - Videos: V… scripted / none [25-writing/00-piece-index.md]
       - Client to supply: <list, or none>

5. **Write `gate.md`** (the five-line format in `00 - control/01 - law/TASK_CONTRACT.md` §2), then `python3 "00 - control/02 - tools/task.py" advance <task-id>`. The task goes to the video factory if the engagement includes video, otherwise to packaging.

## Self-check

- [ ] Were the per-piece checks run before the per-variant ones?
- [ ] Is every variant's surplus named?

## Traps

- **Passing a lazy cross-post because the rest is excellent.** Each variant passes on its own.
