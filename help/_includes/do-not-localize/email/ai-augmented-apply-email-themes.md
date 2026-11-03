---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to create, apply, and reuse themes in the Email Designer to add brand-consistent styling on top of email content and fragments, including converting manual-styling templates into theme-compatible content.

**Intents:**

* Create a theme with a color palette, variants, text settings, spacing, buttons, dividers, and grid layout
* Apply a default or custom theme to an email or content template
* Switch themes and apply a specific color variant to an individual structure component
* Unlock a component's style to override individual styling elements
* Create fragments compatible with themes and associate up to five themes with a fragment
* Convert a manual-styling email template into theme-compatible content using Generate theme from content

**Glossary:**

* **Theme**: Reusable custom styling added on top of standard templates to fit a specific brand and design language *(product-specific)*
* **Use Themes mode**: The mode selected when creating content from scratch to start with a predefined styling theme *(product-specific)*
* **Manual Styling mode**: The alternative mode; if chosen, themes cannot be applied unless you reset your email/design/fragment *(product-specific)*
* **Compatibility mode**: The mode you are in when using content created in HTML, where themes cannot be applied directly *(product-specific)*
* **Color variant**: A distinct color palette and nuance control set within a theme, such as light and dark mode *(product-specific)*
* **Generate theme from content**: A Themes action that automatically detects styling elements in a template and consolidates them into a new theme *(product-specific)*

**Guardrails:**

* This capability is in Limited Availability; contact your Adobe representative to gain access.
* If you choose Manual Styling mode, you cannot apply themes unless you reset your email, design, or fragment.
* Fragments are not cross-compatible between the Use Themes and Manual Styling modes; a fragment used in themed content must itself have been created using themes.
* When using a fragment in email content, the email theme must be one of the themes associated with the fragment; if the theme does not match, the fragment insertion is blocked.
* A fragment can have up to five compatible themes selected (from both the Adobe themes and My themes tabs); this limit is enforced for compatibility and performance reasons. The Adobe default theme cannot be removed, so you can select up to four additional custom themes.
* Content created in HTML is in compatibility mode; to apply themes you must first save it as a new template, then convert the template into theme-compatible content.
* Only email templates can be converted to be theme-compatible; individual emails cannot be converted—you must save content as a template first.
* Gmail and Yahoo! do not load external web fonts and fall back to system fonts; the only Google fonts supported by Gmail are Roboto and Google Sans. Always define fallback fonts.
* Mismatched fragment themes may cause display issues, especially in Outlook 2021 and previous versions.
* The Edit theme button (available in a content template) is not available when using themes in email contents; the specific-variant option cannot be applied to content components (only structure components).

**Terminology:**

* Canonical name: Theme — Acronym: n/a — variants: email theme, Adobe theme, custom theme
* Synonyms: "Use Themes mode" = "Use Themes"
* Do not confuse: "Use Themes mode" (themes can be applied) ≠ "Manual Styling mode" (themes cannot be applied unless reset)
* Do not confuse: "Adobe themes" (built-in themes) ≠ "My themes" (themes you created)

**FAQ:**

* **Q: Is the themes capability generally available?** — No, it is in Limited Availability; contact your Adobe representative to gain access.
* **Q: Can I use any fragment in themed content?** — Only if the fragment was itself created using themes and the email theme matches one of the themes associated with the fragment; otherwise fragment insertion is blocked.
* **Q: How many themes can I associate with a fragment?** — Up to five compatible themes across the Adobe themes and My themes tabs; the Adobe default theme cannot be removed, leaving up to four additional custom themes.
* **Q: Can I convert an existing manually styled asset to use themes?** — Only email templates can be converted (via Generate theme from content); individual emails cannot, so save your content as a template first.
* **Q: What happens to my content when I switch themes?** — The email content remains unchanged, but the styles update to reflect the new theme; overridden (unlocked) styling elements are not changed by the new theme.
* **Q: Why might web fonts not render?** — Gmail and Yahoo! do not load external web fonts and fall back to system fonts; only Roboto and Google Sans are supported by Gmail, so define fallback fonts.

+++

<!-- ai-section-version: 1 | source-hash: dad6c53c -->
