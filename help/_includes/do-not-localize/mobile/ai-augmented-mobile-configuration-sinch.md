---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to configure Sinch as your provider in Journey Optimizer by setting up separate API credentials for SMS, MMS, and RCS messages.

**Intents:**

* Configure Sinch API credentials to send SMS messages
* Configure Sinch MMS API credentials for outbound MMS delivery
* Configure Sinch RCS API credentials to send RCS messages
* Verify the SMS connection by sending a sample message to a designated device
* Route inbound SMS or RCS messages to a custom dataset
* Set an API rate limit for RCS API requests

**Glossary:**

* **SMS Configuration**: The Sinch option used to set up API credentials for sending SMS messages *(product-specific)*
* **MMS Configuration**: The Sinch option for multimedia messaging; used only for outbound delivery of the MMS message, while tracking and responding to inbound messages are handled by the SMS configuration *(product-specific)*
* **RCS Configuration**: The Sinch option used to set up API credentials for sending RCS messages *(product-specific)*
* **Inbound Number**: A unique inbound number or short code that lets you use the same API credentials across different sandboxes, each with its own inbound number or short code *(product-specific)*
* **Override URL**: A custom URL that replaces the default endpoints for SMS delivery reports, feedback data, inbound messages, or event notifications *(product-specific)*
* **API rate limit (requests per second)**: A cap on the maximum number of API calls per second for RCS *(product-specific)*
* **Use custom dataset for inbound**: An option that routes a credential's inbound messages to a pre-created dataset selected from a dropdown *(product-specific)*
* **Verify SMS connection**: An action on existing API credentials that tests them by sending a sample message to a designated device *(product-specific)*

**Guardrails:**

* MMS setup is only for outbound delivery of the MMS message; tracking and responding to inbound messages are handled by the SMS configuration.
* Along with MMS setup, you must also create Sinch API credentials specifically for tracking inbound messages and managing consent requests.
* Native RCS authoring requires Sinch RCS; Twilio, Infobip, and other providers must use a custom provider integration.
* Messages automatically fall back to SMS when the profile's device does not support RCS or is temporarily unreachable via RCS.
* API rate limit (requests per second) for RCS: use your provider's recommended value to avoid throttling (recommended), or leave it at 0 for unlimited requests.
* The custom dataset for inbound schema must be XDM ExperienceEvent and include at least the Message interaction details, Message Execution Details, and Message Profile Details field groups; the schema and dataset must be enabled for Profile.
* The Verify connection sample message must be structured to align with the provider's payload format.

**Terminology:**

* Canonical name: Sinch provider — Acronym: n/a — variants: Sinch configuration
* Do not confuse: "SMS Configuration" ≠ "MMS Configuration" ≠ "RCS Configuration" (three distinct Sinch options)
* Do not confuse: "Sinch" (SMS vendor value for SMS) ≠ "Sinch MMS" (SMS vendor value for MMS) ≠ "Sinch RCS" (SMS vendor value for RCS)

**FAQ:**

* **Q: Which credentials handle inbound tracking for MMS?** — The SMS configuration handles tracking and responding to inbound messages; MMS setup is only for outbound delivery, and you must also create Sinch API credentials specifically for tracking inbound messages and managing consent requests.
* **Q: Can I author RCS natively with Twilio or Infobip?** — No; native RCS authoring requires Sinch RCS, and Twilio, Infobip, and other providers must use a custom provider integration.
* **Q: What happens when a recipient's device does not support RCS?** — Messages automatically fall back to SMS when the profile's device does not support RCS or is temporarily unreachable via RCS.
* **Q: How do I test my SMS API credentials?** — Click Verify SMS connection, fill in the Number and Message fields, and click Verify connection to send a sample message to a designated device.
* **Q: What does the API rate limit setting do for RCS?** — It caps the maximum number of API calls per second; use your provider's recommended value to avoid throttling, or leave it at 0 for unlimited requests.

+++

<!-- ai-section-version: 1 | source-hash: 39fc9e29 -->
