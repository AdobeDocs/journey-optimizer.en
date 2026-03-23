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

At a high level:

* Schemas (your data model) and datasets (your storage tables) live in Adobe Experience Platform
* Identities and the [Real-Time Customer Profile](../audience/get-started-profiles.md) are managed by Identity Service and Profile Service in Adobe Experience Platform
* Journey Optimizer:
  * Reads profile and event data from Adobe Experience Platform for:
    * Journey conditions and transitions
    * Personalization in messages
    * Decisioning and offer selection
  * Writes interaction and orchestration data back into Experience Platform datasets, such as:
    * Tracking and feedback data (sends, opens, clicks, bounces)
    * Journey step events and lifecycle information
  * Can look up additional datasets at runtime via dataset lookup, without copying all of that data into the Real-Time Customer Profile

>[!TIP]
>Think of Adobe Experience Platform as your central data layer, and Journey Optimizer as an application that orchestrates journeys and messages using that shared data foundation.

## Key data concepts in Journey Optimizer {#key-concepts}

When you work with data in Journey Optimizer, you will encounter several related concepts. Understanding how they fit together is critical to a successful implementation.

### Schema (XDM schema) {#schema}

A schema defines the shape and meaning of your data: which fields exist, their data types, and how they relate to each other.

* Schemas are defined using Experience Data Model (XDM) standards
* Schemas live and are managed in Adobe Experience Platform
* Typical schema types used with Journey Optimizer:
  * **XDM Individual Profile** – Customer attributes (for example, name, preferences, consent)
  * **XDM ExperienceEvent** – Behavioral and transactional events (for example, purchases, page views, sign-ups)

[Learn more about schemas](get-started-schemas.md)

### Dataset {#dataset}

A dataset is a storage and management construct for data that conforms to a schema. Think of it as a table with a defined set of columns and rows.

* All data used by Journey Optimizer is stored in Adobe Experience Platform datasets
* Datasets can be:
  * **Profile datasets** – Contribute to Real-Time Customer Profile when profile is enabled
  * **Event datasets** – Store behavioral events used for journeys, segmentation, and analysis
  * **System datasets** – Automatically created by Journey Optimizer for tracking, feedback, and journey step events

[Learn more about datasets](get-started-datasets.md)

[Tutorial: Create datasets and ingest data](https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/tutorials/data-management/create-datasets-and-ingest-data){target="_blank"}

### Source connector {#source-connector}

A source connector streams or batches data from external systems into Adobe Experience Platform.

Examples:

* Adobe Analytics
* Adobe Experience Platform Web SDK
* Cloud storage (for example, S3, Azure Blob)
* CRM or marketing databases

Source connectors handle:

* Authentication and connection to the external system
* Mapping incoming fields to your XDM schemas
* Writing data into the correct datasets in Adobe Experience Platform

[Learn more about source connectors](../start/get-started-sources.md)

### Data source (Journey Optimizer) {#data-source}

A data source in Journey Optimizer defines which fields from Adobe Experience Platform (or external APIs) are exposed inside journeys and messages.

* Configured in the Journey Optimizer UI
* Typically includes:
  * The Adobe Experience Platform data source, which exposes Real-Time Customer Profile attributes and events
  * Optional external or custom data sources that are called at journey runtime for additional enrichment
* Used for:
  * Journey conditions
  * Custom actions and enrichments
  * Personalization in messages

[Learn more about data sources](../datasource/about-data-sources.md)

### Identity and Real-Time Customer Profile {#identity}

An identity is a value that uniquely identifies an entity, such as a person, device, or browser (for example, an email address or CRM ID).

* Identities are organized into identity namespaces (for example, Email, ECID, CRMID)
* Multiple identities for the same person are stitched into a unified identity graph
* Real-Time Customer Profile uses identity stitching to maintain an up-to-date, person-centric view of each customer across channels

[Learn more about identities in Journey Optimizer](../audience/get-started-identity.md)

### Lookup dataset {#lookup-dataset}

