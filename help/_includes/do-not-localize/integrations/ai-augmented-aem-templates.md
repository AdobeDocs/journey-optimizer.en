---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to design templates in Adobe Experience Manager, export (send) them to Journey Optimizer, and use and personalize them as content templates in the Email Designer.

**Intents:**

* Design templates in Experience Manager using its content sources
* Send an Experience Manager template to Journey Optimizer as a content template in a chosen sandbox
* Add Journey Optimizer personalization syntax to the template
* Use, edit, and personalize the imported template as a content template
* Assign data usage labels through Manage access (Object Level Access Control)
* Preview personalized content with the simulation methods before sending

**Glossary:**

* **Content template**: The imported Experience Manager template as it appears in Journey Optimizer, available in the selected sandbox and usable in the Email Designer *(product-specific)*
* **Send to**: The Experience Manager advanced-menu action that exports a template to Journey Optimizer *(product-specific)*
* **Compatibility mode**: The only mode available when editing and personalizing an imported Experience Manager template *(product-specific)*
* **Simulate content**: Option to test content variations with sample input data or AI auto-generation *(product-specific)*
* **Simulate content (AEP profiles)**: Option, selected from the Simulate content dropdown, to preview with test profiles *(product-specific)*

**Guardrails:**

* Integration with Experience Manager is available as a beta to select users only.
* This capability is available with Adobe Experience Manager as a Cloud Service; during the beta the Cloud Service configuration is performed by Adobe.
* To create, edit, and delete content templates you must have the Manage Library Items permission included in the Content Library Manager product profile.
* Proper Journey Optimizer syntax is required for personalization in the Experience Manager template to be effective.
* Bulk template export is not currently supported; templates must be exported individually.
* Syncing between Experience Manager and Journey Optimizer is not currently available; if a template changes after being sent, you must re-export and re-send it.
* Editing and personalizing an imported template is only possible in compatibility mode.

**Terminology:**

* Canonical name: Adobe Experience Manager templates — Acronym: n/a — variants: AEM templates, Experience Manager template, content template
* Synonyms: "export" = "send to Journey Optimizer"
* Do not confuse: "Simulate content" (sample input data or AI auto-generation) ≠ "Simulate content (AEP profiles)" (preview with test profiles)

**FAQ:**

* **Q: How do I get an Experience Manager template into Journey Optimizer?** — From the Experience Manager homepage select Outbound Marketing, then use Send to on the template, enter a Name, and select the target Sandbox.
* **Q: Can I export multiple templates at once?** — No, bulk template export is not currently supported; templates must be exported individually.
* **Q: What happens if I change the template in Experience Manager after sending it?** — Syncing is not available, so you must re-export the template and re-send it to Journey Optimizer.
* **Q: What permission do I need to manage content templates?** — The Manage Library Items permission included in the Content Library Manager product profile.
* **Q: In what mode can I edit an imported template?** — Only in compatibility mode.

+++

<!-- ai-section-version: 1 | source-hash: e329639f -->
