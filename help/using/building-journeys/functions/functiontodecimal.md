---
product: journey optimizer
title: toDecimal
description: Learn about the function toDecimal
feature: Journeys
role: Developer
level: Experienced
keywords: decimal, function, expression, journey
exl-id: d761fa4d-5f99-4dee-b747-3eab464c4071
version: Journey Orchestration
---
# toDecimal {#toDecimal}

Converts an argument value into a decimal value, depending on its type.

## Category

Conversion

## Function syntax

`toDecimal(<parameter>)`

## Parameters

|Parameter|Description|
|--- |--- |
|string|converts the string value as a decimal|
|dateTime|converts the date as the number of milliseconds (epoch milliseconds)|
|boolean|converts the boolean value as 1 if true, 0 if false|
|integer|converts to a decimal (example.: 1 becomes 1.0)|

## Signatures and returned types

`toDecimal(<integer>)`

`toDecimal(<decimal>)`

`toDecimal(<string>)`

`toDecimal(<boolean>)`

Return a decimal.

## Examples

`toDecimal("4.0")`

Returns 4.0.