A lookup dataset lets Journey Optimizer retrieve reference or transactional data at runtime from an Adobe Experience Platform dataset, without storing that data on the Real-Time Customer Profile.

* Useful for:
  * Frequently changing reference data (for example, prices, inventory, store hours)
  * Transactional data that does not need to be stored in the profile, but is needed at message time
* Journey Optimizer performs a dataset lookup during the journey or message execution, based on a key (for example, product ID)

[Learn more about lookup datasets](lookup-aep-data.md)

## Data readiness checklist {#checklist}

Before marketers start building journeys and campaigns, your organization should complete a set of data readiness steps. This ensures that Journey Optimizer can use the right data, at the right time, and in a compliant way.

>[!NOTE]
>The steps below involve multiple roles: data engineers, administrators, and marketers. Use this checklist as a shared plan to prepare your environment.

### 1. Define your identity strategy {#identity-strategy}

* Choose the primary identity for your customers (for example, ECID, email, CRMID)
* Configure identity namespaces in Adobe Experience Platform Identity Service
* Make sure your identity fields are present in your profile-enabled schemas
* Validate that identities are correctly stitched into identity graphs

[Learn more about identities in Journey Optimizer](../audience/get-started-identity.md)

### 2. Design schemas for profile and event data {#design-schemas}

* Create XDM Individual Profile schemas for customer attributes such as:
  * Name and contact information
  * Preferences and interests
  * Lifecycle stage, loyalty tier, consent state
* Create XDM ExperienceEvent schemas for behavioral and transactional data such as:
  * Web and app events (for example, page views, sign-ups)
  * Purchases and transaction details
  * Call center or offline interactions
* Mark the correct fields as identities and profile attributes where appropriate

[Learn more about schemas](get-started-schemas.md)

### 3. Create profile-enabled datasets {#create-datasets}

* In Adobe Experience Platform, create datasets based on your XDM schemas
* Enable Profile on the datasets that should contribute to Real-Time Customer Profile
* Ensure that system-generated datasets created by Journey Optimizer are visible as needed

[Learn more about datasets](get-started-datasets.md)

### 4. Ingest data from your sources {#ingest-data}

* Configure source connectors for systems such as:
  * Adobe Analytics
  * Adobe Experience Platform Web SDK
  * CRM, POS, and other enterprise systems
* Map incoming fields to your XDM schemas
* Validate that data lands in the correct datasets and appears in Real-Time Customer Profile where expected

[Learn more about source connectors](../start/get-started-sources.md)

[Tutorial: Create datasets and ingest data](https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/tutorials/data-management/create-datasets-and-ingest-data){target="_blank"}

### 5. Configure data sources in Journey Optimizer {#configure-data-sources}

In the Journey Optimizer UI:

1. Open the **[!UICONTROL Configurations]** area.
1. Configure the built-in [Adobe Experience Platform data source](../datasource/adobe-experience-platform-data-source.md).
1. Optionally configure [external or custom data sources](../datasource/external-data-sources.md).
1. Select which fields should be available for:
   * Journey conditions and enrichments
   * Personalization in messages
   * Decisioning criteria and ranking

[Learn more about data source configuration](../datasource/about-data-sources.md)

### 6. Verify tracking, feedback, and journey datasets {#verify-datasets}

* Confirm that Journey Optimizer system-generated datasets are available in the Datasets workspace
* Run test journeys and campaigns, then use Query Editor to verify that:
  * Send, open, click, and bounce events are recorded
  * Journey step events and states are captured correctly
* Use these datasets for monitoring, troubleshooting, analysis, reporting, and journey optimization

[Learn more about queries in Journey Optimizer](get-started-queries.md)

## Guardrails and data design considerations {#guardrails}

Some product guardrails and limitations can influence how you design your data model and journeys. Review these early to avoid rework later.

>[!IMPORTANT]
>Always refer to the latest product documentation for guardrails and limitations. The summaries below highlight key items but may evolve over time.

