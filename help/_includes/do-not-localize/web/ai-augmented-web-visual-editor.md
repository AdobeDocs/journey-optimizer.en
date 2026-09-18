---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to author a web experience with the Journey Optimizer visual web designer, including selecting and editing elements, adding components and personalization, navigating the canvas, and changing the device size.

**Intents:**

* Open the web designer from the [!UICONTROL Edit content] screen to author a web experience
* Select and edit elements on the canvas using the contextual menu, right panel icons, and dynamic right panel
* Add and edit components such as Divider, HTML, Image, Heading, Paragraph, and Link
* Add personalization to a container using the personalization editor
* Navigate the designer with breadcrumbs and [!UICONTROL Browse] mode
* Change the device size and zoom focus of the designer display

**Glossary:**

* **Web designer**: The Journey Optimizer visual web authoring editor, powered by the Adobe Experience Cloud Visual Helper Chrome browser extension *(product-specific)*
* **[!UICONTROL Design] mode**: The default web designer mode for performing changes on a page *(product-specific)*
* **[!UICONTROL Browse] mode**: A mode used to navigate to the exact page from the selected configuration you want to personalize, useful for pages behind authentication or not available at a certain URL from the start *(product-specific)*
* **Breadcrumbs**: A control that displays information about the selected element and lets you navigate to any parent, sibling, or child element within the visual editor *(product-specific)*
* **Non-visual edition mode**: An alternative editing mode used by unselecting the [!UICONTROL Visual editor] option to edit web content without loading the visual editor *(product-specific)*

**Guardrails:**

* Visual web authoring is powered by the Adobe Experience Cloud Visual Helper Chrome browser extension, and the prerequisites must be followed to access and author web pages.
* The Adobe Experience Platform Web SDK must be included in your web page.
* If a website fails to load, a message suggests installing the Visual Editing Helper browser extension.
* Changes made at a specific device size apply to all sizes and devices as long as the selectors are the same; editing in normal desktop view also applies to all screen sizes.
* [!DNL Journey Optimizer] does not currently support device size-specific page changes; changes for a separate mobile website with a separate structure should be made in a different campaign.
* The zoom focus can be changed from 25% to 400%.

**Terminology:**

* Canonical name: Web designer — Acronym: n/a — variants: visual web designer, web content designer, visual editor
* Synonyms: "web designer" = "visual web designer"
* Do not confuse: "[!UICONTROL Design] mode" (default mode for performing changes) ≠ "[!UICONTROL Browse] mode" (navigate to the exact page to personalize)

**FAQ:**

* **Q: How do I open the web designer?** — From the [!UICONTROL Edit content] screen, click [!UICONTROL Edit web page].
* **Q: Can I edit web content without the visual editor?** — Yes; unselect the [!UICONTROL Visual editor] option to use the non-visual edition mode instead.
* **Q: What components can I add to a web page?** — Divider, HTML, Image, Heading, Paragraph, and Link.
* **Q: Do device-size changes apply only to that device?** — No; as long as the selectors are the same, changes apply to all sizes and devices. Journey Optimizer does not currently support device size-specific page changes.
* **Q: When should I use [!UICONTROL Browse] mode?** — When dealing with pages behind authentication or not available at a certain URL from the start, and to navigate through all the views of a website when authoring single-page applications.

+++

<!-- ai-section-version: 1 | source-hash: 77a05b9e -->
