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
* Know what to note and whom to contact when an error persists after the listed steps.

**Glossary:**

* **CJMRT** *(product-specific)*: prefix of the IP warmup error codes, followed by an error number and an HTTP status, for example **CJMRT-180021-409**.
* **IP warmup plan**: defined in an Excel file (.xls or .xlsx) with the **[!UICONTROL Warmup Plan]** sheet and the **[!UICONTROL Custom Domain Group]** sheet, and made of phases and runs.
* **Phase** and **run**: a plan is divided into phases, and a phase contains runs. A run can be activated, duplicated, or split to a new phase.
* **Domain group**: a group of domains. The domain groups are global or custom (defined in the **[!UICONTROL Custom Domain Group]** tab of the plan). **[!UICONTROL All]** is a domain group that you can select in a phase.
* **Channel configuration**: the page calls it a "channel surface" in several error messages. It must be active, have the email channel, be of the marketing type, and have domains and IP pools associated.

**Guardrails:**

* Supported plan file formats: .xls and .xlsx.
* The send time of a run must be at least 12 hours from the current time (hard limit) (**CJMRT-180036-400**, **CJMRT-180039-403**).
* A run can be activated only after all the previous runs have ended (**CJMRT-180038-403**).
* The number of targeted profiles must not be negative, and the total number of targeted profiles cannot be zero (**CJMRT-180034-400**, **CJMRT-180035-400**). The 'Last engagement' period cannot be negative (**CJMRT-180040-400**).
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

* The [!DNL View campaigns] permission for the campaign selected in the phase (**CJMRT-180058-403**), and the [!DNL View segments] permission for the audience associated with the campaign selected in the phase (**CJMRT-180059-403**). Your administrator adds the permission to your role and checks that your role includes the access labels of the campaign (**CJMRT-180058-403**) or of the audience (**CJMRT-180059-403**). Otherwise, use **[!UICONTROL Replace]** to select a campaign for the phase that you can access (**CJMRT-180058-403**), or whose audience you can access (**CJMRT-180059-403**).

**Terminology:**

* **Canonical name:** IP warmup plan errors
* **Synonyms:** "channel surface" (in the messages) = "channel configuration" (in the fixes), for the same selection.

**FAQ:**

* **Q: Which file formats can I upload for a plan?** — .xls and .xlsx (**CJMRT-180001-415**, **CJMRT-180002-422**).
* **Q: Why is my plan file rejected as not following the template?** — Fill in the **[!UICONTROL Warmup Plan]** and **[!UICONTROL Custom Domain Group]** sheets exactly as in the template, including the properties and values, the phase numbers, the run numbers, the target volumes, and the custom domain groups. Download the template again if needed.
* **Q: Why is the channel configuration or the campaign refused?** — The channel configuration must be active, have the email channel, be of the marketing type, and have domains and IP pools associated. The campaign must be live, with an audience, with the **[!UICONTROL IP warmup plan activation]** option enabled, and not used in another plan.
* **Q: Why can I not activate a run?** — Set a send time at least 12 hours from now (**CJMRT-180036-400**, **CJMRT-180039-403**), and activate a run only after all the previous runs have ended (**CJMRT-180038-403**). A status change that is not allowed returns **CJMRT-180037-403**: check the status of the run in the plan and use an action available for it (activate a **[!UICONTROL Draft]** run, cancel a **[!UICONTROL Live]** run, or duplicate the run). For **CJMRT-180036-400** and **CJMRT-180039-403**, use **[!UICONTROL Edit run]** (More actions icon).
* **Q: What do I do when a run is cancelled or fails after activation?** — Duplicate the run and activate it again, except for **CJMRT-180060-500**, where you split the run to a new phase and select a different campaign and audience. For **CJMRT-180050-500**, first click the Properties icon next to the plan name and set a duration in the **[!UICONTROL Retry run time]** drop-down list. For **CJMRT-180051-500** and **CJMRT-180052-500**, activate it at a later date and time. For **CJMRT-180054-500**, set a later **[!UICONTROL Send time]** on the duplicate, then activate it. For **CJMRT-180053-500**, review the targeted profiles in **[!UICONTROL Edit run]**, then lower the number or disable the **[!UICONTROL Cancel activated runs in case of errors]** option before you activate it again. For **CJMRT-180051-500** and **CJMRT-180052-500**, splitting the run to a new phase is another documented fix.
* **Q: Why can I not delete a plan, a phase, or a run?** — Only a plan with the status "Not started", a phase with no activated run, and a run in **[!UICONTROL Draft]** status can be deleted (**CJMRT-180043-403**, **CJMRT-180044-403**, **CJMRT-180045-403**). If the plan has started, select **[!UICONTROL More]** > **[!UICONTROL Mark as completed]** instead, once no run is **[!UICONTROL Live]**. If a run of the phase was activated, keep the phase and select **[!UICONTROL Split runs to a new phase]** from the More actions icon of a **[!UICONTROL Draft]** run. For a run that is not in **[!UICONTROL Draft]** status, select **[!UICONTROL Duplicate run]** from the More actions icon.
* **Q: What do I do if the error persists after the listed steps?** — Note the error code, the message, the request ID, and the campaign, journey, or activity concerned, and keep the logs or screenshots. Then contact your administrator for a permission or access error, or contact Adobe Support with these details. For all the support options, see the Getting support section of the error codes reference.

