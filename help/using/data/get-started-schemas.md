---
solution: Journey Optimizer
product: journey optimizer
title: Get Started with schemas
description: Learn how to use Adobe Experience Platform schemas in Adobe Journey Optimizer
feature: Data Model, Datasets, Data Management
role: Engineer, Admin
level: Experienced
keywords: schemas, platform, data, structure
exl-id: c2a8df2e-ff94-4f9a-a53e-bbf9f663cc81
---
# Get Started with schemas {#schemas-gs}

[!DNL Adobe Journey Optimizer] relies on **Adobe Experience Platform schemas** to describe the structure of data in a consistent and reusable way. A schema provides an abstract definition of a real-world object (such as a person) and outlines what data should be included in each instance of that object (such as name, birthday, and so on). When data is ingested into Experience Platform, it is always structured according to an **XDM schema**. 

## Standard & model-based schemas

There are two types of schemas in Adobe Experience Platform:

* **Standard schemas** are hierarchical schemas that use classes and field groups to capture record or time-series data.  

    A standard schema is composed of:  
    
    * A **class** (which defines the data behavior: record or time-series).
    * One or more **field groups** (which add specific fields to the schema).

    In Journey Optimizer, standard schemas are typically used to represent **individual people and their attributes**, capture **time-series interactions** such as clicks, purchases, or logins, and power **Real-Time Customer Profile** for segmentation and personalization.  

    ➡️ [Learn how to create and configure a standard schema in this video](#video-schema) (video)

* **Model-based schemas** are flat, non-hierarchical schemas that do not use classes or field groups. They are used to capture record data for relational entities and are primarily used in [!DNL Journey Optimizer] **Orchestrated campaigns**.

    Examples of relational entities include:  
    * Bookings, contracts, or subscriptions  
    * Products or catalogs  
    * Stores, locations, or partners  

    With model-based schemas, you can send one message per entity (e.g., per booking, per subscription), create segments based on entity attributes (e.g., product category, store location), and improve addressability by reaching all contacts linked to an entity.  

    How model-based schemas work:

    1. **Create schemas manually or import via DDL**
    1. **Link schemas** to define relationships between entities and people (e.g., loyalty transactions linked to members, rewards linked to brands).  
    1. **Ingest data** into your dataset from supported sources.

    ➡️ [Learn how to manage model-based schemas and datasets](../orchestrated/gs-schemas.md)
    ➡️ [Get started with Orchestrated campaigns](../orchestrated/gs-schemas.md)

## How-to video{#video-schema}

Learn how to create a standard schema, add field groups, create, and configure custom field groups.

>[!VIDEO](https://video.tv.adobe.com/v/334461?quality=12)

>[!MORELIKETHIS]
>
>* [Create a schema, a dataset and ingest data to add Test profiles in Journey Optimizer](../audience/creating-test-profiles.md)
>* [XDM System overview](https://experienceleague.adobe.com/docs/experience-platform/xdm/home.html){target="_blank"}
>* [Best practices for data modeling](https://experienceleague.adobe.com/docs/experience-platform/xdm/schema/best-practices.html){target="_blank"}
>* [Create a schema using the Schema Registry API](https://experienceleague.adobe.com/docs/experience-platform/xdm/tutorials/create-schema-api.html){target="_blank"}
>* [Define a relationship between two schemas using the Schema Editor](https://experienceleague.adobe.com/docs/experience-platform/xdm/tutorials/relationship-ui.html){target="_blank"}
