---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to apply Adobe Experience Platform consent policies in Journey Optimizer, through channel configurations or journey custom actions, so that communications respect each customer's consent choices.

**Intents:**

* Understand how consent policies override the default exclusion logic for opted-out profiles
* Leverage consent policies through an email channel configuration by associating a marketing action
* Associate a channel and a required marketing action to a custom action when configuring it
* Define an additional marketing action when adding a custom action in a journey
* Refresh and check the list of consent policies taken into consideration for a custom action

**Glossary:**

* **Consent policy**: A policy you create in Adobe Experience Platform that overrides the default logic, for example to exclude customers who have not consented to receive communication for a given channel *(product-specific)*
* **Marketing action**: A marketing action, such as Email Targeting, associated with a channel configuration or custom action so that all consent policies associated with that marketing action are leveraged *(product-specific)*
* **Required marketing action**: The marketing action defined when configuring a custom action; prefilled from the default marketing action of the selected channel *(product-specific)*
* **Additional marketing action**: A marketing action defined when adding a custom action in a journey, describing the purpose of that custom action in that particular journey *(product-specific)*
* **Consent schema**: The Experience Platform schema that handles consent; by default the consent field value is empty and treated as consent to receive communications *(product-specific)*

**Guardrails:**

* Consent policies are currently only available for organizations that have purchased the Adobe Healthcare Shield or Privacy and Security Shield add-on offerings.
* With consent management, only two journey activities are analyzed: Read audience and Custom action; all other activities are not taken into account, and if a journey starts with an Audience qualification the audience is not taken into account.
* Consent policies only apply when a marketing action (required or additional) is set at the custom action level.
* Attributes that are part of a field group using the out-of-the-box Union Schema are not supported and are hidden from the interface; you need to create another field group using a different schema.
* If a profile is excluded by a consent policy in a custom action, the message is not sent to that profile, but the profile continues the journey and does not go to the timeout and error path when using a condition.
* Before refreshing policies in a custom action positioned in a journey, make sure your journey has no error.
* With live journeys, consent policies are retrieved and updated automatically every 6 hours.
* Selecting None in the Required marketing action field means no consent policy is applied, for example for transactional messages such as a password reset.

**Terminology:**

* Canonical name: Consent policy — Acronym: n/a — variants: custom consent policy, consent management
* Synonyms: "channel configuration" = "channel surface"
* Do not confuse: "Required marketing action" (defined when configuring the custom action, read-only when adding it in a journey) ≠ "Additional marketing action" (defined when adding the custom action in a journey)
* Do not confuse: "Healthcare Shield" ≠ "Privacy and Security Shield" (two distinct add-on offerings, either of which enables consent policies)

**FAQ:**

* **Q: What happens by default when a profile has opted out?** — By default the corresponding profile is excluded from subsequent deliveries; a consent policy can override this default logic.
* **Q: Do I need a specific offering to use consent policies?** — Yes, consent policies are only available for organizations that have purchased the Adobe Healthcare Shield or Privacy and Security Shield add-on offerings.
* **Q: How often are consent policies updated for live journeys?** — With live journeys, consent policies are retrieved and updated automatically every 6 hours.
* **Q: What does the Refresh policies button do?** — It updates and checks the list of policies taken into consideration for the custom action; this is for information purpose only while building a journey.
* **Q: How do I avoid applying a consent policy to a transactional message?** — Select None in the Required marketing action field so that no consent policy is applied.

+++

<!-- ai-section-version: 1 | source-hash: 4b11443e -->
