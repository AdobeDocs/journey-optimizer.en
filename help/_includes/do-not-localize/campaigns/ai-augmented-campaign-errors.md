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
* Know what to note and whom to contact when an error persists after the listed steps

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
* The audience cannot be changed once the campaign is activated (CJMCMP-2025-400). For a recurring Action campaign, click **[!UICONTROL Modify campaign]** to create a new version, or duplicate the campaign, then change the audience.
* Audiences and attributes from audience composition, federated audience composition, or CSV uploads cannot be used with Healthcare Shield or Privacy and Security Shield (CJMCMP-2075, 2077, 2078, 2080, 2081, 2082, 2083).
* Priority can only be in the range of 0-100 (hard limit), and is disabled for transactional campaigns (CJMCMP-2074-400).
* Rapid delivery mode cannot be used with a recurring schedule, a headless campaign, or a campaign that has an experiment. It is limited to audiences of up to 30M profiles (hard limit), and does not accept audiences from audience composition.
* An experiment can have only one holdout, and a campaign can have only one experiment.
* A custom allocation requires a percentage for each treatment (CJMCMP-2040-400), and a treatment percentage cannot be set with a uniform allocation (CJMCMP-2039-400).
* Surfaces are deprecated: select a channel configuration instead (CJMCMP-2119-400).

**Terminology:**

* Canonical name: Campaign errors — variants: campaign errors and warnings
* Acronym: OLAC — Object level access control
* Do not confuse: "error" (a code with a status other than 200) ≠ "warning" (a code with the status 200)

**FAQ:**

* **Q: What do the parts of a campaign error code mean?** — Campaign errors use the prefix CJMCMP, followed by an error number and an HTTP status. Codes with the status 200 are warnings.
* **Q: Why can I not activate the campaign because "The selected audience has not been evaluated yet."?** — CJMCMP-2060-200 is a warning: wait until the audience is evaluated, then activate the campaign.
* **Q: Why can I not change the audience of the campaign?** — CJMCMP-2025-400: the audience cannot be changed once the campaign is activated. For a recurring Action campaign, click **[!UICONTROL Modify campaign]** to create a new version, or duplicate the campaign, then change the audience.
* **Q: Why is my audience refused with Healthcare Shield or Privacy and Security Shield?** — Audiences and attributes from audience composition, federated audience composition, or CSV uploads cannot be used with them. Select another audience.
* **Q: Why does "The message has not been published" appear?** — CJMCMP-2202-400: publish the message, then activate the campaign.
* **Q: Why does "The selected schedule is invalid and will never be fired." appear?** — CJMCMP-2120-400: set a start date in the future, and an end date after the start date.
* **Q: Why does "The campaign is not approved" appear?** — CJMCMP-2121-400: request approval, wait for it, then activate the campaign.
* **Q: Why can I not turn on rapid delivery mode?** — CJMCMP-2310-400 (recurring schedule): turn off rapid delivery, or change the schedule so that it does not recur. CJMCMP-2311-400 (headless campaign): turn off rapid delivery, or use a campaign that is not headless. CJMCMP-2312-400 (campaign with an experiment): turn off rapid delivery, or remove the experiment. CJMCMP-2030-400 (audience larger than 30M): select an audience of up to 30M profiles, or turn off rapid delivery. CJMCMP-2041-400 (audience from audience composition): select another audience, or turn off rapid delivery.
* **Q: What do I do if the error persists after the listed steps?** — Note the error code, the message, the request ID, and the campaign, journey, or activity concerned, and keep the logs or screenshots. Then contact your administrator for a permission or access error, or contact Adobe Support with these details. For all the support options, see the Getting support section of the error codes reference.

**Troubleshooting:**

* CJMCMP-2028-400, "Permission denied for the audience" — Check whether the audience carries an access label that your role does not include, and ask your administrator to add that label to your role. If access cannot be granted, select another audience.
* CJMCMP-2031-400, "You do not have permissions to perform this action. Contact your administrator to set OLAC permissions, and try again" — Check the access labels set on the campaign with **[!UICONTROL Manage access]**, and ask your administrator to add a matching label to your role.
* CJMCMP-2061-400, "You do not have required permissions to perform this action. Contact your administrator to grant you access." — Check that your role includes the permission for this action, such as **[!DNL Manage campaigns]** to edit or **[!DNL Publish campaigns]** to publish, and the access labels set on the campaign, and ask your administrator to add what is missing.
* CJMCMP-2052-400, "The draft version has already been created" — A draft version of the campaign already exists. Open it from the campaign list with **[!UICONTROL Open draft version]**.
* CJMRT-150001-400, "The schedule will never fire for {triggerExpression}. Please update." — The schedule never produces an execution. Update the start date, end date or frequency so that at least one execution is in the future. This code uses the CJMRT prefix.
* CJMRT-150002-400, "The End time {endTime} must be set after the Start time {startTime}" — Set an end time later than the start time. This code uses the CJMRT prefix.
* CJMCMP-2024-400, "A new profile is not allowed for the provisioned campaign" — Creating new profiles is not allowed for this campaign. Turn off the **[!UICONTROL Create new profiles]** option and select an audience of existing profiles.
* CJMCMP-2012-400, "The campaign already has an experiment" — A campaign can have only one experiment. Edit the existing experiment.
* CJMCMP-2009-400, "The campaign status doesn't allow to create an experiment" — The status of the campaign does not allow creating an experiment. Create the experiment while the campaign is in draft.
* CJMCMP-2059-400, "The experiment is not allowed" — The experiment is not allowed for this campaign. Edit the existing experiment, or create the experiment while the campaign is in draft.
* CJMCMP-2058-400, "The experiment dimension entered must be an URL" — The dimension must be a URL. Enter a URL as the dimension.

**Related pages:**

* Audience: Define the Action campaign audience (campaigns/campaign-audience.md)
* Action configuration: Configure the campaign action (campaigns/campaign-action.md)
* Rapid delivery mode: Enable Rapid delivery mode (campaigns/campaign-action.md)
* Schedule: Schedule the Action campaign (campaigns/campaign-schedule.md)
* Activation: Review and activate the campaign (campaigns/review-activate-campaign.md)
* Content experiments: Create a content experiment (content-management/content-experiment.md)
* Permissions and object-level access: Object level access control (administration/object-based-access.md)
* Access labels on audiences: Attribute-based access control (administration/attribute-based-access.md)
* Other error code prefixes: Error codes reference (building-journeys/error-codes-reference.md)
* Support options when an error persists: Getting support (building-journeys/error-codes-reference.md#getting-support)
* Contacting Adobe Support: Support ticket guidelines (start/user-interface.md#support-ticket-guidelines)

+++

<!-- ai-section-version: 1 | source-hash: f3b72432 -->
