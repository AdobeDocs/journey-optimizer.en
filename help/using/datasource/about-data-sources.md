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
TQID: https://experienceleague.adobe.com/eG1QcfpHtxpabUt5e7RZiMIpSAJD6Z6bjO-4wtZEUOg
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: bb359667-ec7d-4d4b-8663-5850fc219d32
    internal-label: Administration
  - id: d556b755-390a-43f0-be32-a08cf6236126
    internal-label: Configuration
  - id: d998adac-2f81-400b-a669-d07bb196e4eb
    internal-label: Journeys
subfeature_v2:
  - id: dd51b532-b93f-4bcf-8dbf-0d007f593aca
    internal-label: Data source configuration
  - id: e30b0a1a-b594-47b8-af94-1e3a2be6df11
    internal-label: Get started
role_v2:
  - id: c66ffd68-0f65-42bb-aa23-b4020f12e0bd
    internal-label: Admin
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
level_v2:
  - id: b5a62a22-46f7-4f0d-b151-3fc640bef588
    internal-label: Intermediate
topic_v2:
  - id: e0eb8757-182f-49f3-94a4-1587d16f5094
    internal-label: Personalization
  - id: eddd9b14-83bd-4ff4-9072-54a4a484abb7
    internal-label: Administration
---
# Get started with data sources {#about-data-sources}

>[!BEGINSHADEBOX]

**On this page:** Understand what data sources are and how to choose the right data access strategy so you can bring additional data into your journeys for conditions, personalization, and timing.

>[!ENDSHADEBOX]

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

>[!TIP]
>
>This option is a good fit if you answer **yes** to both questions:
>* Is the data only useful inside the journey context and not needed elsewhere? If the data is also needed for audiences or other channels, consider Options 2 or 3.
>* Is the external system accessible through an API endpoint that returns the required attributes? If not, you will need to ingest the data into the Data Lake first.

**Option 2 — Dataset in Data Lake, not enabled for Profile**

Ingest data into a dataset to trigger and personalize journeys based on contextual event data, without contributing to the Real-Time Customer Profile. Best suited when:

* Records contain an identity field usable to access profiles already stored in Experience Platform.
* The data is not needed for audience creation or identity stitching outside of Journey Optimizer.

>[!TIP]
>
>This option is a good fit if you answer **yes** to both questions:
>* Do records contain an identity field that can be used to access profiles already stored in Experience Platform? If not, journeys will not be able to access and deliver to profiles.
>* Is the data NOT needed for [audience](../audience/about-audiences.md) creation or identity stitching outside of Journey Optimizer? If it is, use Option 3 instead.

**Option 3 — Profile-enabled dataset in Data Lake**

Ingest data into a [profile-enabled dataset](https://experienceleague.adobe.com/en/docs/experience-platform/catalog/datasets/user-guide#enable-profile){target="_blank"} to create audiences, enrich identity graphs, and leverage data across multiple journeys and RT-CDP destinations. Best suited when:

* The data is useful for audience definitions used in channels beyond Journey Optimizer.
* The data contains multiple identities that contribute to richer, stitched profile fragments.

>[!CAUTION]
>
>**Before you enable a dataset for Profile**, assess the following areas:
>* **Data synchronization** — External databases must be synchronized, with alerts in place to identify ingestion failures.
>* **[Profile guardrails](https://experienceleague.adobe.com/en/docs/experience-platform/profile/guardrails){target="_blank"}** — Profile-specific guardrails apply in addition to the [general data ingestion guardrails](https://experienceleague.adobe.com/en/docs/experience-platform/ingestion/guardrails){target="_blank"} for Experience Platform.
>* **Identity integrity** — Identity data in your source systems must be carefully planned to maintain healthy identity graphs.
>* **Data Lake utilization** — Overall storage consumption, table relationships, and addressable profiles must be assessed before ingestion.

| | Data persisted in Data Lake | Dataset enabled for Profile |
| --- | --- | --- |
| **Option 1** — External data via Custom Actions | No | No |
| **Option 2** — Dataset not enabled for Profile | Yes | No |
| **Option 3** — Profile-enabled dataset | Yes | Yes |

For more information on how to configure an Adobe Experience Platform Data Source and an external data source and how to find and use data in a journey, watch this [tutorial video](https://experienceleague.adobe.com/docs/journey-optimizer-learn/tutorials/journey-configuration/configure-data-sources.html){target="_blank"}.

## How-to video {#video}

Understand what a data source is and learn how to configure Experience Platform and external data sources.

>[!VIDEO](https://video.tv.adobe.com/v/334256?quality=12)

