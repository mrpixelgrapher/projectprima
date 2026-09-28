#!/usr/bin/env python3
"""derive_phase.py - re-derive the company phase from disk (anti-inflation law, handoff §3.1).

Operator for:
  - the Phase Map (handoff §3): derived phase = the first phase whose exit minimum fails;
  - the knowledge-work override (handoff §3): research-dependent outputs are invalid
    until a research-dossier contract, a compiler contract and a handoff contract exist;
  - commercial readiness: whether invoices can be issued (the billing profile).

Usage (run from the company root):
    python3 "00 - control/02 - tools/derive_phase.py"                   # report
    python3 "00 - control/02 - tools/derive_phase.py" --write-manifest  # also write the phase to manifest.json

Exit code: 0 = manifest agrees with (or is below) the derived phase; 3 = manifest OVERCLAIMS.

The gate table below maps each handoff §3 minimum onto this company as the operator
restructured it at the S003 design lock (three departments, routes, client folders,
ledgers; "map to pricing dept": the capability, proof, client and upgrade minimums are
read from the commercial and delivery ledgers). Changing a mapping is a governance
change: log it in `00 - control/03 - state/meta_workspace.md` §4.

Check kinds:
  exists       file or folder exists
  contains     file exists and contains the text
  built        every node on every route in ROUTES.md has an ENTRY that says Status: BUILT
  gated        every node on every route has a `## Writes` table that includes its gate.md
  real_rows    a ledger table has >= N data rows that are not marked `rehearsal`
  filled       a two-column table has no value cell equal to "—"
  done         >= N real (non-rehearsal) tasks are DONE in clients/*/done/ (optionally on a route)
  done_with    >= N real DONE tasks contain a file matching a glob
  unbuilt      no artifact in this company holds it yet (always FAIL, names the gap)
  exercised    needs judgment across the loop; never passes by script
"""
from __future__ import annotations

import datetime
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ROUTES = ROOT / "00 - control" / "01 - law" / "ROUTES.md"
CLIENTS = ROOT / "clients"
TICK = re.compile(r"`([^`\n]+)`")

PHASE_NAMES = {
    0: "UNINITIALIZED",
    1: "FOUNDATION ACTIVE",
    2: "CAPABILITY OS BUILDING",
    3: "ACQUISITION AND PROOF BUILDING",
    4: "DELIVERY AND QUALITY BUILDING",
    5: "CLIENT AND UPGRADE BUILDING",
    6: "GOVERNANCE INSTALLED",
    7: "GOVERNED LOOP EXERCISED",
    8: "LIVE GOVERNED OPERATION",
    9: "META PROMOTION ELIGIBLE",
}


# ---------------------------------------------------------------- check kinds
def exists(path): return ("exists", path)
def contains(path, text): return ("contains", path, text)
def built(): return ("built",)
def gated(): return ("gated",)
def real_rows(path, n=1): return ("real_rows", path, n)
def filled(path): return ("filled", path)
def done(n=1, route=None): return ("done", n, route)
def done_with(glob, n=1): return ("done_with", glob, n)
def unbuilt(what): return ("unbuilt", what)
def exercised(what): return ("exercised", what)


def table_rows(text: str) -> list[str]:
    """Data rows of every markdown table in text (header and separator excluded)."""
    out, lines = [], text.splitlines()
    i = 0
    while i < len(lines):
        if lines[i].lstrip().startswith("|") and i + 1 < len(lines) and re.match(r"^\s*\|[\s:|-]+\|\s*$", lines[i + 1]):
            i += 2
            while i < len(lines) and lines[i].lstrip().startswith("|"):
                out.append(lines[i])
                i += 1
        else:
            i += 1
    return out


def route_nodes() -> list[str]:
    nodes = []
    for row in ROUTES.read_text(encoding="utf-8").splitlines():
        cells = [c.strip() for c in row.strip().strip("|").split("|")]
        if len(cells) >= 3 and cells[0].isdigit():
            n = TICK.findall(cells[1])[0]
            if n not in nodes:
                nodes.append(n)
    return nodes


