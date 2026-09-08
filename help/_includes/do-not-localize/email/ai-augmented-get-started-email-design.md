---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to design email content in the Email Designer — building from scratch, code, or imported HTML — verify it with automated content checks and content quality validation, export it, and follow rendering best practices and client-specific limitations.

**Intents:**

* Choose how to design an email: from scratch, code/paste raw HTML, import existing HTML, convert image designs to HTML, or select an existing content template
* Verify email content with automated content checks before sending
* Validate content quality for readability, cohesiveness, and effectiveness
* Export email content as a zip file containing HTML and assets
* Apply email design best practices to keep emails rendering well across clients
* Account for mobile web browser and Outlook rendering limitations

**Glossary:**

* **Email Designer**: The [!DNL Journey Optimizer] interface used to import content or build responsive emails from scratch, code, or imported HTML *(product-specific)*
* **Automated content checks**: A check that catches HTML and CSS issues — such as unsupported tags, empty divs, and size limit violations — directly in the authoring panel, before sending *(product-specific)*
* **Content quality validation**: A validation that identifies potential issues with readability, content cohesiveness, and effectiveness *(product-specific)*
* **Image to HTML converter**: An AI-powered converter that transforms static image designs into editable email templates *(product-specific)*
* **Export HTML**: An action that saves a zip file to your computer including your HTML and assets *(product-specific)*

**Guardrails:**

* Recommended template widths are between 600px and 800px (recommended).
* Recommended practices: static, table-based layouts; HTML tables and nested tables; simple, inline CSS; web-safe fonts.
* Use with care (may not render everywhere): background images, custom web fonts, wide layouts, image maps, and embedded CSS (embedded CSS is sometimes removed during email delivery).
* Not recommended (generally unsupported in email): JavaScript, `<iframe>` tags, Flash, embedded audio, embedded video, forms, and `<div>` layering.
* Alerts distinguish warnings (recommendations and best practices) from errors (blocking issues that prevent testing or activation).
* Mobile web rendering differences occur only in Gmail Web and Outlook Web when accessed via a mobile browser; Gmail/Outlook native mobile apps and all desktop clients are not affected.
* Outlook rendering: use even numbers for padding, font sizes, and widths; set table widths in pixels not percentages; set image widths using the `width` attribute; include Alt text on all images; apply borders to `<td>` not `<table>`; avoid `border-radius` (rounded corners).

**Terminology:**

* Canonical name: Email Designer — Acronym: n/a — variants: message editor, email design capabilities
* Synonyms: "automated content checks" = "content check"
* Do not confuse: "automated content checks" (HTML/CSS issue detection) ≠ "content quality validation" (readability, cohesiveness, effectiveness)
* Do not confuse: "warnings" (recommendations and best practices) ≠ "errors" (blocking issues that prevent testing or activation)

**FAQ:**

* **Q: What options are available for designing an email?** — Design from scratch, code or paste raw HTML, import existing HTML from a file or .zip, convert image designs to HTML templates, or select an existing built-in or custom template.
* **Q: How can I catch HTML and CSS issues before sending?** — Use automated content checks, which flag unsupported tags, empty divs, and size limit violations in the authoring panel.
* **Q: What template width is recommended?** — Between 600px and 800px.
* **Q: Why does my email look different in Gmail or Outlook on a phone browser?** — This is a known limitation of Gmail Web and Outlook Web via a mobile browser; use simple table-based layouts with fully inlined CSS and avoid relying on media queries or `<style>` blocks for critical layout.
* **Q: How do I export my content?** — Click Export HTML to save a zip file containing your HTML and assets to your computer.

+++

<!-- ai-section-version: 1 | source-hash: 09292cd0 -->
