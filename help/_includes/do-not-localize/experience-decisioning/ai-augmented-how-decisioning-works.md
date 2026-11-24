---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This concept guide explains what each object that the decision engine works with is for, how decision items, collections, decision rules, ranking methods, selection strategies, and decision policies connect, and what Decisioning does each time a profile needs content, without describing how to create the objects in the interface.

**Intents:**

* Identify which Decisioning objects answer the five questions behind every decision.
* Explain how decision items, collections, selection strategies, ranking methods, and decision policies fit together.
* Describe what Decisioning does each time a profile needs content in a message or experience that contains a decision policy.
* Work out how groups of selection strategies and scores produce the ranked list that a decision policy returns.
* Find the page that documents each object: catalog, decision item, collection, decision rule, ranking method, selection strategy, decision policy, and placement.
* Match the Decision management objects with their Decisioning objects.

**Glossary:**

* **Decisioning** *(product-specific)*: Chooses the best decision items for each profile. You create decision items in the Offers catalog, then define who can receive each item and how the items are ranked.
* **Decision engine** *(product-specific)*: Evaluates the decision policy and returns the items to use when a profile needs content in a message or experience that contains a decision policy. It does not choose content on its own: it applies the objects that you configure in advance.
* **Catalog** *(product-specific)*: The container of your decision items. A catalog is linked to a schema that defines all the attributes you can assign to an item, and you can add custom attributes to it. Where to configure it: Decisioning > Catalogs, then Edit schema in the items list.
* **Decision item** *(product-specific)*: An offer or piece of content in the Offers catalog. Each item has its own start and end dates, priority, eligibility (audiences or a decision rule), and capping rules. You approve an item when it is ready to be presented to profiles. Where to configure it: Decisioning > Catalogs.
* **Collection** *(product-specific)*: Groups items with attribute rules. Where to configure it: Catalogs > Collections.
* **Decision rule** *(product-specific)*: A reusable condition that determines who qualifies. You can apply a rule to a decision item or to a selection strategy. Where to configure it: Decisioning > Strategy setup > Rules.
* **Eligibility constraint** *(product-specific)*: The eligibility of a decision item or of a selection strategy: an audience or a decision rule.
* **Ranking method** *(product-specific)*: Sets the order of the qualifying items: the item priority (default), a ranking formula, or an AI model. Where to configure it: Decisioning > Strategy setup > Formulas or AI models.
* **Selection strategy** *(product-specific)*: A reusable object that combines a collection, an eligibility constraint (an audience or a decision rule), and a ranking method. Where to configure it: Decisioning > Strategy setup > Selection strategies.
* **Decision policy** *(product-specific)*: Puts selection strategies in order, sets how many items to return, and defines optional fallback items. It is added to the content of a campaign or journey. A decision policy can also include individual decision items, which you add one at a time: an individual item skips the collection and the selection strategy, but the eligibility constraints set on the item still apply.
* **Strategy sequence** *(product-specific)*: The sequence of selection strategies or decision items of a decision policy, which Decisioning goes through in order. The first selection strategy or decision item in the sequence has the highest priority. Selection strategies that you combine in a group have the same priority and are evaluated together.
* **Qualifying item** *(product-specific)*: An item that a selection strategy keeps because the profile meets the constraints you set. For example: the current date is within the start and end dates of the item; the profile meets the eligibility constraint of the item; the profile meets the eligibility constraint of the selection strategy; no capping rule of the item has reached its threshold.
* **Fallback items** *(product-specific)*: Items that you define in the decision policy. If no item qualifies, Decisioning returns the fallback items. Without fallback items, nothing is displayed.
* **Placement (email only)** *(product-specific)*: A container for the items displayed in an email. When you create a placement, you associate it with a channel configuration. Placements also let you track how items perform in each location. Decisioning placements are currently available for email only. Where to configure it: Decisioning > Strategy setup.
* **Context data** *(product-specific)*: Data that Decisioning receives with the profile, if you use it. Context data is sent in at the time of the request and does not include historical data.
* **Decision event** *(product-specific)*: Information about each decision, sent automatically to Adobe Experience Platform. Capping counters, reports, and AI models are based on these events.
* **Stages of a decision request:** Context (step 1), Filtering (steps 2 and 3), Ranking and selection (steps 4 to 6), and Delivery (step 7). Step 8 sends the results back to Adobe Experience Platform.

