# Stage 02 — SYNTHESIS (the middle of the diamond)

Diamond position: the middle layer. The stage everyone skips. The stage where value is actually *made* rather than gathered or arranged.

Consumes: `research-[slug]/sources/` + `observations/` from Stage 01.
Produces: `research-[slug]/synthesis/SPINE.md` — a thinking document, NOT prose.
Gate to pass before Stage 03: there is at least one stated insight that appears in **no single source** (the OUTPUT_CONTRACT "originality" gate, satisfiable only here).

---

## THE PROMPT (runnable)

```
ROLE: You are a synthesist. The research boundary is drawn. Your job is to compress it
to a spine — the load-bearing structure the article will hang on. You are still NOT
writing the article. You are deciding what it will ARGUE and what it will deliberately
leave out. Output is a reasoning document, not prose.

INPUT: the full BOUNDARY MAP from Stage 01 (all seven sectors).

Produce SPINE.md with these six parts:

1. THE ONE THING — In a single sentence: what does this piece know that the reader does
   not, and that no single source in the boundary states outright? This is the article's
   reason to exist. If you cannot fill this from the boundary, the boundary is too thin —
   STOP and return to Stage 01. Do not manufacture an insight to fill the slot.

2. THE SPINE — The 3-5 load-bearing claims, in argument order, that carry THE ONE THING
   from the reader's current wrong model to the new understanding. Each claim is a
   vertebra: it must connect to the one before and the one after. Number them.

3. THE TENSION — Every piece worth reading holds a tension it resolves or honestly leaves
   open. State the central tension from the boundary's "live disputes" / "contradictions"
   sectors. The article earns its keep by handling this, not by ignoring it.

4. THE EVIDENCE LEDGER — For each spine claim, name which specific particulars from
   boundary sector 5 will support it. This is where the article gets its density. If a
   spine claim has no concrete particulars behind it, it is an opinion, not a claim —
   either find evidence or cut it.

5. THE DELIBERATE OMISSIONS — Name 3+ things from the boundary you are choosing NOT to
   include, and why. A piece that tries to say everything says nothing. Cutting is the
   synthesist's real skill. What you leave out shapes the diamond as much as what you keep.

6. THE READER MOVE — One sentence: the reader believed ___ when they arrived; they
   believe ___ when they leave. If these two are the same, there is no article.

OUTPUT: SPINE.md. Reasoning, claims, ledger — no paragraphs of article prose.
End with: "ORIGINALITY CHECK: the insight in part 1 appears in source(s): NONE / [list].
If any source already states it outright, sharpen until it is genuinely yours."
```

---

## WHY THIS SHAPE (lead)

This is the stage the 16 specs name but no one built, and it's the most important one, so I'm giving it the most reasoning.

Here is the failure I have watched a hundred times, including in my own early work: a writer does real research (boundary is fine), then goes straight to drafting. The result is a *summary*. Competent, sourced, readable — and forgettable, because it has no spine. It reports what's out there. It doesn't argue anything. The reader finishes it and cannot tell you the one thing it said, because it didn't say one thing, it said forty things evenly. That flatness is the "value loss" Carbon described on the call — *"the sense that something is missing."* What's missing is the middle of the diamond: the compression pass where forty gathered things get crushed into one load-bearing insight.

The middle is where a human stops being a search engine and starts being a mind. AI is extraordinary at sectors 1-5 of the boundary and genuinely weak here, because synthesis-to-a-single-spine requires *taste* — choosing what matters, what to cut, what tension to honor. That's why this prompt forces "THE ONE THING" as a hard single-sentence slot with a STOP condition: it refuses to let the work proceed on gathered material alone. The originality gate in the writing-department's OUTPUT_CONTRACT ("at least 1 insight not present in any single source") is mathematically impossible to satisfy if you skip this stage — you can only ever satisfy it *here*, by compression.

The deliberate-omissions part (5) is the one people resist most and it's the most important. Early me wanted to use all the research because gathering it was expensive. Mature me knows the cut IS the craft. The diamond gets its shape from the facets you grind *away*. A spine that carries everything carries nothing.

And the discipline of "no prose yet" again: if you let synthesis and drafting collapse into one step, the spine never gets built — you just start writing and hope an argument emerges. It rarely does. Separating them is the entire trick. Research is one mind. Synthesis is a second. Drafting is a third. Three passes, three different cognitive jobs. That separation, not the model, is the eight-year-matured process.

---

## LINKS

- Policy: this is the unbuilt "middle layer" in `lrp6-content-infrastructure/14 - research-first-blog-generation.md`; it is what makes OUTPUT_CONTRACT gate 2 (originality) achievable.
- Lands in: writing-department `OUTPUT_CONTRACT.md` → `synthesis/`.
- Previous: `01 - PROMPT_boundary_research.md`. Next: `03 - PROMPT_draft_apex.md`.
