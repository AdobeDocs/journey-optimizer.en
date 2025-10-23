---
product: journey optimizer
title: countWithNull
description: Learn about the function countWithNull
feature: Journeys
role: Developer
level: Experienced
keywords: countWithNull, function, expression, journey
exl-id: 8d53b6d8-f00f-4d1a-b6df-951f84a15430
version: Journey Orchestration
---
# countWithNull {#countWithNull}

Counts all the elements of the list including null values.

Note that the parameter `<listObject>` is not supported in this function.

## Category

Aggregation

## Function syntax

`countWithNull(<listAny>)`

## Parameters

| Parameter | Type             |
|-----------|------------------|
| listToProcess | listString, listBoolean, listInteger, listDecimal, listDuration, listDateTime, listDateTimeOnly, listDateOnly|

## Signature and returned type

`countWithNull(<listAny>)`

Returns an integer.

## Example

`countWithNull([10,2,10,null])`

Returns 4.
