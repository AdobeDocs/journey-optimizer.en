---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to add a LINE action to a journey or a campaign and build personalized LINE content, including text, stickers, images, videos, locations, templates, and Flex Messages, by editing the JSON content in the personalization editor.

**Intents:**

* Add a LINE action to a journey or to a campaign
* Choose or create a LINE configuration for the action
* Define LINE content across the supported message types
* Edit the JSON content and add personalization and dynamic content in the personalization editor
* Preview and simulate the LINE message before sending

**Glossary:**

* **LINE action**: The channel action added to a journey or campaign that sends a LINE message to profiles when they reach that step *(product-specific)*
* **Flex Messages**: JSON-based LINE messages that allow complex layouts with rich content *(product-specific)*
* **Stickers**: LINE's native stickers that can be incorporated into a message *(product-specific)*
* **Edit content**: The button used to open the LINE message and configure its content *(product-specific)*
* **Simulate content**: The option used to preview the LINE message content and its personalized content *(product-specific)*

**Guardrails:**

* LINE message types are configured by editing the JSON content directly, using the personalization editor.
* The configuration field is pre-filled, by default, with the last configuration used for that channel by the user.
* Content should be tested and validated with Simulate content before the LINE message is sent to the audience.
* When adding a LINE action to a campaign, the campaign type is either Scheduled - Marketing or API-triggered - Marketing/Transactional.
* For a scheduled campaign, the action trigger frequency can be Once, Daily, Weekly, or Month.

**Terminology:**

* Canonical name: LINE message — Acronym: n/a — variants: LINE action, LINE activity, LINE channel action
* Do not confuse: "Scheduled - Marketing" (executed immediately or on a specified date from the user interface) ≠ "API-triggered - Marketing/Transactional" (executed using an API call)
* Do not confuse: "Edit content" (opens the message to configure its content) ≠ "Edit code" (edits the JSON content)

**FAQ:**

* **Q: Which message types does LINE support in Journey Optimizer?** — Text, Stickers, Images, Videos, Locations, Templates, and Flex Messages.
* **Q: How is LINE content configured?** — The message types are configured by editing the JSON content directly, and personalization and dynamic content are added in the personalization editor.
* **Q: How can the LINE message be previewed before sending?** — Use Simulate content to preview the LINE message content and its personalized content.
* **Q: Where can the impact of a sent LINE message be measured?** — Within the Campaign or Journey reports.

+++

<!-- ai-section-version: 1 | source-hash: 1231f1ca -->