### Journey Optimizer system datasets and TTL {#datasets-ttl}

Journey Optimizer creates several system-generated datasets for tracking, feedback, and journey step events.

* As of February 2025, a time-to-live (TTL) guardrail is being rolled out to some system-generated datasets
* This may affect how long data is retained in those datasets for analysis and troubleshooting

[Learn more about datasets](get-started-datasets.md)

### Streaming segmentation and Journey Optimizer events {#streaming-segmentation}

* As of November 1st, 2024, streaming segmentation no longer supports send and open events from Journey Optimizer tracking and feedback datasets
* For use cases such as frequency capping and fatigue management, use [Business Rules](../conflict-prioritization/rule-sets.md) instead of streaming segments based on send/open events

[Learn more about datasets](get-started-datasets.md)

### Dataset lookup and decisioning {#lookup-guardrails}

Dataset lookup is ideal for:

* Frequently changing attributes (for example, inventory, pricing, weather)
* Data that does not need to be stored on the Real-Time Customer Profile

Review product-specific guardrails (such as dataset size limits and query caps) in the relevant documentation for dataset lookup and decisioning.

[Learn more about lookup datasets](lookup-aep-data.md)

## Example: preparing data for a welcome journey {#example}

The following example shows how the concepts on this page work together in a simple scenario.

**Step 1: Design profile and event schemas**

A data engineer creates:

* An XDM Individual Profile schema for customer attributes (name, email, loyalty tier, consent)
* An XDM ExperienceEvent schema for web sign-up events

**Step 2: Create profile-enabled datasets**

The engineer creates:

* A profile-enabled dataset for CRM attributes based on the profile schema
* An event dataset for web sign-up events based on the event schema

**Step 3: Ingest data into Adobe Experience Platform**

* Web and mobile teams use Adobe Experience Platform Web SDK to stream sign-up events into the event dataset
* CRM data is ingested via a source connector into the profile dataset

**Step 4: Configure the Adobe Experience Platform data source in Journey Optimizer**

An administrator configures the Experience Platform data source in Journey Optimizer and exposes fields such as:

* `profile.person.name.firstName`
* `profile.personalEmail.address`
* `profile.loyaltyTier`

**Step 5: Build and test a welcome journey**

A marketer creates a welcome journey that:

* Listens for a sign-up event
* Uses profile attributes from the data source to personalize the welcome email

Journey Optimizer writes send and open events to tracking datasets and logs journey progress in journey step event datasets.

**Step 6: Analyze and optimize**

A developer or analyst uses Query Editor to:

* Verify that events are flowing correctly
* Analyze performance (opens, clicks, time-to-send)

The team adjusts the journey and content based on these insights.

This end-to-end flow illustrates how schemas, datasets, sources, data sources, and queries work together to enable a simple but common use case.

## Next steps {#next-steps}

Once you understand the basics of data management in Journey Optimizer, explore the following topics for deeper guidance:

* [Get started with schemas](get-started-schemas.md) – Understand the XDM data model used by Journey Optimizer
* [Work with datasets](get-started-datasets.md) – Create, explore, and manage datasets used by Journey Optimizer
* [Configure data sources](../datasource/about-data-sources.md) – Expose profile and event fields inside journeys and messages
* [Use Adobe Experience Platform data (lookup)](lookup-aep-data.md) – Use datasets at runtime for personalization
* [Get started with queries](get-started-queries.md) – Use Query Editor to analyze journey data and troubleshoot
* [Get started with profiles](../audience/get-started-profiles.md) – Understand how Real-Time Customer Profile works in Journey Optimizer

**Tutorials**

* [Set up data overview](https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/tutorials/data-management/set-up-data-overview){target="_blank"} – End-to-end walkthrough of data setup for Journey Optimizer (beginner)
* [Create datasets and ingest data](https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/tutorials/data-management/create-datasets-and-ingest-data){target="_blank"} – Hands-on steps to create a dataset, map it to a schema, and confirm data ingestion
