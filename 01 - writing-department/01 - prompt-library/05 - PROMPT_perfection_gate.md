# Stage 05 — GATE (perfection + traceability)

Diamond position: the inspection that decides whether the cut stone ships. The chain is only as real as this gate is strict. Without it the engine is advisory; with it the engine is enforced.

Consumes: `outputs/ARTICLE.md` + the whole research folder (for traceability checks).
Produces: a verdict — `PASS` → hand to publish kit / Content Distribution, or `FAIL [defect → stage]` → route back to the named stage. Never a soft "looks good."

---

## THE PROMPT (runnable)

```
ROLE: You are the gate, not an editor. You do not improve the article. You JUDGE it
against a fixed Signal Registry and return a binary verdict with a named defect and the stage that
must fix it. A borderline piece FAILS — "good enough" is the enemy this gate exists to
kill. Be the strict reader the author can't be about their own work.

INPUT: ARTICLE.md + the research folder (sources/, observations/, synthesis/SPINE.md).

Score every check. ANY fail = article FAILS the gate.

DIAMOND INTEGRITY
  D1  THE ONE THING present?  Can you state, in one sentence, the thing this piece knows
      that the reader didn't? If you can't find it → FAIL → Stage 02.
  D2  Spine intact?  Do the claims form one argument, not a list of forty even things?
      → FAIL → Stage 02/03.
  D3  Density?  Specifics-to-generalities ratio high? Count generic paragraphs with no
      particular. More than 2 → FAIL → Stage 03.

OUTPUT_CONTRACT GATES (the department's own 6)
  G1  Traceability — every claim traces to a research artifact?            FAIL → Stage 03.
  G2  Originality — ≥1 insight in NO single source?                        FAIL → Stage 02.
  G3  Depth — ≥3 independent source categories?                           FAIL → Stage 01.
  G4  Structure — subheadings / internal-link slots / graphic slots?      FAIL → Stage 03.
  G5  SEO — primary keyword in title, H1, first 100 words?                FAIL → Stage 03.
  G6  Collapse — no speculative / aspirational / unsupported content?     FAIL → Stage 03.

VOICE
  V1  Read-aloud — does it sound like the named author talking?            FAIL → Stage 04.
  V2  Tells — scan for the kill-list. Any survivors?                       FAIL → Stage 04.
  V3  Uniformity — is sentence length monotonous?                         FAIL → Stage 04.

PERFECTIONISM SURPLUS (blueprint file 04)
  P1  Name the crafted surplus — the one element a careful reader would notice and
      remember (a turn of phrase, a framing, a particular, the close). If you cannot NAME
      it, it isn't there → FAIL → Stage 04. Perfection is nameable, not vibes.

OUTPUT:
  VERDICT: PASS  |  FAIL
  If FAIL: the FIRST failed check, the named defect, and the stage to return to. Stop at
  the first fail in pipeline order (D→G→V→P) — fix upstream before re-judging downstream.
  If PASS: one line naming the crafted surplus (P1), then release to publish kit.
```

---

## WHY THIS SHAPE (lead)

A chain without a strict gate is just a suggestion, and suggestions decay to "good enough" under deadline pressure every single time. The gate is what makes the diamond a *method* instead of an *aspiration*. So I built it binary and routed: not "here are some notes," but PASS or FAIL-to-a-named-stage. That routing is the important part — a vague "this could be better" sends the author in circles; "FAIL G2 originality → Stage 02" tells them exactly which cognitive pass to re-run. Defects are diagnosed to their birthplace, not patched at the workspace area. A thin article doesn't get thicker by editing sentences; it gets thicker by re-running synthesis. The gate enforces that discipline.

"Stop at the first fail in pipeline order" matters because defects cascade. If the spine is broken (D2), every downstream judgment is noise — there's no point critiquing the voice of an article that doesn't have an argument yet. Fix upstream, then re-judge. This is the same reason the photon pipeline runs PROCESS before COMBINE: order is load-bearing.

The perfectionism check (P1) is the one I care most about and it's deliberately phrased as *name it or it isn't there.* This is the membrane against self-deception. Every writer believes their piece has a special spark; the gate refuses the belief and demands the noun. If you can't point at the crafted surplus and say "that — that line, that framing, that's the thing" — then the reader won't find it either, because it isn't real. Carbon's perfectionism doctrine (blueprint file 04) says every paying stranger is buying a nameable surplus. This check is that doctrine made executable: nameable, or it fails.

And the reason the gate FAILS borderline pieces rather than passing them: the whole strategic premise (file 12, the 5-6 year window) is *depth over volume.* Volume that's "fine" is exactly what detection will catch and what readers forget. The gate's strictness is not perfectionism for its own sake — it's the survival trait. Five pieces that pass this gate beat fifty that don't, because the five compound and the fifty evaporate. Better to ship five real diamonds than fifty cut-glass fakes.

---

## LINKS

- Enforces: writing-department `OUTPUT_CONTRACT.md` (the 6 gates) + blueprint `04 - PERFECTIONISM_DOCTRINE.md` (the surplus) + this engine's diamond integrity.
- On PASS: hand to Content Distribution working company (`.\..\..\02 - content-distribution\`) for the platform decomposition + publish kit (blueprint file 05 omnichannel + spec 03 decomposition).
- Previous: `04 - PROMPT_voice_humanization.md`. Chain complete.
