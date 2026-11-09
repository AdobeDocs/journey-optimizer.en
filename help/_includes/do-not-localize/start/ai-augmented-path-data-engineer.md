---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page is the Data Engineer getting-started path, covering the essential data configuration steps — identities, schemas, datasets, source connectors, test profiles, and event and action setup — that power the experiences orchestrated by Journey Optimizer.

**Intents:**

* Create identity namespaces and configure supplemental identifiers
* Create schemas and datasets and enable them for profiles
* Configure source connectors to ingest data from external sources
* Create test profiles for test mode and message preview and testing
* Configure Data Sources, Events, and Actions to send messages in journeys
* Query journey step events in the Data Lake to monitor and analyze journey data

**Glossary:**

* **Identity namespace**: A construct that links consumers across devices and channels, producing an identity graph used to personalize experiences *(product-specific)*
* **Supplemental identifier**: A secondary identifier, such as an order ID or booking ID, that enables the same profile to enter multiple journey instances *(product-specific)*
* **Schema**: A set of rules that represent and validate the structure and format of data, providing an abstract definition of a real-world object *(product-specific)*
* **Dataset**: A storage and management construct for a collection of data, typically a table containing a schema (columns) and fields (rows) *(product-specific)*
* **Dataset lookup**: Preparing datasets for runtime lookups to enrich journey execution with real-time data from record datasets *(product-specific)*
* **Test profile**: A profile required when using test mode in a journey and to preview and test messages before sending *(product-specific)*

**Guardrails:**

* Test profiles are required when using test mode in a journey and to preview and test messages before sending.
* For standard journeys and campaigns, use XDM schemas; for Orchestrated campaigns, create relational schemas to enable multi-entity segmentation.
* Message export datasets apply only when message export is enabled at the channel configuration level, after which sent email and Mobile message content is automatically exported to a dedicated Experience Platform dataset.
* You can start working once the System Administrator has granted you access and prepared your environment.
* To send messages in journeys, you must configure Data Sources, Events, and Actions.

**Terminology:**

* Canonical name: Data Engineer — variants: Data Architect
* Acronym: XDM = Adobe Experience Data Model
* Implementation order: Administrator → Data Engineer → Developer → Marketer
* Do not confuse: "XDM schemas" (for standard journeys and campaigns) ≠ "relational schemas" (for Orchestrated campaigns and multi-entity segmentation)

**FAQ:**

* **Q: When are test profiles needed?** — They are required when using test mode in a journey and to preview and test messages before sending.
* **Q: Which schema type should I create?** — XDM schemas for standard journeys and campaigns, and relational schemas for Orchestrated campaigns to enable multi-entity segmentation.
* **Q: What do I need to configure so messages can be sent in journeys?** — Data Sources, Events, and Actions.
* **Q: Where do incoming events come from and how is their data structured?** — Events come from Streaming Ingestion APIs for authenticated and unauthenticated events, and the incoming data is normalized following the Adobe Experience Data Model (XDM).
* **Q: How can I monitor and troubleshoot running journeys?** — Query journey step events in the Data Lake using SQL to analyze entry and exit patterns, error rates and discard reasons, and journey instance states and bottlenecks.

**Personas:**

* **developer:** Can create identity namespaces, configure supplemental identifiers such as order IDs or booking IDs, and create XDM schemas or relational schemas for Orchestrated campaigns. Can create datasets with fields and columns, and configure source connectors to ingest data from external sources. The page states that events come from Streaming Ingestion APIs, and incoming event data is normalized following the Adobe Experience Data Model. Where: "Essential data configuration steps".

**Onboarding:**

* **Level:** Intermediate
* **First minimal step:** Create identity namespaces.
* **Success check:** The result is an identity graph that links consumers across devices and channels.
* **Previous:** Before starting data foundation work, complete Administrator setup: Journey Optimizer Get Started for System Admin (start/path/administrator.md); New to data in Journey Optimizer, understand schemas, datasets, and identities before configuration: Get started with data management in Journey Optimizer (data/gs-data.md)
* **Next:** After completing data foundation work, continue to the Developer role next in the implementation order: Get Started for Developers (start/path/developer.md); To get started with data analysis and troubleshooting once journeys are running, explore query examples: Examples of queries (reports/query-examples.md)

+++

<!-- ai-section-version: 1 | source-hash: dfd22d33 -->
