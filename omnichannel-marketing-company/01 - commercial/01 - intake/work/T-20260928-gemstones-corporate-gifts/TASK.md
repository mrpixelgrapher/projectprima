# TASK T-20260928-gemstones-corporate-gifts

| Field | Value |
|---|---|
| id | T-20260928-gemstones-corporate-gifts |
| kind | rehearsal |
| client | gemstone-seller |
| route | direct |
| includes | — |
| created | 2026-09-28 |
| arrived via | opened for month None |
| node | 01 - commercial/01 - intake |
| folder | 11-intake |
| status | HOLD |
| waiting on | H1 client (rehearsal: not sent): 11-intake/04-questions-round-1-for-client.md |

The operator (`00 - control/02 - tools/task.py`) keeps the table above, the Route and the History. Gate stages decide; the operator moves. Law: `00 - control/01 - law/TASK_CONTRACT.md`.

## Route

Route `direct` from `00 - control/01 - law/ROUTES.md`. Written by the operator; `◀ here` marks the current node.

| Step | Node | Folder in this task | Runs |
|---|---|---|---|
| 1 | 01 - commercial/01 - intake | 11-intake | yes ◀ here |
| 2 | 01 - commercial/02 - scope | 12-scope | yes |
| 3 | 02 - content/01 - discovery | 21-discovery | yes |
| 4 | 02 - content/02 - strategy | 22-strategy | yes |
| 5 | 02 - content/03 - performance | 23-performance | yes |
| 6 | 02 - content/04 - planning | 24-planning | yes |
| 7 | 02 - content/05 - writing | 25-writing | yes |
| 8 | 03 - video-factory/01 - script | 31-script | no (not included) |
| 9 | 03 - video-factory/02 - shots | 32-shots | no (not included) |
| 10 | 03 - video-factory/03 - stills | 33-stills | no (not included) |
| 11 | 03 - video-factory/04 - motion | 34-motion | no (not included) |
| 12 | 03 - video-factory/05 - edit-plan | 35-edit-plan | no (not included) |
| 13 | 02 - content/06 - packaging | 26-packaging | yes |
| 14 | 02 - content/07 - publishing | 27-publishing | no (not included) |
| 15 | 02 - content/08 - delivery | 28-delivery | yes |

## Start here (cold instance)

1. Read `CONTEXT.md` in this folder: what is known so far, compressed, with sources.
2. Read the client folder, `clients/<client>/` (the `client` field above), starting at its `00 - ENTRY.md`.
3. Open the current node's ENTRY at the company root: `<node>/00 - ENTRY.md`, where `<node>` is the `node` field above. Its files in this task go in the folder named in the `folder` field.
4. Run that node's stages in order, each from its own `00 - ENTRY.md`. If `status` is HOLD, the node is waiting on what `waiting on` names: do nothing until it has arrived and the task is resumed.

## History

| Date | Event | Where | Note |
|---|---|---|---|
| 2026-09-28 | created | 01 - commercial/01 - intake | route direct; request captured verbatim via chat |
| 2026-09-28 | hold | 01 - commercial/01 - intake | H1 client (rehearsal: not sent): 11-intake/04-questions-round-1-for-client.md |
