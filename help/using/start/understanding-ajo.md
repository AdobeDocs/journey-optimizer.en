---
solution: Journey Optimizer
product: journey optimizer
title: Understanding Journey Optimizer
description: Learn how Adobe Journey Optimizer works with Adobe Experience Platform to deliver personalized customer experiences
feature: Get Started
topic: Content Management
role: Admin, Developer, User
level: Beginner
keywords: journey optimizer, how it works, architecture, experience platform, functional areas
exl-id: 9df179a0-a5f6-4dbd-a9db-a103731b1854
---
# Understanding Journey Optimizer {#understanding-ajo}

This page explains how Adobe Experience Platform and Journey Optimizer work together, covering the continuous data-to-experience cycle, key functional areas, architecture details, and integration points.

Adobe Journey Optimizer and Adobe Experience Platform work together to enable data-driven personalization at scale. This page explains how these systems operate and how their key functional areas combine to deliver exceptional customer experiences. [Learn about key capabilities](get-started.md) | [Explore key terminology](terminology.md)

## How Journey Optimizer Works {#how-it-works}

Without a unified data foundation, brands are forced to rely on multiple channel-specific tools — making it difficult to maintain a consistent view of each customer or act on their behavior in real time. Journey Optimizer solves this by building on Adobe Experience Platform to connect customer data, content creation, and journey orchestration in a single, continuous system. The result is meaningful brand experiences that drive customer loyalty and lifetime value.

Adobe Journey Optimizer operates as a continuous flow where data is collected, analyzed, and applied to create personalized customer journeys.

![Diagram showing Adobe Experience Platform as the foundational data layer, with Journey Optimizer built on top alongside Real-Time CDP, Customer Journey Analytics, and Adobe Mix Modeler, all sharing core services such as Real-Time Customer Profile, data governance, and identity resolution.](assets/ajo-aep-architecture-diagram.png)

### Adobe Experience Platform: The Foundation {#aep-foundation}

Adobe Experience Platform serves as the backbone, enabling brands to centralize customer data and activate it for personalized experiences:

* **Data Platform** - Central hub for collecting, managing, and structuring customer data to ensure consistency across systems. [Learn about schemas and datasets](../data/get-started-schemas.md)
* **Data Ingestion (Sources)** - Import data from CRM platforms, websites, mobile apps, and cloud storage using pre-built connectors. [Explore data sources](get-started-sources.md)
* **Real-time Customer Profile** - Creates unified profiles by merging data from multiple sources (email interactions, in-store purchases, web behavior). [Learn about profiles](../audience/get-started-profiles.md)
* **Governance Layer** - Governs data access, privacy compliance, and security while adhering to regulations. [View privacy documentation](../privacy/get-started-privacy.md)

### Adobe Journey Optimizer: the orchestration engine {#ajo-orchestration}

Adobe Journey Optimizer applies the data and insights from Adobe Experience Platform to deliver intelligent, personalized customer experiences:

* **Customer Understanding** - Real-time Customer Profiles enable segmentation into audiences for targeted messaging. [Create audiences](../audience/about-audiences.md)
* **Content & Offers** - A built-in visual designer, reusable templates, and a centralized asset library let teams author and personalize messages for any channel — without leaving the platform. Dynamic personalization adapts content based on customer attributes, behavior, and context. Real-time decisioning logic then selects the best offer for each individual. [Design content](../../rp_landing_pages/content-management-landing-page.md) | [Manage assets](../integrations/assets.md) | [Manage offers](../offers/get-started/starting-offer-decisioning.md)
* **Journey & Campaign Management** - Automates sequences of interactions (journeys) or schedules one-time targeted messages (campaigns). [Build journeys](../building-journeys/journey-gs.md) | [Create campaigns](../campaigns/get-started-with-campaigns.md)
* **Delivery (Connections)** - Delivers messages through channels like email, SMS, push notifications, and direct mail; exports data to external systems. [Configure channels](../configuration/get-started-configuration.md)
* **Measurement & Analysis** - Tracks customer engagement and campaign performance with reports for continuous improvement. [View reports](../reports/campaign-global-report-cja.md)

