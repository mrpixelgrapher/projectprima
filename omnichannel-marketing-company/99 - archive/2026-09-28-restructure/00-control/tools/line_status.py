#!/usr/bin/env python3
"""line_status.py - where the assembly line stands, and whether anything skipped ahead.

Operator for the line law in `00-control/ASSEMBLY_LINE.md` (input I-007):
  1. company stations: none is FILLED while an earlier one is EMPTY or PARTIAL (PARTIAL
     company stations are allowed - they hold the operator's rulings plus named gaps);
     units of work: no station holds ANY output while an earlier station is not FILLED;
  2. no unit of work (content piece or client unit) exists while S0-S2 are not all FILLED;
  3. waiting is explicit: [CARBON-BLOCKED ...], [WAITING ...], [dossier: ..., PENDING];
  4. a deliberate deferral [DEFERRED: until <event>, per I-nnn|L-nnn] is listed, not blocking.
     A DEFERRED marker that cites no rule counts as waiting.

Usage (run from anywhere):
    python3 ".../00-control/tools/line_status.py"

Exit code: 0 = no skip-ahead violation; 1 = at least one violation.

The station table is read from ASSEMBLY_LINE.md, not duplicated here. How each
written path is judged (FILLED / PARTIAL / EMPTY) is documented in that file.
"""
from __future__ import annotations

import datetime
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from derive_phase import ROOT, table_rows  # noqa: E402

LINE = ROOT / "00-control" / "ASSEMBLY_LINE.md"
PIECES = ROOT / "01 - writing-department" / "03 - research"
CLIENT_UNITS = ROOT / "09 - delivery"
TICK = re.compile(r"`([^`\n]+)`")
WAIT = re.compile(r"\[(?:CARBON-BLOCKED|WAITING)[^\]]*\]|\[dossier:[^\]]*PENDING\]")
DEFER = re.compile(r"\[DEFERRED:[^\]]*\]")
CITED = re.compile(r"per [IL]-\d{3}")
RANK = {"EMPTY": 0, "PARTIAL": 1, "FILLED": 2}
DEFERRALS: list[str] = []


def load_stations() -> list[dict]:
    stations = []
    for row in table_rows(LINE.read_text(encoding="utf-8")):
        cells = [c.strip() for c in row.strip().strip("|").split("|")]
        if len(cells) < 6 or not re.fullmatch(r"S\d[a-z]?|M", cells[0]):
            continue
        stations.append({"id": cells[0], "name": cells[1], "unit": cells[3], "paths": TICK.findall(cells[4])})
    return stations


def judge(rel: str) -> tuple[str, list[str]]:
    p = ROOT / rel
    if rel.endswith("/"):
        ok = p.is_dir() and any(f.is_file() for f in p.rglob("*"))
        return ("FILLED" if ok else "EMPTY"), []
    if not p.is_file():
        return "EMPTY", []
    text = p.read_text(encoding="utf-8")
    if rel.startswith("01-foundation/"):
        m = re.search(r"^## Claims\s*$(.*?)(?=^## |\Z)", text, re.M | re.S)
        bullets = [ln for ln in (m.group(1).splitlines() if m else []) if re.match(r"^\s*([-*]|\d+\.)\s+\S", ln)]
        if not bullets:
            return "EMPTY", []
        waits = [w for b in bullets for w in WAIT.findall(b)]
        defers = [d for b in bullets for d in DEFER.findall(b)]
        waits += [d for d in defers if not CITED.search(d)]
        DEFERRALS.extend(f"{rel}: {d}" for d in defers if CITED.search(d))
        return ("PARTIAL" if waits else "FILLED"), waits
    if p.name == "GATE.md":
        return ("FILLED" if "VERDICT: PASS" in text else "PARTIAL"), ([] if "VERDICT: PASS" in text else ["[WAITING: gate verdict PASS]"])
    return "FILLED", []


def station_status(st: dict, root: str = "", slug: str = "") -> tuple[str, list[str]]:
    worst, waits = "FILLED", []
    for raw in st["paths"]:
        rel = raw.replace("[root]", root).replace("[slug]", slug)
        s, w = judge(rel)
        waits += w
        if RANK[s] < RANK[worst]:
            worst = s
    return worst, list(dict.fromkeys(waits))


