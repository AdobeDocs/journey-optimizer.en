---
solution: Journey Optimizer, Experience Platform
product: Journey Optimizer
title: Create a dataset to collect events
description: Learn how to create a dataset to collect events
badge: label="Legacy" type="Informative"
feature: Ranking, Decision Management, Datasets
role: Developer
level: Experienced
exl-id: 99963ef4-0b19-475e-96f4-2eac3f680c6f
version: Journey Orchestration
TQID: https://experienceleague.adobe.com/SnbdXcSaDXxO1OapmRL3YYwRmCbBFqcuPlxFt-NEZCc
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: a4cb03e1-327e-499d-9de8-e0c0db8a63a2
    internal-label: Decision capabilities (AJO)
  - id: ad78185d-8f79-40ad-9bad-cbde74af74ee
    internal-label: Guardrails and limitations
role_v2:
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
topic_v2:
  - id: d3cdead0-685a-4489-9250-4bb709942f66
    internal-label: Data collection
  - id: ebde5b41-29c9-4f5e-9ef6-1197e85409e3
    internal-label: Data management
subfeature_v2:
  - id: a7a194a0-75e2-4913-8a83-14714fbf68e6
    internal-label: Decisioning API
  - id: eb547372-2a95-4d13-b0fd-f720c9895880
    internal-label: Edge Decisioning (AJO)
---
# Create a dataset to collect events {#create-dataset}

>[!TIP]
>
>Decisioning, [!DNL Adobe Journey Optimizer]'s new decisioning capability, is now available via the code-based experience and email channels! [Learn more](../../experience-decisioning/gs-experience-decisioning.md)

To collect experience events, you first need to create a dataset where these events will be sent.

Start by creating the schema that will be used in your dataset:

1. From the **[!UICONTROL Data Management]** menu, select **[!UICONTROL Schema]**.

1. Click **[!UICONTROL Create schema]**, in the top right, select **[!UICONTROL Experience Event]** and click **Next**.

    ![](../assets/ai-ranking-xdm-event.png)

    >[!NOTE]
    >
    >Learn more about XDM schemas and fields groups in the [XDM System overview documentation](https://experienceleague.adobe.com/docs/experience-platform/xdm/home.html){target="_blank"}.

1. Enter a name and description for your schema and click **Finish**.
    ![](../assets/ai-ranking-xdm-event-2.png)

1. From the **[!UICONTROL Field groups]** section on the left, select **[!UICONTROL Add]**.

    ![](../assets/ai-ranking-fields-groups.png)

1. In the **[!UICONTROL Search]** field, type "proposition interaction".

1. Select the **[!UICONTROL Experience Event - Proposition Interactions]** field group and click **[!UICONTROL Add field groups]**.

    ![](../assets/ai-ranking-add-field-group.png)

    >[!CAUTION]
    >
    >The schema that will be used in your dataset must have the **[!UICONTROL Experience Event - Proposition Interactions]** field group associated with it. Otherwise you will not be able to use it in your AI model.

1. Save the schema.

>[!NOTE]
>
>Learn more about building schemas in [Basics of schema composition](https://experienceleague.adobe.com/docs/experience-platform/xdm/schema/composition.html#understanding-schemas){target="_blank"}.

you are now ready to create a dataset using this schema. To do this, follow the steps below:

1. From the **[!UICONTROL Data Management]** menu, select **[!UICONTROL Datasets]** and go to the **[!UICONTROL Browse]** tab.

1. Click **[!UICONTROL Create dataset]** and select **[!UICONTROL Create dataset from schema]**.

    ![](../assets/ai-ranking-create-dataset-from-schema.png)
    
1. Select the schema you just created from the list and click **[!UICONTROL Next]**.

1. Provide a unique name for the dataset in the **[!UICONTROL Name]** field and click **[!UICONTROL Finish]**.

    ![](../assets/ai-ranking-dataset-name.png)

>[!NOTE]
>
>This dataset can now be selected to collect event data when [creating an AI model](../ranking/create-ranking-strategies.md).
