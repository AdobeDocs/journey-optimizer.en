---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to integrate Twilio with Journey Optimizer by creating API credentials for SMS, MMS, and RCS messaging so you can deliver Mobile messages in your journeys and campaigns.

**Intents:**

* Create Twilio API credentials for SMS and MMS
* Verify the SMS connection by sending a sample message to a designated device
* Route inbound SMS messages to a custom dataset
* Configure RCS with Twilio through a Custom SMS Provider

**Glossary:**

* **Account SID and Auth Token**: Twilio credentials found in the Account Info pane of the Twilio Console Dashboard page *(product-specific)*
* **Message SID**: The unique identifier assigned to every message created by Twilio's API *(product-specific)*
* **Inbound Number**: A unique inbound number that lets you use the same API credentials across different sandboxes, each with its own inbound number *(product-specific)*
* **Verify SMS connection**: An action on existing API credentials that tests them by sending a sample message to a designated device *(product-specific)*
* **Custom SMS Provider**: The feature through which RCS messaging is supported with Twilio, using "Custom" as the SMS vendor *(product-specific)*
* **Use custom dataset for inbound**: An option that routes a credential's inbound SMS to a pre-created dataset selected from a dropdown *(product-specific)*

**Guardrails:**

* RCS with Twilio requires the Custom SMS Provider feature; existing Twilio SMS credentials are not compatible because RCS requires a distinct payload format.
* RCS credentials must be defined using "Custom" as the SMS vendor, with the appropriate RCS endpoint authentication method, base URL, and headers.
* The custom dataset for inbound schema must be XDM ExperienceEvent and include at least the Message interaction details, Message Execution Details, and Message Profile Details field groups; the schema and dataset must be enabled for Profile.
* The Verify connection sample message must be structured to align with the provider's payload format.

**Terminology:**

* Canonical name: Twilio provider — Acronym: n/a — variants: Twilio configuration
* Do not confuse: "Twilio SMS credentials" (for SMS/MMS) ≠ RCS credentials configured via a Custom SMS Provider (distinct payload format)

**FAQ:**

* **Q: Can I reuse my Twilio SMS credentials for RCS?** — No; existing Twilio SMS credentials are not compatible because RCS requires a distinct payload format, so new credentials must be configured through a Custom SMS Provider.
* **Q: How is RCS supported with Twilio?** — RCS is supported through Twilio using the Custom SMS Provider feature, which enables rich, interactive messages with elements such as carousels, buttons, and multimedia via verified business profiles.
* **Q: Where do I find my Twilio Account SID and Auth Token?** — In the Account Info pane of your Twilio Console Dashboard page.
* **Q: How do I test my SMS API credentials?** — Click Verify SMS connection, fill in the Number and Message fields, and click Verify connection to send a sample message to a designated device.

+++

<!-- ai-section-version: 1 | source-hash: ba3ea2cd -->
