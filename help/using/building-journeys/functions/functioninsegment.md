---
product: journey optimizer
title: inSegment
description: Learn about the function inSegment
feature: Journeys
role: Developer
level: Experienced
keywords: inSegment, function, expression, journey
exl-id: 8417af75-6e97-4ad4-86b4-3ecd264a5560
version: Journey Orchestration
feature_v2: []
subfeature_v2: []
---
# inSegment {#inSegment}

Checks if an individual belongs to a given audience.

>[!NOTE]
>
>You can retrieve up to 100 audiences.

The audience name must be a string constant. It cannot be a field reference nor an expression.

Audiences are defined in the [Adobe Experience Platform](https://platform.adobe.com/audience/overview). The expression editor provides an autocompleted list of audiences.

Audiences can have two statuses:

* realized: Entity qualifies for the segment definition.
* exited: Entity is exiting the segment definition.

Only the individuals with the **Realized** audience participation status will be considered as members of the audience. For more on how to evaluate an audience, refer to the [Segmentation Service documentation](https://experienceleague.adobe.com/docs/experience-platform/segmentation/tutorials/evaluate-a-segment.html#interpret-segment-results). 

`inSegment('segmentName') == true` means that you have a segmentMembership with the entered/existing status.

`inSegment('segmentName') == false` means that you have a segmentMembership of the exited status.

## Category

Adobe Experience Platform

## Function syntax

`inSegment(<parameter>)`

## Parameters

|Parameter|Description|Type|
|--- |--- |--- |
|Segment|The audience name |`<string>`|

## Signature and returned type

`inSegment(<string>)`

Returns a boolean.

## Example

`inSegment("men over 50")`

Explanation:

The function will return **[!UICONTROL true]** if the individual within the journey instance is part of the Adobe Experience Platform audience named "men over 50", **[!UICONTROL false]** otherwise.

+++AI Assistant — Page context

* **TL;DR:** This page documents the legacy `inSegment` function, which checks whether a journey profile belongs to a named Adobe Experience Platform audience and returns a boolean.

**Intents:**
* Check if a profile is an active member of a named audience using `inSegment`
* Use `inSegment('name') == true` to confirm realized (active) audience membership in a journey condition
* Use `inSegment('name') == false` to confirm exited (inactive) audience membership

**Glossary:**
* **Realized**: Audience participation status meaning the entity currently qualifies for the segment definition *(product-specific)*
* **Exited**: Audience participation status meaning the entity is leaving or has left the segment definition *(product-specific)*

**Guardrails:**
* Up to 100 audiences can be retrieved in a single journey
* The audience name must be a string constant; field references and expressions are not supported as parameters

**Terminology:**
* Canonical name: inSegment — Acronym: none — variants: inAudience (current preferred function)
* Synonyms: "inSegment" = "audience membership check" (legacy)
* Do not confuse: "inSegment" (legacy/deprecated function) ≠ "inAudience" (current recommended function)
* Do not confuse: "realized" (active member) ≠ "exited" (no longer a member)

**FAQ:**
* **Q: What is the difference between `inSegment` and `inAudience`?** — `inSegment` is the legacy function name; `inAudience` is the current recommended function. Both check audience membership, but `inAudience` has more complete documentation including guardrails and propagation timing details.
* **Q: What does `inSegment('name') == true` mean?** — It means the profile has a "realized" segmentMembership status, i.e., the individual is an active member of the audience.
* **Q: Can I pass a dynamic expression as the audience name?** — No, the audience name must be a string constant; field references and expressions are not supported.
* **Q: How many audiences can I evaluate in one journey?** — Up to 100 audiences can be retrieved within a single journey.

+++
