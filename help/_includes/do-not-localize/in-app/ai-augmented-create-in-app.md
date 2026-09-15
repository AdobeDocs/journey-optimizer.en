---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to create an In-app message in Adobe Journey Optimizer and add it to a journey or a campaign, including configuring triggers, traits, and display frequency.

**Intents:**

* Add an In-app message to a journey using an Action activity with the In-app action type
* Add an In-app message to a campaign after choosing a Scheduled or API-triggered campaign type
* Select or create an in-app configuration and edit the message content
* Edit triggers, add conditions with Or/And, and refine rules with traits
* Set the display frequency for when the In-app message is active
* Add one or more inbound actions to the in-app message

**Glossary:**

* **In-app action type**: The action type selected on a journey Action activity that displays an in-app message when profiles reach that step *(product-specific)*
* **Wait activity (auto)**: A 3-days Wait activity automatically added after an In-app action so in-app messages have proper timing before profiles reach the end of their journey *(product-specific)*
* **Sent data to Platform**: A trigger fired when the mobile app issues an edge experience event to send data to Adobe Experience Platform, usually the sendEvent API call from the AEP Edge extension *(product-specific)*
* **Trait**: An And-condition refinement drawn from packages such as Device info, Application lifecycle, and Places *(product-specific)*
* **Scheduled - Marketing campaign**: A campaign executed immediately or on a specified date, configured and executed from the user interface, aimed at marketing messages *(product-specific)*
* **API-triggered - Marketing/Transactional campaign**: A campaign executed using an API call, aimed at marketing or transactional messages sent following an action performed by an individual *(product-specific)*

**Guardrails:**

* Legacy native channel activities (Email, Push, SMS, In-app, Web, Code-based experience, and Content Card) are deprecated as of the March 2026 release; existing journeys using these activities continue to work without any changes and no migration is required.
* In a journey, a 3-days Wait activity is automatically added after the In-app action, because in-app messages displayed to a profile automatically expire when the profile reaches the end of their journey.
* In-app messages are not impacted by the user's choice to opt-in or opt-out of push notifications at the operating system.
* To show an in-app message shortly after a push notification, a Wait activity is recommended; typically a 5–15 minute wait is recommended, though exact times vary with payload complexity and personalization needs.

**Terminology:**

* Canonical name: In-app message — Acronym: n/a — variants: in-app notification, In-app action
* Synonyms: "Sent data to Platform" = "Send data to Platform"
* Do not confuse: "Show every time" / "Show once" / "Show until click through" (journey frequency options) ≠ "Everytime" / "Once" / "Until click through" / "X number of times" (campaign frequency options)
* Do not confuse: "Or" condition (adds more Triggers to expand the rule) ≠ "And" condition (adds Traits to fine-tune the rule)

**FAQ:**

* **Q: Where can I add an In-app message?** — In a campaign or in a journey.
* **Q: Are the legacy native In-app journey activities still usable?** — They are deprecated as of the March 2026 release, but existing journeys using them continue to work without changes and no migration is required.
* **Q: Why is a Wait activity added automatically in a journey?** — In-app messages expire when a profile reaches the end of their journey, so a 3-days Wait activity is added after the In-app action to ensure proper timing.
* **Q: Do OS push opt-out settings affect in-app messages?** — No; In-app messages are not impacted by the user's choice to opt-in or opt-out of push notifications at the operating system.
* **Q: What campaign types can send an In-app message?** — Scheduled - Marketing (executed immediately or on a specified date) and API-triggered - Marketing/Transactional (executed using an API call).
* **Q: How do I add more than one action to my in-app message?** — Click the Add action button to add one or more inbound actions.

+++

<!-- ai-section-version: 1 | source-hash: 606fbfef -->
