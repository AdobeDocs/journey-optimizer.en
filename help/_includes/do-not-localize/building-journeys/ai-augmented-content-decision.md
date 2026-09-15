---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to configure and use the Content Decision activity in Journey Optimizer journeys to retrieve personalized offers via a decision policy and route or forward them using conditions and custom actions.

**Intents:**
* Add a Content Decision activity to a journey and configure a decision policy
* Select and sequence decision items and selection strategies within a decision policy
* Use the content decision output in an Optimize activity condition to branch profiles based on retrieved offers
* Forward retrieved offers to an external system using a custom action
* Inspect decisioning data in journey step events for audit and troubleshooting purposes

**Glossary:**
* **Content decision activity**: A journey orchestration activity that evaluates a decision policy and retrieves the best eligible offers for each profile *(product-specific)*
* **Decision policy**: A configuration that specifies which decision items and selection strategies to evaluate, and how many items to return *(product-specific)*
* **Selection strategy**: A ranked evaluation method used within a decision policy to determine which offers are eligible and how they are scored *(product-specific)*
* **Proposition**: The output unit of a decision policy execution, containing the selected items and associated scope and ranking metadata *(product-specific)*
* **listSize function**: An expression editor function used to count the number of items returned by a content decision, e.g. `listSize(@decision{Name.items})>0` *(product-specific)*
* **Offers catalog schema**: The schema that defines the attributes available on decision items; accessible via the Context node in advanced expression editor mode *(product-specific)*

**Guardrails:**
* The output of a Content Decision activity cannot be used in native channel activities (email, push, SMS, etc.)
* The content decision output is only accessible in Advanced mode of the expression editor; it is not available in simple mode
* Decisioning permissions are required to author a decision policy
* Consent policy updates take up to 48 hours to take effect for attributes referenced in a decision policy
* Consent policies are only available to organizations with the Adobe Healthcare Shield or Privacy and Security Shield add-on
* Restricted data usage labels (DULE) on offer schema attributes can result in governance policy violations

**Terminology:**
* Canonical name: Content decision activity — Acronym: none — variants: content decision node, decisioning activity
* Synonyms: "decision policy" = "offer selection policy" ; "proposition" = "decision output"
* Do not confuse: "Content decision activity" ≠ "native channel action" (content decision retrieves offers but does not deliver them directly; a custom action or condition is needed to act on the output)

**FAQ:**
* **Q: Can I use the offers returned by a Content Decision activity directly in an email?** — No, the output of a content decision activity cannot be used in native channel activities; you must pass the offers to a custom action to send them to an external system.
* **Q: How do I check whether any offers were returned for a profile?** — Use the listSize function in the advanced expression editor: `listSize(@decision{ContentdecisionName.items})>0`.
* **Q: Where do I access content decision output in the expression editor?** — Switch to Advanced mode, unfold the Context node, and navigate to your decision policy to see all available offer catalog schema attributes.
* **Q: How long does it take for a consent policy update to apply to a decision policy?** — Up to 48 hours after the consent policy is updated.
* **Q: What decisioning data is available in journey step events?** — Each step event includes exdRequestID, propositionEventType, and an array of propositions — each containing an id, scopeDetails (decision provider, correlationID, decision policy), and an items array with id, name, score, and itemSelection details.

+++
