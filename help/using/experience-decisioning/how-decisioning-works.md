---
solution: Journey Optimizer
product: journey optimizer
title: How Decisioning works
description: Understand how decision items, rules, ranking, selection strategies, and decision policies work together to choose the best items for each profile.
feature: Decisioning
topic: Personalization
role: User
level: Beginner, Intermediate
keywords: decisioning, decision policy, selection strategy, collection, decision item, eligibility, ranking, capping, fallback
---
# How Decisioning works {#how-decisioning-works}

>[!BEGINSHADEBOX]

**On this page:** Understand how decision items, collections, rules, ranking methods, selection strategies, and decision policies fit together, and what Decisioning does each time a profile needs content, so you can set up decisions with confidence.

>[!ENDSHADEBOX]

Feeling lost among all the Decisioning terms? This page is here to help. You do not need to memorize anything: think of it as a map of Decisioning that shows what each piece is for and how the pieces connect, so you can find your way before you start to build.

Decisioning chooses the best decision items for each profile. You create decision items in the Offers catalog, then define who can receive each item and how the items are ranked. When a profile needs content in a message or experience that contains a decision policy, the decision engine evaluates the policy and returns the items to use.

Behind every decision are five questions. Here are the objects that answer them:

![Diagram of the five questions behind every decision and the objects that answer them. Who qualifies, and how often? The profile and context data, audiences, decision rules, and capping rules. What can be shown? Decision items and collections. How are items chosen? Ranking methods, selection strategies, and the decision policy. Where is it delivered? Channel configurations, placements (email only), and the content of campaigns and journeys. Why: is it working? Decision events and reports.](assets/decisioning-five-questions.png){zoomable="yes"}

This page is a concept guide. It explains what each object that the decision engine works with is for, how the objects connect, and what the engine does when a profile needs content. It does not describe how to create the objects in the interface. To find out why an item was or was not selected, see [Troubleshoot Decisioning](decisioning-troubleshooting.md).

