---
product: journey optimizer
title: concat
description: Learn about the function concat
feature: Journeys
role: Data Engineer, Architect
level: Experienced
keywords: concat, function, expression, journey
exl-id: 690c8aa9-f754-4720-b4ed-a338e5d3b79d
version: Journey Orchestration
---
# concat {#concat}

Concatenates two string parameters or a list of strings.

## Category

String

## Function syntax

`concat(<parameters>)`

## Parameters

| Parameter | Type             |
|-----------|------------------|
| List      | listString       |
| string   | string |

## Signature and returned type

`concat(<string>,<string>)`

`concat(<listString>)`

Returns a string.

## Example

`concat("Hello","World")`

Returns "HelloWorld".

`concat(["Hello"," ","World"])`

Returns "Hello World".
