---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to define URL tracking parameters at the email channel configuration level so they are appended to your content links and captured in web analytics and performance reports.

**Intents:**

* Define URL tracking parameters when configuring an email channel configuration
* Enter parameter Name and Value fields, or personalize Value with contextual attributes
* Use predefined contextual attributes in tracking parameters
* Build Adobe Analytics or Google Analytics compatible tracking URLs
* Preview how tracking parameters will be appended to content URLs

**Glossary:**

* **URL tracking parameters**: Parameters defined at the email channel configuration level that are appended to the end of the URLs in your email content, to be captured in web analytics tools and performance reports *(product-specific)*
* **Message profile id**: Message-oriented attribute uniquely identifying each message sent to each targeted profile in a delivery *(product-specific)*
* **Source action id / Source action name**: The ID / name of the Email action added to the journey or campaign *(product-specific)*
* **Source id / Source name / Source version id**: The ID / name / version ID of the journey or campaign the email was sent with *(product-specific)*
* **Offer id**: The ID of the offer used in the email *(product-specific)*

**Guardrails:**

* Activating URL tracking parameters is optional.
* You can add up to 10 tracking parameters using the Add new parameter button.
* Each Value field can contain a number of characters up to the limit of 5 KB.
* The order of URL tracking parameters appended to the URL is random and cannot be controlled; if a specific order is required, parse and reorder them on your side.
* Journeys that were closed or not republished after a product change may fail to populate `context.system.source.actionId`, resulting in empty placeholders; republish the affected journey or remove the reference for closed journeys.

**Terminology:**

* Canonical name: URL tracking — Acronym: n/a — variants: URL tracking parameters
* Synonyms: "Source action id" = "ID of the Email action"; "Source id" = "ID of the journey or campaign"
* Do not confuse: "Source action id / name" (the Email action) ≠ "Source id / name" (the journey or campaign)
* Do not confuse: configuration-level "URL tracking parameters" (applied to all content URLs) ≠ dynamic personalized tracking parameters added to individual links in content

**FAQ:**

* **Q: How many tracking parameters can I add?** — Up to 10, using the Add new parameter button.
* **Q: Is URL tracking mandatory?** — No; activating this feature is optional.
* **Q: Can I control the order of appended parameters?** — No; the order is random and cannot be controlled — parse and reorder on your side if needed.
* **Q: What is the character limit for a Value field?** — Up to 5 KB.
* **Q: Which predefined attributes are available?** — Message profile id, Offer id, Source action id, Source action name, Source id, Source name, and Source version id.
* **Q: Where can I capture these parameters?** — In web analytics tools such as Adobe Analytics or Google Analytics, and in performance reports.

+++

<!-- ai-section-version: 1 | source-hash: 02132b8a -->
