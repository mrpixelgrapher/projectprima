# Substack Hub — Workflow

Type: workflow document — operationalizes Substack as the primary publishing destination and intellectual property repository within the content-distribution department.

## Authority

This workflow sits under the Content Distribution department's governance:

- Parent: `.\..\00 - ENTRY.md` (Content Distribution function folder)
- Department rule: `.\..\WORKING_RULES.md` Rule 2 ("Substack Is The Anchor") — all distribution flows FROM Substack TO platforms, never the reverse.
- Upstream: Writing Department (`.\..\..\01 - writing-department\`) — produces the research-first articles that Substack publishes.
- Downstream: LinkedIn layer, Twitter/Threads layer, Facebook layer, Multi-Platform Architecture — all consume Substack articles as master source.
- Governance: `.\..\..\..\..\..\02 - WORKSPACE_META\03 - folder-governance\RESEARCH_FIRST_CONTENT_PRODUCTION.md`

## Source intent

Derived from `.\..\..\..\..\..\99 - ARCHIVE\tech-bro\2026-06-13-lrp6-infrastructure-buildout\infrastructure\02 - build-substack-distribution-hub.md`. The source declares Substack as the hub in a hub-and-spoke architecture where every major research project, framework, case study, methodology, or long-form analysis is first developed and published as a comprehensive newsletter or deep blog.

## Hub-and-spoke architecture

```
Writing Department (research-first article)
    ↓
Substack Hub (master source publication)
    ↓
    ├── LinkedIn layer (B2B thought leadership derivative)
    ├── Twitter/X + Threads layer (process + implications derivatives)
    ├── Facebook layer (demographic-reach derivative)
    ├── Personal website (executive summary + funnel back to Substack)
    └── Medium (condensed takeaway derivative)
```

**Direction of flow:** every arrow above is one-way. Substack is the canonical source; every other platform is a discovery mechanism that funnels audience back to Substack.

## Workflow steps (per Substack publication)

| Step | Action | Input | Output |
|---|---|---|---|
| 1 | Receive research-first article | Writing Department output (per `.\..\..\01 - writing-department\OUTPUT_CONTRACT.md`) | Article file in Substack-hub drafts folder |
| 2 | Verify RESEARCH_FIRST gate passed | Pre-drafting gate evidence (4 checks) | Gate-passed marker in article metadata |
| 3 | Add Substack-specific structure | SEO title, meta description, SEO keywords, cluster tag, internal links | Structured article file |
| 4 | Add visual assets | Media Department outputs (per `.\..\..\design-visual-artist-brand\01 - foundation\13-media-department\02 - media-department\OUTPUT_CONTRACT.md`) | Inline images + featured image |
| 5 | Publish to Substack | Structured article | Live newsletter URL |
| 6 | Generate decomposition seeds | Article content (per `.\..\..\01 - writing-department\OUTPUT_CONTRACT.md` "decomposition seeds" section) | 6 seeds: core insight, process, contrarian, framework, implication, visual |
| 7 | Distribute seeds to downstream layers | Seeds + Substack URL | Platform-native derivatives (one per layer) |

## Content-cluster organization

Every Substack article belongs to one or more content clusters. Clusters are thematic groupings that let individual newsletters strengthen the authority and discoverability of the entire archive through internal linking and structured navigation.

**Cluster rules:**
1. Every article declares at least one cluster tag in its metadata.
2. Every cluster has a cluster-index article that links to every article in the cluster.
3. Every article links to at least two other articles in the same cluster (internal linking discipline).
4. New clusters require an explicit cluster-index article before any member articles are published.

**Cluster taxonomy (initial):**
- Research methodology / diamond model
- Department-first business model
- AI-era publishing
- Multi-vertical content operating system
- [Add new clusters as the archive grows]

## Website integration

The personal website is the public-facing discovery and conversion layer. Substack is the complete long-form knowledge archive. The integration:

| Website element | Substack target |
|---|---|
| Executive summary article | Full Substack article (canonical link) |
| Framework overview | Substack article that develops the framework in full |
| Research preview | Substack article that publishes the complete research |
| High-level insight | Substack article with the depth the insight implies |

**Rule:** no website article competes with its corresponding Substack article. The website summarizes and routes; Substack develops and archives.

## Self-reinforcing distribution engine

The strategic goal: high-quality research generates long-form authority → long-form authority generates platform-specific content → platform-specific content generates audience attention → audience attention is continuously redirected into owned channels (Substack + website).

**Feedback discipline:**
1. Every Substack article must name its upstream research input (research folder, WORK_AXIOM_BANK axioms consulted, Arena synthesis integrated).
2. Every Substack article must name its downstream derivative outputs (LinkedIn post URL, Twitter thread URL, Threads post URL, Facebook post URL, Medium condensed URL).
3. Every derivative must link back to the Substack article (per `.\..\WORKING_RULES.md` Rule 2).

## Audience-ownership discipline

Unlike algorithm-driven platforms, the Substack newsletter serves as a direct audience ownership layer. Subscriber relationships, distribution reach, and content accessibility remain under the creator's control rather than being dependent on external platform visibility.

**Non-negotiables:**
1. Never gate the newsletter behind a paywall that fragments the archive — the archive is the asset.
2. Every publication strengthens the visibility and credibility of previous work (compounding SEO value).
3. Cross-link every new article to at least two previous articles in the same cluster.
4. Treat the newsletter as a searchable knowledge base, not a collection of isolated articles.

## Read order (cold instance arriving at this file)

1. This file — see the workflow steps and architecture.
2. `.\OUTPUT_CONTRACT.md` — canonical structure of every Substack article.
3. `.\..\WORKING_RULES.md` — department rules this workflow obeys (especially Rule 2: Substack Is The Anchor).
4. `.\..\00 - ENTRY.md` — Content Distribution function folder.
5. `.\..\..\01 - writing-department\OUTPUT_CONTRACT.md` — upstream article structure Substack receives.
6. `.\..\..\design-visual-artist-brand\01 - foundation\13-media-department\02 - media-department\OUTPUT_CONTRACT.md` — upstream visual assets Substack receives.

## Update rule

When this workflow changes, update this file first, then update `.\..\WORKING_RULES.md` if the change affects a department rule, then update `.\..\00 - ENTRY.md` if the workflow diagram or ancestry changes.
