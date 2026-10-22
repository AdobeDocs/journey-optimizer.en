---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains what campaigns are, compares the three campaign types (Orchestrated campaigns, Action campaigns, API triggered campaigns), lists the prerequisites, and outlines the six-step campaign creation workflow.

**Intents:**

* Understand what campaigns are and how they differ from journeys
* Choose between Orchestrated campaigns, Action campaigns (Scheduled), and API-triggered campaigns for a use case
* Know the prerequisites before working with campaigns: audiences, channel configurations, and permissions
* Know which permissions apply to each campaign type
* Follow the six-step campaign creation workflow and find the type-specific guide for each step
* Find the capabilities to explore next, such as scheduling, rate control, audience targeting, approval workflows, quiet hours, and optimization

**Glossary:**

* **Campaign**: A coordinated marketing action that delivers content to a specific audience across one or more channels; actions are performed simultaneously, either immediately or on a defined schedule *(product-specific)*
* **Action campaign** (also known as **Scheduled campaign**): Campaign type for straightforward, one-off or recurring batch communications that run at a specific time *(product-specific)*
* **API-triggered campaign**: Campaign type that is activated through API calls, enabling automated messaging directly from external systems; it supports personalization using both profile attributes and real-time context data from the API payload *(product-specific)*
* **Orchestrated campaign**: Campaign type that provides a visual, drag-and-drop canvas to design and automate sophisticated marketing workflows, from audience segmentation to personalized message delivery across channels *(product-specific)*
* **Marketing** and **Transactional**: The two categories of Action campaigns and of API-triggered campaigns
* **Engageable Profiles**: License metric of the organization to which every profile engaged by a campaign counts *(product-specific)*
* **Channel configurations** (presets): Configurations for the channels used by campaigns *(product-specific)*

**Guardrails:**

* Every profile engaged by a campaign counts toward the organization's **Engageable Profiles** license metric (rolling 12-month window, counted once per sandbox). Activating a campaign to a large or new audience can cause a significant increase in this count.
* For Action campaigns, Marketing requires recipients to be opted in, and Transactional does not require opt-in.

**Prerequisites and permissions:**

* **Audiences**: available in Adobe Experience Platform before creating campaigns.
* **Channel configurations**: created and available for the channels you want to use.
* **Permissions**: appropriate permissions based on the campaign type. Contact your administrator if you cannot access campaign functionalities.
    * Action campaigns and API triggered campaigns: Campaign administrator, Campaign approver, Campaign manager, Campaign viewer.
    * Orchestrated campaigns: Orchestrated Campaign Administrator, Orchestrated Campaign Approver, Orchestrated Campaign Manager, Orchestrated Campaign Viewer.

**Applicability:**

* Scheduling & timing, Approval workflows, and Quiet hours: labeled on the page as Action & API-triggered campaigns.
* In the campaign properties step, configure the schedule for Action campaigns, or the API details for API-triggered campaigns.
* In the activate step, API activation (use the activation endpoint) is for API-triggered campaigns.

**Terminology:**

* Canonical name: Campaigns — variants: Adobe Journey Optimizer campaigns
* Canonical name: Action campaigns — variants: Scheduled campaigns, Action campaigns (Scheduled)
* Canonical name: API-triggered campaigns — variants: API triggered campaigns
* Acronym: CJA — Customer Journey Analytics
* Do not confuse: "campaigns" (actions are performed simultaneously, either immediately or on a defined schedule) ≠ "journeys" (actions execute sequentially)

**FAQ:**

