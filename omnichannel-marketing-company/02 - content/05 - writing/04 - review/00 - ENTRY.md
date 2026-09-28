# 04 · Review

**Purpose:** score each piece's article against every check and return PASS or FAIL, before it fans out to the channels. On a FAIL, name the first failed check, the defect, and where it goes back to. On a PASS, name the crafted surplus. Judge; don't edit.

## Contract

- **Reads:** `25-writing/<P>/06-article.md`, `05-draft.md` (for traceability), `01-sources.md` to `04-spine.md`; the piece brief (`24-planning/briefs/<P>.md`); `gate-prompt.md` in this folder.
- **Writes:** `25-writing/<P>/07-review.md` (each round appends a new report under `## Round N`).
- **Done when:** every check has PASS or FAIL with evidence, and the verdict, route and (on a PASS) SURPLUS line are written.

## Procedure

1. **Run the prompt.** Use the article, plus the piece's research files as they stood after the spine.
2. **Add the limits check. L1:** no claim in the article breaches the brief's Limits (e.g. certification or health claims without a document in hand).
3. **Traceability (G1).** Check it through the draft. Every factual sentence of the article must map to a draft sentence that carries a `[src: …]` marker.
4. **Order.** Run the checks in pipeline order: D1–D3, then G1–G6, then L1, then V1–V3, then P1. **The first FAIL ends the review.** Don't judge downstream of a broken upstream.
5. **Route a FAIL** back to the stage that caused it, inside this node:

   | First failed check | Back to |
   |---|---|
   | D1, D2, G2 | `01 - research/03 - spine/` |
   | G3 | `01 - research/02 - boundary/` (a second ARENA request if the dossier is thin) |
   | D3, G1, G4, G5, G6, L1 | `02 - draft/` |
   | V1, V2, V3, P1 | `03 - voice/` |

   Rerun from there, then review again (round N+1). **Loop limit:** a piece failing the same check 3 times goes to the operator (H2: `25-writing/<P>/07-review-for-operator.md`; hold). A defect that keeps coming back usually sits upstream, in the brief or the strategy.

6. **On a PASS,** write `SURPLUS: <one line naming the element that exceeds expectation>`. Decoration, aspirational claims and generic personalisation don't count (`00 - control/01 - law/PERFECTIONISM_ENFORCEMENT.md`).

## Output template

    # Review — <P> (round N)
    | Check | Result | Evidence (quote or file reference) |
    VERDICT: PASS | FAIL
    First failed check: … · Defect: … · Back to: <node> / <stage>
    SURPLUS: …        (PASS only)

## Worked example

*(illustrative)* `| G2 Originality | FAIL | The one thing ("show buyers how to check a report") is stated outright in L-009 |` → VERDICT: FAIL · Back to: 01 - research / 03 - spine.

## Self-check

- [ ] Were the checks run in order, stopping at the first FAIL?
- [ ] Does every result cite evidence?
- [ ] Does a PASS name a specific surplus element?

## Traps

- **Soft verdicts.** "Mostly fine" is a FAIL. A borderline piece fails.
- **Editing while judging.** A reviewer who rewrites a sentence hides the defect from its source stage.
