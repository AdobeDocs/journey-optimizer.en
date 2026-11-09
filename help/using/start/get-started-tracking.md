---
solution: Journey Optimizer
product: journey optimizer
title: Get started with tracking in Journey Optimizer
description: Learn about tracking and monitoring capabilities available in Journey Optimizer
feature: Monitoring
topic: Administration
role: User
level: Beginner
keywords: tracking, monitor, analytics, reporting, deliverability
exl-id: d5e7adb7-8473-4c29-8ae6-ba979aef97f3
TQID: 'https://experienceleague.adobe.com/jLHTNJlUPQm39EZvTLLBvYT92eGlCBoHpTKBfJ1Zxlk'
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: b49ca41f-eb7a-4f4b-abeb-a97c06fd0c04
    internal-label: Track and monitor
  - id: d998adac-2f81-400b-a669-d07bb196e4eb
    internal-label: Journeys
  - id: bb359667-ec7d-4d4b-8663-5850fc219d32
    internal-label: Administration
subfeature_v2:
  - id: e30b0a1a-b594-47b8-af94-1e3a2be6df11
    internal-label: Get started
  - id: 9bb4b199-a2fd-5580-9021-eafbab678ff5
    internal-label: Monitoring
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
level_v2:
  - id: e8ccd51f-da0d-4e3b-939b-e30d5ebb1ea5
    internal-label: Beginner
topic_v2:
  - id: aa2f3246-cb95-4b30-8899-fdf7d73550cc
    internal-label: Reporting
  - id: b5ce8718-c3af-4fdb-a1a9-fca32f83a87c
    internal-label: Implementation
  - id: bcc5edb5-84c3-4940-9f84-ed88b6c16274
    internal-label: Experimentation
  - id: bce87dde-a4ab-44c9-8a18-ad66e4ddb377
    internal-label: Customer experience
  - id: c1579802-ddd4-4214-8a91-97b2066abe11
    internal-label: Troubleshooting
  - id: c4147b6e-073b-4d3c-9ab1-d60f2f4434ef
    internal-label: Behavioral data
  - id: c7d04a2c-412a-4c9d-9d7a-4456eaa5adeb
    internal-label: Governance
  - id: cdd65e7e-8839-44a2-bc21-0e03623b5dd1
    internal-label: Optimization
  - id: d3cdead0-685a-4489-9250-4bb709942f66
    internal-label: Data collection
  - id: e0eb8757-182f-49f3-94a4-1587d16f5094
    internal-label: Personalization
  - id: eddd9b14-83bd-4ff4-9072-54a4a484abb7
    internal-label: Administration
  - id: f4e6943a-c91a-4134-a2c7-f4f20cfff2f0
    internal-label: Privacy
---
# Get started with tracking in Journey Optimizer {#get-started-tracking}

>[!BEGINSHADEBOX]

**On this page:** Learn what Journey Optimizer tracks automatically, what you must set up, and where to find tracking, deliverability, and system health data.

>[!ENDSHADEBOX]

Tracking lets you measure campaign effectiveness, optimize experiences, and confirm that messages reach recipients. Journey Optimizer collects most interaction data automatically. For some channels, you must configure elements or implement an SDK first.

## Where to find your data {#where-data-lives}

