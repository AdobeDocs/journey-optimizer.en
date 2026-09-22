---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page lists best practices for designing accessible emails and landing pages in the Journey Optimizer Email Designer, in line with WCAG 2.1 level AA, covering text readability, alternative text, readable format, dark mode, accessibility attributes, and testing.

**Intents:**

* Ensure text readability using accessible fonts, font sizing, and color contrast in the Text component Styles tab
* Provide alternative text for images with the Image component
* Use the lang and dir attributes and layout-table roles to support assistive technologies
* Design content for dark mode using the Dark mode view
* Test content accessibility using preview, Email rendering, proofs, and content quality validation
* Provide keyboard navigation and focus support for interactive elements

**Glossary:**

* **Live view**: A generic preview in the Email Designer, accessed via Switch to live view, to compare how rendering might look across various device sizes; the final rendering may vary by email client *(product-specific)*
* **Dark mode**: An Email Designer view you can switch to and define custom settings for, displayed by supporting email clients *(product-specific)*
* **Email rendering**: A testing option that leverages Litmus to simulate designs across major email clients (Apple Mail, Gmail, Outlook) *(product-specific)*
* **Send proofs**: Sending proofs to test the rendering of content before sending it to the real audience *(product-specific)*
* **`role="presentation"`**: An attribute (or `role="none"`) added to layout tables so assistive technologies skip their structure and focus only on the content

**Guardrails:**

* Minimum font size of 16px for body text.
* Maintain a contrast ratio of at least 4.5:1 between text and background; for large text (≥24px or bold 18px), at least 3:1 contrast.
* Ensure text can be zoomed up to 200% without breaking layout.
* WCAG 2.2 focus appearance standards for focus indicators: minimum 2 CSS pixel thick outline, and contrast ratio ≥ 3:1 between focused and unfocused state.
* Interactive elements should have `tabindex="0"` to be included in the natural tab order.
* Keep sentences to around 20 words or less.
* Journey Optimizer testing capabilities are not specifically designed to check full accessibility; they provide a first level of verification, and specific external tools are recommended for consistent checking.
* Use `role="presentation"` exclusively for layout tables; retain the semantic `<table>` structure for data tables.

**Terminology:**

* Canonical name: Accessible content — Acronym: WCAG (Web Content Accessibility Guidelines) — variants: accessible emails, accessible landing pages
* Synonyms: "alternative text" = "alt text"
* Do not confuse: "accessibility of your content" (this page) ≠ "accessibility of the Journey Optimizer interface itself" (separate section)
* Do not confuse: "Live view" (device-size rendering preview) ≠ "Email rendering" (Litmus simulation across email clients) ≠ "Send proofs" (test before sending to real audience)

**FAQ:**

* **Q: What accessibility standard does the Email Designer align with?** — Web Content Accessibility Guidelines (WCAG) 2.1, level AA.
* **Q: What is the minimum recommended body text size and contrast ratio?** — 16px for body text, with a contrast ratio of at least 4.5:1 between text and background (3:1 for large text).
* **Q: Can Journey Optimizer confirm my content is fully accessible?** — No; its testing capabilities provide a first level of verification only, so use specific external tools such as the WebAIM contrast checker, WAVE, and screen readers for consistent checking.
* **Q: How do I make layout tables accessible to screen readers?** — Add `role="presentation"` (or `role="none"`) to layout tables so assistive technologies skip their structure and focus on the content.
* **Q: Which attributes help screen readers interpret content?** — The `lang` (language) and `dir` (text direction) attributes in the content body.

+++

<!-- ai-section-version: 1 | source-hash: 77fd68e9 -->
