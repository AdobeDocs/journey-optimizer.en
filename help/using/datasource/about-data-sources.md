---
solution: Journey Optimizer
product: journey optimizer
title: About data sources
description: Learn how to configure a data source
feature: Journeys, Data Sources
topic: Administration
role: Data Engineer, Data Architect, Admin
level: Intermediate, Experienced
keywords: data, source, journey, plaform
exl-id: e0cb261f-7cf7-42de-8e56-576492e3b5cc
---
# About data sources {#about-data-sources}

>[!CONTEXTUALHELP]
>id="ajo_journey_data_source_list"
>title="About data sources"
>abstract="The data source configuration is always performed by a technical user. The data source configuration allows you to define a connection to a system to retrieve additional information that will be used in your journeys, for: condition definition, parameter and personalization data in actions, custom wait definition, time zone definition."

The data source configuration allows you to define a connection to a system to retrieve additional information that will be used in your journeys, for:

* [condition definition](../building-journeys/condition-activity.md)
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

For more information on how to configure an Adobe Experience Platform Data Source and an external data source and how to find and use data in a journey, watch this [tutorial video](https://experienceleague.adobe.com/docs/journey-optimizer-learn/tutorials/journey-configuration/configure-data-sources.html){target="_blank"}.

## How-to video {#video}

Understand what a data source is and learn how to configure Experience Platform and external data sources.

>[!VIDEO](https://video.tv.adobe.com/v/334256?quality=12)

