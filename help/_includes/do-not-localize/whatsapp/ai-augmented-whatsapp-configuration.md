---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how a System Administrator configures the WhatsApp channel in Journey Optimizer by creating WhatsApp API credentials, a Webhook, and a channel configuration to connect a WhatsApp Business account.

**Intents:**

* Create WhatsApp API credentials and connect a WhatsApp Business Account
* Create a WhatsApp Webhook to capture inbound responses, receive delivery reports, and enable tracking events
* Create a WhatsApp channel configuration and associate marketing actions and consent policies
* Set the sender phone number and WhatsApp Execution Field for a configuration
* Troubleshoot HTTP 500 errors during API credential setup

**Glossary:**

* **API Credentials**: The credential set (API Token and Business Account ID) used to connect Journey Optimizer to a WhatsApp Business Account *(product-specific)*
* **API Token**: A Meta access token from a System User in the same Business Manager as your WhatsApp assets, used to authenticate *(product-specific)*
* **Business Account ID**: Your Meta Business portfolio ID (Business Manager ID), not the WhatsApp Business Account ID *(product-specific)*
* **Webhook**: The communication bridge between Meta's WhatsApp Business Platform and Journey Optimizer that receives real-time notifications about message events and user interactions *(product-specific)*
* **Inbound keyword category**: The classification (Opt-in, Opt-out, Help, Default) that determines which auto-response is sent based on user text *(product-specific)*
* **WhatsApp Execution Field**: The field used to select, among profile attributes, the phone number to use in priority when several numbers are available *(product-specific)*
* **Quality Rating**: A rating (Green/High, Yellow/Medium, Red/Low) reflecting customer feedback on messages sent in the past 24 hours *(product-specific)*
* **Throughput**: The rate at which your phone number can send messages *(product-specific)*

**Guardrails:**

* These steps must be performed by a Journey Optimizer System Administrator.
* Meta tokens expire after about 60 days; renew the token before it lapses.
* The API Token's System User needs whatsapp_business_management, whatsapp_business_messaging, and business_management permissions, plus asset-level access to your WhatsApp Business Account.
* Meta allows only one webhook, callback URL, and Verify Token per WhatsApp Business Account, even across multiple sandboxes or WhatsApp credentials.
* Feedback events (Sent, Delivered, Read, Error, button click) are captured correctly in every sandbox, but inbound events (replies, opt-in/opt-out/help keywords) are only received in the single sandbox where the webhook is registered; register it against your production sandbox to receive inbound events there.
* Without specified opt-in or opt-out keywords, standard consent messages are not enabled.
* A profile must have at least one message sent from Journey Optimizer before incoming messages are captured in the dataset.
* Keywords are not case-sensitive (e.g., stop and STOP are treated the same).
* Configuration names must begin with a letter (A-Z), can only contain alpha-numeric characters, and may also use underscore, dot, and hyphen.
* Do not include a '+' sign before the sender phone number, as this can prevent the opt-out flow from working correctly.
* HTTP 500 troubleshooting: the organization must have the `cjm_whatsapp` entitlement provisioned; without it, the WhatsApp channel cannot be configured.

**Terminology:**

* Canonical name: WhatsApp channel configuration — Acronym: n/a — variants: channel configuration, WhatsApp configuration
* Synonyms: "Business Account ID" = "Meta Business portfolio ID" = "Business Manager ID"
* Do not confuse: "Business Account ID" (Meta Business portfolio / Business Manager ID) ≠ "WhatsApp Business Account ID" (not entered in this field)
* Do not confuse: "API Credentials" ≠ "Webhook" ≠ "channel configuration" (three distinct setup steps)
* Do not confuse: "Processing" (status while checks run) ≠ "Active" (status once checks are successful and the configuration is ready to deliver)

**FAQ:**

* **Q: What are the steps to configure the WhatsApp channel?** — Create WhatsApp API credentials, create a WhatsApp Webhook, then create a WhatsApp channel configuration.
* **Q: Who can configure the WhatsApp channel?** — A Journey Optimizer System Administrator.
* **Q: How often do Meta tokens expire?** — About every 60 days; renew the token before it lapses.
* **Q: Why are my inbound events missing in some sandboxes?** — Meta allows only one webhook per WhatsApp Business Account, so inbound events are only received in the sandbox where the webhook is registered; register it against your production sandbox.
* **Q: What does the channel configuration status mean?** — It shows Processing while checks run and becomes Active once checks are successful, meaning it is ready to deliver messages.
* **Q: What causes an HTTP 500 error during API credential setup?** — Possible causes include a missing `cjm_whatsapp` entitlement, invalid or mismatched API Token or Business Account ID, or credential handling issues; verify entitlements and fields, test credentials with Meta, enable advanced logging, and contact support if it persists.
* **Q: Why shouldn't I add a '+' before the sender phone number?** — It can prevent the opt-out flow from working correctly.

+++

<!-- ai-section-version: 1 | source-hash: 64f03e21 -->
