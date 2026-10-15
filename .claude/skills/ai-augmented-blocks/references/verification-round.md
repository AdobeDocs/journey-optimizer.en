# Verification round — the mandatory final quality gate

This is gate 2 of 2 and the step that guarantees each block is **valid, true, and free of
ambiguity**. It is **not optional and cannot be skipped**, including for single-page updates.

## Why it is separate

The block author (gate 1) is too close to the block to catch their own grounding errors. Gate 2
is an **independent adversarial re-check**: a fresh reviewer that assumes the block may be wrong
and tries to prove it, using the page body, and the related pages the block records, as truth. Run it as a **separate subagent**
that has not seen how the block was written — this independence is what makes it effective. For
a batch of pages, one verifier subagent can cover the whole folder.

## What the verifier does, per page

1. Read the **full source page** `help/using/<folder>/<page>.md`. HTML-comment /
   commented-out content is **not** valid source.
2. Read the **block** `help/_includes/do-not-localize/<folder>/ai-augmented-<page>.md`.
3. Classify **every** claim as GROUNDED / INACCURATE / NOT-GROUNDED against the page body, or
   against a related page recorded in the sync comment (`related:`). Go **line by line** through
   every TL;DR, intent, glossary entry, guardrail, terminology line, FAQ question and answer,
   example, best practice, prerequisite, applicability line, troubleshooting entry and related-page
   entry. A line is grounded only if every fact in it is stated in the page
   body or in a recorded related page, possibly reworded. Wording that exists only in a
   contextual-help block, a front-matter field or an HTML comment is not grounded.
   For every fact taken from a related page: open that page and confirm the fact, confirm the
   **scope matches** (feature, channel, journeys / campaigns, UI), and search the docs for a
   conflicting statement (own page, other related pages). Report any conflict; do not resolve it
   in the block.
4. **Fix every issue by editing only the block file** — preserve the two fixed opening
   paragraphs, the `+++ … +++` fences, and the sync comment. Never modify the source page.
5. Report per page: `clean` or `N issues` + the exact fixes applied.

## The adversarial checklist (highest-risk items first)

- **Numbers and limits.** Every value exact. A limit is `(hard limit)` only if the page uses
  enforcement/maximum wording; `(default)` if raisable/default/configurable (including "request
  more via your Adobe representative" or "raisable via API"); `(recommended)` for advice; no
  qualifier if the page gives none. **Downgrade any cap the generator over-labeled as hard.**
  Every throughput/rate figure carries its scope.
- **Dates, IDs, product/field names, SQL identifiers, status enums, error strings** — verbatim
  from the page. Zero tolerance on compliance/legal timeframes: never invent an SLA, retention,
  or enforcement date; keep any date exactly as the page states it and labeled as the page
  frames it.
- **Synonyms vs Do not confuse.** A Synonym (`"A" = "B"`) requires both forms on the page
  meaning the same thing. Any contrast (`"X" ≠ "Y"`) belongs under "Do not confuse". Move
  mislabels.
- **Validation / test modes** named with the page's exact terms, not conflated across
  classic-vs-redesigned experiences or across channels.
- **Grounding.** Nothing imported from another page, general product knowledge, or an HTML
  comment. Remove anything the page body does not support.
- **Cross-page safety.** Every related-page fact is recorded in `related:`, has the same scope
  as where the block uses it, and does not contradict the own page or another page. Conflicts are
  flagged under Gaps found, and the block keeps only the own page's version.
- **Examples and best practices.** Each is stated in the docs (own or recorded related page),
  concrete and exact, and is labeled as an example or a recommendation, not a limit.
- **Prerequisites and permissions.** Each item is stated as required in the docs; names (permissions,
  add-ons, UI labels) are exact; scope is kept; nothing optional or recommended is listed as
  required; no role or edition is guessed.
- **Applicability.** Every "applies" / "does not apply" is stated in the docs for that exact scope
  (journeys vs campaigns vs orchestrated campaigns, channel, sandbox or organization level, classic
  vs redesigned). Silence in the docs is not "does not apply". Remove anything inferred.
- **Troubleshooting.** Error strings, statuses and UI labels are verbatim. Every cause and fix is
  in the docs; remove any speculated cause. An error with no documented cause is listed without
  one and reported under Gaps found.
- **Related pages.** Every entry is linked from the page or recorded in `related:`, the page
  exists, and the stated situation is supported by the link context, not by assumptions about the
  target page.
- **Duplication.** A fact appears in one section only (for example, a permission is not repeated
  under Guardrails).
- **Style.** No contractions (outside verbatim `[!UICONTROL ...]` / `[!DNL ...]` strings). None
  of the banned words ("synthetic", "fake data", "without real data", "revert", "roll back")
  unless verbatim on the page. UI strings preserved exactly.
- **Common generation errors.** Also check the list in `generation-spec.md` ("Common generation
  errors"): imported contrasts, wrong category labels (mode versus status), merged facts or
  behaviours, "only" versus "any", invented link titles, added reassurance, informal synonyms, and "<channel> action" or
  "<channel> activity" in journeys (must be an Action activity with the channel selected; see
  `generation-spec.md`).
- **Acronyms.** Each acronym is used on the page body or is on the approved list in
  `acronyms.md` with the listed expansion. Remove any other. Do not delete an approved acronym
  just because the page body does not use it. No `Acronym: n/a` lines.
- **Structure.** Two fixed opening paragraphs intact and verbatim; the six required sections present
  and in order where the page supports them; optional sections (Prerequisites and permissions,
  Applicability, Troubleshooting, Examples, Best practices, Related pages) present only when the
  docs support them, and in the order given in `generation-spec.md`; sync comment present.

## Reusable verifier subagent prompt

Fill in the folder and page list. Launch it as an independent general-purpose subagent.

```
You are an ADVERSARIAL fact-checker for Adobe Journey Optimizer doc "AI Knowledge Reference"
blocks. Repo: <repo path>. Assume each block MAY contain errors; try hard to find them. This is
the final accuracy gate.

PAGES (basenames): <p1> <p2> ...
SOURCE: help/using/<folder>/<p>.md   BLOCK: help/_includes/do-not-localize/<folder>/ai-augmented-<p>.md

For EACH page:
1. Read the FULL source page body (HTML-comment / commented-out content is NOT valid source).
2. Read the block.
3. Classify EVERY claim GROUNDED / INACCURATE / NOT-GROUNDED against the page body. Scrutinize:
   numeric limits (hard only if the page uses enforcement/maximum wording; downgrade any
   raisable/default/configurable value the block marked hard; every rate figure needs its
   scope); dates/IDs/field names/SQL identifiers/status enums/error strings verbatim and no
   invented SLA/legal timeframes; Synonyms are true equivalents (mislabels -> Do not confuse);
   prerequisites/permissions, applicability lines, troubleshooting causes and fixes, and related-page
   entries each stated in the page or a recorded related page (never inferred);
   validation/test modes named with the page's exact terms and not conflated; nothing imported
   from other pages or HTML comments; no contractions (outside verbatim [!UICONTROL ...]); no
   banned words (synthetic / fake data / without real data / revert / roll back) unless verbatim.
4. FIX every issue by editing ONLY the block file. Preserve the two fixed opening paragraphs,
   the +++ ... +++ fences, and the sync comment. Do NOT modify source pages.

Report per page: "<p>: clean" or "<p>: N issues" + the exact fixes applied.
```

## Exit criteria

The folder passes gate 2 only when the verifier reports every page as `clean` (either it found
nothing, or it applied fixes and the block is now clean). If it applied fixes, they are already
in the block files — include them in the final report and proceed to the sweep and commit.
