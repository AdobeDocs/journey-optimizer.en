---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page gives a practical overview of how data flows into and out of Journey Optimizer — schemas, datasets, identities, profiles, data sources, and lookup datasets — plus the data readiness steps to complete before building journeys and campaigns.

**Intents:**

* Understand the core data building blocks used by Journey Optimizer (schemas, datasets, identities, profiles).
* Understand how Journey Optimizer uses Adobe Experience Platform data rather than a separate data store.
* Distinguish a source connector from a Journey Optimizer data source.
* Complete the six-step data readiness checklist.
* Understand lookup datasets versus profile storage.

**Glossary:**

* **XDM schema**: rules that represent, validate, and format data, built from a class and field groups *(product-specific)*
* **Dataset**: a storage table for data conforming to a schema *(product-specific)*
* **Source connector (source)**: streams or batches data from external systems into Adobe Experience Platform *(product-specific)*
* **Data source (Journey Optimizer)**: a UI configuration that declares which Adobe Experience Platform or external fields are exposed inside journeys and messages *(product-specific)*
* **Identity**: an identifier that uniquely represents an individual customer, organized into namespaces (Email, ECID, CRMID)
* **Real-Time Customer Profile**: maintains a holistic view of each individual customer by combining data from multiple channels, stitching profile fragments together based on shared identity values *(product-specific)*
* **Profile fragment**: a partial view of a customer based on a specific touchpoint *(product-specific)*
* **Lookup dataset**: a runtime reference to an Adobe Experience Platform dataset without storing that data on the Real-Time Customer Profile *(product-specific)*

**Guardrails:**

* In the data readiness checklist, Steps 1–4 are completed in Adobe Experience Platform and Steps 5–6 are configured in Journey Optimizer.
* Direct access to experience event data via the built-in Adobe Experience Platform data source is deprecated and being progressively disabled.
* As of February 2025, a time-to-live (TTL) guardrail is being rolled out to some Journey Optimizer system-generated datasets.
* As of November 1, 2024, streaming segmentation no longer supports send and open events from Journey Optimizer tracking and feedback datasets; use Business Rules instead.
* Review product-specific guardrails such as dataset size limits and query caps before designing a lookup strategy.

**Terminology:**

* Synonyms: "source connector" = "source"
* Do not confuse: "data source" in Journey Optimizer (a UI configuration that exposes fields inside journeys and messages) ≠ the generic "data source" in the Adobe Experience Platform Glossary (the origin of data, such as a CRM or mobile app)
* Do not confuse: "source connector" (ingests external data into Adobe Experience Platform) ≠ "data source" (exposes Adobe Experience Platform or external fields inside journeys)
* Do not confuse: "lookup dataset" (runtime reference, not stored on the profile) ≠ profile datasets (contribute to Real-Time Customer Profile)

**FAQ:**

* **Q: Does Journey Optimizer keep its own separate data store?** — No; it uses the same Adobe Experience Platform data foundation as other CX Enterprise applications.
* **Q: What is the difference between a source connector and a data source?** — A source connector ingests data into Adobe Experience Platform; a Journey Optimizer data source declares which fields are exposed inside journeys and messages.
* **Q: What is a profile fragment?** — A partial view of a customer based on a specific touchpoint, which Real-Time Customer Profile stitches together into a complete profile.
* **Q: Where are the checklist steps performed?** — Steps 1–4 in Adobe Experience Platform; Steps 5–6 in Journey Optimizer.
* **Q: When should I use a lookup dataset?** — For frequently changing reference or transactional data needed at message time that does not belong on the Real-Time Customer Profile.

**Personas:**

* **developer:** Can use Query Editor to verify that send, open, click, and bounce events are recorded in Journey Optimizer datasets. Can confirm that journey step events and states are captured correctly. The page states that Steps 1-4 of the data readiness checklist are completed in Adobe Experience Platform and Steps 5-6 are configured in Journey Optimizer. Where: "Data readiness checklist".
* **admin:** Can configure the built-in Adobe Experience Platform data source to expose Real-Time Customer Profile attributes inside journeys. Can also configure external data sources to call third-party APIs at journey runtime, such as a loyalty score or inventory level. The page states that configuring data sources is an administrative task that unlocks the data layer for journey authors and marketers. Where: "Data readiness checklist".
* **marketer:** Can create a welcome journey that listens for a sign-up event, as shown in the page's example. Can personalize the welcome email using profile attributes such as [!DNL firstName] and [!DNL personalEmail.address]. The page states that Journey Optimizer writes send and open events to tracking datasets as the journey runs. Where: "Example: preparing data for a welcome journey".

**Onboarding:**

* **Level:** Beginner, Intermediate
* **First minimal step:** Choose a primary identity for your customers, such as ECID, email, or CRMID, and configure the corresponding namespaces in Adobe Experience Platform Identity Service.
* **Success check:** Validate that profiles are correctly stitched into the identity graph.
* **Previous:** Before defining an identity strategy for Journey Optimizer: Get Started with Identities in Journey Optimizer (audience/get-started-identity.md); Before understanding how Real-Time Customer Profile combines data from multiple channels: Get Started with Profiles in Journey Optimizer (audience/get-started-profiles.md)
* **Next:** After completing the data readiness checklist, building a journey: Create your first journey (building-journeys/journey-gs.md); After exposing profile fields through a data source, personalizing a message: Personalize content in Journey Optimizer (personalization/personalize.md)

+++

<!-- ai-section-version: 1 | source-hash: 1e17c925 -->
