---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to author a content card and define its content, either as part of a journey or a campaign, including its configuration, additional delivery rules, and content experiments.

**Intents:**

* Add a content card to a journey by using an Action activity of type Card
* Add a content card to a campaign by selecting the Content card action
* Select or create a content card configuration for the action
* Enable additional delivery rules that control when the card is shown, dismissed, or permanently hidden
* Build rules from Events, Triggers, and Traits, and group them
* Run a content experiment to test multiple variables of a delivery

**Glossary:**

* **Content card**: An inbound, in-app experience that displays personalized content within a dedicated surface of your mobile app and remains available until the user dismisses it or your delivery rules hide it *(product-specific)*
* **Card**: The action type selected in a journey Action activity to deliver a content card *(product-specific)*
* **Content card configuration**: The configuration referenced by the action that defines the content shown *(product-specific)*
* **Inbox configuration**: The configuration that defines the inbox surface for a content card in a campaign *(product-specific)*
* **Additional delivery rules**: Optional rules, enabled with **Enable additional delivery rules** and defined via **Edit rules**, that set when a message is shown, dismissed, or permanently hidden *(product-specific)*
* **Content experiment**: A test of multiple variables of a delivery on sample populations to determine which treatment has the greatest impact on the targeted audience *(product-specific)*
* **Triggers**: Events added to a rule; more can be added with the **Or** condition *(product-specific)*
* **Traits**: Conditions added with the **And** condition to fine-tune a rule *(product-specific)*

**Guardrails:**

* Because Card is an inbound experience activity, it comes with a Wait activity that is added automatically after the Card action (3 days by default).
* Disqualification rules require Web SDK version 2.28.0 or later.
* By default, the close button hides the card; to add more functionality, you must manually define dismissal or disqualification rules.
* Legacy native channel activities (Email, Push, SMS, In-app, Web, Code-based experience, and Content Card) are deprecated as of the March 2026 release; existing journeys using these activities continue to work without any changes and no migration is required.

**Terminology:**

* Canonical name: Content card — Acronym: n/a — variants: Card action, Content card action
* Campaign types: "Scheduled - Marketing" (executed immediately or on a specified date from the interface) — "API-triggered - Marketing/Transactional" (executed using an API call)
* Do not confuse: "Triggers" (events added with the **Or** condition) ≠ "Traits" (conditions added with the **And** condition)
* Do not confuse: "dismissed" (the message is hidden) ≠ "permanently hidden" (governed by disqualification rules)

**FAQ:**

* **Q: Where can I author a content card?** — Either as part of a journey or a campaign.
* **Q: Why does a Wait activity appear after my Card action?** — Because Card is an inbound experience activity, it comes with a Wait activity added automatically (3 days by default).
* **Q: What is required to use disqualification rules?** — Web SDK version 2.28.0 or later.
* **Q: Are the legacy native content card journey activities still usable?** — They are deprecated as of the March 2026 release, but existing journeys using them continue to work without any changes and no migration is required.
* **Q: What happens when a user selects the close button?** — By default, the close button hides the card; you can manually define dismissal or disqualification rules to add more functionality.
* **Q: How do I test multiple variations of my content card in a campaign?** — Select **Create experiment** to test multiple variables of a delivery on sample populations.

+++

<!-- ai-section-version: 1 | source-hash: 0234534e -->
