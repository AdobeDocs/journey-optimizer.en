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
hide: true
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
| **CJMRT-180001-415**, **180002-422** | This file format is not supported. Supported formats are: .xls and .xlsx.<br/>The IP warmup plan is missing. Please upload your plan in an .xls or .xlsx file. | Upload the plan as an Excel file (.xls or .xlsx). [Learn more](ip-warmup-plan.md#prepare-file) |
| **CJMRT-180003-400**, **180004-400**, **180011-400**, **180012-400** | The file could not be uploaded. Please enter the information in the correct format, as provided in the template.<br/>The 'Properties' and 'Value' parameters provided in the Warmup Plan sheet are missing or incorrectly formatted. Please enter the information in the correct format, as provided in the template.<br/>There are errors in the 'Warmup Plan' sheet of the plan. Please enter the information in the correct format, as provided in the template.<br/>There are errors in the 'Custom Domain Group' sheet of the plan. Please enter the information in the correct format, as provided in the template. | The plan does not follow the template. Fill in the **[!UICONTROL Warmup Plan]** and **[!UICONTROL Custom Domain Group]** sheets exactly as in the template, including the properties and values. Download the template again if needed. [Learn more](ip-warmup-plan.md#prepare-file) |
| **CJMRT-180005-400**, **180006-400**, **180007-400**, **180008-400** | The phase number could not be determined. Please enter the information in the correct format, as provided in the template.<br/>The run number is missing from the Warmup Plan sheet. Please enter the information in the correct format, as provided in the template.<br/>The phase number is invalid. Please enter the information in the correct format, as provided in the template.<br/>The run number is invalid. Please enter the information in the correct format, as provided in the template. | The phase number or the run number is missing or not valid. Enter them in the format of the template. [Learn more](ip-warmup-plan.md#prepare-file) |
| **CJMRT-180009-400**, **180013-400** | The target volume for domain group {domainGroup} is invalid. Please enter the information in the correct format, as provided in the template.<br/>The custom domain group provided is invalid. Please enter the information in the correct format, as provided in the template. | A target volume or a custom domain group is not valid. Enter them in the format of the template. [Learn more](ip-warmup-plan.md#prepare-file) |
| **CJMRT-180010-400**, **180014-400** | The domain group provided is neither a global nor a custom domain group defined in the plan. Define custom domain groups and re-upload the plan.<br/>Global domain groups have been included into the 'Custom Domain Group' sheet. Please ensure that only custom domain groups are provided and re-upload the plan. | Define each custom domain group in the **[!UICONTROL Custom Domain Group]** tab, and do not repeat the out-of-the-box domain groups there. Then upload the plan again. [Learn more](ip-warmup-plan.md#custom-domain-group-tab) |

## Channel configuration and campaigns {#config-campaign}

These errors occur when you select the channel configuration of the plan and the campaign of a phase.

See also [Create IP warmup campaigns](ip-warmup-campaign.md).

| Error code | Message | How to fix |
|---|---|---|
| **CJMRT-180015-400**, **180016-400**, **180017-400** | The selected surface is not 'Active'. Please select an 'Active' channel surface.<br/>The selected surface is not supported as it does not contain the 'Email' channel. Please select a valid surface.<br/>The selected surface is not supported as it is not a 'Marketing' type surface. Please select a valid surface. | Select an active channel configuration that has the email channel and is of the marketing type. [Learn more](ip-warmup-campaign.md) |
| **CJMRT-180018-400**, **180019-400**, **180020-400** | The channel surface is missing. Please select a channel surface for the IP warmup plan.<br/>The channel surface is invalid. Please select a valid channel surface with domains associated.<br/>The channel surface is invalid. Please select a valid channel surface with IP pools associated. | Select a channel configuration for the plan. It must have domains and IP pools associated. [Learn more](ip-warmup-plan.md) |
| **CJMRT-180021-409** | The IP warmup plan name {name} is already in use. Please provide a unique name. | An IP warmup plan with this name already exists. Enter a unique name. [Learn more](ip-warmup-plan.md) |
| **CJMRT-180022-400** | The selected retry period is invalid. Please select a value between {minPeriod} and {maxPeriod} minutes. | Select a retry period within the range shown in the message (in minutes). [Learn more](ip-warmup-execution.md#define-runs) |
| **CJMRT-180023-400**, **180024-400**, **180025-400** | The selected campaign is invalid. Please select a campaign configured for IP warmup use case.<br/>The selected campaign is not 'Live'. Please select a 'Live' campaign only.<br/>The selected campaign does not contain any audience. Please select a campaign with an audience selected. | Select a live campaign with an audience, and with the **[!UICONTROL IP warmup plan activation]** option enabled. [Learn more](ip-warmup-campaign.md) |
| **CJMRT-180026-400**, **180027-403** | The selected campaign is invalid. Please select a campaign with the same email surface as of the IP warmup plan.<br/>The selected campaign is already in use in another IP warmup plan. Please select or create another campaign. | Select a campaign that uses the same email channel configuration as the plan, and that is not used in another IP warmup plan. [Learn more](ip-warmup-campaign.md) |

## Phases and domain groups {#phases}

These errors occur when you define the phases of the plan and select domain groups.

See also [Define the phases](ip-warmup-execution.md#define-phases).

| Error code | Message | How to fix |
|---|---|---|
| **CJMRT-180028-400**, **180029-400**, **180030-400**, **180031-400** | The custom domain group mapping was not provided. Please ensure custom domain groups are mapped correctly.<br/>The domain groups are invalid. Please ensure no additional domain groups are provided if 'All' domain group is selected.<br/>No domain groups were provided. Please provide at least one domain group to proceed.<br/>The domain group and associated domains are invalid. Please check and try again. | The domain groups of the phase are missing or not valid. Select at least one domain group. If you select the **[!UICONTROL All]** group, do not select other groups. [Learn more](ip-warmup-execution.md#define-phases) |
| **CJMRT-180032-400**, **180033-400** | The domain group is invalid. Please select a domain group which is part of the global or custom domain groups defined in the IP warmup plan.<br/>The domain group is invalid. Select a domain group which matches with the domain groups defined for this phase. | Select a domain group that is defined in the plan, and that matches the domain groups defined for this phase. [Learn more](ip-warmup-execution.md#define-phases) |
| **CJMRT-180056-400**, **180057-400** | The domain {domain} is already included in another domain group used in the IP warmup plan. Please ensure each domain is associated with only one domain group.<br/>The domain {domain} and {count} others are already included in another domain group used in the IP warmup plan. Please ensure each domain is associated with only one domain group. | A domain is in more than one domain group. Make sure each domain belongs to only one domain group. [Learn more](ip-warmup-plan.md#custom-domain-group-tab) |
| **CJMRT-180043-403**, **180044-403**, **180045-403** | This plan cannot be deleted. Only plans with the status 'Not started' can be deleted.<br/>This phase cannot be deleted. Only phases with no activated run can be deleted.<br/>This run cannot be deleted. Only runs with the status 'Draft' can be deleted. | A plan, phase, or run can be deleted only in some statuses: a plan that is not started, a phase with no activated run, a run in **[!UICONTROL Draft]** status. [Learn more](ip-warmup-execution.md#define-phases) |
| **CJMRT-180047-400**, **180048-400** | You cannot split a phase on its first run. Try splitting the phase from another run or add a run below.<br/>You cannot split the phase here. Only runs with the status 'Draft' can be split to a new phase. | You cannot split a phase on its first run, and only runs in **[!UICONTROL Draft]** status can be split. Split from another run, or add a run below. [Learn more](ip-warmup-execution.md#split-phase) |

## Runs and activation {#runs}

These errors occur when you define and activate the runs of a phase.

See also [Define and activate the runs](ip-warmup-execution.md#define-runs) and [Check the run statuses](ip-warmup-execution.md#run-statuses).

| Error code | Message | How to fix |
|---|---|---|
| **CJMRT-180034-400**, **180035-400**, **180040-400** | The number of targeted profiles is invalid. Please ensure the number entered is not negative.<br/>The total number of targeted profiles cannot be equal to zero. Please provide a valid number and try again.<br/>The 'Last engagement' period cannot be negative. Please provide a valid period and try again. | Enter a number of targeted profiles greater than zero, and an engagement period that is not negative. [Learn more](ip-warmup-execution.md#define-runs) |
| **CJMRT-180036-400**, **180039-403** | The 'Send time' value provided is invalid. Please set the send time to at least 12 hours from the current time.<br/>This run cannot be activated. Please set the send time to at least 12 hours from the current time and try again. | Each run must be activated at least 12 hours before its send time. Set a send time at least 12 hours from now. [Learn more](ip-warmup-execution.md#activate-run) |
| **CJMRT-180038-403** | This run cannot be activated yet. Please activate the run only after all the previous runs have ended. | Activate a run only after all the previous runs have ended. [Learn more](ip-warmup-execution.md#activate-run) |
| **CJMRT-180037-403** | The status transition from {from} to {to} is not allowed. | The status change is not allowed for this run. Check the status of the run. [Learn more](ip-warmup-execution.md#run-statuses) |
| **CJMRT-180046-403** | The IP warmup plan cannot be marked as completed as the last activated run status is 'Live'. Please wait until the run has ended to mark the plan as completed. | The last activated run is still **[!UICONTROL Live]**. Wait until it ends, then mark the plan as completed. [Learn more](ip-warmup-execution.md#run-statuses) |
| **CJMRT-180058-403**, **180059-403** | You cannot perform this action as you do not have the required permission. Contact your administrator to grant you the 'View Campaigns' permission for the campaign selected in the phase.<br/>You cannot perform this action as you do not have the required permission. Contact your administrator to grant you the 'View Segments' permission for the audience associated with the campaign selected in the phase. | You do not have the permission needed on the campaign or the audience of the phase. Ask your administrator for the permission named in the message. [Learn more](ip-warmup-plan.md) |

## Run failures {#failures}

These errors occur when a run is cancelled or fails after it was activated.

See also [Define and activate the runs](ip-warmup-execution.md#define-runs).

| Error code | Message | How to fix |
|---|---|---|
| **CJMRT-180050-500** | The audience has not been evaluated. To enable retries for the run execution, define a retry run time in the IP warmup plan properties before duplicating the run. | The audience was not evaluated in time. Define a retry time window in the plan properties, then duplicate the run and activate it again. [Learn more](ip-warmup-execution.md#define-runs) |
| **CJMRT-180051-500**, **180052-500** | The audience has not been evaluated. Duplicate the run and retry activation to a later date and time, or split to a new phase to alter the phase level configurations.<br/>An error occurred in the audience composition. Duplicate the run and retry activation to a later date and time, or split to a new phase to alter the phase level configurations. | The audience was not evaluated or the audience composition failed. Duplicate the run and activate it again at a later date and time, or split the run to a new phase. [Learn more](ip-warmup-execution.md#split-phase) |
| **CJMRT-180053-500** | The run was cancelled as the number of qualified profiles did not meet the targeted amount, with the 'Cancel run with errors' option enabled. Duplicate the run and review the targeted profile count before proceeding with activation. | The run was cancelled because fewer profiles qualified than targeted, and the **[!UICONTROL Cancel activated runs in case of errors]** option is enabled. Duplicate the run and review the number of targeted profiles before you activate it again. [Learn more](ip-warmup-execution.md#define-runs) |
| **CJMRT-180060-500** | The run failed as there are no qualified profiles. Select the 'Split runs to a new phase' option to choose a different campaign and audience. | No profile qualified for the run. Split the run to a new phase and select a different campaign and audience. [Learn more](ip-warmup-execution.md#split-phase) |
| **CJMRT-180054-500** | The server encountered an internal error and could not execute the run. Duplicate the run to schedule activation at a later date and time. | The run could not be executed because of an internal error. Duplicate the run and schedule it at a later date and time. [Learn more](ip-warmup-execution.md#define-runs) |

## Related topics {#related}

* [Get started with IP warmup plans](ip-warmup-gs.md)
* [IP warmup deliverability guide](ip-warmup-deliverability-guide.md)
* [Create IP warmup campaigns](ip-warmup-campaign.md)
* [Create an IP warmup plan](ip-warmup-plan.md)
* [Run the IP warmup plan](ip-warmup-execution.md)
* [Error codes reference](../building-journeys/error-codes-reference.md)

{{$include /help/_includes/do-not-localize/configuration/ai-augmented-ip-warmup-plan-errors.md}}
