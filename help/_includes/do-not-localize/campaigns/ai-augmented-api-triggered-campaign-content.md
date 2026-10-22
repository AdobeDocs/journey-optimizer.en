---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to design the content of an API triggered campaign, personalize it with contextual data passed in the API payload, attach personalized PDF files, and preview it with **Simulate content**.

**Intents:**

* Open the message content configuration from the **Content** tab or the **Edit content** button
* Personalize a message with contextual data from the API payload
* Attach personalized PDF files to transactional API-triggered email campaigns
* Preview and test the content with **Simulate content**

**Glossary:**

* **Contextual data**: Additional data passed into the API payload and used to personalize the message, referenced with the `{{context.<contextualAttribute>}}` syntax, where `<contextualAttribute>` matches the name of the variable in the API payload *(product-specific)*
* **High Throughput campaigns**: A mode that does not rely on Adobe profiles; all personalization must be included in the API payload as context data *(product-specific)*
* **Simulate content**: Button used to preview and test content with sample input data or AI auto-generation
* **Simulate content (AEP profiles)**: Option selected from the **Simulate content** dropdown to preview with test profiles

**Guardrails:**

* The contextual attributes passed into the request cannot exceed 200kb (hard limit) and are always considered of type string.
* The `context.system` syntax is restricted to Adobe internal usage only and should not be used to pass contextual attributes.
* Contextual data passed in the REST API is used for one-off communication and is not stored against profile. At maximum, a profile is created with the namespace details, if it was found missing.
* Using a large number or heavy contextual data in your content may impact performances.
* For now, no contextual attribute is available for use in the left rail menu. Attributes must be typed directly in the personalization expression, with no check performed by Journey Optimizer.
* A transactional API-triggered email campaign can include up to five PDF attachments in an email, including both static and personalized attachments.

**Applicability:**

* Design content: Email, Mobile message, Push notification
* Personalized PDF attachments: transactional API-triggered email campaigns
* High Throughput campaigns: email channel only, US region only

**Terminology:**

* Canonical name: API triggered campaign content
* Do not confuse: "contextual data passed in the REST API" (one-off, not stored against profile) ≠ "profile-enabled events"
* Do not confuse: **Simulate content** (sample input data or AI auto-generation) ≠ **Simulate content (AEP profiles)** (test profiles)

**FAQ:**

* **Q: How do I use data from the API payload in a message?** — Pass the data into the API payload and add it in the message with the personalization editor, using `{{context.<contextualAttribute>}}`.
* **Q: Can contextual attributes be picked from the left rail menu?** — No. No contextual attribute is available there; attributes must be typed directly in the personalization expression.
* **Q: What is the size limit for contextual attributes?** — They cannot exceed 200kb and are always considered of type string.
* **Q: Is contextual data stored against the profile?** — No. It is used for one-off communication and not stored against profile. At maximum, a profile is created with the namespace details, if it was found missing.
* **Q: How many PDF attachments can an email include?** — For transactional API-triggered email campaigns, up to five, static and personalized attachments included.
* **Q: How do I preview content?** — Click **Simulate content** to test with sample input data or AI auto-generation, or select **Simulate content (AEP profiles)** from the dropdown to preview with test profiles.

**Examples:**

* A customer wants to reset a password. A password reset URL is generated in a third-party tool, passed into the API payload, and added to the message with `{{context.<contextualAttribute>}}`.

**Related pages:**

* Creating email content: Email (email/create-email.md)
* Creating mobile message content: Mobile message (mobile/create-mobile-message.md)
* Creating push notification content: Push notification (push/create-push.md)
* High Throughput campaigns: High Throughput campaigns (campaigns/api-triggered-high-throughput.md)
* Personalized PDF attachments: Learn how to attach personalized PDF files (email/pdf-attachments.md#personalized-attachments)
* Previewing and testing content: Learn how to preview and test content (content-management/preview-test.md)
* Next step, defining the audience: Learn more (campaigns/api-triggered-campaign-audience.md)

+++

<!-- ai-section-version: 1 | source-hash: 45115869 -->
