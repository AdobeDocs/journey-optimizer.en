---
solution: Journey Optimizer
product: journey optimizer
title: IP warmup plan errors
description: Learn what common errors mean when you create and run an IP warmup plan in Adobe Journey Optimizer, and how to fix them
feature: IP Warmup Plans, Deliverability
topic: Administration
role: Admin
level: Experienced
keywords: error, troubleshooting, IP warmup, plan, phase, run
---
# IP warmup plan errors {#ip-warmup-plan-errors}

>[!BEGINSHADEBOX]

**On this page:** Find the cause and the fix for the errors that [!DNL Adobe Journey Optimizer] returns when you upload an IP warmup plan, define its phases and runs, activate runs, or when a run fails.

>[!ENDSHADEBOX]

IP warmup errors use the prefix **CJMRT**, followed by an error number and an HTTP status. For the other error code prefixes, see the [error codes reference](../building-journeys/error-codes-reference.md).

## Plan file {#file}

These errors occur when you upload the Excel file that defines your IP warmup plan.

See also [Prepare the plan file](ip-warmup-plan.md#prepare-file) and [Download the IP warmup plan template](ip-warmup-plan-files.md).

| Error code | Message | How to fix |
|---|---|---|
| **CJMRT-180001-415** | This file format is not supported. Supported formats are: .xls and .xlsx. | Save the plan as an Excel file in .xls or .xlsx format, then upload it again. [Learn more](ip-warmup-plan.md#prepare-file) |
| **CJMRT-180002-422** | The IP warmup plan is missing. Please upload your plan in an .xls or .xlsx file. | When you create the plan, upload the Excel plan file (.xls or .xlsx) prepared from the template. [Learn more](ip-warmup-plan.md#prepare-file) |
| **CJMRT-180003-400** | The file could not be uploaded. Please enter the information in the correct format, as provided in the template. | Fill in the **[!UICONTROL Warmup Plan]** and **[!UICONTROL Custom Domain Group]** sheets exactly as in the template, including the properties and values. Download the template again if needed. [Learn more](ip-warmup-plan.md#prepare-file) |
| **CJMRT-180004-400** | The 'Properties' and 'Value' parameters provided in the Warmup Plan sheet are missing or incorrectly formatted. Please enter the information in the correct format, as provided in the template. | In the **[!UICONTROL Warmup Plan]** sheet, fill in the properties and values exactly as in the template, then upload the file again. Download the template again if needed. [Learn more](ip-warmup-plan.md#prepare-file) |
| **CJMRT-180011-400** | There are errors in the 'Warmup Plan' sheet of the plan. Please enter the information in the correct format, as provided in the template. | Check the phases, runs and domain group columns of the **[!UICONTROL Warmup Plan]** sheet against the template or the sample plan, then upload the file again. [Learn more](ip-warmup-plan.md#prepare-file) |
| **CJMRT-180012-400** | There are errors in the 'Custom Domain Group' sheet of the plan. Please enter the information in the correct format, as provided in the template. | In the **[!UICONTROL Custom Domain Group]** sheet, define each custom domain group on its own row with all its domains on the same row, as in the template. Then upload the file again. [Learn more](ip-warmup-plan.md#prepare-file) |
| **CJMRT-180005-400** | The phase number could not be determined. Please enter the information in the correct format, as provided in the template. | In the **[!UICONTROL Warmup Plan]** sheet, enter the phase number and the run number of each run in the format of the template, then upload the file again. [Learn more](ip-warmup-plan.md#prepare-file) |
| **CJMRT-180006-400** | The run number is missing from the Warmup Plan sheet. Please enter the information in the correct format, as provided in the template. | Enter the run number of each run in the **[!UICONTROL Warmup Plan]** sheet in the format of the template, then upload the file again. [Learn more](ip-warmup-plan.md#prepare-file) |
| **CJMRT-180007-400** | The phase number is invalid. Please enter the information in the correct format, as provided in the template. | Compare the phase numbers of the **[!UICONTROL Warmup Plan]** sheet with the template or the sample plan and correct them, then upload the file again. [Learn more](ip-warmup-plan.md#prepare-file) |
| **CJMRT-180008-400** | The run number is invalid. Please enter the information in the correct format, as provided in the template. | Compare the run numbers of the **[!UICONTROL Warmup Plan]** sheet with the template or the sample plan and correct them, then upload the file again. [Learn more](ip-warmup-plan.md#prepare-file) |
| **CJMRT-180009-400** | The target volume for domain group {domainGroup} is invalid. Please enter the information in the correct format, as provided in the template. | In the **[!UICONTROL Warmup Plan]** sheet, correct the target volume of the domain group named in the message, using the format of the template. Then upload the file again. [Learn more](ip-warmup-plan.md#prepare-file) |
| **CJMRT-180013-400** | The custom domain group provided is invalid. Please enter the information in the correct format, as provided in the template. | Check the custom domain groups in the **[!UICONTROL Custom Domain Group]** sheet against the template, then upload the file again. [Learn more](ip-warmup-plan.md#prepare-file) |
| **CJMRT-180010-400** | The domain group provided is neither a global nor a custom domain group defined in the plan. Define custom domain groups and re-upload the plan. | Define each custom domain group used in the plan in the **[!UICONTROL Custom Domain Group]** tab, or use a group from the **[!UICONTROL OOTB Domain Groups]** tab. Then upload the plan again. [Learn more](ip-warmup-plan.md#custom-domain-group-tab) |
| **CJMRT-180014-400** | Global domain groups have been included into the 'Custom Domain Group' sheet. Please ensure that only custom domain groups are provided and re-upload the plan. | Remove the global domain groups from the **[!UICONTROL Custom Domain Group]** tab so that only custom domain groups remain there, then upload the plan again. [Learn more](ip-warmup-plan.md#custom-domain-group-tab) |

## Channel configuration and campaigns {#config-campaign}

These errors occur when you select the channel configuration of the plan and the campaign of a phase.

See also [Create IP warmup campaigns](ip-warmup-campaign.md).

| Error code | Message | How to fix |
|---|---|---|
| **CJMRT-180015-400** | The selected surface is not 'Active'. Please select an 'Active' channel surface. | When you create the plan, select a channel configuration that is active. [Learn more](ip-warmup-campaign.md) |
| **CJMRT-180016-400** | The selected surface is not supported as it does not contain the 'Email' channel. Please select a valid surface. | When you create the plan, select a channel configuration that has the email channel. [Learn more](ip-warmup-campaign.md) |
| **CJMRT-180017-400** | The selected surface is not supported as it is not a 'Marketing' type surface. Please select a valid surface. | Select a marketing channel configuration: only marketing configurations are available for an IP warmup plan. [Learn more](ip-warmup-campaign.md) |
| **CJMRT-180018-400** | The channel surface is missing. Please select a channel surface for the IP warmup plan. | When you create the plan, select the channel configuration that you want to warm up. [Learn more](ip-warmup-plan.md) |
| **CJMRT-180019-400** | The channel surface is invalid. Please select a valid channel surface with domains associated. | Select a channel configuration created for the domain that you want to warm up, or create one for the domain and IPs identified for your plan. [Learn more](ip-warmup-plan.md) |
| **CJMRT-180020-400** | The channel surface is invalid. Please select a valid channel surface with IP pools associated. | Select a channel configuration created for the IPs that you want to warm up, or create one for the domain and IPs identified for your plan. [Learn more](ip-warmup-plan.md) |
| **CJMRT-180021-409** | The IP warmup plan name {name} is already in use. Please provide a unique name. | Check the existing plan names in **[!UICONTROL Administration]** > **[!UICONTROL Channels]** > **[!UICONTROL Email settings]** > **[!UICONTROL IP warmup plans]**, then enter a name that none of them uses. [Learn more](ip-warmup-plan.md) |
| **CJMRT-180022-400** | The selected retry period is invalid. Please select a value between {minPeriod} and {maxPeriod} minutes. | Click the Properties icon next to the plan name and select a duration within the range of the message in the **[!UICONTROL Retry run time]** drop-down list. [Learn more](ip-warmup-execution.md#define-runs) |
| **CJMRT-180023-400** | The selected campaign is invalid. Please select a campaign configured for IP warmup use case. | Select a campaign whose **[!UICONTROL Schedule]** section has the **[!UICONTROL IP warmup plan activation]** option enabled, or enable it in the campaign. [Learn more](ip-warmup-campaign.md) |
| **CJMRT-180024-400** | The selected campaign is not 'Live'. Please select a 'Live' campaign only. | Activate the campaign so that its status is **[!UICONTROL Live]**, or select a campaign that is already live. [Learn more](ip-warmup-campaign.md) |
| **CJMRT-180025-400** | The selected campaign does not contain any audience. Please select a campaign with an audience selected. | Add a segment-based audience to the campaign, or select a campaign that has one. [Learn more](ip-warmup-campaign.md) |
| **CJMRT-180026-400** | The selected campaign is invalid. Please select a campaign with the same email surface as of the IP warmup plan. | Select a campaign that uses the same email channel configuration as the plan. [Learn more](ip-warmup-campaign.md) |
| **CJMRT-180027-403** | The selected campaign is already in use in another IP warmup plan. Please select or create another campaign. | Select a campaign that is not used in another plan, or create an IP warmup campaign for this plan. [Learn more](ip-warmup-campaign.md) |

## Phases and domain groups {#phases}

These errors occur when you define the phases of the plan and select domain groups.

See also [Define the phases](ip-warmup-execution.md#define-phases).

| Error code | Message | How to fix |
|---|---|---|
| **CJMRT-180028-400** | The custom domain group mapping was not provided. Please ensure custom domain groups are mapped correctly. | Check that every custom domain group of the plan is defined in the **[!UICONTROL Custom Domain Group]** tab of the template. If not, add it and re-upload the plan. [Learn more](ip-warmup-execution.md#define-phases) |
| **CJMRT-180029-400** | The domain groups are invalid. Please ensure no additional domain groups are provided if 'All' domain group is selected. | Select either **[!UICONTROL All]** or specific domain groups for the phase, not both. [Learn more](ip-warmup-execution.md#define-phases) |
| **CJMRT-180030-400** | No domain groups were provided. Please provide at least one domain group to proceed. | Select at least one domain group for the phase. [Learn more](ip-warmup-execution.md#define-phases) |
| **CJMRT-180031-400** | The domain group and associated domains are invalid. Please check and try again. | Check the domain groups selected for the phase and the domains of the custom domain groups in the plan. [Learn more](ip-warmup-execution.md#define-phases) |
| **CJMRT-180032-400** | The domain group is invalid. Please select a domain group which is part of the global or custom domain groups defined in the IP warmup plan. | Select a domain group of the plan: an out-of-the-box group from the **[!UICONTROL OOTB Domain Groups]** tab or a custom group from the **[!UICONTROL Custom Domain Group]** tab. [Learn more](ip-warmup-execution.md#define-phases) |
| **CJMRT-180033-400** | The domain group is invalid. Select a domain group which matches with the domain groups defined for this phase. | Open the phase and select only domain groups that are defined for this phase in the plan. [Learn more](ip-warmup-execution.md#define-phases) |
| **CJMRT-180056-400** | The domain {domain} is already included in another domain group used in the IP warmup plan. Please ensure each domain is associated with only one domain group. | In the **[!UICONTROL Custom Domain Group]** tab, keep the domain named in the message in only one domain group, then upload the plan again. [Learn more](ip-warmup-plan.md#custom-domain-group-tab) |
| **CJMRT-180057-400** | The domain {domain} and {count} others are already included in another domain group used in the IP warmup plan. Please ensure each domain is associated with only one domain group. | In the **[!UICONTROL Custom Domain Group]** tab, keep each of the domains named in the message in only one domain group, then upload the plan again. [Learn more](ip-warmup-plan.md#custom-domain-group-tab) |
| **CJMRT-180043-403** | This plan cannot be deleted. Only plans with the status 'Not started' can be deleted. | If the plan has started, select **[!UICONTROL More]** > **[!UICONTROL Mark as completed]** instead, once no run is **[!UICONTROL Live]**. [Learn more](ip-warmup-execution.md#define-phases) |
| **CJMRT-180044-403** | This phase cannot be deleted. Only phases with no activated run can be deleted. | If a run of the phase was activated, keep the phase and select **[!UICONTROL Split runs to a new phase]** from the More actions icon of a **[!UICONTROL Draft]** run to define the remaining runs in a new phase. [Learn more](ip-warmup-execution.md#define-phases) |
| **CJMRT-180045-403** | This run cannot be deleted. Only runs with the status 'Draft' can be deleted. | To repeat a run that is not in **[!UICONTROL Draft]** status, select **[!UICONTROL Duplicate run]** from the More actions icon instead of deleting it. [Learn more](ip-warmup-execution.md#define-phases) |
| **CJMRT-180047-400** | You cannot split a phase on its first run. Try splitting the phase from another run or add a run below. | Select **[!UICONTROL Split runs to a new phase]** from the More actions icon of a run other than the first one, or add a run below the first run. [Learn more](ip-warmup-execution.md#split-phase) |
| **CJMRT-180048-400** | You cannot split the phase here. Only runs with the status 'Draft' can be split to a new phase. | Select a **[!UICONTROL Draft]** run and choose **[!UICONTROL Split runs to a new phase]** from its More actions icon. [Learn more](ip-warmup-execution.md#split-phase) |

## Runs and activation {#runs}

These errors occur when you define and activate the runs of a phase.

See also [Define and activate the runs](ip-warmup-execution.md#define-runs) and [Check the run statuses](ip-warmup-execution.md#run-statuses).

| Error code | Message | How to fix |
|---|---|---|
| **CJMRT-180034-400** | The number of targeted profiles is invalid. Please ensure the number entered is not negative. | In **[!UICONTROL Edit run]** (More actions icon), enter a number greater than zero for the targeted profiles of each column. [Learn more](ip-warmup-execution.md#define-runs) |
| **CJMRT-180035-400** | The total number of targeted profiles cannot be equal to zero. Please provide a valid number and try again. | In **[!UICONTROL Edit run]** (More actions icon), enter a number greater than zero for the targeted profiles of at least one column. [Learn more](ip-warmup-execution.md#define-runs) |
| **CJMRT-180040-400** | The 'Last engagement' period cannot be negative. Please provide a valid period and try again. | In **[!UICONTROL Edit run]** (More actions icon), enter 0 or a positive number of days in the **[!UICONTROL Last engaged]** field. Enter 0 to disable the engagement period. [Learn more](ip-warmup-execution.md#define-runs) |
| **CJMRT-180036-400** | The 'Send time' value provided is invalid. Please set the send time to at least 12 hours from the current time. | In **[!UICONTROL Edit run]** (More actions icon), set a send time at least 12 hours from now. [Learn more](ip-warmup-execution.md#activate-run) |
| **CJMRT-180039-403** | This run cannot be activated. Please set the send time to at least 12 hours from the current time and try again. | In **[!UICONTROL Edit run]** (More actions icon), set a send time at least 12 hours from now, then select **[!UICONTROL Activate]** again. [Learn more](ip-warmup-execution.md#activate-run) |
| **CJMRT-180038-403** | This run cannot be activated yet. Please activate the run only after all the previous runs have ended. | Check the status of the previous runs in the plan, and activate this run once all of them have ended. [Learn more](ip-warmup-execution.md#activate-run) |
| **CJMRT-180037-403** | The status transition from {from} to {to} is not allowed. | Check the status of the run in the plan and use an action available for it: activate a **[!UICONTROL Draft]** run, cancel a **[!UICONTROL Live]** run, or duplicate the run. [Learn more](ip-warmup-execution.md#run-statuses) |
| **CJMRT-180046-403** | The IP warmup plan cannot be marked as completed as the last activated run status is 'Live'. Please wait until the run has ended to mark the plan as completed. | Wait until the **[!UICONTROL Live]** run ends, then select **[!UICONTROL More]** > **[!UICONTROL Mark as completed]**. [Learn more](ip-warmup-execution.md#run-statuses) |
| **CJMRT-180058-403** | You cannot perform this action as you do not have the required permission. Contact your administrator to grant you the 'View Campaigns' permission for the campaign selected in the phase. | Ask your administrator to grant you that permission, or use **[!UICONTROL Replace]** to select a campaign for the phase that you can access. [Learn more](ip-warmup-plan.md) |
| **CJMRT-180059-403** | You cannot perform this action as you do not have the required permission. Contact your administrator to grant you the 'View Segments' permission for the audience associated with the campaign selected in the phase. | Ask your administrator to grant you that permission, or use **[!UICONTROL Replace]** to select a campaign for the phase whose audience you can access. [Learn more](ip-warmup-plan.md) |

## Run failures {#failures}

These errors occur when a run is cancelled or fails after it was activated.

See also [Define and activate the runs](ip-warmup-execution.md#define-runs).

| Error code | Message | How to fix |
|---|---|---|
| **CJMRT-180050-500** | The audience has not been evaluated. To enable retries for the run execution, define a retry run time in the IP warmup plan properties before duplicating the run. | Click the Properties icon next to the plan name and set a duration in the **[!UICONTROL Retry run time]** drop-down list. Then duplicate the run and activate it again. [Learn more](ip-warmup-execution.md#define-runs) |
| **CJMRT-180051-500** | The audience has not been evaluated. Duplicate the run and retry activation to a later date and time, or split to a new phase to alter the phase level configurations. | Duplicate the run and activate it again at a later date and time, or select **[!UICONTROL Split runs to a new phase]** to change the phase configuration. [Learn more](ip-warmup-execution.md#split-phase) |
| **CJMRT-180052-500** | An error occurred in the audience composition. Duplicate the run and retry activation to a later date and time, or split to a new phase to alter the phase level configurations. | Duplicate the run and activate it again at a later date and time, or select **[!UICONTROL Split runs to a new phase]** to change the phase configuration. [Learn more](ip-warmup-execution.md#split-phase) |
| **CJMRT-180053-500** | The run was cancelled as the number of qualified profiles did not meet the targeted amount, with the 'Cancel run with errors' option enabled. Duplicate the run and review the targeted profile count before proceeding with activation. | Duplicate the run and review the targeted profiles in **[!UICONTROL Edit run]**. Lower the number, or disable the **[!UICONTROL Cancel activated runs in case of errors]** option, then activate the run again. [Learn more](ip-warmup-execution.md#define-runs) |
| **CJMRT-180060-500** | The run failed as there are no qualified profiles. Select the 'Split runs to a new phase' option to choose a different campaign and audience. | Select **[!UICONTROL Split runs to a new phase]** from the More actions icon of the run, then select a different campaign for the new phase. [Learn more](ip-warmup-execution.md#split-phase) |
| **CJMRT-180054-500** | The server encountered an internal error and could not execute the run. Duplicate the run to schedule activation at a later date and time. | Duplicate the run, set a later **[!UICONTROL Send time]**, then activate it. [Learn more](ip-warmup-execution.md#define-runs) |

## Related topics {#related}

* [Get started with IP warmup plans](ip-warmup-gs.md)
* [IP warmup deliverability guide](ip-warmup-deliverability-guide.md)
* [Create IP warmup campaigns](ip-warmup-campaign.md)
* [Create an IP warmup plan](ip-warmup-plan.md)
* [Run the IP warmup plan](ip-warmup-execution.md)
* [Error codes reference](../building-journeys/error-codes-reference.md)

{{$include /help/_includes/do-not-localize/configuration/ai-augmented-ip-warmup-plan-errors.md}}
