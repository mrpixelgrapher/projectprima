#!/usr/bin/env python3
"""check_links.py - verify every path reference in the company's markdown files.

Operator for the "departments are linked" claim. Deterministic, stdlib only.

Usage (run from anywhere):
    python3 "omnichannel-marketing-company/00-control/tools/check_links.py"
    python3 ".../check_links.py" --all        # also list RESOLVED and UNVERIFIED references

What counts as a reference: any text inside `backticks` that looks like a path
(contains / or \\, or ends in .md / .py / .json). Windows separators are
normalised to /. Each reference is resolved against the citing file's folder
first, then against the company root.

Classes:
    RESOLVED      target exists on disk.
    EXTERNAL      target lives in the wider CE workspace (not in this repo). Matched
                  by a row of the register in
                  03 - architecture-governance/EXTERNAL_DEPENDENCY_REGISTER.md.
    PATTERN       a naming pattern, not a link: contains [ ] { } < > * or |.
    UNVERIFIED    bare name/path (no ./ or ../ prefix) that does not resolve. Usually a
                  structure name inside a contract (e.g. `synthesis/SPINE.md`). Reported,
                  never failing.
    BROKEN        explicit relative link (./ or ../) that stays inside the company, does
                  not resolve, and is not registered. FAILS.
    UNREGISTERED  reference that escapes the company root and matches no register row.
                  FAILS - add a register row or correct the path.

Not scanned: `00-control/source-intent/`. Those files are Tier 1 verbatim human input.
Their backticked text quotes paths and fragments as prose (e.g. `/observations/`); it is
not wiring, and it can never be edited to satisfy a checker.

Exit code: 0 when BROKEN + UNREGISTERED == 0, else 1.
"""
from __future__ import annotations

import os
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REGISTER = ROOT / "03 - architecture-governance" / "EXTERNAL_DEPENDENCY_REGISTER.md"
SKIP = (ROOT / "00-control" / "source-intent",)

TICK = re.compile(r"`([^`\n]+)`")
PATTERN_CHARS = set("[]{}<>*|")
PATH_EXT = (".md", ".py", ".json")


def load_register() -> list[tuple[str, str]]:
    """Return (register_id, match_segment) pairs from the register's table.

    Rows look like: | X-01 | `seg-a`, `seg-b` | ... - the ID is column 1, match
    segments are the backticked items in column 2.
    """
    pairs: list[tuple[str, str]] = []
    if not REGISTER.exists():
        return pairs
    for line in REGISTER.read_text(encoding="utf-8").splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 2 or not re.fullmatch(r"X-\d{2}", cells[0]):
            continue
        for seg in TICK.findall(cells[1]):
            pairs.append((cells[0], seg.replace("\\", "/").strip("/")))
    return pairs


def looks_like_path(ref: str) -> bool:
    if ref.startswith(("python", "git ")) or " --" in ref:
        return False
    return "/" in ref or "\\" in ref or ref.endswith(PATH_EXT)


def match_register(norm: str, register: list[tuple[str, str]]) -> str | None:
    padded = "/" + norm.strip("/") + "/"
    for rid, seg in register:
        if "/" + seg + "/" in padded:
            return rid
    return None


def classify(ref: str, src: Path, register) -> tuple[str, str]:
    norm = ref.replace("\\", "/")
    if any(ch in PATTERN_CHARS for ch in norm):
        return "PATTERN", ""
    explicit = norm.startswith(("./", "../", ".\\"))
    for base in (src.parent, ROOT):
        target = Path(os.path.normpath(base / norm))
        if target.exists():
            return "RESOLVED", str(target.relative_to(ROOT)) if ROOT in target.parents or target == ROOT else str(target)
    rid = match_register(norm, register)
    if rid:
        return "EXTERNAL", rid
    target = Path(os.path.normpath(src.parent / norm))
    escapes = ROOT not in target.parents and target != ROOT
    if escapes:
        return "UNREGISTERED", ""
    if explicit:
        return "BROKEN", ""
    return "UNVERIFIED", ""


def main() -> int:
    show_all = "--all" in sys.argv
    register = load_register()
    results: dict[str, list[tuple[str, str, str]]] = defaultdict(list)
    for md in sorted(ROOT.rglob("*.md")):
        if any(skip in md.parents for skip in SKIP):
            continue
        rel = md.relative_to(ROOT)
        for ref in TICK.findall(md.read_text(encoding="utf-8")):
            ref = ref.strip()
            if not looks_like_path(ref):
                continue
            cls, detail = classify(ref, md, register)
            results[cls].append((str(rel), ref, detail))

    order = ["BROKEN", "UNREGISTERED", "EXTERNAL", "UNVERIFIED", "PATTERN", "RESOLVED"]
    print(f"Company root: {ROOT}")
    print(f"Register rows loaded: {len({r for r, _ in register})} ({len(register)} match segments)")
    print("Summary: " + ", ".join(f"{c}={len(results[c])}" for c in order))
    for cls in order:
        if cls in ("RESOLVED", "UNVERIFIED", "PATTERN") and not show_all:
            continue
        if not results[cls]:
            continue
        print(f"\n== {cls} ({len(results[cls])}) ==")
        if cls == "EXTERNAL":
            by_id: dict[str, int] = defaultdict(int)
            for _, _, rid in results[cls]:
                by_id[rid] += 1
            for rid in sorted(by_id):
                print(f"  {rid}: {by_id[rid]} reference(s)")
            continue
        for rel, ref, detail in results[cls]:
            print(f"  {rel}  ->  `{ref}`" + (f"  [{detail}]" if detail and cls == 'RESOLVED' else ""))
    failing = len(results["BROKEN"]) + len(results["UNREGISTERED"])
    print(f"\nRESULT: {'PASS' if failing == 0 else 'FAIL'} ({failing} failing reference(s))")
    return 0 if failing == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
