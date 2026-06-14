#!/usr/bin/env python3
"""Generate a review report for the "On this page" boxes.

For each in-scope page it extracts the frontmatter `description` (the editorial
source of truth) next to the proposed "On this page" sentence, and flags likely
problems so a human can verify all wording at a glance instead of opening every file.

Flags raised:
  - no-description : page has no frontmatter description to compare against.
  - pending        : no "On this page" box yet.
  - multi-sentence : the box contains more than one sentence.
  - TODO           : an unfilled placeholder remains.
  - ungrounded:<w> : content word(s) in the sentence that do NOT appear anywhere on
                     the page (outside the box itself) -> possible hallucination.

This is a review aid, not a hard gate; it always exits 0. Use it to drive the
human sign-off before merging each folder/PR.

Usage:
    python review_report.py help/using/building-journeys
    python review_report.py help/using/reports --format csv --output review.csv
    python review_report.py help --flagged-only          # only rows needing attention
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

LABEL = "**On this page:**"
BOX_BEGIN = ">[!BEGINSHADEBOX]"
BOX_END = ">[!ENDSHADEBOX]"
TODO_MARKER = "{{TODO"
DEFAULT_EXCLUDE_PARTS = {"api-reference", "expression", "functions"}


def is_excluded(path: Path, exclude_parts: set[str]) -> bool:
    return any(part in exclude_parts for part in path.parts)


def read_description(lines: list[str]) -> str | None:
    if not lines or lines[0].strip() != "---":
        return None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            break
        s = lines[i].strip()
        if s.lower().startswith("description:"):
            return s.split(":", 1)[1].strip().strip('"').strip("'") or None
    return None


def extract_sentence(lines: list[str]) -> tuple[str | None, tuple[int, int] | None]:
    """Return (sentence, (begin_idx, end_idx)) for the On this page box, if any."""
    label_idx = next((i for i, l in enumerate(lines) if LABEL in l), None)
    if label_idx is None:
        return None, None
    sentence = lines[label_idx].split(LABEL, 1)[1].strip()
    begins = [i for i, l in enumerate(lines) if l.strip() == BOX_BEGIN and i < label_idx]
    ends = [i for i, l in enumerate(lines) if l.strip() == BOX_END and i > label_idx]
    span = (begins[-1] if begins else label_idx, ends[0] if ends else label_idx)
    return sentence, span


# Capitalized words that are too generic to be worth grounding individually.
GROUNDING_IGNORE = {"learn", "adobe", "experience", "platform", "journey",
                    "journeys", "the", "a", "an"}


def _variants(term: str) -> set[str]:
    """Normalized lookup variants for a candidate term (handles hyphens/plurals)."""
    t = term.lower().rstrip(".,;:'s")
    out = {t, t.replace("-", " "), t.replace("-", "")}
    for part in t.replace("-", " ").split():
        if len(part) >= 3:
            out.add(part)
            out.add(part[:-1] if part.endswith("s") else part)
    return {v for v in out if v}


def grounding_flags(sentence: str, corpus: str) -> list[str]:
    """Flag proper-noun / acronym candidates that don't appear on the page.

    We only check capitalized multi-word names and acronyms (e.g. 'Read Audience',
    'Send-Time Optimization', 'SMS', 'REST') because those are where a wrong feature
    name = a real hallucination. Ordinary lowercase paraphrase words are ignored.
    """
    corpus_l = corpus.lower()
    corpus_nohyphen = corpus_l.replace("-", " ")
    words = sentence.split()
    unmatched: list[str] = []

    # Build capitalized phrases (consecutive Capitalized / ALLCAPS words),
    # skipping the very first word of the sentence (always capitalized).
    i = 0
    while i < len(words):
        raw = words[i].strip("\"'()[]—,.;:")
        is_cap = bool(raw) and (raw[0].isupper() or raw.isupper())
        is_acronym = raw.isupper() and len(raw) >= 2
        if i == 0 or not is_cap:
            i += 1
            continue
        phrase = [raw]
        j = i + 1
        while j < len(words):
            nxt = words[j].strip("\"'()[]—,.;:")
            if nxt and (nxt[0].isupper() or nxt.isupper()):
                phrase.append(nxt)
                j += 1
            else:
                break
        term = " ".join(phrase)
        candidate = term.lower().rstrip(".,;:")
        if candidate not in GROUNDING_IGNORE and not (len(phrase) == 1 and not is_acronym and len(raw) < 3):
            variants = _variants(term)
            if not any(v in corpus_l or v in corpus_nohyphen for v in variants):
                if term not in unmatched:
                    unmatched.append(term)
        i = j
    return unmatched


def analyze(path: Path) -> dict:
    lines = path.read_text(encoding="utf-8").split("\n")
    description = read_description(lines)
    sentence, span = extract_sentence(lines)

    flags: list[str] = []
    if description is None:
        flags.append("no-description")

    if sentence is None:
        flags.append("pending")
    else:
        if TODO_MARKER in sentence:
            flags.append("TODO")
        body = sentence.rstrip()
        if body.endswith("."):
            body = body[:-1]
        if ". " in body:
            flags.append("multi-sentence")
        # Corpus = whole file minus the box block, so the sentence can't match itself.
        if span:
            corpus_lines = lines[: span[0]] + lines[span[1] + 1:]
        else:
            corpus_lines = lines
        ungrounded = grounding_flags(sentence, "\n".join(corpus_lines))
        if ungrounded:
            flags.append("ungrounded:" + ",".join(ungrounded))

    return {
        "path": str(path),
        "description": description or "",
        "sentence": sentence or "",
        "flags": flags,
    }


def collect_files(paths: list[str], exclude_parts: set[str]) -> list[Path]:
    files: list[Path] = []
    for raw in paths:
        p = Path(raw)
        if p.is_dir():
            files.extend(sorted(p.glob("**/*.md")))
        elif p.is_file() and p.suffix == ".md":
            files.append(p)
    seen, result = set(), []
    for f in files:
        if f in seen or is_excluded(f, exclude_parts):
            continue
        seen.add(f)
        result.append(f)
    return result


def md_escape(text: str) -> str:
    return text.replace("|", "\\|")


def render_md(rows: list[dict]) -> str:
    out = ["| Page | Flags | Description (source) | Proposed sentence |",
           "| --- | --- | --- | --- |"]
    for r in rows:
        flags = " ".join(r["flags"]) or "ok"
        out.append("| {} | {} | {} | {} |".format(
            md_escape(r["path"]), md_escape(flags),
            md_escape(r["description"]), md_escape(r["sentence"])))
    return "\n".join(out)


def render_csv(rows: list[dict]) -> str:
    import csv
    import io
    buf = io.StringIO()
    w = csv.writer(buf)
    w.writerow(["page", "flags", "description", "sentence"])
    for r in rows:
        w.writerow([r["path"], " ".join(r["flags"]), r["description"], r["sentence"]])
    return buf.getvalue()


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("paths", nargs="+")
    ap.add_argument("--format", choices=["md", "csv"], default="md")
    ap.add_argument("--output", help="Write to file instead of stdout")
    ap.add_argument("--flagged-only", action="store_true",
                    help="Only include rows that have flags other than 'pending'")
    ap.add_argument("--fail-on-flag", action="store_true",
                    help="Exit non-zero if any page has a flag other than 'pending' "
                         "(use as a CI gate)")
    ap.add_argument("--exclude", nargs="*", default=sorted(DEFAULT_EXCLUDE_PARTS))
    args = ap.parse_args()

    files = collect_files(args.paths, set(args.exclude))
    if not files:
        print("No in-scope .md files found.", file=sys.stderr)
        return 1

    all_rows = [analyze(f) for f in files]

    def non_pending_flags(row: dict) -> list[str]:
        return [f for f in row["flags"] if f != "pending"]

    pending = sum(1 for r in all_rows if "pending" in r["flags"])
    flagged = sum(1 for r in all_rows if non_pending_flags(r))

    rows = [r for r in all_rows if non_pending_flags(r)] if args.flagged_only else all_rows
    rendered = render_md(rows) if args.format == "md" else render_csv(rows)

    # Summary to stderr so it doesn't pollute a redirected report.
    print(f"[summary] files={len(files)} pending={pending} "
          f"flagged(non-pending)={flagged}", file=sys.stderr)

    if args.output:
        Path(args.output).write_text(rendered + "\n", encoding="utf-8")
        print(f"[written] {args.output}", file=sys.stderr)
    else:
        print(rendered)

    if args.fail_on_flag and flagged > 0:
        print(f"[fail] {flagged} page(s) have non-pending flags", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
