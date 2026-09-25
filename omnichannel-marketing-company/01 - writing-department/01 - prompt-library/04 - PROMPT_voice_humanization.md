# Stage 04 — VOICE (humanization)

Diamond position: the polish that makes the apex read as a *person's* work, not a machine's. This is the stage that failed Carbon on the call — *"humanizing it — that's still a mess. It just isn't happening."* This file names the techniques that spec 12 left blank.

Consumes: `outputs/DRAFT.md` + a **voiceprint** of the named author (mandatory hard input).
Produces: `outputs/ARTICLE.md` — publishable, in the author's voice.
Gate to pass: passes the read-aloud test and carries no items from the kill-list below.

---

## THE TWO-PART PROMPT (runnable)

Humanization is two passes. Do not skip part A — it is *why* every "make it sound human" attempt fails.

### Part A — VOICEPRINT EXTRACTION (run once per author, reuse forever)

```
ROLE: You are a voice analyst. Given 3-5 samples of ONE author's real writing, extract
their idiolect — the fingerprint that makes their prose theirs. Output a VOICEPRINT the
drafter can write toward.

SAMPLES: {{3-5 PIECES OF THE AUTHOR'S OWN REAL WRITING}}

Extract:
1. SENTENCE RHYTHM — their distribution of sentence lengths. Do they run long-then-short?
   Use fragments? Average length? Quote 3 sentences that are unmistakably theirs.
2. PUNCTUATION SIGNATURE — em-dashes? semicolons? parentheticals? ellipses? How do they
   handle emphasis — italics, caps, repetition?
3. LEXICON & TICS — recurring words, characteristic transitions, words they'd never use,
   register (formal/wry/blunt). List 10+ signature words/phrases.
4. OPENINGS & CLOSINGS — how do they start a piece? How do they land one?
5. STANCE — do they hedge or assert? Address the reader directly? Use "I"? Tell stories or
   stay abstract?
6. THE TELL — the one thing that, if removed, would make the piece stop sounding like them.

OUTPUT: VOICEPRINT.md — a profile concrete enough that prose can be written TOWARD it.
```

### Part B — VOICE PASS (run per article)

```
ROLE: You are not "humanizing" this draft — that word produces failure. You are
RE-VOICING it: rewriting it so a specific named author could have written it, and so it
carries the natural variance of human prose. The argument and structure are fixed; change
only how it sounds.

INPUT: DRAFT.md + VOICEPRINT.md.

DO, in order:

1. IMPOSE BURSTINESS. Human prose varies wildly in sentence length; AI prose is uniform.
   Break the uniformity: follow a 35-word sentence with a 4-word one. Let one paragraph
   run; cut the next to a single line. Manufacture rhythm. This single move does more for
   "reads as human" than any other.

2. APPLY THE VOICEPRINT. Rewrite openings/closings/transitions in the author's signature.
   Insert their tics, their punctuation habit, their register. Write toward THE TELL.

3. KILL THE AI TELLS (delete or rewrite every instance):
   - "It's important to note / worth noting" · "In today's fast-paced world" ·
     "In conclusion / In summary" as an opener · "Moreover / Furthermore / Additionally"
     ladders · the "not only X, but also Y" reflex · "plays a crucial/vital/pivotal role"
     · "navigate the landscape / realm / world of" · "delve into" · "testament to" ·
     "when it comes to" · perfectly balanced tricolons (three items, equal length, every
     time) · hedging every claim · restating the intro as the conclusion · the smooth
     even paragraph where every sentence is 15-20 words.

4. INJECT THE HUMAN FRICTION. Add, where it fits the author: one aside or parenthetical
   thought; one place where the writer shows a position rather than surveying positions;
   one specific over a smooth generality; if the voiceprint allows it, one sentence that
   starts with "And" or "But." Real writing has texture and a pulse. Leave fingerprints.

5. KEEP ONE DELIBERATE IMPERFECTION. A short tangent, an unresolved aside, a slightly
   unpolished but characterful line. Machine prose is flawless and that flawlessness is
   itself the tell. Do not sand it perfectly smooth.

6. READ-ALOUD TEST. Read it as if speaking. Anywhere you'd never say it that way out loud,
   rewrite until you would. If it doesn't sound like the author *talking*, it isn't done.

DO NOT touch: the spine claims, the evidence, the traceability. Voice only.
OUTPUT: ARTICLE.md, plus a one-line VOICE NOTE: "Voiced toward [author]; tells killed: N;
read-aloud: PASS."
```

