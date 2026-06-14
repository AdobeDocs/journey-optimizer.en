#!/usr/bin/env python3
"""Validate the "On this page" shaded box on AJO doc pages.

Checks, for each in-scope page:
  - the box appears exactly once and is well-formed (matching BEGIN/END);
  - it sits directly after the first H1 (only blank lines in between);
  - it contains the `**On this page:**` label;
  - no leftover TODO placeholder remains.

By default, pages WITHOUT a box are reported as "pending" (not a failure), so the
script can run repo-wide during the rollout. Pass `--require` to also fail when a
box is missing (use this when a folder/PR is meant to be complete).

Exit code is non-zero if any FAIL is found (and, with --require, any pending page).

Usage:
    python validate_on_this_page.py help                       # whole guide
    python validate_on_this_page.py help/using/reports --require
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

BOX_BEGIN = ">[!BEGINSHADEBOX]"
BOX_END = ">[!ENDSHADEBOX]"
LABEL = "**On this page:**"
TODO_MARKER = "{{TODO"

DEFAULT_EXCLUDE_PARTS = {"api-reference", "expression", "functions"}
H1_PREFIX = "# "


def is_excluded(path: Path, exclude_parts: set[str]) -> bool:
    return any(part in exclude_parts for part in path.parts)


def find_first_h1(lines: list[str]) -> int | None:
    for i, line in enumerate(lines):
        if line.startswith(H1_PREFIX) and not line.startswith("##"):
            return i
    return None


def validate_file(path: Path) -> tuple[str, list[str]]:
    """Return (status, problems) where status is PASS / FAIL / PENDING.

    The "On this page" box is identified by its label, NOT by BEGINSHADEBOX,
    because shaded boxes are also used legitimately elsewhere in page bodies.
    """
    lines = path.read_text(encoding="utf-8").split("\n")
    problems: list[str] = []

    label_lines = [i for i, l in enumerate(lines) if LABEL in l]
    if not label_lines:
        return "PENDING", ["no 'On this page' box"]
    if len(label_lines) > 1:
        return "FAIL", [f"found {len(label_lines)} 'On this page' labels (expected 1)"]

    li = label_lines[0]
    begins = [i for i, l in enumerate(lines) if l.strip() == BOX_BEGIN]
    ends = [i for i, l in enumerate(lines) if l.strip() == BOX_END]

    begin_above = max((b for b in begins if b < li), default=None)
    end_below = min((e for e in ends if e > li), default=None)
    if begin_above is None or end_below is None:
        return "FAIL", ["'On this page' label is not wrapped in a shaded box"]
    # Make sure no box boundary sits between the opener/closer and the label.
    if any(begin_above < e < li for e in ends) or any(li < b < end_below for b in begins):
        problems.append("malformed shaded box around the 'On this page' label")

    if TODO_MARKER in "\n".join(lines[begin_above: end_below + 1]):
        problems.append("TODO placeholder not filled in")

    h1_idx = find_first_h1(lines)
    if h1_idx is None:
        problems.append("no H1 found")
    elif begin_above < h1_idx:
        problems.append("box appears before the H1")
    elif any(l.strip() != "" for l in lines[h1_idx + 1: begin_above]):
        problems.append("box is not directly after the H1 (content in between)")

    return ("FAIL", problems) if problems else ("PASS", [])


def collect_files(paths: list[str], exclude_parts: set[str]) -> list[Path]:
    files: list[Path] = []
    for raw in paths:
        p = Path(raw)
        if p.is_dir():
            files.extend(sorted(p.glob("**/*.md")))
        elif p.is_file() and p.suffix == ".md":
            files.append(p)
    seen: set[Path] = set()
    result: list[Path] = []
    for f in files:
        if f in seen or is_excluded(f, exclude_parts):
            continue
        seen.add(f)
        result.append(f)
    return result


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("paths", nargs="+", help="Files or folders to validate")
    ap.add_argument("--require", action="store_true",
                    help="Treat missing boxes (PENDING) as failures")
    ap.add_argument("--exclude", nargs="*", default=sorted(DEFAULT_EXCLUDE_PARTS),
                    help="Path parts to exclude (default: api-reference expression functions)")
    args = ap.parse_args()

    files = collect_files(args.paths, set(args.exclude))
    if not files:
        print("No in-scope .md files found.", file=sys.stderr)
        return 1

    n_pass = n_fail = n_pending = 0
    for f in files:
        status, problems = validate_file(f)
        if status == "PASS":
            n_pass += 1
        elif status == "PENDING":
            n_pending += 1
            if args.require:
                print(f"PENDING {f}: {problems[0]}")
        else:
            n_fail += 1
            for p in problems:
                print(f"FAIL    {f}: {p}")

    print(f"\nSummary: pass={n_pass} fail={n_fail} pending={n_pending} (total={len(files)})")

    if n_fail > 0:
        return 2
    if args.require and n_pending > 0:
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
