---
title: Report on Decisioning
description: Learn how to report on Decisioning.
feature: Decisioning
topic: Integrations
role: User
level: Experienced
badge: label="Limited Availability"
exl-id: 7c45cd8a-8e86-4646-ba0a-db393e92d9da
---

# Report on Decisioning {#decisioning-report}

## Code-based campaigns reporting {#campaigns}

Once code-based experience are live, you can access dedicated reports to monitor Key Performance Indicators (KPIs) as an all-encompassing dashboard, delivering an analysis of essential metrics associated with your campaign.

This encompasses details related to the decision items performances and how users interacted with them. [Learn how to work with Code-based experience reports](../reports/campaign-global-report-cja-code.md)

![](../reports/assets/cja-decisioning-item-performance.png)

## Reporting in Customer Journey Analytics {#cja}

If you are working with Customer Journey Analytics, you can create custom reporting dashboards for your code-based campaigns leveraging Decisioning.

The main steps are listed below. Detailed information on how to work with Customer Journey Analytics is available in the [Customer Journey Analytics documentation](https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-landing){target="_blank"}.

1. Create and configure a **connection** in Customer Journey Analytics. This allows you to connect to the dataset you want reports for. [Learn how to create a connection](https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-connections/create-connection){target="_blank"}

1. Create a **data view** and associate it to the connection created earlier. In the **[!UICONTROL Components]** tab, choose the relevant schema fields you want to show up in reporting. For Decisioning, make sure you include the **propositioninteract** and **propositiondisplay** fields. [Learn how to create and configure data views](https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-dataviews/create-dataview){target="_blank"}

1. Combine data components, tables and visualizations in **workspace projects** to create and share reports for your code-based campaign. [Learn how to create workspace projects](https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-workspace/build-workspace-project/create-projects){target="_blank"}
