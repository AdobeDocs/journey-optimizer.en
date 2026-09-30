---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to leverage web behavioral data already captured through Adobe Analytics or Web SDK and streamed into Adobe Experience Platform to trigger journeys, by configuring the data source, activating it for Journey Optimizer, and adding a rule-based event to a journey.

**Intents:**

* Configure an Adobe Analytics or Web SDK data source from the Sources menu so its data can be used in journeys
* Enable the Analytics source connector for a chosen report suite
* Activate the configuration by contacting Adobe to enable the environment for an Adobe Analytics data source
* Create a rule-based event based on Adobe Analytics or Web SDK data and use it in a journey
* Build a journey that reacts to web behavioral events, such as targeting users who added a product to their cart

**Glossary:**

* **Report suite**: The Adobe Analytics container of data that you select and activate to make its data available to Journey Optimizer *(product-specific)*
* **Analytics source connector**: The connector enabled for a report suite that transforms incoming data into an Experience event and sends it into Adobe Experience Platform *(product-specific)*
* **Data source ID**: The identifier of the data source you created, found in the Dataflows tab of the Sources menu, and shared with Adobe Customer Care to enable the environment *(product-specific)*
* **Experience event**: The event form into which incoming Adobe Analytics or Web SDK data is transformed before being sent into Adobe Experience Platform *(product-specific)*

**Guardrails:**

* This integration only applies for rule-based events and customers who need to use Adobe Analytics or Web SDK data; customers using Adobe Customer Journey Analytics are directed to a separate page.
* The activation step of contacting Adobe to enable the environment is only required for Adobe Analytics data sources.
* When creating the event, the Type must be Unitary and the Event ID type must be Rule based, using the Analytics or WebSDK schema created beforehand.
* Data coming from Adobe Analytics or Web SDK must be enabled before it can be used in journeys.

**Terminology:**

* Canonical name: Adobe Analytics integration — Acronym: n/a — variants: Adobe Analytics data source, Web SDK data, Analytics source connector
* Synonyms: "Web SDK" = "Adobe Experience Platform Web SDK"
* Do not confuse: "Adobe Analytics" (web behavioral data source requiring the extra activation step) ≠ "Adobe Customer Journey Analytics" (covered on a separate page)

**FAQ:**

* **Q: Which event configuration is used for Adobe Analytics or Web SDK data?** — A Unitary event with a Rule based Event ID type, using the Analytics or WebSDK schema.
* **Q: Is the step of contacting Adobe required for Web SDK data?** — No, the activation step is only required for Adobe Analytics data sources.
* **Q: Where do I enable an Adobe Analytics report suite?** — In the Sources menu, in the Adobe Analytics section, select Add data and choose the report suite to enable.
* **Q: What happens to the data once the source connector is enabled?** — Whenever the data comes in, it is transformed into an Experience event and sent into Adobe Experience Platform.
* **Q: What if I use Adobe Customer Journey Analytics instead?** — This page does not apply; refer to the Customer Journey Analytics page instead.

+++

<!-- ai-section-version: 1 | source-hash: c208ad36 -->
