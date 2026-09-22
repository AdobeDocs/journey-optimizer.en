---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page introduces Journey Optimizer's conflict management and prioritization tools—conflict detection, priority scores, and rule sets (journey capping & arbitration, frequency capping by channel, and quiet hours)—and how they work together.

**Intents:**

* Understand which tool to use to spot overlaps, set precedence, or limit message frequency
* Use conflict detection to find overlapping journeys and campaigns
* Assign priority scores to control which communication takes precedence
* Group rules into rule sets for journey capping & arbitration, frequency capping, and quiet hours
* Know the guardrails that affect capping and prioritization

**Glossary:**

* **Conflict detection tool**: Identifies potential overlaps in journeys and campaigns *(product-specific)*
* **Priority scores**: Control which campaigns or journeys take precedence when a customer qualifies for multiple communications *(product-specific)*
* **Rule sets**: Group multiple rules and apply them to the journeys and campaigns of your choice *(product-specific)*
* **Journey capping & arbitration**: Limits how often and how many journeys a customer can enter, using arbitration and priority scores to decide which journey the customer should enter *(product-specific)*
* **Frequency capping by channel and communication type**: Sets frequency capping by communication type across multiple channels, excluding over-solicited profiles *(product-specific)*
* **Quiet hours**: Time-based exclusions so no messages are sent during specific periods (Email, SMS, Push, WhatsApp) *(product-specific)*
* **Arbitration**: Deciding which journey a customer enters when they qualify for multiple journeys, using priority scores to determine the best fit *(product-specific)*

**Guardrails:**

* These tools are available for campaigns and for unitary, Audience Qualification, and Read audience journeys.
* In campaigns, priority score is available for the web, in-app, and code-based inbound channels only.
* It can take up to 10 minutes after a customer enters a journey for the profile counter value to update; a profile entering two journeys within a short window may enter both.
* Entry capping is only supported if the namespace selected in the journey is the highest priority namespace defined in the sandbox; if namespace priority is not configured, the default highest priority is email.
* When multiple audience qualification journeys are activated by the same audience qualification event, entry capping counts will not be accurate.

**Terminology:**

* Canonical name: conflict management & prioritization — Acronym: n/a — variants: conflict & prioritization tools
* Synonyms: none
* Do not confuse: "conflict detection" (spots overlaps) ≠ "priority scores" (sets precedence) ≠ "rule sets" (limit frequency and volume)
* Do not confuse: "journey capping" (limits journey entries or concurrency) ≠ "frequency capping by channel" (limits messages per channel and communication type) ≠ "quiet hours" (time-based message exclusions)

**FAQ:**

* **Q: Which tool spots overlapping journeys and campaigns?** — Conflict detection.
* **Q: How do I decide which message wins when a profile qualifies for several?** — Assign priority scores.
* **Q: How do I limit how often or how many messages a profile receives?** — Use rule sets (frequency capping, journey capping, and quiet hours).
* **Q: On which channels is priority score available in campaigns?** — Web, in-app, and code-based inbound channels only.
* **Q: Why might a profile enter two capped journeys?** — The profile counter can take up to 10 minutes to update, so a profile entering two journeys within a short window may not be recognized as having reached the cap.

+++

<!-- ai-section-version: 1 | source-hash: 51614d84 -->
