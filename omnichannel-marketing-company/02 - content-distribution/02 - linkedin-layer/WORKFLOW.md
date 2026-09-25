# LinkedIn Layer — Workflow

Type: workflow document — operationalizes LinkedIn as the B2B thought-leadership amplification channel within the content-distribution department.

## Authority

This workflow sits under the Content Distribution department's governance:

- Parent: `.\..\00 - ENTRY.md` (Content Distribution function folder)
- Department rule: `.\..\WORKING_RULES.md` Rule 1 (Translation, Not Syndication) + Rule 2 (Substack Is The Anchor).
- Upstream: Substack Hub (`.\..\01 - substack-hub\`) — provides the canonical master source and decomposition seeds.
- Downstream: no downstream consumer — LinkedIn is a terminal amplification layer.
- Governance: `.\..\..\..\..\..\02 - WORKSPACE_META\03 - folder-governance\RESEARCH_FIRST_CONTENT_PRODUCTION.md`

## Source intent

Derived from `.\..\..\..\..\..\99 - ARCHIVE\tech-bro\2026-06-13-lrp6-infrastructure-buildout\infrastructure\04 - build-linkedin-thought-leadership-layer.md`. LinkedIn is positioned as a strategic amplification channel that transforms long-form research, insights, and frameworks originating from the Substack Hub into platform-native professional content. Not a primary publishing destination.

## Position in the hub-and-spoke

```
Substack Hub (canonical master source)
    ↓
LinkedIn Layer (B2B thought-leadership derivative)
    ↓
(link back to Substack in first comment — algorithm deprioritizes external links in post body)
```

**Direction of flow:** Substack → LinkedIn, never reverse. Every LinkedIn post ends with a funnel to the Substack article.

## Workflow steps (per LinkedIn derivative)

| Step | Action | Input | Output |
|---|---|---|---|
| 1 | Receive decomposition seeds | Substack Hub `decomposition-seeds.md` (seeds: core insight, contrarian, framework — per Substack OUTPUT_CONTRACT seed-to-platform mapping) | Seed selection (1-3 seeds per post) |
| 2 | Select post template | `.\..\05 - templates\` (thought leadership, industry commentary, case-study breakdown, contrarian insight, legal/consulting perspective, founder lesson, framework-driven educational) | Template choice |
| 3 | Rewrite in LinkedIn native register | Seed + template + Substack article (for reference, NOT copy-paste) | Draft post in LinkedIn's professional tone, formatting conventions, engagement patterns |
| 4 | Add visual assets | Media Department outputs (custom graphics, visual frameworks, branded content assets) | Inline images or carousel PDF |
| 5 | Verify translation discipline | Rule 1 test: would a native LinkedIn user find this natural, or does it read like a repost? | Pass/fail verdict |
| 6 | Schedule | 30-day deployment framework (per `.\..\WORKING_RULES.md` Rule 4) | Scheduled publication slot |
| 7 | Publish + funnel | Published post + Substack link in first comment | Live LinkedIn post URL + recorded Substack funnel |

## Post templates

| Template | When to use | Seeds that fit |
|---|---|---|
| Thought leadership | Strategic positioning, industry direction | Core insight, Contrarian |
| Industry commentary | Current event or trend | Core insight, Implication |
| Case-study breakdown | Specific engagement or project | Process, Framework |
| Contrarian insight | Challenge to conventional wisdom | Contrarian |
| Legal / consulting perspective | Knowledge-based vertical (law, arbitration, advisory) | Core insight, Framework |
| Founder lesson | Personal-experience framing | Process, Implication |
| Framework-driven educational | Teach a reusable framework | Framework |

## 30-day deployment framework (per department Rule 4)

| Week | Focus | Content |
|---|---|---|
| 1 | Core insight exposure | Main derivative post (thought leadership or framework-driven) |
| 2 | Process / contrarian angle | Secondary post using Process or Contrarian seed |
| 3 | Case-study / founder lesson | Tertiary post using Case-study or Founder-lesson template |
| 4 | Recap + Substack funnel | Summary post with explicit Substack link in body (algorithm-friendly because it's the 4th-week recap, not the lead) |

## Knowledge-based vertical alignment

For the verticals that LinkedIn is specifically designed to serve (law, arbitration, litigation, startup consulting, advisory services, research, professional services):

| Vertical | Primary templates | Primary seeds |
|---|---|---|
| Law / arbitration / litigation | Legal / consulting perspective, Case-study breakdown | Core insight, Framework |
| Startup consulting / advisory | Thought leadership, Founder lesson | Core insight, Contrarian |
| Research / professional services | Framework-driven educational, Industry commentary | Framework, Implication |

Every post for these verticals contributes to a growing public archive of demonstrable expertise. Posts must be referenceable during:
- Client acquisition
- Partnership discussions
- Recruitment opportunities
- Speaking engagements
- Business development efforts

## Visual discipline

Custom graphics, visual frameworks, and branded content assets are mandatory for LinkedIn posts. Stock imagery without provenance is prohibited (per Substack Hub OUTPUT_CONTRACT non-negotiable #3).

**Visual assets from Media Department** — invoke Media's OUTPUT_CONTRACT for the production pipeline.

## Funnel discipline

Every LinkedIn post must funnel qualified audience back to Substack. Mechanism depends on week:

| Week | Funnel placement |
|---|---|
| 1 | Link in first comment (algorithm deprioritizes external links in post body on week 1) |
| 2 | Link in first comment |
| 3 | Link in first comment |
| 4 | Link in post body (recap post; algorithm treats week-4 recap differently) |

## Read order (cold instance arriving at this file)

1. This file — see the workflow steps and templates.
2. `.\OUTPUT_CONTRACT.md` — canonical structure of every LinkedIn derivative.
3. `.\..\WORKING_RULES.md` — department rules this workflow obeys (especially Rules 1, 2, 4).
4. `.\..\01 - substack-hub\OUTPUT_CONTRACT.md` — upstream decomposition seeds this layer consumes.

## Update rule

When this workflow changes, update this file first, then update `.\..\WORKING_RULES.md` if the change affects a department rule, then update `.\..\00 - ENTRY.md` if the workflow diagram or ancestry changes.
