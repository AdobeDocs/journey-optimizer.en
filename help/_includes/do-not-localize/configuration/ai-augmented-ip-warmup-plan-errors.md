---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** The page gives the cause and the fix for the errors that [!DNL Adobe Journey Optimizer] returns when you upload an IP warmup plan, define its phases and runs, activate runs, or when a run fails, grouped into five families: plan file, channel configuration and campaigns, phases and domain groups, runs and activation, and run failures.

**Intents:**

* Identify an IP warmup error from its code: the prefix **CJMRT**, the error number, and the HTTP status.
* Fix an error returned when you upload the Excel file of an IP warmup plan.
* Select a valid channel configuration and a valid campaign for an IP warmup plan.
* Fix an error on the phases, the domain groups, or the runs of a plan, including when you delete or split a phase or a run.
* Understand why a run cannot be activated, and what to do when an activated run is cancelled or fails.

**Glossary:**

* **CJMRT** *(product-specific)*: prefix of the IP warmup error codes, followed by an error number and an HTTP status, for example **CJMRT-180021-409**.
* **IP warmup plan**: defined in an Excel file (.xls or .xlsx) with the **[!UICONTROL Warmup Plan]** sheet and the **[!UICONTROL Custom Domain Group]** sheet, and made of phases and runs.
* **Phase** and **run**: a plan is divided into phases, and a phase contains runs. A run can be activated, duplicated, or split to a new phase.
* **Domain group**: a group of domains. The domain groups are global or custom (defined in the **[!UICONTROL Custom Domain Group]** tab of the plan). **[!UICONTROL All]** is a domain group that you can select in a phase.
* **Channel configuration**: the page calls it a "channel surface" in several error messages. It must be active, have the email channel, be of the marketing type, and have domains and IP pools associated.

**Guardrails:**

* Supported plan file formats: .xls and .xlsx.
* A run must be activated at least 12 hours before its send time (hard limit) (**CJMRT-180036-400**, **CJMRT-180039-403**).
* A run can be activated only after all the previous runs have ended (**CJMRT-180038-403**).
* The number of targeted profiles must be greater than zero, and the 'Last engagement' period cannot be negative.
* The retry period must be within the range shown in the message, in minutes (**CJMRT-180022-400**).
* A domain must belong to only one domain group of the plan.
* If you select the **[!UICONTROL All]** domain group, do not select other groups.
* Do not include global domain groups in the **[!UICONTROL Custom Domain Group]** tab (**CJMRT-180014-400**).
* A campaign used in a plan must be live, have an audience, be configured for the IP warmup use case (**[!UICONTROL IP warmup plan activation]** option enabled), use the same email channel configuration as the plan, and not be used in another IP warmup plan.
* The name of an IP warmup plan must be unique.
* Deletion: only a plan with the status "Not started" can be deleted, only a phase with no activated run can be deleted, and only a run in **[!UICONTROL Draft]** status can be deleted.
* Split: a phase cannot be split on its first run, and only runs in **[!UICONTROL Draft]** status can be split to a new phase.
* A plan cannot be marked as completed while the last activated run is **[!UICONTROL Live]**.

**Prerequisites and permissions:**

* The **View Campaigns** permission for the campaign selected in the phase (**CJMRT-180058-403**), and the **View Segments** permission for the audience associated with the campaign selected in the phase (**CJMRT-180059-403**). Your administrator grants them.

**Terminology:**

* **Canonical name:** IP warmup plan errors
* **Synonyms:** "channel surface" (in the messages) = "channel configuration" (in the fixes), for the same selection.

**FAQ:**

