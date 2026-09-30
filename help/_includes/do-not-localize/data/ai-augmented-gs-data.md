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
* **Real-Time Customer Profile**: the unified profile assembled by stitching profile fragments across channels *(product-specific)*
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

+++

<!-- ai-section-version: 1 | source-hash: 466dff8e -->
