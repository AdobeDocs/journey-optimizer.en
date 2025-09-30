---
solution: Journey Optimizer
product: journey optimizer
title: Configuration steps
description: Learn how to create a model-based schema within Adobe Experience Platform by uploading a DDL
exl-id: 88eb1438-0fe5-4a19-bfb6-2968a427e9e8
version: Campaign Orchestration
---

# Create model-based schemas using a DDL file {#file-upload-schema}

Define the model-based data model required for Orchestrated campaigns by creating schemas such as **Loyalty Memberships**, **Loyalty Transactions**, and **Loyalty Rewards**. Each schema must include a primary key, a versioning attribute, and appropriate relationships to reference entities such as **Recipients** or **Brands**.

Schemas can be created manually through the interface or imported in bulk using a DDL file.

This section provides step-by-step guidance on how to create a model-based schema within Adobe Experience Platform by uploading a DDL (Data Definition Language) file. Using a DDL file allows you to define the structure of your data model in advance, including tables, attributes, keys, and relationships. 

1. [Upload a DDL file](#ddl-upload) to create model-based schemas and define their structure.

1. [Define relationships](#relationships) between tables in your data model.

1. [Link schemas](#link-schema) to connect your model-based data with existing profile entities such as Recipients or Brands.

1. [Ingest data](ingest-data.md) into your dataset from supported sources.

➡️ [Learn more about model-based schemas in Adobe Experience Platform documentation](https://experienceleague.adobe.com/en/docs/experience-platform/xdm/schema/model-based)

## Upload a DDL file{#ddl-upload}

By uploading a DDL file, you can define the structure of your data model in advance, including tables, attributes, keys, and relationships. 

Excel-based schema file uploads are supported. Download the [provided template](assets/template.zip) to easily prepare your schema definitions.

+++The following features are supported when creating model-based schemas in Adobe Experience Platform

* **ENUM**  
  ENUM fields are supported in both DDL-based and manual schema creation, allowing you to define attributes with a fixed set of allowed values.
    Here is an example: 

    ```
    CREATE TABLE orders (
    order_id     INT NOT NULL,
    product_id   INT NOT NULL,
    order_date   DATE NOT NULL,
    customer_id  INT NOT NULL,
    quantity     INT NOT NULL,
    order_status enum ('PENDING', 'SHIPPED', 'DELIVERED', 'CANCELLED'),
    PRIMARY KEY (order_id, product_id)
    );
    ```

* **Schema Label for Data Governance**  
  Labeling is supported at the schema field level to enforce data governance policies such as access control and usage restrictions. For more details, refer to [Adobe Experience Platform documentation](https://experienceleague.adobe.com/docs/experience-platform/xdm/home.html).

* **Composite Key**  
  Composite primary keys are supported in model-based schema definitions, enabling the use of multiple fields together to uniquely identify records.

+++

1. Log in to Adobe Experience Platform.

1. Navigate to the **Data Management** > **Schema** menu.

1. Click **Create Schema**.

1. Select **[!UICONTROL Model-based]** as your **Schema type**.

    ![](assets/admin_schema_1.png)

1. Select **[!UICONTROL Upload DDL file]** to define an entity relationship diagram and create schemas.

    The table structure must contain:
    * At least one primary key.
    * A version identifier, such as a `lastmodified` field of type `datetime` or `number`.
    * For Change Data Capture (CDC) ingestion, a special column named `_change_request_type` of type `String`, which indicates the type of data change (e.g., insert, update, delete) and enables incremental processing.  
    * DDL file must not define more than 200 tables.


    >[!IMPORTANT]
    >
    > Any schema used for targeting must include at least one identity field of type `String` with an associated **identity namespace**.  
    >This ensures compatibility with Adobe Journey Optimizer's targeting and identity resolution capabilities.

1. Drag and drop your DDL file and click **[!UICONTROL Next]**.

    Note that the maximum supported size for a DDL file is 10MB.

1. Type-in your **[!UICONTROL Schema name]**.

1. Set up each schema and its columns, ensuring that a primary key and a version descriptor are specified. 

    One attribute, such as `lastmodified`, must be designated as the version descriptor (type  `datetime`, `long`, or `int`) to ensure datasets are updated with the latest data. Users can change the version descriptor, which becomes mandatory once set. An attribute cannot be both a primary key (PK) and a version descriptor.

    ![](assets/admin_schema_2.png)

1. Mark an attribute as `identity` and map it to a defined identity namespace.

1. Rename, delete, or add a description to each table.

1. Click **[!UICONTROL Done]** once done.

You can now verify the table and field definitions within the canvas. [Learn more in the section below](#entities)

## Define relationships {#relationships}

You can specify relationships directly within the DDL file when creating your schema. If you prefer to define relationships outside of the file, you can do so in the interface by following the steps below.

1. Access the canvas view of your data model and choose the two tables you want to link

1. Click the ![](assets/do-not-localize/Smock_AddCircle_18_N.svg) button next to the Source Join, then drag and guide the arrow towards the Target Join to establish the connection.

    >[!NOTE]
    >
    >Composite keys are supported if defined in the DDL file.

    ![](assets/admin_schema_5.png)

1. Fill in the given form to define the link and click **Apply** once configured.

    ![](assets/admin_schema_3.png)

    **Cardinality**:

     * **1-N**: one occurrence of the source table can have several corresponding occurrences of the target table, but one occurrence of the target table can have at most one corresponding occurrence of the source table.

    * **N-1**: one occurrence of the target table can have several corresponding occurrences of the source table, but one occurrence of the source table can have at most one corresponding occurrence of the target table.

    * **1-1**: one occurrence of the source table can have at most one corresponding occurrence of the target table.

1. All links defined in your data model are represented as arrows in the canvas view. Click on an arrow between two tables to view details, make edits, or remove the link as needed.

    ![](assets/admin_schema_6.png)

1. Use the toolbar to customize and adjust your canvas.

    ![](assets/toolbar.png)

    * **Zoom in**: Magnify the canvas to see details of your data model more clearly.

    * **Zoom out**: Reduce the canvas size for a broader view of your data model.

    * **Fit view**: Adjust the zoom to fit all schemas within the visible area.

    * **Filter**: Choose which schema to display within the canvas.

    * **Force auto layout**: Automatically arrange schemas for better organization.

    * **Display map**: Toggle a minimap overlay to help navigate large or complex schema layouts more easily.

1. Click **Save** once done. This action creates the schemas and associated data sets and enables the data set for use in Orchestrated Campaigns.

1. Click **[!UICONTROL Open Jobs]** to monitor the progress of the creation job. This process may take couple minutes, depending on the number of tables defined in the DDL file. 

    You can also access your DDL import jobs by opening the **[!UICONTROL Upload DDL file]** window and select **[!UICONTROL View all DDL import jobs]**.

    ![](assets/admin_schema_4.png)

## Link schemas {#link-schema}

>[!IMPORTANT]
>
> Only relationships explicitly defined within the DDL file are recognized by the system. Any entity relationships that exist outside of the DDL file will be ignored and not processed.

Establish a relationship between the **loyalty transactions** schema and the **Recipients** schema to associate each transaction with the correct customer record.

1. Navigate to **[!UICONTROL Schemas]** and open your previously create **loyalty transactions**.

1. Click **[!UICONTROL Add Relationship]** from the Customer **[!UICONTROL Field properties]**.

    ![](assets/schema_1.png)

1. Select **[!UICONTROL Many-to-One]** as the relationship **[!UICONTROL Type]**.

1. Link to the existing **Recipients** schema.

    ![](assets/schema_2.png)

1. Enter a **[!UICONTROL Relationship name from current schema]** and **[!UICONTROL Relationship name from reference schema]**.

1. Click **[!UICONTROL Apply]** to save your changes.

Continue by creating a relationship between the **loyalty rewards** schema and the **Brands** schema to associate each reward entry with the appropriate brand.

![](assets/schema_3.png)
