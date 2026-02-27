---
solution: Journey Optimizer
product: journey optimizer
title: Campaign report
description: Learn how to use Live activity data from the Campaign report
feature: Reporting
topic: Content Management
role: User
level: Intermediate
hide: yes
hidefromtoc: yes
exl-id: 58034ec4-62dc-406c-99c4-d6b7aa107140
---
# Live activity campaign report {#campaign-global-report-cja-activity}

>[!BEGINSHADEBOX]

You can access your Live activity campaign report by clicking the **[!UICONTROL Reports]** button from your campaign, then selecting **[!UICONTROL View all time report]**. [Learn more](report-gs-cja.md)

![](assets/report-access.png)

>[!ENDSHADEBOX]

## Sending Statistics {#sending-statistics-mobile}

![](assets/sending-statistics-mobile-live.png)

The **[!UICONTROL Sending Statistics]** table provides a detailed overview of key metrics related to your Live activity campaigns. It displays essential information such as the size of the targeted audience and the number of push notifications successfully delivered, helping you assess the overall reach and performance of your live push notifications.

+++ Learn more about Sending Statistics metrics

* **[!UICONTROL Targeted]**: Number of profiles that qualified for the audience before exclusions, suppressions, or consent removals were applied.

* **[!UICONTROL Sends]**: Total number of push notifications attempted to be sent to targeted profiles.

* **[!UICONTROL Delivered]**: Number of push notifications successfully delivered to devices, relative to the total number of attempted sends.

* **[!UICONTROL Send errors]**: Total number of push notifications that could not be sent due to errors (for example, invalid tokens or connectivity issues).

* **[!UICONTROL Send exclusions]**: Number of profiles excluded from sending by Adobe Journey Optimizer (for example, due to opt-out status or eligibility rules).

+++

## Live activity lifecycle {#lifecycle}

The **[!UICONTROL Live activity lifecycle]** table offers a comprehensive view of how your Live activities progress over time. It provides visibility into key events such as when activities are started, updated, or ended, helping you better understand user engagement and the overall lifecycle of your Live activity campaigns.

The reporting differs depending on whether you are using Transactional or Marketing campaigns.

### Transactional Live activities

![](assets/activity-lifecycle.png)

For Transactional campaign, the Live activities campaign report shows all lifecycle events including remote starts, local starts, updates, and ends.

+++ Learn more about Live activity lifecycle metrics with Transactional campaigns

* **[!UICONTROL Remote starts]**: Total number of Live activities start events initiated remotely, typically triggered by the server or backend systems.

* **[!UICONTROL Local starts]**: Total number of Live activities start events initiated locally on a user's device, often resulting from user interaction or client-side triggers.

* **[!UICONTROL Updates]**: Total number of Live activity updates sent to devices. Updates can include status changes, new content, or progress notifications.

* **[!UICONTROL Ends]**: Total number of Live activities end events sent to devices.

* **[!UICONTROL Totals count]**: Overall total of all Live activity lifecycle events, including starts, updates, and ends, providing a complete measure of Live activity volume.

+++

### Marketing Live activities

![](assets/activity-lifecycle-broadcast.png)

Marketing campaigns use Live activities for broadcast use cases, sending updates to multiple devices simultaneously.

For iOS Live activities in Marketing campaigns, the report shows only **[!UICONTROL Remote Starts]** events and **[!UICONTROL Remote starts errors]** at start. **[!UICONTROL Updates]** and **[!UICONTROL Ends]** events are not tracked because APNs distributes updates to all devices without providing feedback. To view **[!UICONTROL Updates]** and **[!UICONTROL Ends]** events, use [Apple's Push Notification console](https://developer.apple.com/notifications/push-notifications-console/).

+++ Learn more about Live activity lifecycle metrics with Marketing campaigns

* **[!UICONTROL Remote starts]**: Total number of Live activities start events initiated remotely, typically triggered by the server or backend systems.

* **[!UICONTROL Remote starts errors]**: Total number of errors that occurred when attempting to start Live activities remotely (for example, invalid tokens or connectivity issues).

+++

## Error reasons {#error-reasons}

![](assets/error-reasons-activity.png)

The **[!UICONTROL Error Reasons]** table allows you to identify the specific errors that occurred during the sending process of your Live activities, facilitating a thorough analysis of any issues encountered.

## Excluded reasons {#excluded-reasons}

![](assets/excluded-activity.png)

The **[!UICONTROL Excluded Reasons]** table visually depicts the diverse factors that led to the exclusion of user profiles from the targeted audience, preventing them from receiving your Live activity.
