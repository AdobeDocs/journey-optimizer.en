---
product: journey optimizer
title: distinctCount
description: Learn about the function distinctCount
feature: Journeys
role: Data Engineer, Architect
level: Experienced
keywords: distinctCount, function, expression, journey
exl-id: 8796ba91-5c64-43c2-a444-27ac8b719c86
version: Journey Orchestration
---
# distinctCount{#distinctCount}

Counts the number of different values ignoring the null values.

## Category

Aggregation

## Function syntax

`distinctCount(<listAny>)`

## Parameters

| Parameter | Type             | Description             |
|-----------|------------------|------------------|
| listToProcess | listString, listBoolean, listInteger, listDecimal, listDuration, listDateTime, listDateTimeOnly, listDateOnly, or listObject | List to process. For listObject, it must be a field reference. |
| keyAttributeName | string | This parameter is optional and only for listObject. If the parameter is not provided, an object is considered as duplicated if all the attributes have the same values. Otherwise, an object is considered as duplicated if the given attribute has the same value. |

## Signature and returned type

`distinctCount(<listAny>)`

Returns an integer.

`distinctCount(<listObject>)`

`distinctCount(<listObject>,<string>)`

Returns a list of objects.


## Example

`distinctCount([10,2,10,null])`

Returns 2.

`distinctCount(@event{my_event.productListItems})`

Returns the number of strictly distinct objects in the given array of objects (listObject type).

`distinctCount(@event{my_event.productListItems}, "SKU")`

Returns the number of objects which have a distinct "SKU" attribute value{}.
