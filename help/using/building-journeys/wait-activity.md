---
solution: Journey Optimizer
product: journey optimizer
title: Wait activity
description: Learn how to configure the wait activity
feature: Journeys, Activities
topic: Content Management
role: User
level: Intermediate
keywords: wait, activity, journey, next, canvas
exl-id: 7268489a-38c1-44da-b043-f57aaa12d7d5
version: Journey Orchestration
TQID: https://experienceleague.adobe.com/qWxnLiuHh-sJQyUOuRB6CgRIpZ6ud6eO-WNoWcv9JeU
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: b3538224-471e-4c63-a444-9b19d89ae29c
    internal-label: Activities
  - id: d998adac-2f81-400b-a669-d07bb196e4eb
    internal-label: Journeys
subfeature_v2:
  - id: c3f67a94-f1ff-4f5e-bf6f-bc22405930a3
    internal-label: Wait activity
  - id: fa683eda-48de-4558-af32-2673edcd44fe
    internal-label: Events
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
level_v2:
  - id: b5a62a22-46f7-4f0d-b151-3fc640bef588
    internal-label: Intermediate
topic_v2:
  - id: aa2f3246-cb95-4b30-8899-fdf7d73550cc
    internal-label: Reporting
  - id: e0eb8757-182f-49f3-94a4-1587d16f5094
    internal-label: Personalization
---
# Wait activity {#wait-activity}

>[!CONTEXTUALHELP]
>id="ajo_journey_wait"
>title="Wait activity"
>abstract="The Wait activity lets you wait before executing the next activity in the path. It allows you to define the moment when the next activity will be executed. Two options are available: duration and custom."

You can use a **[!UICONTROL Wait]** activity to define a duration before executing the next activity.  The maximum wait duration is **90 days**. 

You can set two types of **Wait** activity:

