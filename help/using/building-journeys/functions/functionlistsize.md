---
product: journey optimizer
title: listSize
description: Learn about the function listSize
feature: Journeys
role: Developer
level: Experienced
keywords: listSize, function, expression, journey
exl-id: dd378e4d-f65a-495c-ac10-b4209d6b6b88
version: Journey Orchestration
---
# listSize {#listSize}

Counts the number of elements in the list.

## Category

List

## Function syntax

`listSize(<parameters>)`

## Parameters

| Parameter | Type             | Description             |
|-----------|------------------|------------------|
| listToProcess | listString, listBoolean, listInteger, listDecimal, listDuration, listDateTime, listDateTimeOnly, listDateOnly, or listObject | List to process. For listObject, it must be a field reference. A listObject cannot contain null object. |

## Signatures and returned type

`listSize(<listInteger>)`

`listSize(<listDecimal>)`

`listSize(<listString>)`

`listSize(<listBoolean>)`

`listSize(<listDateTimeOnly>)`

`listSize(<listDateTime>)`

`listSize(<listDateOnly>)`

`listSize(<listDuration>)`

Return an integer.

`listSize(<listObject>)`

## Example

`listSize([10,2,3])`

Returns 3.

`listSize(@event{my_event.productListItems})`

Returns the number of objects in the given array of objects (listObject type).
