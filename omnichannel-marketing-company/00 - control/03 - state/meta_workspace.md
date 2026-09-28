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
6. *(promoted S002, PT-04)* Before trusting a new gate's FAIL, test it on fixtures in both directions, including the case where a cap or exemption could mask a violation.
7. *(promoted S002, PT-06)* Any description of the disk — a handoff, or the operator's own picture of the line — is a hypothesis. Check it against the files before acting on it, and report where it differs.
8. *(S002)* The line decides what may run next: M6 picks work from the first station that isn't FILLED (`python3 00-control/tools/line_status.py`). Work that produces no content, such as capability cards, may run beside it.

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

### S002 — 2026-09-28

**Input (M0).** The operator's assembly-line directive, stored verbatim in `00-control/source-intent/03 - operator-directives-2026-09-28.md` and logged as I-001 to I-007 in `02-sourcing/input_registry.md`. It decides the friend's role, fixes the buyer type, sets the offer order, sets the platform order, rules on the image gap and on first-piece linking, and states the line law.

**What was done, in order:**
1. Checked the directive against disk (M2) → findings F-11 and F-12.
2. Archived the three placeholder foundation files (`01-foundation/META/archive/2026-09-28-placeholder/`).
3. Wrote the input registry, the source ledger (disk evidence only), the research plan and dossier D-001 (staged, not run).
4. Wrote five claim files in `01-foundation/`, with every bullet tagged.
5. Wrote `00-control/ASSEMBLY_LINE.md` and `00-control/tools/line_status.py`. The operator's first run exposed two deadlocks (F-14), which were fixed. Fixture tests exposed a masked violation (F-15), which was fixed.
6. Extended `derive_phase.py`: the new markers, the two new foundation files, and a paid-offer gate.
7. Built the image-station intake (`04 - media-department/`) and `02 - content-distribution/CHANNEL_ACTIVATION.md`.
8. Appended wiring, waiting and exemption sections to 18 Tier 2 files.
9. Staged F-002 and recorded the answers in F-001.
10. Updated the gap register (64 gaps), `PHASE_DERIVATION.md`, `STATE.md` and this file.

S001 gap-register counts, for the record: 55 gaps (18 fixed, 13 registered or resolved, 17 open, 7 human).

**Findings:**

| ID | Finding | Evidence | Why it matters | Action |
|---|---|---|---|---|
| F-11 | The operator's model said the downstream folders read a voice file that holds "the wrong name". On disk, the writing chain had an **empty** author slot, and the earlier project's identity sat inline in the platform and governance defaults | `01 - writing-department/01 - prompt-library/00 - WIRING_MANIFEST.md`; the LinkedIn contract's vertical list | "Just fill the file" only works once every reader actually reads the file | Created `01-foundation/author-voice.md`, with a one-line pointer in each of its 6 readers (G-C17) |
| F-12 | The operator said "some" platforms need an image. On disk, all of them do, including both pilot channels | source ledger L-006 | Without a producer the pilot can reach text-complete, not complete | Every slot marked WAITING; the decision is surfaced in `00-control/STATE.md` (G-C18) |
| F-13 | Taken literally, "the first piece is excused, later pieces follow the rule" still leaves piece 2 unable to meet a ≥ 2-link minimum | Substack hub contract §4 | A rule that can't be met stalls the second piece the same way it stalled the first | The one-line exemption counts only earlier pieces that exist (G-C19) |
| F-14 | On its first run, the line operator found two deadlocks: the price waits on PR-001, but PR-001 waits on S2; and S1b's own research was scheduled after S1 | first `line_status.py` output | A strict gate plus a rule that schedules something later equals a line that can never move | `[DEFERRED: …, per I-nnn]` (listed, not blocking; must cite its rule). A station's research runs inside that station (G-M14) |
| F-15 | Fixture T4: the S7 image cap turned "a kit exists before the gate" into PARTIAL, which hid a real skip-ahead | fixture run T4 | A cap written for honesty masked a violation | Units are judged on raw output before any cap. Output ahead of an unfilled station is a violation |
| F-16 | "Paid after one proven run" vs the capability law ("market only `live_capability`", which needs ≥ 2 reconciled runs) | handoff §2.5 | Obeying one rule literally would break the other | The first paid audit is sold framed as validated; it becomes live after the second reconciled delivery (G-C20) |
| F-17 | `04-interface/execution-sequence.md` ordered the website and pitch before any proof | that file | It contradicts I-003 | Marked superseded (G-C21) |
| F-18 | The phase advanced to 2 while the line is stuck at S1 | the two operators' output | A cold reader could read "phase 2" as progress on content | Both are recorded side by side in `00-control/PHASE_DERIVATION.md` |

