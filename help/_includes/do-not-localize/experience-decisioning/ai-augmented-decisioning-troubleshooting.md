---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how eligibility, capping, ranking, and fallback items decide which decision items a profile receives, and ends with a checklist to find out why an item was or was not shown.

**Intents:**

* Restrict who can receive a decision item, or who a selection strategy applies to, with audiences or decision rules.
* Limit how often a decision item is presented with capping rules.
* Understand how the ranking method of a selection strategy decides which item comes first when several items qualify.
* Understand when fallback items are displayed.
* Find out when changes take effect.
* Go through the troubleshooting checklist to find out why an item was or was not shown.

**Glossary:**

* **Eligibility** *(product-specific)*: By default, all profiles are eligible for a decision item and for a selection strategy. You can restrict eligibility with audiences or decision rules.
* **Audience**: A list of profiles that Adobe Experience Platform computes from profile attributes and experience events.
* **Decision rule** *(product-specific)*: A condition that runs against the individual profile. It can use profile attributes, audiences, and context data. A rule created for the **Decision item** entity can also use decision item attributes.
* **Capping** *(product-specific)*: Limits how many times a decision item can be presented, with capping rules.
* **Capping rule** *(product-specific)*: A rule that counts decision events (default), impressions, clicks, or custom events. A capping rule applies in total, across all profiles, or per profile. Its scope is the offer level (default), each placement, or specific placements.
* **Ranking method** *(product-specific)*: When several items qualify for a selection strategy, the ranking method of the strategy decides which one comes first.
* **Offer priority** (default ranking method): The items with the highest priority are delivered first. You set the priority on each decision item.
* **Ranking formula**: Calculates a score from your own logic instead of the item priority.
* **AI model**: Uses a trained model system to rank the items for each profile. AI models learn from the impression and conversion events that you collect in a dataset.
* **Auto-optimization models**: Optimize on the overall performance of the offers.
* **Personalized optimization models**: Use customer data to personalize the ranking.
* **Fallback items** *(product-specific)*: Optional items that you select when you configure the decision policy. They are displayed when none of the selection strategies of the policy qualify.
* **Fallback rate**: One of the Decisioning KPIs: the percentage of instances where no selection strategy qualified.

**Guardrails:**

* When an item has several capping rules, the item is capped as soon as any single rule reaches its threshold.
* Decision events are collected automatically. For the other events, the schema that collects your experience events must include the field group for that event. Otherwise, the counter might not be incremented correctly.
* Custom events must be experience events that you ingest. Delivery events, such as an email send, are not supported.
* A fallback item is displayed regardless of the dates and the eligibility constraints set on the item.
* You can select up to the number of items that the policy requests as fallback items.
* If no item qualifies and no fallback is defined, nothing is displayed. In an email, when two decision policies select the same item, the second policy displays a blank space unless a fallback is configured.
* Changes to a decision policy and to the objects it uses can take up to 15 minutes to propagate across all data regions, and up to 30 minutes for Canada. This includes adding an item to a collection, changing a rule or the content of an item, and updating a formula.
* A capping counter can take up to 3 seconds to update. After you approve an item or create a capping rule, it can take up to 15 minutes before events are counted toward the cap.

**Prerequisites and permissions:**

* Decisioning Explainer: it is available to customers who have access to Coworker and Decisioning.

**Applicability:**

* Capping rules that count impressions: apply to inbound channels only.
* Standard impression and click capping: does not apply to push notifications, which do not support it. The page says to use custom events instead.
* Placement scopes: do not apply to capping rules based on Adobe Experience Platform data.

**Terminology:**

* Canonical names used on the page: decision item, collection, decision rule, ranking method, selection strategy, decision policy, capping rule, fallback items.
* Canonical name: Adobe Experience Platform — Acronym: AEP
* Do not confuse: "Audience" ≠ "Decision rule". The audience is not recomputed when a decision is made, so it might not be up to date. A decision rule is evaluated every time a decision is made, so each profile gets the latest result.

**FAQ:**

* **Q:** Why did an item not show up for a profile, or why did a different one show up? **A:** Go through the troubleshooting checklist: dates and status, collection, eligibility, capping, order and number of items, fallback, recent changes, and Coworker.
* **Q:** Which profiles are eligible for a decision item by default? **A:** By default, all profiles are eligible for a decision item and for a selection strategy. You can restrict eligibility with audiences or decision rules.
* **Q:** Why might an audience not be up to date when a decision is made? **A:** The audience is not recomputed when a decision is made, so it might not be up to date. A decision rule is evaluated every time a decision is made.
* **Q:** When do changes take effect? **A:** Changes to a decision policy and to the objects it uses can take up to 15 minutes to propagate across all data regions, and up to 30 minutes for Canada. A capping counter can take up to 3 seconds to update.
* **Q:** What is displayed when no item qualifies? **A:** Fallback items are displayed when none of the selection strategies of the policy qualify. If no fallback is defined, nothing is displayed.
* **Q:** How do I see how often fallback items are displayed? **A:** Check the **Fallback rate** in the Decisioning KPIs.

