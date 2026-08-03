---
title: Get started with [!DNL Journey Optimizer] decision capabilities
description: Learn how to work with [!DNL Journey Optimizer] decision capabilities.
feature: Decisioning
topic: Integrations
role: User
level: Experienced
exl-id: 008d42c7-a523-4857-b34e-0e8dd1dfa507
version: Journey Orchestration
TQID: https://experienceleague.adobe.com/y5aC7N-3FKFf9RQLHV40YtOR4EwHi3EWil-QFVL2tEI
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: a4cb03e1-327e-499d-9de8-e0c0db8a63a2
    internal-label: Decision capabilities
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
topic_v2:
  - id: a004cc84-67b9-4a33-a3a7-8ec7273ef4dc
    internal-label: Metadata
  - id: bcc5edb5-84c3-4940-9f84-ed88b6c16274
    internal-label: Experimentation
  - id: e0eb8757-182f-49f3-94a4-1587d16f5094
    internal-label: Personalization
  - id: fd2e3797-f2ea-4b36-a9af-52acf5e90513
    internal-label: Customer profiles
subfeature_v2:
  - id: a7a194a0-75e2-4913-8a83-14714fbf68e6
    internal-label: Decisioning API
  - id: eb547372-2a95-4d13-b0fd-f720c9895880
    internal-label: Edge Decisioning
  - id: e30b0a1a-b594-47b8-af94-1e3a2be6df11
    internal-label: Get started
---
# Get started with decision capabilities in [!DNL Journey Optimizer] {#gs-decision}

>[!BEGINSHADEBOX]

**On this page:** Compare the Decisioning and Decision management capabilities in Journey Optimizer so you can choose the right approach for delivering personalized offers across your channels.

>[!ENDSHADEBOX]

The decision capabilities in [!DNL Journey Optimizer] empower you to deliver the best offers and personalized experiences to your customers across all touchpoints, at precisely the right moments. These capabilities simplify personalization through a centralized catalog of marketing offers and an advanced decision engine, which uses rules and ranking criteria to deliver the most relevant content for each individual.

Key benefits:

* Improved campaign performance by delivering personalized offers across multiple channels,
* Improved workflows: instead of creating multiple deliveries or campaigns, marketing teams can improve workflows by creating a single delivery and vary the offers in different parts of the template,
* Control over the number of times an offer is shown across campaigns and customers.

Currently, [!DNL Journey Optimizer] provides the two core solutions detailed below.

## Decisioning {#decisioning}

![](assets/gs-decisioning.png)

Our next-generation decision framework, designed to unify existing Journey Optimizer workflows and lay the foundation for managing additional content catalogs. Decisioning offers:

* Schema-based item catalog management: Increase flexibility by associating customized metadata with each offer
* Flexible collection rules: Easily group offers for future evaluation based on various criteria
* Updated decision policy and selection strategy configuration: Allow reusability of decision components
* Experimentation capabilities: Test decision logic against other content components to measure performance

Decisioning is available to all customers for the **Code-based Experience**, **Email**, **Push notification**, and **SMS** channels. For full details about the release cycle and availability phases, see [Journey Optimizer release cycle](../rn/releases.md).

➡️ [Get started with Decisioning](../experience-decisioning/gs-experience-decisioning.md)

>[!NOTE]
>
>To migrate from Decision management to Decisioning, refer to the [migration documentation](../experience-decisioning/migrate-to-decisioning.md) and [Migration API guide](../experience-decisioning/decisioning-migration-api.md).

## Decision management {#decision-management}

![](assets/gs-decision-management.png)

Our established feature in Journey Optimizer, Decision Management uses a central library of marketing offers and a decision engine that applies rules and constraints to real-time customer profiles, leveraging Adobe Experience Platform data to deliver the right offer at the right time.

Decision Management supports the following channels: Email, In-App messaging, Push notifications, SMS, and Direct mail.

➡️ [Get started with Decision management](../offers/get-started/starting-offer-decisioning.md)
