---
solution: Journey Optimizer
product: journey optimizer
title: Journey report
description: Learn how to use data from the journey report
feature: Reporting, Journeys
topic: Content Management
role: User
level: Intermediate
exl-id: 30d4f967-e085-44f1-973d-11e79f693e6e
TQID: https://experienceleague.adobe.com/LvJSxPvyDrrhZGPH0EgWPfHhiHA9o3dQAXAMY-6k4-A
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
  - id: cdd65e7e-8839-44a2-bc21-0e03623b5dd1
    internal-label: Optimization
  - id: e1e0219c-f879-479f-8427-888ed2a6e9c2
    internal-label: Insights
---
# Journey report {#journey-global-report}

>[!BEGINSHADEBOX]

**On this page:** Explore the Adobe Journey Optimizer journey report in Customer Journey Analytics to analyze journey KPIs, statistics, exclusions, action and event performance, and the journey canvas.

>[!ENDSHADEBOX]

The **Journey report** functions as an all-encompassing dashboard, delivering an analysis of essential metrics associated with your journey. This encompasses details such as the count of entered profiles and instances of failed individual journeys, offering a comprehensive insight into your journey's effectiveness and level of engagement.

**Journey report** can be accessed directly from your journey with the **[!UICONTROL View report]** button. 

![](assets/gs-cja-report-3.png)

To learn more about Customer Journey Analytics Workspace and how to filter and analyze data, refer to [this page](https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-workspace/home).

## Journey overview {#journey-global}

The **[!UICONTROL Journey]** report gives you a clear view of the most important tracking data about your journey.

### Journey KPIs {#journey-perfomance}

![](assets/cja-journey-kpis.png)

The **[!UICONTROL Journey]** Key Performance Indicators (KPIs) function as an all-encompassing dashboard, delivering an analysis of essential metrics associated with your journey. This encompasses details such as the count of entered profile and instances of failed individual journeys, offering a comprehensive insight into your journey's effectiveness and level of engagement.

+++ Learn more about Journey KPIs metrics

* **[!UICONTROL Journey engagement]**: Total number of unique individuals who received messages sent through the journey, representing distinct profiles that reached a designated action point in the journey.

* **[!UICONTROL Journey enters]**: Total number of individuals who reached the entry event of the journey.

* **[!UICONTROL Journey exits]**: Total number of individuals who exited the journey.

+++

### Journey stats {#journey-stats}

![](assets/cja-journey-stats.png)

The **[!UICONTROL Journey Statistics]** table offers a detailed summary of crucial data about your journeys. It includes key metrics like the number of failures and successful entries, providing valuable insights into the performance and reach of your emails and journeys.

+++ Learn more about Journey Statistics metrics

* **[!UICONTROL Journey exclusion]**: Total number of individuals who were excluded from the journey due to predefined criteria or suppression rules.

* **[!UICONTROL Journey engagement]**: Total number of unique individuals who received messages sent through the journey, representing distinct profiles that reached a designated action point in the journey.

* **[!UICONTROL Journey enters]**: Total number of individuals who reached the entry event of the journey.

* **[!UICONTROL Journey exits]**: Total number of individuals who exited the journey.

* **[!UICONTROL Journey failures]**: Total number of individual journeys that were not successfully executed.

* **[!UICONTROL Unique Journey enters]**: Total number of individuals who reached the entry event of the journey, multiple interactions of one profile are not taken into account.

* **[!UICONTROL Unique Journey exits]**: Total number of individuals who exited the journey, multiple interactions of one profile are not taken into account.

* **[!UICONTROL Unique Journey failures]**: Total number of individual journeys that were not successfully executed, multiple interactions of one profile are not taken into account.

+++

## Journey exclusion {#journey-exclusion}

