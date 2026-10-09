---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how channel optimization selects an outbound channel for each customer in a journey or campaign using manual priority, profile preferences, or AI propensity scores.

**Intents:**
* Configure multiple outbound channels in a journey or campaign action
* Select a channel optimization method
* Define channel priority and understand fallback behavior
* Validate and test a journey before publication

**Glossary:**
* **Channel optimization**: Selects the best outbound channel for each customer at send time *(product-specific)*
* **[!UICONTROL Manual priority]**: The default mode; selects the first opted-in channel that is not frequency-capped from the configured channel order *(product-specific)*
* **[!UICONTROL Customer profile attribute]**: Selects a channel using the profile's declared preference in the `preferred` attribute; supported values are `email`, `push`, and `sms` *(product-specific)*
* **[!UICONTROL AI optimized]**: Selects the channel with the highest predicted propensity based on historical engagement; scores are stored in the customer profile *(product-specific)*

**Guardrails:**
* Channel optimization is in Limited Availability; access requires contacting an Adobe representative.
* Only native Email, Push, and Mobile message channels are supported; execution through custom actions is not supported.
* A single journey action or campaign supports up to three outbound channels (hard limit), with only one action per channel type.
* AI ranking optimizes for engagement clicks, not orders or revenue, and requires click tracking for all configured channels.
* Quiet hours priority is Mobile messaging, then Push, then Email. Separate journey actions are required for different quiet hours settings per channel.
* Send-Time Optimization and channel optimization cannot be enabled together on the same action.
* Reaction events currently reference only the first channel in a multi-channel action.
* For journeys, validation and error resolution precede testing; publication requires completed testing and current, passed validation.

**Terminology:**
* Do not confuse: **[!UICONTROL Manual priority]** and **[!UICONTROL Customer profile attribute]** use the configured priority list for fallback; **[!UICONTROL AI optimized]** selects a random available fallback channel.
* A channel is unavailable when the customer is not opted in, the channel is not configured, its frequency cap is reached, or the profile preference or AI model score is not populated.

**FAQ:**
* **Q: What happens when the preferred channel is unavailable?** - Journey Optimizer uses the configured fallback list for **[!UICONTROL Customer profile attribute]**.
* **Q: What happens when there is insufficient engagement history for AI ranking?** - The system falls back to a randomly available channel.
* **Q: Can I optimize for revenue using the AI model?** - The AI model optimizes for clicks only. A custom model can be trained offline and applied through the customer profile attribute feature.

+++

<!-- ai-section-version: 1 | source-hash: c06ee19a -->