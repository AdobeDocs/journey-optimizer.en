---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to configure and use Send-Time Optimization in Adobe Journey Optimizer, an AI-powered feature that predicts the best time to send email or push messages to each individual to maximize engagement.

**Intents:**

* Enable Send-Time Optimization on the Email or Push channel of an Action activity in a journey
* Choose whether to optimize for opens or click-throughs on email messages
* Set the maximum wait window (Send within next) for delayed delivery
* Understand how the AI model predicts optimal send times using behavioral data
* Determine whether Send-Time Optimization is appropriate for a given message type
* Use Send-Time Optimization within a Wait activity to delay before any downstream activity, decoupled from the message send

**Glossary:**

* **Send-Time Optimization (STO)**: An AI-powered feature that delays message delivery to each profile until the predicted optimal engagement hour within a configured time window *(product-specific)*
* **Journey AI**: Adobe's AI services powering Send-Time Optimization within Journey Optimizer *(product-specific)*
* **Exploration send time**: A randomly selected send time (used for 5% of sends) to test different times and improve model accuracy *(product-specific)*
* **Optimized send time**: A model-predicted send time selected to maximize click or open rates (used for 95% of sends) *(product-specific)*
* **Send within next**: The maximum number of hours (2–100) the system will wait before sending the message to a given profile *(product-specific)*

**Guardrails:**

* Send-Time Optimization must be enabled by Adobe for the organization; contact Adobe Customer Care or your Adobe representative to activate it.
* Send-Time Optimization is available for the Email and Push channels (selected in an Action activity) within journeys, and for the Wait activity; it is not currently available for messages sent through campaigns or for other action types.
* The organization should use the Email channel for a minimum of 30 days before using Send-Time Optimization within Email, and the Push channel for a minimum of 30 days before using it within Push; an organization that has already used the Email and/or Push channels for at least 30 days does not need to wait longer once the feature is enabled by Adobe.
* Do not use Send-Time Optimization for urgent or time-sensitive operational messages (e.g., order confirmations, password resets, flight gate changes).
* Maximum wait time range is 2–100 hours; recommended range is 6–24 hours for best results.
* Model scores are stored in profile attributes at `_experience.intelligentServices.journeyAI.sendTimeOptimization` and are not human-readable.
* Models are trained weekly initially, then retrained and rescored monthly after 16 weeks.

**Terminology:**

* Canonical name: Send-Time Optimization — Acronym: STO
* Do not confuse: "Exploration send time" ≠ "Optimized send time" (exploration is random for model testing; optimized is model-predicted for engagement)

**FAQ:**

* **Q: Which channels support Send-Time Optimization?** — The Email and Push channels (selected in an Action activity) within journeys, and the Wait activity; messages sent through campaigns and other action types are not currently supported.
* **Q: Should I optimize for opens or clicks on email?** — Optimize for Clicks for most emails. Choose Opens when the message is informational and not intended to drive a specific action.
* **Q: How long does the organization need to wait before enabling STO?** — The organization should use the Email channel (for Email) or the Push channel (for Push) for a minimum of 30 days to allow the collection of send, open, and click events. Results continue to improve for up to 16 weeks.
* **Q: Can STO send push notifications at night?** — Yes, if a user's behavior suggests night-time engagement or if an exploration send time is selected. To avoid this, use a morning send time with a short maximum wait window.
* **Q: What is the expected benefit of Send-Time Optimization?** — Approximately 2–10% improvement in email click rate or push open rate across all optimized messages, though benefits may not be observable on individual small-volume sends.

+++
