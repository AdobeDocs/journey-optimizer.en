---
product: journey optimizer
title: inNextDays
description: Learn about the function inNextDays
feature: Journeys
role: Data Engineer, Architect
level: Experienced
keywords: inNextDays, function, expression, journey
exl-id: 0cb3e0db-dc5b-4d4e-a057-af030d9bdb21
---
# inNextDays {#inNextDays}

Returns true if a given date or dateTime is between now and now + delta days.

## Category

Date

## Function syntax

`inNextDays(<dateTime>,<delta>)`

## Parameters

| Parameter | Type             |
|-----------|------------------|
| date time | dateTime    |
| delta   | integer     |

## Signatures and returned type

`inNextDays(<dateTime>,<integer>)`

Returns a boolean.

## Examples

`inNextDays(toDateTime('2023-12-12T01:11:00Z'), 4)`

Returns true.
