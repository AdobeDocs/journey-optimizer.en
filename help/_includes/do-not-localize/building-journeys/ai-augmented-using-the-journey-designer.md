---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to use the Journey Optimizer journey designer canvas to build a sequenced journey, use the new canvas tools, preview channel content, and copy or paste configured activities.

**Intents:**

* Navigate the journey designer palette, canvas, toolbar, and activity configuration pane.
* Add events, orchestration activities, and action activities to a journey.
* Use the new canvas experience to add activities, expand channel previews, select multiple activities, detach branches, and join branches.
* Preview channel activity content on the canvas while designing, during a simulation, or in test mode.
* Start a journey from an event or a Read Audience activity.
* Copy and paste activities within the same instance.

**Glossary:**

* **Palette**: The left-hand side of the journey designer where available activities are sorted into Events, Orchestration, and Actions categories *(product-specific)*.
* **Canvas**: The central zone in the journey designer where activities are dropped and configured *(product-specific)*.
* **Activity configuration pane**: The right-hand pane that opens when an activity is selected on the canvas and contains the activity settings *(product-specific)*.
* **New journey canvas experience**: A canvas user interface built for complex use cases with performance, automatic layout, and guided authoring capabilities *(product-specific)*.
* **Content preview**: A canvas capability that renders channel activity content inline as thumbnails and opens a centered preview when a thumbnail is selected *(product-specific)*.
* **Simulation**: A context where content preview can reflect the selected test user, personalization values, and the path that user follows through the journey *(product-specific)*.
* **Test mode**: A context where content preview shows visible content for the journey being tested, but the content is not personalized for the targeted test profile *(product-specific)*.

**Guardrails:**

* Actions, the condition activity, the wait activity, and the reaction activity cannot be dropped on the canvas as the first step of a new journey.
* Content preview in test mode is visible but is not personalized for the test profile you target.
* Only event and wait activities can be set in parallel.
* Several events can be added to a journey only if they use the same namespace.
* Copy/paste across different tabs and browsers is supported only within the same instance.
* An event cannot be copied and pasted if the destination journey has an event that uses a different namespace.
* Pasted activities may reference data that does not exist in the destination journey.
* Copy/paste actions cannot be undone; pasted activities must be selected and deleted if they are no longer needed.

**Terminology:**

* Canonical name: journey designer. Variants used on the page: journey canvas, orchestration canvas, canvas.
* Synonyms: "Read Audience" = "Read Audiences".
* Do not confuse: "Simulation" content preview, which can reflect the selected test user and personalization values, is not the same as "test mode" content preview, where content is visible but not personalized for the targeted test profile.
* Do not confuse: "Events" trigger journey entry or movement, while "Actions" are what happens as a result of a trigger, such as sending a message.

**FAQ:**

* **Q: What does the Expand all toolbar icon do?** — It expands all channel activities to show a thumbnail preview of their content directly on the canvas, and each thumbnail can be opened in a fullscreen preview.
* **Q: Is content preview personalized in test mode?** — No. In test mode, the content is visible, but it is not personalized for the test profile you target.
* **Q: When is content preview personalized?** — During a simulation, content preview reflects the selected test user, including personalization values and the path that user follows through the journey.
* **Q: How can profiles enter a journey?** — Profiles can enter when a configured event is received or when a Read Audience activity triggers the journey.
* **Q: Can activities be copied between journeys?** — Yes. Activities can be copied and pasted in the same journey or a different journey, but copy/paste is supported only within the same instance.
* **Q: What can be done with multiple selected activities?** — Multiple selected activities can be copied, deleted, or saved as a journey fragment.

+++

<!-- ai-section-version: 1 | source-hash: 1272b125 -->
