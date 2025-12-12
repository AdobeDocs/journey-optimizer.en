---
solution: Journey Optimizer
product: journey optimizer
title: IP warmup deliverability guide
description: Learn about deliverability fundamentals and best practices for IP warmup
feature: IP Warmup Plans
topic: Administration
role: Admin
level: Experienced
keywords: IP, deliverability, reputation, ISP, engagement
exl-id: TBD
---
# IP warmup deliverability guide {#ip-warmup-deliverability-guide}

When launching email campaigns with new IP addresses or domains in Adobe Journey Optimizer, understanding deliverability fundamentals is crucial for building a strong sender reputation. This guide covers the key concepts, preparation steps, and best practices to help you transition from zero reputation to successful inbox placement.

➡️ [Watch this video to learn about IP warmup deliverability fundamentals](#video)

>[!NOTE]
>
>For step-by-step instructions on implementing IP warmup plans in Adobe Journey Optimizer, refer to [Get started with IP warmup plans](ip-warmup-gs.md).

## Why IP and domain reputation matter {#reputation-matters}

Mailbox providers (Gmail, Yahoo, Microsoft, Apple Mail, and others) evaluate every sender based on four key pillars:

* **Complaints**: Did recipients mark your messages as spam?
* **Engagement**: Do recipients open, click, or reply to your emails?
* **Infrastructure**: Is your sending infrastructure authenticated, stable, and trustworthy?
* **Content**: Does your message content appear legitimate and valuable?

IP warmup primarily addresses the first three pillars by gradually demonstrating to mailbox providers that your new infrastructure is legitimate and wanted before you scale to full sending volume.

## Pre-flight checklist {#pre-flight-checklist}

Before you begin warming up your IP addresses, ensure all foundational elements are in place. The table below outlines the essential tasks to complete before starting your IP warmup plan.

| Task | Why it matters | How to accomplish |
|------|----------------|-------------------|
| Reserve fixed IP(s) and delegate subdomains in AJO | All future reputation attaches to these infrastructure elements | Navigate to **[!UICONTROL Administration]** > **[!UICONTROL Channels]** > **[!UICONTROL Email settings]** > **[!UICONTROL Subdomains]**. [Learn more](delegate-subdomain.md) |
| Configure SPF and DKIM | Confirms your sending server is legitimate and authorized | Automatically handled by Adobe after subdomain delegation and channel configuration creation. [Learn more](delegate-subdomain.md) |
| Set up DMARC record | Enables email authentication reporting and future enforcement policies | Automatically handled by Adobe after subdomain delegation and channel configuration creation. [Learn more](dmarc-record.md) |
| Configure seed list monitoring | Detects inbox placement issues early in your warm-up process | Add seed addresses when creating your channel configuration. [Learn more](seed-lists.md) |
| Build Phase 1 high-engagement audience | Boosts early engagement metrics with your most active recipients | Create an audience of less than 5,000 contacts who opened or clicked in the last 30 days |

>[!CAUTION]
>
>Authentication issues (SPF, DKIM, DMARC) cannot be resolved through volume ramping. Ensure these are correctly configured before you begin sending.

## Sample four-week warmup calendar {#warmup-calendar}

This sample calendar provides a progressive volume ramp based on percentage of your ultimate daily volume (UDV). Adjust these numbers to fit your specific sending requirements and work with your deliverability consultant to create a customized plan.

| Days | % of UDV | Target audience | Content recommendations |
|------|----------|-----------------|------------------------|
| 1–3 | 0.5% | Your most engaged recipients | Use short, plain-text format with a clear call-to-action above the fold |
| 4–7 | 1% | Engaged users plus recent buyers | Add a lightweight hero image, limit links to 3 or fewer |
| 8–14 | 5% | Broader active subscriber list | Introduce your standard email template, but avoid heavy promotional content |
| 15–21 | 25% | Active plus lightly-inactive subscribers | Use normal marketing content while monitoring complaint rates closely |
| 22–28 | 50–100% | Full list (respecting suppression lists) | Transition to your steady-state sending cadence |

>[!NOTE]
>
>Adobe Journey Optimizer provides a dedicated [IP warmup plans feature](ip-warmup-gs.md) that automates volume management and simplifies the warmup process without requiring complex journey configurations.

## Using AJO's IP warmup plans feature {#ajo-warmup-feature}

Adobe Journey Optimizer includes a streamlined IP warmup plans feature that eliminates the need for manual volume capping through complex journey setups. This functionality ensures a standardized approach to building sender reputation.

### How it works

1. **Create IP warmup campaigns**: Build one or more campaigns with the **[!UICONTROL IP warmup plan activation]** option enabled. [Learn more](ip-warmup-campaign.md)

1. **Set up your plan**: Access **[!UICONTROL Administration]** > **[!UICONTROL Channels]** > **[!UICONTROL Email settings]** > **[!UICONTROL IP warmup plans]** and upload your phased warmup template prepared with your deliverability consultant. [Learn more](ip-warmup-plan.md)

1. **Execute phases**: Select a campaign for each phase and activate the corresponding runs. The system automatically excludes profiles from previous runs to prevent over-contacting. [Learn more](ip-warmup-execution.md)

1. **Monitor and adjust**: Use the consolidated reporting dashboard to track progress, monitor run statuses, and modify your plan if issues arise. [Learn more](ip-warmup-execution.md#monitor-plan)

## Real-time monitoring and key metrics {#monitoring}

Adobe Journey Optimizer provides built-in reporting capabilities to track your IP warmup performance:

* **Live reports**: Access real-time measurement and visualization of your campaigns from the **[!UICONTROL Last 24hrs]** tab. [Learn more](../reports/live-report.md)

* **Customer Journey Analytics integration**: For deeper insights, leverage Customer Journey Analytics to analyze data from Adobe Experience Platform and create custom visualizations. [Learn more](../reports/report-gs-cja.md)

### Target metrics

Monitor these key performance indicators throughout your warmup:

| Metric | Target threshold | Action if exceeded |
|--------|-----------------|-------------------|
| Complaint rate | ≤ 0.1% | Audit segment and suppress chronic complainers |
| Hard bounce rate | ≤ 2% | Review list quality and hygiene practices |
| Open rate | ≥ 10% | Verify you're targeting engaged audiences |

>[!TIP]
>
>For comprehensive campaign analytics, use the [campaign live report](../reports/campaign-live-report.md#email-live) and [Customer Journey Analytics report](../reports/campaign-global-report-cja-email.md) features.

## Troubleshooting playbook {#troubleshooting}

Use this decision matrix to address common issues during your warmup:

| Symptom | Likely cause | Recommended action |
|---------|--------------|-------------------|
| Yahoo temporary failures (421 errors) | Volume increased too quickly | Pause sending for 24 hours, then restart at the previous tier |
| Open rate below 2% across seed accounts | IP blocklisting | Check [Google Postmaster Tools](https://postmaster.google.com/) and [Microsoft SNDS](https://sendersupport.olc.protection.outlook.com/snds/); open a deliverability ticket if needed |
| Complaint rate exceeds 0.3% | Mis-targeted or stale audience | Audit segment definitions and exclude chronic complainers from your [suppression list](manage-suppression-list.md) |

>[!IMPORTANT]
>
>It's better to slow down your warmup than to attempt to repair a damaged sender reputation later. Always prioritize maintaining healthy metrics over aggressive volume ramping.

## Post-warmup best practices {#post-warmup}

Once you've completed your warmup plan and metrics have stabilized:

* **Maintain consistency**: Keep daily volume increases below 30% week-over-week to preserve your established reputation

* **Monitor continuously**: Schedule quarterly reputation health checks to identify and address issues proactively

* **Respect engagement signals**: Continue to prioritize engaged recipients and implement re-engagement campaigns for inactive subscribers

* **Keep authentication current**: Regularly verify that your SPF, DKIM, and DMARC records remain properly configured

## Key takeaways {#key-takeaways}

* **IP warmup is essential**: Skipping the warmup process costs more time and reputation than the effort required to do it properly

* **Data-driven decisions**: Track complaint, bounce, and engagement rates daily and adjust your strategy before ISPs penalize you

* **Authentication first, volume second**: Resolve all SPF, DKIM, and DMARC issues before beginning to ramp volume

* **Consistency matters**: Mailbox providers favor predictable sending patterns; avoid sudden volume spikes or irregular sending schedules

## How-to video {#video}

Learn about deliverability fundamentals, reputation building, and best practices for IP warmup in Adobe Journey Optimizer.

>[!VIDEO](https://video.tv.adobe.com/v/3457695/?learn=on)

<!--
>[!NOTE]
>
>For more guidance, explore the [Adobe Journey Optimizer Deliverability Guide blog post](https://experienceleaguecommunities.adobe.com/t5/journey-optimizer-blogs/adobe-journey-optimizer-deliverability-guide-from-zero/ba-p/761950).-->

## Related topics {#related-topics}

* [Get started with IP warmup plans](ip-warmup-gs.md)
* [Create IP warmup campaigns](ip-warmup-campaign.md)
* [Create an IP warmup plan](ip-warmup-plan.md)
* [Execute the IP warmup plan](ip-warmup-execution.md)
* [Set up channel configurations](channel-surfaces.md)
* [Delegate subdomains](delegate-subdomain.md)
* [Manage suppression list](manage-suppression-list.md)
* [Deliverability Best Practice Guide](https://experienceleague.adobe.com/docs/deliverability-learn/deliverability-best-practice-guide/introduction.html)

