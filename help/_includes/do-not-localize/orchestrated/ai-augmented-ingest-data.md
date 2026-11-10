---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to ingest data into Adobe Experience Platform from sources supported for Orchestrated campaigns, configure a dataflow, and manage record deletions through Change data capture.

**Intents:**

* Identify the supported sources for ingesting data for Orchestrated campaigns (Cloud Storage, Cloud Data Warehouses, File-Based Uploads).
* Understand the one-to-one relationship enforced between dataflows and datasets, and how to change a data source.
* Configure a dataflow that ingests structured data into Adobe Experience Platform for Orchestrated campaigns.
* Enable Change data capture on a dataset mapped to a relational schema.
* Manage record deletions in Adobe Experience Platform using Change data capture, a file-based deletion marker, a proxy or sanitized table, or Data Distiller.
* Map source file attributes to target schema fields during dataflow configuration.

**Glossary:**

* **Dataset**: a storage and management construct for a collection of data, typically a table, that contains a schema (columns) and fields (rows) *(product-specific)*
* **Change data capture**: a dataset setting that automatically mirrors all data changes, including deletions, from the source system into Adobe Experience Platform *(product-specific)*
* **Change Request Type**: the file-based ingestion field used to mark a record for deletion with a "d" value *(product-specific)*
* **_change_request_type**: the required column for file-based sources, with values "u" (upsert) or "d" (delete), used to support change tracking *(product-specific)*
* **Data Distiller**: a licensed capability that can be used to support deletion operations directly within Adobe Experience Platform, independent of the source system *(product-specific)*

**Guardrails:**

* Adobe Experience Platform enforces a strict one-to-one relationship between dataflows and datasets (hard limit).
* To change the data source for a dataset, the existing dataflow must first be deleted before creating a new one that references the same dataset and the new source.
* Change data capture cannot be enabled on a dataset that already contains ingested data.
* Adobe Journey Optimizer Campaigns require all onboarded datasets to be enabled with Change data capture.
* Enabling Change data capture on the Dataset details page displays only datasets that are mapped to relational schemas and include both a primary key and a version descriptor.
* For file-based sources only, each row in the data file must include a _change_request_type column with values "u" (upsert) or "d" (delete); without this column, the system does not recognize the data as supporting change tracking, and the Orchestrated campaign toggle does not appear, preventing the dataset from being selected for targeting.
* For file-based sources, the maximum supported upload size is 100MB (hard limit).

**Prerequisites and permissions:**

* Data Distiller must be licensed to use it for deleting records directly within Adobe Experience Platform, independent of the source system.

**Applicability:**

* Applies: Orchestrated campaigns — the supported sources list and the dataflow configuration steps on this page are scoped to Orchestrated campaigns.

**Terminology:**

* Canonical name: Adobe Experience Platform — Acronym: AEP — variants: Platform
* Canonical name: Adobe Journey Optimizer — Acronym: AJO
* Synonyms: "dataflow" = "data flow"
* Do not confuse: "Change data capture" (automatically mirrors source deletions into Adobe Experience Platform) ≠ "Data Distiller" (deletes records only within Adobe Experience Platform, independent of the source system)

**FAQ:**

* **Q: What must I do before changing the data source for an existing dataset?** — Delete the existing dataflow before creating a new one that references the same dataset and the new source, because Adobe Experience Platform enforces a strict one-to-one relationship between dataflows and datasets.
* **Q: Which sources are supported for Orchestrated campaigns?** — Cloud Storage (Amazon S3, Google Cloud Storage, SFTP), Cloud Data Warehouses (Snowflake, Google BigQuery, Data Landing Zone, Azure Databricks), and File-Based Uploads (Local File Upload).
* **Q: Can Change data capture be enabled on a dataset that already has ingested data?** — No, Change data capture cannot be enabled on a dataset that already contains ingested data.
* **Q: How do I delete a record using file-based ingestion?** — Mark the record with a "d" value in the Change Request Type field, which indicates the record should be deleted in Adobe Experience Platform, mirroring the source system.
* **Q: How can I delete records from Adobe Experience Platform without affecting the source data?** — Use a proxy or sanitized source table for Change data capture replication, or, if licensed, use Data Distiller to delete records directly within Adobe Experience Platform.
* **Q: What happens if the _change_request_type column is missing from a file-based source?** — The system does not recognize the data as supporting change tracking, and the Orchestrated campaign toggle does not appear, preventing the dataset from being selected for targeting.

**Related pages:**

* For mapping source file attributes to target schema fields during dataflow configuration: Learn more about targeting dimensions (orchestrated/target-dimension.md)

**Personas:**

* **developer:** Can map each source file attribute to the corresponding field in the target schema during dataflow configuration. Can include a _change_request_type column in file-based source data, with values u for upsert or d for delete, to support change tracking. The page states that without this column, the Orchestrated campaign toggle does not appear, preventing the dataset from being selected for targeting. Where: "Configure a dataflow".
* **admin:** Can configure a dataflow for Orchestrated campaigns using Cloud Storage, Cloud Data Warehouses, or File-Based Uploads sources. Can enable Change data capture only on datasets mapped to relational schemas with a primary key and version descriptor. The page states that a dataflow must be deleted before creating a new one that references the same dataset and a new source. Where: "Guardrails".

**Onboarding:**

* **Level:** Experienced
* **First minimal step:** From the Connections menu, access the Sources menu.
* **Success check:** From the Connections menu, select Sources and access the Data Flows tab to track flow execution, review ingested records, and troubleshoot any errors.
* **Next:** Mapping source file attributes to target schema fields during dataflow configuration: Create your Targeting dimension (orchestrated/target-dimension.md)

+++

<!-- ai-section-version: 1 | source-hash: 84ef80e3 -->
