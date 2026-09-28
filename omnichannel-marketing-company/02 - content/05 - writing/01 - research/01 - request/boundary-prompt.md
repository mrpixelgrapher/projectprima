# Boundary prompt (writing · research · request)

**Used by:** `02 - content/05 - writing/01 - research/01 - request/00 - ENTRY.md` (filled per piece and sent to ARENA) and `02 - boundary/00 - ENTRY.md` (the seven sectors the map is built on). **Origin:** `99 - archive/2026-09-28-restructure/01 - writing-department/01 - prompt-library/01 - PROMPT_boundary_research.md`. The prompt block and its reasoning are carried over verbatim; the stage ENTRY fills its slots and says where its output goes.

## THE PROMPT (runnable — paste into a research-capable model / Arena)

```
ROLE: You are a domain cartographer, not a writer. Your only job in this pass is to
draw the complete boundary of a topic. You will NOT draft anything. A single sentence
of article prose in your output is a failure.

TOPIC: {{TOPIC}}
THE ANGLE THE AUTHOR CARES ABOUT: {{ANGLE}}
DOMAIN: {{DOMAIN}}

Produce a BOUNDARY MAP with these seven sectors. For each, go wider than feels
necessary — the cost of a missing sector is a hollow article later.

1. CORE CLAIMS — What does the informed consensus actually hold? State 5-10 claims a
   domain expert would consider settled. For each, name WHO holds it (a source category,
   not "studies show").

2. LIVE DISPUTES — Where do credible people disagree? State each disagreement as
   "Camp A holds X because P; Camp B holds Y because Q." Minimum 3. If you find none,
   you have not gone deep enough — every real topic has live edges.

3. ADJACENT FIELDS — What neighbouring domains touch this topic and import ideas into it?
   Name 3-5 and the specific idea each contributes.

4. HISTORICAL ARC — How did the current state come to be? Name the 3-4 inflection points
   that changed how the field thinks. Dates, names, specific shifts.

5. CONCRETE PARTICULARS — Harvest the specifics that AI prose usually rounds off:
   named examples, real numbers, dated events, proper nouns, edge cases, exceptions.
   Minimum 12. These are the anti-slop reserve; the draft will spend them.

6. CONTRADICTIONS & UNKNOWNS — What is genuinely unresolved, counterintuitive, or
   commonly-believed-but-wrong? This sector is where original insight will later come
   from. Be specific about WHAT is unknown, not just that uncertainty exists.

7. THE READER'S WRONG MODEL — What does a smart non-expert currently believe about this
   topic that is incomplete or wrong? The article's job is to move them off it; name it
   precisely.

OUTPUT FORMAT:
- One section per sector, sources/categories attached to every claim.
- End with a SATURATION SELF-CHECK: "Boundary nameable? YES/NO. If NO, the three sectors
  still thin are: ___." Be honest — a NO here is correct and useful; a false YES poisons
  everything downstream.

RULES:
- Source categories, never "research shows" / "experts agree" / "it is widely known."
- If you don't actually know a particular, mark it [VERIFY] rather than inventing it.
  A marked gap is an asset; a confident fabrication is the one unrecoverable failure.
- No prose, no outline, no thesis yet. Boundary only.
```

Slots: `{{TOPIC}}`, `{{ANGLE}}`, `{{DOMAIN}}`. If the model can web-search, let it; if not, this becomes the Arena/Carbon-interface research brief (links below).

---

## Why this shape

The whole engine lives or dies here, so let me say plainly why it's built like this.

The partner's car blog failed for one structural reason: there was no boundary pass. She went topic → draft. The AI gave her something that *felt* fine, because AI prose always feels fine — it's optimized to feel fine. But it was the bottom slice of the diamond presented as the whole stone. There was nothing specific in it because nothing specific had been *gathered*. You cannot synthesize what you never collected.

My dissertation in 2021 — 120 pages, two days, 0% AI-detected on GPT-3-era tools — was not an AI feat. It was a boundary feat. I had studied research methodology, so before I let the model write a word, I had drawn the entire edge of the topic: every camp, every dispute, every particular. By the time drafting started, the model wasn't *generating* content, it was *arranging* content I had already made dense. That is the only reason it read as human and survived detection: there was real intellectual mass behind every sentence. Detection catches emptiness dressed as fluency. It does not catch density.

So this prompt is deliberately forbidden from writing. The single hardest discipline in AI-assisted work is making the model *not draft early* — it desperately wants to, because drafting is what it's rewarded for. Sector 5 (concrete particulars, minimum 12) and sector 6 (contradictions) are the two that matter most, because those are the only places original synthesis can come from in Stage 02. The `[VERIFY]` rule exists because a fabricated particular is worse than a missing one — it's the failure that destroys trust and can't be undone after publication.

The saturation self-check is the diamond's lower gate. A NO is the system working. Most bad writing is a premature YES.

---
