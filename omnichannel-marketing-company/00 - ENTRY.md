# Omnichannel Marketing Company

## What this company does

A client sends a vague request, for example *"I'm into precious gemstones selling and want to like build corporate gifts as a sub branch"*. This folder turns it into a complete omnichannel content package: research-backed long-form pieces, a channel-native variant of each for every channel in the plan, visual briefs, and a publishing schedule. It is delivered as one paste-ready package.

## Who sends requests

Founders and small-business owners, and marketers acting for their own clients, who want marketing done. Usually they have no marketing know-how and no clear brief. The line is built to work from one vague sentence.

## How it works

A request becomes a **task folder**. The task floats through ten **nodes**. Each node does one job, reads what earlier nodes wrote into the task, and writes its own files into the task. A task leaves a node only when that node's gate passes. At `04 - planning` the task **branches**, one child task per content piece. At `09 - packaging` the children are **joined** back into the parent. The finished task folder holds everything, and is filed in `10 - delivery/done/`.

    request ─► 01 intake ─► 02 discovery ─► 03 strategy ─► 04 planning ─┬─► 05 research ─► 06 drafting ─► 07 review ─► 08 shaping ─┐
                                                                         │      (one child task per piece; FAIL at 07 goes back)   │
                                                                         └────────────── parent waits ──────────► 09 packaging ◄───┘
                                                                                                                    │
                                                                                                        10 delivery ─► done

## Folders

| Folder | What happens there |
|---|---|
| `00 - control/` | The law every node obeys, the operator tools, company state, the operator's source intent, and registers |
| `01 - intake/` | The vague request becomes a task that knows what was said, what it could mean, and what is missing. Round-1 client questions go out |
| `02 - discovery/` | Client answers, research and the client's own writing become a verified client brief, with every slot filled |
| `03 - strategy/` | Positioning, messages, channel plan and objectives, approved by the client |
| `04 - planning/` | The content plan, one brief per piece, then the branch into child tasks |
| `05 - research/` | Per piece: research the topic out to its full boundary, then compress it into a spine |
| `06 - drafting/` | Per piece: draft from the spine, then re-voice the draft as the client |
| `07 - review/` | Per piece: the quality gate. PASS floats the piece on; FAIL sends it back with the defect named |
| `08 - shaping/` | Per piece: decomposition seeds, the hub version, one variant per channel, visual briefs, a gate per variant |
| `09 - packaging/` | Join the pieces into one publish kit, the schedule, and the client package |
| `10 - delivery/` | Hand over, record what happened, write lessons into the ledgers, file the task |
| `99 - archive/` | Past material, now merged into the nodes above. Read-only |

## Start here

- **A new request:** open `01 - intake/00 - ENTRY.md`.
- **Resuming work:** read `00 - control/03 - state/STATE.md`, then run `python3 "00 - control/02 - tools/task.py" status`.

## Operator commands (run from this folder)

    python3 "00 - control/02 - tools/task.py" new --slug SLUG --client LABEL --via CHANNEL [--kind rehearsal] --text "REQUEST"
    python3 "00 - control/02 - tools/task.py" status
    python3 "00 - control/02 - tools/task.py" check T-…
    python3 "00 - control/02 - tools/task.py" advance T-…
    python3 "00 - control/02 - tools/task.py" advance T-… --to "06 - drafting" --reason "…"
    python3 "00 - control/02 - tools/task.py" branch T-… --start "05 - research" --join "09 - packaging" --children SLUG …
    python3 "00 - control/02 - tools/task.py" join T-… [--absorb]
    python3 "00 - control/02 - tools/check_links.py"
    python3 "00 - control/02 - tools/derive_phase.py"

## Rules of the line

1. A task leaves a node only when every file in the node's `## Writes` table exists in the task, and the node's `gate.md` says `VERDICT: PASS`.
2. Nodes write only inside the task folder. The one exception: `10 - delivery` appends to its ledgers.
3. Nothing is invented. Client facts go to the client, facts about the world go to research, and guesses become stated assumptions (`00 - control/01 - law/BRIEF_SLOTS.md`).
4. Every public piece fans out to every channel in the plan. Each variant passes its own gate and names its crafted surplus (`00 - control/01 - law/OMNICHANNEL_ENFORCEMENT.md`, `00 - control/01 - law/PERFECTIONISM_ENFORCEMENT.md`).
5. Nothing is sold before it has been made, checked and delivered once. The first task of any new offer is a free proof run (`10 - delivery/02 - record/00 - ENTRY.md`).

Location in CE: `03 - work-projects/02 - company/02 - working-companies/omnichannel-marketing-company/`.
