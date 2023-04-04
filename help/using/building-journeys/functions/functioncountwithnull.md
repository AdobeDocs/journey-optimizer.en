---
product: journey optimizer
title: countWithNull
description: Learn about the function countWithNull
feature: Journeys
role: Data Engineer, Architect
level: Experienced
keywords: countWithNull, function, expression, journey
exl-id: 8d53b6d8-f00f-4d1a-b6df-951f84a15430
---
# countWithNull {#countWithNull}

Counts all the elements of the list including null values.

## Category

Aggregation

## Function syntax

`countWithNull(<listAny>)`

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

`countWithNull(<listAny>)`

Returns an integer.

## Example

`countWithNull([10,2,10,null])`

Returns 4.
