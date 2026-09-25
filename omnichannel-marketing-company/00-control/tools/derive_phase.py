#!/usr/bin/env python3
"""derive_phase.py - re-derive the company phase from disk (anti-inflation law, handoff §3.1).

Operator for:
  - the Phase Map (handoff §3): derived phase = the first phase whose exit minimum fails;
  - the knowledge-work override (handoff §3): research-dependent outputs are invalid
    until the three contracts exist;
  - the buyer-facing gate described in `00-control/execute.md`.

Usage (run from anywhere):
    python3 ".../00-control/tools/derive_phase.py"                   # report
    python3 ".../00-control/tools/derive_phase.py" --write-manifest  # also write phase fields to manifest.json

Exit code: 0 = manifest agrees with (or is below) the derived phase; 3 = manifest OVERCLAIMS.

The gate table below is the single source of truth for which artifact satisfies which
phase minimum. Paths for phases 2-8 follow the handoff §8 build job; where the handoff
named no path, S001 chose one and logged the decision in `meta_workspace.md` §4.
Changing a path here is a governance change: log it in `meta_workspace.md` §4.

Check kinds:
  exists      file or folder exists
  contains    file exists and contains the text
  files       folder holds >= N files matching a glob
  rows        markdown table data rows >= N (optionally only rows containing a text)
  tagged      file has a '## Claims' section; every bullet under it carries an evidence
              tag - [src: ...], [dossier: ...] or [CARBON-BLOCKED ...]; at least one bullet
  exercised   an exercised-loop requirement. Never passes by script until its ledger
              schema exists (Build Order Law: the first real ledger row defines the schema).
"""
from __future__ import annotations

import datetime
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TAGS = ("[src:", "[dossier:", "[CARBON-BLOCKED")

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
def exists(path):
    return ("exists", path)


def contains(path, text):
    return ("contains", path, text)


def files(folder, glob, n=1):
    return ("files", folder, glob, n)


def rows(path, n=1, text=None):
    return ("rows", path, n, text)


def tagged(path):
    return ("tagged", path)


def exercised(what):
    return ("exercised", what)


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


def run(check) -> tuple[bool, str]:
    kind = check[0]
    if kind == "exercised":
        return False, "NOT-MACHINE-CHECKED: exercised-loop evidence; schema defined when the first ledger row exists"
    p = ROOT / check[1]
    if kind == "exists":
        return p.exists(), "" if p.exists() else f"missing `{check[1]}`"
    if not p.exists():
        return False, f"missing `{check[1]}`"
    if kind == "contains":
        ok = check[2] in p.read_text(encoding="utf-8")
        return ok, "" if ok else f"`{check[1]}` lacks `{check[2]}`"
    if kind == "files":
        found = [f for f in p.glob(check[2]) if f.is_file()]
        ok = len(found) >= check[3]
        return ok, "" if ok else f"`{check[1]}` holds {len(found)} of >= {check[3]} `{check[2]}`"
    if kind == "rows":
        data = table_rows(p.read_text(encoding="utf-8"))
        if check[3]:
            data = [r for r in data if check[3] in r]
        ok = len(data) >= check[2]
        what = f" containing `{check[3]}`" if check[3] else ""
        return ok, "" if ok else f"`{check[1]}` has {len(data)} of >= {check[2]} table row(s){what}"
    if kind == "tagged":
        text = p.read_text(encoding="utf-8")
        m = re.search(r"^## Claims\s*$(.*?)(?=^## |\Z)", text, re.M | re.S)
        if not m:
            return False, f"`{check[1]}` has no `## Claims` section"
        bullets = [ln for ln in m.group(1).splitlines() if re.match(r"^\s*([-*]|\d+\.)\s+\S", ln)]
        untagged = [b for b in bullets if not any(t in b for t in TAGS)]
        if not bullets:
            return False, f"`{check[1]}` `## Claims` has no bullets"
        ok = not untagged
        return ok, "" if ok else f"`{check[1]}`: {len(untagged)} of {len(bullets)} claim(s) carry no evidence tag"
    raise ValueError(kind)


