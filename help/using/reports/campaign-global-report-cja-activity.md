---
solution: Journey Optimizer
product: journey optimizer
title: Campaign Live activity report
description: Learn how to use Live activity data from the Campaign report
feature: Reporting
topic: Content Management
role: User
level: Intermediate
hide: true
exl-id: 58034ec4-62dc-406c-99c4-d6b7aa107140
TQID: https://experienceleague.adobe.com/NBJkyh9TCAPxD0u3EpwaZth7-ePjEWdg2roQ7J2-RuY
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: a9f73820-6899-47c2-a597-3fec28ab756a
    internal-label: Reporting
  - id: b49ca41f-eb7a-4f4b-abeb-a97c06fd0c04
    internal-label: Track and monitor
subfeature_v2:
  - id: d145add9-d5b9-481b-aa8a-e15e6bb7f813
    internal-label: Performance monitoring
  - id: a7289281-9ae4-47b1-b8cf-4028b98af776
    internal-label: Deliverability
  - id: b5afe8bf-bda6-41b5-ba06-922638872d63
    internal-label: Metrics catalog
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
level_v2:
  - id: b5a62a22-46f7-4f0d-b151-3fc640bef588
    internal-label: Intermediate
topic_v2:
  - id: aa2f3246-cb95-4b30-8899-fdf7d73550cc
    internal-label: Reporting
---
# Live activity campaign report {#campaign-global-report-cja-activity}

>[!BEGINSHADEBOX]

**On this page:** Learn how to read the Live activity campaign report in Adobe Journey Optimizer to track sending statistics, Live activity lifecycle events, error reasons, and exclusion reasons.

>[!ENDSHADEBOX]

>[!BEGINSHADEBOX]

You can access your Live activity campaign report by clicking the **[!UICONTROL Reports]** button from your campaign, then selecting **[!UICONTROL View all time report]**. [Learn more](report-gs-cja.md)

![](assets/report-access.png)

>[!ENDSHADEBOX]

## Sending Statistics {#sending-statistics-mobile}

![](assets/sending-statistics-mobile-live.png)

The **[!UICONTROL Sending Statistics]** table provides a detailed overview of key metrics related to your Live activity campaign. It displays essential information such as the size of the targeted audience and the number of live activity successfully delivered, helping you assess the overall reach and performance of your live activity.

+++ Learn more about Sending Statistics metrics

* **[!UICONTROL Targeted]**: Number of profiles that qualified for the audience before exclusions, suppressions, or consent removals were applied.

* **[!UICONTROL Sends]**: Total number of live activity events attempted to be sent to targeted profiles.

* **[!UICONTROL Delivered]**: Number of live activity events successfully delivered to devices, relative to the total number of attempted sends.

* **[!UICONTROL Send errors]**: Total number of live activity events that could not be sent due to errors (for example, invalid tokens or connectivity issues).

* **[!UICONTROL Send exclusions]**: Number of profiles excluded from sending by Adobe Journey Optimizer (for example, due to opt-out status or eligibility rules).

+++

## Live activity lifecycle {#lifecycle}

The **[!UICONTROL Live activity lifecycle]** table offers a comprehensive view of how your Live activity progresses over time. It provides visibility into key events such as when activity is started, updated, or ended, helping you better understand user engagement and the overall lifecycle of your Live activity campaign.

The reporting differs depending on whether you are using Transactional or Marketing campaigns.

### Transactional Live activity

![](assets/activity-lifecycle.png)

For Transactional campaign, the Live activity campaign report shows all lifecycle events including remote starts, local starts, updates, and ends.

+++ Learn more about Live activity lifecycle metrics with Transactional campaigns

* **[!UICONTROL Remote starts]**: Total number of Live activity start events initiated remotely, typically triggered by the server or backend systems.

* **[!UICONTROL Local starts]**: Total number of Live activity start events initiated locally on a user's device, often resulting from user interaction or client-side triggers.

* **[!UICONTROL Updates]**: Total number of Live activity updates sent to devices. Updates can include status changes, new content, or progress notifications.

* **[!UICONTROL Ends]**: Total number of Live activity end events sent to devices.

* **[!UICONTROL Totals count]**: Overall total of all Live activity lifecycle events, including starts, updates, and ends, providing a complete measure of Live activity volume.

+++

### Marketing Live activity

![](assets/activity-lifecycle-broadcast.png)

Marketing campaigns use Live activity for broadcast use cases, sending updates to multiple devices simultaneously.

For iOS Live activity in Marketing campaigns, the report shows only **[!UICONTROL Remote Starts]** events and **[!UICONTROL Remote starts errors]** at start. **[!UICONTROL Updates]** and **[!UICONTROL Ends]** events are not tracked because APNs distributes updates to all devices without providing feedback. To view **[!UICONTROL Updates]** and **[!UICONTROL Ends]** events, use [Apple's Push Notification console](https://developer.apple.com/notifications/push-notifications-console/).

+++ Learn more about Live activity lifecycle metrics with Marketing campaigns

* **[!UICONTROL Remote starts]**: Total number of Live activity start events initiated remotely, typically triggered by the server or backend systems.

* **[!UICONTROL Remote starts errors]**: Total number of errors that occurred when attempting to start Live activity remotely (for example, invalid tokens or connectivity issues).

+++

#### Retrieving updates and end counts via API {#retrieving-updates-end-api}

As an alternative to using Apple's Push Notification console, Updates and End counts can be obtained through headless API calls.

When executing update or end API calls for broadcast use cases, the response includes a `controlBreakdown` section that provides counters indicating how many update and end calls were executed for the live activity execution. This block is absent for legacy executions without lifecycle data. Execution status can also be retrieved explicitly using the GET endpoint when needed.

**UPDATE / END Response (200 OK)**

```json
{
  "executionId": "HA-exec-abc",
  "campaignId": "campaign-abc-123",
  "campaignVersionId": "v1",
  "audienceId": "audience-segment-id",
  "status": "processing",
  "targetedProfileCount": 150000,
  "createdAt": "2026-02-27T10:00:00Z",
  "executionLifecycle": {
    "lastControlAt": "2026-02-27T10:45:00Z",
    "controlBreakdown": {
      "update": 5,
      "end": 1
    }
  }
}
```

**Execution Status (GET)**

```
GET /im/executions/audience/{executionId}
```

## Error reasons {#error-reasons}

![](assets/error-reasons-activity.png)

The **[!UICONTROL Error Reasons]** table allows you to identify the specific errors that occurred during the sending process of your Live activity, facilitating a thorough analysis of any issues encountered.

## Excluded reasons {#excluded-reasons}

![](assets/excluded-activity.png)

The **[!UICONTROL Excluded Reasons]** table visually depicts the diverse factors that led to the exclusion of user profiles from the targeted audience, preventing them from receiving your Live activity.
