---
solution: Journey Optimizer, Experience Platform
product: Journey Optimizer
title: Offer Library User interface
description: Learn more about the Offer Library User Interface
badge: label="Legacy" type="Informative"
feature: Decision Management
topic: Integrations
role: User
level: Beginner, Intermediate
exl-id: 722f9c3b-b505-48c0-b126-31a7a841c245
version: Journey Orchestration
TQID: https://experienceleague.adobe.com/FVJLylzuMC26anLVrWdBeU2RFrM6EFquGJN6e2ZAuP8
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: a4cb03e1-327e-499d-9de8-e0c0db8a63a2
    internal-label: Decision capabilities (AJO)
  - id: ad78185d-8f79-40ad-9bad-cbde74af74ee
    internal-label: Guardrails and limitations
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
level_v2:
  - id: b5a62a22-46f7-4f0d-b151-3fc640bef588
    internal-label: Intermediate
  - id: e8ccd51f-da0d-4e3b-939b-e30d5ebb1ea5
    internal-label: Beginner
topic_v2:
  - id: f4e6943a-c91a-4134-a2c7-f4f20cfff2f0
    internal-label: Privacy
subfeature_v2:
  - id: a7a194a0-75e2-4913-8a83-14714fbf68e6
    internal-label: Decisioning API
  - id: eb547372-2a95-4d13-b0fd-f720c9895880
    internal-label: Edge Decisioning (AJO)
---
# Offer library user interface {#user-interface}

>[!TIP]
>
>Decisioning, [!DNL Adobe Journey Optimizer]'s new decisioning capability, is now available via the code-based experience and email channels! [Learn more](../../experience-decisioning/gs-experience-decisioning.md)

The **[!UICONTROL Decision management]** section in the left rail provides two menus that give you access to decision management capabilities: 

Use the **[!UICONTROL Offers]** menu to manage and deliver your offers:


![](../assets/offers_menu.png)

* **[!UICONTROL Overview]**: New to [!DNL decision management]? Follow the on-screen steps to get started with setting up placements, offers, and collections. When already familiar with [!DNL decision management], get an overview on your most recent offers, collections and decisions. [Learn more](#overview)
* **[!UICONTROL Offers]**: Create and access your personalized and fallback offers. Learn how to create [offers](../offer-library/creating-personalized-offers.md) and [fallback offers](../offer-library/creating-fallback-offers.md)
* **[!UICONTROL Collections]**: Organize your offers into static and dynamic collections. [Learn more](../offer-library/creating-collections.md)
* **[!UICONTROL Decisions]**: Create and manage decisions to deliver your offers. [Learn more](../offer-activities/create-offer-activities.md)
* **[!UICONTROL Batch decisioning]**: Deliver offer decisions to all profiles in a given Adobe Experience Platform audience. [Learn more](../batch-delivery.md)
* **[!UICONTROL Simulation]**: Validate your decisioning logic by simulating which offers will be delivered to a test profile for a given placement. [Learn more](../offer-activities/simulation.md)

Use the **[!UICONTROL Components]** menu to create and manage components that are required to create offers and decisions:

![](../assets/offer_activities.png)

* **[!UICONTROL Placements]**: Create and manage placements where your offers will display. [Learn more](../offer-library/creating-placements.md)
* **[!UICONTROL Collection qualifiers]**: Create and manage collection qualifiers (previously known as "tags") to organize and filter your offers. [Learn more](../offer-library/creating-tags.md)
* **[!UICONTROL Rules]**: Manage the conditions under which your offers are presented. [Learn more](../offer-library/creating-decision-rules.md)
* **[!UICONTROL Ranking]**: Create and manage ranking formulas to determine which offer should be presented first for a given placement. [Learn more](../ranking/create-ranking-formulas.md)

>[!NOTE]
>
>If you are experiencing issues accessing decision management or some of its features, check with an Admin user that you have been granted the required rights. See [Grant access to Decision Management](starting-offer-decisioning.md#granting-acess-to-decision-management).

## Overview {#overview}

When you are new to [!DNL decision management], the **[!UICONTROL Overview]** tab guides you through the main steps needed to start building your first offer decision. Follow the on-screen steps to start creating placements, offers, and collections. Once you are done with these first steps, you are prompted to created offer decisions.

>[!NOTE]
>
>The main steps to create offers and use them in a decision are presented in [this section](../offer-library/key-steps.md).

When you are more familiar with [!DNL decision management] and you have already created at least one offer decision, the **[!UICONTROL Overview]** tab displays your most recent offers, collections and decisions.

Click an offer or a decision to directly access the selected item's details.

Click the **[!UICONTROL View all]** button to access the offer, collection, or decision lists.

![](../assets/overview_view-all.png)

## Search and filter information {#search-and-filter-information}

Use the **search bar** to find a specific item.

**Filters** can also be accessed by clicking the filter icon on the top left of the list. They allows you to filter the displayed elements according to different criteria. You can, for example, filter the placements that have been created for the email communication channel and image-type contents.

![](../assets/filters.png)

## Customize displayed information {#customize-displayed-information}

Lists from Decision Management menus can be personalized using the configuration button on the top right of the lists.

This allows you to choose the information to display according to your needs.

Note that columns customization is saved for each user.

![](../assets/columns.png)

## Information pane {#information-pane}

In the different lists, select an element to display an information pane that will allow you to retrieve information and perform basic actions on the element. 

![](../assets/information-pane.png)

The offers and decisions lists also allow you to perform bulk actions on several elements. To do this, select the desired offers or decisions, then select the action you want to perform from the information pane. 

Note that you can also duplicate an existing offer or decisions in order to create a copy with the **[!UICONTROL Draft]** status. This can be performed either from the information pane or from an offer or a decision's detailed view.

## Offers and decisions change logs {#changes-logs}

[!DNL Journey Optimizer] allows you to visualize all the changes that have been made to an offer or a decision. To do this, access the **[!UICONTROL Audits]** menu from the left menu. [Learn how to audit actions on resources](../../privacy/audit-logs.md)
