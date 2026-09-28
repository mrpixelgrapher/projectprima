#!/usr/bin/env python3
"""task.py - stage, check, float, branch and join client tasks through the nodes.

A task is a folder. Where it sits is its state: every task lives in exactly one
node's `work/` folder, or in `10 - delivery/done/`. Moving the folder is how it floats.
Contract: `00 - control/01 - law/TASK_CONTRACT.md`.

Usage (run from the company root):
  task.py new --slug SLUG --client LABEL (--text TEXT | --file PATH)
              [--via CHANNEL] [--kind real|rehearsal]
  task.py status
  task.py check TASK
  task.py advance TASK
  task.py advance TASK --to "NN - node" --reason TEXT
  task.py branch TASK --start "NN - node" --join "NN - node" --children SLUG [SLUG ...]
  task.py join TASK [--absorb]
  (global: --date YYYY-MM-DD overrides today's date, for tests and back-dating)

Nodes are the root folders named `NN - name` with NN from 01 to 89 (`00 - control`
and `99 - archive` are not nodes). A node's ENTRY declares what the tool enforces:
  `Status: BUILT`        a task may enter and leave it;
  `## Writes` table      the files a task must hold before it leaves (first column,
                         backticked; `file#Heading` also needs that `## Heading`;
                         every `gate.md` must say VERDICT: PASS);
  `**Branch node:**`     a task leaves only by `branch`, never by `advance`;
  `**Join node:**`       a parent may wait here for its children.

Rules enforced:
  - forward only through a passed gate; into built nodes only;
  - backward only with --reason, written to History;
  - `branch` needs the branch node's gate passed and one brief per child at
    `<NN-node>/briefs/<slug>.md`; it starts the children and parks the parent at the
    join node (WAITING-CHILDREN);
  - a waiting parent cannot advance; a child cannot leave its parent's join node:
    `join --absorb` moves it inside the parent at `<NN-node>/pieces/<child-id>/`;
  - on a forward move, the `Waiting on:` line of the gate just passed is copied to
    the task's `waiting on` field.
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
NODE_NAME = re.compile(r"^(\d{2}) - [a-z-]+$")
TICK = re.compile(r"`([^`\n]+)`")
SEPARATOR = re.compile(r"^\s*\|[\s:|-]+\|\s*$")
NONE = "—"


def refuse(msg: str) -> int:
    print(f"refused: {msg}")
    return 1


# ------------------------------------------------------------------ nodes
def nodes() -> list[Path]:
    out = []
    for d in ROOT.iterdir():
        m = NODE_NAME.match(d.name)
        if d.is_dir() and m and 1 <= int(m.group(1)) <= 89:
            out.append(d)
    return sorted(out, key=lambda d: d.name)


def done_dir() -> Path:
    return nodes()[-1] / "done"


def node_by_name(name: str) -> Path:
    for n in nodes():
        if n.name == name:
            return n
    print(f"no node named {name!r}; nodes are: {', '.join(n.name for n in nodes())}")
    sys.exit(2)


def entry(node: Path) -> str:
    return (node / "00 - ENTRY.md").read_text(encoding="utf-8")


def is_built(node: Path) -> bool:
    m = re.search(r"^Status:\s*\**\s*(NOT BUILT|BUILT)", entry(node), re.M)
    return bool(m) and m.group(1) == "BUILT"


def is_branch_node(node: Path) -> bool:
    return "**Branch node:**" in entry(node)


def is_join_node(node: Path) -> bool:
    return "**Join node:**" in entry(node)


def subfolder(node: Path) -> str:
    """'01 - intake' -> '01-intake' (the node's subfolder inside a task)."""
    return node.name.replace(" - ", "-")


def writes(node: Path) -> list[str]:
    m = re.search(r"^## Writes[^\n]*\n(.*?)(?=^## |\Z)", entry(node), re.M | re.S)
    if not m:
        return []
    out = []
    for row in m.group(1).splitlines():
        if row.lstrip().startswith("|") and not SEPARATOR.match(row):
            first = row.strip().strip("|").split("|")[0]
            out += TICK.findall(first)
    return out


# ------------------------------------------------------------------ tasks
def all_tasks() -> list[tuple[Path, Path | None]]:
    found = []
    for n in nodes():
        work = n / "work"
        if work.is_dir():
            found += [(t, n) for t in sorted(work.iterdir()) if t.is_dir() and t.name.startswith("T-")]
    done = done_dir()
    if done.is_dir():
        found += [(t, None) for t in sorted(done.iterdir()) if t.is_dir() and t.name.startswith("T-")]
    return found


def find(tid: str) -> tuple[Path, Path | None]:
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


def history(task: Path, event: str, node: str, note: str) -> None:
    p = task / "TASK.md"
    text = p.read_text(encoding="utf-8").rstrip("\n")
    p.write_text(text + f"\n| {today()} | {event} | {node} | {note} |\n", encoding="utf-8")


def listed(value: str) -> list[str]:
    return [c.strip() for c in value.split(",") if c.strip() and c.strip() != NONE]


def today() -> str:
    return ARGS_DATE or datetime.date.today().isoformat()


def check_task(task: Path, node: Path) -> list[str]:
    problems = []
    for rel in writes(node):
        path, _, heading = rel.partition("#")
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


def gate_waiting(task: Path, node: Path) -> str | None:
    g = task / subfolder(node) / "gate.md"
    if not g.is_file():
        return None
    m = re.search(r"^Waiting on:\s*(.+?)\s*$", g.read_text(encoding="utf-8"), re.M)
    return m.group(1) if m else None


def start_of(task: Path) -> str | None:
    """A child's start node, recorded in `arrived via` at branch time."""
    m = re.search(r"starts at (\d{2} - [a-z-]+)", field(task, "arrived via"))
    return m.group(1) if m else None


def move(task: Path, dest_dir: Path) -> Path:
    dest_dir.mkdir(parents=True, exist_ok=True)
    target = dest_dir / task.name
    if target.exists():
        print(f"refused: {target.relative_to(ROOT)} already exists")
        sys.exit(1)
    shutil.move(str(task), str(target))
    return target


# ------------------------------------------------------------------ templates
TASK_MD = """# TASK {tid}

| Field | Value |
|---|---|
| id | {tid} |
| kind | {kind} |
| client | {client} |
| created | {date} |
| arrived via | {via} |
| node | {node} |
| status | IN-NODE |
| waiting on | — |
| parent | {parent} |
| children | — |

A task is a folder that floats through the nodes, and where it sits is its state. The operator (`00 - control/02 - tools/task.py`) keeps the table above and the History; gate stages set `status` to HOLD and set `waiting on`. See `00 - control/01 - law/TASK_CONTRACT.md`.

## Start here (cold instance)

1. Read `CONTEXT.md` in this folder: what is known so far, compressed, with sources.{brief_line}
2. Open the current node's ENTRY, at the company root: `<node>/00 - ENTRY.md`, where `<node>` is the `node` field above.
3. Run that node's stages in order, each from its own `00 - ENTRY.md`, writing only inside this folder.

## History

| Date | Event | Node | Note |
|---|---|---|---|
"""

BRIEF_LINE = "\n   This is a child task: `00-brief.md` is your assignment; it outranks the parent's CONTEXT.md where they differ."

CONTEXT_MD = """# CONTEXT — {tid}

Carry-forward. Each node appends one section, `## <node>`, of at most 10 bullets: the load-bearing facts later nodes need. Each bullet ends with its source file in square brackets, e.g. [01-intake/01-parse.md]. Later nodes read this file first, and open an intermediary only when they need the detail.

Tags: [client] the client said it · [src: L-nnn] a logged source · [assumed] we proceed on it until corrected · [ask: CQn] waiting on the client · [research: RQn] waiting on research.
"""

REQUEST_MD = """# Request — {tid}

Captured by `task.py new` on {date}. Verbatim: nothing in the block below has been corrected, summarised or split.

- Arrived via: {via}
- From: {client}
- Kind: {kind}

## The request

```text
{text}
```

## Attachments

None.
"""


def write_task(folder: Path, **kw) -> None:
    folder.mkdir(parents=True)
    (folder / "client").mkdir()
    kw.setdefault("brief_line", "")
    (folder / "TASK.md").write_text(TASK_MD.format(**kw), encoding="utf-8")
    (folder / "client" / "README.md").write_text(
        "Everything from the client goes here, verbatim: answers (`answers-round-1.md` …), approvals, receipts and attachments.\n",
        encoding="utf-8")


# ------------------------------------------------------------------ commands
def cmd_new(a) -> int:
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+){1,4}", a.slug):
        print("slug: 2-5 lowercase words joined by hyphens")
        return 2
    text = Path(a.file).read_text(encoding="utf-8") if a.file else a.text
    if not text or not text.strip():
        print("the request is empty")
        return 2
    first = nodes()[0]
    date = today()
    tid = f"T-{date.replace('-', '')}-{a.slug}"
    if any(t.name == tid for t, _ in all_tasks()):
        return refuse(f"task {tid} already exists")
    task = first / "work" / tid
    kw = dict(tid=tid, kind=a.kind, client=a.client, date=date, via=a.via, node=first.name, parent=NONE)
    write_task(task, **kw)
    (task / "CONTEXT.md").write_text(CONTEXT_MD.format(**kw), encoding="utf-8")
    (task / subfolder(first)).mkdir()
    (task / subfolder(first) / "00-request.md").write_text(REQUEST_MD.format(text=text.rstrip("\n"), **kw), encoding="utf-8")
    history(task, "created", first.name, f"request captured verbatim via {a.via}")
    print(f"created {task.relative_to(ROOT)}")
    return 0


