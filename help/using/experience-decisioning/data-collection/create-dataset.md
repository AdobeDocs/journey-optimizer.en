---
product: experience platform
solution: Experience Platform
title: Create a dataset to collect events
description: Learn how to create a dataset to collect events
feature: Ranking, Decision Management, Datasets
role: Developer
level: Experienced
hide: yes
hidefromtoc: yes
exl-id: 96c1326f-be40-4738-8997-a67dc14872bb
version: Journey Orchestration
---
# Create a dataset to collect events {#create-dataset}

To collect experience events, you first need to create a dataset where these events will be sent.

Start by creating the schema that will be used in your dataset:

1. From the **[!UICONTROL Data Management]** menu, select **[!UICONTROL Schema]**.

1. Click **[!UICONTROL Create schema]**, in the top right, select **[!UICONTROL Experience Event]** and click **Next**.

    ![](../../offers/assets/ai-ranking-xdm-event.png)

    >[!NOTE]
    >
    >Learn more about XDM schemas and fields groups in the [XDM System overview documentation](https://experienceleague.adobe.com/docs/experience-platform/xdm/home.html){target="_blank"}.

1. Enter a name and description for your schema and click **Finish**.
    ![](../../offers/assets/ai-ranking-xdm-event-2.png)

1. From the **[!UICONTROL Field groups]** section on the left, select **[!UICONTROL Add]**.

    ![](../../offers/assets/ai-ranking-fields-groups.png)

1. In the **[!UICONTROL Search]** field, type "proposition interaction".

1. Select the **[!UICONTROL Experience Event - Proposition Interactions]** field group and click **[!UICONTROL Add field groups]**.

    ![](../../offers/assets/ai-ranking-add-field-group.png)

    >[!CAUTION]
    >
    >The schema that will be used in your dataset must have the **[!UICONTROL Experience Event - Proposition Interactions]** field group associated with it. Otherwise you will not be able to use it in your AI model.

1. Save the schema.

>[!NOTE]
>
>Learn more about building schemas in [Basics of schema composition](https://experienceleague.adobe.com/docs/experience-platform/xdm/schema/composition.html#understanding-schemas){target="_blank"}.

You are now ready to create a dataset using this schema. To do this, follow the steps below:

1. From the **[!UICONTROL Data Management]** menu, select **[!UICONTROL Datasets]** and go to the **[!UICONTROL Browse]** tab.

1. Click **[!UICONTROL Create dataset]** and select **[!UICONTROL Create dataset from schema]**.

    ![](../../offers/assets/ai-ranking-create-dataset-from-schema.png)
    
1. Select the schema you just created from the list and click **[!UICONTROL Next]**.

1. Provide a unique name for the dataset in the **[!UICONTROL Name]** field and click **[!UICONTROL Finish]**.

    ![](../../offers/assets/ai-ranking-dataset-name.png)

>[!NOTE]
>
>This dataset can now be selected to collect event data when creating an [AI model](../ranking/create-ai-models.md).
