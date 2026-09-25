# Instruction Gap Register

Type: governance report and living register. Tier 2: append rows and update Status cells; never delete a row. Closed rows stay as the audit trail.
Created: 2026-09-25, session S001, right after the three department folders moved into `omnichannel-marketing-company/`.
Method: every file in the company was read in full. Link claims were checked with `00-control/tools/check_links.py`, and phase claims with `00-control/tools/derive_phase.py`. A gap is listed only if a file shows it; each row cites that file.

## What counts as a gap in the cognitive instructions

An instruction set has a gap wherever a cold instance following it would do one of these:

| Class | The instance would… | Prefix |
|---|---|---|
| Path | follow a link to nothing | G-P |
| External | depend on a system that is not in this repo | G-X |
| Conflict | get two different answers from two files | G-C |
| Doctrine | skip a rule an enforced doctrine says must be in the file | G-D |
| Missing machinery | find a step with no operator, template or artifact to run it | G-M |
| Human | need a fact only a person can give | G-H |

## Status values

| Status | Meaning |
|---|---|
| FIXED S001 | Closed this session. The fix is on disk at the cited path. |
| REGISTERED | Unavoidable external dependency, recorded with its local substitute in `03 - architecture-governance/EXTERNAL_DEPENDENCY_REGISTER.md`. |
| RESOLVED | Resolved by precedence that the instruction files themselves declare. The operative rule is written down. |
| OPEN → x | Not closed. It closes at build phase / event *x* (handoff §8). The proposal is recorded so the decision isn't re-derived. |
| HUMAN | Waiting on a person, via a CARBON_INPUT_FORM. |

## Summary (2026-09-25)

| Class | Total | FIXED | REGISTERED / RESOLVED | OPEN | HUMAN |
|---|---|---|---|---|---|
| Path | 9 | 9 | — | 0 | — |
| External | 6 | 0 | 4 | 2 | — |
| Conflict | 16 | 2 | 8 | 6 | — |
| Doctrine | 6 | 3 | — | 3 | — |
| Missing machinery | 12 | 4 | 1 | 6 | 1 |
| Human | 6 | — | — | — | 6 |

---

## G-P — Path gaps

All nine were closed in S001. The corrections are path-only (Tier 2 allows correcting paths) and applied with line endings preserved. After the fixes, `check_links.py` reports BROKEN 0 and UNREGISTERED 0.

| ID | Gap | Evidence | Resolution | Status |
|---|---|---|---|---|
| G-P01 | Writing ENTRY pointed at ".\templates\"; the real folder is `01 - writing-department/02 - templates/` | `01 - writing-department/00 - ENTRY.md` | Corrected to ".\02 - templates\"; the Local Wiring note says where the article template lives | FIXED S001 |
| G-P02 | LinkedIn layer pointed at ".\templates\"; the templates live in `02 - content-distribution/05 - templates/` | `02 - content-distribution/02 - linkedin-layer/WORKFLOW.md`, `OUTPUT_CONTRACT.md` | Corrected to ".\..\05 - templates\" (2 files) | FIXED S001 |
| G-P03 | Decomposition checklist pointed at ".\templates\" from inside the templates folder | `02 - content-distribution/05 - templates/decomposition-checklist.md` | Corrected to ".\..\05 - templates\" | FIXED S001 |
| G-P04 | Prompt-library wiring manifest named "templates/" | `01 - writing-department/01 - prompt-library/00 - WIRING_MANIFEST.md` | Corrected to ".\..\02 - templates\" | FIXED S001 |
| G-P05 | Stage prompts 01–04 cited "lrp6-content-infrastructure/…" and "/14 - …" (the source working-unit name, plus an absolute path). The specs they mean are in this repo | `01 - writing-department/01 - prompt-library/01…04 - PROMPT_*.md` (LINKS sections) | Corrected to `03 - architecture-governance/01 - content-infrastructure/` specs 01, 12, 13, 14 | FIXED S001 |
| G-P06 | Multi-vertical OS points at writing and distribution through CE-absolute `03 - work-projects\…` paths | `03 - architecture-governance/MULTI_VERTICAL_CONTENT_OS.md` | 5 references corrected to sibling paths | FIXED S001 |
| G-P07 | Research methodology reference points at distribution through a CE-absolute path | `03 - architecture-governance/01 - content-infrastructure/RESEARCH_METHODOLOGY_REFERENCE.md` | Corrected to ".\..\..\02 - content-distribution\" | FIXED S001 |
| G-P08 | Dependency graph rows for writing and distribution use CE-absolute paths | `03 - architecture-governance/COMPANY_DEPENDENCY_GRAPH.md` | Corrected in place; old paths recorded in an appended Topology Update | FIXED S001 |
| G-P09 | 173 references point into the CE workspace (FORGE, WORKSPACE_META, Arena, sibling companies) | `check_links.py` output | Each one matched to a row X-01 to X-15 in `EXTERNAL_DEPENDENCY_REGISTER.md`. The checker now fails on any unregistered escape | FIXED S001 |

