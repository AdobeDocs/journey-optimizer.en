---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page answers frequently asked questions about Decisioning capabilities in Adobe Journey Optimizer, from getting started and the differences with Decision management to eligibility, capping rules, strategy sequence, ranking formulas and AI model behavior, and troubleshooting.

**Intents:**

* Find where to start with Decisioning and name the objects you configure in advance.
* Tell Decision management and Decisioning apart.
* Tell an audience from a decision rule.
* Understand what happens when multiple capping rules are applied to a single offer, and why the item with the highest score is not returned first.
* Understand how AI models (auto-optimization and personalized optimization) behave with new offers, collection changes, minimum traffic, similar offers, and traffic anomalies, and how they optimize without control groups.
* Troubleshoot why an item was not shown to a profile and find how long changes take to apply.

**Glossary:**

* **Decisioning** *(product-specific)*: The next-generation decisioning framework in Adobe Journey Optimizer. It offers a centralized catalog of marketing offers known as decision items, and a decision engine that leverages rules and ranking criteria to select and present the most relevant decision items to each individual.
* **Decision management** *(product-specific)*: The legacy decisioning framework in Adobe Journey Optimizer.
* **Decision items** *(product-specific)*: Offers or pieces of content in the Offers catalog. Each item has its own start and end dates, priority, eligibility, and capping rules. Decision items are integrated into messages and experiences across Journey Optimizer channels: code-based experience, web, email, mobile messages, push notifications, custom channels, and direct mail.
* **Collections** *(product-specific)*: Groups of items based on attribute rules.
* **Decision rules** *(product-specific)*: Reusable conditions that determine who qualifies. A decision rule runs against the individual profile every time a decision is made, and it can use profile attributes, audiences, and context data.
* **Ranking methods** *(product-specific)*: Set the order of the qualifying items: the item priority (default), a ranking formula, or an AI model.
* **Selection strategies** *(product-specific)*: Reusable objects that combine a collection, an eligibility constraint, and a ranking method.
* **Decision policies** *(product-specific)*: Put selection strategies in order, set how many items to return, and define optional fallback items. A decision policy is added to the content of a campaign or journey.
* **Placements (email only)** *(product-specific)*: Containers for the items displayed in an email.
* **Strategy sequence** *(product-specific)*: Selection strategies are evaluated in the order of the strategy sequence. The first selection strategy or decision item in the sequence has the highest priority. Selection strategies that you combine in a group have the same priority, so their qualifying items are ranked together according to their scores.
* **Audience**: A list of profiles that Adobe Experience Platform computes from profile attributes and experience events. It is not recomputed when a decision is made, so it might not be up to date.
* **Auto-optimization** *(product-specific)*: An AI model that serves traffic to the next best available offer based on traffic data from the last 14 days.
* **Personalized optimization** *(product-specific)*: An AI model that uses traffic data from the last 30 days.
* **Explore-exploit strategy**: The "explore-exploit" strategy that both auto-optimization and personalized optimization models employ, which eliminates the need for dedicated control groups. Models begin with 100% exploration, testing different offers to establish baseline performance data. As behavioral events accumulate and prediction accuracy improves, the models automatically balance exploration and exploitation. The system progressively allocates more traffic to high-performing offers while continuing to test alternatives.
* **Datasets (in AI models)**: Capture conversion events (clicks, orders, revenue) that serve as optimization targets for the model.
* **Audiences (in AI models)**: Function as predictor variables that enable the model to personalize recommendations based on customer segment membership. Audiences do not restrict or expand the model's scope. Instead, they provide contextual attributes that improve the model's ability to make personalized predictions across different customer segments. The page states that both components (datasets and audiences) are required for effective performance of personalized optimization models.

**Guardrails:**

