---
solution: Journey Optimizer
product: journey optimizer
title: Custom channel, inbound action, and reporting dataset errors
description: Learn what common errors mean when you manage custom channel credentials, publish inbound actions, and add reporting datasets in Adobe Journey Optimizer, and how to fix them
feature: Channel Configuration, Reporting
topic: Administration
role: Admin
level: Experienced
keywords: error, troubleshooting, custom channel, inbound action, reporting, dataset
---
# Custom channel, inbound action, and reporting dataset errors {#channel-reporting-errors}

>[!BEGINSHADEBOX]

**On this page:** Find the cause and the fix for the errors that [!DNL Adobe Journey Optimizer] returns when you manage the credentials of a custom channel, publish an inbound action, or add a dataset to the reporting configuration.

>[!ENDSHADEBOX]

Errors use the prefixes **CJMRT** (custom channels), **CJMIAS** (inbound actions), and **CJMRPS** (reporting), followed by an error number and an HTTP status. For the other error code prefixes, see the [error codes reference](../building-journeys/error-codes-reference.md).

## Custom channels {#custom-channel}

These errors occur when you manage the API credentials (authentication) of a custom channel.

See also [Manage API credentials for custom channels](../custom-channel/custom-channel-api-credentials.md).

| Error code | Message | How to fix |
|---|---|---|
| **CJMRT-081517-403** | Authentication \"{authId}\" cannot be deactivated because it is associated with an active channel configuration. Update the channel configuration first and try again. | The credentials are used by an active channel configuration and cannot be deactivated. Update the channel configuration first, then deactivate the credentials. [Learn more](../custom-channel/custom-channel-api-credentials.md) |
| **CJMRT-081518-403** | The authentication cannot be activated because the associated channel \"{channelId}\" is not in an active state. Activate the channel first and try again. | The custom channel is not active, so its credentials cannot be activated. Activate the custom channel first. [Learn more](../custom-channel/get-started-custom-channel.md) |
| **CJMRT-081705-400** | A custom channel authentication with the name \"{name}\" already exists. Please use a unique name and try again. | A set of credentials with this name already exists. Enter a unique name. [Learn more](../custom-channel/custom-channel-api-credentials.md) |
| **CJMRT-081704-403** | The \"{operation}\" operation cannot be applied while the resource is in \"{status}\" status. | The status of the credentials does not allow the operation named in the message. Check the status of the credentials, and use an allowed operation. [Learn more](../custom-channel/custom-channel-api-credentials.md) |
| **CJMRT-081707-403** | Transitioning status from \"{from}\" to \"{to}\" is not allowed. | The status transition named in the message is not allowed. Check the current status of the credentials, and use an allowed transition. [Learn more](../custom-channel/custom-channel-api-credentials.md) |
| **CJMRT-081709-403** | Custom channel authentication \"{entityId}\" cannot be deleted while it is in \"{status}\" status. | The credentials cannot be deleted in their current status. Check the status of the credentials. [Learn more](../custom-channel/custom-channel-api-credentials.md) |

## Inbound actions {#inbound}

These errors and warnings occur when you publish a campaign or a journey that uses an inbound action (code-based experience, in-app message, content card, or web action).

See also [Troubleshoot inbound actions](../building-journeys/troubleshooting-inbound.md) and [Guardrails and limitations](../start/guardrails.md).

| Error code | Message | How to fix |
|---|---|---|
| **CJMIAS-0024-400** | Maximum number of allowed live inbound actions across campaigns and journeys has been reached. You need to stop previous inbound actions in order to activate new ones. Please contact Adobe Support for more details. | Your organization reached the maximum number of live inbound actions (500) across campaigns and journeys. Stop campaigns or journeys that use inbound actions you no longer need. [Learn more](../start/guardrails.md) |
| **CJMIAS-0027-400** | The selected audience is a newly created or updated edge segment. It can take up to one hour to activate it. Until then, eligible profiles can be excluded. | The selected audience is a new or updated edge audience, which can take up to one hour to activate (warning). Until then, eligible profiles can be excluded. [Learn more](../campaigns/campaign-audience.md) |
| **CJMIAS-0028-400** | The action cannot be published as no merge policy is active on the edge. You must enable Active-On-Edge option. <a href="https://experienceleague.adobe.com/docs/experience-platform/profile/merge-policies/ui-guide.html?lang=en">Learn more</a>. | No merge policy is active on the edge. Enable the Active-On-Edge option on a merge policy, then publish again. [Learn more](../code-based/code-based-prerequisites.md) |
| **CJMIAS-0029-400** | The action cannot be published as some decision policies are missing. Please check and try again. | A decision policy used by the action is missing. Check the decision policies of the action and recreate those that were deleted. [Learn more](../experience-decisioning/create-decision-policy.md) |
| **CJMIAS-0030-400** | The action cannot be published as some activity fields are invalid or missing. Please check and try again. | Some fields of the action are invalid or missing. Open the action and complete its fields. [Learn more](../campaigns/campaign-action.md) |
| **CJMIAS-0031-400** | The action cannot be published as channel configuration is missing or includes surfaces. Please fix the problem and try again. | The action has no channel configuration, or uses a surface. Select a channel configuration. [Learn more](../configuration/channel-surfaces.md) |

## Reporting datasets {#reporting}

These errors occur when you add datasets to the reporting configuration.

See also [Reporting and experimentation prerequisites](../reports/reporting-configuration.md).

| Error code | Message | How to fix |
|---|---|---|
| **CJMRPS-1046-400** | Dataset must contain at least one supported field group. | The dataset has no supported field group. Select or create a dataset that has at least one (Application Details, Commerce Details, or Web Details), in addition to the Experience Event - Proposition Interactions field group. [Learn more](../reports/reporting-configuration.md#add-datasets) |
| **CJMRPS-1048-400** | Dataset schema should be event type. | The schema of the dataset is not an event type. Select or create an event-type dataset. [Learn more](../reports/reporting-configuration.md#add-datasets) |
| **CJMRPS-1047-409** | Conflict. Dataset has been added already. | The dataset is already added to the reporting configuration. No action is needed. [Learn more](../reports/reporting-configuration.md#add-datasets) |
| **CJMRPS-1049-400** | The maximum limit of {limit} datasets has been reached. | You reached the maximum number of datasets of the reporting configuration. Remove a dataset you do not use, then add the new one. [Learn more](../reports/reporting-configuration.md#add-datasets) |
| **CJMRPS-1041-404** | Provisioning is pending for sandbox. | Provisioning of the sandbox is still pending. Wait until it completes, then add the dataset. [Learn more](../reports/reporting-configuration.md) |
| **CJMRPS-1045-400** | ARES provisioning is pending. Add dataset after provisioning is complete. | ARES provisioning is pending. Wait until provisioning is complete, then add the dataset. [Learn more](../reports/reporting-configuration.md) |
| **CJMRPS-1042-400** | Dataset not found. | The dataset cannot be found. Check that the dataset exists in the sandbox. [Learn more](../reports/reporting-configuration.md#add-datasets) |

## Related topics {#related}

* [Manage API credentials for custom channels](../custom-channel/custom-channel-api-credentials.md)
* [Troubleshoot inbound actions](../building-journeys/troubleshooting-inbound.md)
* [Reporting and experimentation prerequisites](../reports/reporting-configuration.md)
* [Error codes reference](../building-journeys/error-codes-reference.md)

{{$include /help/_includes/do-not-localize/configuration/ai-augmented-channel-reporting-errors.md}}
