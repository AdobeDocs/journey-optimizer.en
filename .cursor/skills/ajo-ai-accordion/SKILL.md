---
name: ajo-ai-accordion
description: Enriches Adobe Journey Optimizer documentation pages with an AI Assistant accordion section appended at the end of each markdown file. Reads each page, auto-generates relevant AI Assistant content based on the page topic, and inserts it as a collapsible accordion. Use when the user wants to add AI information to AJO docs, enrich AJO markdown pages with AI content, or process a file or folder of markdown files with AI accordion sections.
disable-model-invocation: true
---

# AJO AI Accordion Enrichment

Appends an auto-generated AI Assistant accordion at the end of one or more markdown files in the Journey Optimizer documentation repository.

## Target repository

`/Users/sauviat/GitHub/GHEC/journey-optimizer.en/help/using/`

## Accordion syntax (Experience League)

```markdown
+++Title of the accordion

Content here — any standard markdown is valid.

+++
```

**Rules:**
- `+++Title` on one line — title immediately follows `+++`, no space between
- `+++` alone on a line closes the accordion
- Blank line before the opening `+++` and after the closing `+++`

---

## Workflow

### Step 1 — Ask for target(s)

Ask the user:

> Which file or folder do you want to enrich?
> - Single file: path relative to repo root (e.g. `help/using/email/get-started-email.md`)
> - Folder: processes all `.md` files inside recursively (e.g. `help/using/email`)
> - List of files/folders

Use `AskQuestion` if available, otherwise ask conversationally.

If a folder is given, list all `.md` files found and confirm with the user before processing.

### Step 2 — For each file: read and generate

For every target file:

1. **Read the file** in full.
2. **Understand the page topic** — what feature, concept, or task does it cover?
3. **Generate the accordion content** using the content generation rules below.
4. **Check** whether an AI accordion already exists at the end of the file (look for `+++` near the end). If it does, ask the user whether to replace or skip.

### Step 3 — Append the accordion

Append at the very end of the file:

```markdown

+++[ACCORDION_TITLE]

[GENERATED_CONTENT]

+++
```

No other content in the file should be modified.

### Step 4 — Report

After all files are processed:
- List files modified ✓
- List files skipped and reason (already has accordion, empty file, not relevant, etc.)

---

## Content generation rules

Generate the accordion content by analysing the markdown page. Produce the following sections **in order**, formatted as markdown bullet lists. Skip any section for which no meaningful content can be extracted from the page.

---

### Accordion title

Use: `+++AI Assistant — Page context`

---

### Sections to generate (in order)

**1. TL;DR**

One sentence. What does this page teach or enable?

```markdown
- **TL;DR:** [one sentence summary]
```

---

**2. Intents**

Bullet list of what a user can accomplish after reading this page (3–6 items).

```markdown
**Intents:**
- [action the user can perform]
- [action the user can perform]
```

---

**3. Glossary**

Key terms specific to this page/feature, with a short definition. Flag product-specific terms.

```markdown
**Glossary:**
- **[Term]**: [definition] *(product-specific)*
- **[Term]**: [definition]
```

Only include terms that are relevant to this page's topic. Do not pad with generic marketing terms.

---

**4. Guardrails**

Limitations, prerequisites, permissions, or constraints mentioned on the page.

```markdown
**Guardrails:**
- [guardrail or prerequisite]
- [guardrail or prerequisite]
```

---

**5. Terminology**

Canonical product names, acronyms, accepted variants, synonyms, and disambiguation hints. This section is primarily for AI pipeline normalisation.

```markdown
**Terminology:**
- Canonical name: [e.g. Adobe Journey Optimizer]
- Acronym: [e.g. AJO] — variants: [e.g. Journey Optimizer, A-JO]
- Synonyms: [e.g. "brand guidelines" = "brand rules", "branding standards"]
- Do not confuse: [e.g. "AI Assistant" ≠ "Adobe Sensei"]
```

Only include entries that are present or implied on the page.

---

**6. FAQ**

3–6 questions a user might ask about the content of this page, with short answers.

```markdown
**FAQ:**
- **Q: [question]** — [short answer]
- **Q: [question]** — [short answer]
```

---

### What NOT to include

- Do **not** rewrite or summarise the body content of the page (it is already there).
- Do **not** include step-by-step instructions (those are in the page).
- Do **not** invent content that is not supported by the page.

---

### Full accordion template

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
- Canonical name: [name]
- Acronym: [acronym] — variants: [variants]

**FAQ:**
- **Q: [question]** — [short answer]

+++
```

---

## Notes

- Process files one by one, not in bulk, to keep generation quality high.
- If the page is very short or purely a redirect/index page, flag it and ask the user if they want to skip it.
- Do not create new files — only edit existing `.md` files.
