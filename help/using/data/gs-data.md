---
solution: Journey Optimizer
product: journey optimizer
title: Get started with data management in Journey Optimizer
description: Learn how data flows into and out of Adobe Journey Optimizer, including key concepts, setup steps, and guardrails.
feature: Data Management
role: Developer, Admin, User
level: Beginner, Intermediate
exl-id: 25519acb-a017-446a-992b-653d3a8a3d96
---

# Get started with data management {#about-data}

Data is the foundation of every journey, decision, and message you deliver with [!DNL Adobe Journey Optimizer].

This page gives you a practical starting point to understand:

* The core data building blocks used by Journey Optimizer (schemas, datasets, identities, profiles)
* How Journey Optimizer uses Adobe Experience Platform data
* Which data setup steps your team must complete before building journeys and campaigns
* Where to go next for detailed configuration and best practices

Use this guide together with your data engineers, administrators, and marketers so everyone shares a common picture of how data flows into and out of Journey Optimizer.

>[!TIP]
>New to Journey Optimizer? Start with the [Get started guide](../start/get-started.md) to understand the overall product, or watch the [Set up data overview tutorial](https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/tutorials/data-management/set-up-data-overview){target="_blank"} for a practical, beginner-friendly introduction to data setup in Journey Optimizer.

## How Journey Optimizer uses Adobe Experience Platform data {#aep-data}

[!DNL Adobe Journey Optimizer] is built on [!DNL Adobe Experience Platform]. It does not maintain a separate, isolated data store. Instead, it uses the same data foundation as other Experience Cloud applications.

Schemas and datasets live in Adobe Experience Platform. Identities and the [Real-Time Customer Profile](../audience/get-started-profiles.md) are managed by Identity Service and Profile Service. Journey Optimizer reads profile and event data from Adobe Experience Platform to evaluate journey conditions, personalize messages, and select offers. It writes interaction data — such as send, open, click, and bounce events, and journey step events — back into Experience Platform datasets. It can also look up additional datasets at runtime without copying that data into the profile.

>[!TIP]
>Think of Adobe Experience Platform as your central data layer, and Journey Optimizer as an application that orchestrates journeys and messages using that shared data foundation.

## Key data concepts in Journey Optimizer {#key-concepts}

When you work with data in Journey Optimizer, you will encounter several related concepts. The table below gives you a quick overview; the sections that follow explain each concept in more detail.

| Concept | What it is | Primary use in Journey Optimizer |
|---|---|---|
| XDM schema | Rules that represent, validate, and format your data (built from a class + field groups) | Model profile attributes and behavioral events |
| Dataset | Storage table for data conforming to a schema | Hold profile, event, and system-generated data |
| Source connector | Streams or batches data from external systems into AEP | Ingest CRM, analytics, and web data |
| Data source | Exposes AEP or external fields inside journeys | Power journey conditions and message personalization |
| Identity | Identifier that uniquely represents an individual customer | Stitch profiles across channels |
| Lookup dataset | Runtime reference to AEP data without profile storage | Enrich messages with live reference data |

### Schema (XDM schema) {#schema}

A schema is a set of rules that represent, validate, and format your data. It is comprised of a **class** (which defines the base behavior: record or time-series) and optional **field groups** (which add specific fields). Schemas are defined using Experience Data Model (XDM) standards and live in Adobe Experience Platform.

XDM exists to solve a real problem: the same concept — a customer, a purchase, a product — is named and structured differently across source systems. XDM provides a shared language that unifies these concepts under a single definition, regardless of where the data originates. This is what allows Journey Optimizer to work consistently with data from your CRM, your website, your mobile app, and your data warehouse at the same time.

In Journey Optimizer, you typically work with **XDM Individual Profile** schemas for customer attributes (name, preferences, consent) and **XDM ExperienceEvent** schemas for behavioral events (purchases, page views, sign-ups).

➡️ [Learn more about schemas](get-started-schemas.md)

### Dataset {#dataset}

A dataset is a storage and management construct for data that conforms to a schema — think of it as a table with a defined set of columns and rows. All data used by Journey Optimizer is stored in Adobe Experience Platform datasets. These can be profile datasets (contributing to Real-Time Customer Profile), event datasets (storing behavioral data for journeys and analysis), or system datasets automatically created by Journey Optimizer for tracking, feedback, and journey step events.

➡️ [Learn more about datasets](get-started-datasets.md)

### Source connector {#source-connector}

