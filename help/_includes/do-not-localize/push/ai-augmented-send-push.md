---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to preview, validate, and send a push notification in Journey Optimizer, including the simulation methods, the warnings and errors that can block sending, and approval requirements.

**Intents:**

* Preview push notification content using the available simulation methods
* Preview content per device type (iOS, Android, or Web)
* Check and resolve alerts (warnings and errors) before sending
* Understand which errors block testing or activation
* Send the push notification by completing the journey or campaign configuration

**Glossary:**

* **Simulate content**: The option to test content variations with sample input data or AI auto-generation *(product-specific)*
* **Simulate content (AEP profiles)**: The option, selected from the Simulate content dropdown, to preview with test profiles and select the device type (iOS, Android, or Web) *(product-specific)*
* **Warnings**: Alerts that refer to recommendations and best practices *(product-specific)*
* **Errors**: Alerts that prevent you from testing or activating the journey as long as they are not resolved *(product-specific)*

**Guardrails:**

* Errors prevent you from testing or activating the journey until resolved; warnings refer to recommendations and best practices and do not block.
* The push notification size cannot exceed 4KB (hard limit); the "Push iOS/Android payload has exceeded limit of 4KB" error appears when it does — reduce the use of images or emojis to respect the limit.
* "The push version of the message is empty" error appears when the push notification body or title is missing.
* "configuration doesn't exist" error occurs when the selected configuration is deleted after message creation; select another configuration in the message Properties.
* For better deliverability, use phone numbers in formats supported by the provider (for example, Twilio and Sinch only support E.164 format).
* If your campaign is subject to an approval policy, you must request approval before you can send the push notification.

**Terminology:**

* Canonical name: Check & send your push notification — Acronym: n/a — variants: preview push, validate push, send push
* Synonyms: "Simulate content (AEP profiles)" = preview with test profiles
* Do not confuse: "Warnings" (recommendations and best practices; do not block) ≠ "Errors" (prevent testing or activating until resolved)
* Do not confuse: "Simulate content" (test content variations with sample input data or AI auto-generation) ≠ "Simulate content (AEP profiles)" (preview with test profiles by device type)

**FAQ:**

* **Q: How can I preview my push notification?** — Use Simulate content to test variations with sample input data or AI auto-generation, or select Simulate content (AEP profiles) to preview with test profiles by device type (iOS, Android, or Web).
* **Q: What is the push payload size limit?** — The push notification size cannot exceed 4KB; reduce the use of images or emojis to respect it.
* **Q: What stops me from sending my message?** — Unresolved errors, such as an empty push version, a deleted configuration, or a payload exceeding 4KB, prevent testing or activation; warnings do not block.
* **Q: What if my selected configuration was deleted?** — The "configuration doesn't exist" error appears; select another configuration in the message Properties.
* **Q: Do I need approval to send?** — If your campaign is subject to an approval policy, you must request approval before sending the push notification.

+++

<!-- ai-section-version: 1 | source-hash: a49e5ec3 -->
