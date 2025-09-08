---
product: journey optimizer
title: endWith
description: Learn about the function endWith
feature: Journeys
role: Data Engineer, Architect
level: Experienced
keywords: endWith, function, expression, journey
exl-id: ae54c127-9de2-42fd-942c-664d2cfe66d2
version: Journey Orchestration
---
# endWith {#endWith}

Returns true if the second parameter is a suffix of the first one.

## Category

String

## Function syntax

`endWith(<parameters>)`

## Parameters

| Parameter | Type             |
|-----------|------------------|
| string   | string |
| suffix   | string |

## Signature and returned type

`endWith(<string>,<string>)`

Returns a boolean.

## Example

`endWith("Hello World", "World")`

Returns true.

`endWith("Hello World", "Hello")`

Returns false.