* A wait based on a relative duration. [Learn more](#duration) 
* A custom date, using functions to calculate it. [Learn more](#custom) 

<!--
* [Email send time optimization](#email_send_time_optimization)
* [Fixed date](#fixed_date) 
-->

## Recommendations {#wait-recommendations}

Use these recommendations to keep waits predictable and safe.

### Multiple Wait activities {#multiple-wait-activities}

When using multiple **Wait** activities in a journey, be aware that the [global timeout](journey-properties.md#global_timeout) for journeys is 91 days, meaning that profiles are always drop out of the journey maximum 91 days after they entered it. Learn more on [this page](journey-properties.md#global_timeout).

An individual can enter a **Wait** activity only if they have enough time left in the journey to complete the wait duration before the 91 days journey timeout. 

### Wait and reentrance {#wait-reentrance}

A best practice to not use **Wait** activities to block reentrance. Instead, use the **Allow reentrance** option at the journey properties level. Learn more on [this page](../building-journeys/journey-properties.md#entrance).

### Wait and test mode {#wait-test-mode}

In test mode, the **[!UICONTROL Wait time in test]** parameter allows you to define the time that each **Wait** activity will last. The default time is 10 seconds. This will ensure that you get the test results quickly. Learn more on [this page](../building-journeys/testing-the-journey.md).

### Wait and mobile channels {#wait-mobile-channels}

If you want to show an [in-app message](../in-app/create-in-app.md) shortly after sending a [push notification](../../rp_landing_pages/push-landing-page.md), use a **Wait** activity to allow the in-app message payload time to propagate. Typically a 5–15 minute wait is recommended, but exact times can vary depending on payload complexity and personalization needs.

## Configuration {#wait-configuration}

Configure wait duration and timing here.

### Duration wait {#duration}

Select the **Duration** type to set the relative duration of the wait before the execution of the next activity. The maximum duration is **90 days**.

![Define the wait duration](assets/journey55.png)

<!--
## Fixed date wait{#fixed_date}

Select the date for the execution of the next activity.

![Wait activity configuration panel with duration and fixed date options](assets/journey56.png)
-->

### Custom wait {#custom}

Select the **Custom** type to define a custom date, using an advanced expression based on a field coming from an event or a custom action response. You cannot define a relative duration directly, for example, 7 days, but you can use functions to calculate it if needed (eg: 2 days after purchase). 

![Define a custom wait with an expression](assets/journey57.png)

The expression in the editor should provide a `dateTimeOnly` format. Refer to [this page](expression/expressionadvanced.md). For more information on dateTimeOnly format, refer to [this page](expression/data-types.md).

Best practice is to use custom dates that are specific to your profiles, and avoid using the same date for all. For example, do not define `toDateTimeOnly('2024-01-01T01:11:00Z')` but rather `toDateTimeOnly(@event{Event.productDeliveryDate})` which is specific to each profile. Be aware that using fixed dates can cause issues on your journey execution. Learn more about the impact of Wait activities on journey processing rate in [this section](entry-management.md#wait-activities-impact). 


>[!CAUTION]
>
>When working with `dateTimeOnly` expressions, keep the following in mind:
>
>* You can use a `dateTimeOnly` expression directly, or convert to it using a function — for example: `toDateTimeOnly(@event{Event.offerOpened.activity.endTime})` where the field value is in the form `2023-08-12T09:46:06Z`.
>* The **time zone** is defined in the journey properties. As a result, it is not possible from the UI to point at a full ISO-8601 timestamp that mixes time and time zone offset, such as `2023-08-12T09:46:06.982-05`. [Learn more](../building-journeys/timezone-management.md)
>* When building a custom wait expression with `toDateTimeOnly()`, do **not** append `Z` or a time zone offset (e.g., `-05:00`). The expression must reference the journey's configured time zone without explicit time zone designators — otherwise profiles may get stuck in the wait activity.
>
>| | Example |
>| --- | --- |
>| **Correct** | `toDateTimeOnly(concat(toString(toDateOnly(nowWithDelta(2, "days"))),"T10:00:00"))` |
>| **Incorrect** | `toDateTimeOnly(concat(toString(toDateOnly(nowWithDelta(2, "days"))),"T10:00:00Z"))` ❌ (contains `Z`) |

To validate that the wait activity works as expected, you can use step events. [Learn more](../reports/query-examples.md#common-queries).

## Profile refresh after wait {#profile-refresh}

When a profile is parked at a **Wait** activity in a journey starting with a **Read Audience** activity, the journey automatically refreshes the profile's attributes from the Unified Profile Service (UPS) to fetch the latest available data.

* **At journey entry**: Profiles use attribute values from the audience snapshot that was evaluated when the journey started.
* **After a wait node**: The journey performs a lookup to retrieve the latest profile data from UPS, not the older snapshot data. This means profile attributes may have changed since the journey began.

This behavior ensures that downstream activities use current profile information after a wait period. However, it may produce unexpected results if you expect the journey to use only the original snapshot data throughout execution.

Example: If a profile qualifies for a "silver customer" audience at journey start, but upgrades to "gold customer" during a 3-day wait, activities after the wait will see the updated "gold customer" status.

## Automatic wait node  {#auto-wait-node}

>[!CONTEXTUALHELP]
>id="ajo_journey_auto_wait_node"
>title="About the automatic wait node"
>abstract="A **Wait** node is automatically inserted after this inbound action. It is set to 3 days by default, ensuring profiles remain in the journey long enough to view the message or experience. The wait duration can be updated, or the node removed, if the use case requires it."

Each inbound experience activity (In-app message, Code-based experience, or Card) comes with a 3-days **Wait** activity. As inbound messages automatically end when a profile reach out the end of the journey, we assume that you want your users to see it at least for 3 days. You can remove this **Wait** activity, or change its configuration if needed.

+++AI Assistant — Page context

* **TL;DR:** This page explains how to configure the Wait activity in a journey to pause profile progression for a relative duration or until a custom calculated date before executing the next step.

**Intents:**

* Add a Wait activity to pause a journey for a fixed relative duration (up to 90 days)
* Configure a custom Wait using an advanced expression to delay until a profile-specific calculated date
* Understand how Wait activities interact with the journey global timeout (91 days)
* Use the Wait time in test parameter to speed up test mode validation
* Understand how profile attributes are refreshed after a Wait node in Read Audience journeys

**Glossary:**

* **Wait activity**: A journey orchestration activity that pauses profile progression for a specified duration or until a calculated date before the next activity executes *(product-specific)*
* **Duration wait**: A Wait type that sets a relative time period to pause, with a maximum of 90 days *(product-specific)*
* **Custom wait**: A Wait type that uses a `dateTimeOnly` expression derived from profile or event data to define a specific future date/time for resumption *(product-specific)*
* **Automatic wait node**: A 3-day Wait activity automatically inserted after inbound experience activities (In-app, Code-based, Card) to keep the profile in the journey long enough to view the content *(product-specific)*
* **Wait time in test**: A journey test mode parameter that overrides actual wait durations (default 10 seconds) so test results are returned quickly *(product-specific)*

**Guardrails:**

* The maximum wait duration is 90 days.
* Profiles are dropped from a journey after 91 days (global timeout), regardless of pending wait activities.
* A profile can only enter a Wait activity if enough time remains in the journey to complete the wait before the 91-day timeout.
* Do not use Wait activities to block reentrance; use the Allow reentrance option in journey properties instead.
* Custom wait expressions must use `dateTimeOnly` format and must not include a `Z` suffix or explicit time zone offset.
* Using a fixed static date (e.g., `toDateTimeOnly('2024-01-01T01:11:00Z')`) in a custom wait can cause issues; use profile-specific dynamic dates instead.
* Profile attributes are refreshed from the Unified Profile Service after a wait node in Read Audience journeys, which may produce unexpected results if snapshot consistency is expected.

**Terminology:**

* Canonical name: Wait activity — Acronym: none — variants: Wait node, wait step
* Synonyms: "Duration wait" = "relative wait"; "Custom wait" = "expression-based wait"
* Do not confuse: "Duration wait" (relative, e.g. 3 days from now) ≠ "Custom wait" (absolute calculated date from profile data)

**FAQ:**

* **Q: What is the maximum duration for a Wait activity?** — The maximum wait duration is 90 days; profiles are also subject to the 91-day global journey timeout.
* **Q: How does test mode handle Wait activities?** — In test mode, the "Wait time in test" parameter overrides the actual wait duration; the default is 10 seconds so tests complete quickly.
* **Q: Why should I avoid appending Z to a custom wait expression?** — Adding Z or a time zone offset to a `toDateTimeOnly()` expression can cause profiles to get stuck in the wait activity; the expression must rely on the journey's configured time zone.
* **Q: Are profile attributes updated after a Wait node?** — Yes, in journeys starting with Read Audience, the journey refreshes profile attributes from the Unified Profile Service after the wait, so downstream activities may see updated values rather than the original audience snapshot data.
* **Q: What is the automatic wait node?** — A 3-day Wait activity automatically inserted after inbound experience activities (In-app, Code-based, Card) to ensure profiles remain in the journey long enough to see the message; it can be removed or reconfigured as needed.

+++
