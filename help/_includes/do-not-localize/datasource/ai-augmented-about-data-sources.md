---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains what data sources are in Journey Optimizer, the two types available (the built-in Adobe Experience Platform data source and external data sources), and how to choose between three data access strategies before configuring one.

**Intents:**

* Understand what a data source is and when a data source configuration is needed
* Distinguish the pre-configured Adobe Experience Platform data source from external data sources
* Choose a data access strategy among the three available options
* Understand what field groups are used for on a data source
* Decide whether to access external data via custom actions, ingest into a dataset, or use a profile-enabled dataset

**Glossary:**

* **Data source**: A configuration that defines a connection to a system to retrieve additional information used in journeys for condition definition, parameter and personalization data in actions, custom wait definition, and time zone definition *(product-specific)*
* **Pre-configured Adobe Experience Platform data source**: The built-in data source that defines the connection to the Real-time Customer Profile Service *(product-specific)*
* **External data source**: A data source you create to define a connection to external systems *(product-specific)*
* **Field group**: A set of fields that can be retrieved from a data source *(product-specific)*

**Guardrails:**

* The data source configuration is always performed by a technical user.
* A data source configuration is not required if your journeys only leverage local data coming from an event payload.
* Schema relationships are not supported for data sources.
* Because responses are now supported, you should use custom actions instead of data sources for external data source use-cases.
* Before enabling a dataset for Profile (Option 3), assess data synchronization, Profile guardrails, identity integrity, and Data Lake utilization.

**Terminology:**

* Canonical name: data source — Acronym: n/a — variants: data source configuration
* Synonyms: "pre-configured Adobe Experience Platform data source" = "built-in data source"
* Do not confuse: "Adobe Experience Platform data source" (pre-configured, built-in) ≠ "external data source" (one you create)
* Do not confuse: "Option 2 — Dataset in Data Lake, not enabled for Profile" (persisted, not contributing to Profile) ≠ "Option 3 — Profile-enabled dataset in Data Lake" (persisted and enabled for Profile)

**FAQ:**

* **Q: When is a data source configuration required?** — It is not required if your journeys only use local data coming from an event payload; it is needed when you want to retrieve additional information for conditions, personalization, custom wait, or time zone.
* **Q: What are the two types of data sources?** — The pre-configured Adobe Experience Platform data source (built-in) and external data sources that you create.
* **Q: How many external data sources can I create?** — You can create as many external data sources as you need.
* **Q: Which data access strategy should I choose?** — Option 1 accesses external data via custom actions without persisting in the Data Lake, Option 2 ingests into a dataset not enabled for Profile, and Option 3 uses a profile-enabled dataset; choose based on persistence, profile enrichment, and reusability needs.
* **Q: Are schema relationships supported for data sources?** — No, schema relationships are not supported for data sources.

+++

<!-- ai-section-version: 1 | source-hash: 1d9c2ff0 -->
