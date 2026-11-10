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

* **Web In-app message campaign**: A campaign created in Journey Optimizer, from configuring the Web In-app channel to defining the audience, triggers, and content *(product-specific)*
* **Sent data to Platform**: A Platform-package trigger fired when the mobile app issues an edge experience event to send data to Adobe Experience Platform, usually the sendEvent API call from the AEP Edge extension *(product-specific)*
* **Manual trigger**: A Manual-package trigger defined by two associated data elements, a key (a constant defining the data set) and a value (a variable belonging to the set) *(product-specific)*
* **Trait**: An And-condition refinement; available traits are XDM event type and XDM value *(product-specific)*
* **Content experiment**: A configuration where you create treatments to measure performance and identify the best option for your target audience *(product-specific)*
* **Identity namespace**: The namespace chosen to identify individuals from the selected audience *(product-specific)*

**Guardrails:**

* Install the Web SDK tag extension to support Web In-app Messaging.
* Web In-app Messaging supports two types of triggers: Sent data to platform and Manual triggers.
* You choose the campaign execution type: Scheduled or API-triggered.
* Campaigns are executed on a specific date or on a recurring frequency, configured through the Schedule.

**Terminology:**

* Canonical name: Web In-app message campaign — Acronym: n/a — variants: Web In-app message
* Do not confuse: "Sent data to Platform" (Platform-package trigger) ≠ "Manual trigger" (Manual-package trigger using key/value data elements)
* Do not confuse: "Or" condition (adds more Triggers to expand the rule) ≠ "And" condition (adds a custom Trait to fine-tune the rule)

**FAQ:**

* **Q: What are the two Web In-app trigger types?** — Sent data to platform and Manual triggers.
* **Q: What campaign execution types can I choose?** — Scheduled or API-triggered.
* **Q: What frequency options are available for the trigger?** — Everytime, Once, Until click through, and X number of times.
* **Q: How do I identify individuals from my selected audience?** — Choose a namespace in the Identity namespace field.
* **Q: What traits can I add with the And condition?** — XDM event type and XDM value.
* **Q: How do I start designing the message content?** — Use the Edit content button after configuring the campaign.

**Personas:**

* **marketer:** Can enter the Title and Description, select the audience, and choose the Identity namespace to identify individuals. Can select Create experiment to configure a content experiment, edit triggers with Sent data to Platform or Manual trigger, and set the trigger frequency. The page states that Custom upload (CSV) audiences are not supported for in-app messages. Where: "Define your Web In-app message campaign".

**Onboarding:**

* **Level:** Beginner
* **First minimal step:** Install the Web SDK tag extension to support Web In-app Messaging.
* **Success check:** You can find the settings previously configured as App configuration in the Action menu.
* **Previous:** Setting up the Web In-app channel before creating a campaign: In-app channel prerequisites and configuration (in-app/inapp-configuration.md)
* **Next:** Testing and sending the In-app notification after creating it: Check and send your In-app notification (in-app/send-in-app.md); Viewing the campaign report after sending the In-app message: Campaign report (reports/campaign-global-report-cja-inapp.md)

+++

<!-- ai-section-version: 1 | source-hash: fd20639f -->
