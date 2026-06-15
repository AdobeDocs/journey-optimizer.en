#!/usr/bin/env python3
"""Insert the standard "On this page" shaded box after the H1 of AJO doc pages.

The box is placed immediately after the first H1, before any existing content
(including a `>[!CONTEXTUALHELP]` block). The operation is idempotent: a page that
already has a box right after its H1 is skipped.

The sentence itself is intentionally left as a TODO placeholder unless
`--seed-from-description` is passed, in which case the frontmatter `description`
is used as a first draft (still meant to be reviewed/refined by a human or AI).

Usage:
    python add_on_this_page.py help/using/reports            # a folder
    python add_on_this_page.py help/using/reports/foo.md     # one file
    python add_on_this_page.py help/using/reports --seed-from-description
    python add_on_this_page.py help/using/reports --dry-run
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

BOX_BEGIN = ">[!BEGINSHADEBOX]"
BOX_END = ">[!ENDSHADEBOX]"
LABEL = "**On this page:** "
TODO = "{{TODO: describe the purpose of this page in one sentence}}"

# Path parts that mark reference/syntax pages excluded from scope.
DEFAULT_EXCLUDE_PARTS = {"api-reference", "expression", "functions"}

H1_PREFIX = "# "


def is_excluded(path: Path, exclude_parts: set[str]) -> bool:
    return any(part in exclude_parts for part in path.parts)


def read_frontmatter_description(lines: list[str]) -> str | None:
    """Return the frontmatter `description:` value, if present (single-line)."""
    if not lines or lines[0].strip() != "---":
        return None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            break
        stripped = lines[i].strip()
        if stripped.lower().startswith("description:"):
            value = stripped.split(":", 1)[1].strip().strip('"').strip("'")
            return value or None
    return None


def find_first_h1(lines: list[str]) -> int | None:
    for i, line in enumerate(lines):
        if line.startswith(H1_PREFIX) and not line.startswith("##"):
            return i
    return None


def already_has_box(lines: list[str]) -> bool:
    """True if an 'On this page' box already exists anywhere in the file.

    Keyed off the label (not BEGINSHADEBOX) since shaded boxes are also used in
    page bodies; this keeps the insertion idempotent without false matches.
    """
    return any(LABEL in line for line in lines)


def build_box(sentence: str) -> list[str]:
    return [BOX_BEGIN, "", LABEL + sentence, "", BOX_END]


def process_file(path: Path, seed: bool, dry_run: bool) -> str:
    text = path.read_text(encoding="utf-8")
    lines = text.split("\n")

    h1_idx = find_first_h1(lines)
    if h1_idx is None:
        return "skip (no H1)"
    if already_has_box(lines):
        return "skip (already has box)"

    sentence = TODO
    if seed:
        desc = read_frontmatter_description(lines)
        if desc:
            sentence = desc if desc.endswith(".") else desc + "."

    # Collapse blank lines immediately after the H1 so we control spacing.
    rest_start = h1_idx + 1
    while rest_start < len(lines) and lines[rest_start].strip() == "":
        rest_start += 1

    new_lines = (
        lines[: h1_idx + 1]
        + [""]
        + build_box(sentence)
        + [""]
        + lines[rest_start:]
    )
    new_text = "\n".join(new_lines)

    if dry_run:
        return "would edit" + (" (seeded)" if seed and sentence != TODO else " (TODO)")

    path.write_text(new_text, encoding="utf-8")
    return "edited" + (" (seeded)" if seed and sentence != TODO else " (TODO)")


def collect_files(paths: list[str], exclude_parts: set[str]) -> list[Path]:
    files: list[Path] = []
    for raw in paths:
        p = Path(raw)
        if p.is_dir():
            files.extend(sorted(p.glob("**/*.md")))
        elif p.is_file() and p.suffix == ".md":
            files.append(p)
    # De-dupe, drop excluded.
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
    ap.add_argument("paths", nargs="+", help="Files or folders to process")
    ap.add_argument("--seed-from-description", action="store_true",
                    help="Seed the sentence from the frontmatter description")
    ap.add_argument("--dry-run", action="store_true", help="Report without writing")
    ap.add_argument("--exclude", nargs="*", default=sorted(DEFAULT_EXCLUDE_PARTS),
                    help="Path parts to exclude (default: api-reference expression functions)")
    args = ap.parse_args()

    exclude_parts = set(args.exclude)
    files = collect_files(args.paths, exclude_parts)
    if not files:
        print("No in-scope .md files found.", file=sys.stderr)
        return 1

    counts: dict[str, int] = {}
    for f in files:
        status = process_file(f, args.seed_from_description, args.dry_run)
        key = status.split(" (")[0]
        counts[key] = counts.get(key, 0) + 1
        print(f"{status:24} {f}")

    print("\nSummary:", ", ".join(f"{k}={v}" for k, v in sorted(counts.items())))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