### The continuous optimization cycle {#optimization-cycle}

This ecosystem operates as a continuous optimization cycle. Data drives customer understanding, which informs personalized content and decisions. These are orchestrated into journeys, delivered across channels, measured for effectiveness, and refined over time.

![Diagram illustrating the continuous optimization cycle in Journey Optimizer: data ingestion feeds customer profiles, which inform content and offer decisions, orchestrated into journeys, delivered across channels, measured for performance, and refined over time.](../assets/do-not-localize/get-started-flow.png)

## Key functional areas {#functional-areas}

Journey Optimizer includes seven key functional areas that work together seamlessly:

| Functional Area | Purpose | Key Activities |
|-----------------|---------|----------------|
| **Data Management** | Organize customer data | Define schemas, create datasets, import data from various systems. [Learn more](../data/get-started-schemas.md) |
| **Customer Management** | Understand who your customers are | Build unified profiles, resolve identities, create audiences. [Learn more](../audience/get-started-profiles.md) |
| **Content Management** | Create personalized messages | Design emails, manage assets, build templates and fragments, personalize content. [Learn more](../../rp_landing_pages/content-management-landing-page.md) |
| **Decision Management** | Select the best offer in real time | Manage offer library, define rules, apply constraints, establish ranking logic. [Learn more](../offers/get-started/starting-offer-decisioning.md) |
| **Journey Management** | Design automated customer experiences | Create journeys with visual designer, set triggers, add conditions and wait steps. [Learn more](../building-journeys/journey-gs.md) |
| **Connections** | Connect data sources and channels | Configure source connectors, set up channels, connect to external platforms. [Learn more](../configuration/get-started-configuration.md) |
| **Administration & Privacy** | Control setup and compliance | Manage users, configure sandboxes, set up channels, handle privacy requests. [Learn more](../administration/permissions.md) |

### How these areas work together {#working-together}

These functional areas operate in a continuous cycle:

1. **Data Ingestion** - Data flows into Adobe Experience Platform, structured by Data Management
2. **Customer Understanding** - Real-time Customer Profiles unify data; Customer Management creates audiences  
3. **Content & Offer Strategy** - Content Management creates messages; Decision Management defines offer logic
4. **Orchestration** - Journey Management maps interactions across channels using customer data, content, and decisions
5. **Delivery** - Connections facilitate message delivery via channels or share data with external systems
6. **Measurement** - Performance data feeds insights back to refine audiences, content, decisions, and journeys
7. **Governance** - Administration and Privacy controls ensure compliance throughout

## Architecture Details {#architecture-details}

Journey Optimizer is one of four applications natively built on Adobe Experience Platform, alongside Real-Time CDP, Customer Journey Analytics, and Adobe Mix Modeler. It shares AEP's core services — Real-Time Customer Profile, Identity Graph, data governance, and query services — so it accesses a unified customer data foundation without requiring separate integrations. Journey Optimizer can operate as a standalone application or interoperate with other AEP-native applications.

For a deep dive into technical architecture — including integration patterns, prerequisites, and system data flows — see the [Adobe Journey Optimizer Blueprints](https://experienceleague.adobe.com/en/docs/blueprints-learn/architecture/architecture-diagrams/customer-journeys/journey-optimizer/journey-optimizer-overview){target="_blank"}. For implementation considerations, [review guardrails and limitations](guardrails.md).

## Privacy and Security {#privacy-security}

Adobe Experience Cloud's privacy and security practices apply to Adobe Journey Optimizer. These measures ensure compliance with privacy regulations like GDPR, enabling you to deliver personalized experiences while maintaining customer trust. [Learn more about privacy in Journey Optimizer](../privacy/get-started-privacy.md)
