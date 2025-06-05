---
solution: Journey Optimizer
product: journey optimizer
title: Configuration steps
description: Learn how to configure orchestrated campaigns with Adobe Journey Optimizer.
badge: label="Alpha"
hide: yes
hidefromtoc: yes
exl-id: 8c785431-9a00-46b8-ba54-54a10e288141
---
# Configuration steps {#configuration-steps}

+++ Table of Contents

| Welcome to orchestrated campaigns | Launch your first orchestrated campaign | Query the database | Ochestrated campaigns activities|
|---|---|---|---|
|[Get started with orchestrated campaigns](gs-orchestrated-campaigns.md)<br/><br/>[Configuration steps](configuration-steps.md)<br/><br/>[Key steps for orchestrated campaign creation](gs-campaign-creation.md)|[Create an orchestrated campaign](create-orchestrated-campaign.md)<br/><br/>[Orchestrate activities](orchestrate-activities.md)<br/><br/>[Send messages with orchestrated campaigns](send-messages.md)<br/><br/>[Start and monitor the campaign](start-monitor-campaigns.md)<br/><br/>[Reporting](reporting-campaigns.md)|[Work with the rule builder](orchestrated-rule-builder.md)<br/><br/>[Build your first query](build-query.md)<br/><br/>[Edit expressions](edit-expressions.md)|[Get started with activities](activities/about-activities.md)<br/><br/>Activities:<br/>[And-join](activities/and-join.md) - [Build audience](activities/build-audience.md) - [Change dimension](activities/change-dimension.md) - [Combine](activities/combine.md) - [Deduplication](activities/deduplication.md) - [Enrichment](activities/enrichment.md) - [Fork](activities/fork.md) - [Reconciliation](activities/reconciliation.md) - [Split](activities/split.md) -  [Wait](activities/wait.md)|

{style="table-layout:fixed"}

+++

</br>

>[!BEGINSHADEBOX]

Documentation in progress

>[!ENDSHADEBOX]


<!--
This guide walks you through the process of creating a relational schema, configuring a dataset for orchestrated campaigns, ingesting data via an S3 source, and querying the ingested data in the AP platform. Each step is explained in detail with emphasis on why it is important.


You have now:

- Created a relational schema
- Configured a CDC-enabled dataset
- Ingested data via S3
- Scheduled and monitored a data flow
- Queried the ingested data

This setup is essential for running orchestrated AGO campaigns effectively and ensuring timely, accurate data synchronization.

## Create a relational schema / (-) Upload DDL file 

1. Log in to the AP Platform.

1. Navigate to the **Data Management** section > **Schema**.

1. Click on **Create Schema**.

1. You will be prompted to select between two schema types:

    * **Standard**

    * **Relational**, used specifically for orchestrated campaigns

    ![](assets/admin_schema_1.png)

1. Select **Upload DDL file** to define an entity relationship diagram and create schemas.

1. Drag and drop your DDL file and click Next.

1. Configure each schema and its columns. 

1. Type-in your Schema name and click Done.

    ![](assets/admin_schema_2.png)

1. 


A standard SQL, DDL file (create table statements wwith relationships and constraints as applicable)

Customers typically export these from their data warehouses or operational databases.

value: fast track E2E buld schema creation
reduces manual effort significantly

Once the file is imported, the system should create entities, attributes and relations as per specified in the file 

Once imported the users must get an option to select what all entity tables to be brought in
For each entity table, the user must be able to select what all fields need to be added/ removed

As a user, I should be able to indicate which entity corresponds to the "Targetable entity" so that the targetting can happen on this entity. Subsequently there should be validations that there should only be single targetable entity (Only in MVP). Later we plan to bring the concept of change dimension and make multiple entities targetable 

As a user, I should be able to modify the field names, indicate which field is the primary key or create a primary key as a combination of multiple fields (composite keys), mandatory/ optional
It should be mandatory to mark a field as primary key or create primary key as a composite key (if it does not exist). There should also be validations to ensure that there is only one primary key/ entity. 
The fields with unsupported datatypes like maps arrays should be flagged for the user to take action - map to a different datatype; drop the fields
As a user, I should able to indicate some fields as invisible so that they are not visible to marketer for journeys to make the UX simpler (refer FAC)
Once the changes are done, the user should be able to save the changes and start visualizing the brought in entities in an ERD canvas
On saving there should be validations so that the unsupported datatypes like maps arrays should not be included or any other validations; unique primary keys exist. If there are any errors, the errors should be reported back to the user to make changes
The work done should not be lost and as a user, I should be able to pick up where I started

## Select entities

To create links between tables of your datamodel from the Canvas view tab, follow these steps:

1. Access the Canvas view of your data model and choose the two tables you want to link

1. Click the ![](assets/do-not-localize/Smock_AddCircle_18_N.svg) button next to the Source Join, then drag and guide the arrow towards the Target Join to establish the connection.

1. Fill in the given form to define the link and click **Apply** once configured.

    ![](assets/admin_schema_3.png)

    **Cardinality**:

    * **1-N**: one occurrence of the source table can have several corresponding occurrences of the target table, but one occurrence of the target table can have at most one corresponding occurrence of the source table.

    * **N-1**: one occurrence of the target table can have several corresponding occurrences of the source table, but one occurrence of the source table can have at most one corresponding occurrence of the target table.

    * **1-1**: one occurrence of the source table can have at most one corresponding occurrence of the target table.

