---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how developers implement XDM views in single-page applications (SPAs) using the Adobe Experience Platform Web SDK so marketers can run personalization and experimentation on those views through the Journey Optimizer web visual editor.

**Intents:**

* Understand how XDM views represent SPA experiences instead of URLs
* Perform the one-time developer setup to implement XDM views
* Deliver content to views using `sendEvent()` with `renderDecisions` set to `true`
* Pass the XDM view name in `xdm.web.webPageDetails.viewName`
* Invoke `sendEvent()` in React for view changes in an SPA

**Glossary:**

* **Single-page application (SPA)**: A modern web application that uses browser UI rendering often independent of page reloads, triggered by interactions such as scrolls, clicks, and cursor movements *(product-specific)*
* **View**: A logical group of visual elements which together make up an SPA experience; can represent a whole site, a single page, or grouped visual elements within a page *(product-specific)*
* **XDM view**: A view that can be leveraged in Adobe Journey Optimizer to run web personalization and experimentation campaigns on SPAs via the web visual editor *(product-specific)*
* **`viewName`**: The XDM field (`xdm.web.webPageDetails.viewName`) that carries the view being rendered *(product-specific)*

**Guardrails:**

* Implementing XDM views requires a one-time developer setup performed in order: install the Adobe Experience Platform Web SDK, check the web channel prerequisites, determine all XDM views to personalize, and implement `sendEvent()` with `renderDecisions` set to `true` and the corresponding XDM view.
* The XDM view must be passed in `xdm.web.webPageDetails.viewName`.
* A view name cannot be empty.
* On the first `sendEvent()` call, all XDM views that should be rendered are fetched and cached; subsequent `sendEvent()` calls with XDM views passed in are read from the cache and rendered without a server call.

**Terminology:**

* Canonical name: XDM view — Acronym: n/a — variants: view, viewName
* Synonyms: "single-page application" = "SPA"
* Do not confuse: "multi-page application" (page-to-page navigation requiring a page load) ≠ "single-page application" (browser UI rendering independent of page reloads)

**FAQ:**

* **Q: What is a view in the context of SPAs?** — A logical group of visual elements that make up an SPA experience; it can be a whole site, a single page, or grouped elements within a page.
* **Q: Where is the view name passed?** — In `xdm.web.webPageDetails.viewName` within the `sendEvent()` call.
* **Q: Does every view change trigger a server call?** — No; the first `sendEvent()` call fetches and caches all views to be rendered, and subsequent calls with views passed in are served from the cache without a server call.
* **Q: What enables marketers to discover views in the web editor?** — Implementing `sendEvent()` with `renderDecisions` set to `true` and the corresponding XDM view allows marketers to discover the views inside the Journey Optimizer web editor.

+++

<!-- ai-section-version: 1 | source-hash: 1a47a92c -->
