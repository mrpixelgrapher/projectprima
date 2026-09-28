#!/usr/bin/env python3
"""task.py - open, check, move, hold and close client tasks along their route.

A task is a folder. Where it sits is its state: every task lives in exactly one
node's `work/` folder, or in `clients/<client>/done/`. Moving the folder is how it
moves. Law: `00 - control/01 - law/TASK_CONTRACT.md` (the task), `ROUTES.md` (the
order of nodes), `HANDOFFS.md` (holding for something from outside).

Usage (run from the company root):
  task.py new --route engagement --client SLUG --slug SLUG --label LABEL (--text TEXT | --file PATH)
              [--via CHANNEL] [--kind real|rehearsal]
  task.py new --route month --client SLUG --month YYYY-MM [--kind real|rehearsal]
  task.py status
  task.py check TASK
  task.py advance TASK
  task.py advance TASK --to "NN - department/NN - node" --reason TEXT
  task.py hold TASK --on TEXT
  task.py resume TASK --note TEXT
  task.py close TASK --reason TEXT
  (global: --date YYYY-MM-DD overrides today's date, for tests and back-dating)

A node is a folder `NN - <node>` inside a department folder `NN - <department>`
(NN 01-89) that has a `00 - ENTRY.md`. Its folder inside a task is named
`<department digit><node digit>-<node>`, e.g. `01 - commercial/01 - intake` -> `11-intake`.
The node's ENTRY declares what the tool enforces:
  `Status: BUILT`     a task may enter and leave it;
  `## Writes` table   the files a task must hold before it leaves (first column,
                      backticked; `file#Heading` also needs that `## Heading`;
                      every `gate.md` must say VERDICT: PASS).

Rules enforced:
  - forward only through a passed gate, to the next step of the task's route that
    runs (`includes` decides the optional steps); into built nodes only;
  - a task on HOLD does not move until it is resumed;
  - backward only to an earlier step of the same route, with --reason; the gates and
    CONTEXT sections from that step up to the current one are marked superseded
    (renamed, never deleted), so each of those nodes must pass its gate again;
  - on a forward move, the passed gate's `Waiting on:` line is copied to `waiting on`,
    and an `Includes:` line (written only by the proposal gate) to `includes`;
  - a finished or closed task is filed in `clients/<client>/done/`.
Exit code: 0 on success, 1 when a rule refuses the action, 2 on bad usage.
"""
from __future__ import annotations

import argparse
import datetime
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ROUTES = ROOT / "00 - control" / "01 - law" / "ROUTES.md"
CLIENTS = ROOT / "clients"
TEMPLATE = CLIENTS / "00 - template"
NUMBERED = re.compile(r"^(\d{2}) - ([a-z][a-z-]*)$")
TICK = re.compile(r"`([^`\n]+)`")
SEPARATOR = re.compile(r"^\s*\|[\s:|-]+\|\s*$")
SLUG = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+){0,4}")
NONE = "—"
FIELDS = ["id", "kind", "client", "route", "includes", "created", "arrived via", "node", "folder", "status", "waiting on"]


def refuse(msg: str) -> int:
    print(f"refused: {msg}")
    return 1


def usage(msg: str) -> int:
    print(msg)
    return 2


# ------------------------------------------------------------------ nodes and routes
def nodes() -> dict[str, Path]:
    """'01 - commercial/01 - intake' -> its folder."""
    out = {}
    for dept in sorted(ROOT.iterdir()):
        m = NUMBERED.match(dept.name)
        if not (dept.is_dir() and m and 1 <= int(m.group(1)) <= 89):
            continue
        for node in sorted(dept.iterdir()):
            n = NUMBERED.match(node.name)
            if node.is_dir() and n and (node / "00 - ENTRY.md").is_file():
                out[f"{dept.name}/{node.name}"] = node
    return out


def node_dir(rel: str) -> Path:
    found = nodes().get(rel)
    if found is None:
        print(f"no node {rel!r}; nodes are:\n  " + "\n  ".join(nodes()))
        sys.exit(2)
    return found


