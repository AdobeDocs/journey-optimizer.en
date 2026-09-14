---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This guide explains how to define, configure, and optimize journey entry and exit criteria in Adobe Journey Optimizer, with real-world examples and best practices to ensure the right profiles are reached at the right time.

**Intents:**

* Configure event-based, audience-based, or attribute-based entry criteria for a journey
* Set up exit criteria based on journey completion, success metrics, inactivity timeouts, or audience disqualification
* Apply re-entry rules to control whether profiles can enter a journey multiple times
* Avoid overlapping journeys using conflict management and priority scores
* Monitor and optimize entry and exit rates using journey reports

**Glossary:**

* **Entry criteria**: The conditions that determine when a customer profile qualifies to enter a journey *(product-specific)*
* **Exit criteria**: The conditions that define when and how a profile leaves or is removed from a journey *(product-specific)*
* **Audience qualification**: A journey entry mechanism that triggers when a profile enters or exits a streaming audience in real-time *(product-specific)*
* **Re-entrance**: The ability for a profile to enter the same journey more than once, configurable with a wait period *(product-specific)*
* **Frequency capping**: A rule that limits how many messages a profile can receive within a given time window *(product-specific)*

**Guardrails:**

* A profile cannot be present multiple times in the same journey at the same time.
* Re-entrance must be explicitly enabled; the default reentrance wait period is 5 minutes with a maximum of 91 days.
* For advanced multi-journey frequency management, use journey capping and arbitration rather than individual exit criteria.
* Journey overlaps must be managed proactively; use conflict management and priority scores to resolve competing journeys.

**Terminology:**

* Canonical name: Entry criteria — Acronym: n/a — variants: entry conditions, journey triggers
* Canonical name: Exit criteria — Acronym: n/a — variants: exit conditions, profile removal rules
* Synonyms: "audience disqualification" = "audience exit" as an exit trigger
* Do not confuse: "Close to new entrances" ≠ "exit criteria" — the former blocks new entries; exit criteria removes in-progress profiles

**FAQ:**

* **Q: Can a profile be in the same journey twice at the same time?** — No, a profile cannot be present in the same journey at the same time. The profile identity is used as a key to enforce this.
* **Q: How do I prevent a profile from re-entering a journey?** — Disable re-entrance in the journey Properties panel, or add a condition to check whether the profile has already entered.
* **Q: What is the difference between exit criteria and closing a journey?** — Exit criteria removes individual profiles from a live journey based on conditions; closing a journey stops all new entrances while letting current profiles finish.
* **Q: How do I stop over-communicating with customers across multiple journeys?** — Use frequency capping rules and journey capping and arbitration to enforce cross-journey message limits.
* **Q: What is audience disqualification as an exit trigger?** — When a profile no longer meets the target audience segment criteria, it is automatically removed from the journey to keep communications relevant.

+++
