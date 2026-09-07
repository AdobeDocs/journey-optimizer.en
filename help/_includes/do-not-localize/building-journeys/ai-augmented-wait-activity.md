---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to configure the Wait activity in a journey to pause profile progression for a relative duration or until a custom calculated date before executing the next step.

**Intents:**

* Add a Wait activity to pause a journey for a fixed relative duration (up to 90 days)
* Configure a custom Wait using an advanced expression to delay until a profile-specific calculated date
* Understand how Wait activities interact with the journey global timeout (91 days)
* Use the Wait time in test parameter to speed up test mode validation
* Understand how profile attributes are refreshed after a Wait node in Read Audience journeys
* Use Send-Time Optimization within a Wait activity to determine the optimal time before continuing to any downstream activity

**Glossary:**

* **Wait activity**: A journey orchestration activity that pauses profile progression for a specified duration or until a calculated date before the next activity executes *(product-specific)*
* **Duration wait**: A Wait type that sets a relative time period to pause, with a maximum of 90 days *(product-specific)*
* **Custom wait**: A Wait type that uses a `dateTimeOnly` expression derived from profile or event data to define a specific future date/time for resumption *(product-specific)*
* **Send-time optimization wait**: A Wait type that uses Adobe's Send-Time Optimization AI model to select the optimal time to continue to the next activity, decoupled from any message send *(product-specific)*
* **Automatic wait node**: A 3-day Wait activity automatically inserted after inbound experience activities (In-app, Code-based, Card) to keep the profile in the journey long enough to view the content *(product-specific)*
* **Wait time in test**: A journey test mode parameter that overrides actual wait durations (default 10 seconds) so test results are returned quickly *(product-specific)*

**Guardrails:**

* The maximum wait duration is 90 days.
* Profiles are dropped from a journey after 91 days (global timeout), regardless of pending wait activities.
* A profile can only enter a Wait activity if enough time remains in the journey to complete the wait before the 91-day timeout.
* Do not use Wait activities to block reentrance; use the Allow reentrance option in journey properties instead.
* Custom wait expressions must use `dateTimeOnly` format and must not include a `Z` suffix or explicit time zone offset.
* Using a fixed static date (e.g., `toDateTimeOnly('2024-01-01T01:11:00Z')`) in a custom wait can cause issues; use profile-specific dynamic dates instead.
* Profile attributes are refreshed from the Unified Profile Service after a wait node in Read Audience journeys, which may produce unexpected results if snapshot consistency is expected.
* Send-Time Optimization within a Wait activity has no visibility into quiet hours rules; if a downstream channel action is protected by a quiet hours rule set to discard messages, the profile can be removed from the message delivery and exited from the journey.

**Terminology:**

* Canonical name: Wait activity — Acronym: none — variants: Wait node, wait step
* Synonyms: "Duration wait" = "relative wait"; "Custom wait" = "expression-based wait"
* Do not confuse: "Duration wait" (relative, e.g. 3 days from now) ≠ "Custom wait" (absolute calculated date from profile data)

**FAQ:**

* **Q: What is the maximum duration for a Wait activity?** — The maximum wait duration is 90 days; profiles are also subject to the 91-day global journey timeout.
* **Q: How does test mode handle Wait activities?** — In test mode, the "Wait time in test" parameter overrides the actual wait duration; the default is 10 seconds so tests complete quickly.
* **Q: Why should I avoid appending Z to a custom wait expression?** — Adding Z or a time zone offset to a `toDateTimeOnly()` expression can cause profiles to get stuck in the wait activity; the expression must rely on the journey's configured time zone.
* **Q: Are profile attributes updated after a Wait node?** — Yes, in journeys starting with Read Audience, the journey refreshes profile attributes from the Unified Profile Service after the wait, so downstream activities may see updated values rather than the original audience snapshot data.
* **Q: What is the automatic wait node?** — A 3-day Wait activity automatically inserted after inbound experience activities (In-app, Code-based, Card) to ensure profiles remain in the journey long enough to see the message; it can be removed or reconfigured as needed.
* **Q: Does the Send-Time Optimization Wait activity know about quiet hours?** — No. Quiet hours are only evaluated at the message action, so the Wait activity can pick a time inside a quiet-hours window. Depending on the quiet hours rule, the message is then queued until quiet hours end, or discarded, which also exits the profile from the journey.

+++