def folder_of(rel: str) -> str:
    """'01 - commercial/01 - intake' -> '11-intake'."""
    dept, node = rel.split("/")
    d, n = NUMBERED.match(dept), NUMBERED.match(node)
    return f"{int(d.group(1))}{int(n.group(1))}-{n.group(2)}"


def entry(rel: str) -> str:
    return (node_dir(rel) / "00 - ENTRY.md").read_text(encoding="utf-8")


def is_built(rel: str) -> bool:
    m = re.search(r"^Status:\s*\**\s*(NOT BUILT|BUILT)", entry(rel), re.M)
    return bool(m) and m.group(1) == "BUILT"


def writes(rel: str) -> list[str]:
    m = re.search(r"^## Writes[^\n]*\n(.*?)(?=^## |\Z)", entry(rel), re.M | re.S)
    if not m:
        return []
    out = []
    for row in m.group(1).splitlines():
        if row.lstrip().startswith("|") and not SEPARATOR.match(row):
            out += TICK.findall(row.strip().strip("|").split("|")[0])
    return out


def routes() -> dict[str, list[tuple[str, str | None]]]:
    """route name -> [(node, required include or None)] in step order."""
    text = ROUTES.read_text(encoding="utf-8")
    out = {}
    for m in re.finditer(r"^## Route: ([a-z-]+)\s*$(.*?)(?=^## |\Z)", text, re.M | re.S):
        steps = []
        for row in m.group(2).splitlines():
            cells = [c.strip() for c in row.strip().strip("|").split("|")]
            if len(cells) >= 3 and cells[0].isdigit():
                node = TICK.findall(cells[1])[0]
                cond = re.fullmatch(r"includes ([a-z-]+)", cells[2])
                steps.append((node, cond.group(1) if cond else None))
        out[m.group(1)] = steps
    return out


def steps_of(task: Path) -> list[tuple[str, bool]]:
    inc = set(listed(field(task, "includes")))
    return [(n, cond is None or cond in inc) for n, cond in routes()[field(task, "route")]]


# ------------------------------------------------------------------ tasks
def all_tasks() -> list[tuple[Path, str | None]]:
    found = []
    for rel, d in nodes().items():
        work = d / "work"
        if work.is_dir():
            found += [(t, rel) for t in sorted(work.iterdir()) if t.is_dir() and t.name.startswith("T-")]
    if CLIENTS.is_dir():
        for c in sorted(CLIENTS.iterdir()):
            done = c / "done"
            if done.is_dir():
                found += [(t, None) for t in sorted(done.iterdir()) if t.is_dir() and t.name.startswith("T-")]
    return found


def find(tid: str) -> tuple[Path, str | None]:
    for t, n in all_tasks():
        if t.name == tid:
            return t, n
    print(f"no task {tid!r} (run: task.py status)")
    sys.exit(2)


def field(task: Path, key: str) -> str:
    m = re.search(rf"^\| {re.escape(key)} \| (.*?) \|$", (task / "TASK.md").read_text(encoding="utf-8"), re.M)
    return m.group(1).strip() if m else ""


def set_field(task: Path, key: str, value: str) -> None:
    p = task / "TASK.md"
    text = p.read_text(encoding="utf-8")
    new, n = re.subn(rf"^(\| {re.escape(key)} \| ).*?( \|)$", lambda m: m.group(1) + value + m.group(2), text, flags=re.M)
    if n != 1:
        print(f"{p}: field {key!r} not found exactly once")
        sys.exit(2)
    p.write_text(new, encoding="utf-8")


def listed(value: str) -> list[str]:
    return [c.strip() for c in value.split(",") if c.strip() and c.strip() != NONE]


def history(task: Path, event: str, where: str, note: str) -> None:
    p = task / "TASK.md"
    text = p.read_text(encoding="utf-8").rstrip("\n")
    p.write_text(text + f"\n| {today()} | {event} | {where} | {note} |\n", encoding="utf-8")


def today() -> str:
    return ARGS_DATE or datetime.date.today().isoformat()


