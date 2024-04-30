---
title: Decision rules
description: Learn how to work with decision rules
feature: Experience Decisioning
topic: Integrations
role: User
level: Intermediate
hide: yes
hidefromtoc: yes
badge: label="Beta"
exl-id: 033a11b8-c848-4e4a-b6f0-62fa0a2152bf
---
# Decision rules {#rules}

>[!CONTEXTUALHELP]
>id="ajo_exd_config_rules"
>title="Create decision rules"
>abstract="Decision rules allow you to define the audience for decision items by applying constraints, either directly at the decision item level or within a specific selection strategy. This enables you to precisely control which items should be presented to whom."

>[!BEGINSHADEBOX "What you'll find in this documentation guide"]

* [Get started with Experience Decisioning](gs-experience-decisioning.md)
* Manage your decision items: [Configure the items catalog](catalogs.md) - [Create decision items](items.md) - [Manage items collections](collections.md)
* Configure items' selection: **[Create decision rules](rules.md)** - [Create ranking methods](ranking.md)
* [Create selection strategies](selection-strategies.md)
* [Create decision policies](create-decision.md)

>[!ENDSHADEBOX]

Decision rules allow you to define the audience for decision items by applying constraints, either directly at the decision item level or within a specific selection strategy. This enables you to precisely control which items should be presented to whom.

For instance, let's consider a scenario where you have decision items featuring Yoga-related products designed for women. With decision rules, you can specify that these items should only be displayed to profiles whose gender is 'Female' and who have indicated a 'Point of Interest' in 'Yoga'.

>[!NOTE]
>
>In addition to item and selection strategy level decision rules, you can also define your intended audience at the campaign level. [Learn more](../campaigns/create-campaign.md#audience)

The list of decision rules is accessible in the **[!UICONTROL Configuration]** / **[!UICONTROL Decisions rules]** menu.

![](assets/decision-rules-list.png)

## Create a decision rule {#create}

To create a decision rule, follow these steps:

1. Navigate to **[!UICONTROL Configuration]** / **[!UICONTROL Decision rules]** then click **[!UICONTROL Create rule]** button.

1. The decision rules creation screen opens. Name your rule and provide a description.

1. Build the decision rule to suit your needs using the Adobe Experience Platform Segment Builder. To do this, tou can leverage various data sources such as profile attributes, audiences, or context data coming from Adobe Experience Platform. [Learn how to leverage context data in decision rules](#context-data)

    ![](assets/decision-rules-build.png)

    >[!NOTE]
    >
    >The Segment Builder provided to create decision rules presents some specificities compared to the one used with the Adobe Experience Platform Segmentation service.  However, the global process described in the documentation is still valid to build decisions rules. [Learn how to build segment definitions](../audience/creating-a-segment-definition.md)

1. As you are adding and configuring new fields in the workspace, the **[!UICONTROL Audience properties]** pane displays information on the estimated profiles belonging to the audience. Click **[!UICONTROL Refresh estimate]** to update data.

    >[!NOTE]
    >
    >Profile estimates are unavailable when rule parameters include data not in the profile such as context data.

1. Once your decision rule is ready, click **[!UICONTROL Save]**. The created rule appears in the list and is available for use in decision items and selection strategies to govern the presentation of decision items to profiles.

## Leverage context data in decision rules {#context-data}

The Experience Decisioning rule creation screen allows you to leverage any information available in Adobe Experience Platform to create decision rules. For example, you can design a decision rule that requires the current weather to be ≥80 degrees.

To do so, you first need to define the data you want to make available in Experience Decisioning. Once done, this data seamlessly integrates into Experience Decisioning in the **[!UICONTROL Context Data]** tab available when creating a decision rule.

![](assets/decision-rules-context.png)

The steps to feed Experience Decisioning with Adobe Experience Platform data are as follows: 

1. Create an **Experience Event schema**  in Adobe Experience Platform and its associated **dataset**. [Learn how to create schemas](https://experienceleague.adobe.com/en/docs/experience-platform/xdm/ui/resources/schemas){target="_blank"}

1. Create a new Adobe Experience Platform datastream:

    1. Navigate to the **[!UICONTROL Datastreams]** menu and select **[!UICONTROL New Datastream]**.

    1. In the **[!UICONTROL Event Schema]** drop-down list, select the Experience Event schema created earlier then click **[!UICONTROL Save]**.

        ![](assets/decision-rule-context-datastream.png)

    1. Click **[!UICONTROL Add service]** and select "Adobe Experience Platform" as the service. In the **[!UICONTROL Event Dataset]** drop-down list, select the event dataset created earlier and enable the **[!UICONTROL Adobe Journey Optimizer]** option.

        ![](assets/decision-rules-context-datastream-service.png)

Once the datastream is saved, the selected dataset's information is automatically fetched and integrated into Experience Decisioning, typically becoming available within approximately 24 hours.

For further guidance on how to work with Adobe Experience Platform, explore the following resources:

* [Experience Data Model (XDM) schemas](https://experienceleague.adobe.com/en/docs/experience-platform/xdm/schema/composition){target="_blank"}
* [Datasets](https://experienceleague.adobe.com/en/docs/experience-platform/catalog/datasets/overview){target="_blank"}
* [Datastreams](https://experienceleague.adobe.com/en/docs/experience-platform/datastreams/overview){target="_blank"}
