---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how an administrator creates a channel configuration that links a custom channel to a named, reusable preset, including API credentials, an optional subdomain, dynamic parameters, and payload defaults, so that marketers can select it when building campaigns and journeys.

**Intents:**

* Create a channel configuration for an activated custom channel
* Select the API credentials to use for the configuration
* Select a delegated subdomain for tracking links in the payload
* Provide values for dynamic parameters and payload fields
* Save and activate the channel configuration for marketers to select

**Glossary:**

* **Channel configuration**: A named, reusable preset that links a custom channel to credentials, a subdomain, and payload defaults, which marketers select when building campaigns and journeys *(product-specific)*
* **Dynamic parameters**: The section that appears when the channel has headers or query parameters defined as variable, where a value is entered for each parameter *(product-specific)*
* **Payload configuration**: The section that displays payload fields whose Channel config checkbox is enabled, where a value is configured for each field *(product-specific)*
* **Delegated subdomain**: A subdomain that can be selected to track links present in the payload for this configuration *(product-specific)*

**Guardrails:**

* Only activated custom channels can be selected in the Select channel drop-down.
* The API credentials field appears only if the selected channel uses an authentication type other than None.
* The Dynamic parameters section appears only if the channel has headers or query parameters defined as variable.
* The Payload configuration section appears only for payload fields that have the Channel config checkbox enabled.
* Clicking Submit saves and activates the channel configuration.

**Terminology:**

* Canonical name: channel configuration — Acronym: n/a — variants: custom channel configuration, named preset
* Synonyms: "Dynamic parameters" = "variable headers or query parameters"
* Do not confuse: "channel configuration" (the reusable preset) ≠ "custom channel" (the underlying channel definition)
* Do not confuse: "Dynamic parameters" (values for variable headers or query parameters) ≠ "Payload configuration" (values for payload fields enabled for the channel config)

**FAQ:**

* **Q: What does a channel configuration do?** — It links a custom channel to a named, reusable preset that marketers select when building campaigns and journeys.
* **Q: When does the API credentials field appear?** — When the selected channel uses an authentication type other than None.
* **Q: When does the Dynamic parameters section appear?** — When the channel has headers or query parameters defined as variable.
* **Q: Which channels can I select?** — Only your activated custom channels.
* **Q: How do I save a channel configuration?** — Click Submit to save and activate it.

+++

<!-- ai-section-version: 1 | source-hash: fcf9940a -->
