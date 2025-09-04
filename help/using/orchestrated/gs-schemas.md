---
solution: Journey Optimizer
product: journey optimizer
title: Configuration steps
description: Learn how to create a relational schema within Adobe Experience Platform by uploading a DDL
exl-id: 327597f6-8a53-42dc-966a-baae49b58bb3
version: Campaign Orchestration
---

# Get started with Relational Schemas and Datasets{#gs-schemas}

This guide walks you through the process of creating a relational schema, configuring a dataset for Orchestrated campaigns and ingesting data.

![](assets/do-not-localize/schema_admin.png)

A dataset is a storage and management construct for a collection of data, typically a table, that contains a schema (columns) and fields (rows). Data that is successfully ingested into Experience Platform is stored within the data lake as datasets. 

A schema represents and validates the structure and format of data. It provides an abstract definition of a real-world object (such as a person) and outlines what data should be included in each instance of that object (such as name, birthday, and so on).


1. Create [relational schema manually](manual-schema.md) or [using a DDL file](file-upload-schema.md)

    Define the structure of your data model, including tables, attributes, and relationships. Choose to build the schema manually in the user interface or upload a DDL file for faster setup.

    When creating the schema manually, dataset must also be created and enabled manually. Wehn using a DDL file, dataset creation and enablement are automatic.

1. [Link schema](file-upload-schema.md)

    Establish relationships between your schemas to ensure data consistency and enable cross-entity queries. For example, link loyalty transactions to recipients or rewards to brands.

1. [Ingest Data](ingest-data.md)

    Bring data into Adobe Experience Platform from supported sources such as SFTP, cloud storage, or databases.

