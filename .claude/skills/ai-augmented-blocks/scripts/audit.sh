#!/usr/bin/env bash
# Usage: audit.sh [folder]   (folder under help/using/, default: all). Run from anywhere.
# Read-only. Lists pages as: CURRENT, DRIFTED, NO-HASH (block has no sync comment), MISSING, or MIGRATE.
set -uo pipefail
root=$(git rev-parse --show-toplevel); cd "$root"
here="$root/.claude/skills/ai-augmented-blocks/scripts"
dir="help/using/${1:-}"
cur=0; drift=0; miss=0; nohash=0
while IFS= read -r page; do
  case "$page" in help/using/rn/*|*release-notes*|*/toc.md|*/index.md) continue;; esac
  inc=$(grep -o '/help/_includes/do-not-localize/[^ }]*ai-augmented-[^ }]*\.md' "$page" | head -1)
  if [ -z "$inc" ]; then
    grep -q '^+++ AI Knowledge Reference' "$page" && s="MIGRATE (inline block)" || s="MISSING"
    [ "$s" = MISSING ] && miss=$((miss+1)); echo "$s  $page"; continue
  fi
  stored=$(grep -o 'source-hash: [0-9a-f]*' ".${inc}" 2>/dev/null | cut -d' ' -f2 || true)
  if [ -z "$stored" ]; then nohash=$((nohash+1)); echo "NO-HASH  $page"; continue; fi
  now=$("$here/page-hash.sh" "$page")
  if [ "$stored" = "$now" ]; then cur=$((cur+1)); echo "CURRENT  $page"
  else drift=$((drift+1)); echo "DRIFTED  $page  (stored=${stored:-none} now=$now)"; fi
done < <(find "$dir" -name '*.md' | sort)
echo "--- current=$cur drifted=$drift no-hash=$nohash missing=$miss"
