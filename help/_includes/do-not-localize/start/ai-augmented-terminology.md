---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This reference guide defines the essential Journey Optimizer terms and disambiguates pairs of similar-sounding capabilities.

**Intents:**

* Look up definitions for core Journey Optimizer journey, campaign, audience, content, decision, and data terms
* Disambiguate Decisioning versus Decision Management
* Disambiguate the three campaign types (Action, API-triggered, Orchestrated)
* Disambiguate Frequency capping versus journey arbitration
* Disambiguate Content Cards versus In-App messages

**Glossary:**

* **Journey**: A series of connected steps that guide customers through experiences over time, where each step occurs based on customer actions or time triggers *(product-specific)*
* **Campaign**: A coordinated marketing action delivering content to a specific audience across one or more channels; unlike journeys, campaigns execute actions simultaneously *(product-specific)*
* **Engageable Profiles**: The unique customer profiles engaged through journeys, campaigns, or decisioning activities over a rolling 12-month window; this is the key license metric, and each profile is counted once per sandbox *(product-specific)*
* **Test Profile**: Fictitious profiles used for testing and previewing messages before sending to real customers *(product-specific)*
* **Decisioning**: The current-generation decision framework, recommended for new implementations, available for Code-based Experience, Push, SMS, and Email *(product-specific)*
* **Decision Management**: The legacy offer decisioning feature, still supported for existing implementations, supporting Email, In-App, Push, SMS, and Direct mail *(product-specific)*
* **Rule set**: A named group of business rules applied to journeys and campaigns, combining frequency capping, journey entry limits, and quiet hours into a single reusable policy *(product-specific)*

**Guardrails:**

* Many foundational concepts (real-time customer profiles, sandboxes, schemas, datasets) are Adobe Experience Platform concepts, not Journey Optimizer-specific ones.
* Engageable Profiles is measured over a rolling 12-month window and each profile is counted once per sandbox regardless of how many journeys or campaigns it enters.
* Decisioning is recommended for all new implementations; Decision Management is legacy and no longer recommended for new implementations.
* Adobe Journey Optimizer and Journey Optimizer B2B Edition are two separate products; this documentation covers Adobe Journey Optimizer (B2C customer journeys).

**Terminology:**

* Canonical name: Decisioning — Acronym: n/a — variants: current-generation decision framework
* Synonyms: "Action campaigns" = "Scheduled campaigns"
* Do not confuse: "Decisioning" (current, recommended; Code-based Experience, Push, SMS, Email) ≠ "Decision Management" (legacy; Email, In-App, Push, SMS, Direct mail)
* Do not confuse: "Frequency capping" (a profile receives too many messages over time) ≠ "Journey arbitration" (a profile qualifies for multiple journeys simultaneously)
* Do not confuse: "Content Cards" (persistent cards embedded in the app UI) ≠ "In-App messages" (transient overlays, banners, or modals)
* Do not confuse: "Action campaigns" (scheduled batch sends) ≠ "API-triggered campaigns" (real-time, event-driven) ≠ "Orchestrated campaigns" (complex, multi-step workflows with a visual canvas)

**FAQ:**

* **Q: Should new implementations use Decisioning or Decision Management?** — Decisioning is the current-generation framework recommended for all new implementations; Decision Management is legacy and still supported but no longer recommended for new implementations.
* **Q: How is a journey different from a campaign?** — A journey guides customers through connected steps over time based on actions or time triggers, whereas campaigns execute actions simultaneously to a specific audience across one or more channels.
* **Q: What is the key license metric for Journey Optimizer?** — Engageable Profiles, the unique profiles engaged over a rolling 12-month window, counted once per sandbox.
* **Q: What are the three campaign types?** — Action campaigns (scheduled batch sends), API-triggered campaigns (real-time, event-driven messaging via API), and Orchestrated campaigns (complex, multi-step workflows with a visual canvas).
* **Q: Are real-time customer profiles, sandboxes, and schemas defined here?** — No. Those are Adobe Experience Platform concepts; refer to the Adobe Experience Platform glossary for their definitions.

+++

<!-- ai-section-version: 1 | source-hash: 5c3a6b72 -->
