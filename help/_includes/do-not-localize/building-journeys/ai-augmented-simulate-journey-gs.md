---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page introduces the Journey Simulation feature in Adobe Journey Optimizer, explaining how it differs from Test mode, which journey types it supports, how to launch a simulation, how **[!UICONTROL Optimize]** activity methods and other decisioning elements behave during a simulation, and what its node-level, functional, and quantitative limitations are.

**Intents:**
* Understand the difference between Simulation and Test mode for validating journeys
* Launch a Simulation session for a batch, unitary, or mixed journey type
* Identify which journey nodes block or restrict Simulation from running
* Determine how **[!UICONTROL Optimize]** activity methods (**[!UICONTROL Targeting rule]**, **[!UICONTROL Experiment]**, **[!UICONTROL Percentage split]**, **[!UICONTROL Time condition]**, **[!UICONTROL Date condition]**, **[!UICONTROL Profile cap]**) behave during Simulation
* Determine which decisioning elements (offer eligibility, eligibility rule or audience, ranking) are supported during Simulation
* Determine which features are unsupported during Simulation (e.g., consent, frequency capping, STO)
* Plan around quantitative guardrails such as maximum simulated users per sandbox
* Decide whether to use Quick simulation or Manual simulation based on testing needs

**Glossary:**
* **Simulated users**: Temporary profile-like entities created for Simulation. Sending a simulated user triggers a real message send, which can currently result in a persistent profile being created in Adobe Experience Platform *(product-specific)*
* **Simulation**: A journey state (alongside Draft, Test mode, and Live) used for testing with simulated users rather than persistent test profiles *(product-specific)*
* **Journey Agent**: The AI component that generates simulated users, event values, and test settings during Quick simulation and AI-assisted Manual simulation *(product-specific)*
* **Quick simulation**: An automated end-to-end simulation run that generates users and events with minimal manual input *(product-specific)*
* **Manual simulation**: A step-by-step simulation mode where users and events are created and triggered individually *(product-specific)*
* **[!UICONTROL Experiment]** (Path Experimentation): An **[!UICONTROL Optimize]** activity method whose eligibility and allocation the Journey Agent evaluates against the simulated user's profile attributes to select the branch *(product-specific)*

**Guardrails:**
* Requires at least one of: **Simulate journeys**, **Publish journeys**, or **Approve and Publish journeys** permissions
* AI-powered simulation features require the **Generate Content** permission from the AI Assistant capability
* Maximum 20 simulated users per Send all or Trigger selected events batch
* Maximum 50 simulated users per AI generation request
* Maximum 100 unique simulated users per single simulation run
* Maximum 20 journeys running Simulation simultaneously in one sandbox
* Maximum 2,000 active simulated users in one sandbox at a time
* Business event-triggered journeys cannot be simulated
* Supplemental ID journeys with multiple re-entrance enabled cannot be simulated
* Consent policies, frequency capping, opt-out, STO, and quiet hours are not evaluated during Simulation
* Simulated users must not contain real customer data (not GDPR-compliant)

**Terminology:**
* Canonical name: Simulation — Acronym: none — variants: Journey Simulation, Simulation mode
* Canonical name: Simulated users — Acronym: none — variants: test users (in UI labels)
* Canonical name: **[!UICONTROL Experiment]** — variants: Path Experimentation
* Synonyms: "Simulation" = "Simulation mode"; "simulated users" = "test users" (UI label only)
* Do not confuse: "Simulation" ≠ "Test mode" (Test mode uses persistent AEP test profiles; Simulation uses temporary simulated users)
* Do not confuse: **[!UICONTROL Targeting rule]** ≠ **[!UICONTROL Experiment]** (both are **[!UICONTROL Optimize]** activity methods, but the Journey Agent evaluates a configured rule for **[!UICONTROL Targeting rule]** versus eligibility and allocation for **[!UICONTROL Experiment]**)

**FAQ:**
* **Q: What permissions do I need to use Simulation?** — You need at least one of: Simulate journeys, Publish journeys, or Approve and Publish journeys. AI features additionally require Generate Content permission from the AI Assistant capability.
* **Q: How does Simulation differ from Test mode?** — Simulation uses temporary simulated users created on the fly, generally without pre-created profiles in Adobe Experience Platform; Test mode uses persistent profiles explicitly flagged as test profiles in AEP. Sending a simulated user still triggers a real message send, which can result in a persistent profile being created.
* **Q: Can I simulate a journey that starts with a Business Event?** — No. Journeys triggered by a Business Event cannot be run in Simulation.
* **Q: Are the Targeting rule and Experiment methods of the Optimize activity supported in Simulation?** — Yes. The Journey Agent evaluates the configured rule for Targeting rule, or the eligibility and allocation for Experiment (Path Experimentation), against the simulated user's profile attributes to select the branch.
* **Q: Are decisioning elements such as offer eligibility and ranking supported during Simulation?** — Yes. Offer eligibility, eligibility rule, eligibility audience, and ranking by offer priority, formula, or AI Model — Auto are supported. Ranking by AI Model — Personalization is also supported, though returned offers may vary between simulation runs.
* **Q: How many simulated users can I test in a single simulation run?** — Up to 100 unique simulated users per run; each Send all action is capped at 20 users at once.
* **Q: Are consent policies enforced during Simulation?** — No. Consent policy evaluation, frequency capping, opt-out management, and quiet hours are all not evaluated during Simulation.
* **Q: What happens if my journey has more than 50 paths during AI generation?** — The Journey Agent randomly selects paths to produce a maximum of 50 simulated users.

+++

<!-- ai-section-version: 2 | source-hash: 7ccf8cd3 -->
