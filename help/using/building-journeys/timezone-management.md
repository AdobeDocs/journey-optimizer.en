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
---
# Time zone management {#timezone_management}

>[!CONTEXTUALHELP]
>id="ajo_journey_properties_time_zone"
>title="Timezone"
>abstract="Select the journey's time zone. When using a fixed time zone, it is the same for all individuals entering the journey."


You can define a time zone in the [properties](../building-journeys/journey-properties.md#timezone) of your journey.

To access journey properties, click on the pencil icon in the top-right of the screen.

This time zone will be used for every activity of the journey containing a time element such as:

* [Time condition](../building-journeys/condition-activity.md#time_condition)
* [Date condition](../building-journeys/condition-activity.md#date_condition)
* [Custom wait](../building-journeys/wait-activity.md#custom)

<!--
* [Fixed date wait](../building-journeys/wait-activity.md#fixed_date)
-->

You can select a [fixed time zone](#fixed-timezone) or choose to use the time zone [defined in the user profile](#timezone-from-profiles).

## Define a fixed time zone {#fixed-timezone}

The time zone can be fixed. Clear the pre-defined time zone and pick one from the drop-down list. If you use a fixed time zone, it will be the same for all individuals entering the journey.

To do so, in the **[!UICONTROL Journey Properties]** pane, select a time zone. 

![](assets/journey72.png)

## Use profiles time zone {#timezone-from-profiles}

>[!CONTEXTUALHELP]
>id="ajo_journey_properties_profile_time_zone"
>title="Use profile time zone"
>abstract="Check the box to use the real-time profile time zone in wait and condition activities. If a time zone has been defined for a profile, it will be retrieved and used by the journey. If not, the time zone will be the one defined in the timezone field above."

If the entry event of the journey has a namespace, meaning that the journey can reach the Real-time Customer Profile service of Adobe Experience Platform, you may want to use the time zone defined at the profile level. To do so, in **Properties**, check **Use Profile time zone in waits and conditions**. This option is not checked by default.

If a time zone has been defined for a profile, it will be retrieved and used by the journey. If it hasn't, the time zone used will be the one defined in the timezone field.

![](assets/journey73.png)

>[!NOTE]
>
>The profile time zone works with the **timeZone** field existing in the **Preference Details** field group.

## Use time zones in expressions {#timezone-in-expressions}

The start and end dates of a journey cannot be linked to a specific time zone. They are automatically associated to the instance's time zone.
