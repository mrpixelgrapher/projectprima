# Meta Workspace

What this file is: the **repeatable process** this company is built with (§2), and the running record of **what was found, what was decided and why** (§3–§5). The operator asked for this file so that the way work gets done is itself written down and can be repeated, not just the work.

Tiers: §2 is Tier 2 (append amendments, never rewrite; if a step changes, add a dated amendment under it). §3–§5 are append-only logs.
Created: 2026-09-25, session S001. Governing law: `00-control/source-intent/01 - CLOUD_AI_HANDOFF.md`.

---

## 1. The problem this process solves

The inputs this company receives are abstract ("build an omnichannel marketing company for a friend"; "move these folders in and bring around the gaps"). Every session starts with zero memory. Without a fixed process, each session re-derives the situation from scratch, trusts whatever the documents claim, and builds in whatever direction it happens to think of first. The result looks like progress but doesn't compound.

The process below turns any abstract input into governed artifacts on disk, in the same order every time. Each step leaves a file behind, so the next session starts from where this one stopped, not from zero.

## 2. The meta process: abstract input → governed artifact

| Step | Do this | Leaves on disk | Checked by | Prevents |
|---|---|---|---|---|
| **M0 Capture** | Write the raw input to disk verbatim before interpreting it | `00-control/source-intent/NN - *.md` (company-level) or the work unit's intake file | the file exists and has a provenance header | acting on a paraphrase; losing the law when the chat ends |
| **M1 Enter** | Read `00 - ENTRY.md` → `00-control/STATE.md` → only the folder STATE names | nothing new | — | amnesia, blind browsing |
| **M2 Verify disk** | Run the operators; read the files the input names; list every place a document disagrees with disk | findings in §3 | `derive_phase.py`, `check_links.py`, `find`/`ls` output quoted in the finding | implementing stale prescriptions (handoff P11) |
| **M3 Derive** | Derive the phase and state from disk; downgrade any overclaim and name the failing artifact | `00-control/PHASE_DERIVATION.md`, `manifest.json` phase fields | `derive_phase.py` (exit 3 = overclaim) | inherited labels; phase inflation |
| **M4 Decompose** | For each thing the input asks for, ask three questions: does an **artifact** exist, does an **operator** exist, does **evidence** exist? Any "no" becomes a gap row, classed P / X / C / D / M / H | rows in `03 - architecture-governance/INSTRUCTION_GAP_REGISTER.md` | every row cites a path | vague "improve X" work; invisible gaps |
| **M5 Classify** | Put each gap in one class: CE-actionable / agent-executable / human-blocked. Human → CARBON_INPUT_FORM (max 4 questions, recommendation marked). External data → RESEARCH_DOSSIER | `00-control/carbon-input/`, `02-sourcing/01 - dossiers/` | form or dossier exists before dependent work proceeds | stalling; fabricating (handoff P3, P12) |
| **M6 Select one package** | Choose the smallest unit that moves the derived phase or produces a send. Answer P15 first: which files, what each edit does, how to verify | "Next action" in `00-control/STATE.md` | the three answers are written down | scope creep; five half-finished things |
| **M7 Execute row by row** | Action → artifact → verify → next row. Respect the tiers: Tier 1 never edited; Tier 2 append, or correct paths only; Tier 3 regenerate. Anything mechanical becomes a script or a fixed table | the artifacts themselves | `git diff --stat` shows only intended lines | rewriting history; re-deriving mechanics by reasoning |
| **M8 Verify** | Re-run the operators. Read artifacts back. Test any new gate **in both directions** (it must pass when satisfied and fail when not) | operator output quoted in §3 | exit codes | gates that can never pass, or never fail |
| **M9 Crystallize & report** | Update STATE, the registers and §3–§5 here. Report in three tiers (verified / partial / open). Commit | this file, `STATE.md`, commit | a cold reader answers "what exists / what state / what next" from `STATE.md` in 30 s | work done but not meta-work; the next session starting cold |

### 2.1 The same process inside a work unit

A work unit (an article, a client audit, a dossier) is a **folder**, and the folder runs the handoff §4 contract: INTAKE → ORIENTATION → WORKING → OUTPUT → STATE. The folder's own `00 - ENTRY.md` says where each of the five lives and what state the unit is in. M0 is its intake, M1–M3 its orientation, M7 its working, the gated deliverable its output, and M9 its state. The first real instance will be dossier D-001 (see `00-control/STATE.md`). Settle the unit's standard file names only after that instance exists (Build Order Law).

### 2.2 Rules of thumb (earned in S001 — see §5 for their status)

1. If a claim can be checked by a script, write the script before writing the claim.
2. A register that the checker reads beats a list in prose: it cannot silently go stale.
3. Correct a path when a local target exists. Otherwise register it. Never delete a reference.
4. Edit Tier 2 files byte-preservingly (their line endings are mixed). Append new sections at the end with a dated heading.
5. "Resolved" means traced to evidence, not "has text in it".

---

## 3. Session log and findings

