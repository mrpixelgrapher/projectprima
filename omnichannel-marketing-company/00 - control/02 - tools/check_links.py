#!/usr/bin/env python3
"""check_links.py - verify every path reference in the company's markdown files.

Operator for the "every folder is wired" claim. Deterministic, stdlib only.

Usage (run from the company root):
    python3 "00 - control/02 - tools/check_links.py"
    python3 "00 - control/02 - tools/check_links.py" --all   # also list RESOLVED, UNVERIFIED, PATTERN

What counts as a reference: any text inside `backticks` that looks like a path
(contains / or \\, or ends in .md / .py / .json). Windows separators are
normalised to /. Each reference is resolved against the citing file's folder and
each folder above it, then (inside a task folder) against the task root, then against
the company root. Task paths are relative to the task root (`TASK_CONTRACT.md` §1).

Classes:
    RESOLVED      target exists on disk.
    EXTERNAL      target lives in the wider CE workspace (not in this repo). Matched
                  by a row of the register in
                  00 - control/05 - registers/EXTERNAL_DEPENDENCY_REGISTER.md.
    PATTERN       a naming pattern, not a link: contains [ ] { } < > * or |.
    UNVERIFIED    bare name/path (no ./ or ../ prefix) that does not resolve. Usually a
                  structure name inside a contract (e.g. `synthesis/SPINE.md`). Reported,
                  never failing.
    BROKEN        a reference that does not resolve and is not registered, and is either an
                  explicit relative link (./ or ../), a path that starts with a numbered
                  folder (`02 - content/...`, `06 - approval/`), or a path that now exists
                  only in an archive snapshot (stale: point it at the archive or at its
                  successor). FAILS.
    UNREGISTERED  reference that escapes the company root and matches no register row.
                  FAILS - add a register row or correct the path.

Not scanned:
    00 - control/04 - source-intent/  Tier 1 verbatim human input. Its backticked text
                                      quotes paths as prose; it is not wiring, and it can
                                      never be edited to satisfy a checker.
    99 - archive/                     past material, read-only, kept as it was; its old
                                      paths point at the pre-restructure tree.

Exit code: 0 when BROKEN + UNREGISTERED == 0, else 1.
"""
from __future__ import annotations

import os
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REGISTER = ROOT / "00 - control" / "05 - registers" / "EXTERNAL_DEPENDENCY_REGISTER.md"
SKIP = (ROOT / "00 - control" / "04 - source-intent", ROOT / "99 - archive")

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
    if ref.startswith(("python", "git ")) or " --" in ref or ".py " in ref:
        return False
    if len(ref) > 160 or " · " in ref:  # prose in backticks (a worked-example line), not a path
        return False
    return "/" in ref or "\\" in ref or ref.endswith(PATH_EXT)


def match_register(norm: str, register: list[tuple[str, str]]) -> str | None:
    padded = "/" + norm.strip("/") + "/"
    for rid, seg in register:
        if "/" + seg + "/" in padded:
            return rid
    return None


def task_root(src: Path) -> Path | None:
    """The nearest enclosing task folder (T-...), if the file lives in one."""
    for d in src.parents:
        if d == ROOT:
            return None
        if d.name.startswith("T-") and d.parent.name in ("work", "done", "pieces"):
            return d
    return None


def archived_match(norm: str) -> str | None:
    """A path that no longer resolves but exists in an archive snapshot: stale."""
    if not re.match(r"^\d\d ?- ?[A-Za-z]", norm):
        return None
    archive = ROOT / "99 - archive"
    if archive.is_dir():
        for snap in sorted(archive.iterdir()):
            if snap.is_dir() and (snap / norm).exists():
                return str((snap / norm).relative_to(ROOT))
    return None


def classify(ref: str, src: Path, register) -> tuple[str, str]:
    norm = ref.replace("\\", "/")
    if any(ch in PATTERN_CHARS for ch in norm):
        return "PATTERN", ""
    explicit = norm.startswith(("./", "../", ".\\"))
    # the citing folder and each folder above it (so a stage can name a sibling stage or
    # node: `06 - approval/`), the task root (inside a task), then the company root
    bases = [src.parent] + [d for d in src.parent.parents if ROOT in d.parents or d == ROOT]
    bases += [b for b in (task_root(src),) if b]
    for base in bases:
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
    archived = archived_match(norm)
    if archived:
        return "BROKEN", f"now archived: {archived}"
    if explicit or re.match(r"^\d\d - [a-z-]+/", norm):
        # an explicit relative link, or a path that starts with a numbered folder
        # (`02 - content/…`, or a sibling like `06 - approval/`), must resolve
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
            print(f"  {rel}  ->  `{ref}`" + (f"  [{detail}]" if detail and cls in ('RESOLVED', 'BROKEN') else ""))
    failing = len(results["BROKEN"]) + len(results["UNREGISTERED"])
    print(f"\nRESULT: {'PASS' if failing == 0 else 'FAIL'} ({failing} failing reference(s))")
    return 0 if failing == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
