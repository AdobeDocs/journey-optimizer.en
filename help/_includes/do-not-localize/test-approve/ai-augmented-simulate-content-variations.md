---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains the redesigned **[!UICONTROL Simulate content variations]** experience for creating and managing named variants, selecting variants to render, comparing details with previews, and reviewing automatically detected invalid links.

**Intents:**

* Open the content simulation screen by clicking **[!UICONTROL Simulate content]**
* Create variants manually, by uploading a CSV, JSON, or JSONL (JSON Lines) file, by AI generation, or from simulated users
* Name, duplicate, or remove variants, copy attributes, and view configuration details (email only) from their cards
* Select variants to render, preview them or edit their attribute values, show full attribute paths, change the layout, and switch between desktop and mobile views when device-view controls are available
* Export current variants to a CSV file, or use Email-specific tools: **[!UICONTROL Spam report]**, **[!UICONTROL Render email]**, and **[!UICONTROL Send proof]**
* Review invalid-link details for rendered variants or switch back to the classic experience

**Glossary:**

* **[!UICONTROL Simulate content variations]**: The redesigned experience that renders all variants or a selected subset in a scrollable grid, with controls on each card and in the bottom action bar. *(product-specific)*
* **Variant**: A version of the content with different attribute values, created manually, by file upload, with AI, or from a simulated user. *(product-specific)*
* **Simulated users**: Reusable, profile-like test entities that are saved across sessions and can be shared with other users; unlike manually entered variants, they persist beyond the current browser session. *(product-specific)*
* **[!UICONTROL Generate]**: The bottom-action-bar button that auto-generates variants with AI; clicking it replaces all existing variants. *(product-specific)*
* **Content previews and variant details**: Views for displaying rendered content with the eye icon or editing attribute values with the pencil icon. *(product-specific)*
* **[!UICONTROL Vertically stacked]**: The layout where each variant's details and content preview are displayed side by side. *(product-specific)*
* **Full attribute paths**: Paths that identify an attribute's location in profile data and can be shown or hidden in variant details. *(product-specific)*
* **Invalid-links count**: The red count next to the link icon on a variant card when automatic URL validation finds invalid links in that rendered variant. *(product-specific)*
* **[!UICONTROL URL validation failed]**: The dialog that lists each invalid **[!UICONTROL URL]** and its **[!UICONTROL Reason]** for a variant, such as **[!UICONTROL Malformed URL]**. *(product-specific)*
* **[!UICONTROL Send proof]**: An Email-channel tool that sends a proof of one or more variants to a set of email recipients. *(product-specific)*

**Guardrails:**

* You can add up to 30 variants manually or via file upload.
* When using AI generation, up to 40 variants can be created depending on your content's complexity.
* AI generation and desktop/mobile views are available when their controls are provided for the content.
* Clicking **[!UICONTROL Generate]** replaces all existing variants, including any added manually or from a file.
* Editing a simulated-user variant's attribute values is local to testing and is not saved back to the simulated user record.
* **[!UICONTROL Send proof]** accepts up to 10 recipient addresses.
* URLs are automatically validated for each rendered variant.
* Unselected variants remain hidden until they are shown again; they are not removed.
* The mirror page link is not active in proofs sent for variants; it only activates in the final message.

**Terminology:**

* Canonical name: Simulate content variations
* Synonyms: "content variants" = "variants"
* Do not confuse: "[!UICONTROL Simulate content]" (the button that opens the simulation screen) ≠ "[!UICONTROL Simulate content variations]" (the experience) ≠ "[!UICONTROL Old experience]" (returns to the classic layout)
* Do not confuse: content previews (eye icon, view rendering) ≠ variant details (pencil icon, edit attribute values)
* Do not confuse: manually entered variants ≠ "simulated users" (saved, reusable across sessions and persistent beyond the current browser session)
* Do not confuse: selecting simulated users to add as variants ≠ selecting which existing variants to render
* Do not confuse: "[!UICONTROL Send proof]" (send variant proofs to email recipients) ≠ "[!UICONTROL Render email]" (preview across email clients and devices) ≠ "[!UICONTROL Spam report]" (deliverability score)

**FAQ:**

* **Q: How do I open the new experience?** — From your content, click **[!UICONTROL Simulate content]** to open the content simulation screen.
* **Q: Can I render only some variants?** — Yes. Use the variant list icon in the bottom action bar to select the variants to render. **[!UICONTROL Search variants]** helps find a variant, and **[!UICONTROL Show all]** displays every variant again.
* **Q: Does clicking Generate keep my existing variants?** — No. Clicking **[!UICONTROL Generate]** replaces all existing variants, including any added manually or from a file.
* **Q: Can I compare variant details with the preview?** — Yes. In the **[!UICONTROL Vertically stacked]** layout, each variant's details and content preview are displayed side by side.
* **Q: How do I review invalid links?** — Click the red invalid-links count on the variant card to open the **[!UICONTROL URL validation failed]** dialog and review each **[!UICONTROL URL]** and its **[!UICONTROL Reason]**. Use **[!UICONTROL Copy]** to copy the validation details.
* **Q: How do I go back to the old layout?** — Click **[!UICONTROL Old experience]** in the bottom action bar.

+++

<!-- ai-section-version: 2 | source-hash: 622e0e51 -->
