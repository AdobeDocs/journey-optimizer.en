---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page introduces the Journey Optimizer journey designer canvas, explaining how to build multi-step journeys by dragging and dropping events, orchestration, and action activities from the palette.

**Intents:**

* Navigate the journey designer interface (palette, canvas, toolbar, activity configuration pane)
* Add events, orchestration activities, and action activities to a journey canvas
* Configure a fallback alternative path for Condition and Action activities on timeout or error
* Copy and paste activities within the same journey or across different journeys in the same instance
* Start a journey using an event trigger or a Read Audience entry point

**Glossary:**

* **Palette**: The left-hand panel in the journey designer listing all available events, orchestration, and action activities for drag-and-drop onto the canvas *(product-specific)*
* **Canvas**: The central design area of the journey designer where activities are placed, connected, and configured *(product-specific)*
* **Activity configuration pane**: The right-hand panel that opens when an activity is selected on the canvas, used to fill in activity settings *(product-specific)*
* **Journey Fragments**: Reusable sets of pre-built journey nodes that can be inserted directly into the canvas to avoid rebuilding common logic *(product-specific)*
* **Reaction event**: An event activity placed after a message to branch the journey based on recipient tracking interactions (open, click) *(product-specific)*

**Guardrails:**

* Actions, conditions, wait activities, and reaction events cannot be placed as the first step in a new journey.
* Copy/paste is only supported within the same instance; cross-instance copy/paste is not supported.
* You cannot copy/paste an event into a destination journey that uses a different namespace.
* Pasted activities from a different sandbox may reference data that does not exist in the destination journey.
* Only event and wait activities can be set in parallel; other activity types cannot run in parallel.
* Alternative paths (timeout/error fallback) are available only for Condition and Action activities.

**Terminology:**

* Canonical name: Journey Designer — Acronym: none — variants: journey canvas, orchestration canvas
* Synonyms: "palette" = "activity panel"; "canvas" = "design area"
* Do not confuse: "events" (trigger journey entry or branching) ≠ "actions" (what happens to the customer, e.g. send a message)

**FAQ:**

* **Q: How do profiles enter a journey?** — Profiles enter either unitarily in real time when a configured event is received, or in batch when a Read Audience activity triggers the journey.
* **Q: Can I add multiple events to a journey?** — Yes, you can add several events as long as they all use the same namespace.
* **Q: How do I define a fallback when an action fails?** — In the activity properties, enable the "Add an alternative path in case of a timeout or an error" option to add a fallback path after the activity.
* **Q: Can I copy activities from a read-only journey?** — Yes, you can copy activities from any journey regardless of its status, but you can only paste within the same instance.
* **Q: What is a Journey Fragment?** — A reusable set of pre-built journey nodes (e.g. eligibility checks, welcome sequences) that can be inserted directly onto the canvas to avoid rebuilding common logic from scratch.

+++