def route_table(task: Path) -> None:
    """Rewrite the task's `## Route` section from ROUTES.md, `includes` and `node`."""
    here = field(task, "node")
    rows = ["## Route", "",
            f"Route `{field(task, 'route')}` from `00 - control/01 - law/ROUTES.md`. Written by the operator; `◀ here` marks the current node.", "",
            "| Step | Node | Folder in this task | Runs |", "|---|---|---|---|"]
    for i, (n, runs) in enumerate(steps_of(task), 1):
        mark = " ◀ here" if n == here else ""
        rows.append(f"| {i} | {n} | {folder_of(n)} | {'yes' if runs else 'no (not included)'}{mark} |")
    block = "\n".join(rows) + "\n\n"
    p = task / "TASK.md"
    text = p.read_text(encoding="utf-8")
    text = re.sub(r"^## Route\n.*?(?=^## Start here)", lambda m: block, text, flags=re.M | re.S)
    p.write_text(text, encoding="utf-8")


def engagement_row(path: Path, key: str) -> str | None:
    """A value from the client's engagement table (`| Type | retainer |`)."""
    if not path.is_file():
        return None
    m = re.search(rf"^\| {re.escape(key)} \| (.*?) \|$", path.read_text(encoding="utf-8"), re.M)
    return m.group(1).strip() if m else None


def check_task(task: Path, rel: str) -> list[str]:
    problems = []
    for item in writes(rel):
        path, _, heading = item.partition("#")
        f = task / path
        if not f.is_file():
            problems.append(f"missing `{path}`")
            continue
        text = f.read_text(encoding="utf-8")
        if heading and not re.search(rf"^## {re.escape(heading)}\s*$", text, re.M):
            problems.append(f"`{path}` has no section `## {heading}`")
        if f.name == "gate.md" and not re.search(r"^VERDICT:\s*PASS\b", text, re.M):
            problems.append(f"`{path}` does not say VERDICT: PASS")
    return problems


def gate_line(task: Path, rel: str, key: str) -> str | None:
    g = task / folder_of(rel) / "gate.md"
    if not g.is_file():
        return None
    m = re.search(rf"^{key}:\s*(.+?)\s*$", g.read_text(encoding="utf-8"), re.M)
    return m.group(1) if m else None


def supersede(task: Path, rel: str) -> None:
    """Rename a node's gate and CONTEXT section in the task, so its gate must pass again."""
    folder = task / folder_of(rel)
    g = folder / "gate.md"
    if g.is_file():
        n = 1
        while (folder / f"gate-superseded-{n}.md").exists():
            n += 1
        g.rename(folder / f"gate-superseded-{n}.md")
    ctx = task / "CONTEXT.md"
    text = ctx.read_text(encoding="utf-8")
    ctx.write_text(re.sub(rf"^## {re.escape(folder_of(rel))}\s*$", f"## {folder_of(rel)} (superseded {today()})", text, flags=re.M),
                   encoding="utf-8")


def move(task: Path, dest_dir: Path) -> Path:
    dest_dir.mkdir(parents=True, exist_ok=True)
    target = dest_dir / task.name
    if target.exists():
        print(f"refused: {target.relative_to(ROOT)} already exists")
        sys.exit(1)
    shutil.move(str(task), str(target))
    return target


def enter(task: Path, rel: str, status: str) -> None:
    set_field(task, "node", rel)
    set_field(task, "folder", folder_of(rel))
    set_field(task, "status", status)
    (task / folder_of(rel)).mkdir(exist_ok=True)
    route_table(task)


def file_done(task: Path, status: str, event: str, note: str) -> Path:
    client = field(task, "client")
    new = move(task, CLIENTS / client / "done")
    set_field(new, "node", "done")
    set_field(new, "folder", NONE)
    set_field(new, "status", status)
    set_field(new, "waiting on", NONE)
    route_table(new)
    history(new, event, "done", note)
    return new


