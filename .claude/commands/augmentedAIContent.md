# augmentedAIContent

Appends an auto-generated **Quick reference** section at the end of one or more markdown files in the Journey Optimizer documentation repository.

## Target repository

`help/using/` (relative to repo root)

## Section and tab syntax (Experience League)

### Section heading

```
## Quick reference {#quick-reference}
```

### Tabs

```
>[!BEGINTABS]

>[!TAB Tab name]

Content here — any standard markdown is valid.

>[!TAB Another tab]

Content here.

>[!ENDTABS]
```

**Rules:**

- `>[!BEGINTABS]` and `>[!ENDTABS]` each on their own line, surrounded by blank lines
- `>[!TAB Name]` on its own line, followed by a blank line before content
- Tab names are title-case, short (1–3 words)
- Blank line before `>[!BEGINTABS]` and after `>[!ENDTABS]`

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
3. **Generate the section content** using the content generation rules below.
4. **Run the post-generation validation checklist** (see below) — do not skip.
5. **Check** whether a Quick reference section already exists at the end (look for `## Quick reference` near the end). If yes, ask the user: replace or skip?

### Step 3 — Verify every claim against the page body

Before appending, re-read the generated section claim by claim. This step is **mandatory and cannot be skipped**, even for short files. Correct any failure before proceeding to Step 4.

**Terminology and labels**

- [ ] Every term, label, and UI name in the section appears in the page body — not imported from another page or inferred from general product knowledge
- [ ] No synonym is listed unless both forms appear on the page
- [ ] Every "Do not confuse" entry references only concepts mentioned on this page

**Guardrails and limits**

- [ ] Every numeric value matches the page body exactly
- [ ] A limit is called **hard** only if the page body uses that word or clearly implies the system enforces it (e.g., "cannot exceed", "maximum … allowed", "only … supported")
- [ ] A limit is called **recommended** only if the page body uses that word or an equivalent ("for best performance", "it is recommended")
- [ ] If the page body gives no qualifier, the section gives none — do not invent one
- [ ] No meta-commentary about what the source page does or does not say (e.g., "no specific number is stated on this page")

**Glossary definitions**

- [ ] No definition contains technical detail absent from the page body
- [ ] No entry elaborates using information from other pages in the documentation set

**FAQ answers**

- [ ] Every specific detail (UI affordances, button names, field names, step sequences) is stated in the page body — not inferred or imported from other pages
- [ ] No answer introduces information the page body does not address

**Correction rule:** If any check fails, correct the content **before** appending. Log every correction in the Step 5 report.

---

### Step 4 — Append the section

Use the fixed opening block and full template defined in the **Content generation rules** below. Append at the very end of the file, followed immediately by the sync comment:

```
<!-- ai-section-version: 1 | source-hash: [first 8 chars of MD5 of file content before section] -->
```

This comment allows future tooling and writers to detect when the page body has drifted from the section. Do not modify any other content.

### Step 5 — Report

- Files modified ✓
- Files skipped + reason (already has section / empty / index page)
- Any validation warnings raised during Step 2

---

## Content generation rules

Analyse the page and produce the tabs below **in order**. Skip a tab entirely if no meaningful content can be extracted for it.

### Section heading and fixed opening — verbatim, do not modify

Every Quick reference section must begin with this exact block. Copy it as-is; do not paraphrase, condense, or reorder:

```
## Quick reference {#quick-reference}

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.
```

The `>[!BEGINTABS]` block follows immediately after these two paragraphs.

### Tab 1 — Overview

One-sentence TL;DR summary of what the page teaches or enables, followed by 3–6 things a user can accomplish after reading this page.

```
>[!TAB Overview]

**TL;DR**

[one sentence]

**Intents**

* [action]
* [action]
```

### Tab 2 — Glossary

Key terms specific to this page/feature with short definitions. Flag product-specific terms.

```
>[!TAB Glossary]

* **[Term]**: [definition] *(product-specific)*
```

Only include terms relevant to this page. Do not pad with generic marketing terms.

**Validation mode precision rule — mandatory:**
If the page covers any form of testing, previewing, or simulated execution, you MUST distinguish between all modes the page actually describes. Do not collapse distinct modes into a single shorthand entry:
- **Simulation** — renders message content without sending; uses real profiles
- **Test mode** — sends to designated test profiles only; uses persistent AEP test profiles (not synthetic or fake profiles)
- **Dry run** — executes the full journey logic without activating actions; uses real audience data

