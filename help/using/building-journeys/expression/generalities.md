---
solution: Journey Optimizer
product: journey optimizer
title: Syntax
description: Learn about the advanced expression editor
feature: Journeys
role: Data Engineer, Architect
level: Experienced
keywords: syntax, editor, journey
exl-id: c9434b28-2750-4a53-985e-c4a3f940472c
---
# Advanced expression editor syntax {#syntax}

## Parentheses and expression priority{#parentheses-and-expression-priority}

Parentheses can be used to make a complex expression more readable. _(&lt;expression>)_ is the equivalent of _&lt;expression>_. Parenthesis can also be used to define the evaluation order and associativity.

The expressions will be evaluated from left to right. The associativity on arithmetic operators must be applied: multiplications and divisions take priority over additions and subtractions. In order to impose a specific order, parenthesis must be added to delimit the operations. For example:

<!--```5 + 2 * 10 = 25, and (5 + 2) * 10 = 70```-->

|Expression|Evaluation|
|--- |--- |
|`4 + 2 * 10`|<ul><li>'*' takes priority over '+': 2 * 10 is evaluated → 20</li><li>4 + 20 → 24</li></ul>|
|`(4 + 2) * 10`|<ul><li>The parentheses change the priority: (4 + 2) is evaluated → 6</li><li> 6 * 10 → 60</li></ul>|

## Case sensitivity{#case-sensitivity}

Here are the different case sensitivity rules:

* All operators (and, or, etc.) should be written lowercase. For instance, _`<expression1>` and `<expression2>`_ is a valid expression whereas the expression _`<expression1>` AND `<expression2>`_ is not.
* All function names are case sensitive. For instance, _inAudience()_ is valid whereas the function _INAUDIENCE()_ is not.
* Field references and constant values are case sensitive: they are not built-in elements of the language (as opposed to operators and functions), they are authored by the end user.

## Returned expression type{#returned-expression-type}

Depending on the context of use, the expression editor can return different values.

|Advanced expression editor usage|Expected returned expression type|
|--- |--- |
|Condition (data source condition, date condition)|boolean|
|Custom timer|dateTimeOnly|
|Action parameters mapping|Any|
