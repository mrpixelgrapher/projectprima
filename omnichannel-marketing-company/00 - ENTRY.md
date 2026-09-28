# Omnichannel Marketing Company

## What this company does

A client sends a vague request, for example *"I'm into precious gemstones selling and want to like build corporate gifts as a sub branch"*. The company turns it into agreed, paid, monthly organic content that grows their business: research-backed pieces on every channel they bought, engineered to spread on their own and to convert, every one driving traffic to a single destination online (a newsletter, a site, a landing page), plus videos when they want them. No paid ads: the performance is designed into the content.

## Who sends requests

Founders and small-business owners, and marketers acting for their own clients, who want marketing done. Usually they have no marketing know-how and no clear brief. The line is built to work from one vague sentence.

## How it works

A request becomes a **task folder**. The task moves through **nodes**, one at a time: an LLM works the task at one node using only that node's instructions and the task's files, and when the node's gate passes, moves the task to the next node on its **route**. Nothing is skipped; a node that needs something from outside (the client, the operator, ARENA's research, the image factory) holds the task until it arrives. Each client has one permanent **client folder** that every one of their tasks reads and builds on.

    engagement route (a new request):
      01 commercial:  intake ─► scope ─► pricing ─► proposal ─► billing (advance)
      02 content:     discovery ─► strategy ─► performance ─► planning ─► writing
      03 video:       [script ─► shots ─► stills ─► motion ─► edit plan]        (when video is included)
      02 content:     packaging ─► [publishing] ─► delivery                     (publishing when included)
      01 commercial:  billing (on delivery) ─► done, filed in clients/<client>/done/

    month route (each retainer month after the first):
      month-review ─► billing (advance) ─► performance ─► planning ─► writing ─► [video] ─► packaging ─► [publishing] ─► delivery ─► billing ─► done

    direct route (no commercials: rehearsals and internal runs):
      intake ─► scope ─► discovery ─► strategy ─► performance ─► planning ─► writing ─► [video] ─► packaging ─► [publishing] ─► delivery ─► done

## Folders

| Folder | What happens there |
|---|---|
| `00 - control/` | The law every node obeys (task contract, routes, hand-offs, brief slots, instruction standard, doctrines), the operator tools, company state, the operator's own words, and registers |
| `01 - commercial/` | The front door and the money: intake, scope, pricing, proposal, billing, and each month's review and upsell |
| `02 - content/` | The content line: discovery, strategy, performance, planning, writing (the writing department), packaging, publishing, delivery |
| `03 - video-factory/` | Scripts and storyboards become videos: shot design, stills from the image factory, motion prompts, edit plans |
| `clients/` | One permanent folder per client: profile, engagement, rates, brief, voice, creator library, strategy, performance design, results, history, finished tasks |
| `99 - archive/` | Past material, merged into the nodes above. Read-only |

## Start here

- **A new request:** open `01 - commercial/01 - intake/00 - ENTRY.md`.
- **Resuming work:** read `00 - control/03 - state/STATE.md`, then run `python3 "00 - control/02 - tools/task.py" status`.
- **A task on HOLD:** its `waiting on` field says what it waits for; `00 - control/01 - law/HANDOFFS.md` says who carries it and where it lands.

## Operator commands (run from this folder)

    python3 "00 - control/02 - tools/task.py" new --route engagement|direct --client CLIENT --slug SLUG --label "LABEL" --via CHANNEL [--kind rehearsal] --text "REQUEST"
    python3 "00 - control/02 - tools/task.py" new --route month --client CLIENT --month YYYY-MM
    python3 "00 - control/02 - tools/task.py" status
    python3 "00 - control/02 - tools/task.py" check T-…
    python3 "00 - control/02 - tools/task.py" advance T-…
    python3 "00 - control/02 - tools/task.py" advance T-… --to "02 - content/04 - planning" --reason "…"
    python3 "00 - control/02 - tools/task.py" hold T-… --on "…"
    python3 "00 - control/02 - tools/task.py" resume T-… --note "…"
    python3 "00 - control/02 - tools/task.py" close T-… --reason "…"
    python3 "00 - control/02 - tools/check_links.py"
    python3 "00 - control/02 - tools/derive_phase.py"

## Rules of the line

1. One node at a time, in route order. A task leaves a node only when every file in the node's `## Writes` table exists and its `gate.md` says `VERDICT: PASS`.
2. Nodes write only inside the task folder. The exceptions: gates publish passed files to the client folder, and commercial and delivery append their ledgers (`00 - control/01 - law/TASK_CONTRACT.md` §7).
3. Nothing is invented. Client facts come from the client, facts about the world from ARENA, and guesses become stated assumptions (`00 - control/01 - law/BRIEF_SLOTS.md`).
4. Every piece fans out to every channel in the plan, natively, and every variant passes its own gate and names its crafted surplus (`00 - control/01 - law/OMNICHANNEL_ENFORCEMENT.md`, `PERFECTIONISM_ENFORCEMENT.md`).
5. Nothing is made that the engagement doesn't list. On the engagement and month routes, content work starts only after the advance is paid (`01 - commercial/00 - ENTRY.md`); the direct route has no commercial side.

Location in CE: `03 - work-projects/02 - company/02 - working-companies/omnichannel-marketing-company/`.