* Minimum traffic thresholds for effective AI model performance (recommended): Adobe recommends 1,000 impressions per offer/item per week and 100 conversion events per offer/item per week.
* By default, the system will not attempt to build personalized models for offers/items with fewer than 1,000 impressions or 50 conversion events (default).
* In production environments with large offer catalogs (~300 offers) and restrictive business rules, some offers may approach lower absolute thresholds (250 impressions and 25 conversions per 30 days). These represent the minimum data requirements for model training but may not guarantee optimal performance.
* Changes to offer collections (auto-optimization and personalized optimization models): the page states that when several offers are removed simultaneously and the remaining offers have minimal traffic data within the 14-day or 30-day window, the model may exhibit suboptimal behavior, including random distribution patterns or bias toward offers with higher conversion rates based on limited impression data.

**Prerequisites and permissions:**

* Decisioning is only available to users with access to a Decisioning related role, such as Decision managers.
* Decisioning Explainer: available to customers who have access to Coworker and Decisioning.

**Terminology:**

* Canonical name: Decisioning — variants: next-generation decisioning framework, next-generation framework and feature set.
* Canonical name: Decision management — variants: legacy decisioning framework.
* Example of mapping stated by the page (the objects of the two frameworks do not always map one to one): an offer becomes a decision item; a decision maps to a selection strategy and a decision policy.
* Do not confuse: "Decision management" ≠ "Decisioning" (legacy framework versus next-generation framework).
* Do not confuse: "audience" ≠ "decision rule" (they are evaluated differently, see the Glossary).
* Do not confuse: "auto-optimization" ≠ "personalized optimization" (two AI models, see the Glossary).

**FAQ:**

* **What is the difference between Decision management and Decisioning?** Decision management is the legacy decisioning framework. Decisioning is the next-generation framework and feature set, which offers significant capabilities and benefits over Decision management, for example schema-based items, reusable decision logic, experimentation, and integrated authoring. In Decision management, decision logic is tied to a specific placement.
* **What is the difference between an audience and a decision rule?** Both restrict who can receive an item, or who a selection strategy applies to, but they are evaluated differently. An audience is not recomputed when a decision is made, so it might not be up to date. A decision rule runs against the individual profile every time a decision is made, so each profile gets the latest result.
* **What happens when multiple capping rules are applied to a single offer?** An offer is capped as soon as any single condition is met. The offer stops being displayed once any rule reaches its threshold.
* **Why is the item with the highest score not returned first?** Selection strategies are evaluated in the order of the strategy sequence. The items of a later group are placed after the items of the earlier groups, whatever their score.
* **How long do changes take to apply?** Changes to a decision policy and to the objects it uses can take up to 15 minutes to propagate across all data regions, and up to 30 minutes for Canada. This includes adding an item to a collection, changing a rule or the content of an item, and updating a formula. A capping counter can take up to 3 seconds to update. After you approve an item or create a capping rule, it can take up to 15 minutes before events are counted toward the cap.
* **How quickly do AI models incorporate new offers?** Auto-optimization identifies and begins testing new offers on its next training cycle. Its training occurs 3 to 4 times daily, approximately every 6 hours. Personalized optimization identifies and begins testing new offers as they are added to the offer strategy, includes them in random exploration traffic, and personalizes them in the model's next training cycle, which occurs on a weekly basis. Once identified, both models start serving the new offers to some visitors immediately in order to test their performance.

**Troubleshooting:**

* An item was not shown to a profile: go through the troubleshooting checklist, which covers the dates and status of the item, the collection, the eligibility of the profile, capping rules, the order of the strategies and the number of items requested, fallback items, and recent changes. You can also ask the Decisioning Explainer why an offer was or was not shown to a profile or segment.

**Examples:**

* Collection: all the items where the `Category` attribute is `Yoga`.
* Capping rules: an offer has two capping rules, 5 times per profile per week and 100 times total across all users. The offer stops being displayed to a user once they have seen it 5 times in a week, even if the total cap of 100 has not been reached yet. Once 100 total impressions are reached, the offer stops being displayed to all users.
* Strategy sequence: the page states that in the example on the How Decisioning works page, Offer 6 has the highest score (60) but comes last, because it belongs to the group with the lower priority.
* Similar offers (AI models): offers with objectively superior value propositions (for example, a €100 discount versus a €50 discount) will typically dominate across all customer segments regardless of personalization efforts.
* Traffic anomalies (AI models): a temporary traffic spike (for example, twice the daily traffic) has minimal effect on overall model performance because the anomalous traffic represents a small fraction of the 30-day dataset.

