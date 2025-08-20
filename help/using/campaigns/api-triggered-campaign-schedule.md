---
solution: Journey Optimizer
product: journey optimizer
title: chedule an API triggered campaign
description: Learn how to schedule an API triggered campaign.
feature: Campaigns, API
topic: Content Management
role: Developer
level: Experienced
keywords: campaigns, API-triggered, REST, optimizer, messages
exl-id: e04b0d38-6b3d-4086-a0f0-c1b8f6d9634f
---
# Schedule the API triggered campaign {#api-schedule}

Use the **[!UICONTROL Schedule]** tab to define the campaign schedule.

## Set start and end dates

By default, API triggered campaigns start once they are triggered, and end as soon as the message has been sent once. If you do not want to execute your campaign right after it is triggered, you can specify a date and time at which the message should be sent using the **[!UICONTROL Campaign start]** option.

The **[!UICONTROL Campaign end]** option allows you to specify when a campaign should stop being executed. Outside of the specified dates, the campaign will not be executed.

![](assets/api-triggered-schedule.png)

>[!NOTE]
>
>When scheduling campaigns in [!DNL Adobe Journey Optimizer], ensure your start date/time aligns with the desired first delivery.

## Set rate control

[!DNL Journey Optimizer] allows you to enable rate control for outbound actions (Email, SMS, Push notifications).

This feature is particularly useful for preventing overload on downstream systems, such as landing pages or customer care platforms. For example, you can set a rate limit of 165 messages per second to ensure steady delivery without overwhelming downstream systems.

To set rate control, enable the **[!UICONTROL Throttle delivery]** option in the **[!UICONTROL Delivery settings]** section and specify the desired **[!UICONTROL Delivery rate]**.

![](assets/throttling-rate-control.png)

## Next steps {#next}

Once your campaign configuration and content are ready, you can review and activate it. [Learn more](review-activate-campaign.md)
