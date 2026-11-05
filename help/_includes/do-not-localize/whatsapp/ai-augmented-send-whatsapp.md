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

* Errors prevent you from testing or activating the journey, or publishing the campaign, as long as they are not resolved; warnings refer to recommendations and best practices.
* If your campaign is subject to an approval policy, you must request approval before you can send.
* WhatsApp interaction data is stored in the AJO - Email Tracking Experience Event Dataset under the `whatsAppChannelContext` field group.
* To query the dataset, use the `ajo_email_tracking_experience_event_dataset` table in Query Service.

**Terminology:**

* Canonical name: WhatsApp message — Acronym: n/a — variants: WhatsApp
* Do not confuse: "Warnings" (recommendations and best practices) ≠ "Errors" (prevent testing, activating, or publishing as long as they are not resolved)
* Do not confuse: "Simulate content" (test content variations with sample input data or AI auto-generation) ≠ "Simulate content (AEP profiles)" (preview with test profiles)

**FAQ:**

* **Q: How can I preview my WhatsApp message?** — Click Simulate content to test variations with sample input data or AI auto-generation, or select Simulate content (AEP profiles) from the dropdown to preview with test profiles.
* **Q: What is the difference between warnings and errors?** — Warnings refer to recommendations and best practices; errors prevent testing or activating the journey, or publishing the campaign, as long as they are not resolved.
* **Q: How do I send my WhatsApp message?** — Complete the configuration of your journey or campaign; if an approval policy applies, request approval first.
* **Q: Where is WhatsApp interaction data stored?** — In the AJO - Email Tracking Experience Event Dataset, under the `whatsAppChannelContext` field group.
* **Q: How do I query WhatsApp interaction data?** — Use the `ajo_email_tracking_experience_event_dataset` table in Query Service.
* **Q: What can I do with the captured interaction fields?** — Build audiences, run queries, and analyze WhatsApp engagement.

**Personas:**

* **marketer:** Can preview WhatsApp message content using Simulate content or Simulate content (AEP profiles), then check warnings and errors before testing, activating, or publishing. Can complete the journey or campaign configuration to send the message, and analyze interaction data captured under the whatsAppChannelContext field group. The page states that errors prevent testing, activating, or publishing until resolved. Where: "Send your WhatsApp messages".

**Onboarding:**

* **Level:** Beginner
* **First minimal step:** Select Simulate content to preview your WhatsApp message content.
* **Success check:** You can check warnings and errors in the upper section of the editor.
* **Previous:** Learn how to simulate content variations before previewing your message: Simulate content variations (test-approve/simulate-sample-input.md); Learn more about previewing and testing content: Preview and test your content (content-management/preview-test.md)
* **Next:** Request approval before sending if your campaign is subject to an approval policy: Get started with journeys & campaigns approval (test-approve/gs-approval.md); Complete the journey configuration to send the message: Publish the journey (building-journeys/publish-journey.md)

+++

<!-- ai-section-version: 1 | source-hash: ddf62cd4 -->
