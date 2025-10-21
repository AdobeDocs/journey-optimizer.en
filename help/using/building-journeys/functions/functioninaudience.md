---
product: journey optimizer
title: inAudience
description: Learn about the function inAudience
feature: Journeys
role: Developer
level: Experienced
keywords: inAudience, function, expression, journey
exl-id: 8417af75-6e97-4ad4-86b4-3ecd264a5560
version: Journey Orchestration
---
# inAudience {#inAudience}

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

`inAudience('audienceName') == true` means that you have a segmentMembership with the entered status.

`inAudience('audienceName') == false` means that you have a segmentMembership of the exited status.


>[!IMPORTANT]
>
>Changing the name of an existing audience does not automatically update any references to that audience in your journey expressions. If your condition node uses `inAudience('oldAudienceName')`, you must manually edit the expression to use the new name. Failure to do so will cause the journey condition to break.

## Category

Adobe Experience Platform

## Function syntax

`inAudience(<parameter>)`

## Parameters

|Parameter|Description|Type|
|--- |--- |--- |
|Audience|The audience name |`<string>`|

## Signature and returned type

`inAudience(<string>)`

Returns a boolean.

## Example

`inAudience("men over 50")`

Explanation:

The function will return **[!UICONTROL true]** if the individual within the journey instance is part of the Adobe Experience Platform audience named "men over 50", **[!UICONTROL false]** otherwise.

