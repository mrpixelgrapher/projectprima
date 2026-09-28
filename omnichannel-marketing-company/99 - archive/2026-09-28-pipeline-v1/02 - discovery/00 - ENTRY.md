# 02 - discovery

Status: BUILT (session S003, 2026-09-28)

**Purpose:** turn intake's open items into one verified **client brief**, with every slot filled, the frame settled and the client's voice captured. Strategy plans from this brief alone.

**Use when:** a task arrives from `01 - intake`. **Holds while:** client answers that this node needs are outstanding (the gate says HOLD, and `waiting on` names them).

## Stages (run in order: each stage folder's `00 - ENTRY.md` is its instruction)

| # | Stage folder | One job | Writes |
|---|---|---|---|
| 1 | `01 - answers/` | Log the client's reply verbatim; update the slot board; settle F1/F2/F4; send round 2 if needed | `client/answers-round-N.md`, `02-discovery/01-slot-board.md` |
| 2 | `02 - research/` | Run every research question whose condition is met; log sources; surface contradictions | `02-discovery/02-sources.md`, `02-discovery/03-findings.md` |
| 3 | `03 - voice/` | Extract the voiceprint from the client's own writing | `02-discovery/04-voiceprint.md` |
| 4 | `04 - brief/` | Compile the client brief: slots, buyer profiles, market map, proof, open items | `02-discovery/05-client-brief.md` |
| 5 | `05 - gate/` | Check the work, write the carry-forward, float | the `CONTEXT.md` section, `02-discovery/gate.md` |
| — | `work/` | Tasks at this node | — |

Shared definitions: `00 - control/01 - law/BRIEF_SLOTS.md`, `00 - control/01 - law/TASK_CONTRACT.md`.

## Writes (checked by `00 - control/02 - tools/task.py check`)

| File in the task folder | Stage |
|---|---|
| `client/answers-round-1.md` | 1 |
| `02-discovery/01-slot-board.md` | 1 |
| `02-discovery/02-sources.md` | 2 |
| `02-discovery/03-findings.md` | 2 |
| `02-discovery/04-voiceprint.md` | 3 |
| `02-discovery/05-client-brief.md` | 4 |
| `CONTEXT.md#02 - discovery` | 5 |
| `02-discovery/gate.md` | 5 |

## Passes to

`03 - strategy`, with a brief in which every slot first needed at 01 or 02 is Known (or Assumed and shown to the client), and every other slot is Known or routed.

## Past material merged here

| From (now in `99 - archive/2026-09-28-restructure/`) | Became |
|---|---|
| `02-sourcing/research_plan.md` (brief → lane map → runnable queries), `02-sourcing/source_ledger.md` (url · date · claim · confidence · implication) | The research procedure and source-ledger template in `02 - research/` |
| `02-sourcing/01 - dossiers/D-001-buyer-and-problem/DOSSIER.md` (buyer, buying-behaviour, alternatives and channel-fact lanes) | `02 - research/query-bank.md`, reusable for any founder-led client |
| `01 - writing-department/01 - prompt-library/04 - PROMPT_voice_humanization.md`, Part A | `03 - voice/voiceprint-prompt.md` |
| `02 - content-distribution/04 - facebook-layer/WORKFLOW.md` (persona: interest, trigger, angle) | The buyer-profile template in `04 - brief/` |
| `01-foundation/*.md` (claims tagged with their evidence or what they wait on) | The evidence rule on every line of the slot board and the brief |
