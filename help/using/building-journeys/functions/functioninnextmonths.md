---
product: journey optimizer
title: inNextMonths
description: Learn about the function inNextMonths
feature: Journeys
role: Data Engineer, Architect
level: Experienced
keywords: inNextMonths, function, expression, journey
exl-id: e2e520ec-ae9e-4ed6-b50d-606fc6861d56
---
# inNextMonths {#inNextMonths}

Returns true if a given date or dateTime is between now and now + delta months.

## Category

Date

## Function syntax

`inNextMonths(<dateTime>,<delta>)`

## Parameters

| Parameter | Type             |
|-----------|------------------|
| date time | dateTime    |
| delta   | integer     |

## Signatures and returned type

`inNextMonths(<dateTime>,<integer>)`

Returns a boolean.

## Examples

`inNextMonths(toDateTime('2023-01-12T01:11:00Z'), 4)`

Returns true.
