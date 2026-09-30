---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to create inbound and feedback SMS webhooks in Adobe Journey Optimizer to capture opt-in and opt-out consent responses and delivery events for Sinch, Sinch Conversational, Infobip, and custom providers.

**Intents:**

* Create an SMS webhook to capture inbound consent responses and user preferences
* Create a feedback webhook to track delivery and engagement events
* Configure inbound keyword categories such as Opt-In, Opt-Out, Double Opt-In, Help, and Custom
* Configure custom JSON payloads for a custom provider's inbound and feedback webhooks
* Copy the webhook URL to bring inbound and feedback events into Journey Optimizer

**Glossary:**

* **Inbound webhook**: Webhook type used to capture consent responses, such as opt-ins or opt-outs, and to collect user preferences *(product-specific)*
* **Feedback webhook**: Webhook type used to track delivery and engagement events, including deliveries, outbound errors, and read receipts where applicable *(product-specific)*
* **Inbound Keyword Category**: The drop-down grouping keywords into Opt-In, Opt-Out, Double Opt-In, Help, and Custom *(product-specific)*
* **Double Opt-In**: A two-step consent workflow where matching a keyword does not fully opt in the user until they confirm with a second keyword *(product-specific)*
* **Fuzzy Logic**: An Opt-Out option that detects keywords similar to configured Opt-Out keywords and sends the Fuzzy Auto Response when a response is close but not exact *(product-specific)*
* **Default Reply Message**: The message automatically sent when a user's response does not match any configured keyword *(product-specific)*

**Guardrails:**

* The only webhook format supported is JSON; form-data for webhooks is not supported.
* Inbound keyword data is stored in the AJO Email Tracking Dataset system dataset, unless a custom dataset is configured.
* A profile must have at least one message sent from Journey Optimizer before incoming messages are captured.
* Sinch and Sinch Conversational use a single webhook that handles both inbound and feedback events, with no payload configuration required.
* Infobip uses two separate webhooks, one for inbound and one for feedback events, with no payload configuration required.
* Twilio webhooks are not available; inbound and feedback data collection is not supported.
* A custom provider uses two separate webhooks, one for inbound and one for feedback events, and payload configuration is required for both to function.
* Default enabled keywords are Opt-In (Subscribe, Yes, Unstop, Continue, Resume, Begin), Opt-Out (Stop, Quit, Cancel, End, Unsubscribe, No), and Help (Help, Info, Information).
* Keywords are not case sensitive.
* The Custom keyword category configures a single custom keyword.
* The custom inbound webhook payload requires the fields InboundMessage, ProfileNumber, RequestID, OriginTimestamp, and InboundNumber.
* The custom feedback webhook payload requires the fields Client Reference, Code, and Status.
* If the webhook uses API credentials attached to an existing channel configuration, it takes effect immediately; otherwise you must create a new channel configuration.

**Terminology:**

* Canonical name: SMS Webhook — Acronym: n/a — variants: SMS webhooks, Callback URL
* Do not confuse: "Inbound" webhook (captures consent responses and user preferences) ≠ "Feedback" webhook (tracks delivery and engagement events)
* Do not confuse: "Opt-In" (grants consent) ≠ "Double Opt-In" (two-step consent requiring confirmation with a second keyword)
* Do not confuse: "Reply Message" (sent when an inbound message matches a configured keyword) ≠ "Default Reply Message" (sent when the response does not match any configured keyword) ≠ "Fuzzy Auto Response" (sent when a response is close but not an exact Opt-Out keyword)

**FAQ:**

* **Q: What is the difference between an inbound and a feedback webhook?** — An inbound webhook captures consent responses such as opt-ins and opt-outs and collects user preferences, while a feedback webhook tracks delivery and engagement events such as deliveries, outbound errors, and read receipts where applicable.
* **Q: How many webhooks do I create for each provider?** — Sinch and Sinch Conversational use one webhook for both event types; Infobip and custom providers use two separate webhooks; Twilio webhooks are not available.
* **Q: Which webhook format is supported?** — Only JSON is supported; form-data for webhooks is not supported.
* **Q: Which fields must a custom inbound payload include?** — InboundMessage, ProfileNumber, RequestID, OriginTimestamp, and InboundNumber.
* **Q: When does a webhook take effect?** — If it uses API credentials attached to an existing channel configuration, it takes effect immediately; otherwise you must create a new channel configuration.
* **Q: Why are incoming messages not captured for a profile?** — A profile must have at least one message sent from Journey Optimizer before incoming messages are captured.

+++

<!-- ai-section-version: 1 | source-hash: 209fd11f -->
