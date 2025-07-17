---
solution: Journey Optimizer
product: journey optimizer
title: Configuration steps
description: Learn how to create a relational schema within Adobe Experience Platform by uploading a DDL
badge: label="Alpha"
hide: yes
hidefromtoc: yes
---
# Get started with schemas and associated {#file-upload-schema}

+++ Table of Contents

| Welcome to orchestrated campaigns | Launch your first orchestrated campaign | Query the database | Ochestrated campaigns activities|
|---|---|---|---|
|[Get started with orchestrated campaigns](gs-orchestrated-campaigns.md)<br/><br/>Create and manage relational Schemas and Datasets:</br> <ul><li>[Manual schema](manual-schema.md)</li><li>[File upload schema](file-upload-schema.md)</li><li>[Ingest data](ingest-data.md)</li></ul><br/><br/>[Access and manage orchestrated campaigns](access-manage-orchestrated-campaigns.md)<br/><br/>[Key steps to create an orchestrated campaign](gs-campaign-creation.md)|[Create and schedule the campaign](create-orchestrated-campaign.md)<br/><br/>[Orchestrate activities](orchestrate-activities.md)<br/><br/>[Start and monitor the campaign](start-monitor-campaigns.md)<br/><br/>[Reporting](reporting-campaigns.md)|[Work with the rule builder](orchestrated-rule-builder.md)<br/><br/>[Build your first query](build-query.md)<br/><br/>[Edit expressions](edit-expressions.md)<br/><br/>[Retargeting](retarget.md)|[Get started with activities](activities/about-activities.md)<br/><br/>Activities:<br/>[And-join](activities/and-join.md) - [Build audience](activities/build-audience.md) - [Change dimension](activities/change-dimension.md) - [Channel activities](activities/channels.md) - [Combine](activities/combine.md) - [Deduplication](activities/deduplication.md) - [Enrichment](activities/enrichment.md) - [Fork](activities/fork.md) - [Reconciliation](activities/reconciliation.md) - [Save audience](activities/save-audience.md) - [Split](activities/split.md) - [Wait](activities/wait.md)|

{style="table-layout:fixed"}

+++

</br>

>[!BEGINSHADEBOX]

The content on this page is not final and may be subject to change.

>[!ENDSHADEBOX]

This guide walks you through the process of creating a relational schema, configuring a dataset for orchestrated campaigns, ingesting data via an S3 source, and querying the ingested data in the AP platform.

In this example, the setup includes integrating two key entities, **Loyalty Transactions** and **Loyalty Rewards**, and link them to existing core entities **Recipients** and **Brands**. 

![](assets/do-not-localize/schema_admin.png)

1. [Create relational Schema and associated Dataset](#schema)
    
    Define the relational data model for orchestrated campaigns, including the **Loyalty Memberships**, **Loyalty Transactions** and **Loyalty Rewards** entities, along with required keys and versioning attributes.

1. [Link schema](#link-schema)

    Link the **Loyalty Transactions** entity to **Recipients**, and **Loyalty Rewards** to **Brands**, to build a connected data model that supports personalized customer journeys.

1. [Ingest Data](#ingest)

    Bring data into Adobe Experience Platform from supported sources like SFTP, cloud storage, or databases.


<!--### Setting Up Change data capture ingestion {#cdc-ingestion}

If you need to change the data source, you must delete the existing dataflow and create a new one pointing to the same dataset with the new source.

When using Change Data Capture (CDC), it is essential that the source and dataset remain in sync to ensure accurate incremental updates. Follow the steps below:

1. **Schema Requirements**
   - Your schema must include:
     - A **primary key** (e.g., `transaction_id`)
     - A **versioning field** (e.g., `lastmodified` or an incrementing `version_id`)
   - Enable the dataset for **Orchestrated Campaigns** if needed.

2. **CDC Dataflow Setup**
   - During dataflow creation, after choosing your source and files:
     - **Enable the CDC option**
     - Select your CDC-ready dataset
     - Confirm field mappings (especially version field)

3. **Keep Source and Target in Sync**
   - The source system must consistently update the version field so the platform can detect changes accurately.

Once set up, the platform will automatically ingest **only changed or new records** each time the flow runs.
-->
