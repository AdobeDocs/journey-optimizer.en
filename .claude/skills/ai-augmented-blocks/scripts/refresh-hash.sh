#!/usr/bin/env bash
# Usage: refresh-hash.sh <page.md>
# Writes the page's current drift hash into its block's sync comment. Run ONLY after the block
# has passed the independent verification round. Adds the comment if the block has none.
set -euo pipefail
page="${1:-}"; [ -f "$page" ] || { echo "usage: $0 <page.md>" >&2; exit 2; }
root=$(git rev-parse --show-toplevel); cd "$root"
inc=$(grep -o '/help/_includes/do-not-localize/[^ }]*ai-augmented-[^ }]*\.md' "$page" | head -1)
[ -n "$inc" ] && [ -f ".$inc" ] || { echo "no block found for $page" >&2; exit 1; }
h=$("$root/.claude/skills/ai-augmented-blocks/scripts/page-hash.sh" "$page")
f=".$inc"
if grep -q 'source-hash:' "$f"; then
  sed -i.bak -E "s/source-hash: [0-9a-f]+/source-hash: $h/" "$f" && rm -f "$f.bak"
else
  printf '\n<!-- ai-section-version: 1 | source-hash: %s -->\n' "$h" >> "$f"
fi
echo "$page -> $h"