def task_field(task: Path, key: str) -> str:
    m = re.search(rf"^\| {re.escape(key)} \| (.*?) \|$", (task / "TASK.md").read_text(encoding="utf-8"), re.M)
    return m.group(1).strip() if m else ""


def real_done_tasks(route=None) -> list[Path]:
    out = []
    if CLIENTS.is_dir():
        for t in sorted(CLIENTS.glob("*/done/T-*")):
            if (t / "TASK.md").is_file() and task_field(t, "kind") == "real" and task_field(t, "status") == "DONE":
                if route is None or task_field(t, "route") == route:
                    out.append(t)
    return out


def run(check) -> tuple[bool, str]:
    kind = check[0]
    if kind == "exercised":
        return False, "NOT-MACHINE-CHECKED: needs a judgment across an exercised loop"
    if kind == "unbuilt":
        return False, f"NOT BUILT: {check[1]}"
    if kind == "built":
        bad = [n for n in route_nodes() if not re.search(r"^Status:\s*BUILT", (ROOT / n / "00 - ENTRY.md").read_text(encoding="utf-8"), re.M)
               if (ROOT / n / "00 - ENTRY.md").is_file()] + [n for n in route_nodes() if not (ROOT / n / "00 - ENTRY.md").is_file()]
        return not bad, "" if not bad else "not built: " + ", ".join(bad)
    if kind == "gated":
        bad = []
        for n in route_nodes():
            text = (ROOT / n / "00 - ENTRY.md").read_text(encoding="utf-8") if (ROOT / n / "00 - ENTRY.md").is_file() else ""
            m = re.search(r"^## Writes[^\n]*\n(.*?)(?=^## |\Z)", text, re.M | re.S)
            if not (m and "gate.md`" in m.group(1)):
                bad.append(n)
        return not bad, "" if not bad else "no gate in Writes: " + ", ".join(bad)
    if kind == "done":
        found = real_done_tasks(check[2])
        ok = len(found) >= check[1]
        what = f" on route {check[2]}" if check[2] else ""
        return ok, "" if ok else f"{len(found)} of >= {check[1]} real DONE task(s){what} in `clients/*/done/`"
    if kind == "done_with":
        found = [t for t in real_done_tasks() if any(t.glob(check[1]))]
        ok = len(found) >= check[2]
        return ok, "" if ok else f"{len(found)} of >= {check[2]} real DONE task(s) holding `{check[1]}`"
    p = ROOT / check[1]
    if kind == "exists":
        return p.exists(), "" if p.exists() else f"missing `{check[1]}`"
    if not p.exists():
        return False, f"missing `{check[1]}`"
    text = p.read_text(encoding="utf-8")
    if kind == "contains":
        ok = check[2] in text
        return ok, "" if ok else f"`{check[1]}` lacks `{check[2]}`"
    if kind == "real_rows":
        data = [r for r in table_rows(text) if "rehearsal" not in r]
        ok = len(data) >= check[2]
        return ok, "" if ok else f"`{check[1]}` has {len(data)} of >= {check[2]} real row(s)"
    if kind == "filled":
        empty = [r.split("|")[1].strip() for r in table_rows(text) if len(r.split("|")) > 2 and r.split("|")[2].strip() == "—"]
        return not empty, "" if not empty else f"`{check[1]}` empty: " + ", ".join(empty)
    raise ValueError(kind)


