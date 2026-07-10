---
title: Report on Decisioning
description: Learn how to report on Decisioning.
feature: Decisioning
topic: Integrations
role: User
level: Experienced
exl-id: 7c45cd8a-8e86-4646-ba0a-db393e92d9da
version: Journey Orchestration
TQID: https://experienceleague.adobe.com/jbakmb7S9cFitmpa7ypVe8YrYvbZh0E0VogYi3KpNbo
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: a4cb03e1-327e-499d-9de8-e0c0db8a63a2
    internal-label: Decision capabilities
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
topic_v2:
  - id: aa2f3246-cb95-4b30-8899-fdf7d73550cc
    internal-label: Reporting
subfeature_v2:
  - id: a7a194a0-75e2-4913-8a83-14714fbf68e6
    internal-label: Decisioning API
  - id: eb547372-2a95-4d13-b0fd-f720c9895880
    internal-label: Edge Decisioning
---
# Report on Decisioning {#decisioning-report}

>[!BEGINSHADEBOX]

**On this page:** Access dedicated Decisioning reports and build Customer Journey Analytics dashboards so you can monitor key performance indicators and analyze how customers interact with your decision items.

>[!ENDSHADEBOX]

## Decisioning reporting {#campaigns}

Once journeys or campaigns with selection strategies are live, you can access dedicated reports to monitor Decisioning Key Performance Indicators (KPIs).

<!--
Once code-based experiences are live, you can access dedicated reports to monitor Key Performance Indicators (KPIs) as an all-encompassing dashboard, delivering an analysis of essential metrics associated with your campaign.

This encompasses details related to the decision items performances and how users interacted with them. [Learn how to work with Code-based experience reports](../reports/campaign-global-report-cja-code.md)
-->

![](../reports/assets/cja-decisioning-kpis.png)

You can also access details related to the decision items performance and how users interacted with them, delivering an analysis of essential metrics associated with your campaign.

![](../reports/assets/cja-decisioning-item-performance.png)

Learn how to work with Code-based experience reports on Decisioning in [this section](../reports/campaign-global-report-cja-code.md#decisioning-reporting).

## Reporting in Customer Journey Analytics {#cja}

If you are working with Customer Journey Analytics, you can create custom reporting dashboards for your code-based campaigns leveraging Decisioning.

The main steps are listed below. Detailed information on how to work with Customer Journey Analytics is available in the [Customer Journey Analytics documentation](https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-landing){target="_blank"}.

1. Create and configure a **connection** in Customer Journey Analytics. This allows you to connect to the dataset you want reports for. [Learn how to create a connection](https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-connections/create-connection){target="_blank"}

1. Create a **data view** and associate it to the connection created earlier. In the **[!UICONTROL Components]** tab, choose the relevant schema fields you want to show up in reporting. For Decisioning, make sure you include the **propositioninteract** and **propositiondisplay** fields. [Learn how to create and configure data views](https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-dataviews/create-dataview){target="_blank"}

1. Combine data components, tables and visualizations in **workspace projects** to create and share reports for your code-based campaign. [Learn how to create workspace projects](https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-workspace/build-workspace-project/create-projects){target="_blank"}
