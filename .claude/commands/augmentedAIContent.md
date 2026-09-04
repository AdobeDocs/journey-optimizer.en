# augmentedAIContent

Generates an auto-created **AI Knowledge Reference** accordion for one or more markdown pages in the Journey Optimizer documentation repository, and stores it as a **non-localized include** so it is not translated.

## Target repository

`help/using/` (relative to repo root)

## Accordion syntax (Experience League)

```
+++ AI Knowledge Reference

Content here — any standard markdown is valid.

+++
```

**Rules:**

- `+++ AI Knowledge Reference` opens the accordion (one space after `+++`); `+++` alone on a line closes it
- Blank line before the opening `+++` and after the closing `+++`
- The title is always exactly `AI Knowledge Reference`

## Include syntax (Experience League)

```
{{$include /help/_includes/do-not-localize/<folder>/<include-file>.md}}
```

Content pulled in via `{{$include}}` from `help/_includes/do-not-localize/` is **excluded from localization** — this is how the block stays untranslated.

---

## Workflow

### Step 1 — Ask for target(s)

Ask the user:
> Which file or folder do you want to enrich?
> - Single file: path relative to repo root (e.g. `help/using/email/get-started-email.md`)
> - Folder: all `.md` files recursively (e.g. `help/using/email`)
> - List of files/folders

If a folder is given, list the `.md` files found and confirm before processing.

### Step 2 — For each file: read and generate

1. **Read the file** in full.
2. **Understand the page topic** — what feature, concept, or task does it cover?
3. **Generate the block content** using the content generation rules below.
4. **Run the post-generation validation checklist** (see below) — do not skip.
5. **Check** whether an AI Knowledge Reference block already exists — either inline (`+++ AI Knowledge Reference` near the end) or already externalized (an `{{$include /help/_includes/do-not-localize/.../ai-augmented-...}}` line). If yes, ask the user: replace or skip? On replace, overwrite the include file (and if the block was still inline, remove the inline block and add the include line instead).

### Step 3 — Verify every claim against the page body

Before writing the block, re-read the generated content claim by claim. This step is **mandatory and cannot be skipped**, even for short files. Correct any failure before proceeding to Step 4.

**Terminology and labels**

- [ ] Every term, label, and UI name in the block appears in the page body — not imported from another page or inferred from general product knowledge
- [ ] No synonym is listed unless both forms appear on the page
- [ ] Every "Do not confuse" entry references only concepts mentioned on this page

**Guardrails and limits**

- [ ] Every numeric value matches the page body exactly
- [ ] A limit is called **hard** only if the page body uses that word or clearly implies the system enforces it (e.g., "cannot exceed", "maximum … allowed", "only … supported")
- [ ] A limit is called **recommended** only if the page body uses that word or an equivalent ("for best performance", "it is recommended")
- [ ] If the page body gives no qualifier, the block gives none — do not invent one
- [ ] No meta-commentary about what the source page does or does not say (e.g., "no specific number is stated on this page")

**Glossary definitions**

- [ ] No definition contains technical detail absent from the page body
- [ ] No entry elaborates using information from other pages in the documentation set

**FAQ answers**

- [ ] Every specific detail (UI affordances, button names, field names, step sequences) is stated in the page body — not inferred or imported from other pages
- [ ] No answer introduces information the page body does not address

**Correction rule:** If any check fails, correct the content **before** writing the block. Log every correction in the Step 5 report.

---

### Step 4 — Write the block to a do-not-localize include, then include it

The generated block must **not be localized**, so it is not written inline in the page. Instead it lives in a separate include file under `help/_includes/do-not-localize/`, which is excluded from translation, and the page pulls it in with `{{$include}}`. (This is the DOCAC-15581 convention.)

**a. Derive the include filename** from the page path relative to its top-level section folder under `help/using/`: strip the `.md` extension, replace any remaining `/` with `-`, and prefix with `ai-augmented-`. This flattening keeps the flat include directory collision-free.

Examples (section `building-journeys`):

