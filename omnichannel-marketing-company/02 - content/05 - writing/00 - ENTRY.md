# 05 - writing

Status: BUILT (session S003, 2026-09-28; v2 after the design lock)

**Purpose:** the writing department. For every piece in the month plan: research the topic through ARENA until the boundary is mapped, compress it into a spine, draft, re-voice as the client, judge it, then shape it natively for every channel in the plan, script the videos, prompt every still for the image factory, and pass a human check for clarity of thought. It turns complicated knowledge into simple, sharp content that spreads and sends readers to the destination.

**Use when:** a task arrives from `04 - planning` (both routes). All pieces of the month are written inside this one node; each piece has its own folder in the task.

## How the work is laid out in the task

    25-writing/
    ├── 00-piece-index.md          every piece and the stage it has reached (kept current by every stage)
    ├── arena-request-1.md         one ARENA request for all the month's topics (stage 1)
    ├── arena-dossier-1/           what ARENA returns
    ├── P1-<slug>/                 one folder per piece
    │   ├── 01-sources.md  02-boundary-map.md  03-observations.md  04-spine.md   (stage 1)
    │   ├── 05-draft.md  06-article.md  07-review.md  08-seeds.md                  (stages 2–5)
    │   ├── channels/<channel>.md                                                   (stage 6)
    │   └── scripts/<V-id>.md                                                       (stage 7, if video)
    ├── stills/                    one prompt per still, and each returned image next to it (stage 8)
    │   └── 00-still-index.md
    ├── 09-human-check-for-operator.md   (stage 9)
    └── gate.md

## Stages (run in order: each stage folder's `00 - ENTRY.md` is its instruction)

| # | Stage folder | One job | Writes |
|---|---|---|---|
| 1 | `01 - research/` | Per topic: send ARENA the research and the top-post sampling (H3); map the boundary; build the spine | `arena-request-1.md`, `00-piece-index.md`; per piece `01-`–`04-` |
| 2 | `02 - draft/` | Draft the full article from the spine | per piece `05-draft.md` |
| 3 | `03 - voice/` | Re-voice the draft as the client | per piece `06-article.md` |
| 4 | `04 - review/` | Judge the article: PASS, or FAIL back to the stage that caused it | per piece `07-review.md` |
| 5 | `05 - seeds/` | Six self-contained seeds from the passed article, assigned to channels | per piece `08-seeds.md` |
| 6 | `06 - channels/` | One native variant per channel in the plan, each by its channel's craft | per piece `channels/<channel>.md` |
| 7 | `07 - scripts/` | Video script and storyboard for each piece the plan marks as video | per piece `scripts/<V-id>.md` |
| 8 | `08 - visuals/` | One scene prompt per still for the image factory (H4); hold; check what returns | `stills/` |
| 9 | `09 - human-check/` | The operator's manual check: reads human, clear thinking, knowledge compressed into wisdom (H2) | `09-human-check-for-operator.md` |
| 10 | `10 - gate/` | Check every piece and every variant; carry forward; advance | the `CONTEXT.md` section, `25-writing/gate.md` |
| — | `work/` | Tasks at this node | — |

## Writes (checked by `00 - control/02 - tools/task.py check`)

| File in the task folder | Stage |
|---|---|
| `25-writing/00-piece-index.md` | 1 (kept current by every stage) |
| `25-writing/arena-request-1.md` | 1 |
| `25-writing/stills/00-still-index.md` | 8 |
| `25-writing/09-human-check-for-operator.md` | 9 |
| `CONTEXT.md#25-writing` | 10 |
| `25-writing/gate.md` | 10 |

The gate checks every per-piece file by name (step 1 of `10 - gate/`).

## Passes to

`03 - video-factory/01 - script` when the engagement includes video; otherwise `02 - content/06 - packaging`.

## Past material merged here

| From | Became |
|---|---|
| `99 - archive/2026-09-28-restructure/01 - writing-department/01 - prompt-library/` (prompts 01–05: boundary, synthesis, draft, voice, perfection gate) | `01 - research/01 - request/boundary-prompt.md`, `01 - research/03 - spine/spine-prompt.md`, `02 - draft/draft-prompt.md`, `03 - voice/revoice-prompt.md`, `04 - review/gate-prompt.md`, carried verbatim |
| `99 - archive/2026-09-28-restructure/01 - writing-department/OUTPUT_CONTRACT.md` §3 (six decomposition seeds) | `05 - seeds/` |
| `99 - archive/2026-09-28-restructure/02 - content-distribution/05 - templates/*` and each layer's OUTPUT_CONTRACT | The channel folders in `06 - channels/` |
| `99 - archive/2026-09-28-restructure/04 - media-department/VISUAL_BRIEF_CONTRACT.md` | `08 - visuals/`: briefs are now scene prompts for the image factory |
| Pipeline v1 nodes `05 - research`, `06 - drafting`, `07 - review`, `08 - shaping` (`99 - archive/2026-09-28-pipeline-v1/`) | This one node, as the operator decided: the writing department is one node |
