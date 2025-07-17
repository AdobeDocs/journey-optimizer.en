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
|[Get started with orchestrated campaigns](gs-orchestrated-campaigns.md)<br/><br/>Create and manage relational Schemas and Datasets:</br> <ul><li>[Manual schema](manual-schema.md)</li><li>[File upload schema](file-upload-schema.md)</li><li>[Ingest data](ingest-data.md)</li></ul><br/><br/>[Access and manage orchestrated campaigns](access-manage-orchestrated-campaigns.md)<br/><br/>[Key steps to create an orchestrated campaign](gs-campaign-creation.md)|[Create and schedule the campaign](create-orchestrated-campaign.md)<br/><br/>[Orchestrate activities](orchestrate-activities.md)<br/><br/>[Start and monitor the campaign](start-monitor-campaigns.md)<br/><br/>[Reporting](reporting-campaigns.md)|[Work with the rule builder](orchestrated-rule-builder.md)<br/><br/>[Build your first query](build-query.md)<br/><br/>[Edit expressions](edit-expressions.md)<br/><br/>[Retargeting](retarget.md)|[Get started with activities](activities/about-activities.md)<br/><br/>Activities:<br/>[And-join](activities/and-join.md) - [Build audience](activities/build-audience.md) - [Change dimension](activities/change-dimension.md) - [Channel activities](activities/channels.md) - [Combine](activities/combine.md) - [Deduplication](activities/deduplication.md) - [Enrichment](activities/enrichment.md) - [Fork](activities/fork.md) - [Reconciliation](activities/reconciliation.md) - [Save audience](activities/save-audience.md) - [Split](activities/split.md) - [Wait](activities/wait.md)|

{style="table-layout:fixed"}

+++

## Dataflow-to-Dataset limitations

Each dataset in Adobe Experience Platform can only be associated with one active dataflow at a time. This 1:1 cardinality is strictly enforced by the platform.

If you need to switch data sources (e.g., from Amazon S3 to Salesforce):

You must delete the existing dataflow connected to the dataset.

Then, create a new dataflow with the new source mapped to the same dataset.

This ensures reliable data ingestion and is essential when using Change Data Capture (CDC), which depends on a defined primary key and versioning attribute (e.g., lastmodified) for incremental updates.


## Relational schemas / data ingestion limitations

* Number of Schemas - Maximum number of relational schemas (tables in the relational datastore) is 200 
* Relational Schema Size – Maximum Relational Schema Size for Campaign Orchestration will be 100GB. 
* Data Ingestion Frequency – Batch Data Ingestion Frequency for Campaign Orchestration not to exceed one every fifteen minutes. 
* Changes/Updates - Daily updates/changes should be under 20% of total records for a given relational schema