* **Q: Which file formats can I upload for a plan?** — .xls and .xlsx (**CJMRT-180001-415**, **CJMRT-180002-422**).
* **Q: Why is my plan file rejected as not following the template?** — Fill in the **[!UICONTROL Warmup Plan]** and **[!UICONTROL Custom Domain Group]** sheets exactly as in the template, including the properties and values, the phase numbers, the run numbers, the target volumes, and the custom domain groups. Download the template again if needed.
* **Q: Why is the channel configuration or the campaign refused?** — The channel configuration must be active, have the email channel, be of the marketing type, and have domains and IP pools associated. The campaign must be live, with an audience, with the **[!UICONTROL IP warmup plan activation]** option enabled, and not used in another plan.
* **Q: Why can I not activate a run?** — Set a send time at least 12 hours from now (**CJMRT-180036-400**, **CJMRT-180039-403**), and activate a run only after all the previous runs have ended (**CJMRT-180038-403**). A status change that is not allowed returns **CJMRT-180037-403**: check the status of the run.
* **Q: What do I do when a run is cancelled or fails after activation?** — Duplicate the run and activate it again, except for **CJMRT-180060-500**, where you split the run to a new phase and select a different campaign and audience. For **CJMRT-180050-500**, first define a retry time window in the plan properties. For **CJMRT-180051-500** and **CJMRT-180052-500**, activate it at a later date and time. For **CJMRT-180054-500**, schedule the duplicate at a later date and time. For **CJMRT-180053-500**, review the number of targeted profiles before you activate it again. For **CJMRT-180051-500** and **CJMRT-180052-500**, splitting the run to a new phase is another documented fix.
* **Q: Why can I not delete a plan, a phase, or a run?** — Only a plan with the status "Not started", a phase with no activated run, and a run in **[!UICONTROL Draft]** status can be deleted (**CJMRT-180043-403**, **CJMRT-180044-403**, **CJMRT-180045-403**).

**Troubleshooting:**

* **Plan file** (**CJMRT-180001-415** to **CJMRT-180014-400**):
    * Not supported format or missing plan (**CJMRT-180001-415**, **CJMRT-180002-422**): upload the plan as an Excel file (.xls or .xlsx).
    * Template not followed (**CJMRT-180003-400**): fill in the **[!UICONTROL Warmup Plan]** and **[!UICONTROL Custom Domain Group]** sheets exactly as in the template, including the properties and values. Download the template again if needed.
    * Properties and values of the **[!UICONTROL Warmup Plan]** sheet missing or incorrectly formatted (**CJMRT-180004-400**): enter them exactly as in the template.
    * Errors in the **[!UICONTROL Warmup Plan]** sheet (**CJMRT-180011-400**) or in the **[!UICONTROL Custom Domain Group]** sheet (**CJMRT-180012-400**): fill in the sheet named in the message exactly as in the template.
    * Phase number that could not be determined (**CJMRT-180005-400**): enter the phase number and the run number in the format of the template.
    * Run number missing (**CJMRT-180006-400**), phase number not valid (**CJMRT-180007-400**), or run number not valid (**CJMRT-180008-400**): enter it in the format of the template.
    * Target volume for the domain group named in the message not valid (**CJMRT-180009-400**), or custom domain group not valid (**CJMRT-180013-400**): enter it in the format of the template.
    * "The domain group provided is neither a global nor a custom domain group defined in the plan. Define custom domain groups and re-upload the plan." (**CJMRT-180010-400**) and "Global domain groups have been included into the 'Custom Domain Group' sheet. Please ensure that only custom domain groups are provided and re-upload the plan." (**CJMRT-180014-400**): define each custom domain group in the **[!UICONTROL Custom Domain Group]** tab, and remove the global domain groups from it, so that only custom domain groups are defined there. Then upload the plan again.
* **Channel configuration and campaigns** (**CJMRT-180015-400** to **CJMRT-180027-403**):
    * Surface not 'Active' (**CJMRT-180015-400**): select an active channel configuration.
    * Surface without the 'Email' channel (**CJMRT-180016-400**): select a channel configuration that has the email channel.
    * Surface not a 'Marketing' type surface (**CJMRT-180017-400**): select a channel configuration of the marketing type.
    * Channel surface missing (**CJMRT-180018-400**): select a channel configuration for the plan.
    * Channel surface invalid because it has no domains associated (**CJMRT-180019-400**) or no IP pools associated (**CJMRT-180020-400**): select one with domains, or with IP pools, associated.
    * "The IP warmup plan name {name} is already in use. Please provide a unique name." (**CJMRT-180021-409**): an IP warmup plan with this name already exists. Enter a unique name.
    * "The selected retry period is invalid. Please select a value between {minPeriod} and {maxPeriod} minutes." (**CJMRT-180022-400**): select a retry period within the range shown in the message.
    * Campaign not configured for IP warmup (**CJMRT-180023-400**): select a campaign with the **[!UICONTROL IP warmup plan activation]** option enabled.
    * Campaign not 'Live' (**CJMRT-180024-400**): select a live campaign.
    * Campaign without audience (**CJMRT-180025-400**): select a campaign with an audience.
    * Campaign with a different email surface (**CJMRT-180026-400**): select a campaign that uses the same email channel configuration as the plan.
    * Campaign already used in another IP warmup plan (**CJMRT-180027-403**): select or create another campaign.