### S001 — 2026-09-25

**Input (M0):** the handoff (`00-control/source-intent/01 - CLOUD_AI_HANDOFF.md`) and the directive to move the three department folders into the company, link them, and begin closing gaps in the cognitive instructions (`00-control/source-intent/02 - operator-directives-2026-09-25.md`).

**What was done, in order:**
1. Read every file in the scaffold and all three departments (M1–M2).
2. Fetched `main` and fast-forwarded to 7a4eff4 when `03 - architecture-governance/` turned out to be missing from the clone.
3. Moved the three folders with `git mv` (54 renames, 0 deletions).
4. Wrote `00-control/tools/check_links.py`. Ran it cold: 22 BROKEN, 79 UNREGISTERED.
5. Corrected 17 path strings in 12 files, and registered 173 external references in 15 rows (`03 - architecture-governance/EXTERNAL_DEPENDENCY_REGISTER.md`). Rerun: PASS.
6. Stored the source intent verbatim.
7. Wrote `00-control/tools/derive_phase.py` and fixture-tested it both ways. Derived phase 1 against a claimed 3, and wrote the manifest.
8. Staged `CARBON_INPUT_FORM-001`.
9. Appended wiring and doctrine sections to 12 Tier 2 files.
10. Wrote `INSTRUCTION_GAP_REGISTER.md`, `PHASE_DERIVATION.md`, `STATE.md` and this file.

Order note: the handoff's Phase A says to write PHASE_DERIVATION and STATE "before you create or modify anything else". S001 moved the folders and built the two operators first, because the operator's directive asked for the move, and a phase derivation without an operator would itself have been a gate with no operator (handoff §2.7). The derivation was then produced by the operator rather than by reasoning.

**Findings:**

| ID | Finding | Evidence | Why it matters | Action |
|---|---|---|---|---|
| F-01 | The handoff's snapshot (§7.1) didn't match disk. `03 - architecture-governance/` was absent from the clone (it arrived later in 7a4eff4). Distribution has 4 templates, not 6. Content-infrastructure has 16 specs + 1 reference, not 17 specs | `git log origin/main`; `ls` | Documents drift; disk is the only truth (P11). Trusting the snapshot would have meant rebuilding a folder that already existed | Fetched and fast-forwarded; gap G-C16 |
| F-02 | The relocation broke 4 internal links. 9 pointers still aimed at CE-absolute paths whose targets are now local. 173 references point outside this repo | first `check_links.py` run | Extracted subtrees carry phantom references. Deleting them loses lineage; ignoring them strands a cold instance | 17 path corrections + external register; the checker now fails on unregistered escapes |
| F-03 | Line endings are mixed (37 CRLF, 34 LF files). A naive edit rewrote whole files: 625 changed lines for 17 real changes | `git diff --stat` before and after | A Tier 2 diff must show only path fixes and appends, or the audit trail is unreadable | Reverted; re-applied byte-preserving. Rule of thumb 4 |
| F-04 | The manifest claimed phase 3; disk supports phase 1. 7 of 8 phase-1 minimums were missing before the carbon form was staged | `00-control/PHASE_DERIVATION.md` | Every later decision would have been made from an inflated label | Downgraded; the script now owns the phase fields |
| F-05 | The writing and distribution systems were built for a different business: one creator's multi-vertical personal brand (legal, consulting). There is no marketing vertical, no author for this company, and the creator's own cluster topics | `03 - architecture-governance/MULTI_VERTICAL_CONTENT_OS.md`; `02 - content-distribution/01 - substack-hub/WORKFLOW.md` | The whole engine assumes one named author and their Substack. For this company that author is unknown | Gap G-C12; F-001 Q1 and Q4 |
| F-06 | The seed is ambiguous about the friend: "a company **for** a friend" (the friend as operator) vs "**friend referral** → audit" (the friend as a source of buyers) | `00-control/status.md` | "Scope ambiguity is a blocker, not a note" (handoff §2.6). It decides whose voice, whose channels and who is client #1 | F-001 Q1 (recommendation: operator) |
| F-07 | Two doctrines are labelled "ENFORCED", yet the files they name hadn't received their rules (writing gate 7, SURPLUS lines, a per-variant gate) | `03 - architecture-governance/02 - doctrine-enforcement/*.md` vs the named files | An "enforced" rule that never reached the files it governs is documentation, not a gate | Propagated by append: G-D01, G-D02, G-D05 |
| F-08 | The Media Department is absent, yet every output contract makes a Media visual mandatory, so no variant can pass as things stand | the four layer `OUTPUT_CONTRACT.md` files | The biggest blocker to the first publish kit once research is done | Gap G-X04; proposal: in-repo SVG for diagram-class graphics |
| F-09 | The internal-link rules can't be met by a new cluster's first article | Substack hub contract §4 + cluster rule 4 | A gate that can never pass for article #1 would stall the first loop | Gap G-C05; bootstrap proposal recorded |
| F-10 | `execute.md` was a gate with no operator, and `asset-intake.md` looked "resolved" only because every slot had text | `00-control/execute.md`, `asset-intake.md` | Text-presence checks pass vacuously | Operator appended: resolution means evidence (G-M07) |

