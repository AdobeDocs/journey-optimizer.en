---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to create an Orchestrated campaign in Adobe Journey Optimizer and configure its execution schedule to run it immediately, at a specific date and time, or on a recurring basis.

**Intents:**

* Create an Orchestrated campaign and define its properties (name, description, merge policy, tags, custom metadata).
* Choose the Orchestration - Marketing and transactional campaign type.
* Configure a campaign execution schedule using Once, Daily, Several times a day, Weekly, or Monthly frequency.
* Define a validity period to restrict the campaign's execution to a limited time window.
* Preview upcoming execution dates and times for a recurring schedule before activation.
* Proceed to orchestrate the campaign's activities after properties and schedule are configured.

**Glossary:**

* **Orchestrated campaign**: a campaign created from the Orchestration tab of the Campaigns menu, configured with a schedule to control when it starts and how often it runs *(product-specific)*
* **Orchestration - Marketing and transactional**: the campaign type selected when creating an Orchestrated campaign; determines that each message's marketing or transactional status is chosen when adding a channel activity *(product-specific)*
* **Merge policy**: a setting tied to each audience in Adobe Experience Platform that defines how profile information is combined to form a merged profile; only audiences based on the same merge policy as selected are available in the Read audience activity *(product-specific)*
* **Validity period**: a setting that defines a specific start and end date restricting the campaign's execution to a limited time window *(product-specific)*
* **Triggered by a signal**: a scheduling option where the campaign starts when called from the REST API or from another Orchestrated campaign's End activity, instead of running on a schedule *(product-specific)*
* **Preview launch times**: a button for recurring schedules that previews the exact upcoming execution dates and times based on the current configuration *(product-specific)*

**Guardrails:**

* Do not schedule an Orchestrated campaign to run more than every 15 minutes, as it may impede overall system performance and create blocks in the database (recommended).
* The recurring delivery activity does not allow you to define a schedule; use a Scheduling option and set the execution frequency for recurring messages instead.
* Custom metadata fields for Orchestrated campaigns are available in Limited Availability; contact your Adobe representative to gain access.
* Fields marked with an asterisk in the Metadata fields section are required.
* By default, Orchestrated campaigns start when activated manually and end once their associated activities have been executed, unless a schedule is defined.
* For recurring campaigns, if the initial scheduled time has already passed, the campaign rolls over to the next available time slot according to its recurrence rules.

**Terminology:**

* Canonical name: Orchestrated campaign — variants: campaign
* Do not confuse: "Once" frequency (runs the campaign a single time at a specified date and time) ≠ "Triggered by a signal" (starts when called from the REST API or from another Orchestrated campaign's End activity)
* Do not confuse: "Daily recurrence" (frequency applied within Daily or Monthly scheduling) ≠ "Weekly" frequency (a separate top-level scheduling option with its own Frequency and Daily recurrence settings)

**FAQ:**

* **Q: What campaign type is used to create an Orchestrated campaign?** — The Orchestration - Marketing and transactional campaign type.
* **Q: How do I assign a merge policy?** — Select a Merge policy in the campaign properties; only audiences based on that same merge policy are available in the Read audience activity.
* **Q: How often can an Orchestrated campaign be scheduled to run?** — Do not schedule it to run more than every 15 minutes, as this may impede overall system performance and create blocks in the database.
* **Q: Can the recurring delivery activity define its own schedule?** — No, the recurring delivery activity does not allow you to define a schedule; use a Scheduling option and set the execution frequency instead.
* **Q: What happens if a recurring campaign's initial scheduled time has already passed?** — The campaign rolls over to the next available time slot according to its recurrence rules.
* **Q: How can I start a campaign without using a schedule?** — Set it to be Triggered by a signal so it starts when called from the REST API or from another Orchestrated campaign's End activity.

**Related pages:**

* For adding a channel activity and choosing marketing or transactional status: channel activity (orchestrated/activities/channels.md)
* For working with Adobe Experience Platform Unified Tags on a campaign: Learn how to work with tags (start/search-filter-categorize.md)
* For details on custom metadata fields: Learn more on custom metadata (administration/custom-metadata.md)
* For triggering a campaign using a signal instead of a schedule: Learn how to trigger an Orchestrated campaign using a signal (orchestrated/trigger-orchestrated-campaign.md)
* For orchestrating the campaign's activities after setup: Learn how to orchestrate campaign activities (orchestrated/orchestrate-activities.md)

**Personas:**

* **marketer:** Can create an Orchestrated campaign from the Orchestration tab and select the Orchestration - Marketing and transactional campaign type. Can define the campaign name, description, merge policy, tags, and custom metadata fields in the campaign properties. Can schedule the campaign using Once, Daily, Several times a day, Weekly, or Monthly frequency, and preview launch times for recurring schedules. The page states that an Orchestrated campaign should not be scheduled to run more than every 15 minutes. Where: "Schedule the campaign".

**Onboarding:**

* **Level:** Beginner
* **First minimal step:** Browse to the Campaigns menu and select the Orchestration tab.
* **Success check:** You can preview launch times to see the exact upcoming execution dates and times based on the current configuration.
* **Next:** Configuring the campaign to start when it receives a signal instead of running on a schedule: Trigger an Orchestrated campaign using a signal (orchestrated/trigger-orchestrated-campaign.md); Orchestrating the campaign's activities after configuring settings and schedule: Create Orchestrated campaigns with Adobe Journey Optimizer (orchestrated/orchestrate-activities.md)

+++

<!-- ai-section-version: 1 | source-hash: b4d0c56b -->
