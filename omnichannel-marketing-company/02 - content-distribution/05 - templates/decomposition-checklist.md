# Content Decomposition Checklist

## Purpose

Run this checklist after every Substack article publication. Produces the platform-native derivatives for the 30-day deployment cycle.

## Article Reference

- **Title:** [article title]
- **Published:** [date]
- **Substack URL:** [link]
- **Content cluster:** [which cluster this belongs to]

---

## Step 1: Extract Decomposition Seeds

From the published article, extract these 6 seeds:

| # | Seed Type | Content (1-2 sentences) | Target Platforms |
|---|---|---|---|
| 1 | **Core insight** — the single most important claim | | All |
| 2 | **Process breakdown** — how the result was achieved | | Twitter/X, Medium |
| 3 | **Contrarian angle** — what this challenges | | LinkedIn, Twitter/X |
| 4 | **Framework/model** — named reusable structure | | LinkedIn, Instagram |
| 5 | **Implication** — what changes because of this | | Threads, Facebook |
| 6 | **Visual concept** — diagrammable concept | | Instagram, all |

**Gate:** All 6 seeds extracted? ☐ YES → continue ☐ NO → re-read article

---

## Step 2: Write Platform Derivatives

Use the templates in `.\..\05 - templates\` for each platform.

| # | Platform | Template | Seed(s) Used | Status |
|---|---|---|---|---|
| 1 | LinkedIn | `linkedin-post-template.md` | Core insight + framework | ☐ Drafted ☐ Scheduled ☐ Published |
| 2 | Twitter/X | `twitter-thread-template.md` | Process + contrarian | ☐ Drafted ☐ Scheduled ☐ Published |
| 3 | Threads | [write native: 100-300 words + 1 graphic] | Implication + core insight | ☐ Drafted ☐ Scheduled ☐ Published |
| 4 | Instagram | [carousel or infographic] | Visual concept + core insight | ☐ Drafted ☐ Scheduled ☐ Published |
| 5 | Medium | [condensed long-form: 800-1500 words] | Core insight + process | ☐ Drafted ☐ Scheduled ☐ Published |
| 6 | Facebook | [educational framing: 300-600 words] | Implication + core insight | ☐ Drafted ☐ Scheduled ☐ Published |

**Gate:** Each derivative passes the native-register test? (Would a native user find this natural, not a repost?) ☐ YES → continue

---

## Step 3: Schedule 30-Day Deployment

| Week | Focus | Content to Publish | Status |
|---|---|---|---|
| 1 | Core insight exposure | Main derivatives (all platforms) | ☐ |
| 2 | Process deep-dive | Twitter thread, LinkedIn case study, Instagram carousel | ☐ |
| 3 | Implications & discussion | Threads follow-up, LinkedIn poll, Facebook discussion | ☐ |
| 4 | Framework application | Instagram visual, Twitter mini-thread, LinkedIn framework post | ☐ |

---

## Step 4: Custom Graphics

| # | Platform | Graphic Type | Description | Status |
|---|---|---|---|---|
| 1 | LinkedIn | Framework diagram | | ☐ Designed ☐ Produced |
| 2 | Twitter/X | Process visual | | ☐ Designed ☐ Produced |
| 3 | Instagram | Carousel (5-10 slides) | | ☐ Designed ☐ Produced |
| 4 | Facebook | Opening image | | ☐ Designed ☐ Produced |

**Rule:** No stock photos. All graphics are custom and serve as intellectual compression mechanisms.

---

## Step 5: Link Verification

| Platform | Link Placement | Link Target | Verified |
|---|---|---|---|
| LinkedIn | First comment | Substack article URL | ☐ |
| Twitter/X | Final tweet | Substack article URL | ☐ |
| Threads | In post | Substack article URL | ☐ |
| Medium | Canonical link | Substack article URL | ☐ |
| Instagram | Bio link | Substack newsletter URL | ☐ |
| Facebook | In post | Substack article URL | ☐ |

---

## Completion

- [ ] All 6 seeds extracted
- [ ] All 6 platform derivatives drafted
- [ ] 30-day schedule populated
- [ ] Custom graphics designed/produced
- [ ] All links verified
- [ ] Week 1 content published

**Decomposition complete:** [date]
**Next article research domain:** [topic or "TBD"]

## Per-Variant Gate (appended 2026-09-25, session S001)

`.\..\..\03 - architecture-governance\02 - doctrine-enforcement\OMNICHANNEL_ENFORCEMENT.md` Rule 2 requires every channel variant to pass the perfection gate on its own. No per-variant gate was defined, and the Stage 05 gate prompt is shaped for a whole article. This gate only combines existing checks. It adds no new criteria.

A variant passes only if all four checks pass:

| # | Check | Source |
|---|---|---|
| 1 | Every row of that layer's "Output verification" table passes (live-URL rows excepted before publication) | the layer's `OUTPUT_CONTRACT.md`, e.g. `.\..\02 - linkedin-layer\OUTPUT_CONTRACT.md` |
| 2 | V1 read-aloud, V2 no kill-list tells, V3 no monotonous sentence length | `.\..\..\01 - writing-department\01 - prompt-library\05 - PROMPT_perfection_gate.md` |
| 3 | P1: crafted surplus named in one line | same file; `.\..\..\03 - architecture-governance\02 - doctrine-enforcement\PERFECTIONISM_ENFORCEMENT.md` Rule 1 |
| 4 | Rule 1 test: a native user of this platform finds it natural, not a repost. No sentence is copied verbatim from the Substack article or from another variant | `.\..\WORKING_RULES.md` Rule 1 |

Channels with no layer contract yet (website, Medium, Instagram) cannot pass check 1. Their variants stay BLOCKED until gap G-M04 closes.
