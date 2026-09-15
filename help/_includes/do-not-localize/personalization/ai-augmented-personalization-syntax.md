---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains the Handlebars and PQL personalization syntaxes in Journey Optimizer — their general rules, reserved keywords, namespace structure, type system, and best practices for avoiding common runtime errors.

**Intents:**

* Understand when to use Handlebars (`{{...}}`) vs. PQL (`{%= ... %}`) syntax
* Apply general syntax rules: reserved characters, case sensitivity, HTML escaping, backslash handling
* Escape reserved keywords and special attribute keys (hyphenated names, numeric event IDs) correctly
* Apply type coercion when comparing or passing values of mismatched types
* Reference personalization from the available namespaces: Profile, Audience, Offers
* Follow best practices to avoid the most common runtime and validation errors

**Glossary:**

* **Handlebars**: The `{{...}}` templating syntax used for rendering attributes, looping over arrays, and calling block helpers; HTML-escapes output by default. *(product-specific)*
* **Profile Query Language (PQL)**: The `{%= ... %}` expression syntax used for calling built-in functions (e.g. `upperCase()`, `formatDate()`) and evaluating conditional expressions. *(product-specific)*
* **Triple-stash (`{{{ }}}`)**: A Handlebars syntax variant that outputs values without HTML escaping, useful when the value itself contains HTML characters that should not be encoded.
* **Reserved keywords**: PQL identifiers (`next`, `last`, `this`) that cannot be used directly as field or variable names; must be wrapped in backticks when a schema field uses one of these names.
* **Type coercion**: The explicit conversion of a value from one data type to another (e.g. string → number) using functions like `stringToNumber()` or `toBool()`, required before comparison or arithmetic in PQL.
* **Namespace**: The top-level grouping of personalization data — Profile, Audience, Offers — each with its own path structure and access rules.
* **Block helper**: A Handlebars helper identified by `#` before the helper name and a matching closing `/`, used for block constructs like `{{#each}}`.

**Guardrails:**

* The `xEvent` variable is not available in personalization expressions; any reference to `xEvent` results in validation failures.
* PQL function calls inside `{{...}}` Handlebars blocks will fail; use `{%= ... %}` instead.
* The `{% if %}` / `{% elseif %}` / `{% endif %}` conditional syntax is not supported; use `{%#if%}` / `{%else if%}` / `{%/if%}`.
* Backtick escaping for hyphenated field names is only supported inside PQL expressions (`{%= ... %}`). In `{{...}}` Handlebars interpolation, backtick syntax fails — but hyphenated field names can still be referenced directly (e.g. `{{profile.my-custom-field}}`).
* Reserved keywords (`next`, `last`, `this`) must be wrapped in backticks when used as schema field names; applies to both `{{...}}` and `{%= ... %}`.
* Single backslash `\` is not supported as a literal function argument; use double backslash `\\`.
* PQL is strongly typed; mismatched types in comparisons or arithmetic require explicit conversion using `stringToNumber()`, `toBool()`, or similar coercion functions.

**Terminology:**

* **Canonical name:** Handlebars — for the `{{...}}` syntax; PQL — for the `{%= ... %}` syntax
* **Do not confuse:** `{{...}}` (Handlebars — renders variables and helpers, HTML-escaped) ≠ `{%= ... %}` (PQL — evaluates functions and expressions) ≠ `{%#if%}` / `{%/if%}` (conditional block syntax, percent-curly braces)
* **Do not confuse:** `{{profile.person.name}}` (single-stash — HTML-escaped output) ≠ `{{{profile.person.name}}}` (triple-stash — unescaped output)
* **Do not confuse:** reserved keyword backtick escaping (applies to both `{{...}}` and `{%= ... %}`) ≠ hyphenated key backtick escaping (only supported inside `{%= ... %}` PQL expressions, not in `{{...}}`)
* **Do not confuse:** `=` (PQL equality operator — correct) ≠ `==` (not valid PQL — causes a syntax error)

**FAQ:**

* **Q: When should I use `{{...}}` vs. `{%= ... %}`?** — Use `{{...}}` (Handlebars) to render attribute values, loop over arrays, and call block helpers. Use `{%= ... %}` (PQL) to call built-in functions like `upperCase()` and `formatDate()`, and to evaluate conditional expressions.
* **Q: How do I output a value without HTML encoding?** — Use the triple-stash `{{{ }}}` instead of `{{...}}`. Single-brace Handlebars HTML-escapes output (e.g., `&` becomes `&amp;`); triple-stash bypasses escaping.
* **Q: What is the correct equality operator in PQL?** — Use a single `=` for equality comparisons in PQL. Using `==` is a syntax error.
* **Q: How do I reference a schema field whose name is a reserved keyword (e.g. `next`, `last`, `this`)?** — Wrap it in backticks: `{{profile.person.\`next\`.name}}`. This applies to both Handlebars paths and PQL expressions.
* **Q: Can I call PQL functions inside `{{...}}` Handlebars blocks?** — No. `{{...}}` resolves Handlebars variables and helpers only. A PQL function inside `{{...}}` causes a "could not find helper" error. Use `{%= functionName(...) %}` instead.

+++

<!-- ai-section-version: 1 | source-hash: 7fa07aa5 -->
