# Stage 03 — DRAFT (the apex)

Diamond position: the visible top layer. The 10% the reader sees, sitting on the 90% they don't. Written FROM the spine — never from a cold prompt, never from the research directly.

Consumes: `synthesis/SPINE.md` (primary) + `observations/` particulars (for evidence).
Produces: `outputs/DRAFT.md` — structurally complete, not yet voiced.
Gate to pass before Stage 04: every spine claim is present and every claim traces to a particular (OUTPUT_CONTRACT traceability gate).

---

## THE PROMPT (runnable)

```
ROLE: You are a drafter. The spine is built and the evidence ledger is set. Your job is
to write the apex of the diamond — the visible article — by expressing the spine in full
prose. You are NOT discovering what to say; that decision is made. You are EXPRESSING it.
Do not introduce claims that are not on the spine. Do not summarize the research; argue
the spine.

INPUT:
- SPINE.md (THE ONE THING, the numbered spine claims, the tension, the evidence ledger,
  the reader move) — from Stage 02.
- The concrete particulars from Stage 01 sector 5.

TARGET: {{FORMAT}}  (e.g. Substack long-form 2000-5000 words / Medium / LinkedIn article)
PRIMARY KEYWORD (SEO): {{KEYWORD}}

WRITE the draft to this skeleton:

- LEAD (2-3 sentences): open on the reader's wrong model (spine "reader move", start
  state) or the central tension. Never open with "In today's world" or a definition.
  Earn the next sentence.
- BODY: one movement per spine claim, in spine order. Each movement:
    · states the claim,
    · spends specific particulars from the ledger as evidence (names, numbers, cases —
      this is where density goes; a movement with no particular is a hole),
    · connects forward to the next claim so the spine reads as one argument, not a list.
  Subheading every ~300-400 words.
- THE TURN: the place where the tension (spine part 3) is confronted head-on. This is the
  article's spine made visible — do not soften it.
- CLOSE: land THE ONE THING. The reader should leave at the spine's "end state." End on a
  specific image or consequence, not a summary of what was just said.

RULES:
- Every paragraph must carry information. If a paragraph could be deleted with no loss of
  meaning, delete it. (Transitions that only announce structure — "Now let's look at" —
  are deletable.)
- Spend the particulars. An article's density is the ratio of specifics to generalities.
  Front-load specifics; starve the abstractions.
- Do NOT yet worry about voice/rhythm/humanity — that is Stage 04's job. Get the
  structure and the argument right. A well-argued robotic draft is the correct output of
  this stage; a smooth voiceless summary is not.
- Mark every claim's evidence inline as [src: observation-N] so traceability is checkable
  at the gate. Stage 04 will strip these markers.
```

Slots: `{{FORMAT}}`, `{{KEYWORD}}`.

---

## WHY THIS SHAPE (lead)

The single most important instruction in this prompt is: *you are expressing a decision, not making one.* When people let a model "write the article," they're asking it to decide the argument AND express it in the same pass — and it does both badly, because deciding-while-writing produces the flat summary again. By the time we reach Stage 03, every hard decision is already made and sitting in SPINE.md. The draft is now a *rendering* problem, which models are genuinely excellent at. We've moved the hard cognition upstream where it belongs and left the model the job it's best at.

That's also why I deliberately split voice OUT of this stage. Trying to make a draft well-argued AND well-voiced in one pass is how you get a piece that's neither — the model spends its attention budget on sounding nice and under-argues, or vice versa. One job per pass. Structure here, soul next door. The "well-argued robotic draft is the correct output" line is there to stop the operator from prematurely judging Stage 03 by Stage 04's standard. A draft that reads a little mechanical but argues the spine cleanly is exactly right; we fix the mechanical-ness deliberately in 04, with technique, not with hope.

"Spend the particulars" is the density rule from the boundary stage paying off. Those 12+ specifics gathered in Stage 01 were a savings account. The draft is where you spend them. An article's resistance to detection AND its resistance to boredom are the same property: specifics-per-paragraph. AI slop is detectable and dull for the identical reason — it rounds every specific to the nearest generality. We refuse to.

---

## LINKS

- Policy: `lrp6-content-infrastructure/13 - blog-as-knowledge-production.md`; structure mirrors writing-department `OUTPUT_CONTRACT.md` article skeleton.
- Previous: `02 - PROMPT_synthesis_middle.md`. Next: `04 - PROMPT_voice_humanization.md`.
