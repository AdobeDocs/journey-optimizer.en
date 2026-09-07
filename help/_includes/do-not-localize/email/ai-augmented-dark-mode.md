---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how email clients handle dark mode and how to preview the default dark mode and define custom dark mode settings in the Email Designer, along with best practices for consistent rendering.

**Intents:**

* Understand how the main email clients handle dark mode
* Preview the default dark mode in the Email Designer
* Define custom dark mode settings, including specific images for dark mode
* Check rendering with Switch to live view and Simulate content
* Apply best practices for images, backgrounds, and accessible dark mode content

**Glossary:**

* **Dark mode**: A view letting supporting email clients display emails with darker backgrounds and lighter text, buttons, and UI elements *(product-specific)*
* **Full color invert**: The color scheme the default dark mode preview applies to all elements except images and icons, inverting light and dark areas *(product-specific)*
* **Custom dark mode**: Specific styling settings you define that display only when dark mode is enabled in a supporting recipient's email client *(product-specific)*
* **Switch to live view**: A generic preview to compare how content renders across various device sizes, with a Dark mode toggle *(product-specific)*
* **Simulate content**: The option used (via Simulate content (AEP profiles), then Render email with Litmus) to check email rendering *(product-specific)*

**Guardrails:**

* The final dark mode rendering depends on the recipient's email client and can vary a lot from one to another.
* Clients that do not support dark mode (for example Yahoo!Mail, AOL) never display any dark mode rendering, whether or not custom settings are defined.
* Clients that apply their own default dark mode (for example Gmail, Outlook Windows, Outlook Windows Mail) override any custom dark mode settings defined in the Email Designer.
* Custom dark mode renders only on clients supporting the `@media (prefers-color-scheme: dark)` query (for example Apple Mail macOS, Apple Mail iOS, Outlook macOS, Outlook.com, Outlook iOS, Outlook Android).
* The default dark mode preview applies the full color invert color scheme to all elements except images and icons.
* You cannot change the colors of images and icons, but you can define specific assets for dark mode only.
* Some clients such as Apple Mail 16 (macOS 13) will not generate dark mode if images are present in the email content.

**Terminology:**

* Canonical name: Dark mode — Acronym: n/a — variants: Dark mode view, custom dark mode
* Method: Journey Optimizer uses the `@media (prefers-color-scheme: dark)` CSS query for custom dark mode
* Do not confuse: "default dark mode preview" (full color invert applied by the Email Designer) ≠ "custom dark mode" (specific settings you define)
* Do not confuse: "Switch to live view" (generic multi-device preview) ≠ "Simulate content" / "Email rendering" (Litmus-based simulation across email clients)

**FAQ:**

* **Q: Will my dark mode design look the same everywhere?** — No; the final rendering depends on each recipient's email client and can vary; it cannot be guaranteed identical across clients.
* **Q: Why don't my custom dark mode settings appear in Gmail?** — Clients such as Gmail apply their own default dark mode, which overrides the custom settings defined in the Email Designer.
* **Q: Can I change image colors for dark mode?** — No; you cannot change the colors of images and icons, but you can define specific assets to display in dark mode.
* **Q: How do I check the closest rendering to the final result?** — Use Simulate content, then Simulate content (AEP profiles) and Render email with a Litmus account, or the Email rendering option.
* **Q: What color scheme does the default preview use?** — Full color invert, applied to all elements except images and icons.

+++

<!-- ai-section-version: 1 | source-hash: 99152c54 -->
