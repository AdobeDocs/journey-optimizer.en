---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page is a complete reference of operators available in the Journey advanced expression editor, covering logical (`and`, `or`, `not`), comparison (`==`, `!=`, `>`, `>=`, `<`, `<=`, `is null`, `is not null`, `has null`), arithmetic (`+`, `-`, `/`, `*`, `%`), math type-check (`is numeric`, `is integer`, `is decimal`), string concatenation, and date arithmetic operators.

**Intents:**

* Combine boolean conditions using logical operators `and`, `or`, and `not`
* Check whether a field or expression value is null or not null using `is null` / `is not null`
* Detect null values within a list using the `has null` operator
* Compare numeric, datetime, and datetimeonly values using `>`, `>=`, `<`, `<=`, `==`, and `!=`
* Perform arithmetic on numeric values using `+`, `-`, `/`, `*`, and `%`
* Add a duration to a dateTime, dateTimeOnly, or duration value using the `+` operator

**Glossary:**

* **Unary operator**: An operator applied to a single operand; can be left-hand (e.g. `not`) or right-hand (e.g. `is null`) *(product-specific)*
* **Binary operator**: An operator applied between two operands (e.g. `and`, `==`, `+`) *(product-specific)*
* **has null**: A right-hand unary operator that returns true if a list contains at least one null element *(product-specific)*
* **is numeric / is integer / is decimal**: Type-check operators that return a boolean based on the numeric subtype of the expression *(product-specific)*

**Guardrails:**

* When using multiplication (`*`), both operands must be the same numeric type (both integer or both decimal) — mixing types causes an error
* When using the `+` operator for date arithmetic, the expression must be wrapped in parentheses to avoid parsing errors
* Comparison operators (`>`, `>=`, `<`, `<=`) are only valid between compatible types: Datetime with Datetime, DatetimeOnly with DatetimeOnly, or numeric with numeric — any other combination is forbidden
* An empty string `""` is not considered null — `has null` returns false for a list containing `""`
* The `==` and `!=` operators perform no data type control between operands

**Terminology:**

* Canonical name: Operators — Acronym: none — variants: expression operators, journey operators
* Synonyms: `and` = "logical AND"; `or` = "logical OR"; `not` = "logical NOT"; `%` = "modulo"
* Do not confuse: `is null` (expression has no evaluated value) ≠ `== null` (not a valid syntax); `has null` (list contains null) ≠ `is null` (expression itself is null)

**FAQ:**

* **Q: Can I multiply an integer by a decimal directly?** — No; both operands of `*` must be the same type. Use `3.0 * 4.0` (both decimal) or `3 * 4` (both integer).
* **Q: How do I add 15 minutes to a dateTime?** — Use `(toDateTime("...")) + (toDuration("PT15M"))`.
* **Q: What is the difference between `is null` and `has null`?** — `is null` checks whether a single expression has no evaluated value; `has null` checks whether a list contains at least one null element.
* **Q: Does `"" has null` return true?** — No; an empty string is not considered null, so the result is false.
* **Q: Why does `3 * 4.0` cause an error?** — The `*` operator requires both operands to be the same numeric type; mixing integer and decimal is not allowed.

+++
