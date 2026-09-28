# Hand-offs

**Purpose:** every exchange between a task and the world outside the pipeline, in one place. For each one: what the node writes, who carries it and where, what comes back, and where it lands in the task. A node that sends something out holds the task (`task.py hold`) and resumes only when the return has landed (`task.py resume`). Nothing downstream starts early.

Nodes never talk to the outside world themselves. **The operator carries every hand-off.**

## The five hand-offs

| # | Hand-off | The node writes | The operator | Comes back to |
|---|---|---|---|---|
| H1 | **Client** | A client-facing file, named `NN-<name>-for-client.md`, in the node's folder | Sends it to the client, unchanged; pastes the client's reply verbatim | `from-client/<node folder>-<name>-reply.md`, e.g. `11-intake/04-questions-round-1-for-client.md` → `from-client/11-intake-questions-round-1-reply.md` |
| H2 | **Operator decision** | A request in the node's folder, named `NN-<name>-for-operator.md`: what to decide, the options, the recommendation | Decides, and writes the decision | `from-operator/<node folder>-<name>.md`, e.g. `14-proposal/03-signoff-for-operator.md` → `from-operator/14-proposal-signoff.md` |
| H3 | **ARENA** (research) | `<folder>/arena-request-<n>.md` (format below) | Copies it to `D:\ROOT\CE\03 - work-projects\01 - arena`, where the ARENA pipeline processes it and generates `exec.md`; runs `exec.md`; brings back the dossier | `<folder>/arena-dossier-<n>/` (the dossier files, as returned) |
| H4 | **Image factory** (every still: post images, carousel slides, covers, thumbnails, video frames) | One prompt file per still, `<folder>/stills/<still-id>.prompt.md` | Copies the prompt files to `D:\ROOT\CE\03 - work-projects\02 - company\02 - working-companies\design-visual-artist-brand\01 - foundation\13-media-department\03 - media-production\IMAGE_CREATION\00 - INTAKE\01 - queue`; brings back each still | Next to its prompt: `<folder>/stills/<still-id>.<png or jpg>` |
| H5 | **Motion** (movement between two stills) | One prompt file per transition, `<folder>/motion/<transition-id>.prompt.md` | Runs it in the motion (image-to-video) tool with the two stills it names; brings back the clip | Next to its prompt: `<folder>/motion/<transition-id>.mp4` |

## How a node waits

1. Write the outgoing file(s).
2. Run `python3 "00 - control/02 - tools/task.py" hold <task-id> --on "<hand-off>: <file(s)>"`, e.g. `--on "H3 ARENA: 21-discovery/arena-request-1.md"`.
3. Stop. The task stays at this node with status HOLD.
4. When the return has landed where the table says, the operator (or the next LLM session) runs `task.py resume <task-id> --note "<what arrived>"`, and the stage continues from the step after the hand-off.

A return that is incomplete (a dossier missing a requested section, a still that doesn't match its prompt) is a reason to send a second request, numbered `-2`, not to proceed on a gap.

## The ARENA request format (H3)

ARENA turns a vague request into a research dossier. Our request gives it everything it needs to do that without seeing the rest of the task:

    # ARENA request — <task id> · <n>
    Company: Omnichannel Marketing Company · Node: <department/node> · Date: <date>
    ## Who this is for
    <client, what they sell, to whom, where — 3 lines, each with its source tag>
    ## What we must learn
    RQ<n>. <question> — Capture: … — Why: <the decision it feeds>
    …
    ## Top-creator sampling (when requested)
    Niche: … · Channels: … · How many creators per channel: … · Posts per creator: …
    Extract for each: hooks · structures and formats · angles that perform (and saturated ones) ·
    funnel mechanics (CTAs, lead magnets, link placement, cross-posting) · cadence and timing · visual styles
    Rule: record patterns and example links; never copy text as ours.
    ## Output wanted
    A dossier with one section per RQ and one per channel sampled; every claim with its source
    (url or path, date read, confidence, implication).
    ## Return to
    <task folder>/<node folder>/arena-dossier-<n>/

## Rules

- **One hand-off, one file.** A request never hides inside another file.
- **Verbatim back.** Returns are stored as they arrive. Summaries and judgments go in the node's own numbered files, citing the return.
- **Rehearsal tasks** write every outgoing file but never send it. Their hold names the hand-off with "rehearsal: not sent".
