---
product: journey optimizer
title: startWithIgnoreCase
description: Learn about the function startWithIgnoreCase
feature: Journeys
role: Data Engineer, Architect
level: Experienced
keywords: startWithIgnoreCase, function, expression, journey
exl-id: b6bd9f77-272f-4c2b-b085-20ab5f043793
version: Journey Orchestration
---
# startWithIgnoreCase {#startWithIgnoreCase}

Returns true if the second parameter is a prefix of the first one without considering case.

## Category

String

## Function syntax

`startWithIgnoreCase(<parameters>)`

## Parameters

| Parameter   | Type  |
|-------------|--------|
| string      | string |
| prefix      | string |

## Signature and returned type

`startWithIgnoreCase(<string>,<string>)`

Return a boolean.

## Example

`startWithIgnoreCase("rowing is great", "RO")`

Returns true.
