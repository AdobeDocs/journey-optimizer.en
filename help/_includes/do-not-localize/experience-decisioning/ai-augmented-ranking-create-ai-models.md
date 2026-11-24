---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** Explains how to build auto-optimization or personalized optimization AI models, connect them to your conversion datasets, and use them to rank offers.

**Intents:**

* Find the list of AI models under Decisioning > Strategy setup > AI models.
* Create an AI model of the Auto-optimization or the Personalized optimization type.
* Select the dataset(s) where the conversion and impression events are collected.
* For a Personalized optimization AI model, select audiences to train the model and, as a Limited Availability release, profile and context features.
* Optimize a Personalized optimization model on custom Customer Journey Analytics metrics.
* Use an active AI model as the ranking method of a selection strategy, then add that strategy to a decision policy.

**Glossary:**

* **AI model** *(product-specific)*: An item you create in Journey Optimizer to rank offers based on your business goals.
* **Auto-optimization** *(product-specific)*: Type of AI model that optimizes offers based on past offer performance.
* **Personalized optimization** *(product-specific)*: Type of AI model that optimizes and personalizes offers based on audiences and offer performance. Personalized optimization models allow you to define business goals and use customer data to train business-oriented models to serve personalized offers and maximize KPIs. By default, they use offer clicks as the optimization metric.
* **Optimization metric** *(product-specific)*: Section that provides information on the conversion event used by the AI model to calculate the ranking of offers. Impression events and conversion events are automatically captured using the Web SDK or the Mobile SDK that has been provided.
* **Conversion rate**: Journey Optimizer ranks offers based on the conversion rate: Conversion rate = Total number of conversion events / Total number of impression events. It is calculated using two types of metrics, impression events and conversion events.
* **Impression events**: One of the two types of metrics used to calculate the conversion rate: offers that are displayed.
* **Conversion events**: One of the two types of metrics used to calculate the conversion rate: offers that result in clicks via email or web.
* **Custom Customer Journey Analytics metrics**: Metrics from your default Customer Journey Analytics data view. They are displayed in the Conversion event drop-down once the Personalized optimization model type is selected, and let you optimize the model on your own custom metrics.
* **Last Touch**: Attribution model used by default by metrics in Customer Journey Analytics. It assigns 100% of the credit to the touchpoint that occurs most recently before conversion.
* **Experience Event - Proposition Interactions** *(product-specific)*: Field group (previously known as mixin) by which the corresponding event is to be captured each time an offer is displayed and/or clicked.
* **Profile features** *(product-specific, Limited Availability)*: Attributes from your profile schema, selected to train a Personalized optimization AI model in addition to or instead of audiences.
* **Context features** *(product-specific, Limited Availability)*: Context attributes sent with the decision request, selected to train a Personalized optimization AI model in addition to or instead of audiences. Automatic features (always included) and recommended features (can be removed) are pre-selected.

**Guardrails:**

* Datasets: only the datasets created from schemas associated with the Experience Event - Proposition Interactions field group are displayed in the drop-down list.
* Audiences: you can select up to 50 audiences to train a Personalized optimization AI model.
* Profile features and context features of a Personalized optimization AI model are currently available as a Limited Availability release. Contact your Adobe representative to gain access.
    * During Limited Availability, only add profile and context features when creating a new AI model. Do not edit an existing AI model to add these features.
    * Profile features: you can select up to 50 attributes from your profile schema.
    * If applicable, data governance (DULE) policies are automatically applied to the selected profile features.
    * Context features: you can add up to 20 additional context features.
    * Context features are only available for decisioning policies used in inbound channels.

**Prerequisites and permissions:**

* Manage Ranking Strategies permission: you must have it to create, edit, or delete AI models.
* Optimizing on custom Customer Journey Analytics metrics: this capability is only available to Customer Journey Analytics customers with admin rights. Make sure you have integrated Journey Optimizer with Customer Journey Analytics, in order to export Journey Optimizer datasets into your default data views.
* Profile or context features in a Personalized optimization model: make sure the data is available before you start.
    * Profile attributes must exist in your organization's profile schema.
    * Context data is sent by the Web SDK or Mobile SDK and defined in your datastream configuration. If your model uses context features, the decision request must also carry the context values.
* Event types (offer displayed or offer clicked): to be able to send them in, you must set the correct value for each event type in an experience event that is sent into Adobe Experience Platform.

**Terminology:**

* Canonical names: AI model, Auto-optimization, Personalized optimization, Optimization metric.
* Canonical name: Customer Journey Analytics — Acronym: CJA
* Canonical name: Adobe Experience Platform — Acronym: AEP
* Canonical name: Experience Event - Proposition Interactions field group — variants: mixin (previous name, written on the page as "previously known as mixin")
* Term as written on the page: data governance (DULE) policies
* Do not confuse: "Auto-optimization" ≠ "Personalized optimization" (the two AI model types).
* Do not confuse: "Profile features" ≠ "Context features".
* Do not confuse: "Impression events" ≠ "Conversion events" (the two types of metrics of the conversion rate).

