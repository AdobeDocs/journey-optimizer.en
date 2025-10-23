---
product: journey optimizer
title: inNextYears
description: Learn about the function inNextYears
feature: Journeys
role: Developer
level: Experienced
keywords: inNextYears, function, expression, journey
exl-id: e4597772-d53c-4e15-8237-b2460ce31170
version: Journey Orchestration
---
# inNextYears {#inNextYears}

Returns true if a given date or dateTime is between now and now + delta years.

## Category

Date

## Function syntax

`inNextYears(<dateTime>,<delta>)`

## Parameters

| Parameter | Type             |
|-----------|------------------|
| date time | dateTime    |
| delta   | integer     |

## Signatures and returned type

`inNextYears(<dateTime>,<integer>)`

Returns a boolean.

## Examples

`inNextYears(toDateTime('2021-12-12T01:11:00Z'), 4)`

Returns true.
