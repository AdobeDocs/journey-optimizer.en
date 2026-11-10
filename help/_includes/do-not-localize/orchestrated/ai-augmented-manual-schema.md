---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to manually create a relational schema in Adobe Experience Platform, add attributes, link schemas, and create and enable a dataset for use in Orchestrated campaigns.

**Intents:**

* Create a relational schema manually through the Adobe Experience Platform interface.
* Add attributes to a relational schema, including primary key, version descriptor, and required fields.
* Link a relational schema to another schema, such as Recipients, to extend Orchestrated campaigns with additional data.
* Create a dataset from a relational schema and enable it for Orchestrated campaigns.
* Ingest data into the enabled dataset.

**Glossary:**

* **Relational schema**: a schema type created directly through the Adobe Experience Platform interface, enabling detailed configuration of attributes, primary keys, versioning fields, and relationships *(product-specific)*
* **Version Descriptor**: a field, such as `lastmodified` of type `datetime` or `number`, used as a version identifier in a manual schema *(product-specific)*
* **_change_request_type**: a special column of type String used for Change Data Capture (CDC) ingestion, indicating the type of data change (insert, update, delete) and enabling incremental processing *(product-specific)*
* **Composite Key**: a primary key spanning multiple fields, supported in relational schema definitions *(product-specific)*
* **Schema Label**: a data governance label supported at the schema field level to enforce policies such as access control and usage restrictions *(product-specific)*

**Guardrails:**

* Any schema used for targeting must include at least one identity field of type String with an associated identity namespace, to ensure compatibility with Adobe Journey Optimizer's targeting and identity resolution capabilities.
* A manual schema must include at least one primary key and a version identifier, such as a `lastmodified` field of type `datetime` or `number`.
* For Change Data Capture (CDC) ingestion, the `_change_request_type` column must not be part of the table schema; it must only be added to the data file during ingestion.
* ENUM fields are supported in both DDL-based and manual schema creation.
* Composite primary keys spanning multiple fields are supported in relational schema definitions.
* The View relationships diagram on the Relationship tab is read-only; to create or edit a relationship, the schema must be opened from the Browse tab instead.
* After enabling a dataset for Orchestrated campaigns, data ingestion and campaign use are only possible once the enablement setting is fully activated.

**Terminology:**

* Canonical name: Adobe Experience Platform — Acronym: AEP

**FAQ:**

* **Q: What fields must a manual relational schema include?** — At least one primary key and a version identifier, such as a `lastmodified` field of type datetime or number.
* **Q: What is required for a schema used for targeting?** — At least one identity field of type String with an associated identity namespace.
* **Q: Where does the `_change_request_type` column belong?** — It is used for Change Data Capture (CDC) ingestion and must only be added to the data file during ingestion, not to the table schema.
* **Q: Can I edit a relationship from the View relationships diagram?** — No, that view on the Relationship tab is read-only; open the schema from the Browse tab to create or edit a relationship.
* **Q: What must be done after creating a dataset from a relational schema?** — The dataset must be explicitly enabled for Orchestrated campaigns before data ingestion and campaign use are possible.

**Related pages:**

* To ingest data into the created dataset: Configuration steps (orchestrated/ingest-data.md)
* If a schema or dataset returns an error code: Relational schema and dataset errors (orchestrated/relational-schema-errors.md)

**Personas:**

* **developer:** Can add attributes such as customer, membership_level, points_balance, enrollment_date, and lastmodified when defining a relational schema. Can use a special column named _change_request_type of type String to indicate insert, update, or delete for Change Data Capture ingestion. The page states that _change_request_type must only be added to the data file during ingestion, not to the table schema. Where: "Add attributes to your schema".
* **admin:** Can create a dataset from a relational schema and enable the Orchestrated campaigns option from the Datasets settings. Can locate the dataset in the Datasets list before enabling it. The page states that data ingestion and campaign use are only possible once this setting is fully activated. Where: "Enable dataset for orchestrated campaigns".

**Onboarding:**

* **Level:** Experienced
* **First minimal step:** Create a relational schema manually using the Adobe Experience Platform interface.
* **Success check:** You can now start ingesting data into your schema using the source of your choice.
* **Next:** Ingest data into the enabled dataset: Configuration steps (orchestrated/ingest-data.md); If a schema or dataset returns an error code: Relational schema and dataset errors (orchestrated/relational-schema-errors.md)

+++

<!-- ai-section-version: 1 | source-hash: 5c950de8 -->
