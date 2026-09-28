# 01 · Judge

**Purpose:** score the article against every check and return PASS or FAIL. On a FAIL, name the first failed check, the defect, and where it goes back to. On a PASS, name the crafted surplus. Judge; don't edit.

## Contract

- **Reads:** `06-drafting/02-article.md`, `01-draft.md` (for traceability); `05-research/*`; `00-brief.md`; `gate-prompt.md` in this folder.
- **Writes:** `07-review/01-review-report.md`.
- **Done when:** every check has PASS or FAIL with evidence, and the verdict, route and (on a PASS) SURPLUS line are written.

## Procedure

1. **Run the prompt.** Use the article, plus the research folder as it stood at `05 - research`.
2. **Add the limits check. L1:** no claim in the article breaches the brief's Limits (e.g. certification or health claims without a document in hand).
3. **Traceability (G1).** Check it through the draft. Every factual sentence of the article must map to a draft sentence that carries a `[src: …]` marker.
4. **Order.** Run the checks in pipeline order: D1–D3, then G1–G6, then L1, then V1–V3, then P1. **The first FAIL ends the review.** Don't judge downstream of a broken upstream.
5. **Route a FAIL:**

   | First failed check | Back to | Stage there |
   |---|---|---|
   | D1, D2, G2 | `05 - research` | `02 - spine` |
   | G3 | `05 - research` | `01 - boundary` |
   | D3, G1, G4, G5, G6, L1 | `06 - drafting` | `01 - draft` |
   | V1, V2, V3, P1 | `06 - drafting` | `02 - voice` |

6. **On a PASS,** write `SURPLUS: <one line naming the element that exceeds expectation>`. Decoration, aspirational claims and generic personalisation don't count (`00 - control/01 - law/PERFECTIONISM_ENFORCEMENT.md`).

## Output template

    # Review report — <task id> (round N)
    | Check | Result | Evidence (quote or file reference) |
    VERDICT: PASS | FAIL
    First failed check: … · Defect: … · Back to: <node> / <stage>
    SURPLUS: …        (PASS only)

## Worked example

*(illustrative)* `| G2 Originality | FAIL | The one thing ("show buyers how to check a report") is stated outright in L-009 |` → VERDICT: FAIL · Back to: 05 - research / 02 - spine.

## Self-check

- [ ] Were the checks run in order, stopping at the first FAIL?
- [ ] Does every result cite evidence?
- [ ] Does a PASS name a specific surplus element?

## Traps

- **Soft verdicts.** "Mostly fine" is a FAIL. A borderline piece fails.
- **Editing while judging.** A reviewer who rewrites a sentence hides the defect from its source stage.
