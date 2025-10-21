---
product: journey optimizer
title: count
description: Learn about the function count
feature: Journeys
role: Developer
level: Experienced
keywords: count, function, expression, journey
exl-id: 6980c1ec-3afd-4fc9-ae10-76bcf7364a04
version: Journey Orchestration
---
# count {#count}

Counts the elements of the list not taking into account the null values.

## Category

Aggregation

## Function syntax

`count(<listAny>)`

`count(<listObject>)`

## Parameters

| Parameter | Type             | Description             |
|-----------|------------------|------------------|
| listToProcess | listString, listBoolean, listInteger, listDecimal, listDuration, listDateTime, listDateTimeOnly, listDateOnly, or listObject | List to process. For listObject, it must be a field reference. A listObject cannot contain null object. |

## Signatures and returned type

`count(<listAny>)`

Returns an integer.

## Example

`count([10,2,10,null])`

Returns 3.

`count(@event{my_event.productListItems})`

Returns the number of objects in the given array of objects (listObject type). Remark: a listObject cannot contain null object
