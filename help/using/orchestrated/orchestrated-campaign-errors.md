---
solution: Journey Optimizer
product: journey optimizer
title: Orchestrated campaign errors
description: Learn what common errors mean when you build, test, schedule, and publish Orchestrated campaigns in Adobe Journey Optimizer, and how to fix them
feature: Campaigns, Monitoring
topic: Content Management
role: User
level: Intermediate
keywords: error, troubleshooting, orchestrated campaigns, CJMOC
version: Campaign Orchestration
---
# Orchestrated campaign errors {#orchestrated-campaign-errors}

>[!BEGINSHADEBOX]

**On this page:** Find the cause and the fix for the errors that [!DNL Adobe Journey Optimizer] returns when you build, test, schedule, publish, or trigger an Orchestrated campaign, grouped by feature.

>[!ENDSHADEBOX]

When an error occurs, the campaign logs and the alerts on the canvas show the error code and the message. Open the campaign logs to find the activity concerned. [Learn more about the logs](start-monitor-campaigns.md#logs-tasks)

Orchestrated campaign errors use the prefix **CJMOC**, followed by an error number and an HTTP status. For the other error code prefixes, see the [error codes reference](../building-journeys/error-codes-reference.md).

## Permissions and access {#access}

These errors occur when your user does not have the permission or the access needed to create, edit, publish, or trigger an Orchestrated campaign.

See also [Built-in permissions](../administration/ootb-permissions.md).

| Error code | Message | How to fix |
|---|---|---|
| **CJMOC-1001-403** | Unauthorized access to the resource. | Your user does not have the permission needed for this action. Ask your administrator to grant it on your product profile. [Learn more](../administration/ootb-permissions.md) |
| **CJMOC-1005-403** | You do not have access to required permission: {permission}. Check your permissions with your product administrator and try again. | Your user does not have the permission named in the message. Ask your administrator to add it to your product profile. To publish or trigger a campaign, you need the **[!UICONTROL Publish orchestrated campaigns]** permission. [Learn more](../administration/ootb-permissions.md) |
| **CJMOC-1004-403** | You do not have access to some attributes. Check your permissions with your product administrator and try again. | You do not have access to some of the attributes used by the campaign. Ask your administrator for access, or remove those attributes from the campaign. [Learn more](../administration/attribute-based-access.md) |
| **CJMOC-1215-403** | OLAC check failed for operation {operation} on resource {id}. | You do not have object-level access to the resource for this operation. Ask your administrator to grant it. [Learn more](../administration/object-based-access.md) |
| **CJMOC-1216-403** | OLAC check failed for create operation. | You do not have object-level access to create this object. Ask your administrator to grant it. [Learn more](../administration/object-based-access.md) |

## Campaign status and lifecycle {#status}

These errors occur when an action is not possible in the current status of the campaign, or when you try to unpublish a campaign that already started.

See also [Understand the campaign lifecycle](start-monitor-campaigns.md#lifecycle).

| Error code | Message | How to fix |
|---|---|---|
| **CJMOC-1201-400** | The orchestrated campaign version is not in Draft status or the orchestrated campaign ID is not set. Please check and try again. | The campaign is not in **[!UICONTROL Draft]** status, or its ID is not set. Check the campaign and its status. To start again from a Draft, duplicate the campaign. [Learn more](start-monitor-campaigns.md#lifecycle) |
| **CJMOC-1203-400** | The version for the orchestrated campaign id : {id} cannot be published as it is not in Draft status. | The campaign cannot be published because it is not in **[!UICONTROL Draft]** status. Check the campaign status. To start again from a Draft, duplicate the campaign. [Learn more](start-monitor-campaigns.md#lifecycle) |
| **CJMOC-6005-400** | Publication error: the orchestrated campaign current version is not in Draft status. | The publication failed because the current version of the campaign is not in **[!UICONTROL Draft]** status. Check the campaign status. To start again from a Draft, duplicate the campaign. [Learn more](start-monitor-campaigns.md#lifecycle) |
| **CJMOC-1202-400** | The current version for the orchestrated campaign id : {id} is in Live status. | The campaign is **[!UICONTROL Live]** and cannot be edited. Stop it, or use **[!UICONTROL Back to draft]** when it is available. Then edit the campaign and publish it again. [Learn more](start-monitor-campaigns.md#back-to-draft) |
| **CJMOC-6006-400** | Publication error: orchestrated campaign current version is running. It must be terminated before publishing the next version. | The campaign is still running. Stop it, or wait for it to finish, then publish the campaign again. [Learn more](start-monitor-campaigns.md#lifecycle) |
| **CJMOC-6039-500** | Side effect activity already started: {activityId} (channel: {activityChannel}). | A channel activity already started, so messages may have been sent. The campaign cannot go back to draft. Stop it and create a new campaign. [Learn more](start-monitor-campaigns.md#back-to-draft) |
| **CJMOC-6040-500** | This recurring orchestrated campaign has already started executing and cannot be unpublished. You can stop the campaign instead to prevent future executions while preserving execution history. | A recurring campaign that already started cannot go back to draft. Stop it to prevent future executions, or duplicate it to make changes. [Learn more](start-monitor-campaigns.md#back-to-draft) |

## Test mode {#test}

These errors occur when you start or stop a test of a campaign, or when you open the data of an activity that has not run.

See also [Test your campaign before publishing](start-monitor-campaigns.md#test).

| Error code | Message | How to fix |
|---|---|---|
| **CJMOC-2001-400** | Cannot start a test session for the orchestrated campaign version. The campaign version must be in Draft status. | You can start a test only while the campaign is in **[!UICONTROL Draft]** status. Check the campaign status, or duplicate the campaign. [Learn more](start-monitor-campaigns.md#test) |
| **CJMOC-2004-400** | Stop test session failed for orchestrated campaign version. The campaign version must be in Draft status. | The campaign must be in **[!UICONTROL Draft]** status to stop the test session. Check the campaign status, or duplicate the campaign. [Learn more](start-monitor-campaigns.md#test) |
| **CJMOC-2002-400** | Cannot start a test session for the orchestrated campaign version. The campaign version is already in Test. | A test is already running on this campaign. Stop it or restart it, then start a new test. [Learn more](start-monitor-campaigns.md#test) |
| **CJMOC-2005-400** | Stop test session failed for orchestrated campaign version. The campaign version must be in Test status. | No test is running on this campaign, so there is nothing to stop. Start a test first. [Learn more](start-monitor-campaigns.md#test) |
| **CJMOC-2006-400** | Start test session failed for orchestrated campaign version. No orchestration defined. | The campaign has no activities, so the test cannot start. Add activities to the canvas and save the campaign, then start the test. [Learn more](orchestrate-activities.md) |
| **CJMOC-2007-400** | Stop test session failed for orchestrated campaign version. No orchestration defined. | The campaign has no activities. Add activities to the canvas and save the campaign, then try again. [Learn more](orchestrate-activities.md) |
| **CJMOC-4205-400** | Orchestration for the orchestrated campaign id {id} is not defined. | The campaign has no activities. Add activities to the canvas and save the campaign. [Learn more](orchestrate-activities.md) |
| **CJMOC-2009-400** | Cannot fetch profiles data for activity {activity} in orchestratedCampaignVersion id {id}. The activity must have been executed at least once. | The activity has not run yet, so it has no data to show. Run the campaign in test so that the activity executes, then check its data again. [Learn more](start-monitor-campaigns.md#test) |

## Activities {#activities}

These errors occur when an activity is incomplete or disabled, or when the campaign exceeds the activity limits.

See also [Guardrails and limitations](guardrails.md#activities-limitations).

| Error code | Message | How to fix |
|---|---|---|
| **CJMOC-5000-400** | Activity {activityLabel} ({activityId}) has one or more transitions without attached activity. Please add required activities so that the transition is not empty. | Connect each outgoing transition of the activity to another activity, or delete the empty transition. [Learn more](orchestrate-activities.md) |
| **CJMOC-5005-400** | Activity {activityLabel} ({activityId}) has no field. Please select at least one field and try again. | The activity named in the message has no field. Open it and select at least one field. [Learn more](orchestrate-activities.md) |
| **CJMOC-5006-400** | Activity {activityLabel} ({activityId}) has no expression. Select an expression and try again. | The activity named in the message has no expression. Open it and select an expression. [Learn more](orchestrate-activities.md) |
| **CJMOC-5007-400** | Activity {activityLabel} ({activityId}) has no attribute. Please select at least one attribute and try again. | The activity named in the message has no attribute. Open it and select at least one attribute. [Learn more](orchestrate-activities.md) |
| **CJMOC-5008-400** | Activity {activityLabel} ({activityId}) is disabled. Please enable it and try again. | The activity named in the message is disabled. Enable the activity again, then retry. [Learn more](orchestrate-activities.md) |
| **CJMOC-5009-400** | Activity {activityLabel} ({activityId}) is paused. Please enable it and try again. | The activity named in the message is paused. Enable the activity again, then retry. [Learn more](orchestrate-activities.md) |
| **CJMOC-5003-400** | Activity {activityLabel} ({activityId}) has an empty query. Please check and try again. | The activity has an empty query. Open the activity and build the rule, or select an audience. [Learn more](build-query.md) |
| **CJMOC-5016-400** | Activity {activityLabel} ({activityId}) has no audience. Please select an audience and try again. | Open the **[!UICONTROL Read audience]** activity and select an audience. [Learn more](activities/read-audience.md) |
| **CJMOC-5022-400** | Read audience activity {activityLabel} ({activityId}) has a merge policy that does not match with campaign's. | The audience uses a different merge policy than the campaign. Select an audience that uses the merge policy of the campaign, or change the merge policy of the campaign. [Learn more](create-orchestrated-campaign.md) |
| **CJMOC-5011-400** | Activity {activityLabel} ({activityId}) has no targeting dimension. Please add a targeting dimension and try again. | Select a targeting dimension in the activity, or add a **[!UICONTROL Change dimension]** activity before it. [Learn more](target-dimension.md) |
| **CJMOC-5001-400** | Activity {activityLabel} ({activityId}) has no campaign. Please associate an orchestrated campaign to this activity and try again. | The channel activity has no message. Open the activity and create or select the message. [Learn more](activities/channels.md) |
| **CJMOC-5002-400** | The orchestrated campaign does not have any channel or Save audience activity. Please add a channel or Save audience activity and try again. | Add at least one channel activity or **[!UICONTROL Save audience]** activity to the campaign. [Learn more](activities/channels.md) |
| **CJMOC-5026-400** | Activity {activityLabel} ({activityId}) has no title or message. Please provide both and try again. | Enter both a title and a message in the **[!UICONTROL Alert]** activity. [Learn more](activities/alert.md) |
| **CJMOC-6017-400** | The inline campaign count exceeds the maximum allowed in the workflow. | A campaign can contain up to 10 channel activities. Reduce the number of channel activities, or split the delivery across several campaigns. [Learn more](guardrails.md#activities-limitations) |
| **CJMOC-5023-199** | Load file activity is not meant to be used in a scheduled campaign due to short data lifetime of uploaded file | Uploaded files have a short lifetime, so the **[!UICONTROL Load file]** activity is not recommended in a scheduled campaign. This is a warning. Use another data source for scheduled campaigns, or run the campaign once. [Learn more](activities/load-file.md) |
| **CJMOC-1226-400** | Profile Targeting Dimension {id} cannot be deleted: it is referenced by {count} active channel configuration(s). | The targeting dimension is used by active channel configurations. Deactivate or delete those channel configurations, then delete the dimension. [Learn more](target-dimension.md) |

## Schedule {#schedule}

These errors occur when the schedule of the campaign is missing, expired, or not valid.

See also [Schedule the campaign](create-orchestrated-campaign.md#schedule).

| Error code | Message | How to fix |
|---|---|---|
| **CJMOC-5012-400** | No schedule is defined for the orchestrated campaign. Please add a schedule and try again. | The campaign has no schedule. Define a schedule. [Learn more](create-orchestrated-campaign.md#schedule) |
| **CJMOC-5013-400** | The schedule of the orchestrated campaign has no event in the future. Please update the schedule and try again. | The schedule has no execution in the future. Update the start date, or extend the validity period of the schedule. [Learn more](create-orchestrated-campaign.md#schedule) |
| **CJMOC-5014-400** | The orchestrated campaign must not use fixed time when there is a recurring schedule. Please check the schedule and try again. | A recurring schedule cannot use a fixed time. Remove the fixed time, or use a one-time schedule. [Learn more](create-orchestrated-campaign.md#schedule) |
| **CJMOC-5015-400** | The orchestrated campaign schedule has a fixed time in the past. Please update the schedule and try again. | The fixed time of the schedule is in the past. Set a date and time in the future. [Learn more](create-orchestrated-campaign.md#schedule) |

## Signals and chained campaigns {#signal}

These errors occur when a campaign is triggered by a signal, from the API or from the **[!UICONTROL End]** activity of another campaign.

See also [Trigger Orchestrated campaigns using a signal](trigger-orchestrated-campaign.md).

| Error code | Message | How to fix |
|---|---|---|
| **CJMOC-6041-400** | Orchestrated campaigns cannot have both signal activity and recurring schedule. Signal-triggered and recurring campaigns are mutually exclusive. | A campaign cannot be both triggered by a signal and recurring. Choose one: a recurring schedule, or **[!UICONTROL Triggered by a signal]**. [Learn more](trigger-orchestrated-campaign.md#configure-signal) |
| **CJMOC-6042-400** | The campaign referenced by End activity '{endLabel}' ({targetCampaignName}) must be LIVE before this campaign can be published. | Publish the downstream campaign first, then publish this campaign. [Learn more](trigger-orchestrated-campaign.md#signal-end) |
| **CJMOC-6043-400** | The campaign referenced by End activity '{endLabel}' ({targetCampaignName}) is not set to Triggered by a signal and cannot be started from an End activity. Open the downstream campaign, set its schedule to Triggered by a signal, then try again. | Open the downstream campaign and set its schedule to **[!UICONTROL Triggered by a signal]**. [Learn more](trigger-orchestrated-campaign.md#signal-end) |
| **CJMOC-6044-400** | The campaign referenced by End activity '{endLabel}' (workflow id {targetWorkflowId}) does not exist or is not accessible. | Select an existing campaign in the **[!UICONTROL End]** activity, and check that you can access it. [Learn more](trigger-orchestrated-campaign.md#signal-end) |

## Waves {#waves}

These errors occur when a campaign sends messages in waves.

| Error code | Message | How to fix |
|---|---|---|
| **CJMOC-6045-400** | Waves are not supported for a recurring orchestrated campaign | Waves are not available for recurring campaigns. Remove the wave configuration, or use a one-time scheduled campaign. [Learn more](../delivery/send-using-waves.md) |
| **CJMOC-6046-400** | Waves are not supported for a signal-triggered orchestrated campaign | Waves are not available for signal-triggered campaigns. Remove the wave configuration, or use a one-time scheduled campaign. [Learn more](../delivery/send-using-waves.md) |
| **CJMOC-6047-400** | A wave is configured before the orchestrated campaign start | Set the start of the wave after the start of the campaign. [Learn more](../delivery/send-using-waves.md) |

## Related topics {#related}

* [Start and monitor the campaign](start-monitor-campaigns.md)
* [Guardrails and limitations](guardrails.md)
* [Orchestrated campaigns FAQ](orchestrated-campaigns-faq.md)
* [Error codes reference](../building-journeys/error-codes-reference.md)

{{$include /help/_includes/do-not-localize/orchestrated/ai-augmented-orchestrated-campaign-errors.md}}
