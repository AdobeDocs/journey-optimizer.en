---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to create a Web In-app message campaign in Adobe Journey Optimizer, from configuring the Web In-app channel to defining the audience, triggers, frequency, and content.

**Intents:**

* Configure the Web In-app channel by installing the Web SDK tag extension, customizing triggers, and creating a Web In-app configuration
* Create a Web In-app message campaign and choose a Scheduled or API-triggered execution type
* Define campaign properties, select an audience, and choose an Identity namespace
* Create a content experiment to test treatments against a target audience
* Edit triggers using Sent data to Platform or Manual trigger, add conditions, and apply traits
* Set the message display frequency and schedule, then start designing content

**Glossary:**

* **Web In-app message**: An in-app message delivered within a web campaign in Journey Optimizer *(product-specific)*
* **Sent data to Platform**: A Platform-package trigger fired when the mobile app issues an edge experience event to send data to Adobe Experience Platform, usually the sendEvent API call from the AEP Edge extension *(product-specific)*
* **Manual trigger**: A Manual-package trigger defined by two associated data elements, a key (a constant defining the data set) and a value (a variable belonging to the set) *(product-specific)*
* **Trait**: An And-condition refinement; available traits are XDM event type and XDM value *(product-specific)*
* **Content experiment**: A configuration where you create treatments to measure performance and identify the best option for your target audience *(product-specific)*
* **Identity namespace**: The namespace chosen to identify individuals from the selected audience *(product-specific)*

**Guardrails:**

* Install the Web SDK tag extension to support Web In-app Messaging before creating the campaign.
* Web In-app Messaging supports two types of triggers: Sent data to platform and Manual triggers.
* Campaign execution type must be either Scheduled or API-triggered.
* Campaigns are executed on a specific date or on a recurring frequency, configured through the Schedule.

**Terminology:**

* Canonical name: Web In-app message campaign — Acronym: n/a — variants: Web In-app message, In-app message campaign for web
* Synonyms: "Sent data to Platform" = "Sent data to platform trigger"
* Do not confuse: "Sent data to Platform" (Platform-package trigger) ≠ "Manual trigger" (Manual-package trigger using key/value data elements)
* Do not confuse: "Or" condition (adds more Triggers to expand the rule) ≠ "And" condition (adds a custom Trait to fine-tune the rule)

**FAQ:**

* **Q: What are the two Web In-app trigger types?** — Sent data to platform and Manual triggers.
* **Q: What campaign execution types can I choose?** — Scheduled or API-triggered.
* **Q: What frequency options are available for the trigger?** — Everytime, Once, Until click through, and X number of times.
* **Q: How do I identify individuals from my selected audience?** — Choose a namespace in the Identity namespace field.
* **Q: What traits can I add with the And condition?** — XDM event type and XDM value.
* **Q: How do I start designing the message content?** — Use the Edit content button after configuring the campaign.

+++

<!-- ai-section-version: 1 | source-hash: 5d212ba5 -->
