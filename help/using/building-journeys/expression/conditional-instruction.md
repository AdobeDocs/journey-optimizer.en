---
solution: Journey Optimizer
product: journey optimizer
title: Conditional instruction (if, then, else)
description: Learn about conditional instruction
feature: Journeys
role: Developer
level: Experienced
keywords: advanced, condition, action, journey
exl-id: 5a5b35a7-e3b5-4dc0-8a87-e985956b04a4
version: Journey Orchestration
TQID: https://experienceleague.adobe.com/SObpEvgu0D-pcoLVaKM7iRffLTSP1stp1zcg4Ygs-vQ
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: b3538224-471e-4c63-a444-9b19d89ae29c
    internal-label: Activities
  - id: d998adac-2f81-400b-a669-d07bb196e4eb
    internal-label: Journeys
subfeature_v2:
  - id: cce82f05-fc3c-4af7-85ff-8bba603861a7
    internal-label: Condition activities
  - id: d8353d85-5da7-453d-bd68-40ad33fa0ab7
    internal-label: Action activities
role_v2:
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
---
# Conditional instruction (if, then, else) {#conditional-instruction}

The conditional instruction (if, then, else) is supported in the advanced editor. It allows to define more complex expressions. It is composed of the following elements:

* **[!UICONTROL if]**: the condition to be evaluated first.
* **[!UICONTROL then]**: the expression to be evaluated in case the result of the condition evaluation is true.
* **[!UICONTROL else]**: the expression to be evaluated in case the result of the condition evaluation is false.

>[!NOTE]
>
>Parentheses are required around all the expressions.

   ```json
   if  (<expression1>)
   then
      (<expression2>)
   else
      (<expression3>)
   ```

`<expression1>` must return a **boolean**.

`<expression2>` and `<expression3>` must have the same type or compatible types. The supported signatures and returned types are:

   ```json
   boolean,boolean : boolean
   dateTime,dateTime : dateTime
   dateTimeOnly,dateTimeOnly : dateTimeOnly
   decimal,integer : decimal
   integer,decimal : integer
   integer,decimal : decimal
   duration,duration : duration
   string,string : string
   listBoolean,listBoolean : listBoolean
   listDateTime,listDateTime : listDateTime
   listDateTimeOnly,listDateTimeOnly : listDateTimeOnly
   listDateOnly,listDateOnly : listDateOnly
   listDecimal,listDecimal : listDecimal
   listInteger,listInteger : listInteger
   listString,listString : listString
   ```

**Usage**

The conditional instruction allows you to optimize the journey workflow by reducing the number of condition activities. For example, within the same action activity, you can specify two alternatives for a field definition using only one condition expression.

Example for an action activity (for a field that expects a string as the result of the conditional instruction):

   ```json
   if (startWithIgnoreCase(@event{eventiOSPushPermissionAllowed.device.model}, 'iPad') or startWithIgnoreCase(@event{eventiOSPushPermissionAllowed.device.model}, 'iOS'))
   then
      ('apns')
   else
      ('fcm')
   ```

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
