# 03 · Gate

**Purpose:** confirm the article is complete and faithful to the draft, then send it to review.

## Contract

- **Reads:** `06-drafting/01-draft.md`, `02-article.md`; `00-brief.md`.
- **Writes:** the `## 06 - drafting` section of `CONTEXT.md`; `06-drafting/gate.md`.
- **Done when:** `gate.md` says `VERDICT: PASS` and the task has advanced.

## Procedure

1. **Run the checks in order.** Stop at the first failure.

   | # | Check | On failure |
   |---|---|---|
   | W1 | The draft has every skeleton part and a `[src: …]` on every factual sentence | stage 1 |
   | W2 | The draft has ≥ 2 graphic slots and every brief link slot; the CTA matches the brief | stage 1 |
   | W3 | The article has no `[src: …]` markers, keeps the LINK and GRAPHIC markers, and ends with the voice note | stage 2 |
   | W4 | Every article paragraph maps to a draft paragraph (no new claims) | stage 2 |

2. **Write the carry-forward** (at most 5 bullets):

       ## 06 - drafting
       - Title: "…" · words: N [06-drafting/02-article.md]
       - Voice note: … [06-drafting/02-article.md]
       - Slots: N graphics, N links [06-drafting/01-draft.md]

3. **Write `gate.md`** (the five-line format in `00 - control/01 - law/TASK_CONTRACT.md` §2), then run `python3 "00 - control/02 - tools/task.py" advance <task-id>`.

## Self-check

- [ ] Were W1–W4 checked against the files?

## Traps

- **Judging quality here.** Quality is judged at `07 - review`. This gate checks completeness and fidelity.