## G-X — External systems the instructions rely on

Full list with substitutes: `03 - architecture-governance/EXTERNAL_DEPENDENCY_REGISTER.md`. Rows here track only the ones that change what a cold instance can do.

| ID | Gap | Evidence | Resolution / next step | Status |
|---|---|---|---|---|
| G-X01 | The research-first governance rule (parent of both departments) is external | Writing and distribution ENTRY "Governance" lines | Spec 01 + spec 13 + writing WORKING_RULES Rule 1 are the operative text (X-01) | REGISTERED |
| G-X02 | KSE Gate 8, "the mechanical evaluator" of research depth, is external, so the research gate has no operator | `01 - writing-department/00 - ENTRY.md` workflow line 2; `RESEARCH_METHODOLOGY_REFERENCE.md` | Substitute: the 4-check pre-drafting gate, run by hand (X-02). A script operator is G-M02 | REGISTERED |
| G-X03 | Arena research runs are external | Spec 01 "Arena research IS the expansion phase" | RESEARCH_DOSSIER under `02-sourcing/01 - dossiers/`, executed by an agent with web access (X-03) | REGISTERED |
| G-X04 | The Media Department is external, but every output contract makes a Media-produced custom visual mandatory (Substack check 5, LinkedIn check 5, Twitter/Threads check 10, Facebook check 6). As things stand, no article or variant can pass | `02 - content-distribution/*/OUTPUT_CONTRACT.md`; `01 - writing-department/MEDIA_DEPARTMENT_DEPENDENCY.md` | Proposal: at the first article, author diagram-class graphics in-repo as SVG, since frameworks and flows are custom compression graphics, which the rules ask for. Anything photographic or illustrative is a render-dependent unit and stays BLOCKED until a human or tool renders it (handoff §2.7) | OPEN → first article (build Phase D) |
| G-X06 | `DEPARTMENT_FIRST_BUSINESS_MODEL.md` declares the department-router gap "CLOSED", citing a script that is not in this repo | `03 - architecture-governance/DEPARTMENT_FIRST_BUSINESS_MODEL.md` § "The invocation workspace area" | The claim holds only for the CE workspace. Here, route by reading `DEPARTMENT_REGISTRY.md`. Rebuild a router only when a real objective spans ≥ 2 departments (X-06) | REGISTERED |
| G-X11 | The company ENTRY's promotion route (meta-company-template) is external, so "live company" status has no route here | `00 - ENTRY.md` Runtime Law | Status authority here is the derived phase. "Generated attempt" stays true until phase 8 (appended to `00 - ENTRY.md` Company Map). If the operator wants a different bar, that is a governance decision to log in `meta_workspace.md` §4 | OPEN → operator confirmation (low priority) |

(Row IDs follow the register row they concern. X-05, X-07–X-10 and X-12–X-15 are fully covered by the register and need no tracking here.)

## G-C — Conflicts between instruction files