The **[!UICONTROL Journey exclusion]** table presents a comprehensive view of the different factors that resulted in the exclusion of user profiles. To investigate business rules-related exclusions at the Data Lake level and identify whether profiles were excluded due to a cap being reached or a lower priority, use the queries available in [this section](query-examples.md#business-rules-queries).

## Action error {#action-error}

![](assets/cja-journey-action-error.png)

The **[!UICONTROL Action errors]** widget details the different errors which occurred for your journey's actions.

## Journey canvas {#journey-canvas}

![](assets/cja-journey-canvas.png)

The **[!UICONTROL Journey Canvas]** widget allows you to visually trace the trajectory of your targeted profiles as they navigate through your journey. [Learn more in Customer Journey Analytics documentation](https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-workspace/visualizations/journey-canvas/journey-canvas)

Enhance your canvas customization with the following options:

* Add or remove the desired activity type, such as messages or conditions, from the **[!UICONTROL Node type]** drop-down menu.
* Adjust the **[!UICONTROL Percentage value]** to determine the flow distribution among different journey paths.
* Customize your **[!UICONTROL Arrow settings]** to include labels, conditions, or opt for a clean display.
* Enable the **[!UICONTROL Show fallout]** option to visualize profiles that exited your journey directly on the canvas.

The following rules apply when using **[!UICONTROL Node Type]** Filtering:

* When creating a segment on a node, it will still encompass nodes from earlier stages of the journey, even if those nodes have been excluded through the **[!UICONTROL Node type]** filter.

* You cannot create segments formed from an arrow if nodes in earlier stages of the journey have been excluded via the **[!UICONTROL Node type]** filter. In this case, the right-click functionality will be disabled on those arrows.

## Action performance {#action-performance}

### Performance over time {#action-overtime}

![](assets/cja-journey-action-performance.png)

The **[!UICONTROL Performance Over time]** graph allows you to identify and analyze the number of profiles that meet the criteria to be considered target profiles for your actions. This visualization provides valuable insights into the effectiveness of your strategies and helps you make data-driven decisions to optimize your performance.

### Action overview {#action-overview}

![](assets/cja-journey-action-overview.png)

The **[!UICONTROL Action overview]** table serves as a comprehensive dashboard, offering an analysis of key metrics related to the actions in your journey. This includes crucial details such as the number of interactions and the click-through rate

+++ Learn more about Action overview metrics

* **[!UICONTROL Node enters]**: Total number of individuals who have entered a specific node within the journey.

* **[!UICONTROL Journey failure]**: Total number of individual journeys that were not successfully executed.

* **[!UICONTROL Click through rate]**: Percentage of users who interacted with the action.

* **[!UICONTROL Clicks]**: Number of times a content was clicked on in your actions.

* **[!UICONTROL Delivered]**:  Number of actions successfully sent, in relation to the total number of sent actions.

+++

## Events performance {#events-performance}

### Performance over time {#event-overtime}

![](assets/cja-journey-performance-event.png)

The **[!UICONTROL Performance over time]** graph enables you to identify and analyze the number of profiles that qualify as target profiles for your events. This powerful tool helps you track trends and patterns over time, providing valuable insights for optimizing your event strategies.

### Event overview {#event-overview}

![](assets/cja-journey-events-overview.png)

The **[!UICONTROL Event overview]** table shows how many profiles meet your event criteria over time. This tool helps you identify patterns in qualification rates to refine your event strategy.

+++ Learn more about Journey Statistics metrics

* **[!UICONTROL People]**: Number of user profiles who qualify as target profiles for your events.

+++

## Targeting overview {#targeting}

![](assets/cja-journey-targeting-overview.png)

If you set up **[!UICONTROL Targeting rules]** for your content, the **[!UICONTROL Targeting overview]** table provides a detailed view of key engagement metrics, showing how the targeted profiles for each rule interacted with your content.

➡️ [Learn more on Targeting rules](../content-management/optimization-targeting.md)

+++ Learn more about Targeting overview metrics

* **[!UICONTROL People]**: Number of user profiles who qualify as target profiles for your events.

* **[!UICONTROL Unique Clicks]**: Number of profiles who clicked on a content in an email.

* **[!UICONTROL Unique click rate]**: Percentage of targeted profiles who clicked at least once.

+++
