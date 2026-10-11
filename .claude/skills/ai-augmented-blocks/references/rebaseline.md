# Re-baselining existing blocks

Use this when `audit.sh` reports DRIFTED or NO-HASH blocks that were written before the current
hash method existed. A stale or missing hash does **not** mean the block is wrong, and a fresh
hash does **not** make a block right. The hash is only written after the block has been
verified against the page.

Never refresh hashes in bulk without verification. Writing today's hash onto an unchecked block
records "verified" when nobody checked.

## Procedure (one folder = one branch = one JIRA task)

1. **Create the task and branch first** (`DOCAC-<key>`), per `git-jira-tracking.md`.
2. **Audit the folder:** `scripts/audit.sh <folder>`. Save the list. Pages labelled CURRENT are
   done; skip them. MISSING pages are CREATE work, not re-baselining; handle them separately.
3. **Triage thin pages.** Skip any page that is only a link hub or near-empty, and any block
   that should not exist. Say why in the report.
4. **Verify in batches.** For the remaining DRIFTED / NO-HASH pages, launch the independent
   verifier subagent from `verification-round.md` (one subagent can cover about 5 to 10 pages;
   keep batches small enough that it reads each page fully). It fixes the block files.
5. **Check the result.** Every page must be reported `clean` (either found nothing or fixed it).
   If the verifier changed more than a few lines of a block, read the diff before continuing.
6. **Write the hash** for each verified page: `scripts/refresh-hash.sh <page.md>`. Bump
   `ai-section-version` by 1 on any block the verifier changed.
7. **Structural sweep** from `git-jira-tracking.md`, then re-run `scripts/audit.sh <folder>`.
   Every in-scope page should now be CURRENT.
8. **Commit, comment on the task, ask about the PR** (never merge).

## Order of work

Start with folders whose pages change least (for example `administration/`), so the baseline
stays valid. Do high-churn folders (for example `building-journeys/`) last, and re-run the audit
right before opening the PR in case pages changed meanwhile.

## Report per folder

Pages verified clean, pages fixed (with the corrections), pages skipped (+ reason), and the
**Gaps found** list for authors (see `SKILL.md`, step 6).

## After the baseline exists

Once a folder is fully CURRENT, any later DRIFTED page means the page was edited after its block
was last verified. Re-verify and refresh that page only (UPDATE mode).