**Troubleshooting:**

* **Plan file** (**CJMRT-180001-415** to **CJMRT-180014-400**):
    * Not supported format or missing plan (**CJMRT-180001-415**, **CJMRT-180002-422**): save the plan as an Excel file in .xls or .xlsx format and upload it again; for a missing plan, upload the Excel plan file prepared from the template when you create the plan.
    * Template not followed (**CJMRT-180003-400**): fill in the **[!UICONTROL Warmup Plan]** and **[!UICONTROL Custom Domain Group]** sheets exactly as in the template, including the properties and values. Download the template again if needed.
    * Properties and values of the **[!UICONTROL Warmup Plan]** sheet missing or incorrectly formatted (**CJMRT-180004-400**): in the **[!UICONTROL Warmup Plan]** sheet, fill in the properties and values exactly as in the template, then upload the file again.
    * Errors in the **[!UICONTROL Warmup Plan]** sheet (**CJMRT-180011-400**) or in the **[!UICONTROL Custom Domain Group]** sheet (**CJMRT-180012-400**): for the **[!UICONTROL Warmup Plan]** sheet, check the phases, runs and domain group columns against the template or the sample plan; for the **[!UICONTROL Custom Domain Group]** sheet, define each custom domain group on its own row with all its domains on the same row, as in the template. Then upload the file again.
    * Phase number that could not be determined (**CJMRT-180005-400**): in the **[!UICONTROL Warmup Plan]** sheet, enter the phase number and the run number of each run in the format of the template.
    * Run number missing (**CJMRT-180006-400**), phase number not valid (**CJMRT-180007-400**), or run number not valid (**CJMRT-180008-400**): in the **[!UICONTROL Warmup Plan]** sheet, enter the run number in the format of the template, or compare the phase and run numbers with the template or the sample plan and correct them.
    * Target volume for the domain group named in the message not valid (**CJMRT-180009-400**), or custom domain group not valid (**CJMRT-180013-400**): correct the target volume in the **[!UICONTROL Warmup Plan]** sheet, or check the custom domain groups in the **[!UICONTROL Custom Domain Group]** sheet against the template.
    * "The domain group provided is neither a global nor a custom domain group defined in the plan. Define custom domain groups and re-upload the plan." (**CJMRT-180010-400**) and "Global domain groups have been included into the 'Custom Domain Group' sheet. Please ensure that only custom domain groups are provided and re-upload the plan." (**CJMRT-180014-400**): define each custom domain group used in the plan in the **[!UICONTROL Custom Domain Group]** tab (or use a group from the **[!UICONTROL OOTB Domain Groups]** tab), and remove the global domain groups from it, so that only custom domain groups are defined there. Then upload the plan again.
