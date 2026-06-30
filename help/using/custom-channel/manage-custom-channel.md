---
title: Manage and monitor custom channels
description: Learn how to manage the lifecycle of custom channels and channel configurations, and monitor delivery performance through Adobe Journey Optimizer reporting.
feature: Custom Channel
topic: Content Management
role: User
level: Beginner
---

# Manage and monitor custom channels {#manage-custom-channel}

## Manage custom channels {#manage-channels}

Access the custom channel inventory from **[!UICONTROL Administration]** > **[!UICONTROL Channels]** > **[!UICONTROL CHANNEL BUILDER]** > **[!UICONTROL Custom channels]**.

### Edit a channel {#edit-channel}

The fields you can edit depend on the channel's current status:

| Status | Editable fields |
|--------|-----------------|
| **Draft** | All fields |
| **Active** | Name, description, icon, throttling configuration, retry configuration |

To edit a channel, click its name in the inventory, make your changes, and save.

>[!CAUTION]
>
>Modifying throttling or retry settings on an active channel takes effect immediately for all in-flight and future executions.

### Archive a channel {#archive-channel}

Archiving an active channel removes it from all selection drop-downs — Campaign action selector, Journey actions palette, Orchestrated Campaigns channel list, Channel configurations, and Content Templates. Existing journeys and campaigns that already use the channel continue to function normally.

To archive a channel, open it from the inventory and click **[!UICONTROL Archive]**.

### Delete a channel {#delete-channel}

A channel can only be deleted while it is in **[!UICONTROL Draft]** status. Once activated, a channel can only be archived.

To delete a draft channel, open it from the inventory and click **[!UICONTROL Delete]**.

## Monitor delivery performance {#monitor-reporting}

[!DNL Journey Optimizer] provides OOTB reporting for custom channels.

### Reporting metrics {#metrics}

The following metrics are available for custom channels in both live (24h) and global (CJA) reports, consistent with SMS live reports:

| Metric | Description |
|--------|-------------|
| **Attempted deliveries** | Total number of messages sent to the external endpoint. |
| **Successful deliveries** | Messages for which the endpoint returned an HTTP 2xx response. |
| **Profiles targeted** | Number of unique profiles reached. |
| **Clicks** | Number of link clicks tracked in the payload. Requires a subdomain delegated for custom channels. |
| **Errors / Failures** | Number of failed delivery attempts, with breakdown by error reason. |

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

The campaign report includes execution count, successful deliveries, errors, and click data (if link tracking is enabled).

### Monitoring and observability {#monitoring}

In addition to campaign and journey reports, [!DNL Journey Optimizer] provides a dedicated **Custom channels monitoring** dashboard. Access it from **[!UICONTROL Administration]** > **[!UICONTROL Channels]** > **[!UICONTROL Channel builder]** > **[!UICONTROL Custom channels monitoring]**.

The dashboard is similar to the Custom actions monitoring view and provides throughput and error charts at both the **endpoint level** and the **channel level**. Use it to:

* Visualize request throughput over time.
* Identify error spikes and their causes.
* Compare performance across multiple channels or configurations that share the same endpoint.

The dashboard surfaces the following metric in addition to standard delivery metrics:

| Metric | Description |
|--------|-------------|
| **Pre-call failures** | Number of custom channel sends that failed before the HTTP call was ever made to the external endpoint. These failures occur in [!DNL Journey Optimizer]'s own infrastructure layer — not in your external system — and break down into three categories: authentication failures, request generation errors, and HTTP parse errors. |

**Pre-call failure categories:**

| Category | Description |
|----------|-------------|
| **Authentication failures** (`AUTH_*`) | [!DNL Journey Optimizer] could not obtain or refresh the OAuth token or credentials needed to call the endpoint. Check that the API credentials linked to the channel configuration are valid and have not expired. |
| **Request generation errors** (`REQUEST_GENERATION_ERROR`) | [!DNL Journey Optimizer] could not construct a valid HTTP request — for example, because a URL template could not be resolved or a required personalization field was missing. |
| **HTTP parse errors** (`HTTP_PARSE_ERROR`) | [!DNL Journey Optimizer] received a response from the endpoint but could not parse it into a usable structure. |

>[!TIP]
>
>Pre-call failures indicate a problem on the [!DNL Journey Optimizer] side or in the channel configuration, rather than an issue with your external endpoint. Start troubleshooting by reviewing your API credentials and required payload fields.

## Troubleshooting {#troubleshooting}

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
* [Permissions reference](../administration/ootb-permissions.md)
