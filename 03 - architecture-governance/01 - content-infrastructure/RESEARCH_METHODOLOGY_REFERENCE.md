# Research Methodology Reference

Type: pointer document — names the diamond model, points at the CE-native systems that already operationalize it, and declares what is and is not built on top.

## Authority

This file does NOT define a new CE methodology. It names a framing (the "diamond model") and points at the existing systems that realize it. The operational authority lives in:

| Concept | CE-native operationalization |
|---|---|
| 6-dimension confidence evaluation before any task | `.\..\..\..\..\..\01 - FORGE\02 - source-truth\02 - core-runtime\09 - ingestion-and-knowledge\knowledge_sufficiency_gate.py` (KSE, Gate 8) |
| Research MUST precede drafting in content-production tasks | `.\..\..\..\..\..\02 - WORKSPACE_META\03 - folder-governance\RESEARCH_FIRST_CONTENT_PRODUCTION.md` (governance rule) |
| 11 sections of codified cognitive infrastructure (gates, state, anti-patterns, decision hierarchy) | `.\..\..\..\..\..\02 - WORKSPACE_META\03 - folder-governance\02 - orchestration-skill-creator\02 - ORIENTATION\WORKSPACE_ORCHESTRATION_CONTRACT.md` |
| 256+ CONTEXT→RULE→OUTCOME transferable axioms | `.\..\..\..\..\..\03 - work-projects\02 - company\03 - company-creation-protocol\03 - function-folder\04 - runtime\00 - QUERY\WORK_AXIOM_BANK.md` |

## Source intent

Derived from `.\..\..\..\..\..\99 - ARCHIVE\tech-bro\2026-06-13-lrp6-infrastructure-buildout\infrastructure\01 - formalize-research-methodology.md`. That source names the diamond model and extends it beyond writing to business construction, distribution, and transferable mental infrastructure. This document points at where each concept is already realized on disk.

## The Diamond Model (named, not redefined)

**Expand-then-compress:** a research phase expands outward from a single point into the complete boundary of a problem space — mapping every relevant source, perspective, dependency, stakeholder, framework, and edge condition until the full shape is visible. Then a drafting/execution phase compresses the accumulated understanding into a coherent output.

**Why the middle layer matters:** skipping the expansion phase produces outputs with no middle layers of understanding. The output looks correct but has no structural integrity, substantive insight, or long-term value. This is the structural-loss-of-value pattern that `RESEARCH_FIRST_CONTENT_PRODUCTION.md` detects and rejects via its 5 anti-patterns.

**CE realization:**
- The expansion phase is operationalized as KSE's 6 dimensions: domain familiarity, context completeness, reasoning capability, tool readiness, ambiguity clarity, prior art coverage. When any dimension scores LOW or CRITICAL, the gate auto-stages an Arena research run — this is the expansion happening mechanically.
- The compression phase is operationalized as the cognitive sequence's 4 stages (Grounding → Agent 1 → Agent 2 → Agent 3) which take a grounded understanding and produce a structured instruction artifact.
- The anti-patterns in `RESEARCH_FIRST_CONTENT_PRODUCTION.md` (no prior research, single-source claims, outline-fill-in without research artifacts, instantaneous drafting) are the diamond model's failure modes made enforceable.

## Beyond writing — where the diamond model also governs

The source intent extends the model to business construction, distribution, and cognitive transfer. CE realizes each extension in a different system:

