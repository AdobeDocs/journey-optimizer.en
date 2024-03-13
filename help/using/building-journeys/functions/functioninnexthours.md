---
product: journey optimizer
title: inNextHours
description: Learn about the function inNextHours
feature: Journeys
role: Data Engineer, Architect
level: Experienced
keywords: inNextHours, function, expression, journey
exl-id: 079a91b6-49c5-4e68-a240-358ed0cded92
---
# inNextHours {#inNextHours}

Returns true if a given date or dateTime is between now and now + delta hours.

## Category

Date

## Function syntax

`inNextHours(<dateTime>,<delta>)`

## Parameters

| Parameter | Type             |
|-----------|------------------|
| date time | dateTime    |
| delta   | integer     |

## Signatures and returned type

`inNextHours(<dateTime>,<integer>)`

Returns a boolean.

## Examples

`inNextHours(toDateTime('2023-12-12T01:11:00Z'), 4)`

Returns true.
