---
product: journey optimizer
title: avg
description: Learn about the function avg
feature: Journeys
role: Developer
level: Experienced
keywords: avg, function, expression, journey
exl-id: cc70f90c-2d12-42a0-829f-5f28c3c29cad
version: Journey Orchestration
---
# avg {#avg}

Returns the average value among a set of expressions, given either as a list or two expressions. Null values are ignored.


## Category

Aggregation

## Function syntax

`avg(<parameter>)`

## Parameters

Supported types:

* listInteger
* listDecimal
* decimal
* integer

## Signatures and returned type

`avg(<listInteger>)`

`avg(<listDecimal>)`

`avg(<decimal>,<decimal>)`

`avg(<decimal>,<integer>)`

`avg(<integer>,<decimal>)`

`avg(<integer>,<integer>)`

Returns a decimal.

## Examples

`avg(@event{BarBeacon.inventory},5)`

`avg([10,3,8])`

Returns 7.0.

`avg(10.2, 3)`

Returns 6.6.
