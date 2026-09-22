---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page provides step-by-step instructions for running Quick simulation and Manual simulation in Adobe Journey Optimizer, including how to create and manage simulated users, trigger unitary events, override Wait durations, and interpret the Results log.

**Intents:**
* Run a Quick simulation to validate a journey end-to-end with minimal manual input
* Set up Manual simulation to control simulated user creation, event payloads, and wait overrides
* Create simulated users via AI generation, inventory browse, form entry, or JSON
* Trigger unitary events for simulated users during an active simulation session
* Review the Results log to identify errors and uncovered branches after a simulation run
* Reset or close a simulation session to start fresh or exit

**Glossary:**
* **Quick simulation**: An automated simulation mode that generates users and event values using the Journey Agent and runs the full journey with minimal manual steps *(product-specific)*
* **Manual simulation**: A step-by-step simulation mode where practitioners control user creation, event payloads, and timing individually *(product-specific)*
* **Simulated users**: Temporary profile-like entities used in Simulation. Sending a simulated user triggers a real message send, which can currently result in a persistent profile being created in Adobe Experience Platform *(product-specific)*
* **Journey Agent**: The AI component that generates simulated users and event payloads during AI-assisted simulation *(product-specific)*
* **Test settings**: The Simulation panel tab where Wait durations and execution addresses (email, phone, push token) can be overridden for the simulation run *(product-specific)*
* **Results log**: The execution log accessible from the Results tab showing per-activity outcomes, durations, and errors for each simulated user *(product-specific)*

**Guardrails:**
* Requires at least one of: Simulate journeys, Publish journeys, or Approve and Publish journeys permissions
* AI features (Quick simulation, Generate with AI, Generate event values) require the Generate Content permission from the AI Assistant capability
* For event-triggered journeys, the per-user Send icon is not available; entry is triggered through the Test events section
* Wait duration overrides and execution address settings are only shown if the journey includes Wait or Channel activities
* Channel proofs and custom actions or external data sources can execute real outbound calls during Simulation; use non-production contact points and avoid real customer PII in simulated users
* Errors in the Results log require leaving Simulation, fixing the journey, and re-running before publishing

**Terminology:**
* Canonical name: Quick simulation — Acronym: none — variants: none
* Canonical name: Manual simulation — Acronym: none — variants: none
* Canonical name: Simulated users — Acronym: none — variants: test users (UI label in Test users list)
* Synonyms: "Send all" = trigger all listed simulated users into the journey simultaneously
* Do not confuse: "Reset simulation" ≠ "Close simulation" — Reset clears all data and settings; Close merely exits the current session

**FAQ:**
* **Q: What is the difference between Quick simulation and Manual simulation?** — Quick simulation runs the entire journey automatically using AI-generated users and events; Manual simulation lets you create users and events step by step with full control over payloads and timing.
* **Q: Can I reuse simulated users across simulation sessions?** — Yes. Users saved to the inventory can be retrieved via Browse inventory in subsequent sessions.
* **Q: How do I override Wait activity durations during simulation?** — Open the Test settings tab and set a shorter duration, for example 10 seconds, so simulated users move through Wait nodes quickly.
* **Q: How do I trigger a unitary event for a specific simulated user?** — In the Test events section, click the edit icon next to the user to configure the event payload, then click the send icon on that row to trigger only that user's event.
* **Q: What do the Defined duration and Actual duration fields mean in the Results log for Wait activities?** — Defined duration is the live journey's configured wait time; Actual duration is the overridden test duration the simulated user actually spent on the Wait node.
* **Q: What should I do when errors appear in the Results log?** — Leave Simulation, apply the required fixes to the journey, then re-run Simulation until the run shows no errors before publishing.

+++
