---
solution: Journey Optimizer
product: journey optimizer
title: Campaign errors
description: Learn what common errors mean when you configure, schedule, and activate Action and API-triggered campaigns in Adobe Journey Optimizer, and how to fix them
feature: Campaigns, Experimentation
topic: Content Management
role: User
level: Intermediate
keywords: error, troubleshooting, campaign, audience, schedule, experiment, rapid delivery
hide: true
---
# Campaign errors {#campaign-errors}

>[!BEGINSHADEBOX]

**On this page:** Find the cause and the fix for the errors and warnings that [!DNL Adobe Journey Optimizer] returns when you configure, schedule, or activate a campaign, grouped by feature.

>[!ENDSHADEBOX]

Campaign errors use the prefix **CJMCMP**, followed by an error number and an HTTP status. Codes with the status 200 are warnings. For the other error code prefixes, see the [error codes reference](../building-journeys/error-codes-reference.md).

## Audience {#audience}

These errors and warnings occur when you select the audience of a campaign and its identity type.

See also [Define the Action campaign audience](campaign-audience.md).

| Error code | Message | How to fix |
|---|---|---|
| **CJMCMP-2000-400** | The audience is required | Select an audience for the campaign. [Learn more](campaign-audience.md) |
| **CJMCMP-2025-400** | Cannot update the audience for an activated campaign | The audience cannot be changed once the campaign is activated. Create a new version of the campaign, or duplicate it, then change the audience. [Learn more](manage-campaigns.md#modify) |
| **CJMCMP-2028-400**, **CJMCMP-2031-400**, **CJMCMP-2061-400** | Permission denied for the audience<br/>You do not have permissions to perform this action. Contact your administrator to set OLAC permissions, and try again<br/>You do not have required permissions to perform this action. Contact your administrator to grant you access. | Your user does not have the permission on the audience or on the campaign. Ask your administrator to grant the permission or the object-level access. [Learn more](../administration/object-based-access.md) |
| **CJMCMP-2060-200** | The selected audience has not been evaluated yet. The audience must be evaluated before a campaign can be activated | The selected audience has not been evaluated yet (warning). Wait until the audience is evaluated, then activate the campaign. [Learn more](campaign-audience.md) |
| **CJMCMP-2075-400**, **CJMCMP-2077-400**, **CJMCMP-2078-400**, **CJMCMP-2080-400** | The use of audiences and attributes from Audience Composition is currently unavailable for use with Healthcare Shield or Privacy and Security Shield<br/>The use of audiences and attributes from custom uploads (CSV files) and Federated Audience Composition is currently unavailable for use with Healthcare Shield<br/>The use of audiences and attributes from custom uploads (CSV files) and Federated Audience Composition is currently unavailable for use with Privacy and Security Shield<br/>The use of audiences and attributes from Federated Audience Composition is currently unavailable for use with Healthcare Shield | Audiences and attributes from audience composition, federated audience composition, or CSV uploads cannot be used with Healthcare Shield or Privacy and Security Shield. Select another audience. [Learn more](campaign-audience.md) |
| **CJMCMP-2081-400**, **CJMCMP-2082-400**, **CJMCMP-2083-400** | The use of audiences and attributes from Federated Audience Composition is currently unavailable for use with Privacy and Security Shield<br/>The use of audiences and attributes from custom uploads (CSV files) is currently unavailable for use with Healthcare Shield<br/>The use of audiences and attributes from custom uploads (CSV files) is currently unavailable for use with Privacy and Security Shield | Audiences and attributes from federated audience composition or CSV uploads cannot be used with Healthcare Shield or Privacy and Security Shield. Select another audience. [Learn more](campaign-audience.md) |
| **CJMCMP-2024-400** | A new profile is not allowed for the provisioned campaign | Creating new profiles is not allowed for this campaign. Turn off the option that creates profiles, and use an audience of existing profiles. [Learn more](api-triggered-campaign-audience.md) |

## Action and channel configuration {#action}

These errors occur when you configure the action of a campaign.

See also [Configure the campaign action](campaign-action.md).

| Error code | Message | How to fix |
|---|---|---|
| **CJMCMP-2119-400** | Channel surfaces are now deprecated. The current surface cannot be used anymore for new actions. Please select a channel configuration instead | Surfaces are deprecated. Select a channel configuration instead. [Learn more](campaign-action.md) |
| **CJMCMP-2104-400**, **CJMCMP-2201-400** | The message is required<br/>Message ID is required | The action has no message. Create or select the message. [Learn more](campaign-action.md) |
| **CJMCMP-2202-400** | The message has not been published | The message is not published. Publish the message, then activate the campaign. [Learn more](review-activate-campaign.md) |
| **CJMCMP-2105-400**, **CJMCMP-2115-400** | The {channel} channel is not allowed for the provided campaign type<br/>The {channel} channel bound is not allowed | The channel is not available for this type of campaign. Select a channel that the campaign type supports. [Learn more](campaign-action.md) |
| **CJMCMP-2074-400** | Priority can only be in the range of 0-100. Priority is disabled for Transactional campaigns. | Enter a priority from 0 to 100. Priority is not available for transactional campaigns. [Learn more](campaign-action.md#multi-action) |

## Schedule and approval {#schedule}

These errors occur when you schedule or activate a campaign.

See also [Schedule the Action campaign](campaign-schedule.md) and [Review and activate the campaign](review-activate-campaign.md).

| Error code | Message | How to fix |
|---|---|---|
| **CJMCMP-2017-400** | The campaign schedule is required | Define the schedule of the campaign. [Learn more](campaign-schedule.md) |
| **CJMCMP-2120-400** | The selected schedule is invalid and will never be fired. Please update and try again. | The schedule will never run. Set a start date in the future, and an end date after the start date. [Learn more](campaign-schedule.md) |
| **CJMRT-150001-400** | The schedule will never fire for {triggerExpression}. Please update. | The schedule never produces an execution, for example because its end date is in the past. Update the start date, end date or frequency so that at least one execution is in the future. [Learn more](campaign-schedule.md) |
| **CJMRT-150002-400** | The End time {endTime} must be set after the Start time {startTime} | The end time is not after the start time. Set an end time later than the start time. [Learn more](campaign-schedule.md#set-an-end-date) |
| **CJMCMP-2309-400** | The inbound schedule does not match with the campaign schedule | The schedule of the action does not match the schedule of the campaign. Align them. [Learn more](campaign-schedule.md) |
| **CJMCMP-2121-400** | The campaign is not approved | The campaign is not approved. Request approval, wait for it, then activate the campaign. [Learn more](../test-approve/gs-approval.md) |
| **CJMCMP-2052-400** | The draft version has already been created | A draft version of the campaign already exists. Open it from the campaign list with **[!UICONTROL Open draft version]**. [Learn more](manage-campaigns.md#statuses) |

## Rapid delivery {#rapid}

These errors occur when you turn on rapid delivery mode for a push campaign.

See also [Enable Rapid delivery mode](campaign-action.md).

| Error code | Message | How to fix |
|---|---|---|
| **CJMCMP-2310-400**, **CJMCMP-2311-400**, **CJMCMP-2312-400** | The rapid delivery mode cannot be enabled for a recurring schedule<br/>The rapid delivery mode cannot be enabled for a headless campaign<br/>The rapid delivery mode cannot be enabled for an experimental campaign | Rapid delivery mode cannot be used with a recurring campaign, a headless campaign, or a campaign with an experiment. Turn off rapid delivery, or change the campaign. [Learn more](campaign-action.md) |
| **CJMCMP-2030-400**, **CJMCMP-2041-400** | The audience segment cannot be larger than 30M for rapid delivery<br/>The audience composition is not available for the campaign publication in rapid delivery mode | Rapid delivery mode is limited to audiences of up to 30M profiles, and does not accept audiences from audience composition. Select another audience, or turn off rapid delivery. [Learn more](campaign-action.md) |

## Content experiments {#experiment}

These errors occur when you configure a content experiment on a campaign.

See also [Create a content experiment](../content-management/content-experiment.md).

| Error code | Message | How to fix |
|---|---|---|
| **CJMCMP-2019-400**, **CJMCMP-2036-400** | The experiment treatment is required<br/>At least one experiment treatment is required | Define at least one treatment for the experiment. [Learn more](../content-management/content-experiment.md#treatment-experiment) |
| **CJMCMP-2037-400** | The success metric is required | Select a success metric for the experiment. [Learn more](../content-management/content-experiment.md#configure-experiment) |
| **CJMCMP-2038-400** | Only one holdout is allowed | An experiment can have only one holdout. [Learn more](../content-management/content-experiment.md) |
| **CJMCMP-2039-400**, **CJMCMP-2040-400** | The treatment percentage is not allowed for the uniform allocation<br/>The treatment percentage is required for the custom allocation | Set a percentage for each treatment only with a custom allocation, and do not set it with a uniform allocation. [Learn more](../content-management/content-experiment.md#configure-experiment) |
| **CJMCMP-2058-400** | The experiment dimension entered must be an URL | For clicks or page views, the dimension must be a URL. Enter the URL. [Learn more](../content-management/content-experiment.md#configure-experiment) |
| **CJMCMP-2012-400**, **CJMCMP-2009-400**, **CJMCMP-2059-400** | The campaign already has an experiment<br/>The campaign status doesn't allow to create an experiment<br/>The experiment is not allowed | A campaign can have only one experiment, and an experiment cannot be created in every campaign status. Edit the existing experiment, or create the experiment while the campaign is in draft. [Learn more](../content-management/content-experiment.md) |

## Related topics {#related}

* [Access and manage campaigns](manage-campaigns.md)
* [Review and activate an Action campaign](review-activate-campaign.md)
* [Work with API-triggered campaigns](api-triggered-campaigns.md)
* [Error codes reference](../building-journeys/error-codes-reference.md)

{{$include /help/_includes/do-not-localize/campaigns/ai-augmented-campaign-errors.md}}
