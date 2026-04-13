---
solution: Journey Optimizer
product: journey optimizer
title: Get started with data sources
description: Learn how to get started with data sources
feature: Journeys, Data Sources
topic: Administration
role: Developer, Admin
level: Intermediate, Experienced
keywords: data, source, journey, platform
exl-id: e0cb261f-7cf7-42de-8e56-576492e3b5cc
---
# Get started with data sources {#about-data-sources}

>[!CONTEXTUALHELP]
>id="ajo_journey_data_source_list"
>title="About data sources"
>abstract="The data source configuration is always performed by a technical user. The data source configuration allows you to define a connection to a system to retrieve additional information that will be used in your journeys, for: condition definition, parameter and personalization data in actions, custom wait definition, time zone definition."

>[!TIP]
>New to data management in Journey Optimizer? Start with the [Get started with data management](../data/gs-data.md) overview to understand schemas, datasets, identities, and how data flows before configuring data sources.

The data source configuration allows you to define a connection to a system to retrieve additional information that will be used in your journeys, for:

* [condition definition](../building-journeys/conditions.md)
* parameter and personalization data in [actions](../action/action.md)
* [custom wait definition](../building-journeys/wait-activity.md#custom)
* [time zone definition](../building-journeys/timezone-management.md)

➡️ [Discover this feature in video](#video)

This configuration is not required if your journeys only leverage local data coming from an event payload. For example, if your journey is composed of an event followed by a channel action activity that only uses data from the event, there is no need to configure a data source.

There are two types of data sources:

* The **pre-configured** Adobe Experience Platform data source that defines the connection to the Real-time Customer Profile Service. This is a built-in data source. See [this page](../datasource/adobe-experience-platform-data-source.md).
* The **external** data sources that allow you to define a connection to external systems. These are the ones you can create. See [this page](../datasource/external-data-sources.md).

>[!NOTE]
>
>As the responses are now supported, you should use custom actions instead of data sources for external data sources use-cases. For more information on responses, see this [section](../action/action-response.md)

For each data source, you define the information to retrieve using field groups. Field groups are sets of fields that can be retrieved from a data source. See [this page](../datasource/configure-data-sources.md#define-field-groups).

>[!NOTE]
>
>Schema relationships are not supported for data sources.

## Choose your data access strategy {#data-access-strategy}

Before configuring a data source, consider which approach best fits your use case. Three options are available, each with different trade-offs in terms of persistence, profile enrichment, and reusability. For a detailed discussion of these options, see [Best practices for advanced journeys in Journey Optimizer](https://experienceleague.adobe.com/en/perspectives/best-practices-for-advanced-journeys-in-journey-optimizer){target="_blank"}.

**Option 1 — Access external data via Custom Actions (no Data Lake)**

Connect directly to an external API at journey runtime without persisting data in the Experience Platform Data Lake. Best suited when:

* The data is only useful within the journey context and not needed elsewhere.
* The external system is accessible through an API endpoint that returns the attributes needed.

Learn more about [custom actions](../action/action.md) and [custom action responses](../action/action-response.md).

**Option 2 — Dataset in Data Lake, not enabled for Profile**

Ingest data into a dataset to trigger and personalize journeys based on contextual event data, without contributing to the Real-Time Customer Profile. Best suited when:

* Records contain an identity field usable to access profiles already stored in Experience Platform.
* The data is not needed for audience creation or identity stitching outside of Journey Optimizer.

**Option 3 — Profile-enabled dataset in Data Lake**

Ingest data into a [profile-enabled dataset](https://experienceleague.adobe.com/en/docs/experience-platform/catalog/datasets/user-guide#enable-profile){target="_blank"} to create audiences, enrich identity graphs, and leverage data across multiple journeys and RT-CDP destinations. Best suited when:

* The data is useful for audience definitions used in channels beyond Journey Optimizer.
* The data contains multiple identities that contribute to richer, stitched profile fragments.

| | Data persisted in Data Lake | Dataset enabled for Profile |
| --- | --- | --- |
| **Option 1** — External data via Custom Actions | No | No |
| **Option 2** — Dataset not enabled for Profile | Yes | No |
| **Option 3** — Profile-enabled dataset | Yes | Yes |

For more information on how to configure an Adobe Experience Platform Data Source and an external data source and how to find and use data in a journey, watch this [tutorial video](https://experienceleague.adobe.com/docs/journey-optimizer-learn/tutorials/journey-configuration/configure-data-sources.html){target="_blank"}.

## How-to video {#video}

Understand what a data source is and learn how to configure Experience Platform and external data sources.

>[!VIDEO](https://video.tv.adobe.com/v/334256?quality=12)

