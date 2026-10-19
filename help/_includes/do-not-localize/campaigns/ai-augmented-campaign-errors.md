---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page lists the errors and warnings that [!DNL Adobe Journey Optimizer] returns when you configure, schedule, or activate a campaign, grouped by feature, with the cause and the fix for each error family.

**Intents:**

* Find the cause and the fix for an error or warning returned when configuring, scheduling, or activating a campaign
* Tell an error from a warning using the HTTP status of the code
* Fix audience, action and channel configuration, schedule and approval, rapid delivery, and content experiment errors
* Understand which audiences cannot be used with Healthcare Shield or Privacy and Security Shield

**Glossary:**

* **Error code**: Prefix CJMCMP, followed by an error number and an HTTP status, for example CJMCMP-2000-400 *(product-specific)*
* **Warning**: A code with the status 200 *(product-specific)*
* **Rapid delivery mode**: Option turned on for a push campaign
* **Holdout**, **treatment**, **allocation** (uniform or custom): Elements of a content experiment on a campaign
* **Error families, one per section of the page:**
* **Audience** (CJMCMP-2000, 2025, 2028, 2031, 2061, 2060, 2075, 2077, 2078, 2080, 2081, 2082, 2083, 2024): audience missing, audience that cannot be changed after activation, permission denied, audience not evaluated yet, audiences and attributes not available with Healthcare Shield or Privacy and Security Shield, new profile not allowed.
* **Action and channel configuration** (CJMCMP-2119, 2104, 2201, 2202, 2105, 2115, 2074): deprecated surface, missing or unpublished message, channel not allowed for the campaign type, priority range.
* **Schedule and approval** (CJMCMP-2017, 2120, 2309, 2121, 2052 and CJMRT-150001, 150002): missing or invalid schedule, end time before start time, schedule mismatch, campaign not approved, draft version already created.
* **Rapid delivery** (CJMCMP-2310, 2311, 2312, 2030, 2041): rapid delivery mode combined with an unsupported campaign or audience.
* **Content experiments** (CJMCMP-2019, 2036, 2037, 2038, 2039, 2040, 2058, 2012, 2009, 2059): missing treatment or success metric, more than one holdout, allocation percentage, dimension, experiment not allowed.

**Guardrails:**

* Codes with the status 200 are warnings.
* The audience cannot be changed once the campaign is activated (CJMCMP-2025-400). Create a new version of the campaign, or duplicate it, then change the audience.
* Audiences and attributes from audience composition, federated audience composition, or CSV uploads cannot be used with Healthcare Shield or Privacy and Security Shield (CJMCMP-2075, 2077, 2078, 2080, 2081, 2082, 2083).
* Priority can only be in the range of 0-100 (hard limit), and is not available for transactional campaigns (CJMCMP-2074-400).
* Rapid delivery mode cannot be used with a recurring campaign, a headless campaign, or a campaign with an experiment. It is limited to audiences of up to 30M profiles (hard limit), and does not accept audiences from audience composition.
* An experiment can have only one holdout, and a campaign can have only one experiment.
* A set percentage per treatment applies only with a custom allocation; do not set it with a uniform allocation.
* Surfaces are deprecated: select a channel configuration instead (CJMCMP-2119-400).

**Terminology:**

* Canonical name: Campaign errors — variants: campaign errors and warnings
* Acronym: OLAC — Object level access control
* Do not confuse: "error" (a code with a status other than 200) ≠ "warning" (a code with the status 200)

**FAQ:**

* **Q: What do the parts of a campaign error code mean?** — Campaign errors use the prefix CJMCMP, followed by an error number and an HTTP status. Codes with the status 200 are warnings.
* **Q: Why can I not activate the campaign because "The selected audience has not been evaluated yet."?** — CJMCMP-2060-200 is a warning: wait until the audience is evaluated, then activate the campaign.
* **Q: Why can I not change the audience of the campaign?** — CJMCMP-2025-400: the audience cannot be changed once the campaign is activated. Create a new version of the campaign, or duplicate it, then change the audience.
* **Q: Why is my audience refused with Healthcare Shield or Privacy and Security Shield?** — Audiences and attributes from audience composition, federated audience composition, or CSV uploads cannot be used with them. Select another audience.
* **Q: Why does "The message has not been published" appear?** — CJMCMP-2202-400: publish the message, then activate the campaign.
* **Q: Why does "The selected schedule is invalid and will never be fired." appear?** — CJMCMP-2120-400: set a start date in the future, and an end date after the start date.
* **Q: Why does "The campaign is not approved" appear?** — CJMCMP-2121-400: request approval, wait for it, then activate the campaign.
* **Q: Why can I not turn on rapid delivery mode?** — CJMCMP-2310, 2311 and 2312: it cannot be enabled for a recurring schedule, a headless campaign, or an experimental campaign. CJMCMP-2030-400 and CJMCMP-2041-400: the audience cannot be larger than 30M, and cannot come from audience composition.

**Troubleshooting:**

* CJMCMP-2052-400, "The draft version has already been created" — A draft version of the campaign already exists. Open it from the campaign list with **[!UICONTROL Open draft version]**.
* CJMRT-150001-400, "The schedule will never fire for {triggerExpression}. Please update." — The schedule never produces an execution, for example because its end date is in the past. Update the start date, end date or frequency so that at least one execution is in the future. This code uses the CJMRT prefix.
* CJMRT-150002-400, "The End time {endTime} must be set after the Start time {startTime}" — Set an end time later than the start time. This code uses the CJMRT prefix.
* CJMCMP-2024-400, "A new profile is not allowed for the provisioned campaign" — Creating new profiles is not allowed for this campaign. Turn off the option that creates profiles, and use an audience of existing profiles.
* CJMCMP-2012-400, CJMCMP-2009-400, CJMCMP-2059-400 — A campaign can have only one experiment, and an experiment cannot be created in every campaign status. Edit the existing experiment, or create the experiment while the campaign is in draft.
* CJMCMP-2058-400, "The experiment dimension entered must be an URL" — For clicks or page views, the dimension must be a URL.

**Related pages:**

* Audience: Define the Action campaign audience (campaigns/campaign-audience.md)
* Action configuration: Configure the campaign action (campaigns/campaign-action.md)
* Rapid delivery mode: Enable Rapid delivery mode (campaigns/campaign-action.md)
* Schedule: Schedule the Action campaign (campaigns/campaign-schedule.md)
* Activation: Review and activate the campaign (campaigns/review-activate-campaign.md)
* Content experiments: Create a content experiment (content-management/content-experiment.md)
* Permissions and object-level access: Object level access control (administration/object-based-access.md)
* Other error code prefixes: Error codes reference (building-journeys/error-codes-reference.md)

+++

<!-- ai-section-version: 1 | source-hash: d2147801 -->
