---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page documents the two math functions available in AJO journey expressions — `random` for generating a random decimal between 0 and 1, and `round` for rounding a decimal or integer to the nearest integer.

**Intents:**
* Generate a random decimal value between 0 and 1 for sampling or randomization logic using `random`
* Round a decimal number to the nearest integer using `round`
* Apply rounding in business logic where whole numbers are required from decimal calculations

**Glossary:**
* **random**: A function that returns a pseudo-random decimal value from 0 (inclusive) to 1 (exclusive) *(product-specific)*
* **round**: A function that returns the closest integer to the input, with half-values rounding toward positive infinity

**Guardrails:**
* `random()` takes no parameters
* `round` accepts decimal or integer input and always returns an integer
* Ties in `round` are resolved by rounding toward positive infinity (e.g., 3.5 rounds to 4, -3.5 rounds to -3)

**Terminology:**
* Canonical name: Math functions — Acronym: none — variants: mathematical functions, numeric functions
* Synonyms: "round" = "round to nearest integer"
* Do not confuse: "round" (rounds to the nearest integer) ≠ conversion functions like `toInteger` (truncates the decimal part without rounding)

**FAQ:**
* **Q: What does `random()` return?** — It returns a random decimal number between 0 and 1.
* **Q: How does `round` handle negative numbers?** — It rounds toward positive infinity, so `round(-3.14)` returns -3 and `round(-3.54)` returns -3 as well (closest integer toward positive infinity).
* **Q: What is the difference between `round` and `toInteger`?** — `round` rounds to the nearest integer (3.7 becomes 4), while `toInteger` truncates the decimal part without rounding (3.7 becomes 3).
* **Q: Does `random` take any parameters?** — No, `random()` requires no parameters and always returns a decimal between 0 and 1.

+++
