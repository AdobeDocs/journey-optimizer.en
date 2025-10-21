---
product: journey optimizer
title: sum
description: Learn about the function sum
feature: Journeys
role: Developer
level: Experienced
keywords: sum, function, expression, journey
exl-id: a9085f4d-6434-4bc5-8e5d-3f2b6033defc
version: Journey Orchestration
---
# sum {#sum}

Returns the sum of the values of a set of expressions. Null values are ignored.

## Category

Aggregation

## Function syntax

`sum(<parameters>)`

## Parameters

* listInteger
* listDecimal
* duration
* integer
* decimal

## Signatures and returned types

`sum(<listDecimal>)`

Returns a decimal.

`sum(<listInteger>)`

Returns an integer.

`sum(<integer>,<integer>)`

Returns an integer.

`sum(<decimal>,<decimal>)`

Returns a decimal.

## Examples

`sum(@event{BarBeacon.inventory},5)`

`sum([10,3,8])`

Returns 21.

`sum([10.5,null,8.1])`

Returns 18.6.
