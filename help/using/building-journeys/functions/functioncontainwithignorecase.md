---
product: journey optimizer
title: containIgnoreCase
description: Learn about the function containIgnoreCase
feature: Journeys
role: Engineer
level: Experienced
keywords: containIgnoreCase, function, expression, journey
exl-id: 26074584-a215-4515-8a61-7460bd9d4447
version: Journey Orchestration
---
# containIgnoreCase {#containIgnoreCase}

Checks if the second argument string is contained in the first argument string, without taking into account the case.

## Category

String

## Function syntax

`containIgnoreCase(<parameters>)`

## Parameters

| Parameter | Type             |
|-----------|------------------|
| string   | string |
| string searched   | string |

## Signature and returned type

`containIgnoreCase(<string>,<string>)`

Returns a boolean.

## Example

`containIgnoreCase("rowing is great", "GREAT")`

Returns true.
