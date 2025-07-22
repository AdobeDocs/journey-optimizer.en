---
solution: Journey Optimizer
product: journey optimizer
title: Configuration steps
description: Learn how to create a relational schema within Adobe Experience Platform by uploading a DDL
badge: label="Alpha"
hide: yes
hidefromtoc: yes
exl-id: 327597f6-8a53-42dc-966a-baae49b58bb3
---
# Get started with Schemas and Datasets{#gs-schemas}

+++ Table of Contents

| Welcome to orchestrated campaigns | Launch your first orchestrated campaign | Query the database | Ochestrated campaigns activities|
|---|---|---|---|
|[Get started with orchestrated campaigns](gs-orchestrated-campaigns.md)<br/><br/>Create and manage relational Schemas and Datasets:</br> <ul><li>[Get started with Schemas and Datasets](gs-schemas.md)</li><li>[Manual schema](manual-schema.md)</li><li>[File upload schema](file-upload-schema.md)</li><li>[Ingest data](ingest-data.md)</li></ul>[Access and manage orchestrated campaigns](access-manage-orchestrated-campaigns.md)<br/><br/>[Key steps to create an orchestrated campaign](gs-campaign-creation.md)|[Create and schedule the campaign](create-orchestrated-campaign.md)<br/><br/>[Orchestrate activities](orchestrate-activities.md)<br/><br/>[Start and monitor the campaign](start-monitor-campaigns.md)<br/><br/>[Reporting](reporting-campaigns.md)|[Work with the rule builder](orchestrated-rule-builder.md)<br/><br/>[Build your first query](build-query.md)<br/><br/>[Edit expressions](edit-expressions.md)<br/><br/>[Retargeting](retarget.md)|[Get started with activities](activities/about-activities.md)<br/><br/>Activities:<br/>[And-join](activities/and-join.md) - [Build audience](activities/build-audience.md) - [Change dimension](activities/change-dimension.md) - [Channel activities](activities/channels.md) - [Combine](activities/combine.md) - [Deduplication](activities/deduplication.md) - [Enrichment](activities/enrichment.md) - [Fork](activities/fork.md) - [Reconciliation](activities/reconciliation.md) - [Save audience](activities/save-audience.md) - [Split](activities/split.md) - [Wait](activities/wait.md)|

{style="table-layout:fixed"}

+++

</br>

>[!BEGINSHADEBOX]

</br>

The content on this page is not final and may be subject to change.

>[!ENDSHADEBOX]

This guide walks you through the process of creating a relational schema, configuring a dataset for orchestrated campaigns and ingesting data.

![](assets/do-not-localize/schema_admin.png)

1. Create [relational schema manually](manual-schema.md) or [using a DDL file](file-upload-schema.md)

    Define the structure of your data model, including tables, attributes, and relationships. Choose to build the schema manually in the user interface or upload a DDL file for faster setup.

1. [Link schema](file-upload-md)

    stablish relationships between your schemas to ensure data consistency and enable cross-entity queries. For example, link loyalty transactions to recipients or rewards to brands.

1. [Ingest Data](ingest-data.md)

    Bring data into Adobe Experience Platform from supported sources such as SFTP, cloud storage, or databases.

