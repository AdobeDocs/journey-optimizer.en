---
product: journey optimizer
title: toDateTimeOnly
description: Learn about the function toDateTime
feature: Journeys
role: Data Engineer, Architect
level: Experienced
keywords: toDateTimeOnly, function, expression, journey
exl-id: db54c119-5080-403a-b254-43645be6b4a8
---
# toDateTimeOnly{#toDateTimeOnly}

Converts an argument value into a date time only value.

## Category

Conversion

## Function syntax

`toDateTimeOnly(<parameters>)`

## Parameters

| Parameter | Type             |
|-----------|------------------|
| date time in ISO-8601 or "YYYY-MM-DD" format (XDM Date format) | string |
| date time | dateTime|

## Signatures and returned types

`toDateTimeOnly(<dateTime>)`

`toDateTimeOnly(<string>)`
<!--`toDateTimeOnly(<integer>,<integer>,<integer>)`
`toDateTimeOnly(<integer>,<integer>,<integer>,<integer>,<integer>,<integer>)`-->

Return a datetime without considering time zone.

## Examples

`toDateTimeOnly ("2023-08-18")`

returns a dateTime representing 2023-08-18T00:00:00.000

`toDateTimeOnly(now())`

<!--`toDateTimeOnly(2016,8,18,23,17,59)`

Returns 2016-08-18T23:17:59.000.

`toDateTimeOnly(2016,8,18)`

Returns 2016-08-18T00:00:00.000.-->