To set up Decisioning, use [Get started with Decisioning](gs-experience-decisioning.md#prerequisites). It is a task guide that lists the permissions you need and the order in which to create the objects, and it links to the procedure for each one.

>[!NOTE]
>
>This page describes Decisioning. To compare it with the legacy Decision management framework, see [Coming from Decision management?](#compare)

## The building blocks {#building-blocks}

The decision engine does not choose content on its own: it applies the objects that you configure in advance. These objects are the building blocks of the decisioning mechanism. Each one answers a question the engine must resolve when it selects items for a profile: which items are candidates, who qualifies for them, in which order they are presented, and how many are returned.

![Diagram of the Decisioning building blocks and how they connect. Decision items, which have dates, a priority, capping rules, an approval status, and an eligibility constraint, are grouped in collections. A selection strategy combines a collection, an eligibility constraint, and a ranking method. A decision policy puts selection strategies in sequence, sets the number of items, and defines fallback items. You can also add individual items straight to the policy. Decision rules decide who qualifies, ranking methods set the order, and the policy is inserted in the content of your channels.](assets/decisioning-building-blocks-adobe.png){zoomable="yes"}

In short: decision items are grouped in collections. A selection strategy combines a collection with an eligibility constraint and a ranking method. A decision policy puts one or more selection strategies in order and returns the best items to your content.

The table below lists these objects in the order in which they build on each other, and links to the task documentation. The first column shows which of the five questions each object answers.

| Question | Object | Role in the decision | Where to configure it |
| --- | --- | --- | --- |
| What | **Catalog** | The container of your decision items. A catalog is linked to a schema that defines all the attributes you can assign to an item, and you can add custom attributes to it. | **[!UICONTROL Decisioning]** > **[!UICONTROL Catalogs]**, then **[!UICONTROL Edit schema]** in the items list. [Configure the item catalog](catalogs.md) |
| What | **Decision item** | An offer or piece of content in the Offers catalog. Each item has its own start and end dates, priority, eligibility (audiences or a decision rule), and capping rules. You approve an item when it is ready to be presented to profiles. | **[!UICONTROL Decisioning]** > **[!UICONTROL Catalogs]**. [Create decision items](items.md) |
| What | **Collection** | Groups items with attribute rules, for example all the items where the `Category` attribute is `Yoga`. | **[!UICONTROL Catalogs]** > **[!UICONTROL Collections]**. [Manage item collections](collections.md) |
| Who | **Decision rule** | A reusable condition that determines who qualifies. You can apply a rule to a decision item or to a selection strategy. | **[!UICONTROL Decisioning]** > **[!UICONTROL Strategy setup]** > **[!UICONTROL Rules]**. [Create decision rules](rules.md) |
| How | **Ranking method** | Sets the order of the qualifying items: the item priority (default), a ranking formula, or an AI model. | **[!UICONTROL Decisioning]** > **[!UICONTROL Strategy setup]** > **[!UICONTROL Formulas]** or **[!UICONTROL AI models]**. [Ranking methods](ranking/ranking.md) |
| How | **Selection strategy** | A reusable object that combines a collection, an eligibility constraint (an audience or a decision rule), and a ranking method. | **[!UICONTROL Decisioning]** > **[!UICONTROL Strategy setup]** > **[!UICONTROL Selection strategies]**. [Create selection strategies](selection-strategies.md) |
| How | **Decision policy** | Puts selection strategies in order, sets how many items to return, and defines optional fallback items. | Added to the content of a campaign or journey. [Create decision policies](create-decision-policy.md) |
| Where | **Placement** (email only) | A container for the items displayed in an email. When you create a placement, you associate it with a channel configuration. Placements also let you track how items perform in each location. | **[!UICONTROL Decisioning]** > **[!UICONTROL Strategy setup]**. [Work with placements](placements.md) |

A decision policy can also include individual decision items, which you add one at a time. An individual item skips the collection and the selection strategy, but the eligibility constraints set on the item still apply. [Learn how to add items and strategies to a policy](create-decision-policy.md#strategy)

You can use a decision policy in code-based experiences, web, email, push notifications, mobile messages, custom channels, and direct mail. In journeys, the [Content decision activity](../building-journeys/content-decision.md) returns items that you can use in an [Optimize activity](../building-journeys/content-decision.md#add-condition-activity) or in a custom action. Its output cannot be used in native channel activities.

## What happens when a decision is requested {#decision-process}

![Diagram of a decision request in four stages: Context (step 1), Filtering (steps 2 and 3), Ranking and selection (steps 4 to 6), and Delivery (step 7). Decision events then go back to Adobe Experience Platform (step 8), where they feed capping counters, reports, and AI models.](assets/decisioning-request-stages.png){zoomable="yes"}

Each time a profile needs content in a message or experience that contains a decision policy, Decisioning evaluates the policy for that profile. The diagram groups the following steps into four stages: **Context** (step 1), **Filtering** (steps 2 and 3), **Ranking and selection** (steps 4 to 6), and **Delivery** (step 7). Step 8 sends the results back to Adobe Experience Platform.

1. **The request arrives.** Decisioning receives the profile and, if you use it, context data. Context data is sent in at the time of the request and does not include historical data. [Learn more about context data](context-data.md)

1. **Decisioning goes through the strategy sequence in order.** The first selection strategy or decision item in the sequence has the highest priority. Selection strategies that you combine in a group have the same priority and are evaluated together.

1. **Each selection strategy keeps only the items that qualify.** Decisioning starts from the items in the collection of the strategy. An item is kept when the profile meets the constraints you set, for example:

    * The current date is within the start and end dates of the item.
    * The profile meets the eligibility constraint of the item (an audience or a decision rule).
    * The profile meets the eligibility constraint of the selection strategy (an audience or a decision rule).
    * No capping rule of the item has reached its threshold.

    [Learn more about eligibility](decisioning-troubleshooting.md#eligibility)

1. **The qualifying items are ranked.** The ranking method of the selection strategy sets the order: the item priority (default), a ranking formula, or an AI model. [Learn more about ranking](decisioning-troubleshooting.md#ranking)

1. **The selection strategies are combined.** The qualifying items of the strategies in a group are ranked together according to their scores. An item that qualifies in several strategies keeps its highest score. The items of a later group are placed after the items of the earlier groups, and an item that is already ranked is not evaluated again. See the example below.

1. **The best items are selected.** Decisioning returns the first items of the ranked list, up to the number of items requested in the policy. Push notifications and mobile messages return one item. If no item qualifies, Decisioning returns the fallback items you defined. Without fallback items, nothing is displayed. [Learn more about fallback items](decisioning-troubleshooting.md#fallback)

1. **The items are used in your content.** The attributes of the returned items are available as personalization variables. In an email, an item is not repeated across the decision policies of the same message. A policy that has no other item to show displays its fallback item or a blank space. To show the same item in several places, reuse the output of an existing decision policy. [Personalize with decision item attributes](use-decision-policy.md#attributes)

1. **Events feed back into Decisioning.** Information about each decision is sent automatically to Adobe Experience Platform as a decision event. Impressions and clicks are tracked automatically in emails authored in [!DNL Journey Optimizer], but most other channels require your implementation to send them to Experience Platform as experience events. Capping counters, reports, and AI models are based on these events. [Learn more about data collection](data-collection/data-collection.md)

+++Example: groups and scores

In the following example, a decision policy has three selection strategies. Strategy 1 and Strategy 2 are combined in Group 1. Strategy 3 is alone in Group 2.

![Diagram of a decision policy with three selection strategies in two groups. Group 1: Strategy 1 qualifies Offer 1 (10), Offer 2 (20), and Offer 3 (30); Strategy 2 qualifies Offer 3 (45), Offer 4 (40), and Offer 5 (50). Group 2: Strategy 3 qualifies Offer 5, which is already ranked, and Offer 6 (60). The ranked list is Offer 5, Offer 3, Offer 4, Offer 2, Offer 1, and then Offer 6. If the policy requests three items, the first three are returned.](assets/decisioning-groups-scores.png){zoomable="yes"}

| Group | Selection strategy | Qualifying offers and scores |
| --- | --- | --- |
| Group 1 | Strategy 1 | Offer 1 (10), Offer 2 (20), Offer 3 (30) |
| Group 1 | Strategy 2 | Offer 3 (45), Offer 4 (40), Offer 5 (50) |
| Group 2 | Strategy 3 | Offer 5 (already ranked, so it is skipped), Offer 6 (60) |

1. Decisioning ranks Group 1 as a whole. Offer 3 qualifies in both strategies, so it keeps its highest score (45). The ranked list is Offer 5 (50), Offer 3 (45), Offer 4 (40), Offer 2 (20), and Offer 1 (10).

1. Decisioning then adds Group 2. Offer 5 is already in the list, so only Offer 6 is added, at the end of the list.

The final ranked list is Offer 5, Offer 3, Offer 4, Offer 2, Offer 1, and Offer 6. If the policy requests three items, Decisioning returns Offer 5, Offer 3, and Offer 4. Offer 6 has the highest score (60) but comes last, because it belongs to the group with the lower priority.

[Learn more about strategy sequences](create-decision-policy.md#strategy)

+++

## Coming from Decision management? {#compare}

Decision management is the legacy decisioning framework in [!DNL Journey Optimizer]. The objects of the two frameworks do not always map one to one. The table shows how the [migration tooling](decisioning-migration-api.md#entity-mapping) maps Decision management objects to Decisioning objects.

| Decision management | Decisioning | Notes |
| --- | --- | --- |
| Offer | Decision item | A decision item is defined by the schema of the catalog, which you can extend with custom attributes. |
| Collection | Collection | Collection qualifiers are migrated as tags. |
| Rule | Decision rule | |
| Ranking formula | Ranking formula | |
| Decision | Selection strategy, decision policy, and code-based experience campaign | For each migrated decision scope, the migration tooling creates one selection strategy (a collection, an eligibility rule, and a ranking formula), one decision policy (the number of items, the selection strategy, and a fallback item), and one code-based experience campaign. |
| Placement | Channel configuration (not a Decisioning placement) | The migration tooling creates a channel configuration for each Decision management placement. It does not create Decisioning placements, which are currently available for email only and are associated with a channel configuration. You create them manually. |

To learn about the benefits of Decisioning and the migration tooling, see [Benefits of migrating to Decisioning](migrate-to-decisioning.md).

## Learn more {#learn-more}

* [Get started with Decisioning](gs-experience-decisioning.md)
* [Troubleshoot Decisioning](decisioning-troubleshooting.md)
* [Decisioning FAQ](decisioning-faq.md)
* [Decisioning guardrails & limitations](decisioning-guardrails.md)
* [Coworker for Decisioning](experience-decisioning-coworker-skills.md)
* [Report on Decisioning](cja-reporting.md)

{{$include /help/_includes/do-not-localize/experience-decisioning/ai-augmented-how-decisioning-works.md}}
