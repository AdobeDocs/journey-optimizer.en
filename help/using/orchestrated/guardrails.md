---
solution: Journey Optimizer
product: journey optimizer
title: Orchestrated campaigns guardrails and limitations
description: Learn about Orchestrated campaigns guardrails and limitations
exl-id: 82744db7-7358-4cc6-a9dd-03001759fef7
version: Campaign Orchestration
---

# Guardrails and limitations {#guardrails}

You will find below additional guardrails and limitations when using Orchestrated campaigns.

## Dataflow limitations

### Data Design & Storage

* The relational datastore supports a **maximum of 200 tables** (schemas).

* For Orchestrated campaigns, the total size of any individual schema **must not exceed 100 GB**.

* Daily updates to a schema should be **limited to less than 20%** of its total record count to maintain performance and stability.

* Relational data is the primary model supported for ingestion, data modeling, and segmentation use cases.

* Schemas used for targeting must contain at least **one identity field of type `String`**, mapped to a defined identity namespace.

* The average number of attributes per schema **should not exceed 50 columns** to maintain manageability and performance.

### Data Ingestion

* Profile + relational data ingestion is required.

* All ingestion must occur via **Change Data Capture** sources:

    * For **File-based**: `_change_request_type` field is required. Values supported are `U` (upsert) or `D` (delete).

    * For **Cloud-based**: Table logging must be enabled.

* **Partial record updates are not allowed**, each row must be provided as a complete record.

* Batch ingestion for Campaign Orchestration is limited to **once every 15 minutes**.

* Ingestion latency, in relational store, typically ranges **from 15 minutes to 2 hours**, depending on:

    * Data volume

    * System concurrency

    * Type of operation, e.g. inserts are faster than updates

* **Dataflow to dataset relationship is 1–1**. This means only one source can feed one dataset at a given time. To switch the source, the existing dataflow must be deleted and a new dataflow created with the new source.

### Data Modeling

* All schemas, including fact tables, must include **a version descriptor** to ensure proper version control and traceability.

* Each table must have a defined **primary key** to support data integrity and downstream operations.

* The `table_name` assigned during dataset creation is permanent and is used throughout segmentation and personalization features.

* **Field groups are not supported** in the current data modeling framework.

## Activities limitations

* Only **scalar attributes are supported** in audience definitions; **maps and arrays are not allowed**.

* **Segmentation activities primarily relies on relational data**. While profile data can be included, using large profile datasets may impact performance.

* **Limits are enforced on the number of profile attributes** that can be used in both batch and streaming audiences to maintain system efficiency.

* **Enumerations** are fully supported.

* **Read Audiences are not cached**, each campaign execution triggers a full audience evaluation from the underlying data.

* **Optimization is strongly recommended** when working with large or complex audience definitions to ensure performance.

* **Saved audiences activites are static**, they reflect the data available at the time of campaign execution.

* **Appending to a Saved Audience activity is not supported**. Any modifications require a full overwrite of the audience.

## Channel limitations

Only SMS, Push and Email channels are supported in Orchestrated campaigns.
