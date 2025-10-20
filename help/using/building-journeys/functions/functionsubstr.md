---
product: journey optimizer
title: substr
description: Learn about the function substr
feature: Journeys
role: Engineer
level: Experienced
keywords: substr, function, expression, journey
exl-id: 58a3107a-b4f3-43da-b454-5ce597515847
version: Journey Orchestration
---
# substr {#substr}

Returns the sub-string of the string expression between the begin index and the end index. If the end index is not defined, then it is between the begin index and the end.

## Category

String

## Function syntax

`substr(<parameters>)`

## Parameters

| Parameter  | type |
|-------------|----------|
| string | string |
| beginIndex | integer |
| endIndex | integer |

## Signature and returned type

`substr(<string>,<beginIndex>)`

`substr(<string>,<beginIndex>,<endIndex>)`

Return a string.

## Example

`substr("Hello World",6)`

Returns "World".

`substr("Hello World", 0, 5)`

Returns "Hello".
