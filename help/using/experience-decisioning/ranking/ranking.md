---
title: Ranking methods
description: Learn how to work with ranking methods
feature: Decisioning, Ranking
topic: Integrations
role: User
level: Intermediate
exl-id: c1d69bc9-4486-4037-b218-f4f704b2ba9c
version: Journey Orchestration
TQID: https://experienceleague.adobe.com/1qUj05fLaRqqJGfaoL-y5uwtknp7HDkWKocHMde-8lc
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: a4cb03e1-327e-499d-9de8-e0c0db8a63a2
    internal-label: Decision capabilities (AJO)
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
level_v2:
  - id: b5a62a22-46f7-4f0d-b151-3fc640bef588
    internal-label: Intermediate
subfeature_v2:
  - id: a7a194a0-75e2-4913-8a83-14714fbf68e6
    internal-label: Decisioning API
  - id: eb547372-2a95-4d13-b0fd-f720c9895880
    internal-label: Edge Decisioning (AJO)
---
# Ranking methods {#rankings}

Ranking methods allow you to rank items to display for a given profile. Once a ranking method has been created, you can assign it to a selection strategy to define which items should be selected first.

Two types of ranking methods are available:

* **Formulas** allow you to define rules that will determine which item should be presented first, rather than taking into account the item's priority scores.

* **AI models** allow you to use trained model systems that will leverage multiple data points to determine which item should be presented first.

## Create ranking methods {#create}

To create a ranking method, follow these steps:

1. Navigate to the **[!UICONTROL Strategy setup]** menu, then select the **[!UICONTROL Formulas]** or **[!UICONTROL AI models]** menu depending on the type of ranking you want to use.

    ![](../assets/ranking-create.png)

1. Click the **[!UICONTROL Create formula]** or **[!UICONTROL Create AI model]** button in the upper-right corner of the screen.

    Detailed information on how to create ranking formulas and AI models is available in the following sections:

    * [Ranking formulas](ranking-formulas.md)
    * [AI models](ai-models.md)

1. Configure the formula or AI model to suit your needs, then save it.

Your ranking method is now ready to be used in a [selection strategy](../selection-strategies.md) to rank eligible decision items.


