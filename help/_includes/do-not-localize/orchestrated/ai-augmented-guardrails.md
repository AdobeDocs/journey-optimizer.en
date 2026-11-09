---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page lists the guardrails and limitations for Orchestrated campaigns across data storage, ingestion, data modeling, audiences, activities, and channels.

**Intents:**

* Determine how much relational data a schema can hold and how fast it can grow before performance is affected.
* Identify how data must be ingested into the relational store, including required fields and timing.
* Understand data modeling requirements such as version descriptors and primary keys.
* Learn which audience attribute types and audience behaviors are supported.
* Determine how many channel activities and total activities an Orchestrated campaign canvas can contain.
* Identify which channels are supported in Orchestrated campaigns.

**Glossary:**

* **Relational datastore**: the storage layer for Orchestrated campaigns that supports a maximum of 200 tables (schemas) *(product-specific)*
* **Change Data Capture sources**: the required ingestion method for Orchestrated campaigns, which can be file-based (using the `_change_request_type` field) or cloud-based (using table logging) *(product-specific)*
* **Table name**: the `table_name` assigned during dataset creation, used throughout segmentation and personalization features *(product-specific)*
* **Read Audiences**: audience activities that trigger a full audience evaluation from the underlying data at each campaign execution, rather than using cached results *(product-specific)*
* **Saved audience**: an audience activity that is static and reflects the data available at the time of campaign execution *(product-specific)*

**Guardrails:**

* Maximum tables: the relational datastore supports a maximum of 200 tables (schemas) (hard limit).
* Schema size: the total size of any individual schema must not exceed 100 GB (hard limit).
* Daily update volume: daily updates to a schema should be limited to less than 20% of its total record count to maintain performance and stability (recommended).
* Relational data is the primary model supported for ingestion, data modeling, and segmentation use cases.
* Schemas used for targeting must contain at least one identity field of type String, mapped to a defined identity namespace.
* Attributes per schema: the average number of attributes per schema should not exceed 50 columns to maintain manageability and performance (recommended).
* Relational schemas cannot be enabled for Adobe Experience Platform Profiles (hard limit); only Standard XDM schemas are supported for Adobe Experience Platform Profiles. Relational schemas can be enabled for Orchestrated campaigns or Action campaigns.
* Profile + relational data ingestion is required.
* All ingestion must occur via Change Data Capture sources.
* File-based sources require the `_change_request_type` field, with supported values `u` (upsert) or `d` (delete), lowercase only.
* Cloud-based sources require table logging to be enabled.
* Partial record updates are not allowed; each row must be provided as a complete record.
* Batch ingestion frequency for Campaign Orchestration is limited to once every 15 minutes (hard limit).
* Ingestion latency in the relational store typically ranges from 15 minutes to 2 hours, depending on data volume, system concurrency, and type of operation (for example, inserts are faster than updates).
* The dataflow to dataset relationship is 1–1: only one source can feed one dataset at a given time. To switch the source, delete the existing dataflow and create a new dataflow with the new source.
* All schemas, including fact tables, must include a version descriptor.
* Each table must have a defined primary key.
* The `table_name` assigned during dataset creation is permanent.
* Field groups are not supported in the current data modeling framework.
* Support for composite primary keys with file-upload flows is not available at this time.
* Only scalar attributes are supported in audience definitions; maps and arrays are not allowed.
* Segmentation activities primarily rely on relational data; profile data can be included, but using large profile datasets may impact performance.
* Limits are enforced on the number of profile attributes that can be used in both batch and streaming audiences, but the page does not state the figures.
* Enumerations are fully supported.
* Read Audiences are not cached; each campaign execution triggers a full audience evaluation from the underlying data.
* Audience optimization is strongly recommended when working with large or complex audience definitions (recommended).
* Saved audience activities are static; they reflect the data available at the time of campaign execution.
* Appending to a Saved Audience activity is not supported; any modifications require a full overwrite of the audience.
* An Orchestrated campaign supports a maximum of 10 channel activities (Email, Mobile message, Push, or Direct mail) (hard limit, enforced when saving or publishing). Only channel activities count toward this limit; Targeting, Data Management, and flow control activities (for example, Build audience, Load file, Wait, Split, Enrichment, Reconciliation, Fork, End, or Test) do not count. Exceeding the limit causes the save or publish operation to fail.
* The number of activities on an Orchestrated campaign canvas is limited to 500 (hard limit), covering all activity types. This limit is separate from the channel activities limit enforced at publication.
* Keep workflows under 100 activities in practice for maintainability and performance (recommended).
* Only Mobile message, Push, Email, and Direct mail channels are supported in Orchestrated campaigns.

**Terminology:**

* Canonical name: channel activities — variant: channel activities limit
* Do not confuse: channel activities limit (maximum 10 Email, Mobile message, Push, or Direct mail activities, enforced when saving or publishing) ≠ canvas activities limit (maximum 500 activities of any type on the canvas)
* Do not confuse: "Read Audiences" (not cached, evaluated fully at each campaign execution) ≠ "Saved audiences" (static, reflecting data at the time of campaign execution)

**FAQ:**

* **Q: How many tables does the relational datastore support?** — A maximum of 200 tables (schemas).
* **Q: How many channel activities can an Orchestrated campaign have?** — A maximum of 10 channel activities (Email, Mobile message, Push, or Direct mail); exceeding this limit causes the save or publish operation to fail.
* **Q: How many activities total can be on the canvas?** — Up to 500 activities of any type; this is separate from the channel activities limit.
* **Q: Which channels are supported in Orchestrated campaigns?** — Mobile message, Push, Email, and Direct mail.
* **Q: Can relational schemas be enabled for Adobe Experience Platform Profiles?** — No; only Standard XDM schemas are supported for Adobe Experience Platform Profiles.
* **Q: Can I append data to a Saved Audience activity?** — No; any modifications require a full overwrite of the audience.

**Personas:**

* **admin:** Can reduce the number of channel activities or split message delivery across multiple Orchestrated campaigns to stay within the 10 channel activities limit. The page states that exceeding this limit causes the save or publish operation to fail. Where: "Activities limitations".

**Onboarding:**

* **Level:** Intermediate
* **First minimal step:** Include a version descriptor in every schema, including fact tables.

+++

<!-- ai-section-version: 1 | source-hash: 087567cd -->
