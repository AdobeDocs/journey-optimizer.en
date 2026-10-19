---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to browse, filter, view (list and calendar), duplicate, and perform bulk operations on journeys from the Journey Optimizer dashboard.

**Intents:**

* Browse and search journeys from the Overview and Browse tabs
* Filter journeys by status, type, version, tags, creation date, or publication date
* Switch between list view and calendar view to visualize journey schedules
* Add and manage external calendars by uploading CSV files
* Duplicate an existing journey to reuse its settings
* Apply bulk operations to multiple selected journeys from the bulk action bar: add to package, move to folder, edit tags, manage access, delete, pause, or resume

**Glossary:**

* **Journey dashboard**: The main journeys interface with an Overview tab showing key metrics and a Browse tab listing all journeys. *(product-specific)*
* **Discard rate**: The ratio of profiles not eligible to enter the journey (e.g., due to incorrect namespace or reentrance rules) compared to total profiles who attempted entry over the last 24 hours. *(product-specific)*
* **Journeys calendar view**: A visual weekly calendar representation of live and scheduled journeys, accessible by clicking the calendar icon in the journeys list. *(product-specific)*
* **Bulk action bar**: The action bar that appears at the bottom of the journeys list once one or more journeys are selected, offering add to package, move to folder, edit tags, manage access, delete, pause, and resume. *(product-specific)*
* **Bulk pause/resume**: The pause and resume operations available from the bulk action bar, limited to Live journeys (pause) or Paused journeys (resume), up to 10 per operation. *(product-specific)*

**Guardrails:**

* Dashboard metrics refresh every 30 minutes and only when new data is available; they cover the last 24 hours only
* Draft journeys and journeys in test mode are not shown in the calendar view
* Bulk pause/resume is limited to 10 journeys per operation
* The Resume button is only active when Paused journeys are selected; the Pause button is only active when Live journeys are selected
* The calendar displays journeys as 1-hour timespans regardless of actual send or completion time

**Terminology:**

* Canonical name: Journey dashboard — Acronym: none — variants: journeys list, journeys overview
* Synonyms: "Browse tab" = "journeys list"
* Do not confuse: "Discard rate" ≠ "Error rate" — Discard rate counts profiles ineligible to enter; Error rate counts profiles that entered but encountered a processing error
* Note: Add to package, move to folder, edit tags, manage access, and delete are shared with the Campaigns, Fragments, and Templates lists; pause and resume are journey-specific

**FAQ:**

* **Q: Where can I see key journey performance metrics at a glance?** — On the Overview tab of the Journey dashboard, which shows profiles processed, live journeys, error rate, and discard rate for the last 24 hours.
* **Q: How do I find journeys that use a specific event or action?** — Use the Activity filters and Data filters in the journey list to display journeys referencing a specific event, field group, or action.
* **Q: Can I pause multiple journeys at once?** — Yes; select multiple Live journeys in the list and click the Pause button in the bottom bar. Up to 10 journeys can be paused per operation.
* **Q: How do I add external events to the journey calendar?** — Click the calendar add icon, then drag and drop a CSV file with event name, start date, and end date columns; uploaded events are visible to all users in the organization.
* **Q: Why does the calendar show a journey as 1 hour even though it runs longer?** — The calendar displays all journeys as 1-hour timespans for visual consistency; this does not reflect actual send or completion time.
* **Q: What bulk operations can I perform on multiple journeys at once?** — Besides pause and resume, you can select multiple journeys and add them to a package, move them to a folder, edit their tags, manage their access, or delete them, using the bulk action bar at the bottom of the journeys list.

+++
