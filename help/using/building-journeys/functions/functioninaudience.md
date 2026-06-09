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
TQID: https://experienceleague.adobe.com/DU8HtduB2-GmakiaHBMFU1vzBBPoVTNvrOCPWQrr5SU
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: ad78185d-8f79-40ad-9bad-cbde74af74ee
    internal-label: Guardrails and limitations
  - id: d998adac-2f81-400b-a669-d07bb196e4eb
    internal-label: Journeys
subfeature_v2:
  - id: fa683eda-48de-4558-af32-2673edcd44fe
    internal-label: Events
role_v2:
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
topic_v2:
  - id: bce87dde-a4ab-44c9-8a18-ad66e4ddb377
    internal-label: Customer experience
---
# inAudience function {#inAudience}

The `inAudience` function is an Adobe Experience Platform function that enables you to check whether an individual in your journey belongs to a specific audience. This powerful function allows you to create personalized journey paths based on audience membership, enabling sophisticated segmentation and targeting within your customer experiences.

Use the `inAudience` function when you need to:

* Branch journey paths based on audience membership. [Learn more](../conditions.md#using-a-segment)
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

**Propagation timing:** {#propagation-timing}

When using `inAudience()` in a condition node, segment membership evaluation timing varies depending on where the condition appears in the journey:

* **In a Read Audience journey, before a Wait activity:** Journey Optimizer reads from the batch projection of the profile. Data in this projection is refreshed within **2 hours** after ingestion. Audiences that rely on day-based or time-based conditions may experience additional delay. Add a short [Wait activity](../wait-activity.md) at the start of the journey, or allow buffer time to ensure the latest segment membership is reflected.
* **In a unitary event journey, or after a Wait activity:** Segment membership is read from the streaming (unitary) projection. Data is typically available within **15 minutes**. For more details, refer to the [Adobe Experience Platform streaming ingestion documentation](https://experienceleague.adobe.com/en/docs/experience-platform/ingestion/streaming/overview){target="_blank"}.

## Related topics

Learn more about using audiences in Adobe Journey Optimizer:

* **[About audiences](../../audience/about-audiences.md)** - Understand how audiences work in Adobe Experience Platform and Journey Optimizer, including how to create and manage them
* **[Read Audience activity](../read-audience.md)** - Use audiences to trigger journey entry and make all audience members enter a journey
* **[Audience Qualification events](../audience-qualification-events.md)** - Listen to profile entrances and exits from audiences to trigger journey actions in real-time
* **[Using audiences in conditions](../conditions.md#using-a-segment)** - Create conditional journey paths based on audience membership using the Optimize activity
* **[Journey properties - Merge policies](../journey-properties.md)** - Understand how merge policies work when using multiple audiences with the inAudience function

+++AI Assistant — Page context

- **TL;DR:** This page documents the `inAudience` function, which checks in real-time whether a journey profile belongs to a named Adobe Experience Platform audience and returns a boolean used in journey conditions.

**Intents:**
- Branch a journey path based on whether a profile is a member of a specific audience using `inAudience`
- Combine multiple `inAudience` checks with AND/OR logic to create complex targeting conditions
- Verify that a profile has not entered a specific audience using a negation check (`inAudience("...") == false`)
- Understand the propagation timing differences between Read Audience journeys and unitary event journeys
- Identify and fix broken audience references caused by audience renames in Adobe Experience Platform

**Glossary:**
- **Realized**: Audience participation status indicating the individual currently qualifies for the audience definition and is an active member *(product-specific)*
- **Exited**: Audience participation status indicating the individual has left the audience and no longer qualifies *(product-specific)*
- **Merge policy**: A rule in Adobe Experience Platform that determines how profile data from multiple datasets is combined when evaluating audience membership *(product-specific)*
- **Batch projection**: The profile data store refreshed on a schedule (within 2 hours after ingestion) used by Read Audience journeys *(product-specific)*
- **Streaming projection**: The real-time profile data store (typically available within 15 minutes) used in unitary event journeys and after Wait activities *(product-specific)*

**Guardrails:**
- A single journey can retrieve up to 100 audiences
- The audience name parameter must be a string constant; field references and dynamic expressions are not supported
- Renaming an audience in Adobe Experience Platform does not automatically update `inAudience` references in journey expressions — manual updates are required
- Inconsistent merge policies across multiple audiences used in the same journey can cause errors or alerts

**Terminology:**
- Canonical name: inAudience — Acronym: none — variants: inSegment (legacy name)
- Synonyms: "inAudience" = "audience membership check function"
- Do not confuse: "Realized" (active member) ≠ "Exited" (no longer a member)
- Do not confuse: "inAudience" (current function) ≠ "inSegment" (deprecated legacy function)

**FAQ:**
- **Q: What does `inAudience` return when a profile has exited the audience?** — It returns `false`; only profiles with "Realized" status are considered active members and return `true`.
- **Q: How many audiences can I check in a single journey?** — Up to 100 audiences can be retrieved within a single journey.
- **Q: What happens if I rename an audience in Adobe Experience Platform after using it in a journey?** — The journey expression is not updated automatically; you must manually edit the `inAudience` call to use the new audience name, otherwise the condition will break.
- **Q: How quickly is audience membership available after a profile update in a Read Audience journey?** — In a Read Audience journey before a Wait activity, data is read from the batch projection refreshed within 2 hours after ingestion.
- **Q: Can I pass a profile attribute as the audience name parameter?** — No, the audience name must be a string constant; field references and expressions are not supported.

+++