| Where | Best for | Learn more |
|---|---|---|
| **Live reports** | Near-real-time delivery and engagement for the last 24 hours | [Live report](../reports/live-report.md) |
| **All-time reports (Customer Journey Analytics)** | All-time campaign and journey performance, by channel | [Reporting overview](../reports/gs-reports.md) |
| **Query Service and datasets** | Custom analysis, delivery errors, journey step events | [Journey step events](../reports/journey-step-events-overview.md), [Message feedback event dataset](../data/datasets-query-examples.md#message-feedback-event-dataset) |

To help you get started, explore these essential tracking and monitoring topics:

<table style="table-layout:fixed">
<tr style="border: 0;">
  <td>
    <a href="../building-journeys/success-metrics.md">
    <img alt="Metrics" src="../assets/do-not-localize/success-metrics.jpeg">
    </a>
    <div>
    <a href="../building-journeys/success-metrics.md"><strong>Configure success metrics</strong></a>
    </div>
    <p>
    <em>Track custom KPIs aligned with your business objectives</em>
    <p>
  </td>
  <td>
    <a href="../reports/deliverability.md">
    <img alt="Deliverability" src="../assets/do-not-localize/deliverability.jpeg">
    </a>
    <div>
    <a href="../reports/deliverability.md"><strong>Monitor deliverability</strong></a>
    </div>
    <p>
    <em>Ensure your messages reach customer inboxes</em>
    <p>
  </td>
  <td>
    <a href="../reports/gs-reports.md">
    <img alt="Reporting" src="../assets/do-not-localize/reporting.jpeg">
    </a>
    <div>
    <a href="../reports/gs-reports.md"><strong>Explore reporting</strong></a>
    </div>
    <p>
    <em>Access live and historical reports for your journeys and campaigns</em>
    <p>
  </td>
</tr>
</table>

## Track customer interactions by channel {#tracking-by-channel}

Use this table to see what each channel needs before you build. Details for each channel follow.

| Channel | Tracking | What you must do | What is tracked |
|---|---|---|---|
| [Email](#email) | On by default | Optional: adjust tracking options, add URL parameters | Opens, clicks, unsubscribes, link performance |
| [Web](#web) | Requires configuration | Select the elements to track when authoring the page | Displays, clicks, click-through rate, element performance |
| [Push](#push) | Requires Mobile SDK | Integrate the Adobe Experience Platform Mobile SDK; configure click behavior and buttons | Impressions (delivered), clicks (tapped), opens (app launched), button actions |
| [In-app](#in-app) | Requires app integration with the SDK | Configure triggers, display rules, and interactive elements | Triggered, displayed, clicks, dismissals |
| [Mobile messages](#mobile-message) | Link tracking needs an SMS subdomain | Configure an SMS subdomain; use the URL helper function for links | Link clicks, inbound messages and opt-out keyword replies |
| [Code-based experiences](#code-based) | Requires implementation | Datastream, Web or Mobile SDK, display and interaction events | Displays, clicks, click-through rate, element performance |
| [Content cards](#content-cards) | Requires SDK | Add buttons or links; configure display rules | Displays, clicks, click-through rate |
| [Landing pages](#landing-pages) | On by default | None | Visits, conversions, bounce rate, trends |

### Email {#email}

Journey Optimizer tracks opens, clicks, and unsubscribes by default. You can change this behavior:

* **Choose what to track.** Track opens, clicks, or both at the message level. [Learn more](../email/message-tracking.md)
* **Append URL parameters.** Configure tracking parameters (such as `utm_campaign` and `utm_source`) at the surface level to add them to all email links. [Learn more](../email/url-tracking.md)
* **Reuse tracked links.** Links in a saved fragment stay tracked when you reuse the fragment in other journeys or campaigns. [Learn more](../content-management/save-fragments.md)
* **Track mirror page views.** Enable the mirror page option to create a web version of the email and track who views it. [Learn more](../email/message-tracking.md#mirror-page)

>[!NOTE]
>
>Mail privacy features, such as Apple Mail Privacy Protection, can prevent tracking pixels from recording opens. Use clicks as your primary engagement signal. [Learn more](../reports/campaign-global-report-cja-email.md)

View results in the [email campaign report](../reports/campaign-global-report-cja-email.md) and the [email journey report](../reports/journey-global-report-cja-email.md).

### Web {#web}

Web tracking requires explicit configuration. When you author a web page, select the buttons, images, links, or other interactive elements you want to track. Journey Optimizer then captures click events and associates them with profiles, without extra code. [Learn more](../web/monitor-web-experiences.md)

View results in the [web campaign report](../reports/campaign-global-report-cja-web.md) and the [web journey report](../reports/journey-global-report-cja-web.md).

### Push notifications {#push}

>[!IMPORTANT]
>
>Push tracking requires the Adobe Experience Platform Mobile SDK in your app. [Learn how to integrate your mobile app](../push/push-configuration.md#integrate-mobile-app)

With the SDK in place, Journey Optimizer captures impressions (delivered), clicks (tapped), and opens (app launched). To get more detail, configure clickable elements:

* **Body click behavior.** Choose what happens when users tap the notification: open the app, open a deep link, or open a web URL. Each action is tracked. [Learn more](../push/design-push.md#on-click-behavior)
* **Tracking options.** Make sure the push opening and interaction tracking options are enabled in the push activity of your journey or in your campaign. [Learn more](../push/create-push.md#create)
* **Action buttons.** Add buttons (open app, deep link, web URL), each tracked independently. On Android, you can add up to three buttons. On iOS, buttons are defined by a notification category that is preconfigured in your app. [Learn more](../push/design-push.md#add-buttons-push)

View results in the [push campaign report](../reports/campaign-global-report-cja-push.md) and the [push journey report](../reports/journey-global-report-cja-push.md).

### In-app messages {#in-app}

In-app messages track displays and interactions. Configure these settings so the data is accurate:

* **Display rules.** Set when and where messages appear (triggers, frequency, audience conditions) so triggered and displayed counts are meaningful. You can also use day-of-week and time-of-day triggers.
* **Interactive elements.** Add buttons, links, and other elements. Each interaction is tracked with a label.

Tracked metrics include displays, button clicks, dismissals, triggered versus displayed counts, and link performance. A message is *triggered* when its conditions are met, and *displayed* only when the user actually sees it. [Learn how to configure in-app messages](../in-app/create-in-app.md)

View results in the [in-app campaign report](../reports/campaign-global-report-cja-inapp.md) and the [in-app journey report](../reports/journey-global-report-cja-inapp.md).

### Mobile messages {#mobile-message}

* **Link tracking.** Add URLs to your mobile content with the URL helper function. Journey Optimizer shortens each link and tracks clicks. Configure an SMS subdomain first. [Learn more](../mobile/mobile-subdomains.md)
* **Inbound messages and opt-out keywords.** Inbound messages appear in the mobile message report. Replies that match opt-out keywords (such as STOP) update the profile's opt-out status. Native keyword handling is supported with Sinch and Infobip only. Two-way messaging requires at least one prior one-way message to the number, and alphanumeric sender IDs cannot receive replies. [Learn more](../mobile/mobile-opt-out.md#sms-native-keywords)

View results in the [mobile message campaign report](../reports/campaign-global-report-cja-sms.md) and the [mobile message journey report](../reports/journey-global-report-cja-sms.md).

### Code-based experiences {#code-based}

Tracking works only after you configure your implementation to send interaction events to Adobe Experience Platform:

1. Set up a [datastream](https://experienceleague.adobe.com/en/docs/experience-platform/datastreams/overview){target="_blank"} configured for Adobe Experience Platform.
1. Implement event collection with the Web SDK or Mobile SDK.
1. Send display and interaction events when content is shown or clicked.

[Learn more about reporting prerequisites](../code-based/code-based-prerequisites.md#reporting-prerequisites)

View results in the [code-based campaign report](../reports/campaign-global-report-cja-code.md) and the [code-based journey report](../reports/journey-global-report-cja-code.md).

### Content cards {#content-cards}

Content cards require the Adobe Experience Platform Web or Mobile SDK in your app or website. [Learn more](../content-card/content-card-configuration-prereq.md) Add buttons and links to your content card to track interactions, and define display rules so displays and interactions are measured accurately. Cards persist in the app or website until the user dismisses them, so you can observe engagement across sessions. [Learn how to configure content cards](../content-card/create-content-card.md)

View results in the [content card campaign report](../reports/campaign-global-report-cja-content.md) and the [content card journey report](../reports/journey-global-report-cja-content.md).

### Landing pages {#landing-pages}

Landing pages track visits (total and unique), conversions (such as form submissions), bounce rate, and trends over time, with no setup. [Learn how to configure landing pages](../landing-pages/create-lp.md)

View results in the [landing page report](../reports/lp-report-global-cja.md).

## Track journey and campaign activity {#journey-campaign-tracking}

Beyond channel tracking, use these capabilities to measure overall performance:

* **Define success metrics.** Measure KPIs such as purchases, sign-ups, or renewals. [Learn more](../building-journeys/success-metrics.md)
* **Analyze journey step events.** Journey Optimizer automatically streams an event to Adobe Experience Platform for every step a profile takes in a journey. Use them to see entry and exit points, path selection, and drop-off. The schemas and datasets are read-only. [Learn more](../reports/journey-step-events-overview.md)
* **Analyze data outside the built-in reports.** Query step events with Query Service or link them to other datasets in Customer Journey Analytics. [Learn more](../reports/sharing-overview.md)
* **Monitor custom actions.** Review success, error, timeout, capping, and latency metrics for calls your journeys make to external systems. [Learn more](../action/reporting.md)
* **Compare channels.** Use the global [campaign report](../reports/campaign-global-report-cja.md) and [journey report](../reports/journey-global-report-cja.md) to compare performance across channels.

>[!NOTE]
>
>[Send-Time Optimization](../building-journeys/send-time-optimization.md) improves engagement but is not a tracking feature. It is available for Email and Push actions and the Wait activity in journeys (not campaigns), and must be enabled by Adobe.

## Track optimization and decisioning {#optimization-decisioning-tracking}

### Optimization {#optimization-tracking}

* **Experiments.** Define the metrics to track (conversions, clicks, custom events). Journey Optimizer collects data for each treatment. [Learn more](../content-management/optimization-experimentation.md)
* **Targeting rules.** Engagement is tracked for each targeted group so you can compare segments. [Learn more](../content-management/optimization-targeting.md)
* **Journey path optimization.** Add an **Optimize** activity with multiple paths. Journey Optimizer tracks which paths profiles take and measures performance. [Learn more](../building-journeys/optimize.md)

To analyze results, see conversion rates, statistical significance, and lift in the [experimentation campaign report](../reports/campaign-global-report-cja-experimentation.md), the [experimentation journey report](../reports/journey-global-report-cja-experimentation.md), or the [journey targeting report](../reports/journey-global-report-cja.md#targeting).

### Decisioning {#decisioning-tracking}

Journey Optimizer automatically captures a decision event whenever a decision item is selected for a profile. Impressions and clicks depend on the channel:

| Channel | Impressions | Clicks |
|---|---|---|
| Email | Automatic | Automatic |
| Code-based experiences | You implement proposition display events | You implement proposition click events |

For code-based experiences, send proposition interaction events to Adobe Experience Platform with the Web SDK or Mobile SDK. [Learn more](../experience-decisioning/data-collection/schema-requirement.md)

To review decisioning KPIs, compare decision items, and monitor AI model performance, see the [decisioning reports](../experience-decisioning/cja-reporting.md).

## Control how tracking data is used {#data-governance}

Data governance helps you enforce your organization's policies on tracked data:

* **Label.** Apply governance labels to behavioral data that is sensitive or regulated, such as interactions with health or financial content.
* **Restrict.** Create policies that prevent labeled data from being used in certain channels, exported to third-party systems, or used for specific personalization.
* **Enforce.** Journey Optimizer checks policies when you build journeys and campaigns, and blocks publication if data is used in violation of a policy.

[Learn more](../action/action-privacy.md)

## Monitor deliverability and system health {#monitoring-capabilities}

### Deliverability {#deliverability-monitoring}

* **Review the suppression list** to see why addresses are blocked and keep your lists clean. [Learn more](../reports/suppression-list.md)
* **Analyze delivery errors** to diagnose failures. [Learn more](../configuration/email-error-types.md)
* **Follow deliverability best practices**, including reducing complaint rates, IP warmup, and DMARC. [Learn more](../reports/deliverability.md)

>[!NOTE]
>
>Gmail, Apple iCloud, and corporate Microsoft 365 do not return per-recipient spam complaints, so complaints from those providers do not appear on the suppression list. [Learn more](../reports/deliverability.md#providers-no-fbl)

### System health {#system-health}

* **Configure alerts.** Subscribe to notifications for journey errors, custom action failures, and other critical issues. [Learn more](../reports/alerts.md)
* **Review audit logs.** Audit logs automatically record user actions on resources, which helps you troubleshoot issues and demonstrate compliance. You need the **View User Activity Log** permission to view and export them. [Learn more](../privacy/audit-logs.md)
* **Monitor integrations.** Track custom action performance and external system connectivity. [Learn more](../action/reporting.md)

{{$include /help/_includes/do-not-localize/start/ai-augmented-get-started-tracking.md}}