def cmd_status(a) -> int:
    rows = all_tasks()
    if not rows:
        print("no tasks")
        return 0
    print("| Task | Kind | Node | Status | Waiting on | Gate | Parent | Children |")
    print("|---|---|---|---|---|---|---|---|")
    for t, n in rows:
        if n is None:
            gate = NONE
        elif field(t, "status") == "WAITING-CHILDREN":
            kids = listed(field(t, "children"))
            here = sum(1 for c in kids if find(c)[1] == n)
            gate = f"join: {here}/{len(kids)} children arrived"
        elif field(t, "parent") not in ("", NONE) and find(field(t, "parent"))[1] == n:
            gate = "at the join; the parent absorbs it"
        else:
            p = check_task(t, n)
            gate = "ready to advance" if not p else f"{len(p)} open"
        print(f"| {t.name} | {field(t, 'kind')} | {n.name if n else 'done'} | {field(t, 'status')} | "
              f"{field(t, 'waiting on')} | {gate} | {field(t, 'parent')} | {field(t, 'children')} |")
    return 0


def cmd_check(a) -> int:
    task, node = find(a.task)
    if node is None:
        print(f"{a.task} is done")
        return 0
    problems = check_task(task, node)
    for p in problems:
        print(f"- {p}")
    print(f"{a.task} at {node.name}: " + ("READY to advance" if not problems else f"{len(problems)} item(s) open"))
    return 0 if not problems else 1