A source connector (also known as a **source**) helps you ingest data from multiple systems — such as Adobe Analytics, Adobe Experience Platform Web SDK, cloud storage (S3, Azure Blob), or CRM databases — into Adobe Experience Platform. Beyond raw ingestion, connectors enable the structuring, labeling, and enhancement of data using Experience Platform services, including field mapping to your XDM schemas and data governance labeling.

➡️ [Learn more about source connectors](../start/get-started-sources.md)

### Data source (Journey Optimizer) {#data-source}

>[!NOTE]
>The AEP Glossary defines "data source" generically as the origin of data (a CRM, mobile app, etc.). In Journey Optimizer, **data source** has a specific meaning: a UI configuration that controls which fields are exposed inside journeys and messages.

A data source in Journey Optimizer defines which fields from Adobe Experience Platform (or external APIs) are exposed inside journeys and messages. Configured in the Journey Optimizer UI, data sources typically include the built-in Adobe Experience Platform data source (exposing Real-Time Customer Profile attributes and events) and optional external or custom data sources called at journey runtime for additional enrichment. They are used for journey conditions, custom actions, and message personalization.

➡️ [Learn more about data sources](../datasource/about-data-sources.md)

### Identity and Real-Time Customer Profile {#identity}

An identity is an identifier that uniquely represents an individual customer, such as a cookie ID, device ID, email address, or CRM ID. Identities are organized into namespaces (Email, ECID, CRMID), and multiple identities for the same person are stitched into a unified identity graph. Real-Time Customer Profile uses that graph to maintain a holistic view of each individual customer by combining data from multiple channels — including online, offline, CRM, and third-party sources.

A key concept for beginners is the **profile fragment** model. Each time a customer interacts with your brand on a specific device or channel — your website, mobile app, a store — that interaction is recorded as a profile fragment: a partial view of that customer based on that specific touchpoint. Real-Time Customer Profile continuously stitches these fragments together based on shared identity values, building a complete, up-to-date profile. Journey Optimizer reads from this assembled profile to evaluate conditions, select offers, and personalize messages in real time.

➡️ [Learn more about identities in Journey Optimizer](../audience/get-started-identity.md)

### Lookup dataset {#lookup-dataset}

A lookup dataset lets Journey Optimizer retrieve reference or transactional data at runtime from an Adobe Experience Platform dataset, without storing that data on the Real-Time Customer Profile. This is useful for frequently changing reference data (prices, inventory, store hours) or transactional data that is needed at message time but does not belong on the profile. Journey Optimizer performs the lookup during journey or message execution based on a key such as a product ID.

➡️ [Learn more about lookup datasets](lookup-aep-data.md)

## Data readiness checklist {#checklist}

Before marketers start building journeys and campaigns, your organization should complete a set of data readiness steps. This ensures that Journey Optimizer can use the right data, at the right time, and in a compliant way.

>[!NOTE]
>The steps below involve multiple roles: data engineers, administrators, and marketers. Use this checklist as a shared plan to prepare your environment.

### 1. Define your identity strategy {#identity-strategy}

Choose a primary identity for your customers (such as ECID, email, or CRMID) and configure the corresponding namespaces in Adobe Experience Platform Identity Service. Make sure identity fields are present in your profile-enabled schemas and validate that profiles are correctly stitched into the identity graph.

➡️ [Learn more about identities in Journey Optimizer](../audience/get-started-identity.md)

### 2. Design schemas for profile and event data {#design-schemas}

Create **XDM Individual Profile** schemas to capture customer attributes such as name and contact information, preferences and interests, and lifecycle stage or consent state. Create **XDM ExperienceEvent** schemas to capture behavioral and transactional data such as web and app events, purchases, and offline interactions. Mark the correct fields as identities and profile attributes where appropriate.

➡️ [Learn more about schemas](get-started-schemas.md)

### 3. Create profile-enabled datasets {#create-datasets}

In Adobe Experience Platform, create datasets based on your XDM schemas and enable Profile on any dataset that should contribute to Real-Time Customer Profile. Confirm that system-generated datasets created by Journey Optimizer are visible in the Datasets workspace.

➡️ [Learn more about datasets](get-started-datasets.md)

### 4. Ingest data from your sources {#ingest-data}

Configure source connectors for your enterprise systems — such as Adobe Analytics, Adobe Experience Platform Web SDK, or your CRM and POS platforms — and map incoming fields to your XDM schemas. Validate that data lands in the correct datasets and appears in Real-Time Customer Profile where expected.