**Best practices:**

* Recommendation (auto-optimization and personalized optimization models): when modifying offer collections significantly, verify that remaining offers have sufficient historical performance data to maintain model effectiveness.
* Recommendation (AI models): design offers with meaningful differentiation that align with distinct customer segment preferences to maximize AI model effectiveness.

**Related pages:**

* To learn more about Decisioning: Decisioning (experience-decisioning/gs-experience-decisioning.md)
* Where to start, to see how decision items, collections, rules, ranking methods, selection strategies, and decision policies fit together: How Decisioning works (experience-decisioning/how-decisioning-works.md)
* Where to start, to check the prerequisites: prerequisites (experience-decisioning/gs-experience-decisioning.md)
* Where to start, to set up decision items, collections, rules, ranking methods, selection strategies, and a decision policy: key steps (experience-decisioning/gs-experience-decisioning.md)
* In the key concepts answer, to learn more about the building blocks of Decisioning: the building blocks of Decisioning (experience-decisioning/how-decisioning-works.md)
* To learn more about how Decision management objects map to Decisioning: how Decision management objects map to Decisioning (experience-decisioning/how-decisioning-works.md)
* To learn more about the benefits of migrating to Decisioning: benefits of migrating to Decisioning (experience-decisioning/migrate-to-decisioning.md)
* To move Decision management objects: migration tooling (experience-decisioning/decisioning-migration-api.md)
* To learn more about audiences and decision rules: audiences and decision rules (experience-decisioning/decisioning-troubleshooting.md)
* To learn more about capping rules: capping rules (experience-decisioning/items.md)
* To learn more about what happens when a decision is requested: what happens when a decision is requested (experience-decisioning/how-decisioning-works.md)
* When configuring AI models with datasets and audiences: AI models (experience-decisioning/ranking/ai-models.md)
* For personalized optimization models, in the answer on datasets and audiences: personalized optimization models (experience-decisioning/ranking/personalized-optimization-model.md)
* To learn more about auto-optimization: auto-optimization (experience-decisioning/ranking/auto-optimization-model.md)
* To learn more about personalized optimization: personalized optimization (experience-decisioning/ranking/personalized-optimization-model.md)
* In the answer on minimum traffic requirements for AI models, to learn more about data collection requirements: data collection requirements (experience-decisioning/data-collection/data-collection.md)
* When an item does not appear as expected or was not shown to a profile: troubleshooting checklist (experience-decisioning/decisioning-troubleshooting.md)
* To learn when changes take effect: when changes take effect (experience-decisioning/decisioning-troubleshooting.md)
* To ask why an offer was or was not shown to a profile or segment: Decisioning Explainer (experience-decisioning/experience-decisioning-coworker-skills.md)

**Personas:**

* **marketer:** Can follow the key steps to set up decision items, collections, rules, ranking methods, selection strategies, and a decision policy. Can add a decision policy to the content of a campaign or journey. Can ask the Decisioning Explainer why an offer was or was not shown to a profile or segment. The page states that Decisioning is only available to users with access to a Decisioning related role, such as Decision managers. Where: "Getting started".

**Onboarding:**

* **Level:** Intermediate
* **First minimal step:** Read How Decisioning works to see how decision items, collections, rules, ranking methods, selection strategies, and decision policies fit together.
* **Previous:** To see how decision items, collections, rules, ranking methods, selection strategies, and decision policies fit together: How Decisioning works (experience-decisioning/how-decisioning-works.md); To check the prerequisites: prerequisites (experience-decisioning/gs-experience-decisioning.md)
* **Next:** To set up decision items, collections, rules, ranking methods, selection strategies, and a decision policy: key steps (experience-decisioning/gs-experience-decisioning.md); When an item does not appear as expected: troubleshooting checklist (experience-decisioning/decisioning-troubleshooting.md)

+++

<!-- ai-section-version: 1 | source-hash: 54a78248 -->
