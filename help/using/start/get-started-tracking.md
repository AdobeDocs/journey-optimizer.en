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

Adobe Journey Optimizer provides comprehensive tracking and monitoring capabilities to help you understand how your customers interact with your communications, optimize delivery performance, and ensure compliance.

## Tracking capabilities by channel {#tracking-by-channel}

Journey Optimizer offers various tracking options, depending on the channel you're using:

### Email tracking {#email-tracking}

Track email opens, clicks, and engagement to understand recipient behavior:

* **Email opens & clicks**: Enable tracking to monitor how recipients interact with your emails. [Learn more](../email/message-tracking.md)

* **Link tracking**: Track all links included in your email content, including links in fragments. [Learn more](../email/message-tracking.md#insert-links)

* **URL tracking parameters**: Add tracking parameters to URLs to measure marketing effectiveness across channels. [Learn more](../email/url-tracking.md)

* **Mirror page tracking**: Provide an online version of your email with automatic tracking. [Learn more](../email/message-tracking.md#mirror-page)

### Web tracking {#web-tracking}

Monitor how users interact with your web experiences:

* **Click tracking**: Track clicks on specific elements of your website to improve user experience. [Learn more](../web/monitor-web-experiences.md#use-click-tracking)

* **Web reports**: View impressions, click rates, and engagements for your web pages. [Learn more](../web/monitor-web-experiences.md)

### Journey & campaign tracking {#journey-campaign-tracking}

Track and measure the success of your customer journeys and campaigns:

* **Journey metrics**: Configure and track custom success metrics aligned with your KPIs. [Learn more](../building-journeys/success-metrics.md)

* **Journey step events**: Get detailed information about each step profiles take in a journey. [Learn more](../reports/journey-step-events-overview.md)

* **Journey reporting**: Create custom reports to analyze journey performance. [Learn more](../reports/sharing-overview.md)

## Monitoring & analytics capabilities {#monitoring-capabilities}

Beyond tracking interactions, Journey Optimizer provides monitoring tools to ensure optimal performance:

### Deliverability monitoring {#deliverability-monitoring}

* **Suppression list**: Understand which email addresses are excluded from sending and why. [Learn more](../reports/suppression-list.md)

* **Email error types**: Learn about different delivery failures and how to address them. [Learn more](../configuration/email-error-types.md)

* **Deliverability best practices**: Follow guidelines to maximize email deliverability. [Learn more](../reports/deliverability.md)

* **Retries**: Understand how Journey Optimizer handles temporary delivery failures. [Learn more](../configuration/retries.md)

### System monitoring {#system-monitoring}

* **System alerts**: Receive notifications about important system events and journey issues. [Learn more](../reports/alerts.md)

* **Audit logs**: Track actions performed on Journey Optimizer resources for compliance and troubleshooting. [Learn more](../privacy/audit-logs.md)

* **Custom actions monitoring**: Monitor the performance of your custom actions in journeys. [Learn more](../action/reporting.md)

### Performance analytics {#performance-analytics}

* **Journey analytics**: Analyze journey performance, conversion paths, and drop-off points. [Learn more](../reports/journey-global-report-cja.md)

* **Campaign analytics**: Track campaign performance across all channels. [Learn more](../reports/campaign-global-report-cja.md)

* **Real-time monitoring**: Monitor profiles flowing through journeys in real-time. [Learn more](../reports/live-report.md)

* **Customer Journey Analytics integration**: Create comprehensive customer profiles combining journey interactions with other data sources. [Learn more](../reports/cja-ajo.md)

## Key tracking concepts {#key-concepts}

### Data collection & integration {#data-collection}

Journey Optimizer automatically generates tracking data and sends it to Adobe Experience Platform, enabling:

* **Cross-platform analysis**: Combine journey data with other data sources. [Learn more](../data/lookup-aep-data.md)
* **Customer 360 view**: Create comprehensive customer profiles including journey interactions. [Learn more](../audience/get-started-profiles.md)
* **Attribution modeling**: Connect journey touchpoints to business outcomes. [Learn more](../reports/cja-ajo.md)

### Privacy & compliance {#privacy-compliance}

All tracking capabilities in Journey Optimizer respect customer privacy preferences:

* **Consent management**: Honor customer consent policies for tracking and communications. [Learn more](../action/consent.md)

* **Data governance**: Apply data usage labels to control how tracking data is used. [Learn more](../action/action-privacy.md)

* **Privacy requests**: Handle customer requests to access or delete their tracking data. [Learn more](../privacy/requests.md)

## How to implement tracking {#implement-tracking}

To start using tracking capabilities in Journey Optimizer:

1. **Enable tracking** at the message level when creating emails, web experiences, or other communications. [Learn more](#tracking-by-channel)

2. **Configure tracking parameters** at the channel configuration level to automatically append tracking information to URLs. [Learn more](../email/url-tracking.md)

3. **Set up custom metrics** to track specific KPIs aligned with your business goals. [Learn more](../building-journeys/success-metrics.md)

4. **Access reports** to monitor performance and gain insights into customer behavior. [Learn more](../reports/gs-reports.md)

5. **Integrate with analytics tools** like Adobe Analytics or Customer Journey Analytics for advanced analysis. [Learn more](../reports/cja-ajo.md)

## Related topics {#related-topics}

* [Reporting overview](../reports/gs-reports.md)
* [Channel configuration](../configuration/get-started-configuration.md)
* [Journey creation](../building-journeys/journey-gs.md)
* [Campaign creation](../campaigns/create-campaign.md)

