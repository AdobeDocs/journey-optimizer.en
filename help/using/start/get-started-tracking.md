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

---
# Get started with tracking in Journey Optimizer {#get-started-tracking}

Tracking and monitoring enable you to measure campaign effectiveness, optimize customer experiences, and ensure messages reach their intended recipients. Journey Optimizer provides comprehensive tracking capabilities that capture customer interactions, delivery performance, and system health—helping you make data-driven decisions while respecting privacy and maintaining compliance.

Most tracking is automatically configured when you create messages and journeys. For advanced scenarios, you can set up custom metrics, configure URL parameters, and integrate with external analytics platforms. Access your tracking data through built-in reports or export it for deeper analysis in Customer Journey Analytics.

>[!BEGINSHADEBOX]

What you can track in Journey Optimizer:

📧 **Email interactions** - Opens, clicks, and link performance

🌐 **Web behavior** - Page views, clicks, and engagement patterns  

🛤️ **Journey performance** - Custom metrics, step events, and conversion paths

📊 **Deliverability health** - Bounce rates, spam complaints, and sender reputation

⚙️ **System operations** - Alerts, errors, and custom action performance

>[!ENDSHADEBOX]

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

## Track customer interactions across channels {#tracking-by-channel}

Journey Optimizer provides channel-specific tracking capabilities. Here's how to configure and use tracking for each channel.

+++Email tracking

Email tracking is automatically enabled when you create an email message. Journey Optimizer tracks opens, clicks, and unsubscribes by default—no additional configuration needed.

**Configure tracking options:**

* **Enable/disable tracking** - Control tracking at the message level when designing your email. You can choose to track opens, clicks, or both. [Learn more](../email/message-tracking.md)

* **Set up URL tracking parameters** - Configure tracking parameters at the surface level to automatically append campaign identifiers (utm_campaign, utm_source, etc.) to all email links. This enables attribution tracking across your entire digital ecosystem. [Learn more](../email/url-tracking.md)

* **Track links in saved fragments** - When you save a fragment from content that has tracking enabled, the links in that fragment remain tracked when you reuse it in other journeys or campaigns. [Learn more](../content-management/save-fragments.md)

