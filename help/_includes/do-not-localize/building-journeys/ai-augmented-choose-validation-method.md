---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page compares the three journey validation methods in Adobe Journey Optimizer — Journey Simulation, Journey Test mode, and Journey Dry run. It provides a one-question quick pick, a decision guide, a quick-comparison table, and a list of common mistakes to help users choose the right one for their current stage of building a journey.

**Intents:**

* Choose the correct validation method for a given stage of journey building
* Compare Journey Simulation, Journey Test mode, and Journey Dry run side by side
* Understand when to use Journey Simulation for fast iteration without real test profiles
* Understand when to use Journey Test mode for step-by-step manual validation with real test profiles
* Understand when to use Journey Dry run for a final pre-launch check against production data
* Understand which validation methods send real messages or contact real customers
* Avoid common mistakes when picking or using a validation method

**Glossary:**

* **Journey Simulation**: A validation method that uses temporary simulated users, manually created or auto-generated, to test a journey without needing real AEP test profiles. *(product-specific)*
* **Journey Test mode**: A validation method that uses persistent AEP test profiles, flagged in Real-Time Customer Profile, to manually walk through a draft journey's branch and message logic. *(product-specific)*
* **Journey Dry run**: A publication mode that runs a journey against real production audience data without contacting customers or updating profile data; action nodes are bypassed. *(product-specific)*
* **Simulation Agent**: The mechanism that automatically generates test events and matches them to simulated users during Journey Simulation. *(product-specific)*

**Guardrails:**

* Journey Test mode is only available for draft journeys that use a namespace, and supports a maximum of 100 test profiles per session
* Journey Test mode events can only be fired from the interface, not from external systems via API
* Journey Test mode sends real messages to test profiles' real inboxes using the production delivery pipeline
* Disabling Journey Test mode removes all profiles that entered the journey and clears its reporting
* Journey Simulation does not evaluate exit criteria, consent policies, frequency/journey capping, opt-out/suppression, or quiet hours
* Journey Simulation's custom actions and external data source calls are real, not mocked
* Journey Simulation sends real messages to the execution addresses (email, phone, push token) configured on the simulated users, using the same delivery pipeline as production
* Unlike Journey Simulation, Journey Dry run never sends real messages
* Journey Dry run is currently a Limited Availability feature, being rolled out globally over time
* Journey Dry run bypasses action nodes (email, SMS, custom actions) but still routes profiles through branches and nodes using real production data

**Terminology:**

* Canonical name: Journey Simulation — variants: simulate, simulation mode
* Canonical name: Journey Test mode — variants: Test mode, journey testing, test your journey
* Canonical name: Journey Dry run — variants: dry run, dry run mode
* Do not confuse: Journey Simulation (temporary simulated users, no AEP test profiles needed, sends real messages to the simulated users' configured execution addresses) ≠ Journey Test mode (persistent AEP test profiles, sends real messages to those profiles' real inboxes) ≠ Journey Dry run (real production audience data, no contact, no profile update, action nodes bypassed, never sends real messages)

**FAQ:**

* **Q: Which validation method should I use while I am still designing a journey?** — Use Journey Simulation; it needs no real test profiles and runs in seconds, making it ideal for fast iteration.
* **Q: Does Journey Simulation send real messages?** — Yes. Simulation delivers real messages to the execution addresses (email, phone, push token) configured on the simulated users, often the tester's own address. It uses the same delivery pipeline as production, but it does not contact real customers or update live profile data.
* **Q: Does Journey Test mode send real emails or SMS?** — Yes. Journey Test mode delivers real messages to the actual inboxes of your test profiles, using the same delivery pipeline as production. It does not contact real customers, but the messages themselves are real.
* **Q: Does Journey Dry run send any messages?** — No. Dry run bypasses action nodes such as email, SMS, and custom actions, so profiles flow through the journey logic without any message being sent.
* **Q: I need to validate a new branch quickly before a deadline. Which method fits?** — Journey Simulation; it generates simulated users on demand (or reuses ones saved to the inventory) instead of requiring you to pre-create and wait for real test profiles.
* **Q: Is Journey Dry run available to everyone?** — It is currently a Limited Availability feature being rolled out globally over time; check availability for your organization.
* **Q: Can I fire Journey Test mode events from an external system?** — No; in Journey Test mode, events can only be fired from the interface, not from external systems via API.

+++
