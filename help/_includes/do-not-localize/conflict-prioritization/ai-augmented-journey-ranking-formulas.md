---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to create ranking formulas that dynamically rank journeys based on journey attributes, profile attributes, or AI model scores, and how to assign them to a rule set so the best journey is selected per profile when journey caps apply.

**Intents:**

* Create a ranking formula with one or more criteria in [!UICONTROL Orchestration ranking] > [!UICONTROL Ranking formulas]
* Assign ranking scores using variables (journey priority, AI model score), attributes, static values, or a combination
* Optionally reference an AI model with [!UICONTROL Select AI model]
* Express a formula in PQL syntax using the code editor
* Assign the formula to a journey-domain rule set and apply that rule set to journeys

**Glossary:**

* **Ranking formula**: An expression that dynamically ranks journeys based on journey attributes, profile attributes, or AI model scores *(product-specific)*
* **Ranking object**: The entity that the formula applies to; by default set to [!UICONTROL Journey] *(product-specific)*
* **Journey priority**: A manual value assigned to the journey when creating it *(product-specific)*
* **[!UICONTROL Ranking method]**: Rule set setting that selects [!UICONTROL Formula] instead of the default [!UICONTROL Priority] *(product-specific)*
* **[!UICONTROL Criterion]**: A condition (journey attribute, logical operator, matching condition) with an expression that assigns a ranking score *(product-specific)*

**Guardrails:**

* This feature is currently in Limited Availability; contact your Adobe representative to gain access.
* Ranking formulas are only available to organizations that have purchased the **Decisioning** add-on offering.
* Formulas are assigned at the rule set level, not on individual journeys.
* To use a formula, set the rule set [!UICONTROL Ranking method] to [!UICONTROL Formula] instead of the default [!UICONTROL Priority], and select the [!UICONTROL Journey] domain.
* Switching to the code editor (PQL syntax) will prevent you from reverting back to the default builder view for this formula.
* Only one rule set can be applied to a journey at a time.
* Criterion logic: if the first criterion is true for a decision item it takes precedence over the next ones; otherwise the decisioning engine moves on to the next criterion, and so on.
* Example expressions keep weights verbatim: journey priority; journey priority plus 5 (Loyalty tag with Gold status); journey priority plus 2 (Loyalty tag with Silver status).

**Terminology:**

* Canonical name: ranking formula — Acronym: n/a — variants: journey arbitration ranking formulas, journey ranking formula
* Synonyms: none
* Do not confuse: "ranking formula" (a dynamic expression) ≠ "journey priority" (a static manual value) ≠ "AI model score" (a trained model output referenced in a formula)
* Do not confuse: "[!UICONTROL Formula]" ranking method ≠ "[!UICONTROL Priority]" ranking method (the default)

**FAQ:**

* **Q: What can a ranking formula reference?** — A variable (journey priority or AI model score), an attribute (profile or journey attribute), a static value, or a combination of these.
* **Q: How is precedence decided across criteria?** — The first criterion that is true for a decision item takes precedence; otherwise the decisioning engine evaluates the next criterion.
* **Q: Are formulas assigned per journey?** — No, formulas are assigned at the rule set level; the rule set is then applied to journeys.
* **Q: What happens if I switch to the code editor?** — You express the formula in PQL syntax, and this prevents reverting back to the default builder view for that formula.
* **Q: When is the formula applied?** — When the cap is applied; all journeys using the rule set are ranked with the selected formula.

+++

<!-- ai-section-version: 1 | source-hash: 5339e166 -->
