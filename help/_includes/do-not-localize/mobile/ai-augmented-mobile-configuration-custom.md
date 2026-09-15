---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to integrate a custom messaging provider in Journey Optimizer by creating API credentials, choosing an authentication method, and configuring headers, payloads, mTLS, and inbound settings to send SMS and RCS messages beyond the default Sinch, Twilio, and Infobip options.

**Intents:**

* Create a custom provider API credential with SMS vendor set to Custom
* Choose and complete an authentication method (API key, MAC, OAuth, or JWT)
* Configure HTTP headers and the Provider Payload for the request
* Enable mTLS support for mutual client and server authentication
* Route a credential's inbound SMS to a custom dataset
* Verify the SMS connection by sending a sample message to a designated device

**Glossary:**

* **Custom provider**: A third-party messaging provider integrated beyond the default options (Sinch, Twilio, and Infobip) by selecting Custom as the SMS vendor *(product-specific)*
* **Provider Payload**: The request payload used to validate and customize requests, later used during RCS content design *(product-specific)*
* **Channel Type**: An optional classification (SMS, RCS, or MMS) written to XDM experience events for reporting and tracking by channel *(product-specific)*
* **mTLS support**: An option ensuring that both the client and server authenticate each other before establishing a secure connection *(product-specific)*
* **Verify SMS connection**: An action that tests and verifies the API credentials by sending a sample message to a designated device *(product-specific)*

**Guardrails:**

* You can add up to 10 custom header parameters.
* The Content-Type and Charset header fields are set by default and cannot be deleted, though the default Content-Type value can be edited.
* mTLS applies only to the SMS provider (message sending) endpoint; the OAuth token endpoint must not use mTLS and mTLS must be disabled on the token endpoint before testing.
* With Basic or Bearer authentication, the authOption parameter must be included in the JSON payload, and the Provider Payload must reference the template variables {{fromNumber}}, {{toNumber}}, and {{message}}.
* The custom inbound dataset schema must be XDM ExperienceEvent, include the Adobe CJM ExperienceEvent Message interaction details, Message Execution Details, and Message Profile Details field groups, and be enabled for Profile.
* Do not reuse the same API credentials, webhooks, or provider callback URLs (including RCS agents) across sandboxes; create separate agent configurations for each sandbox.

**Terminology:**

* Canonical name: Custom provider — Acronym: n/a — variants: custom messaging provider, custom SMS provider, Bring Your Own Provider
* Do not confuse: "SMS provider (message sending) endpoint" (uses mTLS) ≠ "OAuth token endpoint" (must not use mTLS)
* Do not confuse: "API key" ≠ "MAC authentication" ≠ "OAuth authentication" ≠ "JWT authentication" (the four Auth Type options)

**FAQ:**

* **Q: How many custom header parameters can I add?** — Up to 10 custom header parameters.
* **Q: Which authentication types are supported?** — API key, MAC authentication, OAuth authentication, and JWT authentication.
* **Q: Which endpoint uses mTLS?** — mTLS applies only to the SMS provider (message sending) endpoint; the OAuth token endpoint must not use mTLS.
* **Q: What must the Provider Payload include for Basic or Bearer authentication?** — The authOption parameter in the JSON payload, plus references to the template variables {{fromNumber}}, {{toNumber}}, and {{message}}.
* **Q: How do I test the credential?** — Click Verify SMS connection, fill in the Number and Message fields structured to align with the provider's payload format, then click Verify connection to send a sample message to a designated device.

+++

<!-- ai-section-version: 1 | source-hash: a421ccaf -->
