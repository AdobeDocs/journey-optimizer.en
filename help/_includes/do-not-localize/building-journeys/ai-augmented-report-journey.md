---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to view and interpret the live report embedded in the journey canvas, covering the key profile flow metrics available for published journeys and journeys in Dry run mode.

**Intents:**
* View real-time journey performance metrics directly in the journey canvas
* Interpret Entered, Exited, Error, and Discarded profile counts for the journey and each activity
* Understand why profiles are discarded from a journey
* Troubleshoot missing or unexpected data in journey live reports
* Verify the required permission to access journey live reports

**Glossary:**
* **Live Reporting**: Real-time metrics displayed directly on the journey canvas covering the last 24 hours *(product-specific)*
* **Dry run mode**: A journey execution mode that simulates the journey without sending real messages, in which live reporting is also available *(product-specific)*
* **Discarded profiles**: Profiles that attempted to enter the journey but were rejected due to qualification mismatches, reentry restrictions, or identity issues *(product-specific)*
* **Exited (forced exit)**: Profiles that were removed from the journey while it was paused by a journey practitioner; always zero in Dry run mode *(product-specific)*

**Guardrails:**
* Live report data covers only the past 24 hours.
* Events are displayed with a minimum interval of two minutes from occurrence, typically within five minutes.
* The View journeys report permission is required to see live report data.
* Reporting data is only available for published journeys or journeys in Dry run mode; draft journeys generate no data.
* For Action activities, the Entered metric shows profiles passing through (not executed) in Dry run mode.
* The Exited (forced exit) metric is always zero in Dry run mode.

**Terminology:**
* Canonical name: Live report (journey canvas) — Acronym: none — variants: journey live report, in-canvas reporting
* Synonyms: "Entered profiles" = "profiles who entered the journey"
* Do not confuse: "Live report" ≠ "Journey global report" (live report is the last 24 hours in the canvas; global report covers a wider historical time range in the reporting UI)

**FAQ:**
* **Q: How current is the data shown in the live report?** — Events from the past 24 hours are shown, with a minimum display delay of two minutes and typically within five minutes.
* **Q: Why can I not see any data in my journey live report?** — Check that you have the View journeys report permission, that the journey is published (not in draft), and that the journey name matches the name in the reporting dataset.
* **Q: What causes profiles to be discarded?** — Discards can occur due to audience qualification verb mismatches, reentry policy violations on recurring or event-triggered journeys, or missing/mismatched identity namespace on Read Audience activities.
* **Q: Is the live report available during Dry run mode?** — Yes; live reporting is available for both published live journeys and journeys running in Dry run mode.
* **Q: What does the Entered metric mean for Action activities in Dry run mode?** — It indicates profiles passing through the activity, since actions are not actually executed in Dry run mode.

+++
