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

Understanding how customers interact with your communications is key to creating meaningful experiences and driving results. Journey Optimizer provides comprehensive tracking and monitoring capabilities that give you visibility into customer behavior, delivery performance, and system health—all while respecting privacy and maintaining compliance.

>[!BEGINSHADEBOX]

**What you can track in Journey Optimizer:**

📧 **Email interactions** - Opens, clicks, and link performance

🌐 **Web behavior** - Page views, clicks, and engagement patterns  

🛤️ **Journey performance** - Custom metrics, step events, and conversion paths

📊 **Deliverability health** - Bounce rates, spam complaints, and sender reputation

⚙️ **System operations** - Alerts, errors, and custom action performance

>[!ENDSHADEBOX]

## Track customer interactions across channels {#tracking-by-channel}

Journey Optimizer provides channel-specific tracking capabilities that help you understand how customers engage with your communications.

### Email tracking {#email-tracking}

Track email engagement to understand recipient behavior and optimize your messaging strategy:

* **Opens & clicks** - Monitor how recipients interact with your emails to identify high-performing content. [Learn more](../email/message-tracking.md)

* **Link performance** - Track all links in your content, including those in fragments, to see which calls-to-action drive engagement. [Learn more](../email/message-tracking.md#insert-links)

* **Campaign attribution** - Add tracking parameters to URLs to measure effectiveness across your digital ecosystem. [Learn more](../email/url-tracking.md)

* **Mirror pages** - Automatically generate online versions of emails with built-in tracking. [Learn more](../email/message-tracking.md#mirror-page)

### Web tracking {#web-tracking}

Understand how visitors interact with your personalized web experiences:

* **Element clicks** - Track clicks on specific buttons, images, or links to understand user intent and optimize page layouts. [Learn more](../web/monitor-web-experiences.md#use-click-tracking)

* **Performance metrics** - View impressions, click-through rates, and engagement levels to validate your personalization efforts. [Learn more](../web/monitor-web-experiences.md)

### Journey & campaign tracking {#journey-campaign-tracking}

Measure success at the journey and campaign level:

* **Custom success metrics** - Define and track KPIs aligned with your specific business objectives. [Learn more](../building-journeys/success-metrics.md)

* **Journey step events** - Get granular visibility into every action customers take as they move through your journeys. [Learn more](../reports/journey-step-events-overview.md)

* **Custom reporting** - Build tailored reports that answer your unique business questions. [Learn more](../reports/sharing-overview.md)

* **Custom action monitoring** - Track the performance of integrations with external systems. [Learn more](../action/reporting.md)

## Monitor deliverability & system health {#monitoring-capabilities}

Beyond tracking engagement, Journey Optimizer helps you ensure messages reach inboxes and systems perform optimally.

>[!BEGINTABS]

>[!TAB Deliverability]

**Maintain a healthy sender reputation**

* **Suppression list** - Review excluded addresses and understand why they're blocked. [Learn more](../reports/suppression-list.md)

* **Error analysis** - Diagnose delivery failures with detailed error categorization. [Learn more](../configuration/email-error-types.md)

* **Best practices** - Follow DMARC requirements and industry standards to maximize inbox placement. [Learn more](../reports/deliverability.md)

* **Automatic retries** - Recover from temporary failures with intelligent retry logic. [Learn more](../configuration/retries.md)

>[!TAB System monitoring]

**Stay informed about system health**

* **Real-time alerts** - Receive notifications about journey errors, custom action failures, and critical issues. [Learn more](../reports/alerts.md)

* **Audit logs** - Track all actions on resources for compliance and troubleshooting. [Learn more](../privacy/audit-logs.md)

* **Integration health** - Monitor custom action performance and external system connectivity. [Learn more](../action/reporting.md)

>[!TAB Analytics]

**Transform data into insights**

* **Journey analytics** - Understand conversion paths, drop-off points, and timing optimization opportunities. [Learn more](../reports/journey-global-report-cja.md)

* **Campaign performance** - Track results across all channels in a unified view. [Learn more](../reports/campaign-global-report-cja.md)

* **Live monitoring** - See profile flows through journeys in real-time. [Learn more](../reports/live-report.md)

* **Advanced analysis** - Connect with Customer Journey Analytics for attribution modeling and predictive insights. [Learn more](../reports/cja-ajo.md)

>[!ENDTABS]

## Data & privacy foundations {#key-concepts}

Journey Optimizer's tracking capabilities are built on Adobe Experience Platform, providing seamless data integration and privacy-by-design architecture.

### Automatic data integration {#data-collection}

All tracking data flows automatically to Adobe Experience Platform, enabling:

✨ **Cross-platform analysis** - Combine journey data with Adobe Analytics, CRM data, and other sources for complete customer visibility. [Learn more](../data/lookup-aep-data.md)

✨ **Unified customer profiles** - Journey interactions automatically update Real-Time Customer Profiles for better segmentation and personalization. [Learn more](../audience/get-started-profiles.md)

✨ **Attribution modeling** - Connect touchpoints to business outcomes with advanced Customer Journey Analytics capabilities. [Learn more](../reports/cja-ajo.md)

### Privacy-first tracking {#privacy-compliance}

>[!IMPORTANT]
>
>Journey Optimizer automatically enforces privacy policies and respects customer choices throughout all tracking activities.

**Consent management** - The system honors customer consent preferences, stopping data collection when consent is withdrawn while maintaining essential transactional communications. [Learn more](../action/consent.md)

**Data governance** - Apply usage labels that automatically restrict how tracking data can be used, ensuring compliance with regulations like GDPR and CCPA. [Learn more](../action/action-privacy.md)

**Privacy requests** - Handle data subject requests efficiently through integration with Adobe Experience Platform Privacy Service. [Learn more](../privacy/requests.md)

## Getting started with tracking {#implement-tracking}

Ready to start tracking? Follow these steps to implement tracking in your journeys and campaigns:

>[!BEGINSHADEBOX]

**Your tracking implementation roadmap**

**1. Enable channel tracking** 

Turn on tracking when creating emails, web experiences, or other messages. Each channel has specific tracking options you can configure. [Learn more](#tracking-by-channel)

**2. Configure URL parameters** 

Set up tracking parameters at the channel configuration level to automatically append tracking information to all URLs. [Learn more](../email/url-tracking.md)

**3. Define success metrics** 

Choose the KPIs that matter for your business and configure Journey Optimizer to track them. [Learn more](../building-journeys/success-metrics.md)

**4. Access reports** 

Use Journey Optimizer's built-in reports to monitor performance and understand customer behavior. [Learn more](../reports/gs-reports.md)

**5. Integrate advanced analytics** 

Connect with Customer Journey Analytics for sophisticated analysis and attribution modeling. [Learn more](../reports/cja-ajo.md)

>[!ENDSHADEBOX]

## Next steps {#next-steps}

<table style="table-layout:fixed">
<tr style="border: 0;">
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
</tr>
</table>

