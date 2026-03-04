---
solution: Journey Optimizer, Experience Platform
product: Journey Optimizer
title: Create decision rules
description: Learn how to create decision rules to define to whom offers can be displayed
badge: label="Legacy" type="Informative"
feature: Decision Management
topic: Integrations
role: User
level: Intermediate
exl-id: 401ce05b-412b-4fa0-a516-bf75727f6387
version: Journey Orchestration
---
# Create decision rules {#create-decision-rules}

>[!IMPORTANT]
>
>This page covers decision rules for the legacy **Decision Management** capability. If you are using **Decisioning** — [!DNL Adobe Journey Optimizer]'s current decisioning capability available via code-based experience and email channels — refer to [Build rules](../../experience-decisioning/rules.md) instead.
>
>Not sure which capability you are using? [Learn about Decisioning](../../experience-decisioning/gs-experience-decisioning.md).

## About decision rules {#about}

You can create offer decision rules based on data available in Adobe Experience Platform. Decision rules determine to whom an offer can be shown.

For example, you can specify that you only want a 'Women's Winter Clothing Offer' to be shown when (Gender = 'Female') and (Region = 'Northeast').

➡️ [Discover this feature in video](#video)

Here is a list of limitations to be aware of when working with decision rules:

* Edge decisioning uses the edge profile which does not store events, so any rule used in an edge decision will be invalid.
* When creating a decision rule, looking back into a previous period of time is not supported. For instance, if you specify an experience event that occurred within the last month as a component of the rule. Any attempt to include a lookback period during rule creation will trigger an error when saving it.
<!--* Decision requests that use the hub profile will look at the last 100 experience events on the profile to evaluate rules that reference historical experience events.-->

## Create a decision rule {#create}

The list of created decision rules is accessible in the **[!UICONTROL Components]** menu.

![](../assets/decision_rules_list.png)

To create a decision rule, follow these steps:

1. Go to the **[!UICONTROL Rules]** tab, then click **[!UICONTROL Create rule]**.

    ![](../assets/offers_decision_rule_creation.png)

1. Name your rule and provide a description, then configure the rule according to your needs.
    
    To do this, the Adobe Experience Platform **Segment Builder** is available to help you build the rule's conditions. [Learn how to build segment definitions](../../audience/creating-a-segment-definition.md)
    
    <!--In this example, the rule will target customers that have the "Gold" loyalty level.-->

    ![](../assets/offers_decision_rule_creation_segment.png)

    >[!NOTE]
    >
    >The Segment Builder provided to create decision rules presents some specificities compared to the one used with the **[!UICONTROL Segmentation]** service. However, the global process described in the [Segment Builder](../../audience/creating-a-segment-definition.md) documentation is still valid to build offers decisions rules. Learn more in the [Adobe Experience Platform Segmentation Service documentation](https://experienceleague.adobe.com/docs/experience-platform/segmentation/ui/segment-builder.html).

1. As you are adding and configuring new fields in the workspace, the **[!UICONTROL Audience properties]** pane displays information on the estimated profiles belonging to the audience. Click **[!UICONTROL Refresh estimate]** to update data.

    ![](../assets/offers_decision_rule_creation_estimate.png)

    >[!NOTE]
    >
    >Profile estimates are unavailable when rule parameters include data not in the profile such as context data. For example, an eligibility rule that requires the current weather to be ≥80 degrees.
    
1. Click **[!UICONTROL Save]** to confirm.

1. Once the rule is created, it displays in the **[!UICONTROL Rules]** list. You can select it to display its properties, and edit or delete it.

    ![](../assets/rule_created.png)

>[!CAUTION]
>
>Event-based offers are currently not supported in [!DNL Journey Optimizer]. If you create a decision rule based on an [event](https://experienceleague.adobe.com/docs/experience-platform/segmentation/ui/segment-builder.html#events){target="_blank"}, you will not be able to leverage it in an offer.

## Tutorial video {#video}

>[!VIDEO](https://video.tv.adobe.com/v/329373?quality=12)
