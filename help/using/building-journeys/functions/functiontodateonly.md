---
product: journey optimizer
title: toDateOnly
description: Learn about the function toDateOnly
feature: Journeys
role: Data Engineer, Architect
level: Experienced
keywords: toDateOnly, function, expression, journey
exl-id: 1929644f-8b51-4f95-aea5-627fc1dd115d
---
# toDateOnly{#toDateOnly}

Converts an argument into a dateOnly type value. To learn more on data types, refer to this [section](../expression/data-types.md).

## Category

Conversion

## Function syntax

`toDateOnly(<parameters>)`

## Parameters

| Parameter | Type             |
|-----------|------------------|
| String representation of a date as "YYYY-MM-DD" (XDM format). Also supports ISO-8601 format: only **full-date** part is considered (Refer to [RFC 3339, section 5.6](https://www.rfc-editor.org/rfc/rfc3339#section-5.6) | string |
| date time | dateTime|
| date time without time zone | dateTimeOnly|
| integer value of an epoch in milliseconds| integer |

## Signatures and returned types

`toDateOnly(<dateTime>)`

`toDateOnly(<dateTimeOnly>)`

`toDateOnly(<string>)`

`toDateOnly(<integer>, <integer>, <integer>)`

Returns a dateOnly type value.

## Examples

`toDateOnly("2023-08-18")`

`toDateOnly("2023-08-18T00:00:00.000Z")`

`toDateOnly("2023-08-18T00:00:00")`

all return a dateOnly object representing 2023-08-18.

`toDateOnly(#{ExperiencePlatform.ProfileFieldGroup.person.birthDate})`

Returns a dateOnly.
