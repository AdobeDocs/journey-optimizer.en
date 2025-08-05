---
solution: Journey Optimizer
product: journey optimizer
title: Use the Save audience activity
description: Learn how to use the Save audience activity in an Orchestrated campaign
exl-id: 7b5b03ba-fbb1-4916-8c72-10778752d8e4
---

# Save audience {#save-audience}

>[!CONTEXTUALHELP]
>id="ajo_orchestration_save_audience"
>title="Save audience activity"
>abstract="The **Save audience** activity is a **Targeting** activity that allows you to update an existing audience or create a new one from the population generated earlier in the Orchestrated campaign. Once created, these audiences are added to the list of application audiences and can be accessed from the **Audiences** menu." 

The **[!UICONTROL Save audience]** activity is a **[!UICONTROL Targeting]** activity used to create a new audience or update an existing one based on the population generated earlier in the Orchestrated campaign. Once saved, the audience is added to the list of application audiences and becomes accessible from the **[!UICONTROL Audiences]** menu.

It is commonly used to capture audience segments built within the same campaign workflow, making them available for reuse in future campaigns. Typically, it is connected to other targeting activities, such as **[!UICONTROL Build audience]** or **[!UICONTROL Combine]**, to save the final targeted population. 
Note that with the **[!UICONTROL Save audience]** activity you cannot update an existing audience. You can only create a new audience or overwrite an existing one with a new definition.

## Configure the Save audience activity {#save-audience-configuration}

Follow these steps to configure the **[!UICONTROL Save audience]** activity:

1. Add a **[!UICONTROL Save audience]** activity to your Orchestrated campaign.

1. Enter a **[!UICONTROL Audience label]** that will identify the saved audience.

    >[!NOTE]
    >
    >The audience **[!UICONTROL Label]** must be unique across all campaigns. You cannot reuse an audience name that has already been used in another campaign's **[!UICONTROL Save audience]** activity.

1. Choose a **[!UICONTROL Profile mapping field​]** from your Campaign Targeting dimension. This mapping defines how profiles in the **Saved audience** are linked to the campaign's target dimension during execution.

    Only mappings compatible with the current target dimension, i.e. the one from the incoming transition, will be available in the dropdown list to ensure proper reconciliation between the audience and the campaign context.

    ➡️ [Follow the steps detailed in this page to create your Campaign Targeting dimension](../target-dimension.md)

    ![](../assets/save-audience-1.png)

1. Click **[!UICONTROL Add audience mappings]** to include additional data from attributes of the **[!UICONTROL Target dimension]** or enriched **[!UICONTROL Profile attributes]**.

    This allows you to associate more information with the **[!UICONTROL Saved audience]** activity beyond the primary profile mapping, enhancing targeting and personalization options.

    ![](../assets/save-audience-2.png)

1. Finalize your setup by saving and publishing the Orchestrated campaign. This will generate and store your audience.

1. Publish the campaign for the audience to be created or replaced since the **[!UICONTROL Save audience]** activity does not execute while the campaign is in **[!UICONTROL Draft mode]**.

The content of the saved audience is then available in the detail view of the audience, which can be accessed from the **[!UICONTROL Audiences]** menu, or can be selected when targeting an audience, for example with a **[!UICONTROL Read audience]** activity.

 ![](../assets/save-audience-4.png)


## Example {#save-audience-example}

The following example demonstrates how to create a simple audience using targeting. A query identifies all recipients who booked a trip in the last 30 days by filtering this population within your Orchestrated campaign. By choosing **Recipients - CRMID** as the **Targeting dimension**, the audience targets each individual booking event rather than just the recipient as a whole. The **[!UICONTROL Save audience]** activity then captures these profiles to create a reusable audience of recent purchasers.

![](../assets/save-audience-3.png)
