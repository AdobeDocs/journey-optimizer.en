---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page gives an overview of the four steps an administrator completes once per channel to configure a custom channel in Journey Optimizer so that marketers can then select it in campaigns and journeys like any native channel.

**Intents:**

* Understand the four-step process required to configure a custom channel
* Identify which step defines the endpoint, headers, throttling policy, authentication type, and message payload
* Learn why creating multiple API credential sets is useful
* Determine when delegating a subdomain is required
* Understand what a channel configuration provides to marketers

**Glossary:**

* **Custom channel**: A channel that sends messages to an external system, configured once by an administrator and then selectable by marketers like any native Journey Optimizer channel *(product-specific)*
* **Channel Builder**: The interface where the channel endpoint, authentication, and payload are defined *(product-specific)*
* **API credentials**: The sets of credentials used to authenticate requests sent to your endpoint *(product-specific)*
* **Channel configuration**: A named preset that links the custom channel to a specific set of credentials, a subdomain, and optional payload defaults, which marketers select at authoring time *(product-specific)*

**Guardrails:**

* This capability is available in Limited Availability; contact your Adobe representative to gain access.
* Configuring a custom channel is an administrator task that happens once per channel.
* Delegating a subdomain is optional and required only if your message payload contains trackable links; without a delegated subdomain, link tracking is unavailable for this channel.
* Before you begin, review the prerequisites and guardrails, including the required permissions and supported authentication methods.

**Terminology:**

* Canonical name: custom channel — Acronym: n/a — variants: custom channel configuration
* Synonyms: "channel configuration" = "named preset"
* Do not confuse: "custom channel" ≠ "channel configuration" (the channel configuration is a preset that links a custom channel to credentials, a subdomain, and payload defaults)

**FAQ:**

* **Q: How many steps does configuring a custom channel involve?** — Four: create the custom channel, manage API credentials, optionally delegate a subdomain, and create a channel configuration.
* **Q: Is delegating a subdomain always required?** — No, it is optional and required only when your message payload contains trackable links.
* **Q: Who configures a custom channel?** — An administrator, as a task that happens once per channel.
* **Q: What can marketers do after a custom channel is configured?** — They can immediately select it in campaigns and journeys, just like any native Journey Optimizer channel.
* **Q: Why create multiple credential sets?** — To reuse the same channel definition across different brands or environments without duplicating the channel.

+++

<!-- ai-section-version: 1 | source-hash: c521dbb2 -->
