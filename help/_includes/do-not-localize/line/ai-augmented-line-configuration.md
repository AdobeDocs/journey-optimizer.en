---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to create a LINE channel configuration, from the interface or the API, so that Journey Optimizer can authenticate with the LINE Messaging API and send messages to your customers.

**Intents:**

* Create a LINE channel configuration from the Channel configurations menu
* Associate consent policies to the configuration through marketing actions
* Choose the message type (Marketing or Transactional) for the configuration
* Map the LINE user ID and define the Sender Name
* Configure the LINE Channel settings through the API

**Glossary:**

* **Channel configuration**: The configuration created from Channels > General settings > Channel configurations that defines how Journey Optimizer connects to and sends messages through a channel *(product-specific)*
* **Marketing action**: The setting used to associate consent policies to the messages using this configuration, so that customer preferences are respected *(product-specific)*
* **Channel settings**: The connection settings that store the authorization and configuration details for connecting to the LINE Messaging API *(product-specific)*
* **LINE user ID**: The identifier used to link messages to individual users within your LINE channel *(product-specific)*
* **Sender Name**: The name, such as your brand's name, entered for the configuration *(product-specific)*

**Guardrails:**

* Configuration names must begin with a letter (A-Z) and can only contain alphanumeric characters, underscore, dot, and hyphen.
* Marketing messages require user consent and should comply with LINE's policy regarding user opt-ins.
* Transactional messages can be sent even to users who have unsubscribed from marketing communications but are strictly limited to specific transactional contexts.
* The LINE user ID mapped here must already exist on your customers' Real-Time Customer Profile.
* Channel settings must be set up by reaching out to your Adobe representative.
* The API uses headers including a user token from your technical account, the client ID from Adobe Developer Console, the IMS Organization ID, the sandbox name, and Content-Type application/json.

**Terminology:**

* Canonical name: LINE channel configuration — Acronym: n/a — variants: channel configuration
* Do not confuse: "Marketing" (promotional messages requiring user consent) ≠ "Transactional" (non-commercial messages limited to specific transactional contexts)
* Do not confuse: "Channel settings" (authorization and connection details for the LINE Messaging API) ≠ "Marketing action" (associates consent policies to the configuration)

**FAQ:**

* **Q: What characters are allowed in a configuration name?** — The name must begin with a letter (A-Z) and can only contain alphanumeric characters, underscore, dot, and hyphen.
* **Q: What is the difference between a Marketing and a Transactional configuration?** — Marketing is for promotional messages that require user consent, while Transactional is for non-commercial messages that can reach unsubscribed users but are strictly limited to specific transactional contexts.
* **Q: Does the LINE user ID need to exist beforehand?** — Yes, the LINE user ID mapped in the configuration must already exist on your customers' Real-Time Customer Profile.
* **Q: How are the Channel settings set up?** — Reach out to your Adobe representative to set up your Channel settings.
* **Q: Can the configuration be created through the API?** — Yes, the Channel settings API stores the authorization and configuration details needed to connect to the LINE Messaging API.

+++

<!-- ai-section-version: 1 | source-hash: 023dffb8 -->
