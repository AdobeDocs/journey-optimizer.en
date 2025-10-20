---
product: journey optimizer
title: max
description: Learn about the function max
feature: Journeys
role: Engineer
level: Experienced
keywords: max, function, expression, journey
exl-id: 5c792d33-32b9-4b1b-ab99-3ebfac391678
version: Journey Orchestration
---
# max{#max}

Returns the maximum value among a set of expressions, given either as a list or two expressions. Null values are ignored.

## Category

Aggregation

## Function syntax

`max(<parameter>)`

## Parameters

* listDuration
* listInteger
* listDecimal
* listDateTime
* listDateTimeOnly
* listDateOnly
* duration
* integer
* decimal
* dateTime
* dateTimeOnly

## Signatures and returned types

`max(<listDuration>)`

Returns a duration.

`max(<listInteger>)`

Returns a duration.

`max(<listDateTimeOnly>)`

Returns a datetime without considering time zone.

`max(<listDateTime>)`

Returns a datetime.

`max(<listDateOnly>)`

Returns a date.

`max(<listDecimal>)`

Returns a decimal.

`max(<decimal>,<decimal>)`

Returns a decimal.

`max(<duration>,<duration>)`

Returns a duration.

`max(<dateTime>,<dateTime>)`

Returns a datetime.

`max(<dateTimeOnly>,<dateTimeOnly>)`

Returns a datetime without considering time zone.

`max(<integer>,<integer>)`

Returns an integer.

## Examples

`max(@event{BarBeacon.inventory},5)`

`max([10,3,8])`

Returns 10.

`max([10,null,8])`

Returns 10.