➡️ [Learn more about source connectors](../start/get-started-sources.md)

➡️ [Tutorial: Create datasets and ingest data](https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/tutorials/data-management/create-datasets-and-ingest-data){target="_blank"}

### 5. Configure data sources in Journey Optimizer {#configure-data-sources}

In the Journey Optimizer UI:

1. Open the **[!UICONTROL Configurations]** area.
1. Configure the built-in [Adobe Experience Platform data source](../datasource/adobe-experience-platform-data-source.md).
1. Optionally configure [external or custom data sources](../datasource/external-data-sources.md).
1. Select which fields should be available for journey conditions, message personalization, and decisioning.

➡️ [Learn more about data source configuration](../datasource/about-data-sources.md)

### 6. Verify tracking, feedback, and journey datasets {#verify-datasets}

Confirm that Journey Optimizer system-generated datasets are available in the Datasets workspace. Run test journeys and campaigns, then use Query Editor to verify that send, open, click, and bounce events are recorded and that journey step events and states are captured correctly. Use these datasets for ongoing monitoring, troubleshooting, and journey optimization.

➡️ [Learn more about queries in Journey Optimizer](get-started-queries.md)

## Guardrails and data design considerations {#guardrails}

Some product guardrails and limitations can influence how you design your data model and journeys. Review these early to avoid rework later.

>[!IMPORTANT]
>Always refer to the latest product documentation for guardrails and limitations. The summaries below highlight key items but may evolve over time.

### Journey Optimizer system datasets and TTL {#datasets-ttl}

Journey Optimizer creates several system-generated datasets for tracking, feedback, and journey step events. As of February 2025, a time-to-live (TTL) guardrail is being rolled out to some of these datasets, which may affect how long data is retained for analysis and troubleshooting.

➡️ [Learn more about datasets](get-started-datasets.md)

### Streaming segmentation and Journey Optimizer events {#streaming-segmentation}

As of November 1st, 2024, streaming segmentation no longer supports send and open events from Journey Optimizer tracking and feedback datasets. For use cases such as frequency capping and fatigue management, use [Business Rules](../conflict-prioritization/rule-sets.md) instead of streaming segments based on send/open events.

➡️ [Learn more about datasets](get-started-datasets.md)

### Dataset lookup and decisioning {#lookup-guardrails}

Dataset lookup is ideal for frequently changing attributes (inventory, pricing, weather) or data that does not need to be stored on the Real-Time Customer Profile. Review product-specific guardrails such as dataset size limits and query caps in the relevant documentation before designing your lookup strategy.

➡️ [Learn more about lookup datasets](lookup-aep-data.md)

## Example: preparing data for a welcome journey {#example}

The following example shows how the concepts on this page work together in a simple scenario.

1. A data engineer creates an XDM Individual Profile schema for customer attributes (name, email, loyalty tier, consent) and an XDM ExperienceEvent schema for web sign-up events.
1. Profile-enabled datasets are created for each schema: one for CRM attributes and one for sign-up events.
1. Web and mobile teams stream sign-up events via Adobe Experience Platform Web SDK; CRM data is ingested via a source connector.
1. An administrator configures the Experience Platform data source in Journey Optimizer and exposes fields such as `profile.person.name.firstName`, `profile.personalEmail.address`, and `profile.loyaltyTier`.
1. A marketer creates a welcome journey that listens for a sign-up event and uses those profile attributes to personalize the welcome email. Journey Optimizer writes send and open events to tracking datasets and logs journey progress in journey step event datasets.
1. A developer uses Query Editor to verify that events are flowing correctly and analyzes performance (opens, clicks, time-to-send). The team adjusts the journey and content based on these insights.

This flow illustrates how schemas, datasets, sources, data sources, and queries work together in a complete, beginner-friendly use case.

>[!MORELIKETHIS]
>
>* [Get started with schemas](get-started-schemas.md)
>* [Work with datasets](get-started-datasets.md)
>* [Configure data sources](../datasource/about-data-sources.md)
>* [Use Adobe Experience Platform data (lookup)](lookup-aep-data.md)
>* [Get started with queries](get-started-queries.md)
>* [Get started with profiles](../audience/get-started-profiles.md)
>* [Set up data overview tutorial](https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/tutorials/data-management/set-up-data-overview){target="_blank"}
>* [Create datasets and ingest data tutorial](https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/tutorials/data-management/create-datasets-and-ingest-data){target="_blank"}
