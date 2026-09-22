---
solution: Journey Optimizer
product: journey optimizer
title: Publish the journey
description: Learn how to report on your journey metrics
feature: Journeys
topic: Content Management
role: User
level: Intermediate
keywords: publish, journey, live, validity, check
exl-id: 95d0267e-fab4-4057-8ab5-6f7c9c866b0f
version: Journey Orchestration
TQID: https://experienceleague.adobe.com/iHr0CFVSDz-4tOxNKyCyPZdwva3nfDyuU0Y5XHZEdjk
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: b3538224-471e-4c63-a444-9b19d89ae29c
    internal-label: Activities
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
  - id: aa2f3246-cb95-4b30-8899-fdf7d73550cc
    internal-label: Reporting
  - id: b5520579-b31f-4df7-9281-f0d9f91e2edc
    internal-label: Customer engagement
  - id: cdd65e7e-8839-44a2-bc21-0e03623b5dd1
    internal-label: Optimization
  - id: d00e9f03-e50b-4162-b143-0c0817c937c2
    internal-label: Customer journeys
  - id: e1e0219c-f879-479f-8427-888ed2a6e9c2
    internal-label: Insights
---
# Configure and track your journey metrics {#success-metrics}

>[!BEGINSHADEBOX]

**On this page:** Learn how to configure and assign journey metrics to track performance against your KPIs and measure the effectiveness of your customer journeys in real time.

>[!ENDSHADEBOX]

Gain clear visibility into the effectiveness of your customer journeys with journey metrics. This feature enables you to track performance against defined KPIs, uncover insights into what's working, and identify areas for optimization. By measuring impact in real time, you can drive continuous improvement and make data-informed decisions that elevate customer engagement.

## Prerequisites {#prerequisites}

Before using your journey metrics, you must add a dataset which includes the `Commerce Details`, `Web`, and `Mobile` [field groups](https://experienceleague.adobe.com/docs/experience-platform/xdm/tutorials/create-schema-ui.html#field-group){target="_blank"} under Configuration > Reporting in [!DNL Adobe Experience Platform].

These field groups must be selected from the built-in options, not from custom groups. Refer to the [Add datasets](../reports/reporting-configuration.md#add-datasets) section.

## Available metrics {#metrics}

The list of metrics varies depending on the [field groups](https://experienceleague.adobe.com/docs/experience-platform/xdm/tutorials/create-schema-ui.html#field-group){target="_blank"} included to your dataset. 

If your dataset is not configured, only the following metrics will be available: **[!UICONTROL Click]**, **[!UICONTROL Unique Click]**, **[!UICONTROL Clickthrough Rate]** and **[!UICONTROL Open Rate]**.

Note that with a Customer Journey Analytics license allows you to create custom success metrics. [Learn more](https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-components/cja-calcmetrics/cm-workflow/participation-metric)


|Metrics| Related field group |
|-|-|
|Clicks|No field group required|
|Unique clicks|No field group required|
|Clickthrough rate (CTR)|No field group required|
|Clickthrough open rate (CTOR)|No field group required|
|Page Views|Web field group|
|App Launches|Mobile field group|
|First App Launches|Mobile field group|
|App Installs|Mobile field group|
|App Upgrades|Mobile field group|
|Purchases|Commerce Details field group|
|Checkouts|Commerce Details field group|
|Cart Adds|Commerce Details field group|
|Cart Opens|Commerce Details field group|
|Cart Views|Commerce Details field group|
|Cart Removes|Commerce Details field group|
|Product Views|Commerce Details field group|
|Save For Laters|Commerce Details field group|

## Attribution {#attribution}

Each metric comes with a set attribution which determines which touchpoints or interactions contributed to a specific outcome.

* **Metrics attribution with Journey Optimizer license**:

    With Journey Optimizer license only, the maximum available lookback window for any selected metric is set to 7 days. For these metrics, the attribution model is set by default to **Last Touch**, i.e. the most recent interaction before conversion.

    For example, you can track whether a purchase was made after a customer interacted with your journey within the last 7 days.

* **Metrics attribution with Customer Journey Analytics license**:

    With both Journey Optimizer and Customer Journey Analytics licenses, you can create custom metrics with specific attribution settings or change the built-in metrics' attributions.
     
    Learn more about [Attribution models](https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-dataviews/component-settings/attribution#attribution-models)

## Assign your journey metrics {#assign}

>[!IMPORTANT]
>
>Only one journey metric is allowed per journey.

To begin tracking your journey metrics, follow the steps outlined below:

1. From your **[!UICONTROL Journeys]** menu, click **[!UICONTROL Create Journey]**.

1. Edit the journey's configuration pane to define the name of the journey and set its properties. Learn how to set your journey's properties on [this page](../building-journeys/journey-properties.md).

1. Choose your **[!UICONTROL Journey metrics]** which will be used to measure the effectiveness of your journey.

    Note that the metrics apply to the journey itself and are applicable across all elements of the journey.

    ![Success metrics configuration panel in journey properties](assets/success_metric.png)

1. Click **[!UICONTROL Save]**.

1. Design your journey with the necessary **[!UICONTROL Activities]**.

1. Test and publish your journey. 

1. Open your journey report to track the performance of your assigned success metrics.

    Your chosen metrics are displayed in the report's KPIs and Journey Stats table.

    ![Success metrics dropdown showing available events for goal tracking](assets/success_metric_2.png)

{{$include /help/_includes/do-not-localize/building-journeys/ai-augmented-success-metrics.md}}