| ID | Conflict | Evidence | Operative rule / next step | Status |
|---|---|---|---|---|
| G-C01 | Three different channel sets. Doctrine PUBLISH_KIT: website, substack, medium, twitter-x, linkedin. Distribution architecture: substack, linkedin, twitter/x, threads, facebook, website. Distribution ENTRY registry: 7 platforms, no website. Layer machinery exists only for Substack, LinkedIn, Twitter/X+Threads, Facebook | `03 - architecture-governance/02 - doctrine-enforcement/OMNICHANNEL_ENFORCEMENT.md`; `02 - content-distribution/MULTI_PLATFORM_ARCHITECTURE.md`; `02 - content-distribution/00 - ENTRY.md` | Kit must hold the doctrine's 5. Threads and Facebook are activated extensions ("add channels as machinery activates"; their layer contracts exist). Instagram: no machinery, so log it as partial_publication with that reason. Website and Medium have no layer contract (G-M04). Written into the distribution ENTRY's precedence table | RESOLVED |
| G-C02 | Four 30-day schedules | `02 - content-distribution/WORKING_RULES.md` Rule 4; `MULTI_PLATFORM_ARCHITECTURE.md`; `02 - content-distribution/02 - linkedin-layer/WORKFLOW.md`; specs 03, 11 | WORKING_RULES Rule 4 wins, because MULTI_PLATFORM_ARCHITECTURE says "department rules win". Specs are unrealized design, informational only. The no-same-day rule (architecture + two layer contracts) still binds | RESOLVED |
| G-C03 | Threads length: 100–300 words vs ≤ 500 characters | `02 - content-distribution/00 - ENTRY.md`; spec 03; `02 - content-distribution/03 - twitter-threads-layer/OUTPUT_CONTRACT.md` check 9 | ≤ 500 characters, because the layer contract is the verification check. The platform's real limit is external-world data: verify it in the first dossier; don't assert it | RESOLVED (verify limit in research) |
| G-C04 | Facebook length: 300–600 vs 300–800 words | `02 - content-distribution/WORKING_RULES.md` Rule 5; spec 06 | 300–600 (department rule over spec) | RESOLVED |
| G-C05 | Internal links: ≥ 2 vs ≥ 3. **Bootstrap contradiction:** cluster rule 4 requires a cluster-index article before members, and every article needs ≥ 2 prior cluster links. Article #1 of a new cluster cannot comply | `02 - content-distribution/01 - substack-hub/OUTPUT_CONTRACT.md` §4; `02 - content-distribution/01 - substack-hub/WORKFLOW.md` cluster rules; spec 02; `01 - writing-department/BLOG_AS_KNOWLEDGE_PRODUCTION.md` check 7 | ≥ 2 is operative. Bootstrap proposal: the cluster-index article is exempt; members 1–2 link to the index plus any earlier member, and are logged as partial compliance; links are back-filled when member 3 ships. Decide at the first article | OPEN → first article |
| G-C06 | Research folder naming: `research-[slug]/…/outputs/` vs `research-domain-[topic]/…/articles/` | `01 - writing-department/OUTPUT_CONTRACT.md`; spec 14 | The writing contract (the realized artifact) wins | RESOLVED |
| G-C07 | No file says where `research-[slug]/` folders live | `01 - writing-department/OUTPUT_CONTRACT.md` §1; prompt-library WIRING_MANIFEST "First Production Run" | Proposal: `01 - writing-department/03 - research/research-[slug]/`. Business research stays in `02-sourcing/`. Decide at the first article | OPEN → first article |
| G-C08 | Two output-location schemes: per-layer `.\drafts\[slug]\` (each layer contract) vs `PUBLISH_KIT/` (doctrine) | layer `OUTPUT_CONTRACT.md` "Output location rules"; `OMNICHANNEL_ENFORCEMENT.md` Rule 1 | Both hold, at different pipeline stages: layer `drafts/` = WORKING (metadata, assets, verification); PUBLISH_KIT = OUTPUT (final, paste-ready, channel-ordered). Proposed kit location: `02 - content-distribution/06 - publish-kits/[slug]/PUBLISH_KIT/`. Decide at the first kit | OPEN → first kit (build Phase D) |
| G-C09 | Department statuses (Media COMPLETE, Writing / Distribution ACTIVE, Law OPERATIONAL) are CE-workspace claims. Dependency rule 1 can't be checked here because Media is absent | `03 - architecture-governance/DEPARTMENT_REGISTRY.md` | Statuses are read as inherited claims (appended to the registry). The capability ledger (build Phase C) becomes the authority on what this company can deliver | OPEN → build Phase C |
| G-C10 | Twitter seed: process + contrarian vs `process` only | `02 - content-distribution/00 - ENTRY.md`; `02 - content-distribution/03 - twitter-threads-layer/OUTPUT_CONTRACT.md` rule 3 | Layer contract: metadata seed = `process`; the contrarian angle may shape the hook | RESOLVED |
| G-C11 | Topology: registry D1 (2026-08-18) moved the departments out of this company; the operator directive (2026-09-25) moved them back in | `DEPARTMENT_REGISTRY.md` Topology Reconciliation; `00-control/source-intent/02 - operator-directives-2026-09-25.md` | The directive governs this repo. Topology Update appended to the registry and the dependency graph | FIXED S001 |
| G-C12 | **Vertical mismatch.** Writing + distribution were built for a creator's multi-vertical personal brand (legal, consulting, creative, research, branding). This company is a marketing firm: there is no marketing vertical row, the Substack cluster taxonomy lists the creator's own topics, the LinkedIn `vertical_tag` enum has no marketing value, and the Facebook personas are the creator's | `MULTI_VERTICAL_CONTENT_OS.md` "Vertical profiles"; `02 - content-distribution/01 - substack-hub/WORKFLOW.md` cluster taxonomy; `02 - content-distribution/02 - linkedin-layer/OUTPUT_CONTRACT.md` | Add this company as a vertical, following MULTI_VERTICAL_CONTENT_OS's own "Update rule" (row + ecosystem role + Substack repository + clusters). Whose voice and which Substack depends on F-001 Q1 and Q4 | OPEN → after F-001 answered |
| G-C13 | Writing ENTRY says its templates folder holds article-structure, research-domain and decomposition templates. Only research-domain is there | `01 - writing-department/00 - ENTRY.md` "Templates" | Local Wiring note appended: the article skeleton and decomposition checklist live in distribution `05 - templates` | FIXED S001 |
| G-C14 | Distribution ENTRY says `05 - templates` holds LinkedIn, Twitter/X, Threads, Instagram, Medium and Facebook templates. Only LinkedIn and Twitter/X exist (plus the Substack article template and the checklist) | `02 - content-distribution/00 - ENTRY.md` "Templates" | Noted in the appended Local Wiring. The missing templates are G-M05 | RESOLVED (noted) |
| G-C15 | The company ENTRY says "Active folder: forge-folder"; the manifest says `active_cell: forge-cell`. No such folder exists | `00 - ENTRY.md` Status; `manifest.json` | Kept as-is (Tier 2), flagged in the manifest's `active_cell_note`. The meaning is unknown. Ask only if it turns out to matter | OPEN → low priority |
| G-C16 | The handoff's snapshot doesn't match disk in three places: `03 - architecture-governance/` was missing from the first clone (it arrived in commit 7a4eff4); distribution has 4 templates, not 6; content-infrastructure has 16 specs + 1 reference, not 17 specs | `00-control/source-intent/01 - CLOUD_AI_HANDOFF.md` §7.1 vs disk | Recorded in `meta_workspace.md` §3 (finding F-01). The handoff is Tier 1 and is not edited | RESOLVED (recorded) |

## G-D — Enforced doctrine not yet propagated into the files it names

| ID | Gap | Evidence | Resolution / next step | Status |
|---|---|---|---|---|
| G-D01 | PERFECTIONISM Rule 1 names the writing OUTPUT_CONTRACT, "add gate 7: crafted_surplus". It had 6 gates | `03 - architecture-governance/02 - doctrine-enforcement/PERFECTIONISM_ENFORCEMENT.md`; `01 - writing-department/OUTPUT_CONTRACT.md` | Gate 7 appended, matching prompt 05's existing P1 | FIXED S001 |
| G-D02 | PERFECTIONISM Rule 3: every output template must carry the surplus requirement. None did | `02 - content-distribution/05 - templates/*.md` | SURPLUS line appended to the Substack article, LinkedIn and Twitter templates | FIXED S001 |
| G-D03 | PERFECTIONISM Rule 2: every delivery packet carries a `SURPLUS:` line. No delivery packet template exists | — | Must be built into `09 - delivery/delivery-packet-template.md` when it is created | OPEN → build Phase E |
| G-D04 | OMNICHANNEL Rule 1: every public route ends in a PUBLISH_KIT. The distribution workflow ends in per-layer drafts | `02 - content-distribution/00 - ENTRY.md` workflow | See G-C08 | OPEN → build Phase D |
| G-D05 | OMNICHANNEL Rule 2: each variant passes the perfection gate on its own. No per-variant gate was defined; prompt 05 is article-shaped | `01 - writing-department/01 - prompt-library/05 - PROMPT_perfection_gate.md` | Per-variant gate appended to `decomposition-checklist.md`. It only combines existing checks: layer verification table + V1–V3 + P1 + Rule 1 test | FIXED S001 |
| G-D06 | OMNICHANNEL Rule 4: partial publications must be logged. No file says where | `OMNICHANNEL_ENFORCEMENT.md` Rule 4 | Proposal: `PUBLISH_KIT/partial_publication.yaml` inside each kit. Decide at the first kit | OPEN → first kit |

## G-M — Missing machinery (steps with no operator, template or artifact)

| ID | Gap | Evidence | Resolution / next step | Status |
|---|---|---|---|---|
| G-M01 | No single index joined scaffold and departments; no state file | handoff §7.3 gaps 9–10 | `00 - ENTRY.md` Company Map appended; `00-control/STATE.md` written | FIXED S001 |
| G-M02 | The research gate (KSE substitute) has no script operator. The 4 checks are judged by hand | `01 - writing-department/WORKING_RULES.md` Rule 1 | At the first article, write a checker for the countable checks (≥ 3 source categories, ≥ 5 observations, ≥ 1 synthesis insight, folders on disk). "Original synthesis possible" stays human judgment. Build it from the first real research folder, not before (Build Order Law) | OPEN → first article |
| G-M03 | Stage 04 requires a named author's voiceprint (3–5 real writing samples). No author is named; no `voiceprints/` folder exists | `01 - writing-department/01 - prompt-library/04 - PROMPT_voice_humanization.md`; WIRING_MANIFEST | Human input (G-H01, G-H05) | HUMAN |
| G-M04 | PUBLISH_KIT requires website and Medium variants, but neither has a layer WORKFLOW / OUTPUT_CONTRACT | `OMNICHANNEL_ENFORCEMENT.md` Rule 1; `02 - content-distribution/` has no such layers | Write the two layer contracts while producing the first kit, from the real article | OPEN → build Phase D |
| G-M05 | Threads, Medium and Facebook post templates are named but don't exist (Instagram too, but it has no layer) | `02 - content-distribution/00 - ENTRY.md` | Build each template when its first variant is written | OPEN → first kit |
| G-M06 | The knowledge-work override needs three contracts: research-dossier, compiler, handoff. None exist, so P1–P4 in `03-setup` are invalid | `derive_phase.py` output; handoff §3 | Dossier contract: derive it from dossier D-001 once it has run (build Phase B). Compiler contract: derive it from the first compiled positioning (Phase D). Handoff contract: Phase I, or earlier if a handoff fails | OPEN → Phases B, D, I |
| G-M07 | `execute.md` describes a gate with no operator (handoff §2.7) | `00-control/execute.md` | Operator appended: `derive_phase.py` "Buyer-facing gate", with resolution defined by evidence | FIXED S001 |
| G-M08 | `asset-intake.md` repeats the same thesis lines for 3 surfaces; `work-choices.md` duplicates `status.md` | `00-control/asset-intake.md`, `00-control/work-choices.md` | Left in place (no deletion). STATE.md marks them redundant. Real intake arrives through F-001 and `02-sourcing/input_registry.md` | RESOLVED (noted) |
| G-M09 | The convergence objective ("six slots align") is not measurable | `05-convergence/objective_function.md` | Build Phase B, step 3 | OPEN → build Phase B |
| G-M10 | The writing department's quality stage covers articles only. No quality engine exists for the audit brief or reports | `01 - writing-department/OUTPUT_CONTRACT.md` | `10 - quality/` (build Phase E) | OPEN → build Phase E |
| G-M11 | The handoff (the governing law) existed only in chat | — | Stored verbatim in `00-control/source-intent/` | FIXED S001 |
| G-M12 | No link checker or phase operator existed, so "linked" and "phase 3" were unverifiable claims | — | `00-control/tools/check_links.py`, `00-control/tools/derive_phase.py`; fixture-tested in both directions | FIXED S001 |

## G-H — Human-only inputs

| ID | Question | Staged in | Status |
|---|---|---|---|
| G-H01 | Friend's role: operator, first client, or both | `00-control/carbon-input/CARBON_INPUT_FORM-001.md` Q1 | HUMAN |
| G-H02 | First real buyer: role, size, industry, what they tried | F-001 Q2 | HUMAN |
| G-H03 | Offer and price: audit fee model, retainer price and contents | F-001 Q3 | HUMAN |
| G-H04 | Channels live today, and the name they publish under | F-001 Q4 | HUMAN |
| G-H05 | Author voiceprint: 3–5 real writing samples | queued for F-002 | HUMAN (queued) |
| G-H06 | Public proof permissions: which results, names and numbers | queued for F-002 | HUMAN (queued) |

## Update rule

1. A session that closes a gap sets its Status to `FIXED Sxxx`, cites the fix path in the Resolution cell, and adds a line to `meta_workspace.md` §3.
2. New gaps get the next ID in their class. Never renumber.
3. Recount the Summary table whenever statuses change.
