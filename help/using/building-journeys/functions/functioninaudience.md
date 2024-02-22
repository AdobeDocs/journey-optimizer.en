---
product: journey optimizer
title: inAudience
description: Learn about the function inAudience
feature: Journeys
role: Data Engineer, Architect
level: Experienced
keywords: inAudience, function, expression, journey
exl-id: 8417af75-6e97-4ad4-86b4-3ecd264a5560
---
# inAudience {#inAudience}

Checks if an individual belongs to a given audience.

>[!NOTE]
>
>You can retrieve up to 100 audiences.

The audience name must be a string constant. It cannot be a field reference nor an expression.

Audiences are defined in the [Adobe Experience Platform](https://platform.adobe.com/audience/overview). The expression editor provides an autocompleted list of audiences.

Audiences can have three statuses:

* existing: entity continues to be in the audience.
* realized: entity is entering the audience.
* exited: entity is exiting the audience.

Only the individuals with the **Realized** and **Existing** audience participation statuses will be considered as members of the audience. For more on how to evaluate an audience, refer to the [Segmentation Service documentation](https://experienceleague.adobe.com/docs/experience-platform/segmentation/tutorials/evaluate-a-segment.html#interpret-segment-results). 

`inAudience('audienceName') == true` means that you have an segmentMembership with the entered/existing status.

`inAudience('audienceName') == false` means that you have an segmentMembership of the exited status.

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

The function will return **[!UICONTROL true]** if the individual within the journey instance is part of the Adobe Experience Platform audience named “men over 50”, **[!UICONTROL false]** otherwise.
