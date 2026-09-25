# 14 — Research-First Blog Generation

Type: workflow redesign (Gap 04)

## The Gap

Blog generation currently triggers drafting before contextual sufficiency is achieved. The "diamond model" of knowledge acquisition is not enforced.

## Diamond Model Implementation

```
        ╱╲
       ╱  ╲      ← Drafting (visible 10%)
      ╱    ╲        Article is the apex
     ╱──────╲
    ╱        ╲   ← Synthesis (middle layer)
   ╱          ╲     Original insights, frameworks
  ╱            ╲
 ╱              ╲ ← Research (hidden 90%)
╱________________╲   Sources, observations, boundaries
```

### Expansion Phase (research outward)

1. **Map the boundary:** What are ALL relevant sources, perspectives, frameworks?
2. **Acquire depth:** Collect primary sources, expert opinions, case studies, historical context
3. **Extract observations:** What patterns emerge? What contradictions exist?
4. **Check saturation:** Is there enough material for original synthesis?

**Gate:** If the boundary cannot be fully named, expansion continues.

### Compression Phase (drafting inward)

1. **Identify the core:** What is the single most important insight from accumulated research?
2. **Structure the argument:** How does evidence support this insight?
3. **Write the apex:** The article is the visible top layer — concise, well-supported, original.
4. **Verify traceability:** Every claim connects to accumulated research.

### CE Enforcement

| Check | How | Action if Fail |
|---|---|---|
| Research artifacts exist | Scan for source collections, observation notes | Block drafting, return to expansion |
| Boundary is mapped | KSE dimension: context completeness | Trigger Arena research |
| Original synthesis present | Check: insights not in any single source? | Deepen analysis phase |
| Drafting is synthesis | Check: draft references accumulated research? | Reject top-down draft |

### Research Artifact Structure

```
research-domain-[topic]/
├── sources/           ← Raw collected material
├── observations/      ← Extracted patterns, themes, contradictions
├── synthesis/         ← Original insights, frameworks, relationships
└── articles/          ← Published outputs (apex layer)
```

Each layer survives independently. A future article on the same topic reuses sources and observations without re-acquisition. Only the synthesis and article layers are specific to one publication.

### Integration with Existing CE Architecture

- **Gate 8 (KSE):** Already scores knowledge sufficiency. Extend to specifically evaluate research domain completeness for blog topics.
- **Arena research:** When KSE scores LOW for a blog topic, Arena IS the expansion phase. Arena output becomes the sources layer.
- **Cognitive cognitive sequence:** Blog generation tasks should include a "research domain check" before proceeding to drafting instructions.
