---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to use the built-in Reaction event activity in Adobe Journey Optimizer to branch journey paths based on real-time message engagement data such as email opens and link clicks.

**Intents:**
* Add a Reaction event activity to respond to message opens or clicks within a journey
* Configure a timeout duration and fallback path for profiles that do not engage
* Create a parallel path with a Wait activity to handle non-responders
* Select a specific upstream channel action activity to listen to

**Glossary:**
* **Reaction event**: A built-in journey event activity that listens to real-time tracking data (opens, clicks) from a message sent earlier in the same journey *(product-specific)*
* **Timeout path**: A secondary journey branch that profiles follow if they do not produce the expected reaction within the defined timeout period *(product-specific)*

**Guardrails:**
* The Reaction activity must be placed immediately after a channel action activity; no other activity can be placed between them.
* A Reaction activity cannot be used if there is no channel action activity before it in the path.
* Reaction events can only track messages sent within the same journey; cross-journey tracking is not supported.
* Unsubscription links and mirror page links are not tracked by reaction events.
* Email opens rely on a 0-pixel tracking image; if the email client blocks images (e.g., Gmail), opens will not be recorded.
* Event timeout range is 40 seconds to 90 days; the minimum value in test mode is also 40 seconds.

**Terminology:**
* Canonical name: Reaction events — Acronym: none — variants: reaction activity, engagement tracking event
* Synonyms: "Reaction event" = "message engagement event" = "tracking event"
* Do not confuse: "Reaction event" ≠ "external event" (reaction events are built-in and tied to same-journey messages; external events come from outside the journey)

**FAQ:**
* **Q: Can a Reaction event track a message sent in a different journey?** — No; reaction events only track messages sent within the same journey.
* **Q: How do I handle profiles that do not open or click a message?** — Add a parallel path alongside the Reaction activity with a Wait activity; profiles that do not react within the wait duration will follow that second path.
* **Q: Are unsubscribe link clicks tracked by reaction events?** — No; only tracked link types are captured. Unsubscription and mirror page links are excluded.
* **Q: What happens if an email client blocks images?** — Email opens tracked via the 0-pixel image will not be recorded for clients that block images, such as Gmail.
* **Q: What is the valid timeout range for a reaction event?** — Between 40 seconds and 90 days.

+++
