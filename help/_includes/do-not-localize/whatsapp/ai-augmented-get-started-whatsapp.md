---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page introduces the WhatsApp channel in Journey Optimizer, delivered through Meta's Cloud API, covering how it works in journeys and campaigns along with its use cases, prerequisites, and limitations.

**Intents:**

* Understand how the WhatsApp channel works in Journey Optimizer via Meta's Cloud API
* Decide whether to add a WhatsApp activity to a journey or select WhatsApp as a campaign action
* Evaluate WhatsApp use cases and situations when not to use the channel
* Identify the prerequisites needed to integrate WhatsApp with Journey Optimizer
* Understand the limitations that apply to the WhatsApp channel

**Glossary:**

* **WhatsApp channel**: The Journey Optimizer channel that sends WhatsApp messages directly through Meta's Cloud API *(product-specific)*
* **Cloud API**: Meta's API through which Journey Optimizer sends WhatsApp messages *(product-specific)*
* **WhatsApp Flow template**: A template type that builds guided, multi-step interactions within the chat, such as surveys and lead capture forms *(product-specific)*
* **WhatsApp Business Account**: A Meta business account with a verified sender name and phone number, required to integrate WhatsApp *(product-specific)*

**Guardrails:**

* Prerequisites: a Meta Business Manager account, a WhatsApp Business Account with verified sender name and phone number, a user authorization token with appropriate permissions, and approved Meta templates.
* You must acknowledge WhatsApp content rules, compliance with Meta policies, and 24 Hour conversation limits before proceeding with integration.
* The WhatsApp channel is HIPAA-ready, but third-party vendors are not covered under Adobe's BAA; customers are responsible for their own compliance and vendor validation.
* Automated or predefined response messages are not yet supported.
* Starting April 2025, delivery of all marketing template messages to WhatsApp users with a United States phone number (a +1 dialing code and a US area code) has been temporarily suspended.
* The native integration does not allow integration with third-party Business Service Provider (BSP).
* Explicit recipient opt-in is required by Meta's messaging policies.

**Terminology:**

* Canonical name: WhatsApp channel — Acronym: n/a — variants: WhatsApp, WhatsApp activity, WhatsApp action
* Synonyms: "WhatsApp activity" (in a Journey) = "WhatsApp action" (in a Campaign)
* Do not confuse: "Journey" (add a WhatsApp activity) ≠ "Campaign" (select WhatsApp as an action)
* Do not confuse: "BSP" (Business Service Provider) ≠ "Cloud API" (Meta's native integration used by Journey Optimizer)

**FAQ:**

* **Q: How does Journey Optimizer send WhatsApp messages?** — Directly through Meta's Cloud API, integrating WhatsApp into journeys and campaigns.
* **Q: What do I need before integrating WhatsApp?** — A Meta Business Manager account, a WhatsApp Business Account with verified sender name and phone number, a user authorization token with appropriate permissions, and approved Meta templates.
* **Q: Can I reach US phone numbers with marketing templates?** — Starting April 2025, delivery of all marketing template messages to WhatsApp users with a US phone number (+1 dialing code and US area code) has been temporarily suspended.
* **Q: Is the WhatsApp channel HIPAA-compliant?** — It is HIPAA-ready, but third-party vendors are not covered under Adobe's BAA, and customers are responsible for their own compliance and vendor validation.
* **Q: Can I use a third-party BSP with this integration?** — No, the native integration does not allow integration with third-party Business Service Providers.
* **Q: When should I not use WhatsApp?** — When your audience does not use it, recipients have not opted in, the message is urgent and needs guaranteed delivery, the content is lengthy or complex, or real-time conversational support is not feasible.

+++

<!-- ai-section-version: 1 | source-hash: 49f32f6b -->
