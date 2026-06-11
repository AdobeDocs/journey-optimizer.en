---
solution: Journey Optimizer
product: journey optimizer
title: Time zone management
description: Learn about time zone management
feature: Journeys, Profiles
topic: Content Management
role: User
level: Intermediate
keywords: time zone, properties, journey, condition, time, date, custom
exl-id: 3bcc08d6-1210-4ff9-92f4-edee8285b469
version: Journey Orchestration
TQID: https://experienceleague.adobe.com/PdwGEuWqJcncbkokE0eOhMaEk9L0AmCJ--VZBxxtDDU
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: d998adac-2f81-400b-a669-d07bb196e4eb
    internal-label: Journeys
subfeature_v2:
  - id: fa683eda-48de-4558-af32-2673edcd44fe
    internal-label: Events
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
level_v2:
  - id: b5a62a22-46f7-4f0d-b151-3fc640bef588
    internal-label: Intermediate
topic_v2:
  - id: cdd65e7e-8839-44a2-bc21-0e03623b5dd1
    internal-label: Optimization
---
# Time zone management {#timezone_management}

>[!CONTEXTUALHELP]
>id="ajo_journey_properties_time_zone"
>title="Journey time zone"
>abstract="The time zone setting defines the journey's time zone. When using a fixed time zone, it is the same for all individuals entering the journey."


You can define a time zone in the [properties](../building-journeys/journey-properties.md#timezone) of your journey.

To access journey properties, select the pencil icon in the top-right of the screen.

This time zone will be used for every activity of the journey containing a time element such as:

* [Time condition](../building-journeys/conditions.md#time_condition)
* [Date condition](../building-journeys/conditions.md#date_condition)
* [Custom wait](../building-journeys/wait-activity.md#custom)

<!--
* [Fixed date wait](../building-journeys/wait-activity.md#fixed_date)
-->

You can select a [fixed time zone](#fixed-timezone) or choose to use the time zone [defined in the user profile](#timezone-from-profiles).

## Define a fixed time zone {#fixed-timezone}

The time zone can be fixed. Clear the pre-defined time zone and pick one from the drop-down list. If you use a fixed time zone, it will be the same for all individuals entering the journey.

To do so, in the **[!UICONTROL Journey Properties]** pane, select a time zone. 

![Timezone selection dropdown in journey properties](assets/journey72.png)

## Use profile time zone {#timezone-from-profiles}

>[!CONTEXTUALHELP]
>id="ajo_journey_properties_profile_time_zone"
>title="Use profile time zone"
>abstract="This option uses the real-time profile time zone in **Wait** and **Condition** activities. If a time zone has been defined for a profile, it is retrieved and used in the journey. If not, the time zone is the one defined in the time zone field above."

If the entry event of the journey has a namespace, meaning that the journey can reach the Real-time Customer Profile service of [!DNL Adobe Experience Platform], you may want to use the time zone defined at the profile level. To do so, in **Properties**, check **Use Profile time zone in waits and conditions**. This option is not checked by default.

If a time zone has been defined for a profile, it is retrieved and used by the journey. If it hasn't, the time zone used is the one defined in the time zone field.

![Profile time zone configuration in data sources for personalized timing](assets/journey73.png)

>[!NOTE]
>
>The profile time zone works with the **timeZone** field existing in the **Preference Details** field group.

## Use time zones in expressions {#timezone-in-expressions}

The start and end dates of a journey cannot be linked to a specific time zone. They are automatically associated to the instance's time zone.

+++AI Assistant — Page context

* **TL;DR:** This page explains how to configure time zone settings in Adobe Journey Optimizer journey properties, choosing between a fixed time zone applied to all profiles or a per-profile time zone sourced from the Real-time Customer Profile.

**Intents:**
* Set a fixed time zone on a journey so that all profiles follow the same time reference for conditions and waits
* Enable per-profile time zone so that Wait and Condition activities use each individual's stored time zone preference
* Understand which journey activities are affected by the journey time zone setting
* Identify the profile field group that stores the individual time zone value

**Glossary:**
* **Fixed time zone**: A single time zone selected in Journey Properties that applies uniformly to every profile entering the journey *(product-specific)*
* **Profile time zone**: The per-individual time zone stored in the `timeZone` field of the Preference Details field group, used when the "Use Profile time zone in waits and conditions" option is enabled *(product-specific)*
* **Preference Details field group**: The XDM field group that contains the `timeZone` attribute used for profile-level time zone resolution

**Guardrails:**
* The "Use Profile time zone in waits and conditions" option is only available when the journey's entry event has a namespace (i.e., the journey can reach the Real-time Customer Profile service)
* The option is not checked by default; the fixed time zone is used unless explicitly enabled
* If the option is enabled but no time zone is defined on the profile, the journey falls back to the fixed time zone defined in journey properties
* Journey start and end dates cannot be linked to a specific time zone; they are automatically associated with the instance's time zone

**Terminology:**
* Canonical name: Time zone management — Acronym: none — variants: timezone configuration, journey time zone
* Synonyms: "fixed time zone" = "same for all individuals"; "profile time zone" = "Use Profile time zone in waits and conditions"
* Do not confuse: "journey time zone" (applies to activities) ≠ "instance time zone" (applies to journey start/end dates, set automatically)

**FAQ:**
* **Q: Where do I set the time zone for a journey?** — In the Journey Properties pane, accessible via the pencil icon in the top-right of the journey canvas.
* **Q: Which activities use the journey time zone?** — Time conditions, date conditions, and custom wait activities.
* **Q: How do I make each profile follow their own local time zone?** — In Journey Properties, enable the "Use Profile time zone in waits and conditions" option. This requires the journey to have a namespace so it can reach the Real-time Customer Profile service.
* **Q: What happens if a profile has no time zone defined and the profile time zone option is enabled?** — The journey falls back to the fixed time zone defined in the time zone field in Journey Properties.
* **Q: Which profile field stores the individual's time zone?** — The `timeZone` field within the Preference Details field group in the profile schema.
* **Q: Can I set the journey's start and end dates to a specific time zone?** — No. Journey start and end dates are automatically associated with the instance's time zone and cannot be linked to a custom time zone.

+++
