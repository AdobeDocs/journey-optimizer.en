---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page covers the core syntax rules of the Journey advanced expression editor — operator precedence with parentheses, case sensitivity for operators and functions, and the expected return type for each editor context.

**Intents:**

* Control expression evaluation order by wrapping sub-expressions in parentheses
* Write operators (`and`, `or`, `not`) in lowercase to avoid syntax errors
* Use correctly cased function names (e.g. `inAudience()` not `INAUDIENCE()`)
* Understand that conditions must return a boolean, custom timers must return `dateTimeOnly`, and action parameter mappings can return any type

**Glossary:**

* **Expression priority**: The order in which operators are evaluated; multiplications and divisions take priority over additions and subtractions *(product-specific)*
* **Case sensitivity**: In the advanced editor, operators must be lowercase, function names are case-sensitive, and field references are case-sensitive as authored by the user *(product-specific)*
* **dateTimeOnly**: The return type required for custom timer (Wait activity) expressions; represents a date-time without a timezone *(product-specific)*

**Guardrails:**

* Operators (`and`, `or`, `not`, etc.) must be written in lowercase — uppercase variants are invalid
* All function names are case-sensitive — `inAudience()` is valid but `INAUDIENCE()` is not
* Arithmetic follows standard precedence: `*` and `/` evaluate before `+` and `-`; use parentheses to override
* Conditions always return a boolean; custom timers always return `dateTimeOnly`

**Terminology:**

* Canonical name: Advanced Expression Editor Syntax — Acronym: none — variants: expression syntax, editor syntax
* Synonyms: "expression priority" = "operator precedence"; "parentheses" = "brackets" (in expression context)
* Do not confuse: operator case sensitivity (operators must be lowercase) ≠ field reference case sensitivity (field names are user-authored and case-sensitive as written)

**FAQ:**

* **Q: Does `4 + 2 * 10` evaluate to 60 or 24?** — It evaluates to 24 because `*` takes priority over `+`; use `(4 + 2) * 10` to get 60.
* **Q: Can I write `AND` in uppercase in an expression?** — No; all operators must be lowercase (`and`, `or`, `not`).
* **Q: Are function names case-sensitive?** — Yes; `inAudience()` is valid but `INAUDIENCE()` is not.
* **Q: What type must a condition expression return?** — A boolean.
* **Q: What return type is required for a custom Wait activity timer expression?** — `dateTimeOnly`.

+++