**FAQ:**

* **Which permission do I need to create, edit, or delete AI models?** You must have the Manage Ranking Strategies permission.
* **Which types of AI model can I create?** Auto-optimization, which optimizes offers based on past offer performance, and Personalized optimization, which optimizes and personalizes offers based on audiences and offer performance.
* **On which metric does Journey Optimizer rank offers?** It ranks offers based on the conversion rate, which is Total number of conversion events / Total number of impression events.
* **Can I optimize a Personalized optimization model on my own metrics?** By default, Personalized optimization models use offer clicks as the optimization metric. If you are working with Customer Journey Analytics, you can select a metric from your default Customer Journey Analytics data view in the Conversion event drop-down. This capability is only available to Customer Journey Analytics customers with admin rights.
* **Can I add profile and context features to an existing AI model?** During Limited Availability, only add profile and context features when creating a new AI model. Do not edit an existing AI model to add these features.
* **How do I use an AI model once it is active?** Use it as the ranking method of a selection strategy, then add that strategy to a decision policy. Selection strategies and decision policies are built the same way whether they use an auto-optimization or a personalized optimization model.

**Examples:**

* Profile features (Personalized optimization AI model, Limited Availability): attributes from your profile schema such as loyalty tier or churn propensity score.
* Context features (Personalized optimization AI model, Limited Availability): context attributes such as device type, language, or country code.

**Best practices:**

* Attribution model for custom Customer Journey Analytics metrics (recommendation): it is possible to modify the attribution model, but not all attribution models are ideal for AI model optimization. The page recommends carefully selecting an attribution model that aligns with your optimization goals to ensure model accuracy and performance.

**Related pages:**

* To learn more about the Manage Ranking Strategies permission: Permission levels (administration/high-low-permissions.md)
* To set up context data for profile or context features in a Personalized optimization model: Learn how to set up context data (experience-decisioning/context-data.md)
* To create the dataset where conversion events will be collected: Create a dataset to collect events (experience-decisioning/data-collection/create-dataset.md)
* To set the correct value for each event type (offer displayed or offer clicked) in an experience event sent into Adobe Experience Platform: Configure events capture (experience-decisioning/data-collection/schema-requirement.md)
* For the Auto-optimization model type: Auto-optimization models (experience-decisioning/ranking/auto-optimization-model.md)
* For the Personalized optimization model type: Personalized optimization model (experience-decisioning/ranking/personalized-optimization-model.md)
* For feature types of a Personalized optimization model: Learn more about feature types (experience-decisioning/ranking/personalized-optimization-model.md)
* For a model that uses context features, to pass the context values in the decision request: Personalized optimization model (experience-decisioning/ranking/personalized-optimization-model.md)
* To leverage Journey Optimizer data in Customer Journey Analytics before optimizing on custom metrics: Learn how to leverage Journey Optimizer data in Customer Journey Analytics (reports/cja-ajo.md)
* Once the AI model is live: monitor its training status and performance (experience-decisioning/ranking/ai-model-observability.md)
* To use the active AI model as the ranking method: selection strategy (experience-decisioning/selection-strategies.md)
* To add the selection strategy to a decision policy: decision policy (experience-decisioning/create-decision-policy.md)

**Personas:**

* **marketer:** Can create an AI model of the Auto-optimization or Personalized optimization type and select the dataset(s) where conversion and impression events are collected. For a Personalized optimization model, can select up to 50 audiences and, as a Limited Availability release, profile and context features. Can use an active AI model as the ranking method of a selection strategy, then add that strategy to a decision policy. The page states that you must have the Manage Ranking Strategies permission to create, edit, or delete AI models. Where: "Create an AI model".

**Onboarding:**

* **Level:** Intermediate
* **First minimal step:** Create a dataset where conversion events will be collected.
* **Success check:** Once your model is live, you can monitor its training status and performance.
* **Previous:** To create the dataset where conversion events will be collected: Create a dataset to collect events (experience-decisioning/data-collection/create-dataset.md); To make sure the data is available before using profile or context features in a Personalized optimization model: Learn how to set up context data (experience-decisioning/context-data.md)
* **Next:** To use the active AI model as the ranking method: selection strategy (experience-decisioning/selection-strategies.md); Once your model is live, to monitor its training status and performance: monitor its training status and performance (experience-decisioning/ranking/ai-model-observability.md)

+++

<!-- ai-section-version: 1 | source-hash: d339f38a -->
