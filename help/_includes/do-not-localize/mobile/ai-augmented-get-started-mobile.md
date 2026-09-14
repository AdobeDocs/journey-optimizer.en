---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page introduces mobile messaging in Journey Optimizer across SMS, MMS, and RCS from a single editor, covering use cases, key features, provider support, configuration requirements, and RCS prerequisites.

**Intents:**

* Understand the differences between the SMS, MMS, and RCS channels
* Decide when mobile messaging is or is not the appropriate channel
* Identify the configuration requirements needed before sending Mobile messages
* Identify the prerequisites required to use RCS
* Choose a supported provider for mobile messaging

**Glossary:**

* **SMS (Short Message Service)**: Text-only messages of up to 160 characters, supported across all mobile devices *(product-specific)*
* **MMS (Multimedia Message Service)**: Messages enriched with images, videos, audio clips, and GIFs, plus up to 1,600 characters of text *(product-specific)*
* **RCS (Rich Communication Services)**: Branded, interactive content delivered directly in the customer's native messaging app with no additional app download required *(product-specific)*
* **Channel configuration**: A configuration set up for marketing and transactional messages before sending *(product-specific)*
* **Fallback SMS**: A standard SMS delivered when a recipient's device does not support RCS *(product-specific)*

**Guardrails:**

* SMS sends text-only messages of up to 160 characters.
* MMS supports up to 1,600 characters of text.
* Native RCS authoring requires Sinch RCS (Adobe resell or direct); Twilio, Infobip, and other providers must use a custom provider integration.
* Fallback SMS is strongly recommended, because recipients whose devices do not support RCS will not receive the message unless SMS fallback is available.
* Subdomain configuration is required only if you plan to use URL shortening.
* Built-in handling of standard opt-out keywords (STOP, QUIT, CANCEL, etc.) is available for Sinch and Infobip.
* RCS delivery is supported on Android and iOS devices; carrier and regional availability varies and RCS is not universally available globally.
* Configuration steps are typically performed by a System Administrator.

**Terminology:**

* Canonical name: Mobile messages — Acronym: n/a — variants: mobile messaging, SMS/MMS/RCS messages
* Synonyms: "mobile message" = "SMS/MMS/RCS message"
* Do not confuse: "native RCS authoring" (requires Sinch RCS) ≠ "RCS via custom provider integration" (used by Twilio, Infobip, and other providers)

**FAQ:**

* **Q: Is native RCS messaging available with Twilio or Infobip?** — No; the native RCS designer is not available with third-party providers such as Twilio or Infobip, but RCS can be sent via a custom provider integration.
* **Q: Is native RCS messaging available for Sinch direct customers?** — Yes; customers using Sinch's Conversational API have access to native RCS authoring, including both Adobe resell and Sinch direct customers.
* **Q: Why purchase SMS alongside RCS?** — SMS volume and a short code enable SMS fallback, the recommended path, because profiles whose device or carrier does not support RCS will not receive the message at all if SMS is not configured.
* **Q: Is RCS available everywhere?** — No; RCS is not universally supported across all carriers and regions, so regional availability and carrier support should be researched when planning RCS campaigns.
* **Q: What are the character limits for an RCS message?** — Rich Media (Single) message types support up to 3,072 characters, and Basic RCS message types are limited to 160 characters.

+++

<!-- ai-section-version: 1 | source-hash: 827bad9f -->
