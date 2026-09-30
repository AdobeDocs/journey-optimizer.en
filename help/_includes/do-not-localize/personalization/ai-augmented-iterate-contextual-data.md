---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to use Handlebars `{{#each}}` syntax to loop over arrays from contextual sources — events, custom action responses, dataset lookups, and technical properties — in message personalization, and how to work with arrays in journey expression syntax when configuring journey activities.

**Intents:**

* Iterate over event array data (e.g., cart items, order items) in message personalization using `{{#each}}`
* Iterate over custom action response arrays (e.g., product recommendations) in messages
* Iterate over dataset lookup result arrays in messages
* Combine data from multiple contextual sources in a single personalized message
* Pass array values to custom action parameters using journey expression syntax
* Use arrays as lookup keys in Dataset Lookup activities
* Apply best practices for empty array fallbacks, variable naming, performance, and expression fragment scoping

**Glossary:**

* **Handlebars**: A templating language used in Journey Optimizer message personalization for iteration (`{{#each}}`) and conditional rendering (`{{#if}}`). *(product-specific)*
* **`{{#each}}` helper**: Handlebars syntax for iterating over an array; each iteration exposes the current item via a named variable (e.g., `|product|`). *(product-specific)*
* **Contextual data**: Data available at message send time from journey sources — events, custom action responses, dataset lookups, and journey technical properties — as opposed to static profile attributes. *(product-specific)*
* **`currentEventField`**: A reference used in journey expressions (not Handlebars) to refer to each item in an event array during filtering or mapping operations.
* **`currentActionField`**: Used in journey expressions to refer to each item in a custom action response collection.
* **`currentDataPackField`**: Used in journey expressions to refer to each item in a data source collection.
* **`serializeList`**: A journey expression function that converts a list of values into a delimited string (e.g., comma-separated), suitable for use as a query parameter.
* **Supplemental identifier**: A journey-level identifier that distinguishes concurrent journey instances triggered by the same profile; used to filter an array to the item relevant to the current instance.

**Guardrails:**

* Journeys cannot create dynamic loops where one action node executes multiple times per array item — this is by design to prevent performance issues. Pass the entire array or a serialized list to a single custom action instead.
* Keep event payloads under 50KB total.
* Custom action response payloads should be under 100KB.
* Limit the number of dataset lookup keys and returned entities for performance.
* Expression fragments cannot receive loop-scoped variables (e.g., the current `{{#each}}` iteration item) as parameters — this is a known limitation. Use global variables or inline logic instead.
* Numeric event IDs must be wrapped in backticks in expression paths (e.g., `` context.journey.events.`1697323153`.fieldName ``); without backticks, the PQL parser raises a syntax error.

**Terminology:**

* **Canonical name:** Handlebars iteration — variants: `{{#each}}` loop, each loop, array iteration
* **Do not confuse:** Handlebars `{{#each}}` syntax (used in message content for iteration and display) ≠ journey expression syntax (used in journey activity configuration — uses functions like `first`, `all`, `serializeList`)
* **Do not confuse:** `currentEventField` (journey expressions over event arrays) ≠ `currentActionField` (custom action response collections) ≠ `currentDataPackField` (data source collections)
* **Do not confuse:** `@index` / `@first` / `@last` (Handlebars special variables, only available within `{{#each}}` loops in message content) ≠ `first` / `head` functions (journey expression functions for extracting single items, used in journey activity configuration)

**FAQ:**

* **Q: What is the difference between Handlebars syntax and journey expression syntax when working with arrays?** — Handlebars `{{#each}}` is used in message content for iteration and display. Journey expression syntax — using functions like `first`, `all`, and `serializeList` — is used in journey activity configuration (e.g., custom action parameters, conditions). They are distinct syntaxes used in different contexts.
* **Q: Can I loop a journey action node so it executes once per array item?** — No. Journeys cannot create dynamic loops that execute an action node multiple times per item. Instead, pass the entire array or a serialized list to a single custom action that processes all items, or use external aggregation.
* **Q: Can I pass the current loop item to an expression fragment inside a `{{#each}}` loop?** — No. Expression fragments cannot receive loop-scoped variables as parameters. Use global variables defined outside the loop, or include the personalization logic directly within the loop instead of using a fragment.
* **Q: How do I display fallback content when an array is empty?** — Use the `{{else}}` clause within the `{{#each}}` block. Content inside `{{else}}` is rendered when the array has no items.
* **Q: What do `@index`, `@first`, and `@last` mean inside a `{{#each}}` loop?** — These are special Handlebars variables available only within `{{#each}}` loops in message content: `@index` is the 0-based current iteration index, `@first` is true for the first iteration, and `@last` is true for the last iteration.

+++

<!-- ai-section-version: 1 | source-hash: f85f9dea -->