# ------------------------------------------------------------------ templates
TASK_MD = """# TASK {id}

| Field | Value |
|---|---|
""" + "".join(f"| {k} | {{{k.replace(' ', '_')}}} |\n" for k in FIELDS) + """
The operator (`00 - control/02 - tools/task.py`) keeps the table above, the Route and the History. Gate stages decide; the operator moves. Law: `00 - control/01 - law/TASK_CONTRACT.md`.

## Route

## Start here (cold instance)

1. Read `CONTEXT.md` in this folder: what is known so far, compressed, with sources.
2. Read the client folder, `clients/<client>/` (the `client` field above), starting at its `00 - ENTRY.md`.
3. Open the current node's ENTRY at the company root: `<node>/00 - ENTRY.md`, where `<node>` is the `node` field above. Its files in this task go in the folder named in the `folder` field.
4. Run that node's stages in order, each from its own `00 - ENTRY.md`. If `status` is HOLD, the node is waiting on what `waiting on` names: do nothing until it has arrived and the task is resumed.

## History

| Date | Event | Where | Note |
|---|---|---|---|
"""

CONTEXT_MD = """# CONTEXT — {id}

Carry-forward. Each node appends one section, `## <its folder>` (e.g. `## 11-intake`), of at most 10 bullets: the load-bearing facts later nodes need. Each bullet ends with its source file in square brackets, e.g. [11-intake/01-parse.md]. Later nodes read this file first, and open an intermediary only when they need the detail. A section marked "(superseded …)" was replaced when the task was sent back; read the newer one.

Tags: [client] the client said it · [operator] the operator decided it · [src: L-nnn] a logged source · [assumed] we proceed on it until corrected · [ask: CQn] waiting on the client · [research: RQn] waiting on research.
"""

REQUEST_MD = """# Request — {id}

Captured by `task.py new` on {created}. Verbatim: nothing in the block below has been corrected, summarised or split.

- Arrived via: {arrived_via}
- From: {label} (client folder `clients/{client}/`)
- Kind: {kind}

## The request

```text
{text}
```

## Attachments

None.
"""

FROM_CLIENT = "The client's words, verbatim, as the operator relays them. Names follow `00 - control/01 - law/HANDOFFS.md` H1: `<node folder>-<name>-reply.md`.\n"
FROM_OPERATOR = "The operator's decisions and inputs. Names follow `00 - control/01 - law/HANDOFFS.md` H2: `<node folder>-<name>.md`.\n"


# ------------------------------------------------------------------ commands
def cmd_new(a) -> int:
    rs = routes()
    if a.route not in rs:
        return usage(f"--route: one of {', '.join(rs)}")
    if not SLUG.fullmatch(a.client):
        return usage("--client: the client folder slug, 1-5 lowercase words joined by hyphens")
    client_dir = CLIENTS / a.client
    date = today()
    if a.route == "month":
        if not (a.month and re.fullmatch(r"\d{4}-\d{2}", a.month)):
            return usage("--month YYYY-MM is required for a month task")
        eng = client_dir / "engagement.md"
        kind = engagement_row(eng, "Type")
        if kind != "retainer":
            return refuse(f"a month task needs a retainer: `clients/{a.client}/engagement.md` says Type = {kind or 'nothing'}")
        includes = ", ".join(listed(engagement_row(eng, "Includes") or "")) or NONE
        slug, text, label = f"{a.client}-{a.month}", None, a.label or a.client
    else:
        if not (a.slug and re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+){1,4}", a.slug)):
            return usage("--slug: 2-5 lowercase words joined by hyphens (the business, then the ask)")
        if not a.label:
            return usage("--label: the client as the request states them, e.g. \"gemstone seller\"")
        text = Path(a.file).read_text(encoding="utf-8") if a.file else a.text
        if not text or not text.strip():
            return usage("the request is empty (--text or --file)")
        slug, label, includes = a.slug, a.label, NONE
    tid = f"T-{date.replace('-', '')}-{slug}"
    if any(t.name == tid for t, _ in all_tasks()):
        return refuse(f"task {tid} already exists")
    if not client_dir.exists():
        shutil.copytree(TEMPLATE, client_dir)
        print(f"created client folder clients/{a.client}/ from the template")
    first = rs[a.route][0][0]
    task = node_dir(first) / "work" / tid
    task.mkdir(parents=True)
    (task / "from-client").mkdir()
    (task / "from-client" / "README.md").write_text(FROM_CLIENT, encoding="utf-8")
    (task / "from-operator").mkdir()
    (task / "from-operator" / "README.md").write_text(FROM_OPERATOR, encoding="utf-8")
    kw = dict(id=tid, kind=a.kind, client=a.client, route=a.route, includes=includes, created=date,
              arrived_via=a.via if a.route == "engagement" else f"opened for month {a.month}",
              node=first, folder=folder_of(first), status="IN-NODE", waiting_on=NONE)
    (task / "TASK.md").write_text(TASK_MD.format(**kw), encoding="utf-8")
    (task / "CONTEXT.md").write_text(CONTEXT_MD.format(**kw), encoding="utf-8")
    (task / folder_of(first)).mkdir()
    if text is not None:
        (task / folder_of(first) / "00-request.md").write_text(
            REQUEST_MD.format(text=text.rstrip("\n"), label=label, **kw), encoding="utf-8")
    route_table(task)
    history(task, "created", first, f"route {a.route}; " + (f"request captured verbatim via {a.via}" if text is not None else f"month {a.month}"))
    print(f"created {task.relative_to(ROOT)}")
    return 0


