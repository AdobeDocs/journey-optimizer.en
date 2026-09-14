---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page provides 16 ready-to-use copy-paste personalization recipes covering dates, arrays, strings, conditional logic, and PQL edge cases for use in Journey Optimizer email, SMS, and push content.

**Intents:**

* Copy ready-to-use date/time patterns (current date, countdown, offset dates, time display, weekend detection)
* Copy array and loop patterns (list items, top N items, conditional per-item rendering)
* Copy string formatting patterns (clean and reuse strings, JSON quoting, uppercase date components)
* Copy conditional logic patterns (multi-branch if/elseif/else, null-safe attribute display)
* Handle PQL edge cases (hyphenated keys, numeric event IDs, type coercion)

**Glossary:**

* **Personalization recipe**: A ready-to-use copy-paste pattern for a common personalization use case, using personalization editor syntax. *(product-specific)*
* **`formatDate`**: A function that converts a date to a string using a specified format pattern (e.g. `"MMMM dd, yyyy"`).
* **`dateDiff`**: A function that computes the numeric difference between two dates.
* **`getCurrentZonedDateTime()`**: A function returning the current date and time in a time-zone-aware format.
* **`topN`**: A PQL function that sorts an array by a specified numeric field in descending order and returns the top N items. Must be assigned via `{% let %}` before use in a Handlebars loop.
* **`{% let %}`**: Handlebars variable assignment syntax for storing computed values; required when a PQL function result needs to be referenced in a subsequent Handlebars context.
* **`replaceAll`**: A string function that replaces all occurrences of a pattern in a string; returns a new string without modifying the original.

**Guardrails:**

* `{{#each}}` is not supported in the journey condition activity; use collection management functions for array filtering in journey conditions.
* Backtick escaping for hyphenated attribute keys is only supported inside PQL expressions (`{%= ... %}`); backticks are not accepted in plain Handlebars interpolation (`{{...}}`).
* `topN` is a PQL function and must be assigned to a `{% let %}` variable before being used as a `{{#each}}` loop target.
* When using a loop variable inside a `{%#if%}` block, declare a named loop alias (e.g. `as |order|`); `this.status` is not resolved by the PQL evaluator inside `{%#if%}`.
* Use lowercase `y` in `formatDate` patterns for calendar year; `Y` (week-based year) may produce unexpected values at year-end boundaries.

**Terminology:**

* **Canonical name:** personalization recipe — variants: pattern, template, example, copy-paste pattern
* **Do not confuse:** `{%= ... %}` (PQL expression syntax — evaluated, returns a computed value) ≠ `{{...}}` (Handlebars interpolation — renders a variable or template expression)
* **Do not confuse:** `{%#if%}` / `{%/if%}` (Journey Optimizer conditional syntax, percent-curly braces) ≠ `{{#if}}` / `{{/if}}` (standard Handlebars conditional syntax)
* **Do not confuse:** `topN(array, field, n)` (sorts by field descending, returns top N) ≠ `head(array)` (returns only the first item from the array)
* **Do not confuse:** `dayOfWeek()` (used in message content to adapt display based on day) ≠ the journey Time condition "Day of the week" option (used in the journey Condition activity to route profiles differently)
* **Do not confuse:** date format pattern `y` (calendar year — correct) ≠ `Y` (week-based year — may produce unexpected results at year boundaries)

**FAQ:**

* **Q: What is the difference between `{%= ... %}` and `{{...}}` in personalization?** — `{%= ... %}` is PQL expression syntax — it is evaluated and returns a computed value (number, string, boolean). `{{...}}` is Handlebars interpolation — it renders a variable or template expression. Both appear in personalization content but serve different purposes.
* **Q: How do I use a PQL function result inside a Handlebars `{{#each}}` loop?** — Assign the PQL function result to a variable using `{% let variableName = pqlFunction(...) %}`, then use `{{#each variableName}}` to iterate over it.
* **Q: Can `{{#each}}` be used in a journey condition activity?** — No. `{{#each}}` is available only in message personalization content (email, SMS, push). For array filtering in journey conditions, use collection management functions.
* **Q: How do I reference a field whose name contains a hyphen?** — Wrap the hyphenated key in backticks inside a PQL expression: ``{%= profile.events.`order-total` > 100 %}``. Backticks are not supported in plain Handlebars interpolation — use a `{% let %}` variable as an intermediate step if needed.
* **Q: Why does `topN` need `{% let %}` before a `{{#each}}` loop?** — `topN` is a PQL function that returns a PQL list. Assigning it to a `{% let %}` variable makes the result available in the Handlebars context so it can be iterated with `{{#each}}`.

+++

<!-- ai-section-version: 1 | source-hash: 20c7ee0f -->
