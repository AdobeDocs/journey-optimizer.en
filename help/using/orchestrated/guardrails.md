---
solution: Journey Optimizer
product: journey optimizer
title: Orchestrated campaigns guardrails and limitations
description: Learn about Orchestrated campaigns guardrails and limitations
exl-id: 82744db7-7358-4cc6-a9dd-03001759fef7
version: Campaign Orchestration
TQID: https://experienceleague.adobe.com/ViPJaOPo-AT-naQqq-PaPw-BI5YupYuYAEy56AUEp2A
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: ad78185d-8f79-40ad-9bad-cbde74af74ee
    internal-label: Guardrails and limitations
  - id: b3538224-471e-4c63-a444-9b19d89ae29c
    internal-label: Activities
topic_v2:
  - id: b23e006f-0a29-4f1d-8fd0-77aa56f3d12b
    internal-label: Data modeling
  - id: cdd65e7e-8839-44a2-bc21-0e03623b5dd1
    internal-label: Optimization
  - id: e0eb8757-182f-49f3-94a4-1587d16f5094
    internal-label: Personalization
subfeature_v2:
  - id: b5e335a9-0e5f-4dda-8845-c4ac5dca2be4
    internal-label: Orchestration activities
---
# Guardrails and limitations {#guardrails}

>[!BEGINSHADEBOX]

**On this page:** Review the guardrails and limitations that apply to data storage, ingestion, data modeling, activities, and channels in Orchestrated campaigns.

>[!ENDSHADEBOX]

You will find below guardrails and limitations when using Orchestrated campaigns.

## Dataflow limitations

### Data design & storage

* **Maximum tables** - The relational datastore supports a maximum of 200 tables (schemas).

* **Schema size** - For Orchestrated campaigns, the total size of any individual schema must not exceed 100 GB.

* **Daily update volume** - Daily updates to a schema should be limited to less than 20% of its total record count to maintain performance and stability.

* **Relational data model** - Relational data is the primary model supported for ingestion, data modeling, and segmentation use cases.

* **Identity field** - Schemas used for targeting must contain at least one identity field of type `String`, mapped to a defined identity namespace.

* **Attributes per schema** - The average number of attributes per schema should not exceed 50 columns to maintain manageability and performance.

* **Profiles enablement** - Relational schemas cannot be enabled for Adobe Experience Platform Profiles. Only Standard XDM schemas are supported for Adobe Experience Platform Profiles. Relational schemas can be enabled for Orchestrated campaigns or Action campaigns. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/catalog/datasets/user-guide#enable-profile)

### Data Ingestion {#data-ingestion}

* **Profile and relational ingestion** - Profile + relational data ingestion is required.

* **Change Data Capture sources** - All ingestion must occur via Change Data Capture sources:

    * **File-based sources** - The `_change_request_type` field is required. Values supported are `u` (upsert) or `d` (delete). These values must be lowercase `u` and `d`, not uppercase `U` and `D`.

    * **Cloud-based sources** - Table logging must be enabled.

* **Complete records only** - Partial record updates are not allowed; each row must be provided as a complete record.

* **Batch ingestion frequency** - Batch ingestion for Campaign Orchestration is limited to once every 15 minutes.

* **Ingestion latency** - Ingestion latency in the relational store typically ranges from 15 minutes to 2 hours, depending on:

    * Data volume

    * System concurrency

    * Type of operation (for example, inserts are faster than updates)

* **Dataflow to dataset relationship** - The dataflow to dataset relationship is 1–1. Only one source can feed one dataset at a given time. To switch the source, delete the existing dataflow and create a new dataflow with the new source.

### Data Modeling

* **Version descriptor** - All schemas, including fact tables, must include a version descriptor to ensure proper version control and traceability.

* **Primary key** - Each table must have a defined primary key to support data integrity and downstream operations.

* **Permanent table name** - The `table_name` assigned during dataset creation is permanent and is used throughout segmentation and personalization features.

* **Field groups** - Field groups are not supported in the current data modeling framework.

* **Composite primary keys** - Support for composite primary keys with file-upload flows is not available at this time.

## Activities limitations {#activities-limitations}

* **Channel activities limit** - An Orchestrated campaign supports a maximum of 10 channel activities (Email, SMS, Push, or Direct mail). Only channel activities count toward this limit. Targeting and flow control activities do not count (for example, Build audience, Wait, Split, Enrichment, Reconciliation, Fork, End, or Test).

  If you exceed the limit when saving or publishing, the operation fails. To stay within the limit, reduce the number of channel activities or split message delivery across multiple Orchestrated campaigns.

* **Canvas activities limit** - The number of activities on an Orchestrated campaign canvas is limited to 500. This limit applies to all activity types on the canvas. It is separate from the channel activities limit enforced at publication. For maintainability and performance, keep workflows under 100 activities in practice.

* **Scalar attributes only** - Only scalar attributes are supported in audience definitions; maps and arrays are not allowed.

* **Relational data for segmentation** - Segmentation activities primarily rely on relational data. While profile data can be included, using large profile datasets may impact performance.

* **Profile attribute limits** - Limits are enforced on the number of profile attributes that can be used in both batch and streaming audiences to maintain system efficiency.

* **Enumerations** - Enumerations are fully supported.

* **Read Audiences not cached** - Read Audiences are not cached; each campaign execution triggers a full audience evaluation from the underlying data.

* **Audience optimization** - Optimization is strongly recommended when working with large or complex audience definitions to ensure performance.

* **Saved audiences are static** - Saved audience activities are static; they reflect the data available at the time of campaign execution.

* **No append to Saved Audience** - Appending to a Saved Audience activity is not supported. Any modifications require a full overwrite of the audience.

## Channel limitations

Only SMS, Push, Email and Direct mail channels are supported in Orchestrated campaigns.
