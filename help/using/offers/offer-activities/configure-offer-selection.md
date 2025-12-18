---
solution: Journey Optimizer, Experience Platform
product: Journey Optimizer
title: Configure offers selection in decisions
description: Learn how to manage offers selection into decisions
badge: label="Legacy" type="Informative"
feature: Decision Management
topic: Integrations
role: User
level: Intermediate
exl-id: 8c7135d7-bf5a-4671-afdf-afec60907a56
version: Journey Orchestration
---
# Configure offers selection in decisions {#offers-selection-in-decisions}

>[!TIP]
>
>Decisioning, [!DNL Adobe Journey Optimizer]'s new decisioning capability, is now available via the code-based experience and email channels! [Learn more](../../experience-decisioning/gs-experience-decisioning.md)

If several offers are eligible for a given placement, you can choose the method that will select the best offer for each profile when configuring a decision. You can rank offers by:

* Offer priority
* Ranking formula
* [AI ranking](#use-ranking-strategy)

![](../assets/offer-rank-by.png)

## Offer priority {#offer-priority}

By default, when several offers are eligible for a given placement in a decision, the offers with the highest **priority** will be delivered to the customers first.

![](../assets/offer-priority.png)

Offers' priority scores are assigned when creating an offer. Learn how to create a personalized offer in [this section](../offer-library/creating-personalized-offers.md).

## Ranking formula {#assign-ranking-formula}

In addition to offer priority, Journey Optimizer allows you to create **ranking formulas**. These are formulas that determine which offer should be presented first for a given placement, rather than taking into account the offers' priority scores.

For example, you can boost the priority of all offers where the end date is less than 24 hours from now, or boost offers from the "running" category if the profile's point of interest is "running".

Learn how to create a ranking formula in [this section](../ranking/create-ranking-formulas.md).

Once a formula has been created, you can assign it to a placement in a decision. To do this, follow the steps below:

1. Create a decision or edit an existing one. See [Create decisions](../offer-activities/create-offer-activities.md).

1. Add the placements that will contain your offers. See [Create placements](../offer-library/creating-placements.md).

1. For each placement, add a collection. See [Create collections](../offer-library/creating-collections.md).

1. Select **[!UICONTROL Formula]** as the ranking method, then click **[!UICONTROL Add ranking]**.

    ![](../assets/offer-activity-ranking.png)

1. Select the desired formula, then click **[!UICONTROL Select]**.

    ![](../assets/ranking-selection.png)

The ranking formula is now associated to the placement.

If multiple offers are eligible to be presented in this placement, the decision will use the selected formula to calculate which offer to deliver first.

## AI ranking {#use-ranking-strategy}

<!--If you are an [Adobe Experience Platform](https://experienceleague.adobe.com/docs/experience-platform/landing/home.html){target="_blank"} user leveraging the **Offer Decisioning** application service,-->

You can also use a trained model system that automatically ranks offers to display for a given profile by selecting an AI model. Learn how to create an AI model in [this section](../ranking/create-ranking-strategies.md).

Once an AI model has been created, you can assign it to a placement in a decision. To do this this, follow the steps below:

1. Create a decision or edit an existing one. See [Create decisions](../offer-activities/create-offer-activities.md).

1. Add the placements that will contain your offers. See [Create placements](../offer-library/creating-placements.md).

1. For each placement, add a collection. See [Create collections](../offer-library/creating-collections.md).

1. Choose to rank offers by **[!UICONTROL AI ranking]** from the drop-down list, and click **[!UICONTROL Add ranking]**.

    ![](../assets/ranking-selection-ai-ranking.png)

1. Select the AI model that you created. All the details of the model are displayed.

    ![](../assets/ranking-selection-ai-ranking-selected.png)

1. Click **[!UICONTROL Select]**. The AI model is now associated with the placement.

If multiple offers are eligible, the trained model system will determine which offer should be presented first for a given placement.

