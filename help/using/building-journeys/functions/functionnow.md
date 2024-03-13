---
product: journey optimizer
title: now
description: Learn about the function now
feature: Journeys
role: Data Engineer, Architect
level: Experienced
keywords: now, function, expression, journey
exl-id: 16dcc772-e48d-4f10-be75-62dd39473556
---
# now {#now}

Returns the current date in date time format. For more information on data types, refer to [this page](../expression/data-types.md).

## Category

Date

## Function syntax

`now(<parameter>)`

## Parameters

|Parameter|Description|
|--- |--- |
|string||

## Signatures and returned type

`now()`

`now("<timeZone id>")`

Returns a dateTime.

## Examples

`now()`

 Returns 2023-06-03T06:30Z.

`toString(now())`

Returns "2023-06-03T06:30Z"

`now("Europe/Paris")`

Returns 2023-06-03T08:30+02:00.
