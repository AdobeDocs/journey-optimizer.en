---
solution: Journey Optimizer
product: journey optimizer
title: Get started with audience composition
description: Learn more on audience composition
feature: Audiences, Profiles
topic: Content Management
role: User
level: Beginner
exl-id: af71d24d-77eb-44df-8216-b0aeaf4c4fa4
---
# Get started with audience composition {#get-start-audience-composition}

>[!CONTEXTUALHELP]
>id="ajo_ao_create_composition"
>title="Create a composition"
>abstract="Create a composition workflow to combine existing Adobe Experience Platform audiences into a visual canvas and leverage various activities (split, exclude...) to create new audiences."

>[!CONTEXTUALHELP]
>id="ajo_ao_publish"
>title="Publish your audience"
>abstract="Publish your composition to save the resulting audience(s) into Adobe Experience Platform."

>[!CONTEXTUALHELP]
>id="ajo_ao_audience"
>title="Audience activity"
>abstract="The Audience activity allows you to include in your composition additional profiles belonging to an existing audience."

>[!CONTEXTUALHELP]
>id="ajo_ao_merge_types"
>title="Merge types"
>abstract="Specify how the profiles of the selected audiences should be merged."

>[!CONTEXTUALHELP]
>id="ajo_ao_exclude_type"
>title="Exclude type"
>abstract="Use the Exclude audience type to exclude profiles belonging to an existing audience. The Exclude using attribute type allows you to exclude profiles based on a specific attribute."

>[!CONTEXTUALHELP]
>id="ajo_ao_exclude"
>title="Exclude activity"
>abstract="The Exclude activity allows you to exclude profiles from your composition by selecting an existing audience or using a rule."

>[!CONTEXTUALHELP]
>id="ajo_ao_enrich"
>title="Enrich activity"
>abstract="Use the Enrich activity to enrich your audience with additional attributes coming from Adobe Experience Platform datasets. For example, you can add information related to the product purchased like its name, price, or manufacturer ID and leverage these information to personalize the deliveries sent to the audience."

>[!CONTEXTUALHELP]
>id="ajo_ao_enrich_dataset"
>title="Enrichment dataset"
>abstract="Select the enrichment dataset containing the data that you want to associate to the audience."

>[!CONTEXTUALHELP]
>id="ajo_ao_enrich_criteria"
>title="Enrichment criteria"
>abstract="Select the fields to use as reconciliation key between the source dataset, i.e. the audience, and the enrichment dataset."

>[!CONTEXTUALHELP]
>id="ajo_ao_enrich_attributes"
>title="Enrichment attributes"
>abstract="Select one or multiple attributes from the enrichment dataset to associate to the audience. Once the composition is published, these attributes are associated to the audience and can be leveraged in Journey Optimizer campaigns to personalize deliveries."

>[!CONTEXTUALHELP]
>id="ajo_ao_ranking"
>title="Rank activity"
>abstract="The Rank activity allows you to rank profiles based on a specific attribute and include them into your composition. For example, include the 50 profiles with the largest amount of loyalty points."

>[!CONTEXTUALHELP]
>id="ajo_ao_rank_profilelimit_text"
>title="Add profile limit"
>abstract="Toggle this option on to specify a maximum number of profiles to include in the composition."

<!-- [!CONTEXTUALHELP]
>id="ajo_ao_control_group_text"
>title="Control Group"
>abstract="Use control groups to isolate a portion of the profiles. This allows you to measure the impact of a marketing activity and make a comparison with the behavior of the rest of the population."-->

>[!CONTEXTUALHELP]
>id="ajo_ao_split"
>title="Split activity"
>abstract="The Split activity allows you to divide your composition into multiple paths. When publishing the composition, one audience will be saved into Adobe Experience Platform for each path."

>[!CONTEXTUALHELP]
>id="ajo_ao_split_type"
>title="Split type"
>abstract="Use the Percent split type to randomly split profiles into multiple paths. The Attribute split type allows you to split profiles based on a specific attribute."

>[!CONTEXTUALHELP]
>id="ajo_ao_split_otherprofiles_text"
>title="Other profiles"
>abstract="Toggle this option on to create an additional path with the remaining profiles that do not match any of the conditions specified in the other paths."

