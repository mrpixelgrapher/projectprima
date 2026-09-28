# 02 - strategy

Status: BUILT (session S003, 2026-09-28; v2 after the design lock)

**Purpose:** decide what the client's buyers must hear, where every piece sends them (the destination), what each bought channel does, and what counts as success, and get the client's yes before anything is written. Performance and planning build on this strategy; nothing is produced without it.

**Use when:** a task on the engagement route arrives from `01 - discovery`. **Holds while:** the client hasn't approved the strategy.

## Stages (run in order: each stage folder's `00 - ENTRY.md` is its instruction)

| # | Stage folder | One job | Writes |
|---|---|---|---|
| 1 | `01 - positioning/` | The buyer's problem, the alternatives, the provable difference, one position statement. For a NEW brand: name options | `22-strategy/01-positioning.md` |
| 2 | `02 - messages/` | 3–5 message pillars with proof, objections and buyer stage; the brand voice rules | `22-strategy/02-messages.md` |
| 3 | `03 - destination/` | The one place online every piece drives traffic to, what lives there, and the one action it asks for | `22-strategy/03-destination.md` |
| 4 | `04 - channels/` | Each channel the client bought: its role, focus, cadence and how it sends traffic to the destination | `22-strategy/04-channel-plan.md` |
| 5 | `05 - objectives/` | Measurable objectives: baseline, target, how and when they are read | `22-strategy/05-objectives.md` |
| 6 | `06 - approval/` | The strategy on one page for the client (H1); hold; apply the reply | `22-strategy/06-strategy-for-client.md`, `22-strategy/07-approval.md` |
| 7 | `07 - gate/` | Check; carry forward; publish the strategy to the client folder; advance | the `CONTEXT.md` section, `22-strategy/gate.md` |
| — | `work/` | Tasks at this node | — |

## Writes (checked by `00 - control/02 - tools/task.py check`)

| File in the task folder | Stage |
|---|---|
| `22-strategy/01-positioning.md` | 1 |
| `22-strategy/02-messages.md` | 2 |
| `22-strategy/03-destination.md` | 3 |
| `22-strategy/04-channel-plan.md` | 4 |
| `22-strategy/05-objectives.md` | 5 |
| `22-strategy/06-strategy-for-client.md` | 6 |
| `22-strategy/07-approval.md` | 6 |
| `CONTEXT.md#22-strategy` | 7 |
| `22-strategy/gate.md` | 7 |

## Passes to

`02 - content/03 - performance`, with an approved position, pillars, destination, channel plan and objectives, published as `clients/<client>/strategy.md`.

## Past material merged here

| From | Became |
|---|---|
| `99 - archive/2026-09-28-restructure/02 - content-distribution/MULTI_PLATFORM_ARCHITECTURE.md` (hub-and-spoke, one-way flow, audience coverage, seed map) and `99 - archive/2026-09-28-restructure/02 - content-distribution/00 - ENTRY.md` (platform registry) | `04 - channels/channel-roles.md`; the one-way flow now ends at the destination |
| `99 - archive/2026-09-28-restructure/02 - content-distribution/CHANNEL_ACTIVATION.md` (hub + first spoke chosen from evidence) | Superseded by the design lock: the engagement fixes the channels; `04 - channels/` gives each a role |
| `99 - archive/2026-09-28-restructure/03 - architecture-governance/MULTI_VERTICAL_CONTENT_OS.md` (a per-vertical focus for each channel) | The per-channel "focus for this client" column in the channel plan |
| `99 - archive/2026-09-28-restructure/03 - architecture-governance/01 - content-infrastructure/11 - multi-vertical-content-operating-system.md` (awareness stages) | The buyer-stage field on each pillar in `02 - messages/` |
| `99 - archive/2026-09-28-restructure/05-convergence/objective_function.md` and `99 - archive/2026-09-28-restructure/03-setup/01 - outputs/` (P1…P4) (positioning core, pitch stack) | The measurable objective in `05 - objectives/` and the position statement in `01 - positioning/` |
