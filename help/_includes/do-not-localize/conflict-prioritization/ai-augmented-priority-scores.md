---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to assign a priority score (0-100) to a journey, campaign, or inbound channel action so the most important communication takes precedence when a profile qualifies for more than one under a constraint such as a frequency cap.

**Intents:**

* Assign a priority score to a journey or campaign in its properties
* Assign a priority score to an inbound channel action in the [!UICONTROL Action] activity
* Ensure a specific communication is shown by giving it the highest score
* Override the inherited journey priority for an action by unselecting [!UICONTROL Use journey priority]

**Glossary:**

* **Priority score**: A numeric value from 0-100 assigned to a journey, campaign, or action; the higher the number, the higher the priority *(product-specific)*
* **[!UICONTROL Use journey priority]**: Option, selected by default, that inherits the action's priority from the overall journey priority score *(product-specific)*
* **[!UICONTROL Conflict management]**: Section of the [!UICONTROL Action] activity where the action priority is set *(product-specific)*
* **Inbound channel action**: A web, in-app, or code-based action within the [!UICONTROL Action] activity that can take a priority score *(product-specific)*

**Guardrails:**

* Enter a numeric value from 0-100 in the [!UICONTROL Priority score] field; the higher the number, the higher the priority.
* In campaigns, priority score is available for the web, in-app, and code-based inbound channels only.
* In the [!UICONTROL Action] activity, priority score is available for the web, in-app, and code-based inbound channels only.
* If two journeys or campaigns have the same priority score, the system does not have a tie-breaking mechanism; ensure priority scores are unique to avoid conflicts.
* In the [!UICONTROL Action] activity, [!UICONTROL Use journey priority] is selected by default, so the action inherits the journey's priority score until you unselect it.

**Terminology:**

* Canonical name: priority score — Acronym: n/a — variants: priority, Priority score
* Synonyms: none
* Do not confuse: "priority score" (a static 0-100 value setting precedence) ≠ "ranking formula" (a dynamic expression that ranks journeys)
* Do not confuse: journey or campaign "[!UICONTROL Priority score]" ≠ action "[!UICONTROL Priority]" (which by default inherits the journey score via [!UICONTROL Use journey priority])

**FAQ:**

* **Q: What range can a priority score take?** — A numeric value from 0-100, where the higher the number, the higher the priority.
* **Q: How do I make sure a specific campaign is shown?** — Give it a score of 100.
* **Q: What happens if two items share the same priority score?** — The system has no tie-breaking mechanism, so ensure priority scores are unique.
* **Q: On which channels is priority score available?** — The web, in-app, and code-based inbound channels only.
* **Q: How does an action get its priority?** — By default it inherits the journey priority via [!UICONTROL Use journey priority]; unselect that option to set a separate value from 0-100.

+++

<!-- ai-section-version: 1 | source-hash: 23ffd616 -->