def cmd_advance(a) -> int:
    task, node = find(a.task)
    if node is None:
        return refuse(f"{a.task} is already done")
    order = nodes()
    status = field(task, "status")
    if status == "WAITING-CHILDREN":
        return refuse(f"{a.task} is waiting for its children at {node.name}; run `task.py join {a.task}`")
    parent = field(task, "parent")
    if parent not in ("", NONE):
        p_task, p_node = find(parent)
        if p_node == node:
            return refuse(f"{a.task} has reached its parent's join node; it leaves only by `task.py join {parent} --absorb`")

    if a.to:
        target = node_by_name(a.to)
        if order.index(target) >= order.index(node):
            print("--to is for moving backwards; forward moves use plain advance (the gate must pass)")
            return 2
        if not a.reason:
            return refuse("moving backwards needs --reason")
        start = start_of(task)
        if start and order.index(target) < order.index(node_by_name(start)):
            return refuse(f"{a.task} is a child that starts at {start}; it cannot go back before it")
        new = move(task, target / "work")
        set_field(new, "node", target.name)
        set_field(new, "status", "RETURNED")
        history(new, "returned", target.name, f"from {node.name}: {a.reason}")
        print(f"{a.task}: {node.name} -> {target.name} (RETURNED)")
        return 0

    if is_branch_node(node):
        return refuse(f"{node.name} is a branch node: a task leaves it by `task.py branch`, not `advance` (see its ENTRY)")
    problems = check_task(task, node)
    if problems:
        print(f"refused: the {node.name} gate is not met for {a.task}")
        for p in problems:
            print(f"- {p}")
        return 1
    waiting = gate_waiting(task, node)
    i = order.index(node)
    if i + 1 == len(order):
        new = move(task, done_dir())
        set_field(new, "node", "done")
        set_field(new, "status", "DONE")
        set_field(new, "waiting on", NONE)
        history(new, "done", "done", f"gate of {node.name} passed; filed in {done_dir().relative_to(ROOT)}")
        print(f"{a.task}: {node.name} -> {done_dir().relative_to(ROOT)} (DONE)")
        return 0
    nxt = order[i + 1]
    if not is_built(nxt):
        return refuse(f"the next node, {nxt.name}, is not built")
    new = move(task, nxt / "work")
    set_field(new, "node", nxt.name)
    set_field(new, "status", "ARRIVED")
    note = f"gate of {node.name} passed"
    if parent not in ("", NONE) and find(parent)[1] == nxt:
        waiting = f"join by parent {parent}"
        note += "; reached the parent's join node"
    if waiting is not None:
        set_field(new, "waiting on", waiting)
    history(new, "advanced", nxt.name, note)
    print(f"{a.task}: {node.name} -> {nxt.name} (ARRIVED; waiting on: {field(new, 'waiting on')})")
    return 0


