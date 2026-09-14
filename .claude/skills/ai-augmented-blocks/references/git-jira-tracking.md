# Git, PR, and JIRA tracking

How to land the change safely and track it. Two firm rules from the author:

1. **Ask before opening a PR.** Generate and verify the block regardless, but only open a pull
   request if the author says yes.
2. **Never merge.** These PRs exist for human review. Merging is always the author's decision.

## Structural sweep (run before committing)

For every page processed in the folder:

```bash
cd <repo>
for p in <page1> <page2> ...; do
  f="help/_includes/do-not-localize/<folder>/ai-augmented-$p.md"
  inc="help/using/<folder>/$p.md"
  [ -f "$f" ] || echo "MISSING BLOCK: $f"
  grep -q '^# AI Knowledge Reference' "$f"            || echo "$p: missing H1"
  grep -q '^+++ AI Knowledge Reference' "$f"          || echo "$p: missing accordion open"
  grep -q 'This section contains structured knowledge' "$f" || echo "$p: missing opening para 1"
  grep -q 'ai-section-version' "$f"                   || echo "$p: missing sync comment"
  grep -nEi "\b(isn't|aren't|don't|doesn't|didn't|can't|won't|wouldn't|couldn't|shouldn't|it's|we've|we're|you're|they're|that's|there's|haven't|hasn't|wasn't|weren't)\b" "$f" \
    | grep -vi 'UICONTROL' && echo "  ^ $p contraction"
  grep -q "do-not-localize/<folder>/ai-augmented-$p.md" "$inc" || echo "$p: MISSING include in page"
done
echo "=== sweep done ==="
git status --short
```

Any line printed (other than "sweep done" and the `git status` list) is a defect to fix before
committing.

## Branch and commit (never commit on main)

```bash
git checkout main -q && git pull -q origin main
git checkout -q -b DOCAC-<key> origin/main    # branch name = the JIRA task key
# ... generate + verify + sweep ...
git add help/_includes/do-not-localize/<folder>/ help/using/<folder>/*.md
git commit -q -m "DOCAC-<key> Add AI Knowledge Reference blocks (<folder>)

<one-line what + the verification result>

Co-Authored-By: Claude <model> <noreply@anthropic.com>"
```

**Verify the commit landed on the branch, not on `main`** (a known foot-gun — if you switched to
`main` to inspect pages, a later commit can land there):

```bash
git rev-parse --abbrev-ref HEAD                    # must print DOCAC-<key>
git rev-list --left-right --count origin/main...DOCAC-<key>   # must show  0<TAB>1
```

If a commit accidentally landed on `main`: `git branch -f DOCAC-<key> <sha>` to point the branch
at it, `git checkout DOCAC-<key>`, then `git branch -f main origin/main` to reset local main.
`origin/main` is never affected by a local mistake.

Push: `git push -u origin DOCAC-<key>` (use `--force-with-lease` if the branch already exists
remotely at an older commit).

## Ask about the PR

Ask the author plainly, for example: *"Blocks generated and verified for `<folder>`. Do you want
me to open a PR for review?"* Only if yes:

```bash
gh pr create --base main --head DOCAC-<key> \
  --title "DOCAC-<key> Add AI Knowledge Reference blocks (<folder>)" \
  --body-file <pr-body>.md
```

The PR body ends with the required attribution line
(`🤖 Generated with [Claude Code](https://claude.com/claude-code)`). **Do not merge** — leave the
PR open for review.

## JIRA tracking

Track every change in a DOCAC task (rollout epic: `DOCAC-15582`). Find or create the folder's
task, then:

1. **Comment** with what changed and the verification result (pages covered/skipped, verifier
   clean/corrected, any notable hard-vs-default calls). Include the PR link if one was opened.
2. **Set the fix version** (this program used `AJO26.9`).
3. **Transition** New → In Progress → Resolved (resolution "Fixed"), per your workflow. In this
   project the transition ids were `4` (Start Progress) then `5` (Resolve, with resolution
   `{"name":"Fixed"}`); a task still in "New" must be started before it can be resolved.

Use the corporate JIRA MCP tools (`add_jira_comment`, `update_jira_issue` for `fixVersions`,
`bulk_transition_jira_issues`) or the JIRA UI. If you lack JIRA access, hand this step to
someone who has it and note it in your report.

## One folder = one branch = one task

Do not mix unrelated folders in a single branch or PR. A new page added later is its own small
change (CREATE mode) and can share the folder's task or get its own, as your team prefers.
