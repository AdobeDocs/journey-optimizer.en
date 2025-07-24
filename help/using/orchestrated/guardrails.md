---
solution: Journey Optimizer
product: journey optimizer
title: Orchestrated campaigns guardrails and limitations
description: Learn about Orchestrated campaigns guardrails and limitations
hide: yes
hidefromtoc: yes
exl-id: 82744db7-7358-4cc6-a9dd-03001759fef7
---
# Guardrails and limitations {#guardrails}

+++ Table of Contents

| Welcome to orchestrated campaigns | Launch your first orchestrated campaign | Query the database | Ochestrated campaigns activities|
|---|---|---|---|
|[Get started with orchestrated campaigns](gs-orchestrated-campaigns.md)<br/><br/>Create and manage relational Schemas and Datasets:</br> <ul><li>[Get started with Schemas and Datasets](gs-schemas.md)</li><li>[Manual schema](manual-schema.md)</li><li>[File upload schema](file-upload-schema.md)</li><li>[Ingest data](ingest-data.md)</li></ul>[Access and manage orchestrated campaigns](access-manage-orchestrated-campaigns.md)<br/><br/>[Key steps to create an orchestrated campaign](gs-campaign-creation.md)|[Create and schedule the campaign](create-orchestrated-campaign.md)<br/><br/>[Orchestrate activities](orchestrate-activities.md)<br/><br/>[Start and monitor the campaign](start-monitor-campaigns.md)<br/><br/>[Reporting](reporting-campaigns.md)|[Work with the rule builder](orchestrated-rule-builder.md)<br/><br/>[Build your first query](build-query.md)<br/><br/>[Edit expressions](edit-expressions.md)<br/><br/>[Retargeting](retarget.md)|[Get started with activities](activities/about-activities.md)<br/><br/>Activities:<br/>[And-join](activities/and-join.md) - [Build audience](activities/build-audience.md) - [Change dimension](activities/change-dimension.md) - [Channel activities](activities/channels.md) - [Combine](activities/combine.md) - [Deduplication](activities/deduplication.md) - [Enrichment](activities/enrichment.md) - [Fork](activities/fork.md) - [Reconciliation](activities/reconciliation.md) - [Save audience](activities/save-audience.md) - [Split](activities/split.md) - [Wait](activities/wait.md)|

{style="table-layout:fixed"}

+++

## Dataflow-to-Dataset limitations

Each dataset in Adobe Experience Platform can only be associated with one active dataflow at a time. This 1:1 cardinality is strictly enforced by the platform.

If you need to switch data sources (e.g., from Amazon S3 to Salesforce):

You must delete the existing dataflow connected to the dataset.

Then, create a new dataflow with the new source mapped to the same dataset.

This ensures reliable data ingestion and is essential when using Change Data Capture (CDC), which depends on a defined primary key and versioning attribute (e.g., lastmodified) for incremental updates.


## Relational schemas / data ingestion limitations

* Up to 200 relational schemas (tables) are supported in the relational datastore.

* The total size of a relational schema used for Campaign Orchestration should not exceed 100 GB.

* Batch ingestion for Campaign Orchestration should occur no more frequently than once every 15 minutes.

* Daily changes to a relational schema should remain below 20% of the total record count.

## Data modeling

* Version descriptor is mandatory on all schemas, including fact tables.

* A primary key is required for every table.

* The table_name assigned during dataset creation is used across the segmentation UI and personalization features.
    
    This name is permanent and cannot be changed after creation.

* Field groups are currently not supported.

## Data Ingestion 

* Profile + relational data ingestion is required.

* A change type field is required for file-based ingestion, while table logging must be enabled for Cloud DB ingestion. This is necessary for Change Data Capture (CDC).

* Latency from ingestion to data availability in Snowflake ranges from 15 minutes to 2 hours, depending on data volume, concurrency, and the type of operations (inserts are faster than updates).

* Data monitoring in Snowflake is under development; currently, there is no native confirmation for successful ingestion.

* Direct updates to Snowflake or the dataset are not supported. All changes must flow through CDC sources.

    The query service is read-only.

* ETL is not supported — customers must supply data in the required format.

* Partial updates are not allowed. Each row must be provided as a complete record.

* Ingestion relies on Query Service and Data Distiller.

## Segmentation

* LOV (List of Values) and enumerations are currently available.

* Saved Audiences are static lists, their content reflects the data available at the time the campaign is executed.

* Appending to a Saved Audience is not supported. Updates require a full overwrite.

* Audiences must consist of scalar attributes only; maps and arrays are not supported.

* Segmentation primarily supports relational data. While mixing with profile data is allowed, bringing in large profile datasets can affect performance. To prevent this:

* Guardrails are in place, such as limiting the number of profile attributes selected in batch or streaming audiences.

* Read Audiences are not cached — each campaign run triggers a full read.

    Optimization is needed for large or complex audiences.