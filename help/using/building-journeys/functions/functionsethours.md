---
product: journey optimizer
title: setHours
description: Learn about the function setHours
feature: Journeys
role: Data Engineer, Architect
level: Experienced
keywords: setHours, function, expression, journey
exl-id: ed78c2a9-d83a-4fac-a2e9-7383da131a1f
---
# setHours {#setHours}

Sets the hours of a date time or date time only. For example, if you want to wait until a certain hour tomorrow, you can force the hour.

## Category

Date

## Function syntax

`setHours(<parameter>)`

## Parameters

|Parameter|Type|
|--- |--- |
|date time|dateTime|
|date time without considering time zone|dateTimeOnly|
|hours|integer|

## Signatures and returned type

`setHours(<dateTime>,<hours>)`

Returns a datetime.

`setHours(<dateTimeOnly>,<hours>)`

Returns a datetime without considering time zone.

## Examples

`setHours(toDateTime('2023-12-12T01:11:00Z'), 4)`

Returns 2023-12-12T04:11:00Z.

`setHours(nowWithDelta(1, "days"), 20)`

Returns tomorrow at 8:XY PM, XY being the minutes at the moment of the current time evaluation. If the evaluation happens at 2:45 AM, the returned time will be 8:45 PM.
