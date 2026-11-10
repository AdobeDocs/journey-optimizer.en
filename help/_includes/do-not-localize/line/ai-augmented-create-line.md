---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to send a LINE message from a journey, by adding an Action activity with the LINE channel selected, or from a campaign, and build personalized LINE content, including text, stickers, images, videos, locations, templates, and Flex Messages, by editing the JSON content in the personalization editor.

**Intents:**

* Add an Action activity with the LINE channel to a journey, or create a campaign with the LINE channel
* Choose or create a LINE configuration for the channel
* Define LINE content across the supported message types
* Edit the JSON content and add personalization and dynamic content in the personalization editor
* Preview and simulate the LINE message before sending

**Glossary:**

* **LINE channel**: The channel selected in the Action activity of a journey, or in a campaign, to deliver a LINE message *(product-specific)*
* **Flex Messages**: JSON-based LINE messages that allow complex layouts with rich content *(product-specific)*
* **Stickers**: LINE's native stickers that can be incorporated into a message *(product-specific)*
* **Edit content**: The button used to start designing and configuring the content of the LINE message *(product-specific)*
* **Simulate content**: The option used to preview the LINE message content and its personalized content *(product-specific)*

**Guardrails:**

* LINE message types can be configured by editing the JSON content directly.
* The configuration field is pre-filled, by default, with the last configuration used for that channel by the user.
* The LINE message is sent to the audience once you have performed your tests and validated the content.
* When creating a LINE campaign, the campaign type is either Scheduled - Marketing or API-triggered - Marketing/Transactional.
* In the Action triggers menu, the Frequency of the LINE message can be Once, Daily, Weekly, or Month.

**Terminology:**

* Canonical name: LINE message — Acronym: n/a
* Do not confuse: "Scheduled - Marketing" (executed immediately or on a specified date from the user interface) ≠ "API-triggered - Marketing/Transactional" (executed using an API call)
* Do not confuse: "Edit content" (starts the configuration of the message content) ≠ "Edit code" (edits the JSON content)

**FAQ:**

* **Q: Which message types does LINE support in Journey Optimizer?** — Text, Stickers, Images, Videos, Locations, Templates, and Flex Messages.
* **Q: How is LINE content configured?** — The message types are configured by editing the JSON content directly, and personalization and dynamic content are added in the personalization editor.
* **Q: How can the LINE message be previewed before sending?** — Use Simulate content to preview the LINE message content and its personalized content.
* **Q: Where can the impact of a sent LINE message be measured?** — Within the Campaign or Journey reports.

**Personas:**

* **marketer:** Can add a LINE activity to a journey from the Actions section of the palette, or add a LINE action to a campaign. Can choose or create a LINE configuration, then define content as text, stickers, images, videos, locations, templates, or Flex Messages by editing the JSON content. Can add personalization and dynamic content in the personalization editor, and preview the message with Simulate content. The page states that the configuration field is pre-filled, by default, with the last configuration used for that channel by the user. Where: "Define your LINE content".

**Onboarding:**

* **Level:** Beginner
* **First minimal step:** Open your journey, then drag and drop a LINE activity from the Actions section of the palette.
* **Success check:** The message appears in the preview after you select Save, and Simulate content shows the personalized content.
* **Previous:** Creating your journey before adding a LINE action: Create your first journey (building-journeys/journey-gs.md); Selecting the audience to target before configuring the LINE action in a campaign: About Adobe Experience Platform audiences (audience/about-audiences.md)
* **Next:** Previewing, validating and sending your LINE message: Preview, validate, and send your LINE message (line/send-line.md); Measuring the impact of your sent LINE message in reports: Campaign report (reports/campaign-global-report-cja.md)

+++

<!-- ai-section-version: 1 | source-hash: 0c2aaaed -->
