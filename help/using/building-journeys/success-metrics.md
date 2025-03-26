---
solution: Journey Optimizer
product: journey optimizer
title: Publish the journey
description: Learn how to report on your chosen journey metric
feature: Journeys
topic: Content Management
role: User
level: Intermediate
keywords: publish, journey, live, validity, check
hide: yes
hidefromtoc: yes
---
# Configure and track your journey metric {#success-metrics}

With journey metrics, you can effectively measure the impact of your activities by tracking their performance against predefined metrics.
By tracking these metrics, you can see how well your journey is performing, identify areas for improvement, and make informed decisions to enhance customer engagement.

## Prerequisites {#prerequisites}

Before using your journey metric, you must add a dataset which includes the `Commerce Details` [field group](https://experienceleague.adobe.com/docs/experience-platform/xdm/tutorials/create-schema-ui.html#field-group){target="_blank"}.

## Available metrics {#metrics}

The list of metrics varies depending on the [field groups](https://experienceleague.adobe.com/docs/experience-platform/xdm/tutorials/create-schema-ui.html#field-group){target="_blank"} included to your dataset. 

If your dataset is not configured, only the following metrics will be available: **[!UICONTROL Click]**, **[!UICONTROL Unique Click]**, **[!UICONTROL Clickthrough Rate]** and **[!UICONTROL Open Rate]**.

Note that with a Customer Journey Analytics licence allows you to create custom success metrics. [Learn more](https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-components/cja-calcmetrics/cm-workflow/participation-metric)


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
     
    Learn more on [Attribution models](https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-dataviews/component-settings/attribution#attribution-models)

## Assign your Journey metric {#assign}

To begin tracking your journey metric, follow the steps outlined below:

1. From your **[!UICONTROL Journeys]** menu, click **[!UICONTROL Create Journey]**.

1. Edit the journey's configuration pane to define the name of the journey and set its properties. Learn how to set your journey's properties in [this page](../building-journeys/journey-properties.md).

1. Choose your **[!UICONTROL Journey metrics]** which will be used to measure the effectiveness of your journey.

    Note that the metrics apply to the journey itself and are applicable across all elements of the journey.

    ![](assets/success_metric.png)

1. Click **[!UICONTROL Save]**.

1. Design your journey with the necessary **[!UICONTROL Activities]**.

1. Test and publish your journey. 

1. Open your journey report to track the performance of your assigned success metric.

    Your chosen metric is displayed in the report's KPIs and Journey Stats table.

    ![](assets/success_metric_2.png)
