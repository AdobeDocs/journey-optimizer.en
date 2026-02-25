---
title: Journey arbitration AI models
description: Learn how to create and use AI models to rank journeys for arbitration, so the best journey is selected per profile based on AI-driven scores.
feature: Journeys, Decisioning
role: User
level: Intermediate
version: Journey Orchestration
badge: label="Limited Availability" type="Informative"
hide: true
hidefromtoc: true
---
# Use AI models to rank journeys {#journey-ai-models}

>[!AVAILABILITY]
>
>This feature is currently in Limited Availability. Contact your Adobe representative to gain access.

[!DNL Adobe Journey Optimizer] helps you control which journeys a profile can enter when they qualify for more than the system allows. To do so, you can use [rule sets](rule-sets.md) to define caps on journey entry or concurrency. When a profile is eligible for more journeys than the cap allows, the priority assigned to each journey determines which journeys are selected.

Instead of using priority or ranking formulas, you can use **AI models** to dynamically rank journeys based on trained model scores. You can create AI models from the **[!UICONTROL Orchestration ranking]** section in the UI and use them in rule sets to apply them to journeys.

For an overview of AI model types available in [!DNL Journey Optimizer], see [Get started with AI models](../experience-decisioning/ranking/ai-models.md#ai-model-types) in the Decisioning section.

## Create an AI model {#create-ai-model}

>[!CAUTION]
>
>To create, edit, or delete AI models, you must have the **Manage Ranking Strategies** permission. [Learn more](../administration/high-low-permissions.md#manage-ranking-strategies)

To create an AI model for journey ranking, follow the steps below.

1. Create a dataset where conversion events will be collected. [Learn how](../experience-decisioning/data-collection/create-dataset.md)

1. Access the **[!UICONTROL Orchestration ranking]** section, then select the **[!UICONTROL AI models]** tab. The list of previously created AI models is displayed.

1. Click **[!UICONTROL Create AI model]**.

1. Specify a unique name and, if needed, a description for the AI model.

    ![AI model details pane with name and description fields](assets/journey-model-details.png){width="80%"}

    >[!NOTE]
    >
    >The ranking object is the entity that the ranking formula will apply to. By default, the ranking object is set to **[!UICONTROL Journey]**.

<!--
1. Select the type of AI model you want to create:

    * **[!UICONTROL Auto-optimization]** optimizes based on past performance. [Learn more](../experience-decisioning/ranking/auto-optimization-model.md)
    * **[!UICONTROL Personalized optimization]** optimizes and personalizes based on audiences and performance. [Learn more](../experience-decisioning/ranking/personalized-optimization-model.md)-->

1. The **[!UICONTROL Optimization metric]** section provides information on the conversion event used by the AI model. [!DNL Journey Optimizer] ranks based on the **conversion rate** (Conversion rate = Total number of conversion events / Total number of impression events). The conversion rate is calculated using:

    * **Impression events** (items that are displayed)
    * **Conversion events** (items that result in clicks or conversions)

    These events are automatically captured using the Web SDK or the Mobile SDK. Learn more in the [Adobe Experience Platform Web SDK](https://experienceleague.adobe.com/docs/experience-platform/edge/home.html) overview.

1. Select the dataset(s) where the conversion and impression events are collected. Learn how to create such datasets in [this section](../experience-decisioning/data-collection/create-dataset.md).

    ![Dataset selection for conversion and impression events](../experience-decisioning/assets/ai-model-datasets.png){width="85%"}

    >[!CAUTION]
    >
    >Only the datasets created from schemas associated with the **[!UICONTROL Experience Event - Proposition Interactions]** field group (previously known as mixin) are displayed in the drop-down list.

1. <!--If you are creating a **[!UICONTROL Personalized optimization]** AI model, -->Select the segment(s) to use to train the AI model.

    >[!NOTE]
    >
    >You can select up to 5 audiences.

1. Save and activate the AI model.

The AI model is now available when you configure a rule set.

## Assign the AI model to a rule set {#assign-ai-model-to-ruleset}

To use an AI model to rank your journeys, you need to use it in a formula and assign this formula to a rule set.

1. Create a ranking formula using the AI model you created. [Learn how](journey-ranking-formulas.md#create-journey-ranking-formula)

1. From the **[!UICONTROL Business rules]** menu, create a rule set you want to use for journey arbitration. [Learn how](rule-sets.md#Create)

1. Make sure you select the **[!UICONTROL Journey]** domain.

1. In the rule set properties, set the **[!UICONTROL Ranking method]** to **[!UICONTROL Formula]** (instead of **[!UICONTROL Priority]**).

1. Select the formula that using the AI model that you created from the drop-down list.

1. Create the journey capping rules you want to add to the rule set. [Learn how](journey-capping.md#create-rule)

1. Save the rule set.

Now the formula using the AI model is assigned to the rule set. You can then apply that rule set to your journeys.

## Apply the rule set to a journey {#assign-rule-set-to-journey}

To assign the rule set to a journey, follow the steps below.

1. Create or open the journey you want to assign the rule set to. [Learn how to create a journey](../building-journeys/journey-gs.md)

1. In the journey properties, select the rule set from the drop-down list. [Learn how](journey-capping.md#apply-capping).

    >[!NOTE]
    >
    >Only one rule set can be applied to a journey at a time.

1. Save the journey.

All journeys that use this rule set will be ranked with the selected formula using the AI model when the cap is applied.
