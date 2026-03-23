---
solution: Journey Optimizer
product: journey optimizer
title: Use the Change dimension activity
description: Learn how to use the Change dimension activity
exl-id: 83e66f10-93dd-4759-840c-2c83abc42a28
version: Campaign Orchestration
---

# Change dimension {#change-dimension}

>[!CONTEXTUALHELP]
>id="ajo_orchestration_dimension_complement"
>title="Generate a complement"
>abstract="You can generate an additional outbound transition with the remaining population, which was excluded as a duplicate. To do this, toggle on the **Generate complement** option"

>[!CONTEXTUALHELP]
>id="ajo_orchestration_change_dimension"
>title="Change dimension activity"
>abstract="This activity allows you to change the targeting dimension as you are building an audience. It shifts the axis depending on the data template and the input dimension. For example, you can switch from the "contracts" dimension to the "clients" dimension."

As a marketer, you can enhance audience targeting by shifting from one data entity to a related one within an Orchestrated campaign. This enables you to move beyond user profiles and focus on specific behaviors, such as purchases, bookings, or other interactions.

To achieve this, use the **[!UICONTROL Change dimension]** activity. It allows you to adjust the targeting dimension during the Orchestrated campaign.

>[!NOTE]
>
>For many **multi-entity** scenarios, an explicit **[!UICONTROL Change dimension]** is optional. When the relationship path allows it, you can connect a **[!UICONTROL Build audience]** activity directly to a channel activity and set the **[!UICONTROL One message per secondary dimension]** option. See [Add a channel activity and define its properties](channels.md#add).  The product can infer viable primary and **secondary** dimensions from targetable schemas linked to your query. Add **[!UICONTROL Change dimension]** when you need a deliberate switch of axis in the workflow.

<!--
>[!IMPORTANT]
>
>Please note that the **[!UICONTROL Change Dimension]** and **[!UICONTROL Change Data source]** activities should not be added in one row. If you need to use both activities consecutively, make sure you include an **[!UICONTROL Enrichement]** activity in between them. This ensures proper execution and prevents potential conflicts or errors.-->

## Configure the Change dimension activity {#configure}

Follow these steps to configure the **[!UICONTROL Change dimension]** activity:

1. Add a **[!UICONTROL Change dimension]** activity to your Orchestrated campaign.

   ![](../assets/orchestrated-change-dimension.png)

1. Define the **[!UICONTROL New target dimension]**. During dimension change, all records are kept.

## Example {#example}

This use case focuses on sending an SMS to profiles who have created a wishlist within the past month.

Begin with a **[!UICONTROL Build audience]** activity, using the **[!UICONTROL Wishlist]** targeting dimension to identify all relevant wishlists.

Then, add a **[!UICONTROL Change dimension]** activity to switch the targeting dimension from **[!UICONTROL Wishlist]** to **[!UICONTROL Recipient].** This step ensures the Orchestrated campaign targets the correct profiles linked to those wishlists, allowing the SMS to be sent to the intended profiles.

![](../assets/orchestrated-change-dimension-example.png)
