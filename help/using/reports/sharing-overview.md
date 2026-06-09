---
solution: Journey Optimizer
product: journey optimizer
title: Journey step sharing overview
description: Journey step sharing overview
feature: Journeys, Reporting
topic: Content Management
role: Developer, Admin
level: Experienced
exl-id: 29d6b881-35a3-4c62-9e7d-d0aeb206ea77
TQID: https://experienceleague.adobe.com/JnA4LJ-FiCILS42uZZ5hUBUBQLmSn-R0TwUe-eGhCCg
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
  - id: c66ffd68-0f65-42bb-aa23-b4020f12e0bd
    internal-label: Admin
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
topic_v2:
  - id: a004cc84-67b9-4a33-a3a7-8ec7273ef4dc
    internal-label: Metadata
  - id: aa2f3246-cb95-4b30-8899-fdf7d73550cc
    internal-label: Reporting
  - id: c1579802-ddd4-4214-8a91-97b2066abe11
    internal-label: Troubleshooting
---
# Create journey reports {#design-jo-reports}

In addition to [real-time reports](live-report.md) and built-in [reporting capabilities](report-gs-cja.md), [!DNL Journey Optimizer] can automatically send journey performance data to Adobe Experience Platform so it can be combined with other data for analysis purposes. 

>[!NOTE]
>
>This feature is activated by default on all instances for journey steps events. You cannot modify or update the schemas and datasets that have been created during provisioning for step events. By default, these schemas and datasets are in read-only mode.

For example, you have set up a journey that sends multiple emails. This capability allows you to combine [!DNL Journey Optimizer] data with downstream event data like how many conversions occurred, how much engagement happened on the website, or how many transactions happened in the store. The journey information can be combined with data on Adobe Experience Platform, either from other digital properties or from offline properties to give a more comprehensive view of performance.

[!DNL Journey Optimizer] automatically creates the necessary schemas and streams into datasets to Adobe Experience Platform for each step an individual takes in a journey. A step event corresponds to an individual moving from one node to another in a journey. For example, in a journey that has an event, a condition and an action, three step events are sent to Adobe Experience Platform. 

>[!NOTE]
>
>In addition to profile-level step events, the system also generates internal events for **Read Audience** activities. These events, called `segmentExportJob` events, record the lifecycle of the Read Audience node (such as export job creation, queuing, completion, and errors) and are generated per Read Audience activity, not per individual profile. As a result, these events may not have an associated profile identifier (UPMID). These internal events are useful for monitoring and troubleshooting Read Audience performance and can be queried using the fields documented in the [serviceEvents section](../reports/sharing-field-list.md#servicevents-field). For query examples on how to work with segmentExportJob events, see [Queries related to the Read Audience](../reports/query-examples.md#read-segment-queries).

There are cases where multiple events can be created for the same node. For example, in the case of the Wait activity:

* One event is generated when the profile enters the wait (journeyNodeProcessed attribute is equal to false)
* One event is generated when the profile exits it (journeyNodeProcessed attribute is equal to true)

The list of XDM fields that are passed is comprehensive. Some contain system generated codes and others have human readable friendly names. Examples include the label of the journey activity or the step status: how many times an action timed out or ended in error.

>[!CAUTION]
>
>Datasets cannot be turned on for real time profile service. Please make sure that the **[!UICONTROL Profile]** toggle is turned off.

[!DNL Journey Optimizer] sends data as it occurs, in streaming. You can query this data using the Query Service. You can connect to Customer Journey Analytics or other BI tools to view data related to these steps. 

The following schemas are created:

* Journey Step Event schema for [!DNL Journey Orchestration] – Journey step event that is tied to a Journey Metadata.
* Journey schema with Journey Fields for [!DNL Journey Orchestration] – Journey Metadata to describe Journeys.

![](assets/sharing1.png)

![](assets/sharing2.png)

The following datasets are passed:

* Journey Step Events
* Journeys

![](assets/sharing3.png)

The lists of XDM fields passed to Adobe Experience Platform are detailed here:

* [Step event field list](../reports/sharing-field-list.md)
* [Legacy step event fields](../reports/sharing-legacy-fields.md)

## Integration with Customer Journey Analytics {#integration-cja}

[!DNL Journey Optimizer] step events can be linked to other datasets in [Adobe Customer Journey Analytics](https://experienceleague.adobe.com/docs/analytics-platform/using/cja-overview/cja-overview.html){target="_blank"}. 

The general workflow is:

* [!DNL Customer Journey Analytics] ingests the "Journey Step Event" dataset.
* The **profileID** field in the associated "Journey Step Event schema for Journey Orchestration" is defined as an Identity field. In [!DNL Customer Journey Analytics], you can then link this dataset to any other dataset that has the same value as the person based identifier.
* To use this dataset in [!DNL Customer Journey Analytics], for cross-channel journey analysis, refer to [Customer Journey Analytics documentation](https://experienceleague.adobe.com/docs/analytics-platform/using/cja-usecases/cross-channel.html){target="_blank"}.

➡️ [Work with Customer Journey Analytics](cja-ajo.md){target="_blank"}
