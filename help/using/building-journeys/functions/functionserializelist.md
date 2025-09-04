---
product: journey optimizer
title: serializeList
description: Learn about the function serializeList
feature: Journeys
role: Data Engineer, Architect
level: Experienced
keywords: serializeList, function, expression, journey
exl-id: 7ead9fa1-59b3-4960-818c-fe6321422952
version: Journey Orchestration
---
# serializeList {#serializeList}

Converts a given list (any type except listObject) into a string.

## Category

List

## Function syntax

`serializeList(<parameters>)`

## Parameters

| Parameter | Type             | Description             |
|-----------|------------------|------------------|
| listToProcess | listString, listBoolean, listInteger, listDecimal, listDuration, listDateTime, listDateTimeOnly, listDateOnly | List to convert into a string. |
| separator | string | Separator between each list element in the output string. |
| addQuotes | boolean | This parameter indicates if each element in the output string should include quotes (true) or not (false). |

## Signature and returned type

`serializeList(<listInteger>,<string>,<boolean>)`

`serializeList(<listDecimal>,<string>,<boolean>)`

`serializeList(<listString>,<string>,<boolean>)`

`serializeList(<listBoolean>,<string>,<boolean>)`

`serializeList(<listDateTimeOnly>,<string>,<boolean>)`

`serializeList(<listDateTime>,<string>,<boolean>)`

`serializeList(<listDateOnly>,<string>,<boolean>)`

`serializeList(<listDuration>,<string>,<boolean>)`

Return a string.

## Example

`serializeList(["Hello","World"], " ", false)`

Returns "Hello World".

`serializeList(["Hello", "World"], ",", true)`

Returns ""Hello","World"".