def cmd_status(a) -> int:
    rows = all_tasks()
    if not rows:
        print("no tasks")
        return 0
    print("| Task | Kind | Client | Route | Node | Status | Waiting on | Gate |")
    print("|---|---|---|---|---|---|---|---|")
    for t, n in rows:
        if n is None:
            gate = NONE
        else:
            p = check_task(t, n)
            gate = "ready to advance" if not p else f"{len(p)} open"
        print(f"| {t.name} | {field(t, 'kind')} | {field(t, 'client')} | {field(t, 'route')} | "
              f"{n or 'done'} | {field(t, 'status')} | {field(t, 'waiting on')} | {gate} |")
    return 0


def cmd_check(a) -> int:
    task, rel = find(a.task)
    if rel is None:
        print(f"{a.task} is {field(task, 'status')}")
        return 0
    problems = check_task(task, rel)
    for p in problems:
        print(f"- {p}")
    print(f"{a.task} at {rel}: " + ("READY to advance" if not problems else f"{len(problems)} item(s) open"))
    return 0 if not problems else 1


def cmd_advance(a) -> int:
    task, rel = find(a.task)
    if rel is None:
        return refuse(f"{a.task} is {field(task, 'status')}")
    if field(task, "status") == "HOLD":
        return refuse(f"{a.task} is on HOLD (waiting on: {field(task, 'waiting on')}); run `task.py resume` when it has arrived")
    order = [n for n, _ in steps_of(task)]
    i = order.index(rel)

    if a.to:
        if a.to not in order[:i]:
            return usage(f"--to must be an earlier node on this task's route: {', '.join(order[:i]) or 'none'}")
        if not a.reason:
            return refuse("moving backwards needs --reason")
        j = order.index(a.to)
        for n in order[j:i + 1]:
            if (task / folder_of(n)).is_dir():
                supersede(task, n)
        new = move(task, node_dir(a.to) / "work")
        enter(new, a.to, "RETURNED")
        history(new, "returned", a.to, f"from {rel}: {a.reason} (gates {folder_of(a.to)} to {folder_of(rel)} superseded)")
        print(f"{a.task}: {rel} -> {a.to} (RETURNED)")
        return 0

    problems = check_task(task, rel)
    if problems:
        print(f"refused: the {rel} gate is not met for {a.task}")
        for p in problems:
            print(f"- {p}")
        return 1
    waiting, includes = gate_line(task, rel, "Waiting on"), gate_line(task, rel, "Includes")
    if includes is not None:
        set_field(task, "includes", ", ".join(listed(includes)) or NONE)
    if waiting is not None:
        set_field(task, "waiting on", waiting)
    steps = steps_of(task)
    skipped, nxt = [], None
    for n, runs in steps[i + 1:]:
        if runs:
            nxt = n
            break
        skipped.append(n)
    if nxt is None:
        new = file_done(task, "DONE", "done", f"gate of {rel} passed; route complete")
        print(f"{a.task}: {rel} -> clients/{field(new, 'client')}/done/ (DONE)")
        return 0
    if not is_built(nxt):
        return refuse(f"the next node, {nxt}, is not built")
    new = move(task, node_dir(nxt) / "work")
    enter(new, nxt, "ARRIVED")
    note = f"gate of {rel} passed"
    if skipped:
        note += "; passed over (not included): " + ", ".join(skipped)
    history(new, "advanced", nxt, note)
    print(f"{a.task}: {rel} -> {nxt} (ARRIVED; waiting on: {field(new, 'waiting on')})")
    return 0


