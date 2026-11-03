---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page demonstrates a complete personalization use case: iterating over nested profile arrays (health plans containing prescriptions) with conditional filtering to display only prescriptions in "ready" or "recall" states in an email.

**Intents:**

* See a rendered output example of a personalized health plan email
* Understand the HTML template using nested `{{#each}}` and `{%#if%}` blocks for conditional array iteration
* Understand the required profile data structure: a `plans` array where each plan contains a `prescriptions` array with `state` fields

**Glossary:**

* **Nested iteration**: Using `{{#each}}` loops inside other `{{#each}}` loops to traverse multi-level array structures in profile data (e.g., plans → prescriptions).
* **Prescription state**: A field on each prescription object indicating its lifecycle status in this use case — values used are "ready", "recall", and "picked up". *(use-case specific)*
* **`{%#if%}` / `{%/if%}`**: Conditional block syntax used within message templates to filter array items during iteration (distinct from the double-curly `{{#if}}` Handlebars syntax).

**Terminology:**

* **Canonical name:** nested array iteration — variants: nested loops, nested each, multi-level iteration
* **Do not confuse:** `{{#each}}` / `{{/each}}` (Handlebars iteration syntax, double curly braces) ≠ `{%#if%}` / `{%/if%}` (conditional syntax, percent-curly braces) — both are used together in this template
* **Do not confuse:** "ready" (prescription available for pickup) ≠ "recall" (prescription has been recalled) ≠ "picked up" (prescription already collected — excluded from the output by the conditional filter)

**FAQ:**

* **Q: Which prescription states are included in the email output?** — Only prescriptions with state "ready" or "recall" are displayed. Prescriptions with state "picked up" are excluded by the `{%#if prescription.state = "ready" or prescription.state = "recall"%}` conditional filter.
* **Q: What profile data structure is required for this use case?** — A profile with a `plans` array, where each plan object contains a `prescriptions` array. Each prescription object must have `prescription_id`, `name`, and `state` fields.
* **Q: How are plans and prescriptions iterated in the template?** — The outer `{{#each profile.plans as |plan|}}` loop iterates over each health plan. Inside it, `{{#each plan.prescriptions as |prescription|}}` iterates over each plan's prescriptions, and a conditional block filters to only "ready" or "recall" states.

+++

<!-- ai-section-version: 1 | source-hash: 4b68d597 -->
