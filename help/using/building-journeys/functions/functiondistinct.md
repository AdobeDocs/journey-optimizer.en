---
product: journey optimizer
title: distinct
description: Learn about the function distinct
feature: Journeys
role: Data Engineer
level: Experienced
exl-id: f4e2dd34-b634-4a91-af53-60be155a65d0
---
# distinct {#distinct}

Returns the distinct values or objects of a given list. Null entries are ignored.

## Category

List

## Function syntax

`distinct(<parameters>)`

## Parameters

| Parameter | Type             | Description             |
|-----------|------------------|------------------|
| listToProcess | listString, listBoolean, listInteger, listDecimal, listDuration, listDateTime, listDateTimeOnly, listDateOnly, or listObject | List to process. For listObject, it must be a field reference. |
| keyAttributeName | string | This parameter is optional and only for listObject. If the parameter is not provided, an object is considered as duplicated if all the attributes have the same values. Otherwise, an object is considered as duplicated if the given attribute has the same value. |

## Signatures and returned types

`distinct(<listInteger>)`

Returns a list of integers.

`distinct(<listDecimal>)`

Returns a list of decimals.

`distinct(<listString>)`

Returns a list of strings.

`distinct(<listDateTimeOnly>)`

Returns a list of datetimes without considering time zone.

`distinct(<listDateTime>)`

Returns a list of datetimes.

`distinct(<listDateOnly>)`

Returns a list of dates.

`distinct(<listBoolean>)`

Returns a list of booleans.

`distinct(<listDuration>)`

Returns a list of durations.

`distinct(<listObject>)`

`distinct(<listObject>,<string>)`

Returns a list of objects.


## Examples

`distinct([10,2,10,null])`

Returns `[10, 2]`.
