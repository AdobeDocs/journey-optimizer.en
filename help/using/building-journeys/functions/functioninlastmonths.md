---
product: journey optimizer
title: inLastMonths
description: Learn about the function inLastMonths
feature: Journeys
role: Data Engineer, Architect
level: Experienced
keywords: inLastMonths, function, expression, journey
exl-id: 4933ef43-66b8-462d-867c-03edd4c34947
---
# inLastMonths {#inLastMonths}

Returns true if a given date or dateTime is between now and now - delta months.

## Category

Date

## Function syntax

`inLastMonths(<dateTime>,<delta>)`

## Parameters

| Parameter | Type             |
|-----------|------------------|
| date time | dateTime    |
| delta   | integer     |

## Signatures and returned type

`inLastMonths(<dateTime>,<integer>)`

Returns a boolean.

## Examples

`inLastMonths(toDateTime('2023-12-12T01:11:00Z'), 4)`

Returns true.
