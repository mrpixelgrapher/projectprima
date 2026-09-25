# Twitter/X + Threads Layer — Workflow

Type: workflow document — operationalizes Twitter/X and Threads as two distinct platform-native amplification channels within the content-distribution department. The two platforms share one subfolder because they are fed by the same Substack decomposition seeds and produce complementary derivatives from the same article.

## Authority

This workflow sits under the Content Distribution department's governance:

- Parent: `.\..\00 - ENTRY.md` (Content Distribution function folder)
- Department rule: `.\..\WORKING_RULES.md` Rule 1 (Translation, Not Syndication) + Rule 2 (Substack Is The Anchor).
- Upstream: Substack Hub (`.\..\01 - substack-hub\`) — provides canonical master source and decomposition seeds.
- Downstream: no downstream consumer — Twitter/X and Threads are terminal amplification layers.
- Governance: `.\..\..\..\..\..\02 - WORKSPACE_META\03 - folder-governance\RESEARCH_FIRST_CONTENT_PRODUCTION.md`

## Source intent

Derived from `.\..\..\..\..\..\99 - ARCHIVE\tech-bro\2026-06-13-lrp6-infrastructure-buildout\infrastructure\05 - build-twitter-threads-distribution-layer.md`. Two distinct audience entry points per Substack article:

- **Twitter/X** captures audiences interested in **process and expertise** (HOW outcomes were achieved).
- **Threads** captures audiences interested in **outcomes and discussion** (WHAT outcomes mean, what changes, what happens next).

Both funnel back to Substack.

## Position in the hub-and-spoke

```
Substack Hub (canonical master source)
    ↓
    ├── Twitter/X Layer (process / methodology derivative)
    │     └── thread ends with Substack link
    └── Threads Layer (implications / outcomes derivative)
          └── direct Substack link in post
```

**Direction of flow:** Substack → Twitter/X and Substack → Threads, never reverse.

## Why two platforms share one subfolder

Twitter/X and Threads derivatives for a single Substack article are paired — they come from the same seeds and represent complementary angles on the same content. Grouping them in one folder keeps the per-article derivative set coherent:

```
[article-slug]/
├── twitter-thread.md
├── threads-post.md
├── metadata.json        ← covers both platforms
└── visual-assets/       ← shared or platform-specific assets
```

## Workflow steps (per Twitter+Threads derivative pair)

| Step | Action | Input | Output |
|---|---|---|---|
| 1 | Receive decomposition seeds | Substack Hub `decomposition-seeds.md` (seeds: process, implication — per Substack OUTPUT_CONTRACT seed-to-platform mapping) | Seed selection |
| 2 | Split into two angles | Process seed → Twitter; Implication seed → Threads | Angle brief for each platform |
| 3a | Twitter thread draft | Process angle + Twitter thread template | Draft thread (5-12 tweets) |
| 3b | Threads post draft | Implication angle + Threads post template | Draft Threads post |
| 4 | Add visual assets | Media Department outputs (custom graphics, visual storytelling) | Platform-appropriate visuals |
| 5 | Verify translation discipline | Rule 1 test for each: native user would find it natural, not a repost | Pass/fail per platform |
| 6 | Schedule | 30-day deployment framework (per `.\..\WORKING_RULES.md` Rule 4) | Scheduled slots |
| 7 | Publish + funnel | Published posts + Substack link | Live URLs + recorded Substack funnel |

## Twitter/X framework — process / methodology

Twitter/X content pulls back the curtain on the underlying operating system behind the work.

**Content focus:**
- Methodology
- Process breakdowns
- Decision-making frameworks
- Research systems
- Execution mechanics
- Lessons learned
- Thought leadership (process-oriented)

**Thread structure (5-12 tweets):**

| Tweet | Role |
|---|---|
| 1 | Hook — the outcome or question that interrupted passive scrolling |
| 2-4 | The methodology / process breakdown |
| 5-8 | Decision frameworks, research systems, execution mechanics |
| 9-11 | Lessons learned, edge cases, what would change next time |
| 12 | Funnel — Substack link + invitation to read the full article |

**Thread discipline:**
- Never paste Substack text directly into a tweet. Every tweet is a translation.
- Thread must stand alone — a reader who never clicks through still gets the process insight.
- Final tweet is the only tweet that links to Substack (intermediate links break the thread's native feel).

## Threads framework — outcomes / discussion

Threads content expands on the consequences, applications, and lived experiences associated with the concepts.

**Content focus:**
- Real-world implications
- Practical outcomes
- Behavioral changes
- Business impacts
- Deeper discussions arising from the ideas

**Post structure (single post, up to 500 characters + images):**
- Hook — the implication or question
- Body — what changes, what happens next, why it matters
- Visual — custom graphic that illustrates the implication
- Funnel — direct Substack link in post (Threads allows external links without algorithmic penalty)

**Post discipline:**
- Never paste Substack text. Translation, not syndication.
- Custom graphic mandatory (visual storytelling emphasis on Threads).
- Post must invite discussion, not just broadcast.

## Visual discipline

Both platforms require Media-Department-produced visual assets:

| Platform | Visual requirement |
|---|---|
| Twitter/X | At least one custom graphic per thread (usually tweet 1 or 2); infographic for process breakdowns optional |
| Threads | Mandatory custom graphic illustrating the implication |

Stock imagery without provenance is prohibited (per Substack Hub OUTPUT_CONTRACT non-negotiable #3).

## Funnel discipline

| Platform | Funnel placement |
|---|---|
| Twitter/X | Final tweet of the thread (Substack link) |
| Threads | Direct Substack link in post body |

## Audience-split discipline

The strategic objective is explicit: use Twitter/X to capture process/expertise audiences, use Threads to capture outcomes/discussion audiences. These are distinct segments; content must not collapse them.

**Anti-pattern (detect and reject):**
- Same content on both platforms → rewrite one.
- Thread on Threads, or outcome-discussion post on Twitter/X → swap or rewrite.
- Both platforms published on the same day for the same article → space them within the 30-day framework (per `.\..\WORKING_RULES.md` Rule 4).

## Read order (cold instance arriving at this file)

1. This file — see the dual-platform workflow.
2. `.\OUTPUT_CONTRACT.md` — canonical structure of Twitter + Threads derivative pair.
3. `.\..\WORKING_RULES.md` — department rules this workflow obeys (especially Rules 1, 2, 4).
4. `.\..\01 - substack-hub\OUTPUT_CONTRACT.md` — upstream decomposition seeds this layer consumes.

## Update rule

When this workflow changes, update this file first, then update `.\..\WORKING_RULES.md` if the change affects a department rule, then update `.\..\00 - ENTRY.md` if the workflow diagram or ancestry changes.
