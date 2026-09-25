# Content Distribution

Type: function folder — operational department managing platform-native content decomposition.

## Ancestry

- Parent: `.\..\00 - ENTRY.md`
- Dependency: Writing Department (`.\..\01 - writing-department\`) — provides published articles and decomposition seeds
- Governance: `.\..\..\..\..\02 - WORKSPACE_META\03 - folder-governance\RESEARCH_FIRST_CONTENT_PRODUCTION.md`

## Status

ACTIVE — manages the hub-and-spoke distribution of Writing Department outputs across 6 platforms.

## Working Rules

See `.\WORKING_RULES.md`.

## Templates

See `.\05 - templates\` for platform-specific content templates (LinkedIn, Twitter/X, Threads, Instagram, Medium, Facebook).

## Workflow

```
Article published on Substack (from Writing Department)
  → Receive decomposition seeds (core insight, process, contrarian, framework, implication, visual)
  → Map seeds to platforms per seed-platform mapping
  → Write platform-native derivatives (not reposts — translations)
  → Schedule across 30-day deployment framework
  → Track engagement metrics
  → Feed insights back to Writing Department for next topic selection
```

## Platform Registry

| Platform | Role | Native Register | Primary Seeds |
|---|---|---|---|
| Substack | Owned anchor | Long-form, SEO-rich, 2000-5000 words | Full article |
| LinkedIn | Professional authority | Executive, evidence-based, 200-400 words | Core insight + framework |
| Twitter/X | Process exposure | Thread format, methodology-focused | Process breakdown + contrarian |
| Threads | Discussion layer | Conversational, outcome-focused, 100-300 words | Implication + core insight |
| Instagram | Visual layer | Carousel or infographic, visual-first | Visual concept + core insight |
| Medium | Executive summary | Condensed long-form, 800-1500 words | Core insight + process |
| Facebook | Mature demographic | Educational, accessible, 300-600 words | Implication + core insight |

## Output To

| Consumer | What | Format |
|---|---|---|
| Substack | Published articles | Long-form newsletter |
| LinkedIn | Professional content | Posts with graphics |
| Twitter/X | Process threads | 5-12 tweet threads |
| Threads | Discussion posts | Text + graphic |
| Instagram | Visual content | Carousels, infographics |
| Medium | Condensed articles | Canonical-linked articles |
| Facebook | Educational content | Accessible long-form posts |

## Local Wiring (appended 2026-09-25, session S001)

- Parent `.\..\00 - ENTRY.md` is the company ENTRY. Company state: `.\..\00-control\STATE.md`.
- Upstream: `.\..\01 - writing-department\` (sibling folder).
- Templates on disk in `.\05 - templates\`: `substack-article-template.md`, `linkedin-post-template.md`, `twitter-thread-template.md`, `decomposition-checklist.md`. The Threads, Instagram, Medium and Facebook templates named under "Templates" above do not exist yet (gap G-M05).
- Visual assets: the Media Department is not in this repo (`.\..\03 - architecture-governance\EXTERNAL_DEPENDENCY_REGISTER.md` X-04). Every "custom graphic mandatory" check is blocked until gap G-X04 closes.
- Status in this repo: built, **not exercised**. No layer has a `drafts/` folder yet.

## Known Conflicts and Precedence (appended 2026-09-25, session S001)

Where two instruction files disagree, this table gives the operative rule. Each resolution uses precedence the files themselves declare. Evidence and details are in `.\..\03 - architecture-governance\INSTRUCTION_GAP_REGISTER.md`.

| Topic | Conflict | Operative rule | Gap |
|---|---|---|---|
| Channel set | The doctrine's kit is website, substack, medium, twitter-x and linkedin. This ENTRY's registry lists 7 platforms and omits the website. Layer folders exist for Substack, LinkedIn, Twitter/X + Threads and Facebook | The kit must contain the doctrine's 5. Threads and Facebook ride as activated extensions: the doctrine says "add channels as machinery activates", and their layer contracts exist. Instagram has no machinery, so log it as a partial publication. Website and Medium have no layer contract yet (G-M04) | G-C01 |
| 30-day plan | WORKING_RULES Rule 4, MULTI_PLATFORM_ARCHITECTURE, the LinkedIn WORKFLOW and spec 03 give four different schedules | WORKING_RULES Rule 4, because MULTI_PLATFORM_ARCHITECTURE says "department rules win". The no-same-day rule still binds | G-C02 |
| Threads length | 100–300 words (this ENTRY, spec 03, the checklist) vs ≤ 500 characters (layer OUTPUT_CONTRACT check 9) | ≤ 500 characters, because the layer contract is the verification check. The platform's actual limit goes to research to verify | G-C03 |
| Facebook length | 300–600 words (WORKING_RULES Rule 5) vs 300–800 (spec 06) | 300–600 words | G-C04 |
| Internal links | ≥ 2 (Substack contract) vs ≥ 3 (spec 02) | ≥ 2. The first articles in a new cluster cannot meet this; the bootstrap rule is OPEN | G-C05 |
| Twitter seed | process + contrarian (this ENTRY) vs `process` only (layer contract rule 3) | Metadata `twitter_seed_used` = `process`. The contrarian angle may shape the hook | G-C10 |
