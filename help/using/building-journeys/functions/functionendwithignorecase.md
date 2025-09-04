---
product: journey optimizer
title: endWithIgnoreCase
description: Learn about the function endWithIgnoreCase
feature: Journeys
role: Data Engineer, Architect
level: Experienced
keywords: endWithIgnoreCase, function, expression, journey
exl-id: 278ef1a4-571c-4b5f-b4de-0cfc644ac7d7
version: Journey Orchestration
---
# endWithIgnoreCase {#endWithIgnoreCase}

Checks if the first argument string ends with a specific string (second argument string), not taking into account the case.

## Category

String

## Function syntax

`endWithIgnoreCase(<parameters>)`

## Parameters

| Parameter | Type             |
|-----------|------------------|
| string   | string |
| suffix  | string |

## Signature and returned type

`endWithIgnoreCase(<string>,<string>)`

Returns a boolean.

## Example

`endWithIgnoreCase("rowing is great", "AT")`

Returns true.
