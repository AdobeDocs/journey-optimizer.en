---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to create, apply, favorite, share, and manage predefined filters—saved rule builder queries—for reuse in Orchestrated campaigns.

**Intents:**

* Save a custom filter built in the rule builder as a predefined filter
* Set selected fields as parameters so they remain editable when the filter is applied
* Apply a predefined filter to a rule and edit its parameters
* Switch to rule edition to modify a filter without changing the predefined filter itself
* Mark a predefined filter as a favorite
* Share a predefined filter with other operators in the organization
* Edit or delete an existing predefined filter

**Glossary:**

* **Predefined filter**: a saved rule from the rule builder that can be reused to avoid rebuilding common queries and to standardize targeting logic across orchestrated campaigns *(product-specific)*
* **Set as parameter**: a toggle on a selected field that makes that field editable when the filter is later applied *(product-specific)*
* **Favorite filter**: an option that makes a predefined filter appear in the Favorite filters section of the filter list *(product-specific)*
* **Shared filter**: an option that makes a predefined filter accessible to other operators in the organization, rather than remaining private to its creator *(product-specific)*
* **Switch to rule edition**: an action that lets the current rule being built be edited without modifying the predefined filter itself *(product-specific)*

**Guardrails:**

* Selecting a predefined filter replaces the rule that has been built in the canvas with the selected filter.
* When a filter with parameters is applied, only the fields marked as parameters can be edited.
* Predefined filters are private and visible only to their creator by default.
* Editing a rule after switching to rule edition applies changes only to the current rule being built; the predefined filter itself is not modified.

**Terminology:**

* Canonical name: predefined filter — variants: custom filter (before it is saved)
* Do not confuse: "Favorite filter" (appears in the Favorite filters section for the creator) ≠ "Shared filter" (made accessible to other operators in the organization)
* Do not confuse: applying a predefined filter in a rule (replaces the current canvas rule) ≠ switching to rule edition (edits only the current rule, leaves the predefined filter unchanged)

**FAQ:**

* **Q: What happens when I select a predefined filter in the rule builder?** — It replaces the rule that has been built in the canvas with the selected filter.
* **Q: Can I still edit a predefined filter after applying it?** — Only fields marked as parameters can be edited directly; to change the filter itself, click the ellipsis button and select Switch to rule edition, which applies changes only to the current rule and does not modify the predefined filter.
* **Q: Who can see a predefined filter I create?** — By default it is private and visible only to you, unless you enable the Shared filter option.
* **Q: How do I make selected fields editable when the filter is applied?** — Select the field in the rule builder and toggle on Set as parameter before saving the filter.
* **Q: How do I see my favorite filters?** — Enable the Favorite filter option when saving the filter; it then appears in the Favorite filters section of the filter list.
* **Q: How do I edit or delete a predefined filter?** — Open the predefined filter list using the Select or save filter button, select the ellipsis button next to the filter, and choose the desired action.

**Related pages:**

* To build the rule before saving it as a predefined filter: Learn how to build a rule (orchestrated/build-query.md)

**Personas:**

* **marketer:** Can save a custom filter from the rule builder as a predefined filter, with a label and a description. Can toggle on Set as parameter for selected fields, mark the filter as a favorite, or enable Shared filter when saving. The page states that selecting a predefined filter replaces the rule built in the canvas with the selected filter. Where: "Create a predefined filter".

**Onboarding:**

* **Level:** Intermediate
* **First minimal step:** Open the rule builder and define your filtering conditions.
* **Success check:** Your custom filter is now available in the Predefined Filters list.
* **Previous:** Learn how to build a rule before saving it as a predefined filter: Build your first rule (orchestrated/build-query.md)

+++

<!-- ai-section-version: 1 | source-hash: 71b45a6e -->
