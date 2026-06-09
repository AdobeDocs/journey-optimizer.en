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
>abstract="Select the journey's time zone. When using a fixed time zone, it is the same for all individuals entering the journey."


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
>abstract="Check this option to use the real-time profile time zone in **Wait** and **Condition** activities. If a time zone has been defined for a profile, it is retrieved and used in the journey. If not, the time zone is the one defined in the time zone field above."

If the entry event of the journey has a namespace, meaning that the journey can reach the Real-time Customer Profile service of [!DNL Adobe Experience Platform], you may want to use the time zone defined at the profile level. To do so, in **Properties**, check **Use Profile time zone in waits and conditions**. This option is not checked by default.

If a time zone has been defined for a profile, it is retrieved and used by the journey. If it hasn't, the time zone used is the one defined in the time zone field.

![Profile time zone configuration in data sources for personalized timing](assets/journey73.png)

>[!NOTE]
>
>The profile time zone works with the **timeZone** field existing in the **Preference Details** field group.

## Use time zones in expressions {#timezone-in-expressions}

The start and end dates of a journey cannot be linked to a specific time zone. They are automatically associated to the instance's time zone.
