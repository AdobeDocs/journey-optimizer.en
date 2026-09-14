---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to add a Mobile message action to a journey or a campaign in Journey Optimizer, select or create a Mobile message configuration, and edit the content to send text (SMS), rich communication (RCS), and multimedia (MMS) messages.

**Intents:**

* Add a Mobile message action to a journey by dragging an Action activity and selecting Mobile message
* Add a Mobile message action to a campaign from the Action tab
* Select or create the Mobile message configuration used by the action
* Apply capping rules to a journey Mobile message action through the Business rules drop-down
* Set the campaign action frequency (Once, Daily, Weekly, or Month)
* Track clicks on links in the Mobile message from the Actions tracking section

**Glossary:**

* **Mobile message action**: A channel action added to a journey or campaign that sends a text (SMS), multimedia (MMS), or rich communication (RCS) message to profiles when they reach that step *(product-specific)*
* **Mobile message configuration**: The configuration referenced by the action that defines the content delivered *(product-specific)*
* **Label**: The name that identifies the action in the journey canvas *(product-specific)*
* **Business rules**: A rule set selected in the drop-down list to apply capping rules to a Mobile message action *(product-specific)*
* **Scheduled - Marketing campaign**: A campaign type executed immediately or on a specified date, configured and executed from the user interface, aimed at sending marketing messages *(product-specific)*
* **API-triggered - Marketing/Transactional campaign**: A campaign type executed using an API call, aimed at sending marketing or transactional messages following an action performed by an individual *(product-specific)*

**Guardrails:**

* Legacy native channel activities (Email, Push, SMS, In-app, Web, Code-based experience, and Content Card) are deprecated as of the March 2026 release; existing journeys using them continue to work without changes and no migration is required.
* RCS is not a HIPAA-Ready Service and must not be used to collect, store, or process any sensitive personal data, including permitted health data.
* All SMS/RCS/MMS marketing messages must contain a way for the recipients to easily unsubscribe.
* Campaign action frequency options are Once, Daily, Weekly, and Month.

**Terminology:**

* Canonical name: Mobile message action — Acronym: n/a — variants: SMS action, Mobile message channel action
* Synonyms: "Mobile message" = "SMS/RCS/MMS message"
* Do not confuse: "Scheduled - Marketing" (executed from the user interface) ≠ "API-triggered - Marketing/Transactional" (executed using an API call)

**FAQ:**

* **Q: How do I add a Mobile message to a journey?** — Drag and drop an Action activity, select Mobile message as the action type, click Add, enter a Label, click Configure action, then select or create the Mobile message configuration and edit the content.
* **Q: How do I add a Mobile message to a campaign?** — From the Action tab, click Add action, choose Mobile message, then select or create a configuration and edit the content.
* **Q: Can I limit how often a journey Mobile message action sends?** — Yes, you can apply capping rules by selecting a rule set in the Business rules drop-down list.
* **Q: Are the legacy native SMS journey activities still usable?** — They are deprecated as of the March 2026 release, but existing journeys using them continue to work without changes and no migration is required.
* **Q: How do I track clicks on links in a Mobile message campaign?** — In the Actions tracking section, specify that you want to track clicks on links in your Mobile message.

+++

<!-- ai-section-version: 1 | source-hash: 79834fa8 -->
