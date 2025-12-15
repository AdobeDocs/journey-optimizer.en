---
solution: Journey Optimizer
product: journey optimizer
title: Create your Targeting dimension
description: Learn how to mapp a relational schema to the customer profile
exl-id: 2479c109-cd6f-407e-8a53-77e4477dc36f
version: Campaign Orchestration
---

# Configure a Targeting dimension {#configuration}

With **[!UICONTROL Orchestrated Campaigns]**, you can design and deliver targeted communications at the entity level, leveraging Adobe Experience Platform's relational schema capabilities. Experience Platform uses schemas to describe the structure of data in a consistent and reusable way. When data is ingested into Experience Platform, it is structured according to an XDM schema.

Although segmentation for **[!UICONTROL Orchestrated Campaigns]** operates primarily on relational schemas, the actual message delivery always occurs at the **Profile** level.

When configuring targeting, you define two key aspects:

* **Targetable Schemas**
     
     You specify which relational schemas are eligible for targeting. By default, the schema named `Recipient` is used, but you can configure alternatives such as `Visitors`, `Customers`, etc.

     >[!IMPORTANT]
     >
     > Orchestrated Campaigns allow targeting on any schema that has a direct or related relationship to the **Profile** schema. While its usage is primarily intended on 1:1 relationships, it also supports 1:N relationships, such as Account `>` Recipients, as long as the relationship path is properly modeled in the data model. This enables targeting based on account-level data while still resolving the correct profile identity for message delivery.

* **Profile Linkage**
     
     The system must understand how the target schema maps to the `Profile` schema. This is achieved through a shared identity field — one that exists both in the target schema and the `Profile` schema and is configured as an identity namespace.

➡️ [Learn more about relational schemas in Adobe Experience Platform documentation](https://experienceleague.adobe.com/en/docs/experience-platform/xdm/schema/relational#how-relational-schemas-differ-from-standard-xdm-schemas)

## Create your Targeting dimension {#targeting-dimension}

Start by setting up campaign orchestration by mapping a relational schema to the customer profile.

1. From **[!UICONTROL Administration]**, access the **[!UICONTROL Configurations]** menu and select **[!UICONTROL Campaign Target Dimension]**.
     
     ![](assets/target-dimension-1.png)

1. Click **[!UICONTROL Create]** to start creating your **[!UICONTROL Targeting dimension]**.

1. Choose your [previously configured Schema](gs-schemas.md) ​from the drop-down.
     
     While all relational schemas are displayed, only those with a direct identity relationship to **Profile** are eligible for selection. Avoid choosing non-people schemas, e.g purchases, and select a schema that is directly associated with a profile.

1. Select the **[!UICONTROL Identity value]** that represents the entity you want to target.
     
     In this example, the customer profile is linked to multiple subscriptions, each represented by a unique `crmID` in the `Recipient` schema. By setting the **[!UICONTROL Target Dimension]** to use the `Recipient` schema and its `crmID` identity, you can send messages at the subscription level, rather than to the main customer profile, ensuring each contract or line receives its own personalized message.

     [Learn more in Adobe Experience Platform documentation](https://experienceleague.adobe.com/en/docs/experience-platform/xdm/schema/composition#identity)

     ![](assets/target-dimension-2.png)

1. Click **[!UICONTROL Save]** to complete the setup. Note that once created, a **[!UICONTROL Target dimension]** cannot be removed or edited. 

After configuring the **[!UICONTROL Target Dimension]**, proceed to create and set up your **[!UICONTROL Channel Configuration]** and define the corresponding **[!UICONTROL Execution Details]**.