def cmd_hold(a) -> int:
    task, rel = find(a.task)
    if rel is None:
        return refuse(f"{a.task} is {field(task, 'status')}")
    set_field(task, "status", "HOLD")
    set_field(task, "waiting on", a.on)
    history(task, "hold", rel, a.on)
    print(f"{a.task} at {rel}: HOLD (waiting on: {a.on})")
    return 0


def cmd_resume(a) -> int:
    task, rel = find(a.task)
    if rel is None:
        return refuse(f"{a.task} is {field(task, 'status')}")
    if field(task, "status") != "HOLD":
        return refuse(f"{a.task} is not on HOLD")
    set_field(task, "status", "IN-NODE")
    set_field(task, "waiting on", NONE)
    history(task, "resumed", rel, a.note)
    print(f"{a.task} at {rel}: IN-NODE ({a.note})")
    return 0


def cmd_close(a) -> int:
    task, rel = find(a.task)
    if rel is None:
        return refuse(f"{a.task} is already {field(task, 'status')}")
    new = file_done(task, "CLOSED", "closed", f"at {rel}: {a.reason}")
    hist = CLIENTS / field(new, "client") / "history.md"
    if hist.is_file():
        with hist.open("a", encoding="utf-8") as f:
            f.write(f"| {new.name} | {field(new, 'route')} | {field(new, 'created')} | {today()} | — | — | CLOSED at {rel}: {a.reason} |\n")
    print(f"{a.task}: {rel} -> clients/{field(new, 'client')}/done/ (CLOSED)")
    return 0


ARGS_DATE = None


def main() -> int:
    global ARGS_DATE
    ap = argparse.ArgumentParser(prog="task.py", description=__doc__.split("\n")[0])
    ap.add_argument("--date", help="override today's date (YYYY-MM-DD)")
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("new")
    p.add_argument("--route", required=True); p.add_argument("--client", required=True)
    p.add_argument("--slug"); p.add_argument("--label"); p.add_argument("--month")
    g = p.add_mutually_exclusive_group(); g.add_argument("--text"); g.add_argument("--file")
    p.add_argument("--via", default="message"); p.add_argument("--kind", choices=["real", "rehearsal"], default="real")
    sub.add_parser("status")
    p = sub.add_parser("check"); p.add_argument("task")
    p = sub.add_parser("advance"); p.add_argument("task"); p.add_argument("--to"); p.add_argument("--reason")
    p = sub.add_parser("hold"); p.add_argument("task"); p.add_argument("--on", required=True)
    p = sub.add_parser("resume"); p.add_argument("task"); p.add_argument("--note", required=True)
    p = sub.add_parser("close"); p.add_argument("task"); p.add_argument("--reason", required=True)
    a = ap.parse_args()
    if a.date and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", a.date):
        return usage("--date: YYYY-MM-DD")
    ARGS_DATE = a.date
    return {"new": cmd_new, "status": cmd_status, "check": cmd_check, "advance": cmd_advance,
            "hold": cmd_hold, "resume": cmd_resume, "close": cmd_close}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
