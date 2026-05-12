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
TQID: https://experienceleague.adobe.com/E2ksPVFZBggv1RgEri7jx30G2oSanpmNs77vH9Yuq78
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: ad78185d-8f79-40ad-9bad-cbde74af74ee
    internal-label: Guardrails and limitations
  - id: b3538224-471e-4c63-a444-9b19d89ae29c
    internal-label: Activities
  - id: baecb07f-ce89-4ebb-9cd9-0f7c053f944f
    internal-label: Journey management
  - id: bb359667-ec7d-4d4b-8663-5850fc219d32
    internal-label: Administration
  - id: d556b755-390a-43f0-be32-a08cf6236126
    internal-label: Configuration
  - id: d998adac-2f81-400b-a669-d07bb196e4eb
    internal-label: Journeys
  - id: dc22c819-3f29-4e91-8b7d-5c6719831141
    internal-label: Content management
  - id: fe338112-e2ce-4876-8989-fc4d497613f1
    internal-label: Email
subfeature_v2:
  - id: af7571a6-3ddb-4c1c-abdf-4d4dde592140
    internal-label: Source connectors
  - id: b32bb433-f8c6-4931-8e52-e657230a3bf2
    internal-label: Audiences
  - id: c6e980f5-2d4f-494f-beef-186b9ecf1513
    internal-label: Fragments
  - id: d2e8a157-b3b0-4143-9ff3-809bf400be56
    internal-label: Sandboxes
  - id: d595a60b-bcf5-4a63-a189-66a0be755cc7
    internal-label: Templates
  - id: fdac7813-bd56-47ae-9f6d-fa94ad1c5dee
    internal-label: Overview
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
  - id: c66ffd68-0f65-42bb-aa23-b4020f12e0bd
    internal-label: Admin
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
level_v2:
  - id: e8ccd51f-da0d-4e3b-939b-e30d5ebb1ea5
    internal-label: Beginner
topic_v2:
  - id: aa2f3246-cb95-4b30-8899-fdf7d73550cc
    internal-label: Reporting
  - id: b5520579-b31f-4df7-9281-f0d9f91e2edc
    internal-label: Customer engagement
  - id: b5ce8718-c3af-4fdb-a1a9-fca32f83a87c
    internal-label: Implementation
  - id: bce87dde-a4ab-44c9-8a18-ad66e4ddb377
    internal-label: Customer experience
  - id: c2be0313-b3ae-45e0-b454-d20bf54b23f2
    internal-label: Measurement
  - id: c7d04a2c-412a-4c9d-9d7a-4456eaa5adeb
    internal-label: Governance
  - id: cdd65e7e-8839-44a2-bc21-0e03623b5dd1
    internal-label: Optimization
  - id: d00e9f03-e50b-4162-b143-0c0817c937c2
    internal-label: Customer journeys
  - id: d095671a-1355-40aa-8b5f-06c33c68080b
    internal-label: Security
  - id: e0eb8757-182f-49f3-94a4-1587d16f5094
    internal-label: Personalization
  - id: e1e0219c-f879-479f-8427-888ed2a6e9c2
    internal-label: Insights
  - id: ebde5b41-29c9-4f5e-9ef6-1197e85409e3
    internal-label: Data management
  - id: eddd9b14-83bd-4ff4-9072-54a4a484abb7
    internal-label: Administration
  - id: f4e6943a-c91a-4134-a2c7-f4f20cfff2f0
    internal-label: Privacy
  - id: fd2e3797-f2ea-4b36-a9af-52acf5e90513
    internal-label: Customer profiles
---
# Understanding Journey Optimizer {#understanding-ajo}

This page explains how Adobe Experience Platform and Journey Optimizer work together, covering the continuous data-to-experience cycle, key functional areas, architecture details, and integration points.

Adobe Journey Optimizer and Adobe Experience Platform work together to enable data-driven personalization at scale. This page explains how these systems operate and how their key functional areas combine to deliver exceptional customer experiences. [Learn about key capabilities](get-started.md) | [Explore key terminology](terminology.md)

## How Journey Optimizer works {#how-it-works}

Without a unified data foundation, brands are forced to rely on multiple channel-specific tools — making it difficult to maintain a consistent view of each customer or act on their behavior in real time. Journey Optimizer solves this by building on Adobe Experience Platform to connect customer data, content creation, and journey orchestration in a single, continuous system. The result is meaningful brand experiences that drive customer loyalty and lifetime value.

Adobe Journey Optimizer operates as a continuous flow where data is collected, analyzed, and applied to create personalized customer journeys.

![Diagram showing Adobe Experience Platform as the foundational data layer, with Journey Optimizer built on top alongside Real-Time CDP, Customer Journey Analytics, and Adobe Mix Modeler, all sharing core services such as Real-Time Customer Profile, data governance, and identity resolution.](assets/ajo-aep-architecture-diagram.png)

### Adobe Experience Platform: the foundation {#aep-foundation}

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

## Architecture details {#architecture-details}

Journey Optimizer is one of four applications natively built on Adobe Experience Platform, alongside Real-Time CDP, Customer Journey Analytics, and Adobe Mix Modeler. It shares AEP's core services — Real-Time Customer Profile, Identity Graph, data governance, and query services — so it accesses a unified customer data foundation without requiring separate integrations. Journey Optimizer can operate as a standalone application or interoperate with other AEP-native applications.

For a deep dive into technical architecture — including integration patterns, prerequisites, and system data flows — see the [Adobe Journey Optimizer Blueprints](https://experienceleague.adobe.com/en/docs/blueprints-learn/architecture/architecture-diagrams/customer-journeys/journey-optimizer/journey-optimizer-overview){target="_blank"}. For implementation considerations, [review guardrails and limitations](guardrails.md).

## Privacy and security {#privacy-security}

Adobe Experience Cloud's privacy and security practices apply to Adobe Journey Optimizer. These measures ensure compliance with privacy regulations like GDPR, enabling you to deliver personalized experiences while maintaining customer trust. [Learn more about privacy in Journey Optimizer](../privacy/get-started-privacy.md)
