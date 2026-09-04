---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how the Adobe Experience Platform Web SDK delivers and renders personalized Adobe Journey Optimizer content to web surfaces, covering how to enable Journey Optimizer, render propositions, and debug the implementation.

**Intents:**

* Enable [!DNL Adobe Journey Optimizer] delivery through the [!DNL Experience Platform Web SDK]
* Render Journey Optimizer content propositions automatically on web page surfaces
* Specify additional web surfaces in `sendEvent` requests
* Add a prehiding snippet to hide portions of the page while fetching experiences
* Debug Journey Optimizer personalization implementations

**Glossary:**

* **Surface**: A web page or location on a page identified by a URI where the [!DNL Adobe Journey Optimizer] experience content will be delivered *(product-specific)*
* **Proposition**: In [!DNL Adobe Journey Optimizer], correlates to the experience selected from a [!DNL Journey Optimizer Campaign] *(product-specific)*
* **`renderDecisions`**: A `sendEvent` option that, when set to `true`, automatically renders delivered Journey Optimizer content propositions on web page surfaces *(product-specific)*
* **Prehiding snippet**: A snippet used to hide only certain portions of the page while fetching experiences *(product-specific)*

**Guardrails:**

* Prerequisites must be completed: set up [!DNL Adobe Experience Cloud Visual Editing Helper], enable [!DNL Adobe Journey Optimizer] in your datastream, and enable the [!UICONTROL Active-On-Edge Merge Policy] option.
* Automatic rendering of propositions requires `renderDecisions` to be set to `true` in the `sendEvent` command.
* By default the Web SDK automatically generates the web surface for the current web page; additional surfaces must be specified in the `personalization.surfaces` option or the [!UICONTROL Surfaces] Send event action configuration.
* Journey Optimizer debug traces are available through [!DNL Adobe Experience Platform Assurance]; check for events with the `AJO:` prefix.

**Terminology:**

* Canonical name: Surface — Acronym: n/a — variants: web surface
* Synonyms: "propositions" = "experience selected from a Journey Optimizer Campaign"
* Do not confuse: "Surface" (URI location where content is delivered) ≠ "Proposition" (the experience content selected for delivery)

**FAQ:**

* **Q: How do I turn on automatic rendering of Journey Optimizer content?** — Set the `renderDecisions` option to `true` in the `sendEvent` command.
* **Q: Do I have to declare the web surface for the current page?** — No; by default the Web SDK automatically generates the web surface for the current web page. You only specify additional surfaces via `personalization.surfaces`.
* **Q: How are Journey Optimizer web propositions rendered?** — They are processed similar to `__view__` decision scope propositions and, when `renderDecisions` is `true`, are automatically rendered by the Web SDK.
* **Q: How do I debug the implementation?** — Use Web SDK debugging and [!DNL Adobe Experience Platform Assurance], checking for events with the `AJO:` prefix.

+++

<!-- ai-section-version: 1 | source-hash: 0897546d -->