# ------------------------------------------------------------ the gate table
# EXIT[n] = minimum artifacts to leave phase n (i.e. to hold phase n+1).
EXIT = {
    0: [
        ("company manifest", exists("manifest.json")),
        ("service thesis", contains("00-control/status.md", "Primary Offer:")),
        ("buyer map", contains("00-control/status.md", "Buyer Path:")),
        ("initial system rules", contains("00 - ENTRY.md", "## Runtime Law")),
    ],
    1: [
        ("foundation: customer, evidence-tagged", tagged("01-foundation/customer.md")),
        ("foundation: problem, evidence-tagged", tagged("01-foundation/problem.md")),
        ("foundation: value proposition, evidence-tagged", tagged("01-foundation/value-proposition.md")),
        ("source packet: research plan", exists("02-sourcing/research_plan.md")),
        ("source packet: input registry", exists("02-sourcing/input_registry.md")),
        ("source packet: source ledger (>= 1 row)", rows("02-sourcing/source_ledger.md", 1)),
        ("source packet: >= 1 research dossier", files("02-sourcing/01 - dossiers", "**/*.md", 1)),
        ("source packet: >= 1 carbon input form", files("00-control/carbon-input", "CARBON_INPUT_FORM-*.md", 1)),
    ],
    2: [
        ("capability cards", files("06 - capability/cards", "*.md", 1)),
        ("promotion gates", exists("06 - capability/promotion-gates.md")),
        ("validation-run template", exists("06 - capability/validation-run-template.md")),
        ("capability ledger (>= 1 row)", rows("06 - capability/capability-ledger.md", 1)),
    ],
    3: [
        ("pipeline ledger", exists("07 - acquisition/pipeline-ledger.md")),
        ("cognitive sequence rules", exists("07 - acquisition/sequence-rules.md")),
        ("proof system index", exists("08 - proof/00 - INDEX.md")),
        ("authority claims", exists("08 - proof/authority-claims.md")),
        ("public-proof rules", exists("08 - proof/public-proof-rules.md")),
        ("compiler contract", exists("00-control/contracts/COMPILER_CONTRACT.md")),
    ],
    4: [
        ("intake form", exists("09 - delivery/intake-form.md")),
        ("work packet", exists("09 - delivery/work-packet-template.md")),
        ("delivery packet", exists("09 - delivery/delivery-packet-template.md")),
        ("service ledger", exists("09 - delivery/delivery-ledger.md")),
        ("quality thresholds", exists("10 - quality/quality-thresholds.md")),
        ("QA checklist", exists("10 - quality/qa-checklist.md")),
        ("review report (>= 1 completed)", files("10 - quality/review-reports", "*.md", 1)),
    ],
    5: [
        ("client ledger (>= 1 row)", rows("11 - client-state/client-ledger.md", 1)),
        ("client template", exists("11 - client-state/client-template.md")),
        ("upgrade rules with thresholds", contains("12 - upgrade/upgrade-rules.md", "Threshold")),
        ("rollback rules", contains("12 - upgrade/upgrade-rules.md", "Rollback")),
        ("upgrade brief template", exists("12 - upgrade/upgrade-brief-template.md")),
    ],
    6: [
        ("lessons", exists("13 - memory/lessons.md")),
        ("patterns-to-promote", exists("13 - memory/patterns-to-promote.md")),
        ("drift checks", exists("14 - governance/drift-checks.md")),
        ("readiness dashboard", exists("14 - governance/readiness-dashboard.md")),
        ("phase map", exists("00-control/PHASE_DERIVATION.md")),
        ("exercised matter or governed commercial transition", exercised("matter")),
        ("exercised quality/proof disposition", exercised("disposition")),
    ],
    7: [
        ("matter moved through delivery and quality disposition", exercised("loop")),
        ("client/pipeline transition backed by a named artifact", exercised("transition")),
        ("governance refresh after the loop", exercised("refresh")),
    ],
    8: [
        ("repeated proof", exercised("repeat")),
        ("exercised loop for every sequence claimed operational", exercised("every-sequence")),
        ("readiness dashboard with no open overclaim", exercised("dashboard")),
    ],
}

OVERRIDE = [
    ("research-dossier contract", exists("00-control/contracts/RESEARCH_DOSSIER_CONTRACT.md")),
    ("compiler contract", exists("00-control/contracts/COMPILER_CONTRACT.md")),
    ("handoff contract", exists("00-control/contracts/HANDOFF_CONTRACT.md")),
]
RESEARCH_DEPENDENT = "`03-setup/01 - outputs/` P1-P4 (positioning, pitch stack, website surface, channel copy) and any market-facing claim"

BUYER_FACING = [
    ("foundation evidence-tagged (phase-1 foundation checks)", None),
    ("knowledge-work override contracts present", None),
    (">= 1 `live_capability` row in the capability ledger", rows("06 - capability/capability-ledger.md", 1, "live_capability")),
]


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

    foundation_ok = all(ok for label, ok, _ in report[1][2] if label.startswith("foundation"))
    live_ok, live_why = run(BUYER_FACING[2][1])
    gate = [(BUYER_FACING[0][0], foundation_ok, ""), (BUYER_FACING[1][0], ov_ok, ""), (BUYER_FACING[2][0], live_ok, live_why)]
    print("\n## Buyer-facing gate (operator for `00-control/execute.md`)\n")
    for label, ok, why in gate:
        print(f"- {label}: {'PASS' if ok else 'FAIL'}{(' - ' + why) if why else ''}")
    print(f"\nBuyer-facing asset work: {'OPEN' if all(ok for _, ok, _ in gate) else 'BLOCKED'}")

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
