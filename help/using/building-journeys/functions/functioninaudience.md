---
product: journey optimizer
title: inAudience function
description: Learn about the Adobe Experience Platform inAudience function
feature: Journeys
role: Developer
level: Experienced
keywords: inAudience, function, expression, journey, audience, segmentation
exl-id: 8417af75-6e97-4ad4-86b4-3ecd264a5560
version: Journey Orchestration
---
# inAudience function {#inAudience}

The `inAudience` function is an Adobe Experience Platform function that enables you to check whether an individual in your journey belongs to a specific audience. This powerful function allows you to create personalized journey paths based on audience membership, enabling sophisticated segmentation and targeting within your customer experiences.

Use the `inAudience` function when you need to:

* [Branch journey paths based on audience membership](../condition-activity.md#using-a-segment)
* Apply conditional logic that depends on whether a profile belongs to a specific segment
* Target specific groups of customers with personalized experiences
* Evaluate real-time audience participation within journey conditions
* Combine multiple audience checks to create complex targeting rules

The function evaluates audience membership in real-time and returns a boolean value, making it ideal for decision nodes and conditional expressions. Audiences are defined and managed in [Adobe Experience Platform](https://platform.adobe.com/audience/overview){target="_blank"} (learn more about [working with audiences](../../audience/about-audiences.md) in Journey Optimizer), and the expression editor provides autocomplete suggestions to help you reference them accurately.

**Audience Status:**

Audiences can have two participation statuses:

* **Realized**: The individual qualifies for the audience definition and is an active member
* **Exited**: The individual has left the audience and no longer qualifies

Only individuals with the **Realized** status will be considered as active audience members. When the function returns `true`, it confirms the individual has realized status; when it returns `false`, it indicates exited status. For more information on audience evaluation, refer to the [Segmentation Service documentation](https://experienceleague.adobe.com/docs/experience-platform/segmentation/tutorials/evaluate-a-segment.html#interpret-segment-results){target="_blank"}.

+++Syntax

`inAudience(<parameter>)`

+++

+++Parameters

|Parameter|Description|Type|
|--- |--- |--- |
|Audience|The audience name |`<string>`|

**Important constraints:**

* The audience name must be a string constant
* It cannot be a field reference or an expression
* You can retrieve up to 100 audiences in a single journey

+++

+++Signature and returned type

`inAudience(<string>)`

Returns a boolean:
* `true`: The individual is a member of the audience (realized status)

* `false`: The individual is not a member of the audience (exited status)

+++

+++Examples

`inAudience("men over 50")`

Returns **true** if the individual within the journey instance is part of the Adobe Experience Platform audience named "men over 50", **false** otherwise.

**Practical use cases:**

```
// Simple audience check in a condition
inAudience("Premium Customers") == true

// Multiple audience evaluation
inAudience("High Value Customers") == true AND inAudience("Active Last 30 Days") == true

// Negation check
inAudience("Unsubscribed") == false
```

+++

## Guardrails and limitations {#guardrails}

When using the `inAudience` function in your journeys, be aware of the following guardrails and limitations:

**Audience retrieval limit:**
* You can retrieve up to 100 audiences within a single journey
* The expression editor provides an autocompleted list of available audiences to help you reference them correctly

**Parameter constraints:**
* The audience name must be a string constant
* Field references and expressions are not supported as parameters

**Audience name changes:**
* Changing the name of an existing audience in Adobe Experience Platform does not automatically update any references to that audience in your journey expressions
* If your condition node uses `inAudience('oldAudienceName')`, you must manually edit the expression to use the new name
* Failure to update the audience name will cause the journey condition to break and may result in incorrect journey behavior

**Merge policy considerations:**
* When using multiple audiences with the `inAudience` function, inconsistencies with merge policies can cause errors or alerts
* Refer to [Journey properties](../journey-properties.md) for more information on merge policy behavior

## Related topics

Learn more about using audiences in Adobe Journey Optimizer:

* **[About audiences](../../audience/about-audiences.md)** - Understand how audiences work in Adobe Experience Platform and Journey Optimizer, including how to create and manage them
* **[Read Audience activity](../read-audience.md)** - Use audiences to trigger journey entry and make all audience members enter a journey
* **[Audience Qualification events](../audience-qualification-events.md)** - Listen to profile entrances and exits from audiences to trigger journey actions in real-time
* **[Using audiences in conditions](../condition-activity.md#using-a-segment)** - Create conditional journey paths based on audience membership using the Condition activity
* **[Journey properties - Merge policies](../journey-properties.md)** - Understand how merge policies work when using multiple audiences with the inAudience function