* **Phases and domain groups**:
    * Custom domain group mapping not provided (**CJMRT-180028-400**): make sure the custom domain groups of the plan are mapped correctly.
    * **[!UICONTROL All]** group selected together with other domain groups (**CJMRT-180029-400**): if you select **[!UICONTROL All]**, do not select other groups.
    * No domain group provided (**CJMRT-180030-400**): select at least one domain group.
    * Domain group and associated domains not valid (**CJMRT-180031-400**): check the domain groups selected for the phase and the domains of the custom domain groups in the plan.
    * Domain group not part of the global or custom domain groups defined in the plan (**CJMRT-180032-400**): select a domain group that is defined in the plan.
    * Domain group not matching the phase (**CJMRT-180033-400**): select a domain group that matches the domain groups defined for this phase.
    * "The domain {domain} is already included in another domain group used in the IP warmup plan." (**CJMRT-180056-400**, **CJMRT-180057-400**): make sure each domain belongs to only one domain group.
    * Delete not allowed (**CJMRT-180043-403** to **CJMRT-180045-403**): see the guardrails.
    * Split on the first run (**CJMRT-180047-400**): split from another run, or add a run below.
    * Split from a run that is not in **[!UICONTROL Draft]** status (**CJMRT-180048-400**): select a **[!UICONTROL Draft]** run to split from.
* **Runs and activation**:
    * "The number of targeted profiles is invalid" (**CJMRT-180034-400**) and "The total number of targeted profiles cannot be equal to zero" (**CJMRT-180035-400**): enter a number greater than zero.
    * "The 'Last engagement' period cannot be negative" (**CJMRT-180040-400**): enter a period that is not negative.
    * Send time less than 12 hours away (**CJMRT-180036-400**, **CJMRT-180039-403**): set a send time at least 12 hours from now. For **CJMRT-180039-403**, then activate the run again.
    * "The IP warmup plan cannot be marked as completed as the last activated run status is 'Live'." (**CJMRT-180046-403**): wait until the run has ended, then mark the plan as completed.
* **Run failures** (a run is cancelled or fails after it was activated):
    * "The audience has not been evaluated. To enable retries for the run execution, define a retry run time in the IP warmup plan properties before duplicating the run." (**CJMRT-180050-500**): define a retry time window in the plan properties, then duplicate the run and activate it again.
    * Audience not evaluated (**CJMRT-180051-500**) or audience composition error (**CJMRT-180052-500**): duplicate the run and activate it again at a later date and time, or split the run to a new phase.
    * "The run was cancelled as the number of qualified profiles did not meet the targeted amount, with the 'Cancel run with errors' option enabled." (**CJMRT-180053-500**): the **[!UICONTROL Cancel activated runs in case of errors]** option is enabled. Duplicate the run and review the number of targeted profiles before you activate it again.
    * "The run failed as there are no qualified profiles." (**CJMRT-180060-500**): split the run to a new phase and select a different campaign and audience.
    * "The server encountered an internal error and could not execute the run." (**CJMRT-180054-500**): duplicate the run and schedule it at a later date and time.

**Related pages:**

* Preparing the plan file: Prepare the plan file (configuration/ip-warmup-plan.md)
* Plan template: Download the IP warmup plan template (configuration/ip-warmup-plan-files.md)
* Campaigns for IP warmup: Create IP warmup campaigns (configuration/ip-warmup-campaign.md)
* Defining phases, defining and activating runs, and run statuses: Run the IP warmup plan (configuration/ip-warmup-execution.md)
* Other error code prefixes: Error codes reference (building-journeys/error-codes-reference.md)

+++

<!-- ai-section-version: 1 | source-hash: b9b83746 -->
