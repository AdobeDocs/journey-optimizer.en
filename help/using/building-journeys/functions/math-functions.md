---
product: journey optimizer
title: Math functions
description: Learn about math functions
feature: Journeys
role: Developer
level: Experienced
keywords: math, functions, expression, journey, calculation, number
version: Journey Orchestration
exl-id: da710b22-3112-41fe-8b91-2b6563b79f27
---
# Math functions {#math-functions}

Math functions provide essential mathematical operations for numerical calculations within your journey expressions. These functions enable you to perform precise numeric computations and transformations on your data.

Use math functions when you need to:

* Generate random values for testing, sampling, or randomization ([random](#random))
* Round decimal numbers to the nearest integer for cleaner data presentation ([round](#round))
* Perform mathematical calculations on numeric fields
* Transform numeric values for business logic and decision making

Math functions handle both decimal and integer types, automatically managing type conversions to ensure accurate results in your journey expressions.

## random {#random}

Generates a random number between 0 and 1.

+++Syntax

`random()`

+++

+++Signature and returned type

`random()`

Returns a decimal.

+++

## round {#round}

Returns the closest integer value to the argument with ties rounding to positive infinity.

+++Syntax

`round(<parameters>)`

+++

+++Parameters

* decimal
* integer

+++

+++Signatures and returned type

`round(<decimal>)`

`round(<integer>)`

Return an integer.

+++

+++Examples

`round(3.14)`

Returns 3.

`round(3.54)`

Returns 4.

`round(-3.14)`

Returns -3.

`round(3)`

Returns 3.

+++
