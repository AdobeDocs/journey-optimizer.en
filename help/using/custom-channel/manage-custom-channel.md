---
title: Manage and monitor custom channels
description: Learn how to manage the lifecycle of custom channels and channel configurations, and monitor delivery performance through Adobe Journey Optimizer reporting.
feature: Custom Channel
topic: Content Management
role: User
level: Beginner
---

# Manage and monitor custom channels {#manage-custom-channel}

Once a custom channel is created and activated, you can manage its lifecycle and monitor delivery performance through the [!DNL Journey Optimizer] interface.

## Manage custom channels {#manage-channels}

Access the custom channel inventory from **[!UICONTROL Administration]** > **[!UICONTROL Channels]** > **[!UICONTROL Channel Builder]** > **[!UICONTROL Custom channels]**.

All custom channels are listed in the inventory, along with their current status and the authentification type used to connect to the external endpoint.

You can filter the custom channels by status (Draft, Active, or Archived), who created them, and search by name.

To edit a channel, click its name in the inventory, make your changes, and save. For active channels, you can only edit the following fields: Name, Description, Icon, Throttling configuration, Retry configuration

>[!CAUTION]
>
>Modifying throttling or retry settings on an active channel takes effect immediately for all in-flight and future executions.

To archive a channel, open it from the inventory and click **[!UICONTROL Archive]**. Archiving an active channel removes it from all selection drop-downs — campaign action selector, journey actions palette, orchestrated campaigns channel list, channel configurations, and content templates. Existing journeys and campaigns that already use the channel continue to function normally.

## Monitor delivery performance {#monitor-reporting}

[!DNL Journey Optimizer] provides out-of-the-box reporting for custom channels.

### Reporting metrics {#metrics}

The following metrics are available for custom channels in both live (24h) and global (CJA) reports.

| Metric | Description |
|--------|-------------|
| **Attempted deliveries** | Total number of messages sent to the external endpoint. |
| **Successful deliveries** | Messages for which the endpoint returned an HTTP 2xx response. |
| **Profiles targeted** | Number of unique profiles reached. |
| **Clicks** | Number of link clicks tracked in the payload. Requires a subdomain delegated for custom channels. |
| **Errors / Failures** | Number of failed delivery attempts, with breakdown by error reason. |

Learn more about [live reports](../reports/live-report.md) and [global reports](../reports/report-gs-cja.md).

For details on reporting functionalities, refer to [this documentation](../reports/report-cja-manage.md).

<!--
### Journey reports {#journey-reports}

To view delivery data for a custom channel action in a journey:

1. Open the journey from the **[!UICONTROL Journeys]** list.
1. Click **[!UICONTROL View report]** in the top-right area.
   * **[!UICONTROL Live report]** – Data for the last 24 hours.
   * **[!UICONTROL All time]** – Full lifetime data via Customer Journey Analytics (CJA).

### Campaign reports {#campaign-reports}

To view delivery data for a custom channel campaign:

1. Open the campaign from the **[!UICONTROL Campaigns]** list.
1. Click **[!UICONTROL Reports]** in the top-right area.

The campaign report includes execution count, successful deliveries, errors, and click data (if link tracking is enabled).-->

### Monitoring {#monitoring}

In addition to campaign and journey reports, [!DNL Journey Optimizer] provides a dedicated custom channels monitoring dashboard. Access it from **[!UICONTROL Administration]** > **[!UICONTROL Channels]** > **[!UICONTROL Channel Builder]** > **[!UICONTROL Custom channels monitoring]**.

This dashboard lets you monitor the reliability and performance of the API calls [!DNL Journey Optimizer] makes to your external endpoints when delivering custom channel messages. Use it to quickly spot integration issues, latency, and throttling limits.

The Custom channels monitoring dashboard functions like other all-time reports in [!DNL Journey Optimizer]. You can select a time range, filter by channel or endpoint, and drill down to see the campaigns and journeys that rely on each custom channel.

#### Custom channel metrics {#monitoring-kpis}

The **[!UICONTROL Custom channel metrics]** section provides a consolidated view of the operational health and reliability of your custom channel calls.

![Custom channel metrics](assets/custom_channel_metrics.png){width="100%"}

+++ Learn more about custom channel metrics

* **[!UICONTROL Successful calls]**: Total number of HTTP calls that returned a valid response without error.

* **[!UICONTROL 4xx/5xx errors]**: Number of failed calls due to client-side (4xx) or server-side (5xx) errors, highlighting configuration issues or endpoint failures.

* **[!UICONTROL Timeout calls]**: Number of calls that failed because they exceeded the maximum response time. This helps surface latency or performance issues with external endpoints.