def cmd_branch(a) -> int:
    parent, node = find(a.task)
    if node is None:
        return refuse("cannot branch a done task")
    if not is_branch_node(node):
        return refuse(f"{node.name} is not a branch node (its ENTRY has no `**Branch node:**` line)")
    order = nodes()
    start, join = node_by_name(a.start), node_by_name(a.join)
    if not (order.index(node) < order.index(start) < order.index(join)):
        print("--start must come after the branch node, and --join after --start")
        return 2
    if not is_join_node(join):
        return refuse(f"{join.name} is not a join node (its ENTRY has no `**Join node:**` line)")
    if not all(is_built(n) for n in (start, join)):
        return refuse("the start and join nodes must both be built")
    problems = check_task(parent, node)
    if problems:
        print(f"refused: the {node.name} gate is not met for {a.task}")
        for p in problems:
            print(f"- {p}")
        return 1
    if len(set(a.children)) != len(a.children):
        print("--children lists a slug twice")
        return 2
    bad = [s for s in a.children if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+){0,4}", s)]
    if bad:
        print("child slugs: 1-5 lowercase words joined by hyphens: " + ", ".join(bad))
        return 2
    briefs = parent / subfolder(node) / "briefs"
    missing = [s for s in a.children if not (briefs / f"{s}.md").is_file()]
    if missing:
        return refuse("the branch node must write a brief per child first: " +
                      ", ".join(f"`{subfolder(node)}/briefs/{s}.md`" for s in missing))
    existing = {t.name for t, _ in all_tasks()}
    ids = [f"{parent.name}.{s}" for s in a.children]
    clash = [c for c in ids if c in existing]
    if clash:
        return refuse("child task(s) already exist: " + ", ".join(clash))

    for slug, cid in zip(a.children, ids):
        child = start / "work" / cid
        write_task(child, tid=cid, kind=field(parent, "kind"), client=field(parent, "client"), date=today(),
                   via=f"branch of {parent.name}, starts at {start.name}", node=start.name, parent=parent.name,
                   brief_line=BRIEF_LINE)
        shutil.copy(parent / "CONTEXT.md", child / "CONTEXT.md")
        shutil.copy(briefs / f"{slug}.md", child / "00-brief.md")
        history(child, "branched", start.name, f"from {parent.name} at {node.name}; brief copied to 00-brief.md")
    old = listed(field(parent, "children"))
    set_field(parent, "children", ", ".join(old + ids))
    history(parent, "branched", node.name, f"{len(ids)} child task(s) started at {start.name}")
    new = move(parent, join / "work")
    set_field(new, "node", join.name)
    set_field(new, "status", "WAITING-CHILDREN")
    set_field(new, "waiting on", "children: " + ", ".join(a.children))
    history(new, "parked", join.name, f"waits here until every child arrives; then `task.py join {parent.name} --absorb`")
    for cid in ids:
        print(f"created {cid} at {start.name}")
    print(f"{parent.name}: {node.name} -> {join.name} (WAITING-CHILDREN)")
    return 0


