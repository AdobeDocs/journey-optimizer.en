---
title: Ranking methods
description: Learn how to work with ranking methods
feature: Experience Decisioning, Ranking
topic: Integrations
role: User
level: Intermediate
badge: label="Limited Availability"
exl-id: c1d69bc9-4486-4037-b218-f4f704b2ba9c
---
# Ranking methods {#rankings}

>[!CONTEXTUALHELP]
>id="ajo_exd_config_formulas"
>title="Create ranking formulas"
>abstract="Formulas allow you to define rules that will determine which item should be presented first, rather than taking into account the item's priority scores. Once a ranking method has been created, you can assign it to a selection strategy to define which items should be selected first."

Ranking methods allow you to rank items to display for a given profile. Once a ranking method has been created, you can assign it to a selection strategy to define which items should be selected first.

Two types of ranking methods are available:

* **Formulas** allow you to define rules that will determine which item should be presented first, rather than taking into account the item's priority scores.

* **AI models** allow you to use trained model systems that will leverage multiple data points to determine which item should be presented first.

## Create ranking methods {#create}

To create a ranking method, follow these steps:

1. Navigate to the **[!UICONTROL Strategy setup]** menu then select the **[!UICONTROL Formulas]** or **[!UICONTROL AI models]** menu depending on the type of ranking you want to use.

1. Click the **[!UICONTROL Create formula]** or **[!UICONTROL Create AI model]** button in the upper-right corner of the screen.

    ![](assets/ranking-create.png)

1. Configure the formula or AI model to suit your needs then save it.

    Detailed information on how to create ranking formulas and AI models are available in the decision management documentation:

    * [Ranking formulas](../offers/ranking/create-ranking-formulas.md)
    * [AI models](../offers/ranking/ai-models.md)


## Leverage decision items attributes in formulas {#items}

Ranking formulas are expressed in **PQL syntax** and can leverage various attributes such as profile attributes, [context data](context-data.md) and attributes related to your decision items.

To leverage attributes related to your decision items in formulas, make sure you follow the syntax below in your ranking formula's code. Expand each section for more information:

+++Leverage decision items standard attributes

![](assets/formula-attribute.png)

+++

+++Leverage decision items custom attributes

![](assets/formula-attribute-custom.png)

+++
