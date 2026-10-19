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
* **Domain group**: a group of domains. The domain groups are global (the out-of-the-box domain groups) or custom (defined in the **[!UICONTROL Custom Domain Group]** tab). **[!UICONTROL All]** is a domain group that you can select in a phase.
* **Channel configuration**: the page calls it a "channel surface" in several error messages. It must be active, have the email channel, be of the marketing type, and have domains and IP pools associated.

**Guardrails:**

* Supported plan file formats: .xls and .xlsx.
* A run must be activated at least 12 hours before its send time (hard limit) (**CJMRT-180036-400**, **CJMRT-180039-403**).
* A run can be activated only after all the previous runs have ended (**CJMRT-180038-403**).
* The number of targeted profiles must be greater than zero, and the 'Last engagement' period cannot be negative.
* The retry period must be within the range shown in the message, in minutes (**CJMRT-180022-400**).
* A domain must belong to only one domain group of the plan.
* If you select the **[!UICONTROL All]** domain group, do not select other groups.
* Do not repeat the out-of-the-box domain groups in the **[!UICONTROL Custom Domain Group]** tab.
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
* **Q: What do I do when a run is cancelled or fails after activation?** — Duplicate the run and activate it again. For **CJMRT-180050-500**, first define a retry time window in the plan properties. For **CJMRT-180051-500** and **CJMRT-180052-500**, activate it at a later date and time. For **CJMRT-180054-500**, schedule the duplicate at a later date and time. For **CJMRT-180053-500**, review the number of targeted profiles before you activate it again. Another documented fix is splitting to a new phase (**CJMRT-180051-500**, **CJMRT-180052-500**, **CJMRT-180060-500**).
* **Q: Why can I not delete a plan, a phase, or a run?** — Only a plan with the status "Not started", a phase with no activated run, and a run in **[!UICONTROL Draft]** status can be deleted (**CJMRT-180043-403**, **CJMRT-180044-403**, **CJMRT-180045-403**).

**Troubleshooting:**

* **Plan file** (**CJMRT-180001-415** to **CJMRT-180014-400**):
    * Not supported format or missing plan (**CJMRT-180001-415**, **CJMRT-180002-422**): upload the plan as an Excel file (.xls or .xlsx).
    * Template not followed (**CJMRT-180003-400**, **CJMRT-180004-400**, **CJMRT-180011-400**, **CJMRT-180012-400**): messages name the 'Properties' and 'Value' parameters of the Warmup Plan sheet, and the 'Warmup Plan' and 'Custom Domain Group' sheets. See the FAQ.
    * Phase number or run number missing or not valid (**CJMRT-180005-400** to **CJMRT-180008-400**): enter them in the format of the template.
    * Target volume or custom domain group not valid (**CJMRT-180009-400**, **CJMRT-180013-400**): enter them in the format of the template.
    * "The domain group provided is neither a global nor a custom domain group defined in the plan. Define custom domain groups and re-upload the plan." (**CJMRT-180010-400**) and "Global domain groups have been included into the 'Custom Domain Group' sheet. Please ensure that only custom domain groups are provided and re-upload the plan." (**CJMRT-180014-400**): define each custom domain group in the **[!UICONTROL Custom Domain Group]** tab, and do not repeat the out-of-the-box domain groups there. Then upload the plan again.
* **Channel configuration and campaigns** (**CJMRT-180015-400** to **CJMRT-180027-403**):
    * Surface not 'Active', without the 'Email' channel, or not a 'Marketing' type surface (**CJMRT-180015-400**, **CJMRT-180016-400**, **CJMRT-180017-400**): select an active channel configuration that has the email channel and is of the marketing type.
    * Channel surface missing or invalid (**CJMRT-180018-400**, **CJMRT-180019-400**, **CJMRT-180020-400**): select a channel configuration for the plan, with domains and IP pools associated.
    * "The IP warmup plan name {name} is already in use. Please provide a unique name." (**CJMRT-180021-409**): an IP warmup plan with this name already exists. Enter a unique name.
    * "The selected retry period is invalid. Please select a value between {minPeriod} and {maxPeriod} minutes." (**CJMRT-180022-400**): select a retry period within the range shown in the message.
    * Campaign invalid, not 'Live', or without audience (**CJMRT-180023-400**, **CJMRT-180024-400**, **CJMRT-180025-400**): see the FAQ.
    * Campaign with a different email surface, or already used in another IP warmup plan (**CJMRT-180026-400**, **CJMRT-180027-403**): select a campaign that uses the same email channel configuration as the plan, and that is not used in another IP warmup plan.
* **Phases and domain groups**:
    * Domain groups missing or not valid (**CJMRT-180028-400** to **CJMRT-180031-400**): select at least one domain group. If you select the **[!UICONTROL All]** group, do not select other groups.
    * Domain group not defined in the plan or not matching the phase (**CJMRT-180032-400**, **CJMRT-180033-400**): select a domain group that is defined in the plan, and that matches the domain groups defined for this phase.
    * "The domain {domain} is already included in another domain group used in the IP warmup plan." (**CJMRT-180056-400**, **CJMRT-180057-400**): make sure each domain belongs to only one domain group.
    * Delete not allowed (**CJMRT-180043-403** to **CJMRT-180045-403**) and split not allowed (**CJMRT-180047-400**, **CJMRT-180048-400**): see the guardrails. For a split, split from another run, or add a run below.
* **Runs and activation**:
    * "The number of targeted profiles is invalid", "The total number of targeted profiles cannot be equal to zero", "The 'Last engagement' period cannot be negative" (**CJMRT-180034-400**, **CJMRT-180035-400**, **CJMRT-180040-400**): see the guardrails.
    * "The IP warmup plan cannot be marked as completed as the last activated run status is 'Live'." (**CJMRT-180046-403**): wait until the run has ended, then mark the plan as completed.
* **Run failures** (a run is cancelled or fails after it was activated):
    * "The audience has not been evaluated. To enable retries for the run execution, define a retry run time in the IP warmup plan properties before duplicating the run." (**CJMRT-180050-500**): define a retry time window in the plan properties, then duplicate the run and activate it again.
    * Audience not evaluated or audience composition error (**CJMRT-180051-500**, **CJMRT-180052-500**): duplicate the run and activate it again at a later date and time, or split the run to a new phase.
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

<!-- ai-section-version: 1 | source-hash: 29d3689f -->