| Domain | CE system that operationalizes it |
|---|---|
| Writing / content | RESEARCH_FIRST_CONTENT_PRODUCTION governance rule + KSE Gate 8 |
| Business construction (reverse-engineering organizations) | WORK_AXIOM_BANK (tacit → explicit) + COMPANY_DEPENDENCY_GRAPH (sequential build order) |
| Distribution (owned-media authority) | WORKSPACE_ORCHESTRATION_CONTRACT § 11 (dream lifecycle authority) + the content-distribution company at `.\..\..\..\..\..\03 - work-projects\02 - company\02 - working-companies\02 - content-distribution\` |
| Cognitive transfer (from individual to scalable) | WORK_AXIOM_BANK CONTEXT→RULE→OUTCOME format (the documented mechanism for making individual talent replicable) |

## AI as force multiplier (not replacement)

The source intent declares: "AI should be positioned as a force multiplier for an existing research process rather than a replacement for one. The quality ceiling of any AI-assisted output is determined by the quality and depth of the underlying research architecture feeding it."

CE realization: KSE's scoring is domain-agnostic. When CE's underlying research architecture is shallow (no WORK_AXIOM_BANK entries for a domain, no prior art coverage), KSE scores LOW and refuses to dispatch. The gate forces the research layer to deepen before AI execution proceeds. This is the force-multiplier discipline made mechanical.

## Strategic window (named, actionable now)

The source intent declares: "current AI capabilities provide an unprecedented leverage opportunity for individuals capable of combining rigorous research with accelerated production. However, this window is unlikely to remain unchanged indefinitely."

CE realization: the worklist compiler (`ce_worklist.py` + `CE_WORKLIST_SOURCES.json`) reads 13 registered state workspace areas and emits a prioritized action list every session. The strategic window shows up as a long CE-ACTIONABLE queue of domain-build work that can be executed now with AI leverage. The discipline is to execute the queue systematically rather than deferring it — every completed item becomes a durable asset that persists regardless of future technological shifts.

## Transferable mental infrastructure (named, realized)

The source intent declares: "studying exceptional individuals, identifying the frameworks underlying their performance, extracting those frameworks from the individual, and converting them into reusable systems that others can apply."

CE realization: this is exactly what `WORK_AXIOM_BANK.md` does. Every entry is a CONTEXT→RULE→OUTCOME triple extracted from observed behavior. The bank is the mechanism for converting isolated talent into scalable knowledge. Every new axiom added is a unit of transferable cognitive infrastructure.

## Diamond model applied to blog generation

**Source intent** (from `.\..\..\..\..\..\99 - ARCHIVE\tech-bro\2026-06-13-lrp6-infrastructure-buildout\gaps\04 - rebuild-blog-generation-knowledge-sufficiency-synthesis.md`): the core issue is not writing quality but process architecture. Drafting must not begin before sufficient domain understanding is established. The draft should emerge by collapsing the accumulated research inward toward the core narrative, argument, or insight — with the final article representing only the visible top layer of a much larger underlying knowledge structure.

**Blog-generation workflow (research-first synthesis model):**

| Phase | Action | Output on disk | Gate |
|---|---|---|---|
| 1. Expand | Comprehensively map subject space: all relevant sources, perspectives, historical context, technical details, competing viewpoints, adjacent concepts, supporting evidence | `research-[topic-slug]/sources/` + `observations/` | KSE Gate 8 — all 6 dimensions score SUFFICIENT |
| 2. Consolidate | Define the full boundary of the topic; produce robust contextual knowledge package | `research-[topic-slug]/synthesis/` with synthesis-only insights | At least 1 insight traceable to synthesis, not any single source |
| 3. Collapse (draft) | Collapse accumulated research inward toward core narrative / argument / insight | `research-[topic-slug]/outputs/` draft article | Draft is visibly the top layer of the underlying structure |

**Knowledge-sufficiency gate:** KSE Gate 8 (`.\..\..\..\..\..\01 - FORGE\02 - source-truth\02 - core-runtime\09 - ingestion-and-knowledge\knowledge_sufficiency_gate.py`) is the mechanical evaluator. It scores 6 dimensions (domain familiarity, context completeness, reasoning capability, tool readiness, ambiguity clarity, prior art coverage). When any dimension scores LOW or CRITICAL, the gate refuses to dispatch — this is the explicit gate that prevents writing from starting until the research layer reaches an acceptable threshold.

**Research artifacts as first-class outputs:** research artifacts, contextual packages, source collections, and synthesis notes are permanent first-class workflow outputs — not transient intermediates. They survive beyond the article they produced and are queryable by future articles. The WORK_AXIOM_BANK is the most explicit realization: every research pass contributes axioms that compound across articles.

**Missing-middle-layer anti-pattern:** the failure mode this workflow eliminates is "only the lowest layer of research and the highest layer of prose exist while the critical middle layer of understanding is missing." This is the same anti-pattern named in `.\..\..\..\..\..\02 - WORKSPACE_META\03 - folder-governance\RESEARCH_FIRST_CONTENT_PRODUCTION.md` (anti-pattern #3: "Here's an outline, fill it in" with no research artifacts on disk) and `.\..\..\01 - writing-department\BLOG_AS_KNOWLEDGE_PRODUCTION.md` (4-stage workflow with explicit stage gates).

**Traceability chain:** every generated article must be traceable back to a sufficiently explored research diamond. Traceability is realized as:
- Article metadata references the research folder path (`upstream_research_path` field in Substack Hub `metadata.json`).
- Research folder survives beyond the article (under `research-[topic-slug]/`).
- Synthesis-only insights in `synthesis/` are identifiable as synthesis, not source restatement.
- Axioms contributed to WORK_AXIOM_BANK are referenced from the synthesis.

**CE realization:** the diamond model's application to blog generation is not a new system. It is the existing RESEARCH_FIRST_CONTENT_PRODUCTION governance rule + KSE Gate 8 + the content-cluster discipline + WORK_AXIOM_BANK + the Writing Department's research-folder structure, wired together as a blog-specific workflow. The blog-specific wiring is documented at `.\..\..\01 - writing-department\BLOG_AS_KNOWLEDGE_PRODUCTION.md`.

## Read order (cold instance arriving at this file)

1. This file — see the named concepts and where they live.
2. `.\..\..\..\..\..\02 - WORKSPACE_META\03 - folder-governance\RESEARCH_FIRST_CONTENT_PRODUCTION.md` — the enforcement rule.
3. `.\..\..\..\..\..\01 - FORGE\02 - source-truth\02 - core-runtime\09 - ingestion-and-knowledge\knowledge_sufficiency_gate.py` — the mechanical evaluator.
4. `.\..\..\..\..\..\02 - WORKSPACE_META\03 - folder-governance\02 - orchestration-skill-creator\02 - ORIENTATION\WORKSPACE_ORCHESTRATION_CONTRACT.md` — the workspace-level contract.
5. `.\..\..\..\..\..\03 - work-projects\02 - company\03 - company-creation-protocol\03 - function-folder\04 - runtime\00 - QUERY\WORK_AXIOM_BANK.md` — the axiom bank.

## Update rule

This file is a pointer document. When one of the systems it points at changes, update the relevant row in the table above. Do not add new concepts here — if a new concept emerges, it belongs in the source system, and this file gets a new row pointing at it.