# ------------------------------------------------------------ the gate table
C = "01 - commercial"
K = "02 - content"
# EXIT[n] = minimum artifacts to leave phase n (i.e. to hold phase n+1). Handoff §3 names in the labels.
EXIT = {
    0: [
        ("company manifest", exists("manifest.json")),
        ("service thesis", contains("00 - ENTRY.md", "## What this company does")),
        ("buyer map", contains("00 - ENTRY.md", "## Who sends requests")),
        ("initial system rules", contains("00 - ENTRY.md", "## Rules of the line")),
    ],
    1: [
        ("foundation: task contract", exists("00 - control/01 - law/TASK_CONTRACT.md")),
        ("foundation: routes", exists("00 - control/01 - law/ROUTES.md")),
        ("foundation: brief slots", exists("00 - control/01 - law/BRIEF_SLOTS.md")),
        ("foundation: every node on every route BUILT", built()),
        ("source packets: intake names every missing input (client questions)", exists(f"{C}/01 - intake/04 - questions/00 - ENTRY.md")),
        ("source packets: research is staged as an ARENA request", exists(f"{K}/01 - discovery/01 - requests/00 - ENTRY.md")),
        ("source packets: hand-off law (client, operator, ARENA, image factory, motion)", exists("00 - control/01 - law/HANDOFFS.md")),
        ("source packets: input registry (>= 1 row)", real_rows("00 - control/05 - registers/input_registry.md", 1)),
    ],
    2: [
        ("capability cards: every node declares its outputs and its gate", gated()),
        ("promotion gates: proposal sign-off and acceptance", exists(f"{C}/04 - proposal/05 - gate/00 - ENTRY.md")),
        ("validation-run template: the delivery record", exists(f"{K}/08 - delivery/02 - record/00 - ENTRY.md")),
        ("capability ledger: delivery ledger (>= 1 real row)", real_rows(f"{K}/08 - delivery/ledgers/delivery-ledger.md", 1)),
    ],
    3: [
        ("pipeline ledger: proposals (>= 1 real row)", real_rows(f"{C}/ledgers/proposals.md", 1)),
        ("cognitive sequence rules: routes", exists("00 - control/01 - law/ROUTES.md")),
        ("proof system: client results (>= 1 real month)", done_with("15-month-review/02-review.md", 1)),
        ("authority claims", unbuilt("no file states the company's own public claims and their evidence")),
        ("public-proof rules", unbuilt("no rule for when a client result may be shown publicly")),
        ("compiler contract: research compiled into a spine", exists(f"{K}/05 - writing/01 - research/03 - spine/00 - ENTRY.md")),
    ],
    4: [
        ("intake form", exists(f"{C}/01 - intake/00 - ENTRY.md")),
        ("work packet: the piece brief", exists(f"{K}/04 - planning/03 - briefs/piece-brief-template.md")),
        ("delivery packet: the client package", exists(f"{K}/06 - packaging/03 - package/00 - ENTRY.md")),
        ("service ledger: delivery ledger", exists(f"{K}/08 - delivery/ledgers/delivery-ledger.md")),
        ("quality thresholds: the review gate prompt", exists(f"{K}/05 - writing/04 - review/gate-prompt.md")),
        ("QA checklist: the human check", exists(f"{K}/05 - writing/09 - human-check/human-check.md")),
        ("review report (>= 1 completed, in a real task)", done_with("25-writing/*/07-review.md", 1)),
    ],
    5: [
        ("client ledger (>= 1 real row)", real_rows(f"{C}/ledgers/clients.md", 1)),
        ("client template", exists("clients/00 - template/00 - ENTRY.md")),
        ("upgrade rules with thresholds: upsell triggers", contains(f"{C}/05 - month-review/03 - upsell/00 - ENTRY.md", "Trigger")),
        ("rollback rules", unbuilt("no rule for pausing or reducing an engagement")),
        ("upgrade brief template: the upsell offer", exists(f"{C}/05 - month-review/03 - upsell/00 - ENTRY.md")),
    ],
    6: [
        ("lessons", exists(f"{K}/08 - delivery/ledgers/lessons-log.md")),
        ("patterns-to-promote: the promotion rule", contains(f"{K}/08 - delivery/04 - lessons/00 - ENTRY.md", "Promotion rule")),
        ("drift checks", unbuilt("no check compares what the company says, sells and has delivered")),
        ("readiness dashboard", unbuilt("`task.py status` shows tasks, not readiness")),
        ("phase map", exists("00 - control/03 - state/PHASE_DERIVATION.md")),
        ("exercised matter: a real task DONE", done(1)),
        ("exercised quality/proof disposition: a real task DONE with a review PASS", done_with("25-writing/*/07-review.md", 1)),
    ],
    7: [
        ("matter moved through delivery and quality disposition", done_with("28-delivery/02-record.md", 1)),
        ("client transition backed by a named artifact: client ledger", real_rows(f"{C}/ledgers/clients.md", 1)),
        ("governance refresh after the loop", exercised("refresh")),
    ],
    8: [
        ("repeated proof: >= 2 real tasks DONE", done(2)),
        ("an exercised loop for every route: engagement", done(1, "engagement")),
        ("an exercised loop for every route: month", done(1, "month")),
        ("readiness dashboard with no open overclaim", exercised("dashboard")),
    ],
}

