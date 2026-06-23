# augmentedAIContent

Appends an auto-generated AI Assistant accordion at the end of one or more markdown files in the Journey Optimizer documentation repository.

## Target repository

`help/using/` (relative to repo root)

## Accordion syntax (Experience League)

```
+++Title of the accordion

Content here — any standard markdown is valid.

+++
```

**Rules:**
- `+++Title` on one line — title immediately follows `+++`
- `+++` alone on a line closes the accordion
- Blank line before the opening `+++` and after the closing `+++`

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
3. **Generate the accordion content** using the rules below.
4. **Check** whether an AI accordion already exists at the end (look for `+++AI Assistant` near the end). If yes, ask the user: replace or skip?

### Step 3 — Append the accordion

Append at the very end of the file. Do not modify any other content.

### Step 4 — Report

- Files modified ✓
- Files skipped + reason (already has accordion / empty / index page)

---

## Content generation rules

Analyse the page and produce the sections below **in order** as markdown bullet lists. Skip sections where no meaningful content can be extracted.

### Accordion title

`+++AI Assistant — Page context`

### 1. TL;DR

One sentence summary of what the page teaches or enables.

```
- **TL;DR:** [one sentence]
```

### 2. Intents

3–6 things a user can accomplish after reading this page.

```
**Intents:**
- [action]
- [action]
```

### 3. Glossary

Key terms specific to this page/feature with short definitions. Flag product-specific terms.

```
**Glossary:**
- **[Term]**: [definition] *(product-specific)*
```

Only include terms relevant to this page. Do not pad with generic marketing terms.

### 4. Guardrails

Limitations, prerequisites, permissions, or constraints mentioned on the page.

```
**Guardrails:**
- [guardrail]
```

### 5. Terminology

Canonical names, acronyms, accepted variants, synonyms, disambiguation. Primarily for AI pipeline normalisation.

```
**Terminology:**
- Canonical name: [name] — Acronym: [acronym] — variants: [list]
- Synonyms: "[term A]" = "[term B]"
- Do not confuse: "[term]" ≠ "[other term]"
```

### 6. FAQ

3–6 questions a user might ask, with short answers.

```
**FAQ:**
- **Q: [question]** — [short answer]
```

### What NOT to include

- Do **not** rewrite or summarise body content (it is already in the page)
- Do **not** include step-by-step instructions
- Do **not** invent content not supported by the page

### Full template

```markdown

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

- **TL;DR:** [one sentence]

**Intents:**
- [intent]

**Glossary:**
- **[Term]**: [definition]

**Guardrails:**
- [guardrail]

**Terminology:**
- Canonical name: [name] — Acronym: [acronym] — variants: [variants]
- Synonyms: "[a]" = "[b]"
- Do not confuse: "[x]" ≠ "[y]"

**FAQ:**
- **Q: [question]** — [short answer]

+++
```

---

## Notes

- Process files one by one for quality.
- Flag very short or index-only pages and ask the user whether to skip.
- Do not create new files — only edit existing `.md` files.
