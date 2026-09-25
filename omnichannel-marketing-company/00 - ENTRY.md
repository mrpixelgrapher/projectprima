# ENTRY - Omnichannel Marketing Company

## Parent

Parent: `.\03 - work-projects\02 - company\03 - company-creation-protocol`

This is a generated attempt, not a live company.

## Ancestry

- Parent: `.\03 - work-projects\02 - company\03 - company-creation-protocol`
- Root map: `.\02 - WORKSPACE_META\06 - human-readable\CANONICAL_PATHS.md`

## Read Order

1. `manifest.json`
2. `00-control/status.md`
3. `00-control/asset-intake.md`
4. The exact file named by the user's task

## Status

- Folder class: generated attempt
- Promotion status: not promoted
- Active folder: `forge-folder`

## Runtime Law

- Do not route live Company work here unless this attempt is explicitly named.
- Do not treat generated scaffold files as proof of a live operating company.
- Buyer-facing asset work remains blocked at `00-control/asset-intake.md` if any required field is unresolved.
- Promotion or rebuild must go through `../../01 - meta-company-template/00 - control/10 - raw-idea-intake/<idea-id>/raw_idea_input.md`.

## Company Map (appended 2026-09-25, session S001)

Added because the scaffold and the departments had no shared index (handoff §7.3, gap 10). The Read Order above still applies. This section adds where everything is and what runs next.

### Cold-boot order

1. `manifest.json`, then `00-control/status.md` (Read Order steps 1–2 above).
2. `00-control/STATE.md`: the derived phase, what is real and what is placeholder, the gap list, and the exact next action.
3. Run the two operators and compare their output with STATE.md:
   - `python3 00-control/tools/derive_phase.py` re-derives the phase from disk. Exit 3 means the manifest overclaims.
   - `python3 00-control/tools/check_links.py` checks that every path reference resolves or is registered. Exit 1 means a link is broken.
4. Enter only the folder STATE.md names. `meta_workspace.md` explains the repeatable process and why decisions were made.

### Folders

Two tracks share this folder. **Pipeline** folders hold this company's own build state. **Department** folders hold reusable operating methodology that the pipeline calls. Their numbers overlap (`01-foundation` vs `01 - writing-department`) because the departments kept their original names, which keeps their sibling-relative links working (decision D-02 in `meta_workspace.md`).

| Folder / file | Track | What it is | State on 2026-09-25 |
|---|---|---|---|
| `00-control/` | control | status, state, phase derivation, operators (`tools/`), carbon input forms | real |
| `00-control/source-intent/` | control | the handoff and the operator directives, verbatim (Tier 1) | real |
| `01-foundation/` | pipeline | customer, problem, value proposition | placeholder |
| `02-sourcing/` | pipeline | research plan, input registry, source ledger, dossiers | question bank only |
| `03-setup/01 - outputs/` | pipeline | P1 positioning, P2 pitch stack, P3 website surface, P4 channel copy | stubs; invalid until the knowledge-work override is satisfied |
| `04-interface/` | pipeline | execution sequence | plan, not exercised |
| `05-convergence/` | pipeline | objective function | placeholder |
| `01 - writing-department/` | department | research-first article engine: rules, contract, 5 stage prompts | substantive, not exercised (0 research folders) |
| `02 - content-distribution/` | department | Substack hub plus LinkedIn, Twitter/X + Threads and Facebook layers; templates | substantive, not exercised (0 drafts) |
| `03 - architecture-governance/` | governance | registry, dependency graph, doctrine enforcement, 16 specs, instruction-gap and external-dependency registers | substantive |
| `meta_workspace.md` | control | the repeatable meta process, plus the findings and decisions log | real |

Future pipeline folders are declared by the gate table in `00-control/tools/derive_phase.py`: `06 - capability/`, `07 - acquisition/`, `08 - proof/`, `09 - delivery/`, `10 - quality/`, `11 - client-state/`, `12 - upgrade/`, `13 - memory/`, `14 - governance/`, and `00-control/contracts/`. Create each one when its build phase starts, not before.

### How the tracks connect

    02-sourcing (dossiers) ──► 01-foundation ──► 03-setup outputs (compiled, never drafted cold)
          ▲
          │ Stage 01 boundary discipline reused for business research
          │
    01 - writing-department ──► 02 - content-distribution ──► PUBLISH_KIT (one per article)
      research → spine → draft → voice → gate    Substack hub → channel-native variants

    03 - architecture-governance: the rules every folder obeys, plus the registers of what is still missing

- **Research.** Business research (buyer, market) lives in `02-sourcing/`. Article research lives in the writing department's `research-[slug]/` folders. Both follow the boundary discipline of `01 - writing-department/01 - prompt-library/01 - PROMPT_boundary_research.md`.
- **Positioning and site copy** in `03-setup` are compiled from dossiers, never drafted cold (handoff §2.4).
- **Public content** flows from writing to distribution and ends in a PUBLISH_KIT (`03 - architecture-governance/02 - doctrine-enforcement/OMNICHANNEL_ENFORCEMENT.md`).
- **External CE references** inside department files resolve through `03 - architecture-governance/EXTERNAL_DEPENDENCY_REGISTER.md`. Open instruction gaps are listed in `03 - architecture-governance/INSTRUCTION_GAP_REGISTER.md`.
- **Status label.** "Generated attempt, not a live company" (above) stays true until `derive_phase.py` derives phase 8, LIVE GOVERNED OPERATION. The promotion route named in the Runtime Law lives outside this repo (register X-11) and cannot run here, so until it can, the derived phase is the status authority.
