---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains the `if / then / else` conditional instruction available in the Journey advanced expression editor, including syntax rules, supported type combinations, and a practical usage example.

**Intents:**

* Write a conditional expression using `if`, `then`, and `else` to return different values based on a boolean condition
* Reduce the number of condition activities in a journey by embedding inline conditional logic within a single action activity
* Determine which data type combinations are valid for the `then` and `else` branches
* Apply the conditional instruction to route push notification tokens to either APNS or FCM based on device model

**Glossary:**

* **Conditional instruction**: An `if / then / else` expression construct in the advanced editor that evaluates a boolean and returns one of two expressions *(product-specific)*
* **Advanced expression editor**: The Journey Optimizer interface for writing complex expressions used in conditions, wait activities, and action parameter mapping *(product-specific)*

**Guardrails:**

* Parentheses are required around all expressions in the `if`, `then`, and `else` clauses
* The `if` clause (`<expression1>`) must return a boolean type
* The `then` and `else` expressions (`<expression2>` and `<expression3>`) must have the same type or compatible types (e.g. `decimal` and `integer` are compatible, `string` and `integer` are not)
* Not all type combinations are supported — only the pairs listed in the supported signatures table are valid

**Terminology:**

* Canonical name: Conditional Instruction — Acronym: none — variants: if/then/else, ternary-style condition
* Synonyms: "conditional instruction" = "inline condition" = "if-then-else expression"
* Do not confuse: conditional instruction (inline expression) ≠ Condition activity (a journey canvas node)

**FAQ:**

* **Q: Does the `if` clause need to be wrapped in parentheses?** — Yes, parentheses are required around all expressions including the condition in the `if` clause.
* **Q: Can I use `if / then / else` to return a number from one branch and a string from another?** — No; `<expression2>` and `<expression3>` must have the same or compatible types.
* **Q: How does the conditional instruction reduce journey complexity?** — It lets you specify two field value alternatives within a single action activity using one expression, avoiding a separate Condition activity node on the canvas.
* **Q: What type does the conditional instruction return if both branches are strings?** — It returns a `string`.
* **Q: Can `if / then / else` be used to select a push notification channel?** — Yes; for example, evaluating the device model to return `'apns'` for Apple devices or `'fcm'` for others.

+++
