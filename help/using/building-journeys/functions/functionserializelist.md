---
product: journey optimizer
title: serializeList
description: Learn about the function serializeList
feature: Journeys
role: Data Engineer, Architect
level: Experienced
keywords: serializeList, function, expression, journey
exl-id: 7ead9fa1-59b3-4960-818c-fe6321422952
---
# serializeList {#serializeList}

Converts the list (any type) given in the first parameter to a string. The second parameter represents the separator to use. The third parameter is a boolean value indicating if each element of the expression should include quotes.

## Category

List

## Function syntax

`serializeList(<parameters>)`

## Parameters

| Parameter | Type             |
|-----------|------------------|
| String    | String           |
| Boolean   | Boolean          |
| DateTimeOnly | DateTimeOnly  |
| List      | listString       |
| List      | listBoolean      |
| List      | listPoint        |
| List      | listDecimal      |
| List      | listDuration     |
| List      | listDateTime     |
| List      | listDateTimeOnly |
| List      | listDateOnly     |

## Signature and returned type

`serializeList(<listInteger>,<string>,<boolean>)`

`serializeList(<listDecimal>,<string>,<boolean>)`

`serializeList(<listString>,<string>,<boolean>)`

`serializeList(<listBoolean>,<string>,<boolean>)`

`serializeList(<listDateTimeOnly>,<string>,<boolean>)`

`serializeList(<listDateTime>,<string>,<boolean>)`

`serializeList(<listDateOnly>,<string>,<boolean>)`

`serializeList(<listDuration>,<string>,<boolean>)`

`serializeList(<listPoint>,<string>,<boolean>)`

Return a string.

## Example

`serializeList(["Hello","World"], " ", false)`

Returns "Hello World".

`serializeList(["Hello", "World"], ",", true)`

Returns ""Hello","World"".
