# Company Function Design Flow Analysis

Scope: `03 - work-projects/02 - company`

Purpose: simulate how a zero-context Instruction Processor agent enters Company, identify token-waste and non-determinism in the instruction chain, and record the repairs made to the folder rules files.

## Bounded Method

- Read CE root boot workspace areas only through the prescribed dry-run boot entrypoint and `BOOT_REPORT.md`.
- Did not read forbidden session-state files.
- Did not read raw idea payloads, live company payloads, generated run bodies, or prompt-bank bodies.
- Read only Company root entry workspace areas, one-level Company subcell entries, meta-company control workspace areas, packet headers/bodies, stage README files, and the Tech Bro Scratchpad entry because the stimulus explicitly asked for that comparison.

## Boot Observation

The boot dry run returned `BOOT OK`, but `BOOT_REPORT.md` and `REALIZED_FUNCTION_NODE.md` pointed to a stale `zetaquar

For this pass, the current user stimulus explicitly instructed continuing against boot blockers. The stale boot mismatch is therefore evidence, not governing task context.

## First-Principles Entry Simulation

### 1. CE root

A generic agent entering the workspace first sees root `AGENTS.md` by native agent convention. That file says FORGE defines active runtime, WORKSPACE_META defines orchestration rules, and the agent must run:

```text
python "01 - FORGE/02 - source-truth/00 - runtime-entrypoints/BOOT.py" --dry-run --input-file "<resolved input file path>" --emit-report
```

If no input file is available, the agent passes direct task prose as positional stimulus text. It must not pass a file path as stimulus text.

Then it may read only:

```text
01 - FORGE/03 - active-runs/02 - session-state/state/BOOT_REPORT.md
```

Correct action: boot first, then follow the report. Failure mode observed in this run: the report can remain stale relative to a fresh stimulus and point the agent into an unrelated realized function folder.

### 2. `03 - work-projects`

If the agent is routed or instructed into work projects, `ENTRY.md` explains the folder map and says to avoid blind subcell reads. It also says specific project work can enter the named project folder directly.

Pre-repair issue: it implied every project has a normal `ENTRY.md`; Tech Bro Scratchpad actually uses `[READ FIRST] ENTRY.md`.

Repair: `03 - work-projects/ENTRY.md` now names the Tech Bro entry file explicitly.

### 3. `03 - work-projects/02 - company`

The first file an agent is likely to encounter is `AGENTS.md`, because native agent runtimes auto-load that name. Pre-repair, `AGENTS.md` contained:

- higher authority stack
- local entry rule: read `ENTRY.md`
- company set
- navigation rules
- write rules

Its direct action was: read `ENTRY.md` before any company work.

`ENTRY.md` then contained:

- read order: `AGENTS.md`, then `ENTRY.md`, then one matching subcell entry
- subcell map
- route selection rules
- safe raw idea entry path
- first-read law
- slug alias law

Wrong interpretation risk: if an agent reads `AGENTS.md` automatically, then reads `ENTRY.md`, the `ENTRY.md` read order can send it back to `AGENTS.md`. This is not infinite if the agent is disciplined, but it is a repeat-read trap.

Repair: Company `AGENTS.md` is now explicitly an adapter pointer, and Company `ENTRY.md` is the only execution entry. If the agent arrived from `AGENTS.md`, it must not reread `AGENTS.md`.

### 4. Route selection inside Company

For the current architecture task, `ENTRY.md` routes to `SURFACE_MAP.md` for navigation upkeep. `SURFACE_MAP.md` says it is not first-read authority. This is correct as long as it remains support material only.

For a net-new company idea, `ENTRY.md` routes to:

```text
01 - meta-company (copy this folder before modding)/ENTRY.md
```

### 5. `01 - meta-company`

Pre-repair flow:

1. `ENTRY.md`
2. `AGENTS.md`
3. `00-control/NATIVE_PACKET_STATE_MACHINE.md`
4. `00-control/execute.md`
5. `05 - assets/01 - prompt-chain/03 - agentic-runbook.md`
6. packet headers in declared order
7. first matching packet body plus declared `read_set`

Wrong interpretation risks:

- `ENTRY.md` told the agent to read `AGENTS.md`; `AGENTS.md` told the agent to read `ENTRY.md` first.
- `execute.md` skipped `01 - slot-resolution.md` and jumped from context intake to deterministic expansion.
- Several workspace areas defined `<WORK_PROJECTS_ROOT>` as an absolute Windows path.
- Stage and sub-agent role names drifted between packet headers and `SUBAGENTS.md`.
- `02 - deterministic-expansion.md` was described in `SUBAGENTS.md` as writing the downstream Function Folder intake, but the actual packet only writes `function_node_staged.md`; `03 - convergence-gate.md` performs the downstream handoff.

Repairs made: meta-company `ENTRY.md`, `AGENTS.md`, `execute.md`, state machine, runbook, stage README, write workspace areas, and `SUBAGENTS.md` now agree on one packet-per-pass execution.

## Actual Instruction Propagation Structure

Current intended path for Company is:

```text
CE root AGENTS.md
-> BOOT.py dry-run
-> BOOT_REPORT.md
-> 03 - work-projects/ENTRY.md
-> 03 - work-projects/02 - company/AGENTS.md as adapter if auto-loaded
-> 03 - work-projects/02 - company/ENTRY.md
-> one selected route only
```

For net-new idea ingress:

```text
02 - company/ENTRY.md
-> 01 - meta-company (copy this folder before modding)/ENTRY.md
-> 01 - meta-company (copy this folder before modding)/AGENTS.md
-> 00-control/NATIVE_PACKET_STATE_MACHINE.md
-> 00-control/execute.md
-> 05 - assets/01 - prompt-chain/03 - agentic-runbook.md
-> packet headers until first true trigger
-> selected packet plus declared read_set only
-> declared write_set only
```

For live company work:

```text
02 - company/ENTRY.md
-> 02 - working companies/ENTRY.md
-> named company ENTRY.md
```

For generated attempts:

```text
02 - company/ENTRY.md
-> 03 - NEW Generated company attempts/ENTRY.md
-> named attempt manifest/status only if explicitly named
```

For legacy tooling:

```text
02 - company/ENTRY.md
-> 00 - company tools/ENTRY.md
-> instructions.md and factory-maturity-ladder.md only as required
```

For governance work:

```text
02 - company/ENTRY.md
-> 05 - architecture-governance/ENTRY.md
-> named governance report
```

## Discrepancy Map

| Discrepancy | Impact | Repair |
|---|---|---|
| Root Company had both `AGENTS.md` and `ENTRY.md` acting like entries | repeat reads and authority ambiguity | `AGENTS.md` now declares itself an adapter pointer; `ENTRY.md` is the single execution entry |
| Historical archive folder was unnumbered and typo-heavy | local folder did not independently compile as a numbered workspace area | renamed to `04 - historical-company-building-research/` and updated references |
| No governance folder for design-flow findings | audit output would become root loose prose | added `05 - architecture-governance/` with its own `ENTRY.md` |
| `execute.md` skipped `01 - slot-resolution.md` | raw idea could jump into function-folder expansion before refinement | rewrote `execute.md` as a packet router that stops after one selected packet |
| `<WORK_PROJECTS_ROOT>` was defined as an absolute machine path | non-portable between Windows machines and bridge mounts | changed definitions to `<CE_ROOT>/03 - work-projects` |
| `SUBAGENTS.md` role names did not match packet headers | parent could dispatch the wrong role with the wrong return expectation | aligned role names and outputs with packet headers |
| Stage 02 was described as writing downstream Function Folder intake | duplicate handoff risk and false completion | Stage 02 now writes only `function_node_staged.md`; Stage 03 writes downstream handoff and receipt |
| Packet `00 - context-intake.md` mentioned unresolved fields in JSON while output is markdown | output-format confusion | changed wording to markdown outputs |
| `03 - work-projects/ENTRY.md` implied Tech Bro has normal `ENTRY.md` | false path read | now names `[READ FIRST] ENTRY.md` explicitly |
| `00 - company tools/prompt.md` embedded absolute Windows paths | non-portable legacy fallback | replaced with `<CE_ROOT>` token references |

## Sub-Agent Creation Rules

Global rule: sub-agents are packet-bound. They may be spawned only after the parent has selected one packet from disk. The sub-agent receives no chat history, sibling folders, prompt-bank excerpts, or broad state.

Native app dispatch input must contain only:

- `idea_id`
- selected packet path
- exact `read_set`
- exact `write_set`
- packet `input_format`
- packet `output_format`
- packet `blocker_format`

Completion is file-system based. Chat text from a sub-agent is never completion evidence.

| Packet | Trigger condition | Spawn condition | Direct inputs | Scope | Completion/writeback |
|---|---|---|---|---|---|
| `00 - context-intake.md` | `raw_idea_input.md` exists and `raw_idea_staged.md` is missing | raw idea contains multiple source files or long dumps | packet file; `10 - raw-idea-intake/<idea-id>/raw_idea_input.md` | compress arbitrary business seed into staged signals | write `20 - raw-idea-staged/<idea-id>/raw_idea_staged.md` and `30 - legacy-refinement/<idea-id>/legacy_refinement_input.md` |
| `01 - slot-resolution.md` | `legacy_refinement_input.md` exists and `legacy_refinement_staged.md` is missing | one idea can be resolved without sibling packets | packet file; `30 - legacy-refinement/<idea-id>/legacy_refinement_input.md` | resolve staged seed into deterministic company design | write `30 - legacy-refinement/<idea-id>/legacy_refinement_staged.md` and `40 - function-folder-intake/<idea-id>/function_node_input.md` |
| `02 - deterministic-expansion.md` | `function_node_input.md` exists and `function_node_staged.md` is missing | input is self-contained and names no undeclared reads | packet file; `40 - function-folder-intake/<idea-id>/function_node_input.md` | build one Function Folder-ready execution packet | write `50 - function-folder-ready/<idea-id>/function_node_staged.md` |
| `03 - convergence-gate.md` | `function_node_staged.md` exists and `handoff_receipt.md` is missing | parity check needs independent review | packet file; `50 - function-folder-ready/<idea-id>/function_node_staged.md` | verify handoff parity and terminal readiness | write `<WORK_PROJECTS_ROOT>/03 - FUNCTION_FOLDER/02 - STAGING/COMPANY_PACKET_INTAKE/<idea-id>/function_node_input.md` and `50 - function-folder-ready/<idea-id>/handoff_receipt.md` |

## Raw Idea Lifecycle

Unprocessed ideas live at:

```text
01 - meta-company (copy this folder before modding)/00-control/10 - raw-idea-intake/<idea-id>/raw_idea_input.md
```

Naming law:

- folder name is `idea-id`
- only required intake file is `raw_idea_input.md`
- no other file in that folder is needed to start packet `00`

Lifecycle:

1. Raw idea intake
   - Input: `10 - raw-idea-intake/<idea-id>/raw_idea_input.md`
   - Packet: `00 - context-intake.md`
   - Transform: reduce raw idea into named actors, buyer path signals, offer signals, asset/workspace area signals, proof signals, tool route signals, blockers
   - Outputs: `20 - raw-idea-staged/<idea-id>/raw_idea_staged.md`; `30 - legacy-refinement/<idea-id>/legacy_refinement_input.md`
   - Completion: staged file exists; next-stage input exists; blocker token on line 1 if unusable

2. Legacy refinement
   - Input: `30 - legacy-refinement/<idea-id>/legacy_refinement_input.md`
   - Packet: `01 - slot-resolution.md`
   - Transform: resolve company seed, leverage actor, buyer path, primary offer, tool route, channel split, proof structure, first function-folder goal
   - Outputs: `30 - legacy-refinement/<idea-id>/legacy_refinement_staged.md`; `40 - function-folder-intake/<idea-id>/function_node_input.md`
   - Completion: staged refinement exists; function-folder input exists; unresolved fields are explicit blockers

3. Function-folder intake
   - Input: `40 - function-folder-intake/<idea-id>/function_node_input.md`
   - Packet: `02 - deterministic-expansion.md`
   - Transform: expand one self-contained company design into a bounded execution packet with exact read/write sets and disk-verifiable completion test
   - Output: `50 - function-folder-ready/<idea-id>/function_node_staged.md`
   - Completion: staged function-folder packet exists; blocker token on line 1 if input is not self-contained

4. Convergence gate
   - Input: `50 - function-folder-ready/<idea-id>/function_node_staged.md`
   - Packet: `03 - convergence-gate.md`
   - Transform: verify packet quality and copy the self-contained packet into Function Folder staging
   - Outputs: `<WORK_PROJECTS_ROOT>/03 - FUNCTION_FOLDER/02 - STAGING/COMPANY_PACKET_INTAKE/<idea-id>/function_node_input.md`; `50 - function-folder-ready/<idea-id>/handoff_receipt.md`
   - Completion: `function_node_staged.md` and `handoff_receipt.md` both exist, and the receipt confirms parity or records a blocker

Stable refined status is reached only when both terminal Company files exist and the downstream Function Folder intake copy exists.

## Legacy Prompt Handling

Current packet headers say their `prompt_source` is the packet file itself and that no external prompt-bank body is attached at runtime. This is deterministic and token-efficient, but it means the folder is not currently executing external prompt-bank bodies for this chain.

If external legacy prompts are promoted later, the required change is header-level, not chat-level:

- add exact root-relative prompt-bank path
- add prompt hash
- add that prompt to the packet `read_set`
- keep one selected packet per pass
- keep the output format unchanged unless the state machine is updated in the same pass

## Tech Bro Scratchpad Comparison

Tech Bro Scratchpad uses a stronger local-entry membrane:

```text
03 - scratchpad/[READ FIRST] ENTRY.md
```

It declares itself a local function folder and explicitly forbids external boot prerequisites. Raw source material enters:

```text
03 - scratchpad/00-SELF/SOURCE_FILES/
```

The local index and state choose one concrete source file, then the flow is:

```text
source file
-> First Cognitive Sequence grounded artifact
-> IC Second cognitive sequence instructions artifact
-> promoted staged file
-> failure-check proof
```

Important difference: Tech Bro's source folder is input material only, not authority. Company now mirrors that principle: `raw_idea_input.md` is input material only; packet headers are authority.

## Architectural Rules To Propagate

Every folder should independently compile before an agent enters children:

- exactly one execution entry workspace area per folder
- `AGENTS.md` may exist only as adapter law; it must point to the entry and avoid loops
- every non-entry markdown file must be support, report, or packet material with a declared role
- root-level loose artifacts should become numbered folders or governed support files
- all cross-root paths use `<CE_ROOT>` or root-relative paths, never machine-specific absolute paths
- stage movement must be visible as file creation, not chat memory
- each sub-agent receives one packet and declared reads only
- each stage writes its declared outputs and then stops
- blocked stages still write the expected stage output with a literal blocker token on line 1
- only token-expensive discoveries should be promoted into durable entry/rule workspace areas

## Repair Log

Changed workspace areas:

- `03 - work-projects/ENTRY.md`
- `03 - work-projects/02 - company/AGENTS.md`
- `03 - work-projects/02 - company/ENTRY.md`
- `03 - work-projects/02 - company/SURFACE_MAP.md`
- `03 - work-projects/02 - company/00 - company tools/instructions.md`
- `03 - work-projects/02 - company/00 - company tools/prompt.md`
- `03 - work-projects/02 - company/01 - meta-company (copy this folder before modding)/AGENTS.md`
- `03 - work-projects/02 - company/01 - meta-company (copy this folder before modding)/ENTRY.md`
- `03 - work-projects/02 - company/01 - meta-company (copy this folder before modding)/00-control/NATIVE_PACKET_STATE_MACHINE.md`
- `03 - work-projects/02 - company/01 - meta-company (copy this folder before modding)/00-control/execute.md`
- `03 - work-projects/02 - company/01 - meta-company (copy this folder before modding)/00-control/SUBAGENTS.md`
- `03 - work-projects/02 - company/01 - meta-company (copy this folder before modding)/00-control/MASTER.md`
- `03 - work-projects/02 - company/01 - meta-company (copy this folder before modding)/00-control/WRITE_SURFACE.md`
- `03 - work-projects/02 - company/01 - meta-company (copy this folder before modding)/00-control/WORKING_STATE.md`
- `03 - work-projects/02 - company/01 - meta-company (copy this folder before modding)/00-control/40 - function-folder-intake/README.md`
- `03 - work-projects/02 - company/01 - meta-company (copy this folder before modding)/05 - assets/01 - prompt-chain/00 - context-intake.md`
- `03 - work-projects/02 - company/01 - meta-company (copy this folder before modding)/05 - assets/01 - prompt-chain/03 - agentic-runbook.md`
- `03 - work-projects/02 - company/01 - meta-company (copy this folder before modding)/05 - assets/01 - prompt-chain/03 - convergence-gate.md`

Moved workspace area:

- `carbon's limited thinking abou all this - company building in deterministic scripts/`
- to `04 - historical company-building research/`

Added workspace areas:

- `05 - architecture-governance/ENTRY.md`
- `05 - architecture-governance/function-design-flow-analysis.md`

## Follow-Up Resolution

- Follow-up pass on 2026-05-11 rewrote generated LexBridge run packets, context manifests, dispatch packets, capability cards, dashboard data, and related governance workspace areas to remove machine-specific CE-root paths.
- LexBridge now has cold portability law at `02 - working companies/lexbridge/11-governance/portability-contract.md`.
- The processed output for that follow-up pass is `02 - working companies/lexbridge/11-governance/processed-session-output.md`.

## Remaining Risks

- `working_rules.py` was not changed because the relevant learning belongs in Company entry/control workspace areas, not in the Function Folder query executable.
- The boot stale-continuation issue is outside Company and should be fixed in FORGE/WORKSPACE_META routing separately.
