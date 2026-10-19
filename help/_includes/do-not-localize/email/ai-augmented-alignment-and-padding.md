---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to adjust the vertical alignment and padding of columns in a structure component in the Email Designer, and how to locate and fix residual fragment padding for correct mobile rendering using breadcrumb navigation.

**Intents:**

* Adjust vertical alignment (Top, Middle, Bottom) of a column in a structure component
* Set padding for all sides, or different padding per side, of a column
* Fine-tune padding by breaking synchronization with the lock icon
* Identify and remove hidden or residual fragment padding affecting mobile rendering

**Glossary:**

* **Alignment**: A Styles-tab setting for a column, with options Top, Middle, or Bottom *(product-specific)*
* **Padding**: A Styles-tab setting defining padding for all sides of a column, with an option for Different padding for each side *(product-specific)*
* **Navigation tree**: The left-hand menu used to select a structure component or column *(product-specific)*
* **Breadcrumb navigation**: Used to select each parent structure or column within a fragment to locate hidden padding or margin specific to mobile devices *(product-specific)*

**Guardrails:**

* Residual or hidden fragment padding is particularly common when fragments have been unlocked or when inheritance has been broken, as leftover styling can remain in the underlying column or text components.
* Accumulated styling from repeatedly inserting and removing fragments is expected behavior; verify padding values using breadcrumb navigation, especially when targeting mobile devices.
* For Gmail on Android, use column padding rather than large fixed margins, and use a smaller image width, because Gmail on Android often renders oversized images and margins incorrectly.

**Terminology:**

* Canonical name: Vertical alignment and padding — Acronym: n/a — variants: alignment and padding, column padding
* Synonyms: "Different padding for each side" = "fine tune the padding"
* Do not confuse: "Alignment" (Top/Middle/Bottom vertical positioning) ≠ "Padding" (space on the sides of a column)

**FAQ:**

* **Q: What vertical alignment options are available for a column?** — Top, Middle, or Bottom.
* **Q: How do I set different padding on each side of a column?** — Select Different padding for each side and click the lock icon to break synchronization.
* **Q: Why does my fragment have extra padding on mobile but not desktop?** — Leftover styling can remain when fragments are unlocked or inheritance is broken; use the Navigation tree or breadcrumb to select parent structures/columns and remove or readjust the padding.
* **Q: How should I handle images and dividers for Gmail on Android?** — Use column padding rather than large fixed margins and a smaller image width, since Gmail on Android often renders oversized images and margins incorrectly.

+++

<!-- ai-section-version: 1 | source-hash: b3a152e8 -->
