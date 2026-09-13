---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains the modular Journey Optimizer packaging model, in which you start with a base offer (Campaigns, Journeys, or Campaigns & Journeys) and add channel add-ons and the Decisioning add-on, and it includes a reference for legacy Select, Prime, and Ultimate packaging.

**Intents:**

* Identify which base offer matches your engagement use case
* Select the channel add-ons that unlock the messaging surfaces you need
* Understand what the Decisioning add-on unlocks
* Compare orchestration capabilities and channel availability across base offers
* Map legacy Select, Prime, and Ultimate packaging to current capabilities

**Glossary:**

* **Base offer**: The starting license that determines your orchestration capability — Campaigns, Journeys, or Campaigns & Journeys *(product-specific)*
* **Outbound Delivery**: The channel add-on that includes email, push notifications, and direct mail *(product-specific)*
* **Mobile**: The channel add-on that includes in-app messaging, push notifications, content cards, and code-based channels for mobile surfaces *(product-specific)*
* **Web**: The channel add-on that includes the web channel and code-based channels for web surfaces *(product-specific)*
* **All Channels**: An add-on that bundles Outbound Delivery, Mobile, and Web in a single purchase *(product-specific)*
* **Decisioning**: The advanced-capability add-on for real-time best-offer selection across channels *(product-specific)*
* **Total Data Volume**: The storage entitlement measured per addressable profile, which differs by base offer *(product-specific)*

**Guardrails:**

* Storage entitlement differs by package: Campaigns customers receive 15 KB per addressable profile, while Journeys and Campaigns & Journeys customers receive 75 KB per addressable profile.
* Channels are not bundled into the base offer; you select the channel add-on or add-on bundle that fits.
* Orchestrated campaigns support email, SMS, push notifications, and direct mail only; web, in-app, code-based, and content card channels are not supported in orchestrated campaign workflows.
* Decisioning is a distinct advanced-capability add-on and is not included in any base offer by default; contact your Adobe representative to add it.
* SMS / MMS and WhatsApp availability depends on your licensed configuration and are not part of the standard Outbound Delivery, Mobile, or Web add-ons.
* WhatsApp requires a WhatsApp Business account.
* In Journey Optimizer – Journeys, audience-based orchestration is supported only within journey use cases, not as standalone batch campaigns.
* Basic transactional messaging (event-triggered email, push, and SMS) is included with every base offer.
* Code-based experiences require the Mobile or Web add-on.

**Terminology:**

* Canonical name: Journey Optimizer – Campaigns & Journeys — Acronym: n/a — variants: Campaigns & Journeys
* Synonyms: "modular packaging model" = "current packaging model"
* Do not confuse: "Journey Optimizer – Campaigns" (batch, audience-based orchestration) ≠ "Journey Optimizer – Journeys" (real-time, event-driven orchestration)
* Do not confuse: base offers (determine orchestration capability) ≠ add-ons (unlock channels and advanced capabilities)
* Do not confuse: "Outbound Delivery" ≠ "Mobile" ≠ "Web" ≠ "All Channels" (distinct channel add-ons)
* Do not confuse: modular packaging (current) ≠ Select, Prime, and Ultimate (legacy packaging)

**FAQ:**

* **Q: Does every base offer include every channel?** — No; the base offer determines your orchestration capability, and channel add-ons determine which messaging surfaces you can engage.
* **Q: How much storage does each package include?** — Campaigns customers receive 15 KB per addressable profile, and Journeys and Campaigns & Journeys customers receive 75 KB per addressable profile.
* **Q: Which channels do orchestrated campaigns support?** — Email, SMS, push notifications, and direct mail only.
* **Q: Is Decisioning included by default?** — No; it is a distinct advanced-capability add-on that is not included in any base offer by default, so contact your Adobe representative to add it.
* **Q: Are Select, Prime, and Ultimate still the current packaging model?** — No; the current model is modular, built around base offers and add-ons, while Select, Prime, and Ultimate are legacy packaging.

+++

<!-- ai-section-version: 1 | source-hash: e4639b30 -->