**Three-tier receipt (S002):**
- **Verified:** the line operator reports stuck at S1, no skip-ahead, exit 0, and was fixture-tested on 5 cases. `derive_phase.py` gives phase 2 and the manifest agrees; the paid-offer gate is CLOSED. `check_links.py` passes. The gap register recount was scripted from its rows. Every Tier 2 change is an append or a path fix (`git diff --numstat`).
- **Partial:** the identity binding and channel activation are written and pointed to, but no unit has read them yet.
- **Open:** F-002 (the friend); D-001 not run; Phase C not built; the image producer decision.

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
| D-13 | The voice file is `01-foundation/author-voice.md` (station S1a). Its readers are bound by one-line pointers; no folder is rebuilt | edit every reader to carry the name | The operator asked for exactly one file to hold the truth (I-001). Pointers make that literally true | Low |
| D-14 | The first spoke is LinkedIn | Twitter/X | It was read off the wiring: week-1 pairing, core-insight seed, buyer type, doctrine set with machinery (`02 - content-distribution/CHANNEL_ACTIVATION.md`) | Low: change the Activation cells |
| D-15 | Piece folders: `01 - writing-department/03 - research/research-[slug]/`. Kits: `02 - content-distribution/06 - publish-kits/[slug]/PUBLISH_KIT/` | decide at first use | The line's station table needs real paths to be checkable. The locations are the S001 proposals | Low |
| D-16 | The image station is a numbered department (`04 - media-department/`), built intake-first. A producer exists iff `PRODUCER.md` exists | put the briefs inside each layer; wait for a producer before designing anything | The registry models Media as a department. One switch file makes "operational" checkable | Low |
| D-17 | Marker grammar: `[src: L-/I-nnn]`, `[dossier: …, PENDING]`, `[CARBON-BLOCKED: …]`, `[WAITING: …]`, `[DEFERRED: until …, per I-/L-nnn]` | a single "blocked" tag | The line has to tell apart what can be looked up, what only a person knows, what depends on a system, and what a rule deliberately schedules later | Low |
| D-18 | Line strictness: company stations may be PARTIAL (rulings plus named gaps). Units are strict: no output ahead of an unfilled station | strict everywhere | Strict everywhere would have forbidden recording the operator's own rulings. Units are where skipping ahead produces false content | Low |
| D-19 | S1a needs the name, the field **and** the way of talking. Account handles moved to `CHANNEL_ACTIVATION.md` (read at S7) | name and field only | The operator's own words: "a real name, a real field, a real way of talking" before a single sentence. Handles aren't needed to write | Low |
| D-20 | The first paid audit is sold framed as validated; it goes live after a second reconciled delivery | sell as an established service after one run; stay free until two runs | Reconciles I-003 with capability law §2.5 without breaking either | Low |
| D-21 | Prices and proof permissions are not asked in F-002 | ask them now | I-003 defers prices to after PR-001; there is nothing to grant permission for yet | — |
| D-22 | D-001 is staged, not run, this session | run lane L1 now | This session's package was the early-station pass. Lane L1 is the first item in the next action list | — |

---

## 5. Patterns seen (candidates; promoted rows are marked)

A pattern is promoted to an orientation rule (and later to `13 - memory/patterns-to-promote.md`) only after it has been seen in **two or more** real instances (handoff §3, phase 9: "promote only proven patterns").

| ID | Pattern | Instances | Status |
|---|---|---|---|
| PT-01 | A doctrine labelled ENFORCED is often not propagated. Check its "Affected" list against the files it names | 1 (S001: gate 7, surplus lines) | candidate |
| PT-02 | Extracted subtrees carry phantom references. Fix with a register the checker reads, not with deletion | 1 (S001) | candidate |
| PT-03 | Mixed line endings turn small edits into whole-file rewrites. Always edit byte-preservingly | 1 (S001) | candidate |
| PT-04 | A new gate must be fixture-tested in both directions before its FAIL is trusted | 2 (S001: `derive_phase.py`; S002: `line_status.py` T4 caught a masked violation) | **promoted S002** → §2.2 rule 6 |
| PT-05 | Slot checks based on text presence pass vacuously. "Resolved" must mean traced to evidence | 1 (S001: `execute.md` / `asset-intake.md`) | candidate |
| PT-06 | Descriptions of the disk drift from it: verify before acting (P11) | 2 (S001: handoff snapshot F-01; S002: the operator's identity and image model, F-11 and F-12) | **promoted S002** → §2.2 rule 7 |
| PT-07 | A new operator finds design flaws in the rules around it on its first run. Build and run it before polishing the prose | 1 (S002: F-14) | candidate |
| PT-08 | A strict gate needs a "deferred by rule" state, or it deadlocks with any rule that schedules something later | 1 (S002: F-14) | candidate |