OVERRIDE = [
    ("research-dossier contract (the ARENA request and dossier)", contains("00 - control/01 - law/HANDOFFS.md", "## The ARENA request format")),
    ("compiler contract (the spine)", exists(f"{K}/05 - writing/01 - research/03 - spine/00 - ENTRY.md")),
    ("handoff contract (task contract and hand-offs)", contains("00 - control/01 - law/TASK_CONTRACT.md", "## 6. The client folder")),
]
RESEARCH_DEPENDENT = "every piece written at `02 - content/05 - writing/` and every market claim in a brief"


def main() -> int:
    derived, report = None, []
    for n in range(0, 9):
        results = [(label, *run(c)) for label, c in EXIT[n]]
        passed = all(ok for _, ok, _ in results)
        report.append((n, passed, results))
        if not passed and derived is None:
            derived = n
    if derived is None:
        derived = 9

    manifest_path = ROOT / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    claimed = manifest.get("phase")

    print(f"# Phase derivation - {datetime.date.today().isoformat()}")
    print(f"\nDerived phase: **{derived} - {PHASE_NAMES[derived]}**")
    print(f"Manifest claim: {claimed} - {manifest.get('phase_label')}")
    overclaim = isinstance(claimed, int) and claimed > derived
    if overclaim:
        print(f"MANIFEST OVERCLAIMS by {claimed - derived} phase(s): downgrade to {derived} (run with --write-manifest).")

    print("\n## Exit minimum per phase (first FAIL = derived phase)\n")
    print("| Phase | Exit minimum | Result | Missing |")
    print("|---|---|---|---|")
    for n, passed, results in report:
        for label, ok, why in results:
            print(f"| {n} {PHASE_NAMES[n]} | {label} | {'PASS' if ok else 'FAIL'} | {why} |")

    ov = [(label, *run(c)) for label, c in OVERRIDE]
    ov_ok = all(ok for _, ok, _ in ov)
    print("\n## Knowledge-work override\n")
    for label, ok, why in ov:
        print(f"- {label}: {'PASS' if ok else 'FAIL ' + why}")
    print(f"\nOverride: {'SATISFIED' if ov_ok else 'NOT SATISFIED - INVALID until satisfied: ' + RESEARCH_DEPENDENT}")

    bp_ok, bp_why = run(filled(f"{C}/billing-profile.md"))
    print("\n## Commercial readiness\n")
    print(f"- billing profile filled: {'PASS' if bp_ok else 'FAIL - ' + bp_why}")
    print(f"\nInvoices: {'can be issued' if bp_ok else 'HOLD at billing until the operator fills `01 - commercial/billing-profile.md`'}")

    if "--write-manifest" in sys.argv:
        manifest["phase"] = derived
        manifest["phase_label"] = PHASE_NAMES[derived]
        manifest["phase_derived_on"] = datetime.date.today().isoformat()
        manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"\nmanifest.json written: phase={derived} ({PHASE_NAMES[derived]})")
        return 0
    return 3 if overclaim else 0


if __name__ == "__main__":
    sys.exit(main())