**Three-tier receipt (S001):**
- Verified: the folders moved (git renames); links PASS (`check_links.py`); phase 1 derived and written (`derive_phase.py`, exit 0); gates fixture-tested both ways; the gap register's summary recounted from its rows.
- Partial: the channel-matrix and 30-day precedence resolutions are written down (G-C01, G-C02) but not yet exercised on a real kit.
- Open: everything tagged OPEN or HUMAN in the gap register; the research dossier (next session).

---

## 4. Decision log

| ID | Decision | Alternatives considered | Why | Cost to reverse |
|---|---|---|---|---|
| D-01 | Move the three folders **directly** into `omnichannel-marketing-company/` with `git mv` | a `departments/` subfolder | Literal operator directive. Keeps every sibling link (".\..\01 - writing-department\" etc.) valid. `git mv` preserves history (P17) | Low: `git mv` back |
| D-02 | Keep the departments' original names, even though their numbers overlap the scaffold's (`01-foundation` / `01 - writing-department`) | renumber the departments | Renaming would break 37 cross-department name references in the original files (counted with `git grep` at the pre-move commit), and would override the operator's own naming. The Company Map in `00 - ENTRY.md` explains the two tracks | Medium: rename plus relink |
| D-03 | Correct a path when a local target exists; otherwise register it | delete dead references; leave them | Tier 2 allows path correction; deletion loses lineage (P17); leaving them strands cold instances | Low |
| D-04 | Gate-table paths where the handoff named none: `06 - capability/`, `07 - acquisition/`, `00-control/contracts/`, and the file names inside `08`–`14` | wait and name them later | A phase gate must name its artifact to have a verification path (§2.7). The numbering continues the handoff's `08 - proof` … `14 - governance` | Low: edit the table in `derive_phase.py`, log here |
| D-05 | Foundation evidence convention: a `## Claims` section; every bullet tagged `[src:]`, `[dossier:]` or `[CARBON-BLOCKED]` | tagging every line of the file | Makes the Phase B acceptance ("no sentence unsourced and unmarked") machine-checkable, while leaving room for context prose | Low |
| D-06 | Exercised-loop checks never pass by script until a real ledger row defines their schema | define ledger schemas now | Build Order Law: instance first. A schema written before any matter exists would be guesswork, and a gate that passes on guesswork is inflation | Low |
| D-07 | Buyer-facing gate = foundation tagged + override contracts + ≥ 1 `live_capability` row | "phase ≥ N" | Derived directly from handoff §2.4 (compile from dossiers), §2.5 (market only live capabilities) and the override | Low |
| D-08 | The manifest's `phase`, `phase_label` and `phase_derived_on` are written only by `derive_phase.py --write-manifest` | hand-edit | "Do not hand-edit what a process regenerates" (P18) | Low |
| D-09 | Store the handoff and directives verbatim as Tier 1 source intent | summarise them | Conversation is not evidence; a summary is not the law | — |
| D-10 | "Live company" = derived phase 8 (LIVE GOVERNED OPERATION), because the ENTRY's promotion route is outside this repo | phase 7; operator decides | Phase 8 is the Phase Map's own "live" label. Open to operator override (G-X11) | Low |
| D-11 | Tier 2 edits = new dated sections appended at the end of the file | inline insertions | Keeps original prose intact; makes each session's changes auditable in one place | — |
| D-12 | New files use LF and company-root-relative forward-slash paths. Existing files keep their own endings and `.\` style | convert everything | Converting would rewrite every Tier 2 file (F-03). `check_links.py` resolves both styles | Low |

---

## 5. Patterns seen (candidates, not promoted)

A pattern is promoted to an orientation rule (and later to `13 - memory/patterns-to-promote.md`) only after it has been seen in **two or more** real instances (handoff §3, phase 9: "promote only proven patterns").

| ID | Pattern | Instances | Status |
|---|---|---|---|
| PT-01 | A doctrine labelled ENFORCED is often not propagated. Check its "Affected" list against the files it names | 1 (S001: gate 7, surplus lines) | candidate |
| PT-02 | Extracted subtrees carry phantom references. Fix with a register the checker reads, not with deletion | 1 (S001) | candidate |
| PT-03 | Mixed line endings turn small edits into whole-file rewrites. Always edit byte-preservingly | 1 (S001) | candidate |
| PT-04 | A new gate must be fixture-tested in both directions before its FAIL is trusted | 1 (S001: `derive_phase.py`) | candidate |
| PT-05 | Slot checks based on text presence pass vacuously. "Resolved" must mean traced to evidence | 1 (S001: `execute.md` / `asset-intake.md`) | candidate |
| PT-06 | A handoff snapshot drifts from disk within hours. Verify before acting (P11) | 1 (S001: F-01) | candidate |