Include only the modes present in the page. Copy the product-accurate term from the page body — do not substitute "synthetic profiles", "fake data", or "without real data" for any of these.

### Tab 3 — Terminology

Canonical names, acronyms, accepted variants, synonyms, disambiguation. Primarily for AI pipeline normalisation.

```
>[!TAB Terminology]

* **Canonical name:** [name] — Acronym: [acronym] — variants: [list]
* **Synonyms:** "[term A]" = "[term B]"
* **Do not confuse:** "[term]" ≠ "[other term]"
```

**Status and lifecycle precision rule:**
When the page describes a lifecycle (journey statuses, message statuses, campaign states, etc.), copy the exact status labels from the page body. Do not paraphrase. Use "Do not confuse" entries to disambiguate statuses that share a root word but have distinct meaning. Example:

```
* Do not confuse: "Stop" (user-initiated action) ≠ "Stopped" (resulting status) ≠ "Close" (action on Live journey allowing in-progress profiles to finish) ≠ "Closed" (resulting status)
```

### Tab 4 — Guardrails & Limitations

Limitations, prerequisites, permissions, or constraints mentioned on the page.

```
>[!TAB Guardrails & Limitations]

* [guardrail]
```

**Guardrail precision rules — mandatory:**

- **Qualify every numeric limit** as either recommended or hard. Example: "Maximum 10 dataset lookups per message (hard limit)" not "Maximum 10 dataset lookups".
- **Qualify every throughput or rate figure** with its scope. Example: "150,000 messages/hour TPS cap (per sandbox)" not "150,000 messages/hour cap".
- **Cross-check every guardrail against the page body** before including it. If the page says 10 and the section would say 5, the section is wrong. The page body is authoritative.
- **Do not infer guardrails** that are not stated on the page. If a constraint exists but the page does not state it, omit it.

### Tab 5 — FAQ

3–6 questions a user might ask, with short answers. Format each as a bold question heading followed by a paragraph answer.

```
>[!TAB FAQ]

**Q: [question]**

[short answer]
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

Run this checklist on every section before appending. Flag any failure to the user before proceeding.

### Guardrail check

- [ ] Every numeric value in the section exists verbatim or is derivable from the page body
- [ ] Every limit is qualified as recommended or hard
- [ ] Every throughput figure includes its scope (sandbox / org / instance)

### Terminology check
- [ ] All validation modes (Simulation, Test mode, Dry run) present in the page are included and named with page-accurate terms
- [ ] All lifecycle statuses use the exact labels from the page body
- [ ] No imprecise verbs in FAQ answers ("revert", "synthetic", "fake data", "without real data") unless present verbatim in page

### Scope check
- [ ] Glossary does not contain generic marketing terms unrelated to the page
- [ ] FAQ answers do not introduce information absent from the page

If any check fails, correct the section before appending. Log the correction in the Step 4 report.

---

## Sync responsibility

The Quick reference section is a derivative of the page body at a point in time. It must be treated as part of the page.

**When the page body is updated (release PRs, corrections, etc.):**

- If the update changes any guardrail, limit, status label, or validation mode described in the section → regenerate or manually update the section in the same PR.
- If the update is unrelated to section content (e.g. procedure steps, screenshot updates) → the section may remain unchanged, but review it briefly.

The sync comment appended after the section (`<!-- ai-section-version -->`) is the signal: if the file content before the section has changed since that hash was written, the section is a candidate for review.

---

## Full template

```markdown

## Quick reference {#quick-reference}

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

>[!BEGINTABS]

>[!TAB Overview]

**TL;DR**

[one sentence]

**Intents**

* [intent]

>[!TAB Glossary]

* **[Term]**: [definition] *(product-specific)*

>[!TAB Terminology]

* **Canonical name:** [name] — Acronym: [acronym] — variants: [variants]
* **Synonyms:** "[a]" = "[b]"
* **Do not confuse:** "[x]" ≠ "[y]"

>[!TAB Guardrails & Limitations]

* [guardrail — type: recommended|hard — scope: sandbox|org]

>[!TAB FAQ]

**Q: [question]**

[short answer]

>[!ENDTABS]

<!-- ai-section-version: 1 | source-hash: [hash] -->
```

## Notes

- Process files one by one for quality.
- Flag very short or index-only pages and ask the user whether to skip.
- Do not create new files — only edit existing `.md` files.
- The post-generation validation checklist is not optional. Run it for every file, including bulk operations.
