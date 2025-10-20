---
product: journey optimizer
title: split
description: Learn about the function split
feature: Journeys
role: Engineer
level: Experienced
keywords: split, function, expression, journey
exl-id: 37bcdf98-203c-4f82-8d8a-be2b2c45c4e7
version: Journey Orchestration
---
# split {#split}

Splits the first argument string with a separator string (second argument string, which can be a regular expression) to produce a list of strings (tokens).

## Category

String

## Function syntax

`split(<parameters>)`

## Parameters

|Parameter|Type|
|-----------|------------------|
|input string|string|
|separator string|string|

## Signatures and returned type

`split(<input string>, <separator string>)`

Returns a listString.

## Example

`split("A_B_C", "_")`

Returns `["A","B","C"]`

Example with an event field 'event.appVersion' with value: "20.45.2.3434"

`split(@event{event.appVersion}, "\\.")`

Returns `["20", "45", "2", "3434"]`
