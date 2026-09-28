# 01 - discovery

Status: BUILT (session S003, 2026-09-28; v2 after the design lock)

**Purpose:** learn the client's world well enough that strategy can decide from facts. ARENA researches the buyer, the market and the rules, and samples the top creators in the client's niche; the client supplies what only they know. The node turns what comes back into three files the client keeps: the client brief, the creator library and the voiceprint.

**Use when:** a task on the engagement route arrives from `01 - commercial/06 - billing-advance`.

## Stages (run in order: each stage folder's `00 - ENTRY.md` is its instruction)

| # | Stage folder | One job | Writes |
|---|---|---|---|
| 1 | `01 - requests/` | Send ARENA the research questions and the creator-sampling spec (H3), and the client any questions discovery needs (H1); hold | `21-discovery/01-requests.md`, `21-discovery/arena-request-1.md` (+ client round file if needed) |
| 2 | `02 - findings/` | Read the dossier and the client's answers into a source ledger, findings and the updated slot board | `21-discovery/02-slot-board.md`, `03-sources.md`, `04-findings.md` |
| 3 | `03 - creators/` | Turn the creator sampling into a pattern library per channel | `21-discovery/05-creator-library.md` |
| 4 | `04 - voice/` | Extract the voiceprint from the client's own writing, or model it on creators they choose | `21-discovery/06-voiceprint.md` |
| 5 | `05 - brief/` | Compile the client brief: slots, buyer profiles, market map, proof, open items | `21-discovery/07-client-brief.md` |
| 6 | `06 - gate/` | Check; carry forward; publish brief, creator library and voice to the client folder; advance | the `CONTEXT.md` section, `21-discovery/gate.md` |
| — | `work/` | Tasks at this node | — |

Shared definitions: `00 - control/01 - law/BRIEF_SLOTS.md`, `TASK_CONTRACT.md`, `HANDOFFS.md` (H1, H3).

## Writes (checked by `00 - control/02 - tools/task.py check`)

| File in the task folder | Stage |
|---|---|
| `21-discovery/01-requests.md` | 1 |
| `21-discovery/arena-request-1.md` | 1 |
| `21-discovery/02-slot-board.md` | 2 |
| `21-discovery/03-sources.md` | 2 |
| `21-discovery/04-findings.md` | 2 |
| `21-discovery/05-creator-library.md` | 3 |
| `21-discovery/06-voiceprint.md` | 4 |
| `21-discovery/07-client-brief.md` | 5 |
| `CONTEXT.md#21-discovery` | 6 |
| `21-discovery/gate.md` | 6 |

## Passes to

`02 - content/02 - strategy`, with every slot first needed at intake or discovery Known, and every other slot Known or routed.

## Past material merged here

| From | Became |
|---|---|
| `99 - archive/2026-09-28-restructure/02-sourcing/research_plan.md`, `source_ledger.md` (brief → lane map → queries; url · date · claim · confidence · implication) | The ARENA request's lanes in `01 - requests/`, and the source-ledger format in `02 - findings/` |
| `99 - archive/2026-09-28-restructure/02-sourcing/01 - dossiers/D-001-buyer-and-problem/DOSSIER.md` | `01 - requests/query-bank.md` |
| `99 - archive/2026-09-28-restructure/01 - writing-department/01 - prompt-library/04 - PROMPT_voice_humanization.md`, Part A | `04 - voice/voiceprint-prompt.md` |
| `99 - archive/2026-09-28-restructure/02 - content-distribution/04 - facebook-layer/WORKFLOW.md` (persona: interest, trigger, angle) | The buyer-profile template in `05 - brief/` |
| Pipeline v1 `99 - archive/2026-09-28-pipeline-v1/02 - discovery/02 - research/` (live research by the node) | `02 - findings/`: research is now done by ARENA; the node reads the dossier |
