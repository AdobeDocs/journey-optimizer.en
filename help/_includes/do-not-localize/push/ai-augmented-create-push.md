---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to create a push notification for mobile (iOS and Android) and web within a journey or a campaign, and how to use Rapid delivery mode for high-volume push sending.

**Intents:**

* Add a Push action to a journey and configure it with a push configuration
* Add a Push notification to a campaign (Scheduled or API-triggered)
* Apply capping rules and Send time optimization to a push action
* Preview push content using test profiles or sample input data from a CSV / JSON file or added manually
* Enable and use Rapid delivery mode for very fast, high-volume push sending

**Glossary:**

* **Push action**: A push notification channel action that sends a push notification to profiles when they reach that step of the journey *(product-specific)*
* **Push configuration**: The configuration referenced by the action that defines the content delivered; can be created for mobile or for web *(product-specific)*
* **Rapid delivery mode**: A Journey Optimizer add-on that allows very fast push message sending in large volumes through campaigns *(product-specific)*
* **Send time optimization**: An option that predicts the best time to send the message to maximize engagement based on historical open and click rates *(product-specific)*
* **Business rules**: A drop-down for selecting a capping rule set to apply to the push action *(product-specific)*

**Guardrails:**

* Legacy native channel activities (Email, Push, SMS, In-app, Web, Code-based experience, and Content Card) are deprecated as of the March 2026 release; existing journeys using them continue to work without changes and no migration is required.
* Rapid delivery is available for Scheduled campaigns only and is not available for API-triggered campaigns.
* No personalization is allowed in a Rapid delivery push message.
* The target audience for Rapid delivery must contain less than 30M profiles.
* Up to 5 campaigns can be executed simultaneously using Rapid delivery mode.
* In test mode, messages are not sent via the Rapid delivery mode.
* Rapid delivery mode is a Journey Optimizer add-on.

**Terminology:**

* Canonical name: Push notification action — Acronym: n/a — variants: Push action, Push activity, Push notification
* Canonical name: Rapid delivery mode — Acronym: n/a — variants: Rapid delivery
* Synonyms: "Rapid delivery mode" = "Rapid delivery"
* Do not confuse: "Scheduled - Marketing" campaign ≠ "API-triggered - Marketing/Transactional" campaign
* Do not confuse: "Business rules" (capping rule set) ≠ "Send time optimization" (best send time prediction)

**FAQ:**

* **Q: Where can I create a push notification?** — In a journey (by adding an Action activity and selecting Push) or in a campaign (by choosing the Push notification action).
* **Q: What frequencies can a push campaign use?** — Once, Daily, Weekly, or Monthly.
* **Q: What are the requirements for Rapid delivery mode?** — Scheduled campaigns only, no personalization in the message, an audience of less than 30M profiles, and up to 5 Rapid delivery campaigns running simultaneously.
* **Q: Does Rapid delivery mode send messages in test mode?** — No, in test mode messages are not sent via the Rapid delivery mode.
* **Q: How can I preview my push content?** — Use test profiles or sample input data uploaded from a CSV / JSON file or added manually.

+++

<!-- ai-section-version: 1 | source-hash: 5cfde834 -->