This documentations provides detailed information on how to work with audience composition within Adobe Journey Optimizer. If you are a Real-time Customer Profile only customer and are not using Adobe Journey Optimizer, [click here](https://experienceleague.adobe.com/docs/experience-platform/segmentation/ui/audience-composition.html){target="_blank"}.

>[!ENDSHADEBOX]

Audience composition allows you to create **composition workflows**, where you can combine existing Adobe Experience Platform audiences into a visual canvas and leverage various activities (split, exclude...) to create new audiences.

Once done, the **resulting audiences** are saved backed into Adobe Experience Platform along with existing audiences and can be leveraged in Journey Optimizer campaigns and journeys to target customers. Learn how to target audiences in Journey Optimizer
![](assets/audiences-process.png)

>[!IMPORTANT]
>
>The use of audiences and attributes from audience composition is currently unavailable for use with Healthcare Shield or Privacy and Security Shield.
>
>Enrichment attributes are not yet integrated with the policy enforcement service. Therefore, any data usage labels you apply to your enrichment attributes will not be enforced in Journey Optimizer campaigns or journeys.

Audience composition is accessible from Adobe Journey Optimizer **[!UICONTROL Audiences]** menu:

![](assets/audiences-browse.png)

* The **[!UICONTROL Overview]** tab provides a dedicated dashboard with key metrics related to your organization's audience data. To learn more, refer to [Adobe Experience Platform Dashboards guide](https://experienceleague.adobe.com/docs/experience-platform/dashboards/guides/segments.html).

* The **[!UICONTROL Browse]** tab lists all existing audiences stored into Adobe Experience Platform.

* The **[!UICONTROL Compositions]** tab allows you to create composition workflows where you can combine and arrange audiences to create new ones.

## Create a composition workflow {#create}

To create a composition workflow, follow these steps:

1. Access the **[!UICONTROL Audiences]** menu and select **[!UICONTROL Create Audience]**.

1. Select **[!UICONTROL Compose Audience]**.
    
    ![](assets/audiences-create.png)

1. The composition canvas displays with two default activities:

    * **[!UICONTROL Audience]**: the starting point of your composition. This activity allows you to select one or multiple audiences as a basis for your workflow,

    * **[!UICONTROL Save]**: the last step of your composition. This activity allows you to save the result of your workflow into a new audience.

1. Open the composition properties to specify a title and a description. 

    If no title is defined in the properties, the composition's label is set to  "Composition" followed by its creation date and time.

    ![](assets/audiences-properties.png)

1. Configure your composition by adding as many activities as needed between the **[!UICONTROL Audience]** and **[!UICONTROL Save]** activities. For more information on how to create a composition, refer to the [Audience composition documentation](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-composition).

    ![](assets/audiences-publish.png)

1. Once your composition is ready, click the **[!UICONTROL Publish]** button to publish the composition and save the resulting audiences into Adobe Experience Platform.

    >[!IMPORTANT]
    >
    >You can publish up to 10 compositions in a given sandbox. If you have reached this threshold, you need to delete a composition to free up space and publish a new one.
 
    If any error occurs during publishing, alerts will display with information on how to resolve the issue.

    ![](assets/audiences-alerts.png)

1. The composition is published. The resulting audiences are saved into Adobe Experience Platform and are ready to be targeted in Journey Optimizer. [Learn how to target audiences in Journey Optimizer](../audience/about-audiences.md#segments-in-journey-optimizer)

>[!NOTE]
>
>Audiences from **audience composition** are executed daily, so you may need to wait up to 24 hours to use them in Journey Optimizer. Enriched attributes in audience composition audiences are as fresh as the last composition run, which can be up to 24 hours in the past.

## Access compositions {#access}

All created compositions can be accessed from the **[!UICONTROL Compositions]** tab. You can duplicate or delete an existing composition at any time using the ellipsis button in the list.

Compositions can have multiple statuses:

* **[!UICONTROL Draft]**: the composition is in progress and has not been published.
* **[!UICONTROL Published]**: the composition has been published, resulting audiences have been saved and are available for use.

![](assets/audiences-compositions.png)

>[!NOTE]
>
>Audience composition is currently not integrated with the sandbox reset capability. Before initiating a sandbox reset, you need to delete your compositions manually to ensure that the associated audience data is cleaned up properly. Detailed information is available in Adobe Experience Platform [Sandbox documentation](https://experienceleague.adobe.com/docs/experience-platform/sandbox/ui/user-guide.html#delete-audience-compositions)
