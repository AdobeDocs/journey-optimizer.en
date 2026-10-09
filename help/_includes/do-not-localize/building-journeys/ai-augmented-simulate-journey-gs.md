---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page introduces **[!UICONTROL Simulation]** in Adobe Journey Optimizer, explaining how it differs from **[!UICONTROL Test mode]**, which journey types it supports, how to launch a simulation, how **[!UICONTROL Optimize]** activity methods and other decisioning elements behave during a simulation, and what its node-level, functional, and quantitative limitations are.

**Intents:**
* Understand the difference between Simulation and Test mode for validating journeys
* Launch a Simulation session for a batch or unitary journey type
* Identify which journey nodes block or restrict Simulation from running
* Determine how **[!UICONTROL Optimize]** activity methods (**[!UICONTROL Targeting rule]**, **[!UICONTROL Experiment]**, **[!UICONTROL Percentage split]**, **[!UICONTROL Time condition]**, **[!UICONTROL Date condition]**, **[!UICONTROL Profile cap]**) behave during Simulation
* Determine which decisioning elements (offer eligibility, eligibility rule or audience, ranking) are supported during Simulation
* Determine which features are unsupported during Simulation (e.g., consent, frequency capping, STO)

**Glossary:**
* **Simulated users**: Temporary profile-like entities created for Simulation. Sending a simulated user triggers a real message send; if an impacted dataset, such as feedback or tracking events, is profile-enabled, a persistent profile can be created in Adobe Experience Platform *(product-specific)*
* **Simulation**: A journey feature used for testing with simulated users rather than persistent test profiles *(product-specific)*
* **Journey Dry run**: A validation method that runs a journey against real production audience and segmentation data without contacting real customers or updating profile information *(product-specific)*
* **[!UICONTROL Experiment]** (Path Experimentation): An **[!UICONTROL Optimize]** activity method whose routing is handled by Decisioning, with random assignment that is non-deterministic per simulated user *(product-specific)*

**Guardrails:**
* The journey must be validated before entering **[!UICONTROL Simulation]**. Errors in the Alerts panel must be resolved and validation rerun before continuing.
* To use **[!UICONTROL Simulation]**, assign at least one of: **Simulate journeys**, **Publish journeys**, or **Approve and Publish journeys** permissions from the **[!UICONTROL Journeys]** capability; these permissions also allow users to create and manage simulated users without **[!UICONTROL Simulated Users]** permissions
* Managing simulated users without **[!UICONTROL Simulation]** requires **Manage Simulated Users** or **View Simulated Users** from the **[!UICONTROL Simulated Users]** capability
* AI-powered simulation features (**[!UICONTROL Quick simulation]**, AI-generated users, and **[!UICONTROL Generate event values]**) require **[!UICONTROL Generate Content]** from the **[!UICONTROL AI Assistant]** capability
* Maximum 20 simulated users per **[!UICONTROL Send all]** or **[!UICONTROL Trigger selected events]** batch (hard limit)
* Maximum 50 simulated users per AI generation request (hard limit)
* Maximum 100 unique simulated users per single simulation run (hard limit); with a supplemental ID on a Read audience journey, this counts total journey runs rather than unique users
* Maximum 20 journeys running **[!UICONTROL Simulation]** simultaneously in one sandbox (hard limit)
* Maximum 2,000 active simulated users in one sandbox at a time (hard limit)
* Journeys that start with a business event cannot be run in **[!UICONTROL Simulation]**
* Consent policies, frequency capping, and quiet hours are not evaluated during Simulation; opt-out management and STO are not evaluated or applied
* Simulated users are not GDPR-compliant persistent profiles; do not include real customer data in simulated users

**Terminology:**
* Canonical name: Simulation
* Canonical name: Simulated users
* Canonical name: **[!UICONTROL Experiment]** — variants: Path Experimentation
* Do not confuse: "Simulation" ≠ "Test mode" (Test mode uses persistent profiles flagged as test profiles in Adobe Experience Platform; Simulation uses temporary simulated users)
* Do not confuse: "Journey Simulation" ≠ "Journey Test mode" ≠ "Journey Dry run" (the three validation methods use different data and validation approaches)
* Do not confuse: **[!UICONTROL Targeting rule]** ≠ **[!UICONTROL Experiment]** (both are **[!UICONTROL Optimize]** activity methods, but AI evaluates the configured rule for **[!UICONTROL Targeting rule]**, whereas routing for **[!UICONTROL Experiment]** is handled by Decisioning)

**FAQ:**
* **Q: What permissions do I need to use Simulation?** — Assign at least one of: **Simulate journeys**, **Publish journeys**, or **Approve and Publish journeys** from the **[!UICONTROL Journeys]** capability. These permissions also let you create and manage simulated users; **[!UICONTROL Simulated Users]** permissions are not required. AI features additionally require **[!UICONTROL Generate Content]** from the **[!UICONTROL AI Assistant]** capability.
* **Q: How does Simulation differ from Test mode?** — Simulation uses temporary simulated users without pre-created profiles in Adobe Experience Platform; Test mode uses persistent profiles explicitly flagged as test profiles in Adobe Experience Platform. Sending a simulated user triggers a real message send; if an impacted dataset is profile-enabled, a persistent profile can be created.
* **Q: Can I simulate a journey that starts with a business event?** — No. Journeys that start with a business event cannot be run in **[!UICONTROL Simulation]**.
* **Q: Are the Targeting rule and Experiment methods of the Optimize activity supported in Simulation?** — **[!UICONTROL Targeting rule]** is evaluated by AI against the simulated user's profile attributes. For **[!UICONTROL Experiment]** (Path Experimentation), routing is handled by Decisioning and assignment is random and non-deterministic per simulated user.
* **Q: Are decisioning elements such as offer eligibility and ranking supported during Simulation?** — Yes. Offer eligibility, eligibility rule, and ranking by offer priority or formula are supported. Eligibility audience is supported when the audience is added to the simulated user's profile. **[!UICONTROL AI Model - Auto]** requires the necessary data in the configured dataset. **[!UICONTROL AI Model - Personalization]** considers the audience for ranking, not eligibility; returned offers may vary between simulation runs.
* **Q: How many simulated users can I test in a single simulation run?** — Up to 100 unique simulated users per run; with a supplemental ID on a Read audience journey, the limit counts total journey runs. Each **[!UICONTROL Send all]** action is capped at 20 users at once.

+++

<!-- ai-section-version: 2 | source-hash: 274b044e -->