* **Add mirror page tracking** - Enable mirror page option to create a web version of your email with automatic tracking of who views it. [Learn more](../email/message-tracking.md#mirror-page)

**Monitor performance:** View real-time metrics in campaign and journey reports including opens, clicks, and link-level performance. [Campaign reports](../reports/campaign-global-report-cja-email.md) | [Journey reports](../reports/journey-global-report-cja-email.md)

+++

+++Web tracking

Web tracking requires explicit configuration to track user interactions with your web modifications.

**Set up click tracking:**

When authoring a web page, you can select specific elements (buttons, images, links) that you want to track. This enables click tracking for those elements without requiring additional code. [Learn more](../web/monitor-web-experiences.md)

* **Track any clickable element** - Select buttons, images, links, or any interactive element in your web personalization.
* **Automatic data collection** - Once configured, Journey Optimizer automatically captures click events and associates them with profiles.
* **Monitor in real-time** - Track user interactions as they happen to validate personalization effectiveness.

**View tracking data:** Access display metrics, click-through rates, and element-level performance in reports. [Campaign reports](../reports/campaign-global-report-cja-web.md) | [Journey reports](../reports/journey-global-report-cja-web.md)

+++

+++Push notification tracking

Push tracking is automatically enabled and captures impressions (delivered), clicks (tapped), and opens (app launched). To maximize tracking value, configure clickable elements in your push content.

**Configure tracked elements:**

* **Body click behavior** - Set what happens when users tap the notification: open app, navigate to a deeplink, or open a web URL. Each action is automatically tracked. [Learn more](../push/design-push.md#on-click-behavior)

* **Add action buttons** - Include up to 3 buttons (Android) or multiple buttons (iOS) with independent tracking for each button action (open app, deeplink, web URL). [Learn more](../push/design-push.md#add-buttons-push)

* **Enable tracking** - Verify tracking is enabled in your push journey activity or campaign tracking settings. [Learn more](../push/create-push.md#create)

>[!NOTE]
>
>Push tracking requires mobile SDK implementation. Ensure your app has the Adobe Experience Platform Mobile SDK properly configured. [Learn more](../push/push-configuration.md#integrate-mobile-app)

**Analyze engagement:** View click-through rates, button performance, and tracked link details in reports. [Campaign reports](../reports/campaign-global-report-cja-push.md) | [Journey reports](../reports/journey-global-report-cja-push.md)

+++

+++In-app message tracking

In-app messages automatically track displays and user interactions. Configure triggers and content to maximize tracking effectiveness.

**Set up tracking:**

* **Define display rules** - Set when and where in-app messages appear using triggers (app launch, screen load), frequency rules, and audience conditions. Proper configuration ensures accurate tracking of both triggered and displayed messages.

* **Add tracked elements** - Include buttons, links, and interactive elements in your message content. Each interaction is automatically tracked with detailed labels.

* **Optimize display timing** - Configure day-of-week and time-of-day rules to maximize the likelihood that triggered messages are actually displayed to users.

[Learn how to configure In-app messages](../in-app/create-in-app.md)

**What gets tracked:** Journey Optimizer automatically captures displays, button clicks, dismissals, triggered vs. displayed metrics, and link performance. [Campaign reports](../reports/campaign-global-report-cja-inapp.md) | [Journey reports](../reports/journey-global-report-cja-inapp.md)

+++

+++SMS & MMS tracking

SMS tracking requires minimal setup—Journey Optimizer automatically shortens and tracks links you include in messages.

**How it works:**

* **Automatic link tracking** - Add any URL to your SMS content using the URL helper function. Journey Optimizer automatically shortens the link and tracks clicks without additional configuration. To use URL shortening, you must first configure an SMS subdomain. [Learn more](../sms/sms-subdomains.md)

* **Inbound message tracking** - Replies from recipients are automatically captured, allowing you to monitor two-way conversations and response patterns. [Learn more](../sms/sms-opt-out.md#sms-native-keywords)

**View metrics:** Access link click data, inbound message volumes, and message type performance in reports. [Campaign reports](../reports/campaign-global-report-cja-sms.md) | [Journey reports](../reports/journey-global-report-cja-sms.md)

+++

+++Code-based experience tracking

Code-based experiences require implementation setup to send tracking data to Adobe Experience Platform.

**Prerequisites:**

Before tracking will work, you need to configure your implementation to send interaction events (displays, clicks) to Adobe Experience Platform. This requires:

* Setting up a datastream configured for Adobe Experience Platform. [Learn more](https://experienceleague.adobe.com/docs/experience-platform/edge/datastreams/overview.html)
* Implementing event collection in your code using Web SDK or Mobile SDK.
* Sending display and interaction events when content is shown or clicked.

[Learn more about implementation prerequisites](../code-based/code-based-prerequisites.md#reporting-prerequisites)

**What gets tracked:** Once implemented, track displays, clicks, click-through rates, and element-level performance across any digital touchpoint (websites, mobile apps, IoT devices, etc.). [Campaign reports](../reports/campaign-global-report-cja-code.md) | [Journey reports](../reports/journey-global-report-cja-code.md)

+++

+++Content card tracking

Content cards automatically track user interactions. Configure content and display rules to control tracking behavior.

**How to implement:**

* **Design tracked content** - Add buttons and links to your content card. Each interactive element is automatically tracked with labels and URLs.

* **Configure persistence** - Content cards persist across app sessions, allowing you to track long-term engagement patterns. Set expiration rules to control how long cards remain trackable.

* **Set up display rules** - Define when and where cards appear to ensure accurate tracking of displays vs. interactions.

[Learn how to configure content cards](../content-card/create-content-card.md)

**Monitor engagement:** Track displays, clicks, click-through rates, and engagement patterns across multiple sessions. [Campaign reports](../reports/campaign-global-report-cja-content.md) | [Journey reports](../reports/journey-global-report-cja-content.md)

+++

+++Landing page tracking

Landing pages come with built-in tracking that requires no additional setup. Journey Optimizer automatically captures visits, conversions, and bounce rates.

**What's tracked automatically:**

* **Visits** - Total and unique visits to measure reach
* **Conversions** - Form submissions, subscription confirmations, or other defined actions
* **Bounce rate** - Percentage of visitors who leave without interacting
* **Performance trends** - Time-series data showing how metrics evolve

[Learn how to configure landing pages](../landing-pages/create-lp.md)

**Monitor performance:** Track visit patterns, conversion rates, and bounce rates over time to understand how users interact with your forms and identify areas for improvement. [Campaign reports](../reports/lp-report-global-cja.md)

+++

## Track your journey and campaign activity {#journey-campaign-tracking}

Beyond channel-level tracking, configure tracking to measure overall performance and understand customer behavior across your marketing initiatives.

* **Define custom success metrics** - Configure specific KPIs aligned with your business objectives (purchases, sign-ups, renewals, etc.) beyond standard engagement metrics. [Learn more](../building-journeys/success-metrics.md)

* **Enable journey step events** - Activate detailed tracking of every action customers take as they move through journeys. This provides granular visibility into entry/exit points, path selection, and drop-off locations. [Learn more](../reports/journey-step-events-overview.md)

* **Set up scheduling** - Configure send-time optimization to track performance across different timing strategies and identify optimal send windows. [Learn more](../building-journeys/send-time-optimization.md)

* **Configure custom actions monitoring** - Set up tracking for integrations with external systems to monitor API calls, response times, and error patterns. [Learn more](../action/reporting.md)

* **Custom reporting & data export** - Build tailored reports and export tracking data to external systems for deeper analysis. [Learn more](../reports/sharing-overview.md)

**View unified performance:** Access comprehensive reports for both campaigns and journeys to compare performance across email, push, SMS, and other channels, and to understand which combinations drive the best results. [Campaign reports](../reports/campaign-global-report-cja.md) | [Journey reports](../reports/journey-global-report-cja.md)

## Track optimization & decisioning performance {#optimization-decisioning-tracking}

Journey Optimizer automatically tracks optimization experiments, targeting strategies, and decisioning performance. Configure your settings to ensure proper data collection.

### Set up optimization tracking {#optimization-tracking}

* **Optimization in your campaigns and journeys**

    * When creating experiments, define which metrics to track (conversions, clicks, custom events). Journey Optimizer automatically collects performance data for each treatment. [Learn more](../campaigns/campaigns-message-optimization.md#experimentation)

    * Create targeting rules to deliver different content to different audience segments. Journey Optimizer automatically tracks engagement metrics for each targeted group, allowing you to compare performance across segments. [Learn more](../campaigns/campaigns-message-optimization.md#targeting)

* **Journey path optimization** - Add an **Optimize** activity to your journey and configure multiple paths. Journey Optimizer automatically tracks which paths profiles take and measures performance. [Learn more](../building-journeys/optimize.md)

**Analyze results:** View conversion rates, statistical significance, and lift between treatments in experimentation reports, or compare engagement metrics across targeted segments. [Experimentation campaign report](../reports/campaign-global-report-cja-experimentation.md) | [Experimentation journey report](../reports/journey-global-report-cja-experimentation.md) | [Journey targeting report](../reports/journey-global-report-cja.md#targeting)

### Track decisioning performance {#decisioning-tracking}

When using Decisioning to personalize content, Journey Optimizer automatically tracks decision events, impressions, and clicks with no additional configuration required.

* **Automatic event capture** - Journey Optimizer automatically captures decision events whenever a decision item is selected for a profile.
* **Impression tracking** - For emails, impressions are tracked automatically. For code-based experiences, you need to implement proposition display events in your code.
* **Click tracking** - Clicks on decision items are automatically tracked in emails; code-based experiences require implementing click events.

**Prerequisites for code-based tracking:** To track decisioning in code-based experiences, ensure your implementation sends proposition interaction events (displays and clicks) to Adobe Experience Platform using Web SDK or Mobile SDK. [Learn more](../experience-decisioning/data-collection/schema-requirement.md)

**Analyze performance:** View decisioning KPIs, compare decision items, analyze selection strategies, and monitor AI model performance in reports. [Learn more](../experience-decisioning/cja-reporting.md)

## Control tracking data usage {#data-governance}

Data governance policies allow you to control how tracking data can be used across your organization:

* **Label sensitive tracking data** - Apply governance labels to tracked behavioral data (e.g., clicks on health content, financial product interactions) to mark it as sensitive or regulated.

* **Restrict data usage** - Create policies that prevent labeled tracking data from being used in certain channels, exported to third-party systems, or used for specific personalization scenarios.

* **Automatic enforcement** - Journey Optimizer automatically checks governance policies when you build journeys and campaigns, blocking publication if tracked data is being used in violation of defined policies.

Data governance ensures compliance with regulations like GDPR and CCPA while still allowing you to track and analyze customer behavior within approved boundaries. [Learn more](../action/action-privacy.md)

## Monitor deliverability & system health {#monitoring-capabilities}

Beyond tracking engagement, configure monitoring to ensure messages reach inboxes and systems perform optimally.

Deliverability monitoring helps ensure your messages reach recipients' inboxes and maintain healthy sender reputation by tracking key indicators:

* **Review the suppression list** regularly to understand why addresses are blocked and maintain list hygiene. [Learn more](../reports/suppression-list.md)

* **Analyze delivery errors** to diagnose failures and take corrective action. [Learn more](../configuration/email-error-types.md)

* **Follow best practices** for DMARC, SPF, and DKIM to maximize inbox placement. [Learn more](../reports/deliverability.md)

Set up proactive monitoring to receive real-time notifications about critical events and system issues, enabling you to respond quickly before they impact your customer experiences:

* **Configure alerts** - Set up real-time notifications for journey errors, custom action failures, and critical issues to respond quickly to problems. [Learn more](../reports/alerts.md)

* **Enable audit logs** - Activate audit logging to track all actions on resources for compliance and troubleshooting. [Learn more](../privacy/audit-logs.md)

* **Monitor integrations** - Track custom action performance and external system connectivity to identify integration issues early. [Learn more](../action/reporting.md)

