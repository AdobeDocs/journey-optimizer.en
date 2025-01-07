---
title: Decisioning use case
description: Learn how to create decisions using experiments with the code-based channel
feature: Decisioning
topic: Integrations
role: User
level: Intermediate, Experienced
hide: yes
hidefromtoc: yes
exl-id: 09770df2-c514-4217-a71b-e31c248df543
---
# Decisioning use case {#experience-decisioning-uc}

This use case presents all the steps needed to use Decisioning with the [!DNL Journey Optimizer] code-based channel.

<!--In this use case, you create a campaign where you define two delivery treatments - each containing a different decision policy in order to measure which one performs best for your target audience.-->

In this use case, you are unsure if a specific ranking formula will perform better than the pre-assigned offer priorities.

To measure which one performs best for your target audience, create a campaign using [Content Experiment](../content-management/content-experiment.md) where you define two delivery treatments:

<!--Set up the experiment such that:-->

* The first treatment contains one selection strategy with priority as the ranking method.
* The second treatment contains a different selection strategy for which a formula is the ranking method.

## Create selection strategies

First, you need to build two selection strategies: one with priority as the ranking method, and another one with a formula as the ranking method.

### Create the first selection strategy

In the first selection strategy, select priority as the ranking method. Follow the steps below.

1. Create a decision item. [Learn how](items.md)

1. Set the **[!UICONTROL Priority]** of the decision item compared to others. If a profile qualifies for multiple items, a higher priority grants the item precedence over others.

    ![](assets/exd-uc-item-priority.png)

    >[!NOTE]
    >
    >The priority is an integer data type. All attributes that are integer data types should contain integer values (no decimals).

1. Set the decision item's eligibility:

    * Define audiences or rules to restrict the item to specific profiles only. [Learn more](items.md#eligibility)

    * Set capping rules to define the maximum number of times an offer can be presented. [Learn more](items.md#capping)

1. If needed, repeat the steps above to create additional decision items.

1. Create a **collection** where your decision item(s) will be included. [Learn more](collections.md)

1. Create a [selection strategy](selection-strategies.md#create-selection-strategy) and select the [collection](collections.md) that contains the offer(s) to consider.

1. [Choose the ranking method](#select-ranking-method) to use to select the best offer for each profile.

    In this case, select **[!UICONTROL Offer priority]**: if multiple offers are eligible for this strategy, the Decisioning engine uses the value set as **[!UICONTROL Priority]** in the offer(s). [Learn more](selection-strategies.md#offer-priority)

    ![](assets/exd-uc-strategy-priority.png)

### Create the second selection strategy

In the second selection strategy, select a formula as the ranking method. Follow the steps below.

1. Create a decision item. [Learn how](items.md)

<!--1. Set the same **[!UICONTROL Priority]** as for the first decision item. TBC?-->

1. Set the decision item's eligibility:

    * Define audiences or rules to restrict the item to specific profiles only. [Learn more](items.md#eligibility)

    * Set capping rules to define the maximum number of times an offer can be presented. [Learn more](items.md#capping)

1. If needed, repeat the steps above to create additional decision items.

1. Create a **collection** where your decision item(s) will be included. [Learn more](collections.md)

1. Create a [selection strategy](selection-strategies.md#create-selection-strategy) and select the [collection](collections.md) that contains the offer(s) to consider.

1. [Choose the ranking method](#select-ranking-method) you want to use to select the best offer for each profile.

    In this case, select **[!UICONTROL Formula]** to use a specific calculated score to choose which eligible offer to deliver. [Learn more](selection-strategies.md#ranking-formula)

    ![](assets/exd-uc-strategy-formula.png)

## Build a code-based experience campaign

<!--To present the best dynamic offer and experience to your visitors on your website or mobile app, add a decision policy to a code-based campaign.

Define two delivery treatments each containing a different decision policy.-->

Once you configured the two selection strategies, create a code-based experience campaign where you define a different treatment for each strategy to compare which one performs best.

1. Create a campaign, and select the **[!UICONTROL Code-base experience]** action. [Learn more](../code-based/create-code-based.md)

1. From the campaign summary page, click **[!UICONTROL Create experiment]** to start configuring your content experiment. [Learn more](../content-management/content-experiment.md)

    ![](assets/exd-uc-create-experiment.png)

1. Click **[!UICONTROL Edit content]**.

<!--1. Sart personalizing **Treatment A** by clicking **[!UICONTROL Create]**.

    ![](assets/exd-uc-create-treatment-a.png)-->

1. From the content edition window, start personalizing **Treatment A** by clicking **[!UICONTROL Edit code]**.

    ![](assets/exd-uc-experiment-treatment-a.png)

1. Select **[!UICONTROL Decision policy]**, click **[!UICONTROL Add decision policy]** and fill in the decision details. [Learn more](create-decision.md)

   ![](assets/decision-code-based-create.png)

1. Select the first strategy that you created. Click **[!UICONTROL Add strategy]**.

1. Click **[!UICONTROL Create]**. The new decision is added under **[!UICONTROL Decisions]**.

    ![](assets/decision-code-based-decision-added.png)

1. Click the more actions icon (three dots) and select **[!UICONTROL Add]**. Now you can add all the decision attributes you want inside this.

    ![](assets/decision-code-based-add-decision.png)

1. You can also add any other attribute available in the personalization editor, such as profile attributes.

    ![](assets/decision-code-based-decision-profile-attribute.png)

1. From the content edition window, select **Treatment B**, and repeat the steps above to create another decision policy and select the second selection strategy that you created.

    ![](assets/exd-uc-experiment-treatment-b.png)

1. Save your content.
