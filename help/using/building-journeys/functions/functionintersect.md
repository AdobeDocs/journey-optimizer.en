---
product: journey optimizer
title: intersect
description: Learn about the function intersect
feature: Journeys
role: Data Engineer, Architect
level: Experienced
keywords: intersect, function, expression, journey
exl-id: e236efa9-91a8-4f08-94c6-45f1e060bb2f
---
# intersect{#intersect}

Returns the common values in the two input lists. If one of the two lists is null, returns an empty list.

## Category

List

## Function syntax

`intersect(<parameters>)`

## Parameters

| Parameter | Type             |
|-----------|------------------|
| list 1 | list |
| list 2 | list |

## Signatures and returned types

`intersect(listString,listString)`: listString
`intersect(listDecimal,listDecimal)`: listDecimal
`intersect(listInteger,listInteger)`: listInteger
`intersect(listDateTime,listDateTime)`: listDateTime
`intersect(listDateTimeOnly,listDateTimeOnly)`: listDateTimeOnly
`intersect(listDateOnly,listDateOnly)`: listDateOnly
`intersect(listDuration,listDuration)`: listDuration
`intersect(listBoolean,listBoolean)`: listBoolean

Returns a list.

## Examples

```json
intersect(
    ["sports", "news", "documentary"],
    ["sports", "movies", "documentary"]
)
```

Returns ["sports", "news"]

```json
intersect(
    #{ExperienceDataPlatform.profile.interests},
    ["sports", "documentary"]
)
```

Returns common items between profile attributes and given list of categories.

```json
intersect(
    #{ExperienceDataPlatform.profile.interests},
        @event{myEvent.sport_interests}
)
```

Returns common items between profile attributes and given event field.
