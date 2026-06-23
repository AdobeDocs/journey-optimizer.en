---
solution: Journey Optimizer
product: journey optimizer
title: Advanced expression editor syntax
description: Learn about the syntax used in the advanced expression editor
feature: Journeys
role: Developer
level: Experienced
keywords: syntax, editor, journey
exl-id: c9434b28-2750-4a53-985e-c4a3f940472c
version: Journey Orchestration
TQID: https://experienceleague.adobe.com/-PTYUf-njT3-LsI-A5IKEMDGOl4JecZ-ayM0rU4f2HI
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: d998adac-2f81-400b-a669-d07bb196e4eb
    internal-label: Journeys
role_v2:
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
subfeature_v2: []
---
# Advanced expression editor syntax {#syntax}

Syntax basics when using the [Advanced expression editor](expressionadvanced.md) are listed below. <!-- Samples of use of the advanced expression editor are available on [this page](advanced-editor-use-cases.md).-->

## Parentheses and expression priority {#parentheses-and-expression-priority}

Parentheses can be used to make a complex expression more readable. _(&lt;expression>)_ is the equivalent of _&lt;expression>_. Parenthesis can also be used to define the evaluation order and associativity.

The expressions will be evaluated from left to right. The associativity on arithmetic operators must be applied: multiplications and divisions take priority over additions and subtractions. In order to impose a specific order, parenthesis must be added to delimit the operations. For example:

<!--```5 + 2 * 10 = 25, and (5 + 2) * 10 = 70```-->

|Expression|Evaluation|
|--- |--- |
|`4 + 2 * 10`|<ul><li>'*' takes priority over '+': 2 \* 10 is evaluated → 20</li><li>4 + 20 → 24</li></ul>|
|`(4 + 2) * 10`|<ul><li>The parentheses change the priority: (4 + 2) is evaluated → 6</li><li> 6 * 10 → 60</li></ul>|

## Case sensitivity {#case-sensitivity}

Here are the different case sensitivity rules:

* All operators (and, or, etc.) should be written lowercase. For instance, _`<expression1>` and `<expression2>`_ is a valid expression whereas the expression _`<expression1>` AND `<expression2>`_ is not.
* All function names are case sensitive. For instance, _inAudience()_ is valid whereas the function _INAUDIENCE()_ is not.
* Field references and constant values are case sensitive: they are not built-in elements of the language (as opposed to operators and functions), they are authored by the end user.

## Returned expression type {#returned-expression-type}

Depending on the context of use, the expression editor can return different values.

|Advanced expression editor usage|Expected returned expression type|
|--- |--- |
|Condition (data source condition, date condition)|boolean|
|Custom timer|dateTimeOnly|
|Action parameters mapping|Any|

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
