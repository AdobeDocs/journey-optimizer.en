---
product: journey optimizer
title: inLastYears
description: Learn about the function inLastYears
feature: Journeys
role: Data Engineer, Architect
level: Experienced
keywords: inLastYears, function, expression, journey
exl-id: cdf653d2-967e-4a1b-92e5-37dd22f379f9
---
# inLastYears {#inLastYears}

Returns true if a given date or dateTime is between now and now - delta years.

## Category

Date

## Function syntax

`inLastYears(<dateTime>,<delta>)`

## Parameters

| Parameter | Type             |
|-----------|------------------|
| date time | dateTime    |
| delta   | integer     |

## Signatures and returned type

`inLastYears(<dateTime>,<integer>)`

Returns a boolean.

## Examples

`inLastYears(toDateTime('2023-12-12T01:11:00Z'), 4)`

Returns true.
