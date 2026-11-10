---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This overview explains how the direct mail offline channel works, generating personalized extraction files that third-party direct mail providers use to send physical mail to your customers.

**Intents:**

* Understand that direct mail is an offline channel handled by a third-party provider
* Understand how extraction files are generated and sent to a server
* Learn what to configure before creating direct mail messages
* Understand where direct mail messages can be created

**Glossary:**

* **Direct mail**: An offline channel that personalizes and generates the extraction files required by third-party direct mail providers to send mail to your customers *(product-specific)*
* **Extraction file**: The automatically generated file containing all targeted profiles and selected data, such as postal addresses and profile attributes, sent to the server of your choice so that it is accessible by your chosen third-party direct mail provider *(product-specific)*
* **Third-party direct mail provider**: The external provider to which the file is made accessible, who handles the actual mailing process *(product-specific)*

**Guardrails:**

* Before creating direct mail messages, you must configure file routing and a direct mail channel configuration.
* You need audiences and profile data, such as postal addresses, in Adobe Experience Platform.
* Direct mail messages can be created in journeys and campaigns, but they are not available for use in API-triggered campaigns.
* Obtaining any required customer consents is handled with your chosen third-party direct mail provider.
* Use of mailing services is subject to additional terms and conditions from the applicable third-party direct mail provider; Adobe does not control or take responsibility for your use of third-party products.

**Terminology:**

* Canonical name: Direct mail — Acronym: n/a — variants: direct mail channel, direct mail message
* Do not confuse: "Journey Optimizer" (generates the extraction file and sends it to the server of your choice) ≠ "third-party direct mail provider" (handles the actual mailing)

**FAQ:**

* **Q: What is the direct mail channel?** — An offline channel that personalizes and generates extraction files for third-party providers to send physical mail.
* **Q: What do I need before creating direct mail messages?** — File routing and a direct mail channel configuration, plus audiences and profile data such as postal addresses in Adobe Experience Platform.
* **Q: Where can direct mail messages be created?** — In journeys and campaigns; they are not available for use in API-triggered campaigns.
* **Q: Who performs the actual mailing?** — Your chosen third-party direct mail provider, to which the file is made accessible, handles the actual mailing process.

**Personas:**

* **marketer:** Can configure file routing and a direct mail channel configuration before creating direct mail messages. Can create direct mail messages in journeys and campaigns using audiences and profile data, such as postal addresses, from Adobe Experience Platform. The page states that direct mail messages are not available for use in API-triggered campaigns. Where: "Guardrails".

**Onboarding:**

* **Level:** Beginner
* **First minimal step:** Configure file routing and a direct mail channel configuration before creating direct mail messages.
* **Success check:** The extraction file containing targeted profiles and selected data, such as postal addresses, is sent to the server of your choice.
* **Previous:** For file routing and a direct mail channel configuration before creating direct mail messages: Direct mail configuration (direct-mail/direct-mail-configuration.md)
* **Next:** Ready to create direct mail deliveries and configure extraction files for offline channels: Create a direct mail message (direct-mail/create-direct-mail.md); Ready to test, validate, and publish direct mail deliveries: Check & send a direct mail message (direct-mail/test-send-direct-mail.md)

+++

<!-- ai-section-version: 1 | source-hash: b9a90cfd -->
