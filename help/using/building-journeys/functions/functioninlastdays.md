---
product: journey optimizer
title: inLastDays
description: Learn about the function inLastDays
feature: Journeys
role: Data Engineer, Architect
level: Experienced
keywords: inLastDays, function, expression, journey
exl-id: 1b150568-17c2-454d-847e-17bac3d0b35d
---
# inLastDays {#inLastDays}

Returns true if a given dateTime is between now and now - delta days.

## Category

Date

## Function syntax

`inLastDays(<dateTime>,<delta>)`

## Parameters

| Parameter | Type             |
|-----------|------------------|
| date time | dateTime    |
| delta   | integer     |

## Signatures and returned type

`inLastDays(<dateTime>,<integer>)`

Returns a boolean.

## Examples

`inLastDays(toDateTime('2023-12-12T01:11:00Z'), 4)`

Returns true.
