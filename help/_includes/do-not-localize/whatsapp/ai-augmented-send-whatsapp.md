---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to preview, validate, and send a WhatsApp message in Journey Optimizer, and how to analyze the WhatsApp interaction data captured in the tracking dataset.

**Intents:**

* Preview WhatsApp message content using Simulate content or Simulate content (AEP profiles)
* Check warnings and errors before testing, activating, or publishing
* Complete the journey or campaign configuration to send the WhatsApp message
* Analyze WhatsApp interaction data returned from the channel
* Build audiences and run queries on captured WhatsApp engagement fields

**Glossary:**

* **Simulate content**: The option used to test content variations with sample input data or AI auto-generation *(product-specific)*
* **Simulate content (AEP profiles)**: An option selected from the Simulate content dropdown to preview with test profiles *(product-specific)*
* **Warnings**: Alerts that refer to recommendations and best practices; for example, shown if your text message is empty *(product-specific)*
* **Errors**: Alerts that prevent testing or activating the journey, or publishing the campaign, until resolved; for example, a missing subject line *(product-specific)*
* **whatsAppChannelContext**: The field group under which WhatsApp interaction data is stored in the AJO - Email Tracking Experience Event Dataset *(product-specific)*

**Guardrails:**

* Errors prevent you from testing or activating the journey, or publishing the campaign, until they are resolved; warnings do not block.
* If your campaign is subject to an approval policy, you must request approval before you can send.
* WhatsApp interaction data is stored in the AJO - Email Tracking Experience Event Dataset under the `whatsAppChannelContext` field group.
* To query the dataset, use the `ajo_email_tracking_experience_event_dataset` table in Query Service.

**Terminology:**

* Canonical name: WhatsApp message — Acronym: n/a — variants: WhatsApp
* Synonyms: "Simulate content (AEP profiles)" = "preview with test profiles"
* Do not confuse: "Warnings" (recommendations/best practices; do not block) ≠ "Errors" (block testing, activation, or publishing until resolved)
* Do not confuse: "Simulate content" (test content variations with sample input data or AI auto-generation) ≠ "Simulate content (AEP profiles)" (preview with test profiles)

**FAQ:**

* **Q: How can I preview my WhatsApp message?** — Click Simulate content to test variations with sample input data or AI auto-generation, or select Simulate content (AEP profiles) from the dropdown to preview with test profiles.
* **Q: What is the difference between warnings and errors?** — Warnings are recommendations and best practices and do not block; errors prevent testing or activating the journey, or publishing the campaign, until resolved.
* **Q: How do I send my WhatsApp message?** — Complete the configuration of your journey or campaign; if an approval policy applies, request approval first.
* **Q: Where is WhatsApp interaction data stored?** — In the AJO - Email Tracking Experience Event Dataset, under the `whatsAppChannelContext` field group.
* **Q: How do I query WhatsApp interaction data?** — Use the `ajo_email_tracking_experience_event_dataset` table in Query Service.
* **Q: What can I do with the captured interaction fields?** — Build audiences, run queries, and analyze WhatsApp engagement.

+++

<!-- ai-section-version: 1 | source-hash: 19298f05 -->
