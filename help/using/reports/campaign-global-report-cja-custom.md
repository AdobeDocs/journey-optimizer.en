---
solution: Journey Optimizer
product: journey optimizer
title: Campaign report
description: Learn how to use custom channel data from the Campaign report
feature: Reporting
topic: Content Management
role: User
level: Intermediate
---
# Custom channel campaign report {#campaign-global-report-cja-custom-channel}

>[!BEGINSHADEBOX]

**On this page:** Learn how to read the Custom channel campaign report in Adobe Journey Optimizer to review KPIs, outcomes, latency, and outcome breakdown for your custom channel calls.

>[!ENDSHADEBOX]

>[!BEGINSHADEBOX]

You can access your Custom channel campaign report by clicking the **[!UICONTROL Reports]** button from your campaign, then selecting **[!UICONTROL View all time report]**. [Learn more](report-gs-cja.md)

![](assets/report-access.png)

>[!ENDSHADEBOX]

## KPIs {#kpis-custom}

![](assets/kpis-custom.png)

The **[!UICONTROL KPIs]** section provides a consolidated view of the operational health and reliability of your custom channel calls.

+++ Learn more about KPIs metrics

* **[!UICONTROL Successful calls]**: Total number of HTTP calls that returned a valid response without error.

* **[!UICONTROL 4xx errors]**: Number of failed calls due to client-side errors, highlighting configuration issues or endpoint failures.

* **[!UICONTROL 5xx errors]**: Number of failed calls due to server-side errors, highlighting configuration issues or endpoint failures.

* **[!UICONTROL Timeout calls]**: Number of calls that failed because they exceeded the maximum response time. This helps surface latency or performance issues with external endpoints.

* **[!UICONTROL Pre-call failures]**: Number of custom channel sends that failed before the HTTP call was ever made to the external endpoint. These failures occur in [!DNL Journey Optimizer]'s own infrastructure layer, not in your external system, and include authentication failures, request generation errors, and HTTP parse errors.

* **[!UICONTROL Average latency]**: Average end-to-end response time (in milliseconds) for all HTTP calls, including successful calls, errors, and timeouts.

+++

## Custom channel outcomes {#outcomes-custom}

![](assets/outcomes-custom.png)

The **[!UICONTROL Outcomes]** graph shows the HTTP call KPI trend over the selected time period, with a granularity that depends on the selected time range (per day for a 7-day report, per hour for a 1-day time range, or per minute for a 1-hour time range), while the **[!UICONTROL Outcome breakdown]** table provides a hierarchical breakdown of these HTTP call metrics, from overall metrics per endpoint at the top level, to metrics per custom channel using that endpoint, down to the campaigns and journeys that rely on them at the bottom level.

+++ Learn more about Outcome breakdown metrics

* **[!UICONTROL Custom channel successful]**: Total number of HTTP calls that returned a valid response without error.

* **[!UICONTROL 4xx errors]**: Number of failed calls due to client-side errors, highlighting configuration issues or endpoint failures.

* **[!UICONTROL 5xx errors]**: Number of failed calls due to server-side errors, highlighting configuration issues or endpoint failures.

* **[!UICONTROL Timeout calls]**: Number of calls that failed because they exceeded the maximum response time. This helps surface latency or performance issues with external endpoints.

* **[!UICONTROL Pre-call failures]**: Number of custom channel sends that failed before the HTTP call was ever made to the external endpoint. These failures occur in [!DNL Journey Optimizer]'s own infrastructure layer, not in your external system, and include authentication failures, request generation errors, and HTTP parse errors.

* **[!UICONTROL Calls]**: Total number of HTTP calls, including successful calls, errors, and timeouts.

+++

## Latency {#latency-custom}

![](assets/latency-custom.png)

The **[!UICONTROL Latency]** graph and tables visualize the trend of latency metrics. These views allow you to track performance patterns, identify peak latency periods, and monitor the impact of optimizations or system changes over time.

+++ Learn more about Latency metrics

* **[!UICONTROL Average latency]**: Average end-to-end response time (in milliseconds) for all HTTP calls, including successful calls, errors, and timeouts.

* **[!UICONTROL Average successful latency]**: Average end-to-end response time (in milliseconds) for HTTP calls that returned a valid response without error.

+++
