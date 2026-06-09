---
solution: Journey Optimizer
product: Journey Optimizer
title: Get started with AI models
description: Learn about AI models that allow to rank offers
feature: Ranking, Decisioning
topic: Artificial Intelligence
role: User
level: Intermediate
exl-id: 07679823-2288-4528-b09a-12fd76a69482
version: Journey Orchestration
TQID: https://experienceleague.adobe.com/sWJEr5Pm1wl83Q-2HVb-7mqy7hasQ1ffqRDmJsOFomw
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
level_v2:
  - id: b5a62a22-46f7-4f0d-b151-3fc640bef588
    internal-label: Intermediate
topic_v2:
  - id: bbbea26f-9621-49eb-9ab8-e06fb3bbce8c
    internal-label: Artificial intelligence
  - id: cdd65e7e-8839-44a2-bc21-0e03623b5dd1
    internal-label: Optimization
  - id: d3cdead0-685a-4489-9250-4bb709942f66
    internal-label: Data collection
feature_v2:
  - id: a4cb03e1-327e-499d-9de8-e0c0db8a63a2
    internal-label: Decision capabilities
subfeature_v2:
  - id: a7a194a0-75e2-4913-8a83-14714fbf68e6
    internal-label: Decisioning API
  - id: eb547372-2a95-4d13-b0fd-f720c9895880
    internal-label: Edge Decisioning
  - id: e30b0a1a-b594-47b8-af94-1e3a2be6df11
    internal-label: Get started
---
# Get started with AI models {#ai-models}

[!DNL Journey Optimizer] allows you to use a trained model system that ranks offers to display for a given profile.

This feature enables you to create different **AI models** based on your business goals. Using these different goal-based strategies in a decision, the trained model system will help you understand how the different AI models are impacting your goals.

<!--
For example, you can select an AI model for the email channel and another one for the push channel. For each channel, the trained model system will leverage multiple data points to determine which offer should be presented first for a given decision policy?, rather than taking into account the offers' priority scores or a [ranking formula](create-ranking-formulas.md).

>[!IMPORTANT]
>
>For now, ranking models are not supported in Journey Optimizer authored channels.
-->

## AI model types {#ai-model-types}

>[!CONTEXTUALHELP]
>id="ajo_exd_ai_model_type"
>title="Choose the model type"
>abstract="Select the type of AI model you want to create: **Auto-optimization** optimizes offers based on past offer performance, while **Personalized optimization** optimizes and personalizes offers based on audiences and offer performance."
>additional-url="https://experienceleague.adobe.com/en/docs/journey-optimizer/using/decisioning/offer-decisioning/rankings/ai-models/create-ranking-strategies#create-ranking-strategy" text="Create an AI model"

Two types of AI models are available in [!DNL Journey Optimizer]:

* **Auto-optimization models** aim to serve offers that maximize the return (KPIs) set by business clients. These KPIs could be in the form of conversion rates, revenue, etc. At this point, Auto-optimization focuses on optimizing offer clicks with offer conversion as our target. Auto-optimization is non-personalized and optimizes based on "global" performance of the offers. [Learn more](auto-optimization-model.md)

* **Personalized optimization models** allow you to define business goals and utilizes customer data to train business-oriented models to serve personalized offers and maximize KPIs. [Learn more](personalized-optimization-model.md)

## Build an AI model {#create-ai-model}

The main steps to be able to create and use AI models are as follows:

1. Create a dataset where conversion and impression events will be collected. [Learn more](../data-collection/create-dataset.md)

1. Create an AI model that will leverage events from the dataset to rank offers. [Learn more](create-ai-models.md)

1. Configure your offer schema to automatically capture events. [Learn more](../data-collection/schema-requirement.md)

    >[!IMPORTANT]
    >
    >Ranking models require feedback events to be sent in as experience events in order to be collected. [Learn more about Decisioning data collection](../data-collection/data-collection.md)

1. Assign the AI model to a selection strategy to rank eligible offers. [Learn more](../selection-strategies.md#select-ranking-method)

1. Monitor your AI model's training status and performance. [Learn more](ai-model-observability.md)
