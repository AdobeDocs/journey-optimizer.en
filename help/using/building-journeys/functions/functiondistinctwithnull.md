---
product: journey optimizer
title: distinctWithNull
description: Learn about the function distinctWithNull
feature: Journeys
role: Engineer
level: Experienced
keywords: distinctWithNull, function, expression, journey
exl-id: 73fa9837-d2e1-4f0a-a423-cf7728882eba
version: Journey Orchestration
---
# distinctWithNull {#distinctWithNull}

Returns the distinct values or objects of a given list. If the list has at least one null entry, a null entry will be present in the returned list.

Note that the parameter `<listObject>` is not supported in this function.

## Category

List

## Function syntax

`distinctWithNull(<parameters>)`

## Parameters

| Parameter | Type             | Description             |
|-----------|------------------|------------------|
| listToProcess | listString, listBoolean, listInteger, listDecimal, listDuration, listDateTime, listDateTimeOnly, listDateOnly| List to process.|

## Signatures and returned types

`distinctWithNull(<listInteger>)`

Returns a list of integers.

`distinctWithNull(<listDecimal>)`

Returns a list of decimals.

`distinctWithNull(<listString>)`

Returns a list of strings.

`distinctWithNull(<listDateTimeOnly>)`

Returns a list of datetimes without considering time zone.

`distinctWithNull(<listDateTime>)`

Returns a list of datetimes.

`distinctWithNull(<listDateOnly>)`

Returns a list of dates.

`distinctWithNull(<listBoolean>)`

Returns a list of booleans.

`distinctWithNull(<listDuration>)`

Returns a list of durations.

## Examples

`distinctWithNull([10,2,10,null])`

Returns [10, 2, null]
