---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to review, delete, and undo changes applied to a web page from the Modifications pane, and how to add CSS selector and page head modifications directly in Journey Optimizer.

**Intents:**

* Review the changes made to a page from the Modifications pane
* Delete a single modification, multiple modifications, all modifications, or only invalid modifications
* Undo and redo actions using the Undo/Redo button
* Add a modification directly from the pane as a CSS Selector or Page `<head>` type
* Configure a CSS Selector modification with a Set Content or Set Attribute action
* Add custom JavaScript or CSS code through a Page `<head>` modification

**Glossary:**

* **Modifications pane**: The pane used to navigate through and manage all components, adjustments, and styles added to a web page, and to add new modifications *(product-specific)*
* **Invalid modifications**: Changes that were overridden by other changes, for example a color modification whose target text was later deleted *(product-specific)*
* **CSS Selector modification**: A modification type that uses the CSS Element Selector field to identify HTML elements (DOM nodes) and apply a Set Content or Set Attribute action *(product-specific)*
* **Page `<head>` modification**: A modification type for adding custom code to the `<head>` container, executed at the beginning of page load *(product-specific)*
* **Set Content**: A CSS Selector action that specifies the content placed into the element identified by the CSS Element Selector *(product-specific)*
* **Set Attribute**: A CSS Selector action that associates an attribute (name and value) with the current CSS selector; an existing attribute's value is updated, otherwise a new attribute is added *(product-specific)*

**Guardrails:**

* Proceed with care when deleting an action, as it may impact subsequent actions.
* You can only add `<script>` and `<style>` elements to the `<head>` section; adding `<div>` tags and other elements might cause remaining `<head>` elements to pop into the `<body>`.
* Do not perform document.write actions in custom code scripts, as scripts are executed asynchronously and this often causes document.write to appear in the wrong place.
* If you create an element and then modify it, do not delete the original element, because the modifying action would no longer have anything to modify and would stop working.
* If you use the Page `<head>` modification type for two campaigns impacting the same URL, JavaScript is injected from both campaigns and Journey Optimizer automatically determines the order; make sure the code does not depend on placement and has no conflicts.
* Always wrap custom code in one element; if the code is no longer needed, leave the container empty but do not remove it.

**Terminology:**

* Canonical name: Modifications pane — Acronym: n/a — variants: Modifications panel
* Synonyms: "CSS Element Selector" = "CSS selector field used to find and select HTML elements"
* Do not confuse: "Set Content" (specifies content placed into the selected element) ≠ "Set Attribute" (associates an attribute name and value with the CSS selector)
* Do not confuse: "Delete modification" (removes one modification) ≠ "Undo" (cancels an action, reversible with Redo)
* Do not confuse: "invalid modifications" (changes overridden by other changes) ≠ modifications you intentionally delete

**FAQ:**

* **Q: How do I delete all modifications at once?** — Use the More actions button on top of the Modifications pane to delete all modifications at once.
* **Q: What are invalid modifications?** — Changes that were overridden by other changes, such as a color modification whose target text was later deleted; you can delete only the invalid modifications.
* **Q: What can I add in a Page `<head>` modification?** — Only `<script>` and `<style>` elements; adding `<div>` tags and other elements might cause remaining `<head>` elements to pop into the `<body>`.
* **Q: What is the difference between Set Content and Set Attribute?** — Set Content specifies the content placed into the element identified by the CSS Element Selector; Set Attribute associates an attribute name and value with the CSS selector, updating it if it already exists.
* **Q: Can I undo changes?** — Yes, use the Undo/Redo button on the top right; click and hold to switch between Undo and Redo, then click to apply.

+++

<!-- ai-section-version: 1 | source-hash: 44fbd25e -->
