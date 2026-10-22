# Generation spec — AI Knowledge Reference blocks

The single source of truth for what an AI Knowledge Reference block contains and how it is
written. Follow it exactly for every page. (This mirrors the legacy
`.claude/commands/augmentedAIContent.md`; the skill is the canonical version.)

## Sources rule

The goal of a block is to help AI tools retrieve the **right** information every time, with
concrete guidance, examples / use cases and best practices. Everything in a block must therefore
come from **the Journey Optimizer documentation** (`help/using/`), never from general product
knowledge, inference, or HTML-commented / commented-out content.

1. **The block's own page body is the primary source.** Start there. Rewording and restructuring
   is fine; adding meaning is not.
2. **Any related AJO docs page may add** concrete guidance, a sample, a use case or a best
   practice, under the **cross-page safety rules** below. Record every related page you used in
   the sync comment (`related: <folder>/<page>.md, ...`).
3. If neither the page nor a related page says it, the block does not either. Report the missing
   information under **Gaps found** (see `SKILL.md`, step 6).

### Cross-page safety rules (no mix-up, no wrong guidance)

- **Same scope.** A fact from a related page applies only if the scope matches: the same feature,
  channel, journeys vs campaigns vs orchestrated campaigns, sandbox / organization level, and
  the same UI (the single Action activity, not the legacy per-channel activities). Never carry a
  limit, status, permission or behavior from one channel or feature to another.
- **The own page wins.** A related page adds to the own page; it never overrides it.
- **Conflicts are flagged, not resolved.** If the own page and a related page (or two related
  pages) disagree, do not pick a side and do not blend them. Use only the own page's version, or
  leave the point out, and flag the discrepancy (see "Page-fix tasks" in `git-jira-tracking.md`).
- **Numbers keep their source.** Copy a number, limit or date exactly from its page, with that
  page's scope and qualifier. Never combine figures from two pages.
- **Prefer the most specific page.** Use the page that is about the topic, not a page that
  mentions it in passing.
- **Say where it comes from when it matters.** When a fact comes from a related page, word it so
  it stays true on its own (name the feature it belongs to) rather than implying the own page says
  it.

## Accordion + include syntax

```
+++ AI Knowledge Reference

Content here — standard markdown.

+++
```

- `+++ AI Knowledge Reference` opens (one space after `+++`); `+++` alone closes.
- Blank line before the opening `+++` and after the closing `+++`.
- The title is always exactly `AI Knowledge Reference`.
- The whole accordion lives in a do-not-localize include and the page pulls it in with
  `{{$include /help/_includes/do-not-localize/<folder>/ai-augmented-<page>.md}}`. Content under
  `help/_includes/do-not-localize/` is excluded from localization — this is how the block stays
  untranslated.

## Include file structure

```
---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

[fixed opening — verbatim]

[the six sections in order]

+++

<!-- ai-section-version: 1 | source-hash: <first 8 chars of md5 of page body> | related: <folder>/<page>.md, ... (only if related pages were used) -->
```

- **Filename:** derive from the page path relative to its top-level `help/using/<folder>/`
  section: strip `.md`, replace any remaining `/` with `-`, prefix with `ai-augmented-`.
  - `help/using/building-journeys/end-journey.md` → `ai-augmented-end-journey.md`
  - `help/using/building-journeys/expression/journey-properties.md` →
    `ai-augmented-expression-journey-properties.md`
- One subfolder per top-level section (`building-journeys/`, `email/`, `data/`, …).

## Fixed opening — verbatim, never modify

Every block begins with these two paragraphs exactly. Copy byte-for-byte; do not paraphrase,
condense, or reorder:

```
This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.
```

## The sections, in order

Six sections are required (skip one only if the page yields nothing for it). Six more are
optional: add each one **only when the docs state the content** (page body or a recorded related
page), and never pad a block to include them. Write sections in this order:

1. TL;DR
2. Intents
3. Glossary
4. Guardrails
5. Prerequisites and permissions *(optional)*
6. Applicability *(optional)*
7. Terminology
8. FAQ
9. Troubleshooting *(optional)*
10. Examples *(optional)*
11. Best practices *(optional)*
12. Related pages *(optional)*

Each fact appears in one section only. If a fact fits two, keep it in the more specific one and
do not repeat it (for example, a permission lives under Prerequisites and permissions, not also
under Guardrails). The FAQ is the exception: its answers may restate a fact in one sentence.

### 1. TL;DR
One sentence: what the page teaches or enables. `* **TL;DR:** [one sentence]`

### 2. Intents
3–6 things a user can accomplish after reading the page.

### 3. Glossary
Key page-specific terms with short definitions; flag product-specific terms with
`*(product-specific)*`. No generic marketing padding.

**Validation-mode precision (mandatory):** if the page covers testing/previewing/simulated
execution, distinguish every mode the page actually names — do not collapse them. Use the
page's exact term (for example `Simulate content`, `Simulate content (AEP profiles)`,
`Send proof`, `Test mode`, `Dry run`, `Simulation`, `test profile`, `sample input`). Never
substitute "synthetic profiles", "fake data", or "without real data" for any of them.

