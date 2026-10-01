---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to run Quick simulation and Manual simulation in Adobe Journey Optimizer to validate journey paths and review results using simulated users.

**Intents:**
* Run Quick simulation to validate a journey end to end with generated users and event values
* Set up Manual simulation to control simulated-user selection, send order, event payloads, and Wait overrides
* Create or add simulated users using AI generation, inventory, a form, or JSON
* Trigger unitary events for simulated users during an active simulation session
* Review the Results log to identify errors and uncovered branches after a simulation run
* Use Reset simulation to start a new run or Stop simulation to exit the current session

**Glossary:**
* **Quick simulation**: A simulation that runs end to end with generated users, event values, and default test settings, powered by the Journey Agent *(product-specific)*
* **Manual simulation**: A simulation run step by step, where you create simulated users, trigger them into the journey, define event payloads, and override Wait durations *(product-specific)*
* **Simulated users**: Temporary profile-like entities defined in Simulation settings. Sending one triggers a real message send; if an impacted dataset is profile-enabled, this can create a persistent profile in Adobe Experience Platform *(product-specific)*
* **Journey Agent**: The agent used to generate simulated users and event values or payloads during simulation *(product-specific)*
* **Test settings**: The tab used to override Wait activity durations during simulation *(product-specific)*
* **Results log**: The execution log, opened from the Results tab, that shows activity execution details, timestamps, branch decisions, and errors *(product-specific)*

**Guardrails:**
* For journeys starting with an Event, the per-user Send icon is not available; simulated-user entry is triggered by sending the event in Test events
* The Update values step appears only if the journey uses Waits or Channels; it lets you adjust Wait durations and execution addresses
* In simulation content preview, if simulated-user data was fetched before Update Profile runs, previewed values are pre-update throughout. If the data was fetched after the activity runs, for example after reloading the page, previewed values are post-update throughout, including in earlier email activities. A single preview does not show pre-update values before the activity and post-update values after it.
* When errors appear in the Results log, leave Simulation, apply the required journey changes, and run Simulation again until the run looks correct before publishing

**Terminology:**
* Canonical name: Quick simulation — Acronym: none — variants: none
* Canonical name: Manual simulation — Acronym: none — variants: none
* Canonical name: simulated users — Acronym: none — UI label: Test users is the list containing simulated users
* Send all sends every simulated user in the list into the journey
* Do not confuse: Reset simulation clears data from the current run, selected simulated users, defined event values, and other test settings so a new simulation can start from scratch; Stop simulation exits the current simulation session
* Do not confuse: simulated-user data fetched before Update Profile runs produces pre-update preview values throughout; data fetched after it runs, for example after reloading the page, produces post-update values throughout, including in earlier email activities. One preview does not mix pre-update and post-update values.

**FAQ:**
* **Q: What is the difference between Quick simulation and Manual simulation?** — Quick simulation runs the journey end to end with generated users, event values, and default test settings; Manual simulation lets you create simulated users, trigger them into the journey, define event payloads, and override Wait durations.
* **Q: Why does content preview show the same profile attribute value before and after Update Profile?** — Previewed values depend on when simulated-user data was last fetched. Data fetched before the activity runs shows pre-update values throughout; data fetched after it runs, for example after reloading the page, shows post-update values throughout, including in earlier email activities.
* **Q: Can I reuse simulated users across simulation sessions?** — Yes. Users saved to the inventory can be retrieved with Browse inventory in subsequent sessions.
* **Q: How do I override Wait activity durations during simulation?** — Open the Test settings tab and set a shorter duration, for example 10 seconds, so simulated users move through Wait activities quickly.
* **Q: How do I trigger a unitary event for a specific simulated user?** — In Test events, configure the user's event payload with the edit icon, then select the send icon on that user's row to trigger only that user's event.
* **Q: What do the Defined duration and Actual duration values mean in the Results log for Wait activities?** — Defined duration is the duration specified on the Wait activity for the published journey; Actual duration is the elapsed time the simulated user remained on the Wait activity, set from the Test settings tab.
* **Q: What should I do when errors appear in the Results log?** — Leave Simulation, apply the required journey changes, and run Simulation again before publishing.

+++

<!-- ai-section-version: 1 | source-hash: 9a8ee7f0 -->