| Page | Include file |
|---|---|
| `help/using/building-journeys/end-journey.md` | `ai-augmented-end-journey.md` |
| `help/using/building-journeys/expression/journey-properties.md` | `ai-augmented-expression-journey-properties.md` |

**b. Write the include file** at `help/_includes/do-not-localize/<section-folder>/<include-file>` (create the `<section-folder>` subdirectory if it does not exist — one subfolder per top-level AJO section, e.g. `building-journeys/`, `email/`). Use exactly this structure — `title` frontmatter, an `# AI Knowledge Reference` heading, the complete accordion from the **Full template** below, then the sync comment:

```
---
title: AI Knowledge Reference
---
# AI Knowledge Reference

[complete "+++ AI Knowledge Reference" accordion from the Full template below]

<!-- ai-section-version: 1 | source-hash: [first 8 chars of MD5 of the including page's body, excluding the {{$include}} line] -->
```

**c. Add the include call** as the last line of the page, preceded by a blank line. Do not modify any other page content:

```
{{$include /help/_includes/do-not-localize/<section-folder>/<include-file>}}
```

The sync comment still enables drift detection: the source-hash is computed over the including page's body, so future tooling and writers can tell when the page has drifted from the block. Two files change per page: the **include file** (created) and the **page** (one `{{$include}}` line added).

### Step 5 — Report

