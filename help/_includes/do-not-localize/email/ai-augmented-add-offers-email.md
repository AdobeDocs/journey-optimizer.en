---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to insert an offer decision into a Journey Optimizer email using the Offer decision content component so the Decision Management engine delivers the best personalized offer to each recipient, and how to preview those offers with test profiles.

**Intents:**

* Insert an offer decision into an email using the Offer decision content component
* Select a placement and a matching decision to display in the component
* Preview the different offers in a decision using the Offer section or content component arrows
* Preview offers per profile using test profiles and the Preview tab

**Glossary:**

* **Offer decision**: A content component and decision that leverages the Decision Management engine to pick the best offer to deliver to each customer *(product-specific)*
* **Placement**: A container used to showcase offers; only decisions compatible with the selected placement are shown *(product-specific)*
* **Simulate content**: The action to select test profiles for previewing offers; "Simulate content (AEP profiles)" identifies test profiles by an Identity namespace, while clicking "Simulate content" directly lets you test variations with sample input data or AI auto-generation *(product-specific)*

**Guardrails:**

* Before starting, you must define an offer decision.
* Only decisions that are compatible with the selected placement display in the list.
* If changes are made to an offer decision being used in a journey's message, you must unpublish the journey and republish it so the changes are incorporated.

**Terminology:**

* Canonical name: Offer decision — Acronym: n/a — variants: decision, personalized offer
* Synonyms: "Decision Management engine" = "Decision Management"
* Do not confuse: "Simulate content (AEP profiles)" (identify test profiles by namespace) ≠ "Simulate content" clicked directly (test variations with sample input data or AI auto-generation)

**FAQ:**

* **Q: What must I do before inserting a decision into an email?** — You must first define an offer decision.
* **Q: Which decisions appear when I select a placement?** — Only decisions that are compatible with the selected placement.
* **Q: If I change an offer decision used in a journey message, do updates apply automatically?** — When you update an offer, fallback offer, offer collection, or offer decision referenced in a message, updates are automatically reflected; however, if the offer decision is used in a journey's message, you must unpublish and republish the journey.
* **Q: How do I preview offers per profile?** — Use Simulate content to add test profiles, then use the Preview tab and select a test profile to see the corresponding offer.

+++

<!-- ai-section-version: 1 | source-hash: 53b79ca6 -->
