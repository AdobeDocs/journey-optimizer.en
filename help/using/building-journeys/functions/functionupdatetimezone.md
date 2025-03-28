---
product: journey optimizer
title: updateTimeZone
description: Learn about the function updateTimeZone
feature: Journeys
role: Data Engineer, Architect
level: Experienced
keywords: updateTimeZone, function, expression, journey
exl-id: 1bf4662e-55d0-4631-af93-1430ec7ed7e2
---
# updateTimeZone {#updateTimeZone}

Returns a new date time, with a new time zone on the same instant.

## Category

Date

## Function syntax

`updateTimeZone(<parameters>)`

## Parameters

* time zone id: string
* dateTime

## Signature and returned type

`updateTimeZone(<dateTime>,<timeZone id>)`

Returns a datetime.

## Examples

`updateTimeZone( toDateTime("2023-08-28T08:15:30.123-07:00"), "Europe/Paris"))`

Returns 2023-08-28T17:15:30.123+02:00.

<!--`updateTimeZone( toDateTime("2019-08-28T08:15:30.123-07:00"), toTimeZone("Europe/Paris")))`
Returns "2019-08-28T17:15:30.123+02:00".-->

`updateTimeZone(@event{MyExpEvent.timestamp}, "Australia/Sydney")`

If the value of the timestamp field is `2021-11-16T16:55:12.939318+01:00`, then the function returns `2021-11-17T02:55:12.942115+11:00`.
