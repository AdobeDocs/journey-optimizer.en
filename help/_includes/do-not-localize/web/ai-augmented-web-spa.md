---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to author single-page applications in the Journey Optimizer web designer by defining views in the Web SDK implementation, discovering them with [!UICONTROL Browse] mode, and applying modifications to selected views.

**Intents:**

* Author single-page applications (SPAs) in the web designer visual editor
* Define views in the Adobe Experience Platform Web SDK implementation
* Discover views in the web designer using [!UICONTROL Browse] mode
* Apply a modification made in one view to other selected views
* Perform bulk actions on modifications across views

**Glossary:**

* **View**: A whole site or a group of visual elements on a site, such as the home page, the entirety of the products site, or the delivery preferences frame on all the checkout pages *(product-specific)*
* **[!UICONTROL Browse] mode**: A web designer mode used to navigate through the pages of a website to discover its views *(product-specific)*
* **[!UICONTROL Apply to more views]**: A [!UICONTROL More actions] option that applies a selected modification to other selected views *(product-specific)*
* **[!UICONTROL Modifications] pane**: The left-side pane displaying modifications, from which more actions can be taken on each modification *(product-specific)*

**Guardrails:**

* A one-time developer setup is needed to define the views in the Adobe Experience Platform Web SDK implementation before views can be authored.
* If you have not discovered views using [!UICONTROL Browse] mode, you will not be able to select them for applying your modifications.
* Applying a modification to other views requires first adding a modification while in a specific view.

**Terminology:**

* Canonical name: View — Acronym: n/a — variants: SPA view
* Synonyms: "single-page application" = "SPA"
* Do not confuse: "[!UICONTROL Browse] mode" (used to discover and navigate to views) ≠ "[!UICONTROL Apply to more views]" (action that applies a modification to other selected views)

**FAQ:**

* **Q: How do I discover the views of my website?** — Access the web designer, swap to [!UICONTROL Browse] mode, and navigate between the different pages; the view name displayed on top changes as you go through each page.
* **Q: Why can't I select views to apply my modifications to?** — You must first discover the views using [!UICONTROL Browse] mode; otherwise you cannot select them.
* **Q: How do I apply a modification to other views?** — In the [!UICONTROL Modifications] pane, select the modification, click [!UICONTROL More actions], choose [!UICONTROL Apply to more views], select the target views, and click [!UICONTROL Apply].
* **Q: What is the prerequisite for authoring SPAs?** — A one-time developer setup to define the views in the Adobe Experience Platform Web SDK implementation.

+++

<!-- ai-section-version: 1 | source-hash: 946707f6 -->
