---
solution: Journey Optimizer
product: journey optimizer
title: Use the Change dimension activity
description: Learn how to use the Change dimension activity
hide: yes
hidefromtoc: yes
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

The **Change dimension** activity is a **Targeting** activity. This activity allows you to change the targeting dimension as you are building your multi-step campaign. It shifts the axis depending on the data template and the input dimension. [Learn more on targeting dimensions](../../audience/about-recipients.md#targeting-dimensions)

For example, you can switch a multi-step campaign's targeting dimension from "Recipients" to "Subscribers application" in order to send push notifications to the targeted recipients.

>[!IMPORTANT]
>
>Please note that the **[!UICONTROL Change Dimension]** and **[!UICONTROL Change Data source]** activities should not be added in one row. If you need to use both activities consecutively, make sure you include an **[!UICONTROL Enrichement]** activity in between them. This ensures proper execution and prevents potential conflicts or errors.

## Configure the Change dimension activity {#configure}

Follow these steps to configure the **Change dimension** activity:

1. Add a **Change dimension** activity to your multi-step campaign.

   ![](../assets/workflow-change-dimension.png)

1. Define the **New target dimension**. During dimension change, all records are kept. Other options are not available yet. 

1. Execute the multi-step campaign to view the result. Compare the data in the tables before and after the change dimension activity, and compare the structure of the multi-step campaign tables.

## Example {#example}

In this example, we want to send an SMS delivery to all the profiles who have made a purchase. To do this, we first use a **[!UICONTROL Build audience]** activity linked to a custom "Purchase" targeting dimension to target all purchases that occurred.

We then use a **[!UICONTROL Change dimension]** activity to switch the multi-step campaign targeting dimension to "Recipients". This allows us to be able to target the recipients who match the query.

![](../assets/workflow-change-dimension-example.png)
