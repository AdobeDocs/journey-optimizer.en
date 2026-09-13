---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to configure a data source from the Configurations menu and how to define field groups so your journeys retrieve only the specific data they need.

**Intents:**

* Configure a data source from the Administration Configurations menu
* Define one or several field groups for a data source
* Name field groups and select only the fields needed to reduce request latency
* Check how many journeys use a field group with the Used in field and View journeys button
* Add fields to, or remove fields from, a field group according to its lifecycle rules

**Glossary:**

* **Field group**: A set of fields that you can retrieve from a data source and use in a journey *(product-specific)*
* **Used in**: The field that displays the number of journeys using a field group, with a View journeys button to list them *(product-specific)*

**Guardrails:**

* The data source configuration is always performed by a technical user.
* When a data source field is used in a journey, the system retrieves all fields defined for that field group; selecting only the fields you need reduces request latency and increases performance.
* If a field group has no field, it is not displayed in the expression editor.
* You can add or remove fields from a field group only if it is not used in any draft or live journey.
* If a field group is used in one or more draft or live journeys, you can incrementally add new fields from the selected schema, but cannot deselect, remove, or modify fields that have already been selected.
* Updates to a field group are not permitted if existing fields of a schema already in use by draft or live journeys are modified, for example changing the data type of a field.

**Terminology:**

* Canonical name: field group — Acronym: n/a — variants: field groups
* Do not confuse: "add fields to the built-in data source" ≠ "create a new external data source"

**FAQ:**

* **Q: Where do I configure a data source?** — In the Administration menu section, select Configurations, then in the Data Sources section click Manage to display the list of data sources.
* **Q: Why should I select only the fields I need in a field group?** — When a field is used in a journey, the system retrieves all fields defined for that field group, so selecting only the fields you need reduces request latency and increases performance.
* **Q: Why is my field group not showing in the expression editor?** — If a field group has no field, it is not displayed in the expression editor.
* **Q: Can I modify fields already used by a draft or live journey?** — No, if a field group is used in one or more draft or live journeys you can incrementally add new fields but cannot deselect, remove, or modify fields already selected.
* **Q: How do I remove a field from a field group used in journeys?** — Duplicate the field group, remove the unwanted fields in the duplicate, update each journey to use the duplicate, stop the old journey versions, and then remove the original field group once it is no longer used.

+++

<!-- ai-section-version: 1 | source-hash: b9f7ff69 -->