### 4. Guardrails
Limits and constraints stated on the page. Prerequisites and permissions go under their own
section (below).

- **Qualify every numeric limit** as `(hard limit)` or `(recommended)` — but **only** when the
  page uses enforcement wording (error / rejected / maximum / cannot exceed / only … supported)
  or recommendation wording (for best performance / it is recommended). If the page gives no
  qualifier, give none. **Never label a raisable, default, or configurable value as hard.**
  Values that can be raised "by contacting your Adobe representative" or via an API are
  `(default)`, not hard.
- **Qualify every throughput/rate figure with its scope** (per sandbox / per org / per instance).
- **Cross-check every number against the page body.** The page body is authoritative.
- **Do not infer** guardrails the page does not state. No meta-commentary ("the page does not
  specify …").

### 5. Prerequisites and permissions (optional)
What must be in place before the user can do what the page describes: required permissions or
permission names, product add-ons or capabilities, and setup that must already exist. One bullet
per item, with the page's exact names (permission names, add-on names, UI labels).

- State a prerequisite only when the docs present it as required. Do not turn an optional step
  or a recommendation into a prerequisite.
- Keep each item's scope (channel, journeys vs campaigns, sandbox or organization level). Never
  carry a permission or add-on from one feature or channel to another.
- Do not guess which role or product edition grants a permission; name only what the docs name.

### 6. Applicability (optional)
Where the feature applies and where it does not. A short list or table covering only the
dimensions the docs actually state: journeys vs campaigns vs orchestrated campaigns, channels,
sandbox vs organization level, experiences (classic vs redesigned), and deprecated or legacy
variants.

- Each line says **applies** or **does not apply** and names the scope exactly as the docs do.
- Only what the docs state. Absence from the docs is not "does not apply": leave the cell out
  and report it under **Gaps found**.
- A related-page fact must satisfy the cross-page safety rules (same scope, recorded in
  `related:`).
- Do not repeat the channel names or limits already given under Guardrails; point to the scope
  only.

### 7. Terminology
Canonical names, acronyms, variants, synonyms, disambiguation.

- **SMS / Mobile message:** write "Mobile message" for the channel and list SMS as a variant
  (`acronyms.md`, "Terms and distinctions"). Keep "SMS" only for SMS-specific guidance, exact
  UI / permission / credential names, and where SMS is listed next to MMS and RCS.
- **Acronyms:** include one only if it is used on the page body or is on the approved list in
  `acronyms.md` (use the expansion given there). Never invent one. If there is none, omit the
  line; do not write `Acronym: n/a`. Acronyms marked "needs confirmation" in that file are not
  used until a writer confirms them.
- **Synonyms** (`"A" = "B"`) only for **true equivalents** — both forms must appear on the page
  meaning the same thing. Anything that is a *contrast* goes under **Do not confuse**
  (`"X" ≠ "Y"`), not Synonyms.
- **Status/lifecycle precision:** copy exact status labels from the page body; do not
  paraphrase. Use "Do not confuse" to separate statuses that share a root word.

### 8. FAQ
3–6 likely questions with short answers. Answers use the **same verbs and nouns as the page
body**. Do not introduce "revert", "reset", or "roll back" unless the page uses them.

### 9. Troubleshooting (optional)
Documented symptoms and error messages with their documented cause and resolution. One entry
per item: the symptom or error label verbatim (for example
`configuration doesn't exist`, with no `[!UICONTROL ...]` tag), then the cause, then what the docs say to do.

- Copy error strings, status values and UI labels exactly. Do not paraphrase an error label.
- Give the cause and the fix only if the docs give them. If the docs list an error without a
  cause, list the error and the documented context, and report the missing cause under
  **Gaps found**. Never speculate about causes.
- Resolution wording is limited to what the docs say; do not turn it into step-by-step
  instructions (see "What NOT to include").

### 10. Examples (optional)
Concrete samples and use cases the docs give: a short scenario, a sample value or payload, a
typical configuration. Keep each one short and exact, and name the feature it belongs to. Only
what the page or a recorded related page states; never invent an example.

### 11. Best practices (optional)
Recommendations the docs give ("it is recommended", "for best performance", "we recommend"),
each with its scope. Label them as recommendations, not as limits. Only what the docs state.

### 12. Related pages (optional)
Pages the reader should consult next, each with the situation in which to use it ("for X, see
Y"). This guides retrieval to the right page.

- Name each page by its link text on the page. When the link text is generic ("Learn more",
  "this section"), use the target page's title and, if relevant, its section heading. Use the format `* <situation>: <page name> (<folder>/<page>.md)`.
- Include only pages that the page body links to or that are recorded in the `related:` sync
  comment. Do not add pages you only believe are relevant.
- The situation must be stated or clearly implied by the page's own link context. Do not add
  claims about what the target page contains beyond that.
- Do not repeat comparisons already covered under "Do not confuse"; use this section for routing
  only.

## What NOT to include

- Do not rewrite or summarize body content, or give step-by-step instructions.
- Do not invent content unsupported by the docs (the page, or a recorded related page).
- Do not use these imprecise terms unless they appear **verbatim** on the page:
  "synthetic", "fake data", "without real data", "revert", "roll back".
- **No contractions** anywhere in block prose — spell out "is not", "does not", "cannot",
  "it is", etc. (The only exception is a verbatim product UI or error string such as
  `configuration doesn't exist`, which is preserved exactly.)
- **No `[!UICONTROL ...]` or `[!DNL ...]` tags.** Write UI labels and product names as plain text (for example **Modify campaign**,
  not `**[!UICONTROL Modify campaign]**`). When copying a label from the page, strip the tag and
  keep the text and any bold.

## Common generation errors (check each before gate 1)

These are the mistakes the independent verifier most often had to fix. Look for them
deliberately.

- **Imported contrasts or definitions.** "Do not confuse" and Glossary entries must be built
  from what *this page* says. Do not describe a neighbouring feature (for example Test mode or
  Simulation on a Dry run page) from general knowledge. If the page only links to a comparison
  page, say that and stop. Do not define a term the page uses but never explains; report it
  under **Gaps found** instead.
- **Wrong kind of label.** Use the page's own category word: do not call a mode a "status", a
  flag a "boolean field", or a field a "dataset" unless the page does. A "status" is a
  lifecycle value the page names as one.
- **Merged facts.** When the page says A counts towards X and B counts towards Y, keep them
  separate. Do not write "A and B count towards X and Y".
- **Merged behaviours.** If the page gives two activity types different behaviours (for
  example "not executed" versus "disabled, responses set to null"), state each one. Do not
  collapse them into one phrase such as "disabled and not executed".
- **"Only" and "any".** Copy the page's scope word. "Can be used in any Draft journey with no
  error" is not the same claim as "Only Draft journeys with no errors can be used".
- **Invented titles and links.** Name a link by its text on the page, not by the title of the
  target page, unless the page uses that title.
- **Added reassurance or consequences.** Do not add statements such as "no content is lost" or
  "this is safe" that the page does not make.
- **Informal synonyms.** A phrase used once as a verb or in passing (for example "smoke test")
  is not a synonym for a feature name.
- **"<channel> action" or "<channel> activity" in journeys.** The palette has ONE **Action**
  activity (the legacy per-channel activities are deprecated). The user drags it onto the canvas
  and selects the channel as the **action type**. After that, the canvas node shows the label the
  user typed as its title and the **channel name as its type** (for example a node titled "Luma
  email action" whose type is "Email"; the right pane is "Actions: Email" with a "Configure
  action" button). "Channel action" is only a generic term in the docs, not a node name. Write
  "an Action activity with the Email channel selected" or "the Email channel", never "the Email
  action" or "Email activity" as if it were the node's name, even when the page body still says
  so: report that wording under **Gaps found** so the page is fixed. In campaigns the user
  chooses the channel in the campaign's Actions section; keep that wording. Statements that the
  legacy native channel activities (Email, Push, SMS, In-app, Web, Code-based experience,
  Content Card) are deprecated stay as they are. Orchestrated campaigns do use "channel
  activities"; do not change those.
- **FAQ drift.** FAQ questions and answers reuse the page's nouns and verbs ("reporting
  metrics", "quotas"), not paraphrases such as "analytics queries" or "limits".

## Step 3 — verify every claim (self-check, gate 1)

Before writing the include, re-read the generated content claim by claim. Mandatory, even for
short pages. Correct any failure before writing, and log the correction in the report.

- Every term/label/UI name in the block appears in the page body or in a recorded related page.
- No synonym unless both forms appear on the page; every "Do not confuse" references only
  concepts on this page.
- Every numeric value matches the page body exactly; every limit qualifier is justified by the
  page's wording; no invented qualifier.
- No glossary/FAQ detail imported from other pages or general knowledge.
- Every optional section present (Prerequisites and permissions, Applicability, Troubleshooting,
  Related pages) is stated in the docs; an optional section with no support is omitted, not filled.
- No banned imprecise term unless verbatim on the page; no contractions.

## Post-generation checklist (gate 1, continued)

- [ ] Every numeric value exists verbatim / is derivable from the page body.
- [ ] Every limit qualified correctly (hard vs recommended vs none); no default/raisable value
      mislabeled as hard.
- [ ] Every throughput figure has its scope.
- [ ] All validation modes present on the page are named with page-accurate terms.
- [ ] All lifecycle statuses use exact page labels.
- [ ] Synonyms are true equivalents; contrasts are under "Do not confuse".
- [ ] No banned words / no contractions (outside verbatim UI strings).
- [ ] Glossary has no generic terms; FAQ introduces nothing absent from the page.
- [ ] Optional sections appear in the specified order, each fact appears once, and no optional
      section was added without documented support.
- [ ] Prerequisites and permissions: names are exact, scope is kept, nothing optional is listed as
      required.
- [ ] Applicability: every "applies" / "does not apply" is stated in the docs.
- [ ] Troubleshooting: error strings are verbatim and every cause or fix is documented.
- [ ] Related pages: each is linked from the page or recorded in `related:`.

Gate 1 is the author-of-the-block checking their own work. It does **not** replace the
independent verification round (gate 2) in `verification-round.md`.
