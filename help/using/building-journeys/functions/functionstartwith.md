---
product: journey optimizer
title: startWith
description: Learn about the function startWith
feature: Journeys
role: Data Engineer, Architect
level: Experienced
keywords: startWith, function, expression, journey
exl-id: 1abdf947-2873-4e45-a26c-cb895980e76a
version: Journey Orchestration
---
# startWith {#startWith}

Returns true if the second parameter is a prefix of the first one.

## Category

String

## Function syntax

`startWith(<parameters>)`

## Parameters

| Parameter   | Type  |
|-------------|--------|
| string      | string |
| prefix      | string |

## Signature and returned type

`startWith(<string>,<string>)`

Return a boolean.

## Example

`startWith("Hello World", "Hello")`

Returns true.

`startWith("Hello World", "World")`

Returns false.
