---
product: journey optimizer
title: distinctCountWithNull
description: Learn about the function distinctCountWithNull
feature: Journeys
role: Data Engineer, Architect
level: Experienced
keywords: distinctCountWithNull, function, expression, journey
exl-id: 2c3f629f-2220-44a4-9b0c-8aa602301098
version: Journey Orchestration
---
# distinctCountWithNull {#distinctCountWithNull}

Counts the number of different values including the null values.

Note that the parameter `<listObject>` is not supported in this function.

## Category

Aggregation

## Function syntax

`distinctCountWithNull(<listAny>)`

## Parameters

| Parameter | Type             |
|-----------|------------------|
| listToProcess | listString, listBoolean, listInteger, listDecimal, listDuration, listDateTime, listDateTimeOnly, listDateOnly|

## Signature and returned type

`distinctCountWithNull(<listAny>)`

Returns an integer.

## Example

`distinctCountWithNull([10,2,10,null])`

Returns 3.
