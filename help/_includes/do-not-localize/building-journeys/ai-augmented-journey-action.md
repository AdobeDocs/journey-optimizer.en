---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to use the unified Action activity in the journey canvas to configure built-in channel actions (email, push, SMS, in-app, web, content card, code-based experience), build multi-inbound-action groups, and apply optimization or multilingual settings.

**Intents:**
* Add a built-in channel action (email, push, SMS, in-app, web, content card, code-based experience) to a journey using the Action activity
* Configure a multi-action group to deliver multiple inbound actions simultaneously from a single journey node
* Apply frequency capping rules to an outbound channel action to prevent message fatigue
* Update message content in a live journey without republishing
* Connect a third-party messaging system to a journey using custom actions
* Enable Rapid delivery mode for high-volume urgent push notifications

**Glossary:**
* **Action activity**: The unified journey canvas activity that serves as the single entry point for all built-in channel actions, replacing individual legacy channel activities *(product-specific)*
* **Multi-action**: A configuration within a single Action activity node that allows up to 10 inbound channel actions to be delivered simultaneously *(product-specific)*
* **Rapid delivery mode**: An add-on that enables very fast, high-volume push message sending for time-critical alerts *(product-specific)*
* **Automatic Wait node**: A 3-day Wait activity automatically inserted after each inbound channel action to give profiles time to view the experience before the journey advances *(product-specific)*
* **Priority score**: A value assigned to a journey action to determine which inbound experience takes precedence when multiple actions compete for the same channel configuration *(product-specific)*

**Guardrails:**
* Legacy individual channel activities (Email, Push, SMS, In-app, Web, Code-based experience, Content Card) are deprecated as of the March 2026 release; existing journeys continue to work without migration
* Multi-action is only available for inbound channels; outbound channels such as Email are not supported in multi-action groups
* A multi-action group supports a maximum of 10 inbound actions
* In a live journey, personalization attributes (profile attributes and contextual data) cannot be changed; only message content can be updated
* In-app triggers cannot be modified in a live journey

**Terminology:**
* Canonical name: Action activity — Acronym: none — variants: channel action, message activity, built-in channel action
* Synonyms: "Action activity" = "channel action activity"
* Do not confuse: "Action activity" ≠ "custom action" — the Action activity uses built-in native channels, while a custom action integrates with a third-party system via API

**FAQ:**
* **Q: What channels are available in the Action activity?** — Email, Push, SMS/RCS/MMS, In-app, Web, Code-based experience, and Content Card.
* **Q: Can I send to multiple inbound endpoints in the same journey node?** — Yes, using the Multi action type you can add up to 10 inbound actions (Code-based experience, In-app, Content Card, Web) in a single Action activity node.
* **Q: What happens to journeys that use the deprecated legacy channel activities?** — They continue to work without any changes; no migration is required.
* **Q: Can I change the email subject line of a live journey?** — You can update message content in a live journey, but you cannot change personalization attributes or contextual data used in that content.
* **Q: How do I apply frequency capping to a channel action?** — Use the Business rules drop-down in the action configuration to select a rule set that applies capping rules for the selected channel.

+++