**Guardrails:**

* Push notifications and mobile messages return one item.
* In an email, an item is not repeated across the decision policies of the same message. A policy that has no other item to show displays its fallback item or a blank space.

**Applicability:**

* Applies: a decision policy can be used in code-based experiences, web, email, push notifications, mobile messages, custom channels, and direct mail.
* Applies: in journeys, the output of the Content decision activity can be used in an Optimize activity or in a custom action.
* Does not apply: in journeys, the output of the Content decision activity cannot be used in native channel activities.
* Applies: automatic tracking of impressions and clicks in emails authored in Journey Optimizer.
* Does not apply: automatic tracking of impressions and clicks in most other channels. Most other channels require your implementation to send them to Experience Platform as experience events.

**Terminology:**

* Canonical name: Adobe Experience Platform — Acronym: AEP — variants: Experience Platform
* Canonical name: Adobe Journey Optimizer — Acronym: AJO — variants: Journey Optimizer
* Canonical name: decision item — variants: item
* Canonical name: decision policy — variants: policy
* Canonical name: selection strategy — variants: strategy (as in "Strategy 1")
* Canonical name: Decision management — the legacy decisioning framework in Journey Optimizer. The objects of the two frameworks do not always map one to one.
* Mapping of Decision management objects to Decisioning objects, as shown by the migration tooling:
    * Offer maps to Decision item.
    * Collection maps to Collection (collection qualifiers are migrated as tags).
    * Rule maps to Decision rule.
    * Ranking formula maps to Ranking formula.
    * Decision maps to Selection strategy, decision policy, and code-based experience campaign. For each migrated decision scope, the migration tooling creates one selection strategy (a collection, an eligibility rule, and a ranking formula), one decision policy (the number of items, the selection strategy, and a fallback item), and one code-based experience campaign.
    * Placement maps to Channel configuration. The migration tooling creates a channel configuration for each Decision management placement. It does not create Decisioning placements: you create them manually.
* **Do not confuse:**
    * "Decisioning" ≠ "Decision management" (the legacy decisioning framework).
    * Decision management "Placement" ≠ Decisioning "placement": see the mapping above.
    * Decision management "Decision" ≠ "decision policy": see the mapping above.

**FAQ:**

* **What does Decisioning do each time a profile needs content?** In a message or experience that contains a decision policy, Decisioning evaluates the policy for that profile and returns the items to use. This happens in eight steps, from the arrival of the request to the decision events sent to Adobe Experience Platform.
* **What happens if no item qualifies?** Decisioning returns the fallback items you defined. Without fallback items, nothing is displayed.
* **Which selection strategy or decision item has the highest priority?** Decisioning goes through the strategy sequence in order. The first selection strategy or decision item in the sequence has the highest priority. Selection strategies that you combine in a group have the same priority and are evaluated together.
* **What happens when an item qualifies in several selection strategies?** The qualifying items of the strategies in a group are ranked together according to their scores, and an item that qualifies in several strategies keeps its highest score. The items of a later group are placed after the items of the earlier groups, and an item that is already ranked is not evaluated again.
* **How can I show the same item in several places of an email?** In an email, an item is not repeated across the decision policies of the same message. To show the same item in several places, reuse the output of an existing decision policy.
* **Where can I use the output of the Content decision activity in a journey?** In an Optimize activity or in a custom action. Its output cannot be used in native channel activities.

**Examples:**

* Collection (Decisioning): a collection can group all the items where the `Category` attribute is `Yoga`.
* Groups and scores (decision policy): a decision policy has three selection strategies. Strategy 1 and Strategy 2 are combined in Group 1, and Strategy 3 is alone in Group 2. Strategy 1 qualifies Offer 1 (10), Offer 2 (20), and Offer 3 (30). Strategy 2 qualifies Offer 3 (45), Offer 4 (40), and Offer 5 (50). Strategy 3 qualifies Offer 5 (already ranked, so it is skipped) and Offer 6 (60). Offer 3 keeps its highest score (45). The final ranked list is Offer 5, Offer 3, Offer 4, Offer 2, Offer 1, and Offer 6. If the policy requests three items, Decisioning returns Offer 5, Offer 3, and Offer 4. Offer 6 has the highest score (60) but comes last, because it belongs to the group with the lower priority.

