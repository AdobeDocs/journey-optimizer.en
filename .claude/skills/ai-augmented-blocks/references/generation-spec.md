# Generation spec — AI Knowledge Reference blocks

The single source of truth for what an AI Knowledge Reference block contains and how it is
written. Follow it exactly for every page. (This mirrors the legacy
`.claude/commands/augmentedAIContent.md`; the skill is the canonical version.)

## Golden rule

A block may contain **only what is derivable from its own page body.** Not other pages, not
general product knowledge, not HTML-commented / commented-out content. If the page does not say
it, the block does not either.

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

<!-- ai-section-version: 1 | source-hash: <first 8 chars of md5 of page body> -->
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

## The six sections, in order

Skip a section only if the page yields no meaningful content for it.

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
Limits, prerequisites, permissions, constraints stated on the page.

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

### 5. Terminology
Canonical names, acronyms, variants, synonyms, disambiguation.

- **Synonyms** (`"A" = "B"`) only for **true equivalents** — both forms must appear on the page
  meaning the same thing. Anything that is a *contrast* goes under **Do not confuse**
  (`"X" ≠ "Y"`), not Synonyms.
- **Status/lifecycle precision:** copy exact status labels from the page body; do not
  paraphrase. Use "Do not confuse" to separate statuses that share a root word.

### 6. FAQ
3–6 likely questions with short answers. Answers use the **same verbs and nouns as the page
body**. Do not introduce "revert", "reset", or "roll back" unless the page uses them.

## What NOT to include

- Do not rewrite or summarize body content, or give step-by-step instructions.
- Do not invent content unsupported by the page.
- Do not use these imprecise terms unless they appear **verbatim** on the page:
  "synthetic", "fake data", "without real data", "revert", "roll back".
- **No contractions** anywhere in block prose — spell out "is not", "does not", "cannot",
  "it is", etc. (The only exception is a verbatim product UI string such as
  `[!UICONTROL configuration doesn't exist]`, which is preserved exactly.)

## Step 3 — verify every claim (self-check, gate 1)

Before writing the include, re-read the generated content claim by claim. Mandatory, even for
short pages. Correct any failure before writing, and log the correction in the report.

- Every term/label/UI name in the block appears in the page body.
- No synonym unless both forms appear on the page; every "Do not confuse" references only
  concepts on this page.
- Every numeric value matches the page body exactly; every limit qualifier is justified by the
  page's wording; no invented qualifier.
- No glossary/FAQ detail imported from other pages or general knowledge.
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

Gate 1 is the author-of-the-block checking their own work. It does **not** replace the
independent verification round (gate 2) in `verification-round.md`.
