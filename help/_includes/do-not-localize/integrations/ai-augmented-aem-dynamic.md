---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to insert, adjust, and personalize Adobe Experience Manager dynamic media in Journey Optimizer content, including text overlays, dynamic media templates, and countdown timers.

**Intents:**

* Insert an Adobe Experience Manager dynamic media asset into HTML content using the asset selector
* Adjust image parameters such as height, width, rotate, flip, brightness, and hue
* Personalize a dynamic media text overlay with different text per treatment or profile
* Add a dynamic media template using the Image component or HTML component
* Insert a countdown timer that updates in real time when recipients open the email

**Glossary:**

* **Dynamic media**: Adobe Experience Manager media renditions selected through the asset selector, where changes made in Adobe Experience Manager are instantly reflected in Journey Optimizer content *(product-specific)*
* **Text overlay personalization**: Replacing a dynamic media text overlay with new text, which can differ per treatment or profile *(product-specific)*
* **Dynamic media template**: A template added in Journey Optimizer that supports personalization fields, inserted via the Image or HTML component *(product-specific)*
* **Countdown timer**: A Dynamic Media component that updates in real time when recipients open the email, showing time remaining or a fallback message after the end date *(product-specific)*
* **Layer parameter**: The base element where overlay text is placed, required to update dynamic media text overlays *(product-specific)*

**Guardrails:**

* The dynamic media integration is only available for customers using Dynamic Media Manager as a Cloud Service.
* For Healthcare customers, the integration is enabled only upon licensing the Journey Optimizer Healthcare Shield and Adobe Experience Manager Extended Security for Healthcare add-on offerings.
* Text overlay personalization is available exclusively in Dynamic Media Scene7 mode; for Healthcare customers, since Scene7 mode is not accessible, content is rendered using a Journey Optimizer binary copy of the image.
* Dynamic media template is available exclusively in Dynamic Media Scene7 mode; for Healthcare customers, since Scene7 mode is not accessible, content will not be rendered.
* The Layer parameter is required to update your dynamic media text overlay.
* For countdown timers, the End time must be entered in GMT (Greenwich Mean Time) only; the system does not accept other time zones.
* For Dynamic Media Scene7 assets, Journey Optimizer adds default modifiers `bfc=off&fmt=png-alpha` at the start of the URL; if the preset also sets `fmt` or `bfc`, it takes precedence because Scene7 uses the last occurrence of a repeated parameter.

**Terminology:**

* Canonical name: dynamic media — Acronym: n/a — variants: Adobe Experience Manager dynamic media, dynamic media renditions
* Synonyms: "Scene7 mode" = "Dynamic Media Scene7 mode"
* Do not confuse: "text overlay personalization" (replacing overlay text on a dynamic media asset) ≠ "dynamic media template" (a template with personalization fields inserted via the Image or HTML component)

**FAQ:**

* **Q: Do I need to manually update assets changed in Adobe Experience Manager?** — No; changes made to assets in Adobe Experience Manager are instantly reflected in Journey Optimizer content, so the most up-to-date versions are always in use.
* **Q: Which customers can use the dynamic media integration?** — Only customers using Dynamic Media Manager as a Cloud Service.
* **Q: Why cannot Healthcare customers use text overlays or templates the same way?** — Those features are exclusive to Scene7 mode, which is not accessible for Healthcare customers; text overlay content is rendered using a Journey Optimizer binary copy, and dynamic media templates will not be rendered.
* **Q: What time zone does the countdown timer End time use?** — GMT (Greenwich Mean Time) only; the system does not accept other time zones.
* **Q: How do I deliver an asset in its original format such as GIF or SVG?** — The asset selector returns a `/images`-based URL, so you must manually update the URL to use the `/content` path instead.

+++

<!-- ai-section-version: 1 | source-hash: 1b680601 -->
