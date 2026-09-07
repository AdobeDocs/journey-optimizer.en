---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page documents all aggregation functions available in AJO journey expressions, covering how to compute averages, sums, min/max values, counts, and distinct counts over lists and arrays.

**Intents:**
* Calculate the average of a list of numeric values using `avg`
* Sum numeric values in a list or from event fields using `sum`
* Find the minimum or maximum value in a list using `min` or `max`
* Count non-null, null-only, or all elements in a list using `count`, `countOnlyNull`, or `countWithNull`
* Count distinct values in a list, with or without nulls, using `distinctCount` or `distinctCountWithNull`
* Filter unique objects in a listObject by a specific key attribute using `distinctCount` with a key parameter

**Glossary:**
* **listObject**: A list of complex objects (field references); cannot contain null objects *(product-specific)*
* **listAny**: A list of any supported scalar type (string, boolean, integer, decimal, duration, dateTime, dateTimeOnly, dateOnly) *(product-specific)*
* **Null value**: An absent or undefined element in a list; most aggregation functions ignore nulls unless the function explicitly handles them (e.g., `countOnlyNull`, `countWithNull`, `distinctCountWithNull`)

**Guardrails:**
* `countOnlyNull`, `countWithNull`, and `distinctCountWithNull` do not support the `<listObject>` parameter type
* `distinctCount` on a `listObject` requires the list to be a field reference, not an inline literal
* `count` on a `listObject` requires the list to be a field reference; a listObject cannot contain null objects

**Terminology:**
* Canonical name: Aggregation functions — Acronym: none — variants: aggregate functions, collection functions
* Synonyms: "count" = "count non-null elements"; "countWithNull" = "count all elements including nulls"
* Do not confuse: "distinctCount" (ignores nulls) ≠ "distinctCountWithNull" (includes nulls as a distinct value)

**FAQ:**
* **Q: Does `avg` include null values in its calculation?** — No, `avg` ignores null values automatically.
* **Q: What is the difference between `count` and `countWithNull`?** — `count` excludes null values from the total, while `countWithNull` counts every element including nulls.
* **Q: Can I use `countOnlyNull` on a listObject?** — No, `<listObject>` is not supported by `countOnlyNull`, `countWithNull`, or `distinctCountWithNull`.
* **Q: How do I count distinct objects in an array based on a specific attribute?** — Use `distinctCount(@event{...}, "attributeName")` providing the key attribute name as the second parameter.
* **Q: What does `max` return when the list contains nulls?** — `max` ignores null values and returns the maximum among the non-null elements.

+++