* **[!UICONTROL Pre-call failures]**: Number of custom channel sends that failed before the HTTP call was ever made to the external endpoint. These failures occur in [!DNL Journey Optimizer]'s own infrastructure layer — not in your external system. There are three categories:

  | Category | Description |
  |----------|-------------|
  | **Authentication failures** (`AUTH_*`) | [!DNL Journey Optimizer] could not obtain or refresh the OAuth token or credentials needed to call the endpoint. Check that the API credentials linked to the channel configuration are valid and have not expired. |
  | **Request generation errors** (`REQUEST_GENERATION_ERROR`) | [!DNL Journey Optimizer] could not construct a valid HTTP request — for example, because a URL template could not be resolved or a required personalization field was missing. |
  | **HTTP parse errors** (`HTTP_PARSE_ERROR`) | [!DNL Journey Optimizer] received a response from the endpoint but could not parse it into a usable structure. |

  >[!TIP]
  >
  >Pre-call failures indicate a problem on the [!DNL Journey Optimizer] side or in the channel configuration, rather than an issue with your external endpoint. Start troubleshooting by reviewing your API credentials and required payload fields.

* **[!UICONTROL Average latency]**: Average end-to-end response time (in milliseconds) for all HTTP calls, including successful calls, errors, and timeouts.

<!--
* **[!UICONTROL Capped calls]**: Number of calls that were blocked due to capping limits, ensuring downstream systems are not overloaded.

* **[!UICONTROL Average RPS]**: Number of requests per second processed by the custom channel over the selected time range.

* **[!UICONTROL Average successful latency]**: Average end-to-end response time (in milliseconds) for successful calls only, excluding failed requests and timeouts.

* **[!UICONTROL Average queue time]**: Average time (in milliseconds) calls spent waiting in the execution queue before being sent. This only applies to throttled endpoints, where [!DNL Journey Optimizer] queues calls when the throughput limit is reached.-->

+++

#### Custom channels outcomes over time {#outcomes-overtime}

![Custom channel outcomes over time](assets/custom_channel_metrics.png){width="100%"}

The **[!UICONTROL Custom channels outcomes over time]** graph shows the HTTP call KPI trend over the selected time period. The granularity of the time series depends on the selected time range:

* For a 7-day report, each data point shows the KPIs for one day.
* For a 1-day time range, the graph shows the KPIs per hour.
* For a 1-hour time range, the graph shows the KPIs per minute.

#### Latency over time {#latency-overtime}

![Custom channel latency over time](assets/custom_channel_latency.png){width="100%"}

The **[!UICONTROL Latency over time]** graph visualizes the trend of latency metrics over the selected time period. This time-series view allows you to track performance patterns, identify peak latency periods, and monitor the impact of optimizations or system changes over time.

#### Custom channel outcome breakdown {#outcome-breakdown}

![Custom channel outcome breakdown](assets/custom_channel_latency.png){width="100%"}

The **[!UICONTROL Custom channel outcome breakdown]** table provides a hierarchical breakdown of HTTP call metrics — from overall metrics per endpoint at the top level, to metrics per custom channel using that endpoint, down to the campaigns and journeys that rely on them at the bottom level.

#### Latency breakdown {#latency-breakdown}

The **[!UICONTROL Latency breakdown]** table provides a detailed breakdown of latency metrics across your custom channels. This view helps you identify which specific endpoints or channels are experiencing performance issues, enabling you to pinpoint and address latency bottlenecks effectively.

#### Insight Builder {#insight-builder}

Use the **[!UICONTROL Insight Builder]** to create custom visualizations and dashboards based on the custom channel metrics. This tool allows you to combine multiple KPIs, apply filters, and create tailored views that align with your monitoring and reporting needs. [Learn more](../reports/report-cja-manage.md#insight-builder)

## Troubleshooting {#troubleshooting}

If you encounter issues with your custom channel, the following table lists common symptoms, possible causes, and recommended resolutions.

| Symptom | Possible cause | Resolution |
|---------|----------------|------------|
| **HTTP 401 / 403 errors** | Authentication failure — credentials expired or incorrect. | Update the credentials in **[!UICONTROL Administration]** > **[!UICONTROL Channels]** > **[!UICONTROL API credentials]**. |
| **HTTP 429 errors** | External endpoint is throttling requests from [!DNL Journey Optimizer]. | Review your endpoint's rate limits. Reduce the throttling setting in the Channel Builder policy configuration. |
| **HTTP 5xx errors** | External system is down or returning server errors. | Check your external system's health dashboard. Configure error paths on the journey action activity to handle transient failures gracefully. |
| **Unresolved personalization tokens** | Expression references an attribute not present on the profile. | Verify the XDM attribute path is correct. Add a default value fallback: `{{profile.person.name.firstName \| default("Valued Customer")}}`. |
| **Required field validation error** | A required payload field has no value at authoring time. | Ensure all required fields are populated in the content editor. Alternatively, remove the required constraint in the Channel Builder if the field is truly optional. |

## Related resources {#related}

* [Get started with custom channels](get-started-custom-channel.md)
* [Configure a custom channel](custom-channel-configuration.md)
* [Global report overview](../reports/report-gs-cja.md)
* [Journey live report](../reports/live-report.md)
