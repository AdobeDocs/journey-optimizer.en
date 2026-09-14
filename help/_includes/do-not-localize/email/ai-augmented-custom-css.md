---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to add custom CSS to email content in the Email Designer for advanced styling, how to keep the CSS valid, how it is implemented in the HTML, and how to troubleshoot styles that are not applied.

**Intents:**

* Add custom CSS to email content for advanced and specific styling
* Ensure the entered CSS is valid so it is applied and can be saved
* Understand where custom CSS is injected in the generated HTML
* Troubleshoot custom CSS that is not applied
* Understand custom CSS behavior with imported content

**Glossary:**

* **Add Custom CSS**: The Email Designer option (available when Body is selected) to enter custom CSS in a dedicated text area *(product-specific)*
* **CSS styles section**: The section, shown when Body is selected and content is present, from which custom CSS is added *(product-specific)*
* **global-custom**: The `data-name="global-custom"` `<style>` tag added to the end of the `<head>` where custom CSS is placed *(product-specific)*
* **Compatibility mode**: The mode for imported external HTML content (unless converted) in which the CSS styles section is not available *(product-specific)*

**Guardrails:**

* The CSS styles section is only available when content is already present in the editor; the Add custom CSS button is only available when Body is selected.
* Custom CSS must be valid and follow proper syntax; invalid CSS (for example using `<style>` tags, or syntax errors such as missing braces) triggers an error message and cannot be saved.
* When using a template with locked content, you cannot add custom CSS; the button changes to View custom CSS and existing custom CSS is read-only.
* If you remove all content, the CSS styles section disappears and the previously defined custom CSS is no longer applied; adding content back reapplies it.
* For imported external HTML content in Compatibility mode (unless converted), the CSS styles section is not available.
* Users are responsible for the security of their custom CSS and should ensure it does not introduce vulnerabilities or break the layout.
* Custom CSS is not interpreted or validated by the Settings pane; it is independent and can only be modified through the Add Custom CSS option.

**Terminology:**

* Canonical name: Custom CSS — Acronym: CSS — variants: Add Custom CSS, custom CSS styles
* Synonyms: "Add custom CSS" = "Add Custom CSS" (button); becomes "View custom CSS" for locked content
* Do not confuse: "custom CSS" (`global-custom` style tag) ≠ default/system-generated CSS styles (other `data-name` style tags such as `default`, `grid`, `acr-theme`)
* Do not confuse: "Compatibility mode" (imported external HTML, no CSS styles section) ≠ content created with the Email Designer (custom CSS visible and editable)

**FAQ:**

* **Q: Why is the Add custom CSS button missing?** — The CSS styles section requires content in the editor, and the button is only available when Body is selected.
* **Q: What happens if my CSS is invalid?** — An error message is displayed indicating the CSS cannot be saved; `<style>` tags and syntax errors such as missing braces are not accepted.
* **Q: Where is my custom CSS added in the HTML?** — To the end of the `<head>` section as a `<style data-name="global-custom">` tag.
* **Q: My custom CSS is not applied — what should I check?** — Verify the CSS is valid, that it is in the `global-custom` style tag, that `data-disabled` is not set to `true`, and that it is not overridden by other rules including an applied theme; consider adding `!important`.
* **Q: Can I add custom CSS to a template with locked content?** — No; the button becomes View custom CSS and any existing custom CSS is read-only.

+++

<!-- ai-section-version: 1 | source-hash: d4b155f9 -->
