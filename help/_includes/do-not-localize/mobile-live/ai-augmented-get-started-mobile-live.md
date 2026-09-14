---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page introduces Live activities as persistent, real-time updates on the iPhone Lock Screen and Dynamic Island, and explains that in Adobe Journey Optimizer they are sent only through API-triggered campaigns.

**Intents:**

* Understand what Live activities are and how state-based engagement differs from push notifications
* Determine when to use API-triggered Marketing (broadcast) versus API-triggered Transactional (individual) campaigns
* Plan the quick start steps: create a mobile configuration, integrate the Mobile SDK, create a Live activity, and track campaigns

**Glossary:**

* **Live activity**: A persistent, glanceable UI element on the device lock screen that presents real-time, up-to-date information throughout an ongoing event *(product-specific)*
* **State-based engagement**: A continuous, contextual presence that updates dynamically as events evolve, in contrast to one-time alerts
* **Dynamic Island**: The iPhone display area where Live activities appear alongside the Lock Screen
* **API-triggered Marketing**: The campaign type used for broadcast use cases, sending audience-based updates at scale *(product-specific)*
* **API-triggered Transactional**: The campaign type used for individual use cases, sending 1:1 real-time updates per user *(product-specific)*

**Guardrails:**

* Live activities in Adobe Journey Optimizer are only compatible with Apple iOS.
* Live activities can only be initiated via API-triggered campaigns, and all personalization is performed through your own payload.
* Broadcast use cases require an API-triggered Marketing campaign; individual use cases require an API-triggered Transactional campaign.

**Terminology:**

* Canonical name: Live activity — Acronym: n/a — variants: Live activities
* Synonyms: "broadcast use cases" = "audience-based updates sent at scale"
* Synonyms: "individual use cases" = "1:1 real-time updates per user"
* Do not confuse: "API-triggered Marketing" (broadcast, audience-based) ≠ "API-triggered Transactional" (individual, 1:1)
* Do not confuse: "Live activity" (persistent, continuously updatable presence) ≠ "push notification" (one-time alert)

**FAQ:**

* **Q: Which platforms support Live activities in Journey Optimizer?** — Only Apple iOS.
* **Q: How are Live activities initiated?** — Only via API-triggered campaigns, with all personalization performed through your own payload.
* **Q: When should I use API-triggered Marketing versus API-triggered Transactional?** — Marketing for broadcast, audience-based use cases such as sports scores or flight status; Transactional for individual 1:1 use cases such as order tracking or booking confirmations.
* **Q: What are the quick start steps?** — Create a mobile configuration, integrate the Adobe Experience Platform Mobile SDK, create a Live activity through an API-triggered campaign, then track the impact with built-in reports.

+++

<!-- ai-section-version: 1 | source-hash: e61d7a77 -->
