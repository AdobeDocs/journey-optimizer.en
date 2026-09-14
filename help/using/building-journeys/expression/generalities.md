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

{{$include /help/_includes/do-not-localize/building-journeys/ai-augmented-expression-generalities.md}}
