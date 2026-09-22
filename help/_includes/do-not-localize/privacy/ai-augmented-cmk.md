---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to set up and manage Azure customer managed keys (CMK) so you can encrypt your Adobe Journey Optimizer data with your own keys and keep it protected in transit and at rest.

**Intents:**

* Understand what customer managed keys (CMK) provide in Journey Optimizer
* Learn the two-part setup process across Adobe Experience Platform and Customer Journey Analytics
* Understand which add-on offerings are required to use CMK
* Understand how data is encrypted in transit and at rest

**Glossary:**

* **[!DNL Customer Managed Keys] (CMK)**: Azure customer managed keys that Healthcare Shield and Privacy & Security Shield customers can leverage and apply to their data to encrypt Adobe Journey Optimizer data with their own keys *(product-specific)*
* **Healthcare Shield**: add-on offering whose purchase enables the Customer Managed Keys functionality *(product-specific)*
* **Privacy & Security Shield**: add-on offering whose purchase enables the Customer Managed Keys functionality *(product-specific)*
* **Customer Journey Analytics (CJA)**: certain components are used in the background during CMK setup, so the CJA portion of the setup must be completed even if CJA has not been purchased *(product-specific)*

**Guardrails:**

* [!DNL Customer Managed Keys] functionality is currently available only for organizations that have purchased the Healthcare Shield or Privacy & Security Shield add-on offering (availability constraint)
* The setup process involves two parts, leveraging technology from both Adobe Experience Platform and Customer Journey Analytics (CJA)
* Completing the Customer Journey Analytics portion of the setup is necessary even if CJA has not been purchased, because certain CJA components are used in the background
* Data is encrypted in transit and at rest, and remains protected regardless of whether Customer Managed Keys are used

**Terminology:**

* Canonical name: Customer Managed Keys — Acronym: CMK — variants: customer managed keys, Azure Customer Managed Keys
* Do not confuse: "Healthcare Shield" ≠ "Privacy & Security Shield" (two distinct add-on offerings that each enable the CMK functionality)

**FAQ:**

* **Q: Who can use Customer Managed Keys?** — Organizations that have purchased the Healthcare Shield or Privacy & Security Shield add-on offering.
* **Q: Do you need to complete the Customer Journey Analytics setup even without purchasing CJA?** — Yes, because certain CJA components are used in the background.
* **Q: Is data encrypted even if you do not use CMK?** — Yes, both Adobe Experience Platform and Customer Managed Keys encrypt data in transit and at rest, and data remains protected regardless of whether CMK is used.
* **Q: What are the two parts of the setup?** — One part in Adobe Experience Platform and one part in Customer Journey Analytics.

+++

<!-- ai-section-version: 1 | source-hash: 7c08224c -->
