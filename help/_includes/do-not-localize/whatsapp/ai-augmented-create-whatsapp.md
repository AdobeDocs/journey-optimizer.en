---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to create a WhatsApp message in Journey Optimizer by adding a WhatsApp action to a journey or campaign, building content from a Meta-approved template, adding media and personalization, and previewing it with Simulate content.

**Intents:**

* Add a WhatsApp action to a journey or a campaign
* Choose a Template category (Marketing, Utility, or Authentication) and select a Meta-approved WhatsApp template
* Add media URLs to replace template placeholders and personalize the template content
* Configure call-to-action and quick reply buttons supported by WhatsApp
* Preview WhatsApp content, shortened URLs, and personalization with Simulate content
* Track clicks and supported WhatsApp button interactions in campaign reporting

**Glossary:**

* **WhatsApp action**: A channel action added to a journey or campaign that sends a WhatsApp message to profiles when they reach that step *(product-specific)*
* **WhatsApp template**: A message template created and designed in Meta that must be approved by Meta before it can be selected in Journey Optimizer *(product-specific)*
* **Template category**: The classification of a WhatsApp template — Marketing, Utility, or Authentication *(product-specific)*
* **WhatsApp Flow template**: A template type that delivers interactive multi-screen experiences such as surveys or lead capture forms within the WhatsApp conversation *(product-specific)*
* **Simulate content**: The option used to preview WhatsApp message content, shortened URLs, and personalized content *(product-specific)*
* **Image URL field**: The field where external media URLs (from Adobe Experience Manager or other sources) are added to replace placeholder media in the template *(product-specific)*

**Guardrails:**

* Only Outbound messages elements are supported in Journey Optimizer.
* **Copy code** interactive buttons are not supported, and their interactions are not tracked.
* For **Visit website** / **Call to action – URL**, only one URL button is permitted, with variable parameters included.
* Images must be JPEG or PNG in 8-bit RGB or RGBA format and under 5 MB.
* Videos must be 3GPP or MP4, under 16 MB, and hosted via URL.
* Audio is only available for response messages; must be AAC, AMR, MP3, MP4 audio, or OGG, hosted on a URL, and under 16 MB.
* Documents must be under 100 MB, hosted on a URL, and in .txt, .xls/.xlsx, .doc/.docx, .ppt/.pptx, or .pdf format.
* A WhatsApp template must first be designed in Meta and approved by Meta before use; approval usually takes a few hours but may take up to 24 hours.
* Meta's template media are only placeholders; to display images, audio, or video you must provide external URLs (from Adobe Experience Manager or other sources).
* For campaigns, only the **Scheduled - Marketing** campaign type is described, with Frequency options of Once, Daily, Weekly, or Month.
* All inbound WhatsApp responses, including those submitted through WhatsApp Flow templates, are captured in the AJO Channel Tracking Event Dataset.

**Terminology:**

* Canonical name: WhatsApp action — Acronym: n/a — variants: WhatsApp activity, WhatsApp channel action
* Synonyms: "Visit website" = "Call to action – URL"
* Do not confuse: "Quick reply" (short preset tappable replies) ≠ "Call to action" buttons (Visit website, Call on WhatsApp, Call phone number)
* Do not confuse: "Call on WhatsApp" (opens a WhatsApp chat with the specified number) ≠ "Call phone number" (initiates a phone call to the number)
* Do not confuse: "Marketing" ≠ "Utility" ≠ "Authentication" (Template categories)

**FAQ:**

* **Q: How do I create a WhatsApp message?** — Add a WhatsApp action to a journey or campaign, then use the Edit content button to choose a Template category, select a Meta-approved WhatsApp template, add media URLs, and personalize it.
* **Q: Do I create the WhatsApp template in Journey Optimizer?** — No. You first create and design your template in Meta, and it must be approved by Meta before you can select it in Journey Optimizer.
* **Q: How long does Meta template approval take?** — It usually takes a few hours but may take up to 24 hours.
* **Q: Why don't my template's images or videos display?** — Meta's template media are only placeholders; you must supply external URLs (from Adobe Experience Manager or other sources) in the Image URL field.
* **Q: How can I preview my WhatsApp message?** — Use Simulate content to preview the message content, shortened URLs, and personalized content.
* **Q: Which button interactions are tracked in reporting?** — Interactions on Quick reply, Call to action – URL, and Call to action – phone are tracked; Copy code buttons are not supported and are not tracked.

+++

<!-- ai-section-version: 1 | source-hash: abd76bc6 -->
