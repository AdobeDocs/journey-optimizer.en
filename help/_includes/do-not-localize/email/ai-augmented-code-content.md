---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to use the Code your own mode to write or paste raw HTML in the Email Designer code editor to build email content, add personalization, and work with date and time using the available functions and workarounds.

**Intents:**

* Write or paste raw HTML to build email content using Code your own
* Add personalization using the left pane of the code editor
* Preview the message design and personalization using test profiles
* Clear content and start a new design with Change your design
* Work with current date and time using available functions and recommended workarounds

**Glossary:**

* **Code your own**: A mode to write or paste raw HTML to build email content directly in the Email Designer; once chosen, you stay in the code editor and cannot switch to the visual editor *(product-specific)*
* **Advanced HTML editor**: A different feature that lets you toggle between HTML view and the visual (Desktop) view at any time; not the same as Code your own *(product-specific)*
* **`getCurrentZonedDateTime()`**: Returns the current date and time with time zone information; the recommended alternative to `now()` *(product-specific)*
* **`currentTimeInMillis()`**: Returns current time in epoch milliseconds *(product-specific)*

**Guardrails:**

* You must have HTML skills; once you choose Code your own, you stay in the code editor and cannot switch to the visual editor.
* The `now()` function is not supported in the Email Builder's expression language; while available in journey conditions, it cannot be used within email content or the code editor.
* The personalization editor in the Email Designer has some function limitations compared to journey expressions.
* Images from Adobe Experience Manager Assets cannot be referenced when using Code your own; store referenced images in a public location.

**Terminology:**

* Canonical name: Code your own — Acronym: n/a — variants: code editor, code your own content
* Synonyms: "Code your own" = "code editor mode"
* Do not confuse: "Code your own" (code editor only, no switch to visual editor) ≠ "advanced HTML editor" (toggles between HTML view and visual Desktop view)

**FAQ:**

* **Q: Can I switch from the code editor to the visual editor?** — No; once you choose Code your own, you stay in the code editor. (The separate advanced HTML editor does allow toggling between HTML and Desktop views.)
* **Q: Can I use `now()` in email content or the code editor?** — No; `now()` is not supported in the Email Builder's expression language, though it is available in journey conditions. Use `getCurrentZonedDateTime()` (recommended) or `currentTimeInMillis()`.
* **Q: Can I reference AEM Assets images in Code your own?** — No; store images referenced in your HTML code in a public location.
* **Q: How can I perform date calculations in email content?** — Pre-calculate date fields in your data pipeline or profile attributes, use date manipulation functions with profile date values, or use computed attributes.

+++

<!-- ai-section-version: 1 | source-hash: 1711a6a4 -->
