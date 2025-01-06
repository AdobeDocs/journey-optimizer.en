---
title: Create selection strategies
description: Learn how to create selection strategies
feature: Decisioning
topic: Integrations
role: User
level: Intermediate
exl-id: 1b73b398-050a-40bb-a8ae-1c66e3e26ce8
---
# Create selection strategies {#selection-strategies}

>[!CONTEXTUALHELP]
>id="ajo_exd_config_strategies"
>title="Define your selection strategies"
>abstract="A selection strategy is reusable and consists of a collection associated with an eligibility constraint and a ranking method to determine the offers to be shown when selected in a decision policy."
>additional-url="https://experienceleague.adobe.com/docs/journey-optimizer/using/decisioning/experience-decisioning/create-decision.html" text="Create decision policies"

>[!CONTEXTUALHELP]
>id="ajo_exd_strategy_eligibility"
>title="Restrict the eligible profiles"
>abstract="You can restrict the selection of offers for this selection strategy. By default, all profiles are eligible, but you can use audiences or rules to limit the offer selection to specific profiles only."
>additional-url="https://experienceleague.adobe.com/docs/journey-optimizer/using/audiences-profiles-identities/audiences/about-audiences.html" text="Use audiences"
>additional-url="https://experienceleague.adobe.com/docs/journey-optimizer/using/decisioning/experience-decisioning/selection/rules.html" text="Use decision rules"

A selection strategy is reusable, and consists of a collection associated with an eligibility constraint and a ranking method to determine the offers to be shown when selected in a [decision policy](create-decision.md).

## Access and manage selection strategies

1. Go to **[!UICONTROL Decisioning]** > **[!UICONTROL Strategy setup]** > **[!UICONTROL Selection strategies]**.

1. All the selection strategies created so far are listed. Filters are available to help you retrieve strategies according to the ranking method.

    ![](assets/strategy-list-filters.png)

1. Click a selection strategy name to edit it.

1. The collection, ranking method and eligibility selected for each strategy are also displayed. You can click the icon next to each collection name to directly edit a collection.

    ![](assets/strategy-list-edit-collection.png)

## Create a selection strategy {#create-selection-strategy}

To create a selection strategy, follow the steps below.

1. From the **[!UICONTROL Selection strategies]** inventory, click **[!UICONTROL Create selection strategy]**.

    ![](assets/strategy-create-button.png)

1. Add a name for your strategy.

    >[!NOTE]
    >
    >Currently only the default **[!UICONTROL Offers]** catalog is available.

1. Fill in the details for your selection strategy, starting by the name.

    ![](assets/strategy-create-screen.png)

1. Select the [collection](collections.md) that contains the offers to consider.

1. Use the **[!UICONTROL Eligibility]** field to restrict the selection of offers for this selection strategy.

    ![](assets/strategy-create-eligibility.png)

    * To restrict the selection of the offers to the members of an Experience Platform audience, select **[!UICONTROL Audiences]** and choose an audience from the list. [Learn how to work with audiences](../audience/about-audiences.md)

    * If you want to add a selection constraint with a decision rule, use the **[!UICONTROL Decision rule]** option and select the rule of your choice. [Learn how to create a rule](rules.md)

1. Define the ranking method you want to use to select the best offer for each profile. [Learn more](#select-ranking-method)

    ![](assets/strategy-create-ranking.png)

    * By default, if multiple offers are eligible for this strategy, the [Offer priority](#offer-priority) method uses the value defined in the offers.

    * If you want to use a specific calculated score to choose which eligible offer to deliver, select [Formula](#ranking-formula) or [AI model](#ai-ranking).

1. Click **[!UICONTROL Create]**. It is now ready to be used in a [decision policy](create-decision.md)

## Select a ranking method {#select-ranking-method}

>[!CONTEXTUALHELP]
>id="ajo_exd_strategy_ranking"
>title="Define how to rank offers"
>abstract="If several offers are eligible for a given selection strategy, choose the method that will select the best offer for each profile when creating a selection strategy: priority or ranking formula."
>additional-url="https://experienceleague.adobe.com/docs/journey-optimizer/using/decisioning/experience-decisioning/create-decision.html" text="Create decision policies"

If several offers are eligible for a given selection strategy, you can choose the method that will select the best offer for each profile when creating a selection strategy. You can rank offers by:

* [Offer priority](#offer-priority)
* [Formula](#ranking-formula)
* [AI ranking](#ai-ranking)

### Offer priority {#offer-priority}

By default, when several offers are eligible for a given placement in a decision policy, the items with the highest **priority** will be delivered to the customers first.

![](assets/item-priority.png)

Offers' priority scores are assigned when creating a [decision item](items.md).

### Ranking formula {#ranking-formula}

In addition to offer priority, Journey Optimizer allows you to create **ranking formulas**. These are formulas that determine which offer should be presented first for a given placement, rather than taking into account the offers' priority scores.

For example, you can boost the priority of all offers where the end date is less than 24 hours from now, or boost offers from the "running" category if the profile's point of interest is "running". Learn how to create a ranking formula in [this section](ranking.md).

Once created, you can use this formula in a selection strategy. If multiple offers are eligible to be presented when using this selection strategy, the decision will use the selected formula to calculate which offer to deliver first.

### AI ranking {#ai-ranking}

You can also use a trained model system that automatically ranks offers to display for a given profile by selecting an AI model. Learn how to create an AI model in [this section](ranking.md).

Once an AI model has been created, you can use it in a selection strategy. If multiple offers are eligible, the trained model system will determine which offer should be presented first for this selection strategy.
