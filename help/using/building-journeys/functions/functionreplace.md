---
product: journey optimizer
title: replace
description: Learn about the function replace
feature: Journeys
role: Data Engineer, Architect
level: Experienced
keywords: replace, function, expression, journey
exl-id: 3eb35fd6-2d11-4f24-b0d9-5334e7ed7872
version: Journey Orchestration
---
# replace {#replace}

Replaces the first occurrence matching the target string by the replacement string in the base string.

The replacement proceeds from the beginning of the string to the end, for example, replacing "aa" with "b" in the string "aaa" will result in "ba" rather than "ab".

## Category

String

## Function syntax

`replace(<parameters>)`

## Parameters

| Parameter | Type         |
|-----------|--------------|
| base      | string       |
| target    | string (RegExp)       |
| replacement  | string    |

## Signature and returned type

`replace(<base>,<target>,<replacement>)`

Return a string.

## Example 1

`replace("Hello World", "l", "x")`

Returns "Hexlo World".

## Example 2 {#example_2}

Because the target parameter is a RegExp, depending on the string you want to replace, you may need to escape some characters. Here is an example:

* string to evaluate: `|OFFER_A|OFFER_B`
* provided by a profile attribute `#{ExperiencePlatform.myFieldGroup.profile.myOffers}`
* String to be replaced: `|OFFER_A`
* String replaced by: `''`
* You need to add `\\` before the `|` character.

The expression is:

`replace(#{ExperiencePlatform.myFieldGroup.profile.myOffers}, '\\|OFFER_A', '')`

The returned string is: `|OFFER_B`

You can also build the string to be replaced from a given attribute:

`replace(#{ExperiencePlatform.myFieldGroup.profile.myOffers}, '\\|' + #{ExperiencePlatform.myFieldGroup.profile.myOfferCode}, '')`
