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
     > The target schema must have a 1:1 relationship with the `Profile` schema. For example, you cannot use `Purchases` as a target schema, since it typically represents a one-to-many relationship.

* **Profile Linkage**
     
     The system must understand how the target schema maps to the `Profile` schema. This is achieved through a shared identity field — one that exists both in the target schema and the `Profile` schema and is configured as an identity namespace.

➡️ [Learn more about relational schemas in Adobe Experience Platform documentation](https://experienceleague.adobe.com/en/docs/experience-platform/xdm/schema/relational#how-relational-schemas-differ-from-standard-xdm-schemas)

## Create your Targeting dimension {#targeting-dimension}

Start by setting up campaign orchestration by mapping a relational schema to the customer profile.

1. From **[!UICONTROL Administration]**, access the **[!UICONTROL Configurations]** menu and select **[!UICONTROL Campaign Target Dimension]**.
     
     ![](assets/target-dimension-1.png)

1. Click **[!UICONTROL Create]** to start creating your **[!UICONTROL Targeting dimension]**.

1. Choose your [previously configured Schema](gs-schemas.md) ​from the drop-down.
     
     While all relational schemas are visible, only schemas with a direct identity relationship to the **Profile** are eligible for selection.

1. Select the **[!UICONTROL Identity value]** that represents the entity you want to target.
     
     In this example, the customer profile is linked to multiple subscriptions, each represented by a unique `crmID` in the `Recipient` schema. By setting the **[!UICONTROL Target Dimension]** to use the `Recipient` schema and its `crmID` identity, you can send messages at the subscription level, rather than to the main customer profile, ensuring each contract or line receives its own personalized message.

     [Learn more in Adobe Experience Platform documentation](https://experienceleague.adobe.com/en/docs/experience-platform/xdm/schema/composition#identity)

     ![](assets/target-dimension-2.png)

1. Click **[!UICONTROL Save]** to complete the setup. Note that once created, a **[!UICONTROL Target dimension]** cannot be removed or edited. 

After configuring the **[!UICONTROL Target Dimension]**, proceed to create and set up your **[!UICONTROL Channel Configuration]** and define the corresponding **[!UICONTROL Execution Details]**.