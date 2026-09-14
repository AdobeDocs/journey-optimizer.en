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
* **Extraction file**: The automatically generated file containing all targeted profiles and selected data, such as postal addresses and profile attributes, sent to a server for the provider to retrieve *(product-specific)*
* **Third-party direct mail provider**: The external provider that retrieves the exported file and handles the actual mailing process *(product-specific)*

**Guardrails:**

* Before creating direct mail messages, you must configure file routing and a direct mail channel configuration.
* You need audiences and profile data, such as postal addresses, in Adobe Experience Platform.
* Direct mail messages can be created in journeys and campaigns, but they are not available for use in API-triggered campaigns.
* Obtaining any required customer consents is handled with your chosen third-party direct mail provider.
* Use of mailing services is subject to additional terms and conditions from the applicable third-party direct mail provider; Adobe does not control or take responsibility for your use of third-party products.

**Terminology:**

* Canonical name: Direct mail — Acronym: n/a — variants: direct mail channel, direct mail message
* Synonyms: "extraction file" = "export file"
* Do not confuse: "Journey Optimizer" (generates and exports the extraction file) ≠ "third-party direct mail provider" (handles the actual mailing)

**FAQ:**

* **Q: What is the direct mail channel?** — An offline channel that personalizes and generates extraction files for third-party providers to send physical mail.
* **Q: What do I need before creating direct mail messages?** — File routing and a direct mail channel configuration, plus audiences and profile data such as postal addresses in Adobe Experience Platform.
* **Q: Where can direct mail messages be created?** — In journeys and campaigns; they are not available for use in API-triggered campaigns.
* **Q: Who performs the actual mailing?** — Your chosen third-party direct mail provider retrieves the exported file and handles the mailing process.

+++

<!-- ai-section-version: 1 | source-hash: 02e80fb2 -->
