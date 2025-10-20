---
product: journey optimizer
title: countOnlyNull
description: Learn about the function countOnlyNull
feature: Journeys
role: Engineer
level: Experienced
keywords: countOnlyNull, function, expression, journey
exl-id: d06fc594-33dd-48ce-8c62-2f2892a867da
version: Journey Orchestration
---
# countOnlyNull {#countOnlyNull}

Counts the number of null values in the list.

Note that the parameter `<listObject>` is not supported in this function.

## Category

Aggregation

## Function syntax

`countOnlyNull(<listAny>)`

## Parameters

| Parameter | Type             |
|-----------|------------------|
| listToProcess | listString, listBoolean, listInteger, listDecimal, listDuration, listDateTime, listDateTimeOnly, listDateOnly|

## Signature and returned type

`countOnlyNull(<listAny>)`

Returns an integer.

## Example

`countOnlyNull([10,2,10,null])`

Returns 1.
