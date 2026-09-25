# 07 — Department Dependency Model

Type: organizational model

## Principle

Departments are built in sequence, not simultaneously. Each department's output creates the foundation the next department needs. This is a factory pipeline, not parallel construction.

## Department Registry

| # | Department | Status | Core Output |
|---|---|---|---|
| 1 | Media | COMPLETE | Visual assets, production workflows, content creation systems |
| 2 | Writing | IN PROGRESS | Research-first articles, newsletters, knowledge production |
| 3 | Law | OPERATIONAL | Legal services, contracts, compliance frameworks |
| 4 | Design | PLANNED | Brand identity, visual systems, design templates |
| 5 | Branding | PLANNED | Strategic positioning, market identity, brand architecture |
| 6 | Operations | PLANNED | Cross-department coordination, resource allocation |

## Dependency Chain

```
Media (1) → Writing (2) → Law (3) → Design (4) → Branding (5) → Operations (6)
                ↑                                        ↑
                └── Research methodology (shared) ────────┘
```

### Why This Order

1. **Media first:** Visual production systems, content creation workflows, and asset management infrastructure must exist before writing can be visually supported.
2. **Writing second:** Research-first content production builds on media's visual capabilities and creates the knowledge assets that legal, design, and branding work depends on.
3. **Law third:** Legal frameworks for content, IP, contracts, and compliance need an established content operation to govern.
4. **Design fourth:** Brand identity systems require established content and legal frameworks before visual identity can be formalized.
5. **Branding fifth:** Strategic positioning depends on having content, legal protection, and design systems in place.
6. **Operations sixth:** Cross-department coordination only makes sense when there are multiple departments to coordinate.

## Universal Operational Foundation

All departments share:
- Research-first methodology (Governance Rule 01)
- Content distribution architecture (Specs 02-06)
- AI-assisted workflows (amplification, not replacement)
- Documented processes and decision trees
- Quality standards and output templates

## Multi-Entity Support

The department infrastructure supports multiple legally distinct entities:
- Legal services firm
- Consulting practice
- Creative agency / media brand
- Design studio

Each entity uses the shared departmental infrastructure while maintaining its own positioning, client relationships, and revenue model.

## CE Implementation

Each department maps to a CE function folder or skill set:
- Media → Visual production pipeline (`03 - work-projects/04 - domains/02 - nano-banana/`)
- Writing → Knowledge Sufficiency workflows + blog generation function
- Law → Legal document templates and compliance frameworks
- Design → Brand identity templates and visual system specs
- Branding → Strategic positioning frameworks and market analysis
- Operations → Cross-function coordination governance