- Files modified ✓ (include file created + page's `{{$include}}` line)
- Files skipped + reason (already has block / empty / index page)
- Any validation warnings raised during Step 2

---

## Content generation rules

Analyse the page and produce the sections below **in order** inside the accordion. Skip a section entirely if no meaningful content can be extracted for it.

### Fixed opening — verbatim, do not modify

Every AI Knowledge Reference accordion must begin with this exact block. Copy it as-is; do not paraphrase, condense, or reorder:

```
+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.
```

The page-specific sections below follow immediately after these two paragraphs, still inside the same accordion. (The whole accordion is written into the do-not-localize include file, per Step 4 — not inline in the page.)

### 1. TL;DR

One sentence: what does this page teach or enable?

```
* **TL;DR:** [one sentence]
```

### 2. Intents

3–6 things a user can accomplish after reading this page.

```
**Intents:**

* [action]
* [action]
```

### 3. Glossary

Key terms specific to this page/feature with short definitions. Flag product-specific terms.

```
**Glossary:**

* **[Term]**: [definition] *(product-specific)*
```

Only include terms relevant to this page. Do not pad with generic marketing terms.

**Validation mode precision rule — mandatory:**
If the page covers any form of testing, previewing, or simulated execution, you MUST distinguish between all modes the page actually describes. Do not collapse distinct modes into a single shorthand entry:
- **Simulation** — renders message content without sending; uses real profiles
- **Test mode** — sends to designated test profiles only; uses persistent AEP test profiles (not synthetic or fake profiles)
- **Dry run** — executes the full journey logic without activating actions; uses real audience data

Include only the modes present in the page. Copy the product-accurate term from the page body — do not substitute "synthetic profiles", "fake data", or "without real data" for any of these.

### 4. Guardrails

Limitations, prerequisites, permissions, or constraints mentioned on the page.

```
**Guardrails:**

* [guardrail]
```

**Guardrail precision rules — mandatory:**

- **Qualify every numeric limit** as either recommended or hard. Example: "Maximum 10 dataset lookups per message (hard limit)" not "Maximum 10 dataset lookups".
- **Qualify every throughput or rate figure** with its scope. Example: "150,000 messages/hour TPS cap (per sandbox)" not "150,000 messages/hour cap".
- **Cross-check every guardrail against the page body** before including it. If the page says 10 and the block would say 5, the block is wrong. The page body is authoritative.
- **Do not infer guardrails** that are not stated on the page. If a constraint exists but the page does not state it, omit it.

### 5. Terminology

Canonical names, acronyms, accepted variants, synonyms, disambiguation. Primarily for AI pipeline normalisation.

```
**Terminology:**

* Canonical name: [name] — Acronym: [acronym] — variants: [list]
* Synonyms: "[term A]" = "[term B]"
* Do not confuse: "[term]" ≠ "[other term]"
```

**Status and lifecycle precision rule:**
When the page describes a lifecycle (journey statuses, message statuses, campaign states, etc.), copy the exact status labels from the page body. Do not paraphrase. Use "Do not confuse" entries to disambiguate statuses that share a root word but have distinct meaning. Example:

```
* Do not confuse: "Stop" (user-initiated action) ≠ "Stopped" (resulting status) ≠ "Close" (action on Live journey allowing in-progress profiles to finish) ≠ "Closed" (resulting status)
```

### 6. FAQ

3–6 questions a user might ask, with short answers.

```
**FAQ:**

* **Q: [question]** — [short answer]
```

**FAQ precision rule:**
Answers must use the same verb and noun choices as the page body. Do not introduce verbs like "revert", "reset", or "roll back" unless the page uses them. If a transition ends a session (e.g. exiting test mode returns the journey to its prior state), say exactly that — do not say "the journey reverts to Draft".

### What NOT to include

- Do **not** rewrite or summarise body content (it is already in the page)
- Do **not** include step-by-step instructions
- Do **not** invent content not supported by the page
- Do **not** use the following imprecise terms unless they appear verbatim in the page body: "synthetic", "fake data", "without real data", "revert", "roll back" (when describing product state transitions)

---

## Post-generation validation checklist

Run this checklist on every block before writing the include. Flag any failure to the user before proceeding.

### Guardrail check

- [ ] Every numeric value in the block exists verbatim or is derivable from the page body
- [ ] Every limit is qualified as recommended or hard
- [ ] Every throughput figure includes its scope (sandbox / org / instance)

### Terminology check
- [ ] All validation modes (Simulation, Test mode, Dry run) present in the page are included and named with page-accurate terms
- [ ] All lifecycle statuses use the exact labels from the page body
- [ ] No imprecise verbs in FAQ answers ("revert", "synthetic", "fake data", "without real data") unless present verbatim in page

### Scope check
- [ ] Glossary does not contain generic marketing terms unrelated to the page
- [ ] FAQ answers do not introduce information absent from the page

If any check fails, correct the block before writing the include. Log the correction in the Step 5 report.

---

## Sync responsibility

The AI Knowledge Reference block is a derivative of the page body at a point in time. It must be treated as part of the page.

**When the page body is updated (release PRs, corrections, etc.):**

- If the update changes any guardrail, limit, status label, or validation mode described in the block → regenerate or manually update the block in the same PR.
- If the update is unrelated to block content (e.g. procedure steps, screenshot updates) → the block may remain unchanged, but review it briefly.

The sync comment inside the include file (`<!-- ai-section-version -->`) is the signal: if the including page's body has changed since that hash was written, the block is a candidate for review. When updating, edit the include file under `help/_includes/do-not-localize/`, not the page.

---

## Full template

Include file (`help/_includes/do-not-localize/<section-folder>/ai-augmented-<page>.md`):

```markdown
---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** [one sentence]

**Intents:**

* [intent]

**Glossary:**

* **[Term]**: [definition] *(product-specific)*

**Guardrails:**

* [guardrail — qualify each numeric limit as recommended|hard, each throughput figure with scope sandbox|org]

**Terminology:**

* Canonical name: [name] — Acronym: [acronym] — variants: [variants]
* Synonyms: "[a]" = "[b]"
* Do not confuse: "[x]" ≠ "[y]"

**FAQ:**

* **Q: [question]** — [short answer]

+++

<!-- ai-section-version: 1 | source-hash: [hash] -->
```

Line added to the page:

```
{{$include /help/_includes/do-not-localize/building-journeys/ai-augmented-end-journey.md}}
```

## Notes

- Process files one by one for quality.
- Flag very short or index-only pages and ask the user whether to skip.
- The only new file created per page is its do-not-localize include (Step 4); the page itself is edited only to add the single `{{$include}}` line. Do not otherwise create or restructure files.
- The post-generation validation checklist is not optional. Run it for every file, including bulk operations.
