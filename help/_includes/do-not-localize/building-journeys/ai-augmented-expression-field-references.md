---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to reference event fields and data source field groups in journey expressions, including default value syntax, map access functions (`entry`, `firstEntryKey`, `keys`), and inline data source parameter passing with the `params` keyword.

**Intents:**

* Reference an event field in an expression using the `@event{eventName.fieldPath}` syntax
* Reference a data source field group using the `#{dataSourceName.fieldGroupName.fieldPath}` syntax
* Assign a fallback default value to a field reference so expressions do not return null
* Retrieve a specific entry from an identity map or subscription map using the `entry()` function
* Retrieve all keys from a map field using the `keys()` function
* Pass parameter values to an external data source inline using the `params` keyword

**Glossary:**

* **Field reference**: An expression syntax that points to a named field within an event payload or data source field group *(product-specific)*
* **defaultValue**: An optional fallback expression appended to a field reference that is returned when the field is absent or null *(product-specific)*
* **entry(key)**: A map function that retrieves the collection entry associated with the given key *(product-specific)*
* **firstEntryKey()**: A map function that returns the first key of a map field *(product-specific)*
* **keys()**: A map function that returns all keys of a map field *(product-specific)*
* **params keyword**: Inline syntax for specifying parameter values for external data source fields within the main expression *(product-specific)*

**Guardrails:**

* Field names containing special characters (starting with a digit, containing `-`, or characters outside `a-z A-Z 0-9 _`) must be wrapped in single or double quotes
* The default value expression must return the same data type as the field — mismatched types are invalid
* When the `params` keyword is used to define parameter values inline, the separate parameter tab on the right of the editor disappears
* Functions used as default values must be encapsulated in parentheses

**Terminology:**

* Canonical name: Field References — Acronym: none — variants: field path, field expression
* Synonyms: `@event{...}` = "event field reference"; `#{...}` = "data source field reference"
* Do not confuse: event fields (prefixed `@`) ≠ data source fields (prefixed `#`)

**FAQ:**

* **Q: How do I reference a field whose name starts with a number?** — Wrap the field name in single or double quotes, e.g. `#{OpenWeather.weatherData.rain.'3h'}`.
* **Q: What happens when a referenced field is missing from the event payload and no default value is set?** — The expression returns `null`.
* **Q: How do I set a dynamic default value using a function?** — Wrap the function call in parentheses, e.g. `defaultValue: (now())`.
* **Q: How do I retrieve the email address stored as the first key in a subscriber map?** — Use the `firstEntryKey()` function on the subscribers map field.
* **Q: How do I pass a parameter to an external data source without using the right-side tab?** — Use the `params` keyword inline: `#{DataSource.group.field, params: {paramName: value}}`.

+++
