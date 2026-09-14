---
name: ai-augmented-blocks
description: "Generate and maintain AI Knowledge Reference blocks for Adobe Journey Optimizer docs (journey-optimizer.en). Use when a new page under help/using/ needs an AI block, when an existing page changed and its block may have drifted, or when asked to add/update/verify AI Knowledge Reference (AI-augmented) content. Produces a do-not-localize include under help/_includes/do-not-localize/<folder>/ai-augmented-<page>.md, wires it into the page with {{$include}}, runs a mandatory independent verification round so the block is true and unambiguous, tracks the work in a DOCAC JIRA task, and (only after asking the author) opens a PR. NEVER merges."
---

# AI Knowledge Reference blocks

This skill generates and maintains **AI Knowledge Reference** accordion blocks for the
Adobe Journey Optimizer documentation (`journey-optimizer.en`). The blocks are structured,
non-localized context appended to doc pages so the AI Assistant answers questions about
Journey Optimizer more accurately.

Each block is stored as a **do-not-localize include** (so it is never translated) and pulled
into its page with `{{$include}}`. A block contains **only facts derivable from its own page
body** — nothing imported from other pages, general product knowledge, or HTML comments.

> **Read the reference files before generating anything.** They contain the actual rules, not
> a summary:
> - `references/generation-spec.md` — block structure, the fixed opening, section-by-section
>   content rules, and every precision rule (hard-vs-recommended limits, validation modes,
>   status labels, no contractions, the banned-word list).
> - `references/verification-round.md` — the **mandatory** independent adversarial fact-check
>   that is the final quality gate. This is not optional and cannot be skipped.
> - `references/git-jira-tracking.md` — branch/commit/PR flow (ask the author before opening a
>   PR; **never merge**) and DOCAC JIRA tracking.

## When this skill applies

- **New page** created under `help/using/<folder>/` → generate a block for it.
- **Existing page changed** → check whether its block drifted from the page body and update it.
- Asked to **add, update, verify, or audit** AI Knowledge Reference / AI-augmented blocks.

## Scope and exclusions

- **In scope:** pages under `help/using/<folder>/`.
- **Out of scope — never add blocks here:**
  - `help/rp_landing_pages/` (get-started / landing pages) — excluded by author rule.
  - Thin navigation/link hubs, index-only pages, and near-empty pages. When a page is a bare
    list of links with no substantive concepts, **skip it and say why** — do not force a block.
  - Release notes (`help/using/rn/`, release-notes pages).
- When in doubt whether a page is substantive enough, judge by content: if it teaches real
  concepts, constraints, or terminology, cover it; if it only points elsewhere, skip it.

## Workflow

Work **one folder (or one page) at a time**. Do not batch unrelated folders into one branch.

### 1 — Determine targets and mode

Ask the author (or infer from the request / open files) which pages to process, and detect the
mode per page:

- **CREATE** — the page has no `{{$include .../ai-augmented-<page>.md}}` line and no existing
  inline `+++ AI Knowledge Reference` block → generate a new block.
- **UPDATE** — the page already has a block. Compute the page-body hash and compare it to the
  `source-hash` in the include's sync comment (see below). If they differ, the page drifted →
  regenerate/refresh the block. If they match, the block is current → skip (report "up to date").
- **MIGRATE** — the page has an *inline* `+++ AI Knowledge Reference` block (not yet
  externalized) → move it into a do-not-localize include and replace it with the `{{$include}}`
  line, preserving content fidelity.

Compute the page-body hash the same way everywhere (used for the sync comment and drift check):

```bash
md5 -q help/using/<folder>/<page>.md | cut -c1-8
```

Compute it **before** editing the page (the hash covers the body as it is when the block is
generated). On Linux use `md5sum help/using/<folder>/<page>.md | cut -c1-8`.

### 2 — Generate (or refresh) the block

Follow `references/generation-spec.md` exactly for every page. Key invariants:

- Two **fixed opening paragraphs**, verbatim, byte-for-byte (never paraphrased).
- Sections in order: **TL;DR, Intents, Glossary, Guardrails, Terminology, FAQ**.
- Every claim grounded in the page body only. No contractions. Qualify numbers as
  `(hard limit)` / `(recommended)` **only** when the page uses enforcement/recommendation
  wording; otherwise no qualifier. Use the page's exact validation-mode and status labels.
  Preserve `[!UICONTROL ...]` / `[!DNL ...]` strings verbatim. Never use the banned imprecise
  terms unless they appear verbatim on the page.

**Include file** — `help/_includes/do-not-localize/<folder>/ai-augmented-<page>.md`
(create the `<folder>` subdirectory if needed; flatten any nested page path with `-`):

```
---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

[fixed opening paragraphs + the six sections]

+++

<!-- ai-section-version: 1 | source-hash: <first 8 chars of md5 of the page body> -->
```

**Page edit** — add exactly one line, as the last content line, preceded by a blank line
(do not touch anything else in the page):

```
{{$include /help/_includes/do-not-localize/<folder>/ai-augmented-<page>.md}}
```

On UPDATE, edit the include file only (and bump `ai-section-version` if you wish to track
revisions); the page's `{{$include}}` line usually stays the same. Refresh the `source-hash` to
the current page-body hash once the block matches the page again.

Run the **self-check** in `references/generation-spec.md` (Step 3 verify-every-claim + the
post-generation checklist) before moving on. This is gate 1 of 2.

### 3 — Independent verification round (mandatory final gate)

This is the step the author specifically requires: **confirm each block is valid, true, and
free of ambiguity.** Run it as a *fresh, independent* pass — ideally a separate subagent that
sees only the page body and the block, with no memory of how the block was written — following
`references/verification-round.md`. It re-checks every claim, downgrades any mislabeled limit,
fixes Synonyms-vs-Do-not-confuse errors, and removes anything not grounded in the page. Apply
every fix to the include file before continuing. This is gate 2 of 2 and cannot be skipped.

### 4 — Structural sweep

Before committing, sweep every block for structure and hygiene (see the sweep snippet in
`references/git-jira-tracking.md`): front matter + `# AI Knowledge Reference` heading, the
`+++ … +++` fences, the fixed opening paragraph, the sync comment, no contractions (excluding
verbatim `[!UICONTROL ...]`), and a matching `{{$include}}` line in the page.

### 5 — Track in JIRA, then ask about a PR (never merge)

Follow `references/git-jira-tracking.md`:

1. Commit on a branch named for the JIRA task (`DOCAC-<key>`), never on `main`. Verify the
   commit landed on the branch (1 commit ahead of `origin/main`), not on `main`.
2. Update the DOCAC task: comment with what changed + the verification result, set the fix
   version, and transition it as your team's process requires.
3. **Ask the author whether they want a pull request.** Only open one if they say yes.
4. **Never merge.** These PRs are for human review; merging is always the author's call.

### 6 — Report

Report per page: created / updated / migrated / skipped (+ reason), the verification result
(clean or corrected, with the corrections), the JIRA task, and the PR link if one was opened.

## Notes for writers running this skill

- The block is a **derivative of the page body at a point in time** — treat it as part of the
  page. When you change a page in a way that touches a guardrail, limit, status label, or
  validation mode, update the block in the same change.
- JIRA and PR steps need access to the corporate JIRA and GitHub. If you do not have that
  access, still generate + verify the block and open the change locally; hand the JIRA/PR steps
  to someone who does.
- This skill lives in the repo so the whole writing team shares one process. Improve the
  reference files here rather than keeping private copies.
