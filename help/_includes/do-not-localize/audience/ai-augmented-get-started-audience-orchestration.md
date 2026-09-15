---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** Audience composition lets you create composition workflows that combine existing Adobe Experience Platform audiences in a visual canvas and apply activities such as split, exclude, enrich, and rank to produce new audiences that are saved back into Adobe Experience Platform for use in Journey Optimizer campaigns and journeys.

**Intents:**

* Create a composition workflow that combines existing Adobe Experience Platform audiences
* Apply Audience, Split, Exclude, Enrich, and Rank activities to build new audiences
* Enrich an audience with additional attributes from Adobe Experience Platform datasets
* Publish a composition to save the resulting audiences into Adobe Experience Platform
* Access, duplicate, or delete existing compositions and track their status

**Glossary:**

* **Audience composition**: Capability to create composition workflows that combine existing Adobe Experience Platform audiences in a visual canvas to create new audiences *(product-specific)*
* **Composition workflow**: A workflow on the composition canvas where audiences are combined and arranged using activities to create new audiences *(product-specific)*
* **Resulting audiences**: The new audiences produced by a composition, saved back into Adobe Experience Platform once published *(product-specific)*
* **Audience activity**: The starting-point activity that selects one or multiple audiences as the basis for the workflow *(product-specific)*
* **Save activity**: The last-step activity that saves the result of the workflow into a new audience *(product-specific)*
* **Enrich activity**: Activity that enriches an audience with additional attributes coming from Adobe Experience Platform datasets *(product-specific)*
* **Rank activity**: Activity that ranks profiles based on a specific attribute and includes them into the composition *(product-specific)*
* **Split activity**: Activity that divides the composition into multiple paths, saving one audience per path when published *(product-specific)*

**Guardrails:**

* You can publish up to 10 compositions in a given sandbox (hard limit); if you reach this threshold you must delete a composition to free up space before publishing a new one.
* Audiences from audience composition are executed daily, so you may need to wait up to 24 hours before using them in Journey Optimizer.
* Enriched attributes in audience composition audiences are as fresh as the last composition run, which can be up to 24 hours in the past.
* The use of audiences and attributes from audience composition is currently unavailable with Healthcare Shield or Privacy and Security Shield.
* Enrichment attributes are not yet integrated with the policy enforcement service, so data usage labels applied to enrichment attributes are not enforced in Journey Optimizer campaigns or journeys.
* Audience composition is not integrated with the sandbox reset capability; you must delete compositions manually before a sandbox reset so associated audience data is cleaned up.
* If any error occurs during publishing, alerts display with information on how to resolve the issue.

**Terminology:**

* Canonical name: Audience composition — Acronym: n/a — variants: composition, composition workflow
* Synonyms: "resulting audiences" = "audiences created by the composition"
* Do not confuse: "Draft" (composition in progress, not published) ≠ "Published" (composition published, resulting audiences saved and available)
* Do not confuse: "Audience activity" (starting point of the composition) ≠ "Save activity" (last step that saves the result)

**FAQ:**

* **Q: How do I create a new audience with audience composition?** — Access the Audiences menu, select Create Audience then Compose Audience, add activities between the Audience and Save activities, then Publish.
* **Q: How many compositions can I publish in a sandbox?** — Up to 10 in a given sandbox; if you reach the threshold you must delete one to publish another.
* **Q: How soon can I use an audience from a composition?** — Audiences from audience composition are executed daily, so it may take up to 24 hours.
* **Q: What statuses can a composition have?** — Draft (in progress, not published) and Published (resulting audiences saved and available for use).
* **Q: Can I use audience composition with Healthcare Shield or Privacy and Security Shield?** — No, use of audiences and attributes from audience composition is currently unavailable with Healthcare Shield or Privacy and Security Shield.

+++

<!-- ai-section-version: 1 | source-hash: 3d7dfc65 -->
