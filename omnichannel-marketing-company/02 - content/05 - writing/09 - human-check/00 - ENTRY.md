# 09 · Human check

**Purpose:** before anything leaves writing, a person reads it. The operator checks every piece by hand against `human-check.md` in this folder: it reads like a human wrote it, it shows clear thinking, and it compresses a lot of knowledge into something the reader can use. The review gate judges rules; this check judges the reading.

## Contract

- **Reads:** `25-writing/00-piece-index.md`; every piece's `06-article.md`, `07-review.md` and `channels/*.md`; `human-check.md` in this folder; `00 - control/01 - law/HANDOFFS.md` (H2).
- **Writes:** `25-writing/09-human-check-for-operator.md`.
- **Done when:** `from-operator/25-writing-human-check.md` gives every piece PASS, after any FIX items were fixed and checked again.

## Procedure

1. **Write the request:** for each piece, the article's path, its review's SURPLUS line, and the variants to read (all variants of the first piece; for the rest, the long-form, one text-social and one visual-social variant, chosen so every channel is read at least once in the month). Attach the checklist: "Read each against `02 - content/05 - writing/09 - human-check/human-check.md`. For each piece reply PASS, or FIX with the line and what's wrong."
2. **Hold (H2):** `task.py hold <task-id> --on "H2 operator: 25-writing/09-human-check-for-operator.md"`.
3. **When the answer lands,** resume. For each FIX, send the piece back to the stage that owns the problem:

   | The operator's note is about | Back to |
   |---|---|
   | The argument, clarity or what the piece says | `01 - research/03 - spine/` or `02 - draft/` |
   | Sounding like a machine, or not like the client | `03 - voice/` |
   | One channel's variant | that channel's folder in `06 - channels/` |

   Then review again (for article changes), and ask the operator to check only the fixed items.

## Output template

    # Human check — <task id>
    | P | Article | Review SURPLUS | Variants to read |
    Checklist: 02 - content/05 - writing/09 - human-check/human-check.md
    Reply per piece: PASS, or FIX — <line> — <what's wrong>

## Worked example

*(illustrative)* Operator reply: "P1 PASS. P2 FIX — para 3 'it is widely acknowledged that authenticity matters' — filler, says nothing; P3 PASS." → P2 back to `03 - voice/` (a machine tell), reviewed again, re-checked alone.

## Self-check

- [ ] Is every piece's article in the request, and every channel read at least once?
- [ ] Was every FIX fixed and checked again?

## Traps

- **Treating the check as optional.** Nothing leaves writing without the operator's PASS.
