#!/usr/bin/env bash
# Usage: page-hash.sh <page.md>
# Prints the 8-char drift hash of a page: md5 of the page with its own
# ai-augmented {{$include}} line removed, so adding/removing the include
# line never changes the hash.
set -euo pipefail
[ -f "${1:-}" ] || { echo "usage: $0 <page.md>" >&2; exit 2; }
if command -v md5 >/dev/null 2>&1; then sum() { md5 -q; }; else sum() { md5sum | cut -d' ' -f1; }; fi
grep -v '{{\$include .*ai-augmented-' "$1" | sum | cut -c1-8