1. All links defined in your data model are represented as arrows in the canvas view. Click on an arrow between two tables to view details, make edits, or remove the link as needed.

1. Use the toolbar to customize and adjust your canvas.

    * **Zoom in**: Magnify the canvas to see details of your data model more clearly.

    * **Zoom out**: Reduce the canvas size for a broader view of your data model.

    * **Fit view**: Adjust the zoom to fit all schemas and/or audiences within the visible area.

    * **Toggle interactivity**: Enable or disable user interaction with the canvas.

    * **Filter**: Choose which schema to display within the canvas.

    * **Force auto layout**: Automatically arrange schemas and/or audiences for better organization.

1. Click **Save** once done.

Doc AEP: https://experienceleague.adobe.com/en/docs/experience-platform/xdm/tutorials/create-schema-ui

## Add data

1. Set up

1. Connect existing or new account

1. Select dataset fields

1. Map desired source fields to target dataset fields

1. 

## Set up sources

Adobe Experience Platform allows data to be ingested from external sources while providing you with the ability to structure, label, and enhance incoming data using Experience Platform services. You can ingest data from a variety of sources such as Adobe applications, cloud-based storages, databases, and many others.

6 sources compatible avec data relationel, tout ce qui est fichier (data storage), SFTP, azure blob, amazon S3, database cloud snowflake, 


![](assets/admin_sources_1.png)

https://experienceleague.adobe.com/en/docs/experience-platform/sources/ui-tutorials/create/local-system/local-file-upload


## Create datasets






## Relational 

## Create a relational schema / (-) Upload DDL file 


1. Log in to the AP Platform.
1. Navigate to the **Schema Management** section.
1. Click on **Create Schema**.

1. You will be prompted to select between two schema types:
    * **Standard**
    * **Relational** (used specifically for AGO campaigns)

1. Click on **Create Manual**.
1. Provide a **Schema Name** (e.g., `test_demo_ck001`).
1. Choose **Schema Type**:
    - **Record Type** (required for AGO campaigns)
    - **Time Series** (not applicable here)
1. Click **Finish** to proceed to the schema design canvas.

## Select entities and fields to import

1. In the canvas, add attributes (fields) to your schema.
1. Add a **Primary Key** (mandatory).
1. Add a **Version Descriptor** attribute (for CDC support):
    - This must be of type **DateTime** or **Numeric** (Integer, Long, Short, Byte).
    - Common example: `last_modified`

> **Why?** The **Primary Key** uniquely identifies each record, and the **Version Descriptor** tracks changes, supporting CDC (Change Data Capture) and data mirroring.

1. Mark the appropriate fields as **Primary Key** and **Version Descriptor**.
1. Click **Save**.

---




## 5. Creating a Dataset

1. Navigate to **Datasets**.
1. Click on **Create Dataset**.
1. Select the schema you just created.
1. Assign a **Dataset Name** (same as schema is fine).
1. Optionally, add tags (e.g., `AGO_campaigns`).
6. Ensure the checkbox **"Relational Schema"** is checked.
7. Click **Finish**.

> **Note:** Only one dataset can be created per relational schema.


## 6. Enabling the Dataset

1. Click **Enable** for the dataset.
1. Wait a few moments for the status to show **Enabled**.

> **Why?** Without enabling, the dataset cannot be used in orchestrated campaigns or ingest data.

## 7. Creating a Data Source (S3)

1. Navigate to **Sources**.
1. Click **Create Source**.
1. Choose the source type (e.g., **S3 Bucket**).
1. Provide connection details:
    - Bucket Path (optionally include subfolder path)
1. Save the source.

## 8. Preparing and Uploading Data

1. Prepare your CSV file with:
    - Column headers matching your schema attributes
    - `last_modified` column
    - `change_type` column (`U`/`DU` for upsert, `D` for delete)

> **Important:** `change_type` is required but does not need to be defined in the schema.

1. Save the file as `.csv`.

1. Upload the file to the specified folder in your S3 bucket.


## 9. Ingesting Data from S3

1. Go to **Sources** and find your S3 source.
1. Click **Add Data**.
1. Select the uploaded file.
1. Specify the file format as **CSV** and any compression type if applicable.
1. Review the data preview (ensure `change_type`, `last_modified`, and primary key are visible).
1. Click **Next**.

### Enable Change Data Capture (CDC)

- Check **Enable Change Data Capture**.
- Select the dataset enabled for AGO campaigns.

### Field Mapping

- Fields are auto-mapped (note that `change_type` is not mapped and that's expected).
- Click **Next**.

### Scheduling

- Schedule ingestion frequency (minute, hour, day, week).
- Set start time (immediate or future).
- Click **Finish** to create the data flow.

## 10. Monitoring Data Flow

1. Navigate back to **Sources > Data Flows**.
1. Wait 4–5 minutes for the first run (initial overhead).
1. Monitor:
    - Status (Started, Completed)
    - Number of records ingested
    - Errors (if any)

> **Tip:** Ingested data first lands in the **Data Lake**.

## 11. Data Replication to Data Store

The **Data Store** is updated:

- Every **15 minutes**, or

- If **Data Lake size exceeds 5MB**

This is a background replication process.


## 12. Querying the Dataset

1. Navigate to **Query Services**.
1. Click **Create Query**.
1. Example query:

   ```sql
   SELECT * FROM test_demo_ck001;
   ```

1. Run the query.

> **Note:** If ingestion is incomplete, query will return an error. Check data flow status.



-->