---

## WHY THIS SHAPE (lead)

This is the file Carbon most needed, so I'm going to be exact about why "humanize this" never works and what does.

**Why "make it sound human" fails.** When you tell a model to humanize, you give it no target. "Human" is an average, and the model's failure mode IS regression to an average — so you ask it to fix averageness by aiming at averageness. It produces a *differently* bland text. There is no such thing as "human in general" to write toward. There are only specific humans. This is the entire reason Part A exists and is mandatory: you do not humanize toward humanity, you re-voice toward **one named author with an extractable fingerprint.** The partner's car blog couldn't be humanized because we were humanizing toward nobody. Give the engine her own three best pieces of writing and the problem becomes tractable in one pass.

**Why my 2021 dissertation hit 0% detection on GPT-3-era tools** — weaker models than today's — and why it matters here. Two reasons, both reproduced in this prompt. First: the content had real research density (Stages 01-03), so there was genuine specificity that detectors read as human, because hollowness-dressed-as-fluency is exactly the signal they catch. Second: I wasn't writing toward "academic English," I was writing toward *my own* voice, which the model could match because I fed it my own prior writing. Density plus voiceprint. Detection has improved since, which is why Carbon's 5-6 year window is real — but the method's logic is unchanged: detectors catch *emptiness and uniformity*, and this stage attacks uniformity (burstiness, friction, deliberate imperfection) while Stages 01-03 already killed emptiness.

**Burstiness first, because it's the highest-leverage move.** "Perplexity and burstiness" is the actual axis most detectors score. AI writes sentences of monotonously similar length and predictability. Humans spike and crash — a long winding thought, then a hammer. Manufacturing that variance does more than any word-swap. I put it as step 1 deliberately.

**The kill-list is empirical, not theoretical.** Every phrase on it is a genuine model tell I've watched flag piece after piece. "Delve," "testament to," "navigate the landscape," the Moreover-ladder, the perfect tricolon, the conclusion that just restates the intro. These are the tics. A human editor's eye skips them; a detector's model lights up on them; a discerning reader feels the machine behind them. Killing them by checklist is mechanical and reliable — which is exactly why it belongs in a prompt rather than in someone's hoped-for good taste.

**The deliberate imperfection (step 5) is the counterintuitive one** and I want CE to hold onto it, because the instinct is to polish it back out. Flawlessness is a tell. A real writer leaves a fingerprint smudge — a tangent they loved too much to cut, a line that's more characterful than correct. That smudge is not a defect to be cleaned; it is the proof of a hand. Sand it away and you've rebuilt the machine.

One ethical line, stated plainly so CE enforces it: this stage is for making genuinely-researched, genuinely-authored work read in the author's true voice and not like sterile generated text. It rides on Stages 01-03 having produced real substance. It is not a tool for passing empty fabricated content off as human — that path fails the gate at Stage 05 (no traceable research = no publish) by design. Voice without substance is the exact slop we're eliminating, not producing.

---

## LINKS

- Policy this makes runnable: `.\..\..\03 - architecture-governance\01 - content-infrastructure\12 - ai-era-publishing-methodology.md` (it asserts the 5-6 year window and "low-detectability techniques" but names none — they are named here).
- Requires: a `voiceprints/[author].md` in the writing-department (CE: create this folder on install).
- Lands in: writing-department `OUTPUT_CONTRACT.md` → `outputs/ARTICLE.md`.
- Previous: `03 - PROMPT_draft_apex.md`. Next: `05 - PROMPT_perfection_gate.md`.
