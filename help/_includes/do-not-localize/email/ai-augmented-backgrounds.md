---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to set background colors and images at the body, viewport, structure, and column levels of an email in the Email Designer, and Adobe's recommendations for doing so.

**Intents:**

* Set a Background color for the whole email at the body level
* Set the same background color for all structure components using Viewport background color
* Set a different background color for each structure component
* Set a Background image for the content of a structure component
* Set a background color (and, rarely, a background image) at the column level

**Glossary:**

* **Background color**: A color applied to the whole email when the body settings are selected in the navigation tree *(product-specific)*
* **Viewport background color**: A setting that applies the same background color to all structure components, selectable separately from the background color *(product-specific)*
* **Background image**: An image set for the content of a structure component; falls back to the row background color when not supported *(product-specific)*

**Guardrails:**

* Some email programs / clients do not support background images; when not supported, the row background color is used instead, so select an appropriate fallback background color.
* When setting a different background color per structure component, do not set a viewport background color, as it may hide the structure background colors.
* Adobe recommends setting background colors at the column level as the most common use case, for more flexibility when editing the whole email content.
* Try not to use background colors on image or text components, as they are difficult to manage.

**Terminology:**

* Canonical name: Background — Acronym: n/a — variants: background color, background image
* Do not confuse: "Background color" (body-level, whole email) ≠ "Viewport background color" (same color for all structure components)
* Do not confuse: "Background color" (supported broadly) ≠ "Background image" (not supported by all email clients)

**FAQ:**

* **Q: Where does Adobe recommend setting background colors?** — At the column level, which is the most common use case and allows more flexibility when editing the whole email content.
* **Q: What happens if a background image is not supported by an email client?** — The row background color is used instead, so select an appropriate fallback background color.
* **Q: How do I apply the same background color to all structure components?** — Select Viewport background color, which can be set separately from the background color.
* **Q: Why might my per-structure background colors not appear?** — A viewport background color may hide the structure background colors; do not set one in that case.

+++

<!-- ai-section-version: 1 | source-hash: fd466bfc -->
