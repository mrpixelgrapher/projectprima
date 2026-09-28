# Output Contract — Writing Department

## Required Output Structure

Every Writing Department execution produces:

### 1. Research Folder (mandatory)

```
research-[topic-slug]/
├── sources/           ← Minimum 3 independent source categories
├── observations/      ← Extracted patterns (minimum 5 observations)
├── synthesis/         ← Original insights (minimum 1 not in any single source)
└── outputs/           ← Published article(s)
```

### 2. Published Article (mandatory)

**Structure:**
```markdown
# [Title — SEO-optimized, specific, benefit-driven]

## Lead (2-3 sentences)
Hook: the specific problem or question this article resolves.

## Body (2000-5000 words)
Subheadings every 300-400 words.
Internal links to related articles.
Custom graphics at minimum 2 per article.

## Key Takeaways (3-5 bullets)

## Call to Action
Subscribe link + next article recommendation.
```

**Verification checks (must all pass):**

| # | Gate | Test |
|---|---|---|
| 1 | Traceability | Every claim links to a research artifact |
| 2 | Originality | At least 1 insight not present in any single source |
| 3 | Depth | 3+ independent source categories cited |
| 4 | Structure | Subheadings, internal links, graphics present |
| 5 | SEO | Primary keyword in title, H1, first 100 words |
| 6 | Collapse | No speculative, aspirational, or unsupported content |

### 3. Decomposition Seeds (mandatory, for Content Distribution handoff)

After publication, extract:

| Seed | Content | Target Platform(s) |
|---|---|---|
| Core insight | Single most important claim (1-2 sentences) | All platforms |
| Process breakdown | How the result was achieved (step-by-step) | Twitter/X, Medium |
| Contrarian angle | What this challenges (1 sentence + evidence) | LinkedIn, Twitter/X |
| Framework/model | Named reusable structure | LinkedIn, Instagram |
| Implication | What changes because of this (1-2 sentences) | Threads, Facebook |
| Visual concept | Diagrammable concept description | Instagram, all |

### 4. Audit Trail (mandatory)

Every output file must include at the bottom:

```markdown
---
## Audit Trail
- Research folder: [path]
- Sources consulted: [count] across [categories]
- Observations extracted: [count]
- Original insights: [count]
- Pre-drafting gate: PASSED [date]
- Platform seeds extracted: [count]
- Distribution handoff: [date or PENDING]
```

## Format Source

All output follows CE collapse rules and TERMINOLOGY.md canonical terms.

## Non-Negotiable Rules

1. No article published without a research folder on disk.
2. No article published without passing all 6 verification checks.
3. No article published without decomposition seeds extracted.
4. No article published without an audit trail.
5. Research folders are never deleted — they are permanent assets.

## Gate 7 — Crafted Surplus (appended 2026-09-25, session S001)

Added because `.\..\03 - architecture-governance\02 - doctrine-enforcement\PERFECTIONISM_ENFORCEMENT.md` Rule 1 names this contract directly: "Writing department OUTPUT_CONTRACT gates → add gate 7: crafted_surplus". The stage-05 gate prompt already checks it as P1 (`.\01 - prompt-library\05 - PROMPT_perfection_gate.md`). This brings the contract into line with the prompt.

| # | Gate | Test |
|---|---|---|
| 7 | Crafted surplus | Name the specific element that exceeds expectation. If you cannot name it, the article is not done. Decoration, aspirational claims and generic personalisation do not count (the doctrine's anti-theater clause). |

Non-negotiable rule 2 ("all 6 verification checks") now covers 7 checks, under the doctrine above. The Audit Trail gains one line:

    - SURPLUS: [one line naming the crafted surplus]
