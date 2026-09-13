---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to create AI models that dynamically rank journeys based on trained model scores, and how to reference them in ranking formulas so the best-performing journey is selected per profile when journey entry caps apply.

**Intents:**

* Create an AI model in the [!UICONTROL Orchestration ranking] > [!UICONTROL AI models] tab
* Choose an [!UICONTROL Optimization metric] from the default Customer Journey Analytics data view
* Select the datasets and segments used to train the model
* Reference an AI model in a ranking formula using [!UICONTROL AI model score] as the ranking method
* Assign the formula to a rule set and apply it to journeys so ranking applies when a cap is reached

**Glossary:**

* **AI model**: A trained model whose scores dynamically rank journeys, used in ranking formulas instead of static priority *(product-specific)*
* **Ranking object**: The entity that the ranking formula applies to; by default set to [!UICONTROL Journey] *(product-specific)*
* **Conversion rate**: Total number of conversion events / Total number of impression events; the basis on which [!DNL Journey Optimizer] ranks *(product-specific)*
* **Impression events**: Items that are displayed *(product-specific)*
* **Conversion events**: Items that result in clicks or conversions *(product-specific)*
* **[!UICONTROL AI model score]**: Ranking method that uses the AI model's score in a formula criterion *(product-specific)*

**Guardrails:**

* This feature is currently in Limited Availability; contact your Adobe representative to gain access.
* AI models are only available to organizations that have purchased the **Decisioning** add-on offering.
* Only datasets created from schemas associated with the [!UICONTROL Experience Event - Proposition Interactions] field group are displayed in the drop-down list.
* You can select up to 5 datasets where the conversion and impression events are collected (hard limit).
* You can select up to 50 audiences to train the AI model (hard limit).
* Impression and conversion events are automatically captured using the Web SDK or the Mobile SDK.
* Only one rule set can be applied to a journey at a time.

**Terminology:**

* Canonical name: AI model — Acronym: n/a — variants: journey arbitration AI models, AI model score
* Synonyms: none
* Do not confuse: "AI model" (trained model producing scores) ≠ "ranking formula" (the expression that references priority, attributes, or AI model score) ≠ "journey priority" (a manual value)
* Do not confuse: "impression events" (items that are displayed) ≠ "conversion events" (items that result in clicks or conversions)

**FAQ:**

* **Q: When are AI model rankings applied?** — When a profile is eligible for more journeys than the cap allows; all journeys using the rule set are ranked with the formula referencing the AI model.
* **Q: What metric does the AI model optimize on?** — A metric you select from the default Customer Journey Analytics data view; ranking is based on conversion rate (Total number of conversion events / Total number of impression events).
* **Q: How many datasets and audiences can I use?** — Up to 5 datasets and up to 50 audiences.
* **Q: Which datasets can I select?** — Only datasets created from schemas associated with the [!UICONTROL Experience Event - Proposition Interactions] field group.
* **Q: How do I use the AI model in a formula?** — Use the [!UICONTROL Select AI model] button, then in at least one [!UICONTROL Criterion] set [!UICONTROL AI model score] as the ranking method.

+++

<!-- ai-section-version: 1 | source-hash: 3924d398 -->