**Related pages:**

* To set up Decisioning (a task guide that lists the permissions you need and the order in which to create the objects, and links to the procedure for each one): Get started with Decisioning (experience-decisioning/gs-experience-decisioning.md)
* To find out why an item was or was not selected: Troubleshoot Decisioning (experience-decisioning/decisioning-troubleshooting.md)
* To configure the item catalog: Configure the item catalog (experience-decisioning/catalogs.md)
* To create decision items: Create decision items (experience-decisioning/items.md)
* To manage item collections: Manage item collections (experience-decisioning/collections.md)
* To create decision rules: Create decision rules (experience-decisioning/rules.md)
* For ranking methods: Ranking methods (experience-decisioning/ranking/ranking.md)
* To create selection strategies: Create selection strategies (experience-decisioning/selection-strategies.md)
* To create decision policies: Create decision policies (experience-decisioning/create-decision-policy.md)
* To work with placements: Work with placements (experience-decisioning/placements.md)
* To add items and strategies to a policy: Learn how to add items and strategies to a policy (experience-decisioning/create-decision-policy.md)
* For the activity that returns items in journeys: Content decision activity (building-journeys/content-decision.md)
* For the activity in which the returned items can be used in journeys: Optimize activity (building-journeys/content-decision.md)
* At the step where the request arrives: Learn more about context data (experience-decisioning/context-data.md)
* At the step where each selection strategy keeps only the items that qualify: Learn more about eligibility (experience-decisioning/decisioning-troubleshooting.md)
* At the step where the qualifying items are ranked: Learn more about ranking (experience-decisioning/decisioning-troubleshooting.md)
* At the step where the best items are selected, including fallback items: Learn more about fallback items (experience-decisioning/decisioning-troubleshooting.md)
* To use the attributes of the returned items as personalization variables: Personalize with decision item attributes (experience-decisioning/use-decision-policy.md)
* At the step where events feed back into Decisioning: Learn more about data collection (experience-decisioning/data-collection/data-collection.md)
* After the example of groups and scores: Learn more about strategy sequences (experience-decisioning/create-decision-policy.md)
* For how the migration tooling maps Decision management objects to Decisioning objects: migration tooling (experience-decisioning/decisioning-migration-api.md)
* For the benefits of Decisioning and the migration tooling: Benefits of migrating to Decisioning (experience-decisioning/migrate-to-decisioning.md)
* Listed under Learn more: Decisioning FAQ (experience-decisioning/decisioning-faq.md)
* Listed under Learn more: Decisioning guardrails & limitations (experience-decisioning/decisioning-guardrails.md)
* Listed under Learn more: Coworker for Decisioning (experience-decisioning/experience-decisioning-coworker-skills.md)
* Listed under Learn more: Report on Decisioning (experience-decisioning/cja-reporting.md)

**Personas:**

* **marketer:** Can create decision items in the Offers catalog and approve an item when it is ready to be presented to profiles. Can set the eligibility of a decision item or of a selection strategy with an audience or a decision rule. Can choose the ranking method: the item priority (default), a ranking formula, or an AI model. Can add a decision policy to the content of a campaign or journey. Can put selection strategies in order in the policy, set how many items to return, and define optional fallback items. Can use a decision policy in code-based experiences, web, email, push notifications, mobile messages, custom channels, and direct mail. Can use the attributes of the returned items as personalization variables. The page states that push notifications and mobile messages return one item. Where: "The building blocks".

**Onboarding:**

* **Level:** Beginner, Intermediate
* **First minimal step:** Use Get started with Decisioning to see the permissions you need and the order in which to create the objects.
* **Success check:** Decisioning returns the first items of the ranked list, up to the number of items requested in the policy. The attributes of the returned items are available as personalization variables.
* **Next:** To set up Decisioning, with a task guide that lists the permissions you need and the order in which to create the objects: Get started with Decisioning (experience-decisioning/gs-experience-decisioning.md); To find out why an item was or was not selected: Troubleshoot Decisioning (experience-decisioning/decisioning-troubleshooting.md)

+++

<!-- ai-section-version: 1 | source-hash: f8f9d93f -->
