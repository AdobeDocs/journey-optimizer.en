---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to edit web content with the Journey Optimizer web designer, including adding components, personalization, navigating with breadcrumbs and browse mode, and adjusting the device size.

**Intents:**

* Open the web designer from the Action tab or web experience activity and start authoring a page
* Edit elements using the contextual menu, right panel icons, and the dynamic right panel
* Add components such as Divider, HTML, Image, Heading, Paragraph, and Link
* Add personalization to a container using the personalization editor
* Navigate the page with breadcrumbs and switch between Design and Browse modes
* Change the device size and zoom focus of the web designer display

**Glossary:**

* **Web designer**: The visual editor in Journey Optimizer used to author web experiences, powered by the Adobe Experience Cloud Visual Helper chrome browser extension *(product-specific)*
* **Breadcrumbs**: A control (Expand/Collapse Breadcrumbs) that displays information about the selected element and lets you navigate to any parent, sibling, or child element *(product-specific)*
* **Design mode**: The default web designer mode used to make changes to the page *(product-specific)*
* **Browse mode**: A mode you can swap to in order to navigate to the exact page from the selected configuration you want to personalize, useful for pages behind authentication or single-page applications *(product-specific)*
* **Visual Editing Helper browser extension**: The browser extension suggested when a website fails to load in the web designer *(product-specific)*

**Guardrails:**

* To access and author web pages in the Journey Optimizer user interface, you must follow the web prerequisites.
* The web page must include the Adobe Experience Platform Web SDK.
* If you created a pages matching rule, you must enter any URL matching that rule; the changes are then applied to all pages matching the rule.
* Editing a web experience in a specific device size (or in the normal desktop view) applies the changes to all sizes and devices, not just the device size you are working in, as long as the selectors are the same.
* Journey Optimizer does not support device size-specific page changes; for a separate mobile website with a separate site structure, make the mobile-specific changes in a different campaign.
* The zoom focus can be changed from 25% to 400%.

**Terminology:**

* Canonical name: web designer — Acronym: n/a — variants: web content designer, visual editor
* Synonyms: "Adobe Experience Cloud Visual Helper" = "Visual Editing Helper browser extension"
* Do not confuse: "Design" mode (default mode for making changes) ≠ "Browse" mode (mode for navigating to the exact page to personalize)
* Do not confuse: "Heading" and "Paragraph" components (each similar to using the Text component in the Email Designer) ≠ "Text" component (the Email Designer component they are compared to)

**FAQ:**

* **Q: What powers web authoring in Journey Optimizer?** — Web authoring is powered by the Adobe Experience Cloud Visual Helper chrome browser extension, and the page must include the Adobe Experience Platform Web SDK.
* **Q: Which components can I add to a web page?** — Divider, HTML, Image, Heading, Paragraph, and Link, inserted with the Insert before or Insert after buttons.
* **Q: How do I add personalization?** — Select a container, choose the personalization icon from the contextual menu bar, and add your changes using the personalization editor.
* **Q: When should I use Browse mode?** — When you need to reach pages behind authentication or not available at a starting URL, or to navigate through all views when authoring single-page applications.
* **Q: Do device-size edits apply only to that device?** — No; as long as the selectors are the same, changes apply to all sizes and devices, and device size-specific page changes are not supported.

+++

<!-- ai-section-version: 1 | source-hash: 920b1eca -->