def cmd_join(a) -> int:
    parent, node = find(a.task)
    if node is None:
        return refuse(f"{a.task} is done")
    kids = listed(field(parent, "children"))
    if not kids:
        return refuse(f"{a.task} has no children")
    if field(parent, "status") != "WAITING-CHILDREN":
        return refuse(f"{a.task} is not waiting for children (status {field(parent, 'status')}); nothing to join")
    ready, located = True, []
    for cid in kids:
        c_task, c_node = find(cid)
        here = c_node == node
        ready &= here
        located.append(c_task)
        print(f"- {cid}: " + ("arrived" if here else f"at {c_node.name if c_node else 'done'} ({field(c_task, 'status')})"))
    print(f"join at {node.name}: " + ("READY: every child has arrived" if ready else "NOT READY"))
    if not ready:
        return 1
    if not a.absorb:
        return 0
    pieces = parent / subfolder(node) / "pieces"
    for c_task in located:
        set_field(c_task, "status", "JOINED")
        set_field(c_task, "waiting on", NONE)
        history(c_task, "joined", node.name, f"absorbed into {parent.name} at {subfolder(node)}/pieces/")
        move(c_task, pieces)
    set_field(parent, "status", "IN-NODE")
    set_field(parent, "waiting on", NONE)
    history(parent, "joined", node.name, f"{len(located)} child task(s) absorbed into {subfolder(node)}/pieces/")
    print(f"absorbed {len(located)} child task(s) into {parent.relative_to(ROOT)}/{subfolder(node)}/pieces/")
    return 0


ARGS_DATE = None


def main() -> int:
    global ARGS_DATE
    ap = argparse.ArgumentParser(prog="task.py", description=__doc__.split("\n")[0])
    ap.add_argument("--date", help="override today's date (YYYY-MM-DD)")
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("new"); p.add_argument("--slug", required=True); p.add_argument("--client", required=True)
    g = p.add_mutually_exclusive_group(required=True); g.add_argument("--text"); g.add_argument("--file")
    p.add_argument("--via", default="message"); p.add_argument("--kind", choices=["real", "rehearsal"], default="real")
    sub.add_parser("status")
    p = sub.add_parser("check"); p.add_argument("task")
    p = sub.add_parser("advance"); p.add_argument("task"); p.add_argument("--to"); p.add_argument("--reason")
    p = sub.add_parser("branch"); p.add_argument("task"); p.add_argument("--start", required=True)
    p.add_argument("--join", required=True); p.add_argument("--children", nargs="+", required=True)
    p = sub.add_parser("join"); p.add_argument("task"); p.add_argument("--absorb", action="store_true")
    a = ap.parse_args()
    if a.date and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", a.date):
        print("--date: YYYY-MM-DD")
        return 2
    ARGS_DATE = a.date
    return {"new": cmd_new, "status": cmd_status, "check": cmd_check, "advance": cmd_advance,
            "branch": cmd_branch, "join": cmd_join}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
