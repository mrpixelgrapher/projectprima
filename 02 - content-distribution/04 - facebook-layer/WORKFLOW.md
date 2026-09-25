# Facebook Layer — Workflow

Type: workflow document — operationalizes Facebook as a strategic audience-acquisition layer focused on older, financially capable demographics not effectively captured by LinkedIn, Twitter/X, or Threads.

## Authority

This workflow sits under the Content Distribution department's governance:

- Parent: `.\..\00 - ENTRY.md` (Content Distribution function folder)
- Department rule: `.\..\WORKING_RULES.md` Rule 1 (Translation, Not Syndication) + Rule 2 (Substack Is The Anchor).
- Upstream: Substack Hub (`.\..\01 - substack-hub\`) — provides canonical master source and decomposition seeds.
- Downstream: no downstream consumer — Facebook is a terminal amplification layer.
- Governance: `.\..\..\..\..\..\02 - WORKSPACE_META\03 - folder-governance\RESEARCH_FIRST_CONTENT_PRODUCTION.md`

## Source intent

Derived from `.\..\..\..\..\..\99 - ARCHIVE\tech-bro\2026-06-13-lrp6-infrastructure-buildout\infrastructure\06 - build-facebook-demographic-reach-layer.md`. Facebook is positioned as a strategic audience-acquisition layer targeting older, financially capable demographics — mature readers, professionals approaching retirement, business owners, investors, and other high-income segments — who are not effectively captured by LinkedIn, Twitter/X, or Threads.

## Position in the hub-and-spoke

```
Substack Hub (canonical master source)
    ↓
Facebook Layer (demographic-reach derivative)
    ↓
(direct Substack link in post body)
```

**Direction of flow:** Substack → Facebook, never reverse.

## Why Facebook when LinkedIn + Twitter + Threads exist

| Platform | Primary audience | What it misses |
|---|---|---|
| LinkedIn | B2B professionals, active career-stage | Mature readers, retirees, business owners not in active career mode |
| Twitter/X | Process / methodology audiences | Demographics that don't engage with threads |
| Threads | Outcomes / discussion audiences | Older demographics not on Threads |
| **Facebook** | **Mature readers, professionals approaching retirement, business owners, investors, high-income segments** | — |

The strategic objective: expand audience diversity across the ecosystem and systematically funnel high-value readers from platform-owned attention into creator-owned channels (Substack + website + knowledge base).

## Workflow steps (per Facebook derivative)

| Step | Action | Input | Output |
|---|---|---|---|
| 1 | Receive decomposition seeds | Substack Hub `decomposition-seeds.md` (seeds: core insight, implication, visual — mapped to Facebook per Substack OUTPUT_CONTRACT) | Seed selection |
| 2 | Map to audience persona | Persona set (mature reader, approaching-retirement professional, business owner, investor, high-income segment) | Persona-aligned angle brief |
| 3 | Rewrite in Facebook native register | Seed + persona + Substack article (for reference, NOT copy-paste) | Draft Facebook post |
| 4 | Add visual assets | Media Department outputs (custom graphics, strong visual storytelling) | Compelling visual |
| 5 | SEO-informed messaging check | SEO keywords from Substack article `metadata.json` | Messaging aligned with discoverability |
| 6 | Verify translation discipline | Rule 1 test: native Facebook user would find this natural, not a repost | Pass/fail verdict |
| 7 | Schedule | 30-day deployment framework (per `.\..\WORKING_RULES.md` Rule 4) | Scheduled publication slot |
| 8 | Publish + funnel | Published post + Substack link in post body + website / knowledge-base links | Live Facebook post URL + recorded funnel |

## Audience personas

| Persona | Core interest | Emotional triggers | Messaging angle |
|---|---|---|---|
| Mature reader (50+) | Wisdom, perspective, long-view thinking | Legacy, reflection, accumulated experience | "Here's what I've learned over decades of doing this" framing |
| Approaching-retirement professional | Transition planning, next-phase expertise | Security, relevance, continued contribution | "Your expertise has value beyond your current role" framing |
| Business owner | Operational leverage, scalability, risk management | Growth, protection, succession | "Here's how to build something that outlasts you" framing |
| Investor | Quality signals, durable value, long-term returns | Confidence, evidence, track record | "Here's the research behind the claim" framing |
| High-income segment generally | Premium insight, exclusive depth, differentiated thinking | Status, access, quality | "Here's the deeper analysis most people skip" framing |

## Content themes that resonate

Across the five personas, the following themes land:

- Legacy / long-view thinking
- Transition / next-phase planning
- Operational leverage / scalability
- Research-backed claims (depth over speed)
- Differentiated insight (premium, not commoditized)
- Strategic windows (time-sensitive, opportunity-based)

**Themes that do NOT land on Facebook** (push to other platforms):
- Process breakdowns and execution mechanics (Twitter/X territory)
- B2B thought leadership and networking (LinkedIn territory)
- Outcomes-and-discussion quick takes (Threads territory)

## Visual discipline

Facebook prioritizes strong visual storytelling. Every Facebook post has at least one compelling custom graphic from the Media Department. Visuals should be:
- High-production-value (Facebook audiences expect polish).
- Storytelling-oriented (a single image that tells a story, not just illustrates a point).
- On-brand and professional-credibility-aligned.

Stock imagery without provenance is prohibited (per Substack Hub OUTPUT_CONTRACT non-negotiable #3).

## SEO-informed messaging

Facebook content must carry SEO discipline from the Substack source article:

- Primary keyword appears naturally in post copy.
- Messaging angles reflect the Substack article's SEO keyword set.
- Where appropriate, Facebook post text can reinforce the Substack article's SEO performance through consistent terminology (this is not keyword stuffing; it is cross-platform semantic consistency).

The objective: maximize organic reach and reduce dependence on platform algorithms.

## Funnel discipline

Facebook content is an entry point into controlled assets:

| Funnel target | How Facebook post links |
|---|---|
| Substack (primary) | Direct link in post body |
| Website (secondary) | Link in post body or first comment |
| Knowledge base (tertiary) | Link in first comment if relevant |

**Rule:** every Facebook post must link to at least one controlled asset. No orphan posts.

## Integration with 30-day deployment framework

Facebook participates in the same 30-day framework as the other platforms (per `.\..\WORKING_RULES.md` Rule 4) but its publication slot is chosen to avoid overlap with the LinkedIn, Twitter, and Threads slots for the same article.

**Week assignment discipline:**
- Facebook publications should generally land in week 2 or week 3 of the 30-day framework (week 1 is LinkedIn's core-insight exposure; week 4 is recap).
- Avoid same-day publication with any other platform derivative of the same article.

## Brand-narrative consistency

Facebook adaptation must maintain consistency with the overall brand narrative. Persona-aligned does not mean brand-deviant.

**Rule:** every Facebook post must be recognizable as the same voice that publishes on LinkedIn, Twitter, and Threads — translated for persona, not rebranded.

## Read order (cold instance arriving at this file)

1. This file — see the demographic-reach workflow.
2. `.\OUTPUT_CONTRACT.md` — canonical structure of every Facebook derivative.
3. `.\..\WORKING_RULES.md` — department rules this workflow obeys (especially Rules 1, 2, 4).
4. `.\..\01 - substack-hub\OUTPUT_CONTRACT.md` — upstream decomposition seeds this layer consumes.

## Update rule

When this workflow changes, update this file first, then update `.\..\WORKING_RULES.md` if the change affects a department rule, then update `.\..\00 - ENTRY.md` if the workflow diagram or ancestry changes.
