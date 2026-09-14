---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page introduces Journey Optimizer custom channels, which let you bring any outbound HTTP endpoint into Journey Optimizer as a full channel using the Channel Builder, explains how they differ from custom actions, and outlines the configure, create, send, and monitor workflow.

**Intents:**

* Understand what custom channels are and what problem they solve
* Decide when to use a custom channel versus a custom action
* Identify use cases suited to custom channels, such as unsupported messaging platforms or custom delivery providers
* Understand the end-to-end workflow of configuring, creating, sending, and monitoring a custom channel
* Learn which capabilities custom channels support in campaigns and journeys

**Glossary:**

* **Custom channels**: A capability that lets you bring any outbound channel into Journey Optimizer for use in campaigns and journeys, like a native channel *(product-specific)*
* **Channel Builder**: The interface where administrators create and configure new custom channels without engineering involvement *(product-specific)*
* **Custom actions**: A capability for retrieving data from or pushing information to an external system as a step within a journey, available in journeys only *(product-specific)*
* **Channel configuration**: A configuration created and linked to the custom channel that a marketer selects when adding the channel to a journey or campaign *(product-specific)*

**Guardrails:**

* Custom channels are available in Limited Availability; contact your Adobe representative to gain access.
* Custom channels support POST as the only HTTP method.
* Custom actions are available in journeys only and support GET, PUT, and POST methods.
* Configuring a custom channel is an administrator task performed in the Channel Builder; adding the channel to a journey or campaign is a marketer task.

**Terminology:**

* Canonical name: Custom channels — Acronym: n/a — variants: custom channel capability, custom channel
* Synonyms: "Channel Builder" = the UI used to create and configure custom channels
* Do not confuse: "Custom channels" (send messages to end users through a platform not natively supported, available in campaigns and journeys, POST only) ≠ "Custom actions" (retrieve data from or push information to an external system, available in journeys only, GET/PUT/POST)

**FAQ:**

* **Q: What are custom channels?** — They let you bring any outbound HTTP endpoint into Journey Optimizer as a full channel so you can use it in campaigns and journeys, just like a native channel.
* **Q: When should I use a custom channel instead of a custom action?** — Use a custom channel when you need to send messages to end users through a platform not natively supported, and use a custom action when you need to retrieve data from or push information to an external system as a step within a journey.
* **Q: Which HTTP method do custom channels support?** — Custom channels support POST as the only HTTP method.
* **Q: What are the main stages of setting up and using a custom channel?** — Configure the channel in the Channel Builder (Admin), create the message in a journey or campaign (Marketer), send the personalized payload when a profile qualifies, and monitor performance through reporting and monitoring dashboards.
* **Q: Do I need engineering effort to set up a custom channel?** — No, administrators configure the channel through the Channel Builder UI; no custom code or engineering effort is required.
* **Q: What are typical use cases for custom channels?** — Unsupported messaging platforms such as WeChat or Kakao Talk, custom delivery providers, legacy messaging gateways that expose an HTTP endpoint, and industry-specific channels such as healthcare or banking notifications.

+++

<!-- ai-section-version: 1 | source-hash: bea60f28 -->
