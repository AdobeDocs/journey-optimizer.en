---
product: journey optimizer
title: distinctCount
description: Learn about the function distinctCount
feature: Journeys
role: Data Engineer, Architect
level: Experienced
keywords: distinctCount, function, expression, journey
exl-id: 8796ba91-5c64-43c2-a444-27ac8b719c86
---
# distinctCount{#distinctCount}

Counts the number of different values ignoring the null values.

## Category

Aggregation

## Function syntax

`distinctCount(<listAny>)`

## Parameters

| Parameter | Type             |
|-----------|------------------|
| List      | listString       |
| List      | listBoolean      |
| List      | listInteger      |
| List      | listDecimal      |
| List      | listDuration     |
| List      | listDateTime     |
| List      | listDateTimeOnly |
| List      | listDateOnly     |

## Signature and returned type

`distinctCount(<listAny>)`

Returns an integer.

## Example

`distinctCount([10,2,10,null])`

Returns 2.