* **Channel configuration and campaigns** (**CJMRT-180015-400** to **CJMRT-180027-403**):
    * Surface not 'Active' (**CJMRT-180015-400**): select an active channel configuration.
    * Surface without the 'Email' channel (**CJMRT-180016-400**): select a channel configuration that has the email channel.
    * Surface not a 'Marketing' type surface (**CJMRT-180017-400**): select a channel configuration of the marketing type.
    * Channel surface missing (**CJMRT-180018-400**): select a channel configuration for the plan.
    * Channel surface invalid because it has no domains associated (**CJMRT-180019-400**) or no IP pools associated (**CJMRT-180020-400**): select a channel configuration created for the domain (or for the IPs) that you want to warm up, or create one for the domain and IPs identified for your plan.
    * "The IP warmup plan name {name} is already in use. Please provide a unique name." (**CJMRT-180021-409**): check the existing plan names in **[!UICONTROL Administration]** > **[!UICONTROL Channels]** > **[!UICONTROL Email settings]** > **[!UICONTROL IP warmup plans]**, then enter a name that none of them uses.
    * "The selected retry period is invalid. Please select a value between {minPeriod} and {maxPeriod} minutes." (**CJMRT-180022-400**): click the Properties icon next to the plan name and select a duration within the range of the message in the **[!UICONTROL Retry run time]** drop-down list.
    * Campaign not configured for IP warmup (**CJMRT-180023-400**): select a campaign whose **[!UICONTROL Schedule]** section has the **[!UICONTROL IP warmup plan activation]** option enabled, or enable it in the campaign.
    * Campaign not 'Live' (**CJMRT-180024-400**): activate the campaign so that its status is **[!UICONTROL Live]**, or select a campaign that is already live.
    * Campaign without audience (**CJMRT-180025-400**): add a segment-based audience to the campaign, or select a campaign that has one.
    * Campaign with a different email surface (**CJMRT-180026-400**): select a campaign that uses the same email channel configuration as the plan.
    * Campaign already used in another IP warmup plan (**CJMRT-180027-403**): select a campaign that is not used in another plan, or create an IP warmup campaign for this plan.
* **Phases and domain groups**:
    * Custom domain group mapping not provided (**CJMRT-180028-400**): check that every custom domain group of the plan is defined in the **[!UICONTROL Custom Domain Group]** tab of the template; if not, add it and re-upload the plan.
    * **[!UICONTROL All]** group selected together with other domain groups (**CJMRT-180029-400**): if you select **[!UICONTROL All]**, do not select other groups.
    * No domain group provided (**CJMRT-180030-400**): select at least one domain group.
    * Domain group and associated domains not valid (**CJMRT-180031-400**): check the domain groups selected for the phase and the domains of the custom domain groups in the plan.
    * Domain group not part of the global or custom domain groups defined in the plan (**CJMRT-180032-400**): select a domain group of the plan: an out-of-the-box group from the **[!UICONTROL OOTB Domain Groups]** tab or a custom group from the **[!UICONTROL Custom Domain Group]** tab.
    * Domain group not matching the phase (**CJMRT-180033-400**): select a domain group that matches the domain groups defined for this phase.
    * "The domain {domain} is already included in another domain group used in the IP warmup plan." (**CJMRT-180056-400**, **CJMRT-180057-400**): in the **[!UICONTROL Custom Domain Group]** tab, keep each domain named in the message in only one domain group, then upload the plan again.
    * Delete not allowed (**CJMRT-180043-403** to **CJMRT-180045-403**): see the guardrails. For a plan that has started, select **[!UICONTROL More]** > **[!UICONTROL Mark as completed]** instead, once no run is **[!UICONTROL Live]** (**CJMRT-180043-403**); for a phase with an activated run, select **[!UICONTROL Split runs to a new phase]** from the More actions icon of a **[!UICONTROL Draft]** run (**CJMRT-180044-403**); for a run that is not in **[!UICONTROL Draft]** status, select **[!UICONTROL Duplicate run]** from the More actions icon (**CJMRT-180045-403**).
    * Split on the first run (**CJMRT-180047-400**): select **[!UICONTROL Split runs to a new phase]** from the More actions icon of a run other than the first one, or add a run below the first run.
    * Split from a run that is not in **[!UICONTROL Draft]** status (**CJMRT-180048-400**): select a **[!UICONTROL Draft]** run and choose **[!UICONTROL Split runs to a new phase]** from its More actions icon.
