---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to record and honor your customers' channel and topic preferences through consent policies so that Journey Optimizer only targets customers based on their choices.

**Intents:**

* Retrieve customer consent to opt in or out for native outbound channels
* Ask customers which topics they wish to subscribe to
* Define preference attributes at the profile level using the Boolean operator
* Create a page, using the Web SDK or a landing page, to capture customer preferences
* Create a consent policy in Experience Platform and leverage it in Journey Optimizer

**Glossary:**

* **Preference attribute**: A Boolean (true/false) attribute defined at the profile level, such as Newsletter_Email, captured in a Profile-enabled dataset schema and mapped to the unified customer profile *(product-specific)*
* **Consent policy**: A policy created in Experience Platform, applied in Journey Optimizer through channel configurations or journey custom actions, used to honor preferences *(product-specific)*
* **Consent event**: The event triggered when a customer selects or deselects a preference, saved against the profile attributes as true for opted-in and false for opted-out *(product-specific)*
* **Subscription topic**: A category of communication a customer can subscribe to, such as Newsletters, Offers, and New Product Launches *(product-specific)*

**Guardrails:**

* This capability is currently only available for organizations that have purchased the Adobe Healthcare Shield or Privacy and Security Shield add-on offerings.
* Consent takes precedence over preferences: a customer who opted out from receiving any communications cannot be targeted even if a preferred channel and topic are indicated.
* The supported channels are Email, Push, SMS and InApp.
* Preference attributes must be present in the profile data, which is why they must be defined at the profile level.
* The domain of the landing page being used must belong to the upper brand and not to a sub-brand, because the preferences collected are stored in the profile data which is at the upper-brand level.

**Terminology:**

* Canonical name: Preference — Acronym: n/a — variants: contact preference, communication preference, subscription preference
* Synonyms: "opted-in" = "true"; "opted-out" = "false"
* Do not confuse: "consent" (whether a customer agreed to receive communications) ≠ "preference" (the channels and topics a customer selected); consent takes precedence over preferences

**FAQ:**

* **Q: Which channels are supported for retrieving consent?** — The supported channels are Email, Push, SMS and InApp.
* **Q: What takes precedence when consent and preferences conflict?** — Consent takes precedence over preferences; a customer who opted out from all communications cannot be targeted regardless of their preferred channel or topic.
* **Q: How are preference attributes defined?** — Define them with the Boolean operator (true/false) at the profile level; they are captured in a Profile-enabled dataset schema and mapped to the unified customer profile.
* **Q: How can I capture customer preferences?** — Create a web page using the Adobe Experience Platform Web SDK, or use a Journey Optimizer landing page that includes forms to capture preferences through profile data.
* **Q: Why must the landing page domain belong to the upper brand?** — Because the preferences collected are stored in the profile data, which is at the upper-brand level.

+++

<!-- ai-section-version: 1 | source-hash: 5a8562ef -->