* **Q: What is a campaign?** — Campaigns are coordinated marketing actions that deliver content to a specific audience across one or more channels. Unlike journeys where actions execute sequentially, campaigns perform actions simultaneously, either immediately or on a defined schedule.
* **Q: Which campaign types are available?** — Three: Orchestrated campaigns (complex, multi-step marketing workflows), Action campaigns, also known as Scheduled campaigns (simple, scheduled batch communications), and API triggered campaigns (real-time, event-driven messaging with external systems).
* **Q: What do I need before creating a campaign?** — Audiences available in Adobe Experience Platform, channel configurations (presets) for the channels you want to use, and the appropriate permissions for the campaign type.
* **Q: Which permissions do I need?** — For Action campaigns and API triggered campaigns: Campaign administrator, Campaign approver, Campaign manager or Campaign viewer. For Orchestrated campaigns: Orchestrated Campaign Administrator, Orchestrated Campaign Approver, Orchestrated Campaign Manager or Orchestrated Campaign Viewer.
* **Q: Which campaign type should I start with if I am not sure?** — Start with Action campaigns for scheduled batch communications or API-triggered campaigns for real-time messaging; these cover most common use cases.
* **Q: What are the steps of the campaign creation workflow?** — Plan your campaign, configure campaign properties, design your content, review and test, activate your campaign, then monitor and analyze.

**Examples:**

* Action campaigns: monthly newsletters to customer segments, time-sensitive promotional announcements, seasonal marketing campaigns, product launch communications, and service disruption notifications.
* API-triggered campaigns: password reset confirmations, cart abandonment recovery, order confirmations and shipping updates, account activity notifications, and real-time personalized recommendations.
* Orchestrated campaigns: multi-step customer engagement programs, complex segmentation and targeting strategies, cross-channel campaign orchestration, brand-initiated marketing at scale, and advanced workflow automation with multiple decision points.
* Action campaign Transactional category: disruptions, emergencies, cancellations. API-triggered campaign Transactional category: messages following individual actions (password resets, cart purchases, and so on).

**Best practices:**

* Always review your campaign before activation: preview content with test profiles, check targeting, verify schedule and activation settings, request approval if using the approval workflow, and test deliverability with seed lists.
* If you are not sure which campaign type to choose, start with Action campaigns or API-triggered campaigns.

**Related pages:**

* Create your first Action campaign: Create your first campaign (campaigns/create-campaign.md)
* Orchestrated campaigns: Learn about Orchestrated campaigns (orchestrated/gs-orchestrated-campaigns.md)
* API-triggered campaigns: Learn about API-triggered campaigns (campaigns/api-triggered-campaigns.md)
* Audiences: Get started with audiences (audience/about-audiences.md)
* Engageable Profiles count: Monitor your Engageable Profiles count (audience/license-usage.md)
* Channel configurations: Set up channel configurations (configuration/channel-surfaces.md)
* Supported channels by campaign type: See supported channels by campaign type (channels/gs-channels.md#channels)
* Built-in roles: Learn about built-in roles (administration/ootb-product-profiles.md)
* Action campaign properties: Action campaign properties (campaigns/campaign-properties.md)
* API-triggered campaign properties: API-triggered campaign properties (campaigns/api-triggered-campaign-properties.md)
* Orchestrated campaign setup, content, review, activation and analytics: Orchestrated campaign setup (orchestrated/create-orchestrated-campaign.md)
* Action campaign content: Action campaign content (campaigns/campaign-content.md)
* API-triggered campaign content: API-triggered campaign content (campaigns/api-triggered-campaign-content.md)
* Review and activate Action campaigns: Review Action campaigns (campaigns/review-activate-campaign.md)
* Review and activate API-triggered campaigns: Review API-triggered campaigns (campaigns/review-activate-api-triggered-campaign.md)
* Action campaign reports: Action campaign reports (reports/campaign-global-report-cja.md)
* API-triggered campaign monitoring: API-triggered campaign monitoring (campaigns/api-triggered-campaigns.md#monitor)
* Send using waves: send using waves (delivery/send-using-waves.md)
* Scheduling: Learn about scheduling (campaigns/campaign-schedule.md)
* Audience targeting: Select campaign audience (campaigns/campaign-audience.md)
* Approval workflows: Review and activate (campaigns/review-activate-campaign.md)
* Quiet hours: Configure quiet hours (conflict-prioritization/quiet-hours.md)
* Optimization with targeting rules and content experiments: Optimize campaigns (content-management/gs-message-optimization.md)

+++

<!-- ai-section-version: 1 | source-hash: 2e2f590e -->
