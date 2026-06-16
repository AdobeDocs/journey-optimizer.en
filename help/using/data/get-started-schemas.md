---
solution: Journey Optimizer
product: journey optimizer
title: Get Started with schemas
description: Learn how to use Adobe Experience Platform schemas in Adobe Journey Optimizer
feature: Data Model, Datasets, Data Management
role: Developer, Admin
level: Experienced
keywords: schemas, platform, data, structure
exl-id: c2a8df2e-ff94-4f9a-a53e-bbf9f663cc81
TQID: https://experienceleague.adobe.com/fWsW9Rvyd8L4nphczzc7GF1rbO7HuYsjqDBBpy3uoGU
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: aeebb91a-f216-4d5f-8da1-3a7e6f696ed0
    internal-label: Data management activity
subfeature_v2:
  - id: b3a93754-a8b8-46eb-9421-7eccaeeb3dff
    internal-label: Best practices
  - id: a1cdc218-59b7-4eef-b5cf-2a7ad74b3371
    internal-label: Journey Optimizer schemas
  - id: d6e5c7fd-c1d6-4137-98cd-138ccde6752f
    internal-label: Datasets
  - id: cf3fbcd7-c075-4ae4-8de5-96e736ab2ea3
    internal-label: Data ingestions
  - id: e30b0a1a-b594-47b8-af94-1e3a2be6df11
    internal-label: Get started
role_v2:
  - id: c66ffd68-0f65-42bb-aa23-b4020f12e0bd
    internal-label: Admin
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
topic_v2:
  - id: b23e006f-0a29-4f1d-8fd0-77aa56f3d12b
    internal-label: Data modeling
  - id: e0eb8757-182f-49f3-94a4-1587d16f5094
    internal-label: Personalization
  - id: ebde5b41-29c9-4f5e-9ef6-1197e85409e3
    internal-label: Data management
---
# Get Started with schemas {#schemas-gs}

>[!BEGINSHADEBOX]

**On this page:** Understand how Adobe Experience Platform standard and relational schemas define the structure of your data so you can model profiles, behavioral events, and relational entities for personalization and orchestrated campaigns in Adobe Journey Optimizer.

>[!ENDSHADEBOX]

[!DNL Adobe Journey Optimizer] relies on **Adobe Experience Platform schemas** to describe the structure of data in a consistent and reusable way. A schema provides an abstract definition of a real-world object (such as a person) and outlines what data should be included in each instance of that object (such as name, birthday, and so on). When data is ingested into Experience Platform, it is always structured according to an **XDM schema**. 

## Standard & relational schemas

There are two types of schemas in Adobe Experience Platform:

* **Standard schemas** are hierarchical schemas that use classes and field groups to capture record or time-series data.  

    A standard schema is composed of:  
    
    * A **class** (which defines the data behavior: record or time-series).
    * One or more **field groups** (which add specific fields to the schema).

    In Journey Optimizer, standard schemas are typically used to represent **individual people and their attributes**, capture **time-series interactions** such as clicks, purchases, or logins, and power **Real-Time Customer Profile** for segmentation and personalization.  

    ➡️ [Learn how to create and configure a standard schema in this video](#video-schema) (video)

* **Relational schemas** are flat, non-hierarchical schemas that do not use classes or field groups. They are used to capture record data for relational entities and are primarily used in [!DNL Journey Optimizer] **Orchestrated campaigns**.

    Examples of relational entities include:  
    * Bookings, contracts, or subscriptions  
    * Products or catalogs  
    * Stores, locations, or partners  

    With relational schemas, you can send one message per entity (e.g., per booking, per subscription), create segments based on entity attributes (e.g., product category, store location), and improve addressability by reaching all contacts linked to an entity.  

    How relational schemas work:

    1. **Create schemas manually or import via DDL**
    1. **Link schemas** to define relationships between entities and people (e.g., loyalty transactions linked to members, rewards linked to brands).  
    1. **Ingest data** into your dataset from supported sources.

    ➡️ [Learn how to manage relational schemas and datasets](../orchestrated/gs-schemas.md)
    ➡️ [Get started with Orchestrated campaigns](../orchestrated/gs-schemas.md)

## How-to video{#video-schema}

Learn how to create a standard schema, add field groups, create, and configure custom field groups.

>[!VIDEO](https://video.tv.adobe.com/v/334461?quality=12)

>[!MORELIKETHIS]
>
>* [Get started with data management in Journey Optimizer](gs-data.md)
>* [Create a schema, a dataset and ingest data to add Test profiles in Journey Optimizer](../audience/creating-test-profiles.md)
>* [XDM System overview](https://experienceleague.adobe.com/docs/experience-platform/xdm/home.html){target="_blank"}
>* [Best practices for data modeling](https://experienceleague.adobe.com/docs/experience-platform/xdm/schema/best-practices.html){target="_blank"}
>* [Create a schema using the Schema Registry API](https://experienceleague.adobe.com/docs/experience-platform/xdm/tutorials/create-schema-api.html){target="_blank"}
>* [Define a relationship between two schemas using the Schema Editor](https://experienceleague.adobe.com/docs/experience-platform/xdm/tutorials/relationship-ui.html){target="_blank"}