* **Runs and activation**:
    * "The number of targeted profiles is invalid" (**CJMRT-180034-400**) and "The total number of targeted profiles cannot be equal to zero" (**CJMRT-180035-400**): in **[!UICONTROL Edit run]** (More actions icon), enter a number greater than zero for the targeted profiles of each column (**CJMRT-180034-400**) or of at least one column (**CJMRT-180035-400**).
    * "The 'Last engagement' period cannot be negative" (**CJMRT-180040-400**): in **[!UICONTROL Edit run]** (More actions icon), enter 0 or a positive number of days in the **[!UICONTROL Last engaged]** field; enter 0 to disable the engagement period.
    * Send time less than 12 hours away (**CJMRT-180036-400**, **CJMRT-180039-403**): in **[!UICONTROL Edit run]** (More actions icon), set a send time at least 12 hours from now. For **CJMRT-180039-403**, then select **[!UICONTROL Activate]** again.
    * "The IP warmup plan cannot be marked as completed as the last activated run status is 'Live'." (**CJMRT-180046-403**): wait until the **[!UICONTROL Live]** run ends, then select **[!UICONTROL More]** > **[!UICONTROL Mark as completed]**.
* **Run failures** (a run is cancelled or fails after it was activated):
    * "The audience has not been evaluated. To enable retries for the run execution, define a retry run time in the IP warmup plan properties before duplicating the run." (**CJMRT-180050-500**): click the Properties icon next to the plan name and set a duration in the **[!UICONTROL Retry run time]** drop-down list, then duplicate the run and activate it again.
    * Audience not evaluated (**CJMRT-180051-500**) or audience composition error (**CJMRT-180052-500**): duplicate the run and activate it again at a later date and time, or split the run to a new phase.
    * "The run was cancelled as the number of qualified profiles did not meet the targeted amount, with the 'Cancel run with errors' option enabled." (**CJMRT-180053-500**): the **[!UICONTROL Cancel activated runs in case of errors]** option is enabled. Duplicate the run and review the targeted profiles in **[!UICONTROL Edit run]**; lower the number, or disable the option, then activate the run again.
    * "The run failed as there are no qualified profiles." (**CJMRT-180060-500**): select **[!UICONTROL Split runs to a new phase]** from the More actions icon of the run, then select a different campaign for the new phase.
    * "The server encountered an internal error and could not execute the run." (**CJMRT-180054-500**): duplicate the run, set a later **[!UICONTROL Send time]**, then activate it.

**Related pages:**

* Preparing the plan file: Prepare the plan file (configuration/ip-warmup-plan.md)
* Plan template: Download the IP warmup plan template (configuration/ip-warmup-plan-files.md)
* Campaigns for IP warmup: Create IP warmup campaigns (configuration/ip-warmup-campaign.md)
* Defining phases, defining and activating runs, and run statuses: Run the IP warmup plan (configuration/ip-warmup-execution.md)
* Other error code prefixes: Error codes reference (building-journeys/error-codes-reference.md)
* Support options when an error persists: Getting support (building-journeys/error-codes-reference.md#getting-support)
* Contacting Adobe Support: Support ticket guidelines (start/user-interface.md#support-ticket-guidelines)

+++

<!-- ai-section-version: 1 | source-hash: de6ae2e3 -->
