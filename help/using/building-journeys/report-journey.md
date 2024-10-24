---
solution: Journey Optimizer
product: journey optimizer
title: Publish the journey
description: Learn how to report on your journey
feature: Journeys
topic: Content Management
role: User
level: Intermediate
keywords: publish, journey, live, validity, check
---
# Live report in the journey canvas {#report-journey}

>[!NOTE]
>
>If you cannot see data in your journey live report, your access rights must be extended to include the **[!UICONTROL View journeys report]** permission. [Learn more](../administration/permissions.md)

After your journey is published, **Live Reporting** provides metrics from the last 24 hours, directly within the journey canvas.

The displayed events occurred within the past 24 hours, with a minimum interval of two minutes between the event and its display, typically within five minutes.

![](assets/journey_live_report.png)

For your live journey, you have access to:

* **[!UICONTROL Entered profiles]**: Total number of individuals who entered this activity.
* **[!UICONTROL Exited profiled]**: Total number of individuals who exited the journey from that activity, due to an exit criteria.
* **[!UICONTROL Profiles in error]**: Total number of individuals who encountered an error during their journey.
* **[!UICONTROL Discarded profiles]**: Total number of individuals who were discarded from the journey for one of the following reasons:

    * For **Audience Qualification** activities, a discard can happen if the expected verb for audience qualification mismatch what journey has received (e.g. "exited" instead of "realized").
    * For **event-triggered** journeys, a discard can happen if the individual attempted to reenter the journey too soon or when reentry was not allowed.
    * On **recurring** journeys, a discard is counted on each recurrence if the individual is already in the journey and the reentry policy is not set to "force reentrance".
    * On **Read Audience** activities, a discard occurs if no identity is set for the exported individual, or if the received identity namespace does not match the expected one for the journey.

For each activity within every live journey, you have access to:

* **[!UICONTROL Entered profiles]**: Total number of individuals who entered this activity.
* **[!UICONTROL Exited profile]**: Total number of individuals who exited the journey from that activity, due to an exit criteria.
* **[!UICONTROL Error]**: Total number of individuals who had an error on that activity.
