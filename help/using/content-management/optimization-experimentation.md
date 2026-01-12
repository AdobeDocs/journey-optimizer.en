---
solution: Journey Optimizer
product: journey optimizer
title: Use experimentation in message optimization
description: Learn how to use content experiments to test multiple versions of content and determine which performs best.
role: User
level: Intermediate
keywords: experimentation, optimization, A/B testing, content experiment, treatments
---
# Use experimentation {#experimentation}

>[!NOTE]
>
>This page provides an overview of how to use experimentation within content optimization. For detailed information about content experiments, including configuration options, metrics, and analysis, see the [Content experiment documentation](../content-management/get-started-experiment.md).

Experimentation allows you to test multiple versions of content to determine which performs best based on predefined success metrics.

To set up experimentation, follow the steps below.

Let's say you want to test the following promotional messages in a campaign:

* **Treatment A**: "20% off your next purchase"
* **Treatment B**: "Free shipping on orders over $50"
* **Treatment C**: "Get your $10 gift card"

To set up experimentation and determine which message drives the most purchases, follow the steps below.

1. Create a [journey](../building-journeys/journey-gs.md#jo-build) or a [campaign](../campaigns/create-campaign.md).

    >[!NOTE]
    >
    >If you are in a journey, add an **[!UICONTROL Action]** activity, choose a channel activity and select **[!UICONTROL Configure action]**. [Learn more](../building-journeys/journey-action.md#add-action)

1. From the **[!UICONTROL Actions]** tab, select two inbound actions, for example [code-based experience](../code-based/get-started-code-based.md) and [In-app](../../rp_landing_pages/in-app-landing-page.md).

1. In the **[!UICONTROL Optimization]** section, select **[!UICONTROL Create experiment]**.

    ![](../campaigns/assets/msg-optimization-select-experiment.png){width=85%}

1. Design and configure your content experiment as wanted. [Learn how](../content-management/content-experiment.md)

    ![](../campaigns/assets/msg-optimization-create-experiment.png){width=85%}

    Once the experiment is defined, it applies to all the actions inserted in that campaign or through the journey **[!UICONTROL Action]** activity, meaning that the same customers see the same offers across all surfaces.

    >[!NOTE]
    >
    >You can select other actions: the experimentation applies to all actions added to the campaign or to the journey [Action activity](../building-journeys/journey-action.md).

1. [Activate](review-activate-campaign.md) your journey or campaign.

Once the journey/campaign is live, users are randomly assigned the different content variations. [!DNL Journey Optimizer] tracks which variation drives more purchases and provides actionable insights.

Follow the success of your campaign with the [journey](../reports/journey-global-report-cja.md) and [campaign](../reports/campaign-global-report-cja-experimentation.md) reports. <!--Link to Experimentation journey reportis missing-->

