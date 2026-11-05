---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to create relational schemas in Adobe Experience Platform by uploading a DDL file, defining relationships between tables, and linking schemas to existing entities for use in Orchestrated campaigns.

**Intents:**

* Upload a DDL file to create relational schemas and define their structure.
* Define relationships between tables in the data model, either within the DDL file or in the interface.
* Link a relational schema to existing profile entities such as Recipients or Brands.
* Identify the required table structure elements: primary key, version identifier, and identity field for targeting.
* Monitor the progress of a DDL import job.
* Resolve schema or dataset errors returned during this process.

**Glossary:**

* **Relational schema**: a schema created to define the data model required for Orchestrated campaigns, such as Loyalty Memberships, Loyalty Transactions, or Loyalty Rewards *(product-specific)*
* **DDL file**: a Data Definition Language file used to define tables, attributes, keys, and relationships of a data model in advance *(product-specific)*
* **ENUM**: a field type supporting a fixed set of allowed values, supported in both DDL-based and manual schema creation *(product-specific)*
* **Composite key / Composite relationships**: primary keys or relationships spanning multiple fields, supported in relational schema definitions and created automatically when loading from a DDL or Excel file *(product-specific)*
* **Schema label**: a labeling mechanism at the schema field level used to enforce data governance policies such as access control and usage restrictions *(product-specific)*
* **Version descriptor**: an attribute (for example `lastmodified`) designated to ensure datasets are updated with the latest data; type `datetime`, `long`, or `int` *(product-specific)*
* **Identity field**: a field of type `String` with an associated identity namespace, required on any schema used for targeting *(product-specific)*
* **Cardinality**: the type of relationship between two tables — 1-N, N-1, or 1-1 *(product-specific)*

**Guardrails:**

* A DDL file must not define more than 200 tables (hard limit).
* A table cannot reference itself: self-referential relationships are not allowed in the DDL file (hard limit).
* The maximum supported size for a DDL file is 10MB (hard limit).
* The DDL file name must contain only letters, numbers, underscores (_), hyphens (-), or spaces, and include a single extension (hard limit).
* The table structure must contain at least one primary key and a version identifier, such as a `lastmodified` field of type `datetime` or `number`.
* For Change Data Capture (CDC) ingestion, the table structure must contain a special column named `_change_request_type` of type `String`.
* Any schema used for targeting must include at least one identity field of type `String` with an associated identity namespace, to ensure compatibility with Adobe Journey Optimizer's targeting and identity resolution capabilities.
* An attribute cannot be both a primary key (PK) and a version descriptor.
* The version descriptor becomes mandatory once set, though users can change it.
* Only relationships explicitly defined within the DDL file are recognized by the system; any entity relationships that exist outside of the DDL file are ignored and not processed.
* The **View relationships diagram** from the **Relationship** tab is read-only; to create or edit a relationship, the schema must be opened from the **Browse** tab instead.
* Saving the data model creates the schemas and associated data sets and enables the data set for use in Orchestrated campaigns.

**Terminology:**

* Canonical name: relational schema — variants: schema
* Do not confuse: "1-N" cardinality (one source occurrence can have several target occurrences, but one target occurrence has at most one corresponding source occurrence) ≠ "N-1" cardinality (one target occurrence can have several source occurrences, but one source occurrence has at most one corresponding target occurrence) ≠ "1-1" cardinality (one source occurrence can have at most one corresponding target occurrence)
* Do not confuse: "primary key" (uniquely identifies records) ≠ "version descriptor" (ensures datasets are updated with the latest data) — an attribute cannot be both

**FAQ:**

* **Q: What must a table structure contain to create a relational schema from a DDL file?** — At least one primary key, a version identifier such as a `lastmodified` field of type `datetime` or `number`, and for CDC ingestion a `_change_request_type` column of type `String`.
* **Q: Is there a limit on the number of tables in a DDL file?** — Yes, a DDL file must not define more than 200 tables.
* **Q: Can a table reference itself in the DDL file?** — No, self-referential relationships are not allowed in the DDL file.
* **Q: What is the maximum DDL file size?** — 10MB.
* **Q: What is required for a schema used for targeting?** — At least one identity field of type `String` with an associated identity namespace.
* **Q: Are relationships defined outside the DDL file recognized?** — No, only relationships explicitly defined within the DDL file are recognized; entity relationships that exist outside of the DDL file are ignored and not processed.
* **Q: Where can a relationship be created or edited?** — From the Browse tab; the View relationships diagram from the Relationship tab is read-only.

**Related pages:**

* For ingesting data into a dataset after creating relational schemas: Ingest data (orchestrated/ingest-data.md)
* For resolving a schema or dataset error code: Relational schema and dataset errors (orchestrated/relational-schema-errors.md)

**Personas:**

* **developer:** Can create relational schemas by uploading a DDL file that defines tables, attributes, keys, and relationships. Can use ENUM fields with a fixed set of allowed values, and composite primary keys and composite relationships spanning multiple fields. The page states that any schema used for targeting must include at least one identity field of type String with an associated identity namespace. Where: "Upload a DDL file".
* **admin:** Can select Relational as the Schema type and select Upload DDL file to define an entity relationship diagram. Can navigate the Data Management > Schema menu to create a schema, then select Open Jobs to monitor the DDL import job. The page states that a DDL file must not define more than 200 tables and must not exceed 10MB in size. Where: "Guardrails".

**Onboarding:**

* **Level:** Experienced
* **First minimal step:** Select Relational as your Schema type.
* **Success check:** You can now verify the table and field definitions within the canvas.
* **Next:** After creating relational schemas, ingest data into your dataset: Configuration steps (orchestrated/ingest-data.md); If a schema or dataset returns an error code: Relational schema and dataset errors (orchestrated/relational-schema-errors.md)

+++

<!-- ai-section-version: 1 | source-hash: 26f7fe6f -->
