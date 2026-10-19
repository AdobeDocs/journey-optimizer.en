---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to configure Infobip as your provider in Journey Optimizer by setting up SMS API credentials, and how to enable RCS messaging with Infobip through a Custom SMS Provider integration.

**Intents:**

* Configure SMS API credentials with Infobip as the SMS vendor
* Set the DLT Principal Entity ID and Content Template ID and the message validity period
* Enable Fuzzy Opt-out detection and customize the Fuzzy Auto Reply confirmation
* Route a credential's inbound SMS to a custom dataset
* Enable RCS messaging with Infobip through a Custom SMS Provider
* Verify the SMS connection by sending a sample message to a designated device

**Glossary:**

* **Validity Period**: The message validity period in hours; if messages cannot be delivered within this timeframe, the system makes additional attempts to resend them *(product-specific)*
* **Fuzzy Opt-out**: An option that detects SMS messages resembling opt-out keywords (for example, CANCIL), including common opt-out phrases and certain offensive terms *(product-specific)*
* **Fuzzy Auto Reply**: The field where the confirmation reply for a fuzzy opt-out is customized *(product-specific)*
* **Inbound Number**: A unique inbound number that allows the same API credentials to be used across different sandboxes, each with its own inbound number *(product-specific)*
* **Custom SMS Provider**: The feature used to enable RCS messaging with Infobip, requiring new API credentials with a distinct payload format *(product-specific)*

**Guardrails:**

* The default validity period is 48 hours.
* RCS with Infobip requires new API credentials configured via a Custom SMS Provider; existing Infobip SMS credentials are not compatible, as RCS requires a distinct payload format.
* The custom inbound dataset schema must be XDM ExperienceEvent, include the Adobe CJM ExperienceEvent Message interaction details, Message Execution Details, and Message Profile Details field groups, and be enabled for Profile.
* The verify-connection message must be structured to align with the provider's payload format.

**Terminology:**

* Canonical name: Infobip provider — Acronym: n/a — variants: Infobip SMS provider, Infobip configuration
* Do not confuse: "Fuzzy Opt-out" (the detection option) ≠ "Fuzzy Auto Reply" (the field for the confirmation reply)
* Do not confuse: "Infobip SMS API credentials" (for SMS) ≠ "Custom SMS Provider credentials" (required for RCS with Infobip)

**FAQ:**

* **Q: What is the default message validity period?** — 48 hours; if messages cannot be delivered within this timeframe, the system makes additional attempts to resend them.
* **Q: Can I use the same API credentials across sandboxes?** — Yes; add a unique Inbound Number so the same API credentials can be used across different sandboxes, each with its own inbound number.
* **Q: How do I enable RCS with Infobip?** — RCS is supported through Infobip using the Custom SMS Provider feature; register your business for RCS via Infobip, create a custom SMS webhook, and create a new API credential selecting Custom as the SMS vendor.
* **Q: Can existing Infobip SMS credentials be used for RCS?** — No; existing Infobip SMS credentials are not compatible because RCS requires a distinct payload format.
* **Q: What does Fuzzy Opt-out do?** — It identifies SMS messages that indicate a user wants to unsubscribe even when the message does not exactly match a defined opt-out keyword, helping campaigns remain compliant.

+++

<!-- ai-section-version: 1 | source-hash: 698c0ea1 -->
