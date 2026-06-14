# "On this page" box tooling

Tooling to add and verify the standard **"On this page"** shaded box at the top of
AJO documentation pages. See the spec in `.cursor/rules/on-this-page-box.mdc`.
Rollout is tracked under epic **DOCAC-14936** (one task per top-level folder).

## What the box looks like

```text
# Page Title {#anchor}

>[!BEGINSHADEBOX]

**On this page:** <one clear sentence describing the page's purpose>

>[!ENDSHADEBOX]
```

## Recommended workflow (per folder / Jira task)

Run from the repository root (`journey-optimizer.en/`).

1. **Insert boxes** (seeding a first-draft sentence from each page's frontmatter
   `description`). Mechanical, idempotent, never touches frontmatter:

   ```bash
   python scripts/on-this-page/add_on_this_page.py help/using/reports --seed-from-description
   ```

   Preview first with `--dry-run`.

2. **Refine the wording.** The seed is a starting point — edit each sentence so it
   reads as a purpose statement (one sentence, plain text, American English). If you
   skip `--seed-from-description`, a `{{TODO...}}` placeholder is inserted instead and
   the validator will flag any that remain.

3. **Validate** before opening the PR:

   ```bash
   python scripts/on-this-page/validate_on_this_page.py help/using/reports --require
   ```

   Exit code is non-zero on any failure, so it can gate CI.

## Scope / exclusions

Reference and syntax pages are excluded by default (path parts `api-reference`,
`expression`, `functions`). Override with `--exclude ...` if needed.

## Repo-wide progress check

```bash
python scripts/on-this-page/validate_on_this_page.py help
```

Without `--require`, pages still missing a box are reported as `pending` (not a
failure), so you can track rollout progress across the guide.