**Troubleshooting:**

* A profile did not receive the item you expected. The page says to go through these checks:
    * Dates and status: Is the current date within the start and end dates of the decision item? Also check its status: you approve an item when it is ready to be presented to profiles.
    * Collection: Does the collection used by the selection strategy contain the item? Select **Preview collection** to list the items that match the collection rules.
    * Eligibility: Does the profile meet the eligibility constraints of both the item and the selection strategy? To test a decision rule, use **Simulate rule**.
    * Capping: Has a capping rule of the item reached its threshold?
    * Order and number of items: Do the strategies earlier in the sequence already provide all the items that the policy requests? Items of a group with a higher priority come before the items of later groups, whatever their score.
    * Fallback: Does the policy define fallback items?
    * Recent changes: Did you change the policy or one of its objects in the last 15 minutes (30 minutes for Canada)?
    * Coworker: Ask the Decisioning Explainer why an offer was or was not shown to a profile or segment.

**Examples:**

* Ranking formula: you can boost the offers whose end date is less than 24 hours from now.

**Related pages:**

* If you are new to Decisioning, to see how decision items, collections, rules, ranking methods, selection strategies, and decision policies fit together: How Decisioning works (experience-decisioning/how-decisioning-works.md)
* For more on eligibility: Learn more about eligibility (experience-decisioning/items.md)
* For more on decision rules: decision rules (experience-decisioning/rules.md)
* For more on capping rules: Learn more about capping rules (experience-decisioning/items.md)
* To set the priority on each decision item (Offer priority ranking method): Create decision items (experience-decisioning/items.md)
* To check the dates and status of a decision item: Manage decision items (experience-decisioning/items.md)
* For the Ranking formula ranking method: Ranking formulas (experience-decisioning/ranking/ranking-formulas.md)
* For the AI model ranking method: AI models (experience-decisioning/ranking/ai-models.md)
* For the requirements and limitations of auto-optimization models: Auto-optimization (experience-decisioning/ranking/auto-optimization-model.md)
* For the requirements and limitations of personalized optimization models: Personalized optimization (experience-decisioning/ranking/personalized-optimization-model.md)
* For more on fallback items: Learn more about fallback items (experience-decisioning/create-decision-policy.md)
* To see how often fallback items are displayed: Learn more about Decisioning KPIs (reports/campaign-global-report-cja-code.md)
* To check that the collection contains the item: Manage item collections (experience-decisioning/collections.md)
* To test a decision rule: Learn how to simulate a rule (experience-decisioning/rules.md)
* To ask why an offer was or was not shown to a profile or segment: Decisioning Explainer (experience-decisioning/experience-decisioning-coworker-skills.md)
* To measure how your items perform: Report on Decisioning (experience-decisioning/cja-reporting.md)
* Listed under Learn more: Get started with Decisioning (experience-decisioning/gs-experience-decisioning.md)
* Listed under Learn more: Decisioning FAQ (experience-decisioning/decisioning-faq.md)
* Listed under Learn more: Decisioning guardrails & limitations (experience-decisioning/decisioning-guardrails.md)
* Listed under Learn more: Coworker for Decisioning (experience-decisioning/experience-decisioning-coworker-skills.md)

**Personas:**

* **marketer:** Can use the troubleshooting checklist to find out why an item was or was not shown, with Preview collection and Simulate rule. The page states that the Decisioning Explainer is available to customers who have access to Coworker and Decisioning. Where: "Troubleshooting checklist".

**Onboarding:**

* **Level:** Intermediate
* **First minimal step:** Check that the current date is within the start and end dates of the decision item, and check its status.
* **Success check:** Preview collection lists the items that match the collection rules.
* **Previous:** You are new to Decisioning: see how decision items, collections, rules, ranking methods, selection strategies, and decision policies fit together: How Decisioning works (experience-decisioning/how-decisioning-works.md)
* **Next:** To measure how your items perform: Report on Decisioning (experience-decisioning/cja-reporting.md); To ask why an offer was or was not shown to a profile or segment: Decisioning Explainer (experience-decisioning/experience-decisioning-coworker-skills.md)

+++

<!-- ai-section-version: 1 | source-hash: f262af18 -->