def main() -> int:
    stations = load_stations()
    company = [s for s in stations if s["unit"] == "company"]
    piece = [s for s in stations if s["unit"] == "piece"]
    side = [s for s in stations if s["unit"] == "side"]
    violations: list[str] = []

    print(f"# Assembly line - {datetime.date.today().isoformat()}\n")
    print("## Company stations\n")
    results = []
    for st in company:
        status, waits = station_status(st)
        results.append((st, status))
        print(f"- {st['id']:<4} {st['name']:<12} {status:<8}" + (f"  waiting on: {', '.join(waits)}" if waits else ""))

    def rank_of(sid: str) -> int:
        return int(sid[1])

    for st, status in results:
        if status == "FILLED":
            earlier = [(e, s) for e, s in results if rank_of(e["id"]) < rank_of(st["id"]) and s != "FILLED"]
            for e, s in earlier:
                violations.append(f"{st['id']} is FILLED while earlier station {e['id']} is {s}")
    company_done = all(s == "FILLED" for _, s in results)

    print("\n## Side station\n")
    producer = True
    for st in side:
        status, _ = station_status(st)
        producer = status == "FILLED"
        label = "OPERATIONAL" if producer else "NOT OPERATIONAL"
        print(f"- {st['id']:<4} {st['name']:<12} {label}" + ("" if producer else f"  (no `{st['paths'][0]}`): every image slot stays WAITING; S7 is capped at PARTIAL"))

    units = []
    if PIECES.is_dir():
        units += [("piece", d.name[len("research-"):], str(d.relative_to(ROOT)) + "/") for d in sorted(PIECES.glob("research-*")) if d.is_dir()]
    if CLIENT_UNITS.is_dir():
        units += [("client", d.name, str(d.relative_to(ROOT)) + "/") for d in sorted(CLIENT_UNITS.iterdir()) if d.is_dir()]

    print("\n## Units of work\n")
    if not units:
        print("- none (stations S3-S8 are EMPTY)")
    for kind, slug, root in units:
        if not company_done:
            violations.append(f"{kind} unit `{root}` exists while company stations S0-S2 are not all FILLED")
        if kind == "client":
            print(f"- client `{root}`: station files are fixed at the first instance (see ASSEMBLY_LINE.md)")
            continue
        print(f"- piece `{slug}`:")
        prev = []
        for st in piece:
            status, waits = station_status(st, root.rstrip("/"), slug)
            # Units are stricter than company stations: any output at a later station
            # while an earlier one is not FILLED is a skip-ahead (checked before the S7 cap).
            if status != "EMPTY" and any(s != "FILLED" for s in prev):
                violations.append(f"piece `{slug}`: {st['id']} has output while an earlier piece station is not FILLED")
            prev.append(status)
            if st["id"] == "S7" and not producer and status == "FILLED":
                status, waits = "PARTIAL", waits + ["[WAITING: side station M, no image producer]"]
            print(f"    {st['id']:<3} {st['name']:<8} {status}" + (f"  waiting on: {', '.join(waits)}" if waits else ""))

    print("\n## Deferred by rule (listed, not blocking)\n")
    for d in dict.fromkeys(DEFERRALS):
        print(f"- {d}")
    if not DEFERRALS:
        print("- none")

    first_open = next(((st, s) for st, s in results if s != "FILLED"), None)
    print("\n## Line position\n")
    if first_open:
        same_rank = [st["id"] for st, s in results if rank_of(st["id"]) == rank_of(first_open[0]["id"]) and s != "FILLED"]
        print(f"Stuck at {'/'.join(same_rank)}: {first_open[0]['name']} is {first_open[1]}. Units cannot start until S0-S2 are FILLED.")
    else:
        print("Company stations are FILLED. Units may run: see each unit's first non-FILLED station above.")

    print("\n## Skip-ahead check\n")
    if violations:
        for v in violations:
            print(f"- VIOLATION: {v}")
    else:
        print("- none")
    return 1 if violations else 0


if __name__ == "__main__":
    sys.exit(main())
