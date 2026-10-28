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

If the error persists after you follow the steps, note the error code, the message, the request ID, and the campaign, journey, or activity concerned, and keep the logs or screenshots. Then contact your administrator for a permission or access error, or [contact Adobe Support](../start/user-interface.md#support-ticket-guidelines) with these details. For all the support options, see [Getting support](../building-journeys/error-codes-reference.md#getting-support).

## Custom channels {#custom-channel}

These errors occur when you manage the API credentials (authentication) of a custom channel.

See also [Manage API credentials for custom channels](../custom-channel/custom-channel-api-credentials.md).

| Error code | Message | How to fix |
|---|---|---|
| **CJMRT-081517-403** | Authentication \"{authId}\" cannot be deactivated because it is associated with an active channel configuration. Update the channel configuration first and try again. | Update the channel configuration that uses the credentials, then deactivate them. [Learn more](../custom-channel/custom-channel-api-credentials.md) |
| **CJMRT-081518-403** | The authentication cannot be activated because the associated channel \"{channelId}\" is not in an active state. Activate the channel first and try again. | Activate the custom channel first, then activate the credentials. [Learn more](../custom-channel/get-started-custom-channel.md) |
| **CJMRT-081705-400** | A custom channel authentication with the name \"{name}\" already exists. Please use a unique name and try again. | Enter a unique name for the credentials. [Learn more](../custom-channel/custom-channel-api-credentials.md) |
| **CJMRT-081704-403** | The \"{operation}\" operation cannot be applied while the resource is in \"{status}\" status. | In **[!UICONTROL Administration]** > **[!UICONTROL Channels]** > **[!UICONTROL Channel builder]** > **[!UICONTROL API credentials]**, check the status of the credentials and use an operation that this status allows. [Learn more](../custom-channel/custom-channel-api-credentials.md) |
| **CJMRT-081707-403** | Transitioning status from \"{from}\" to \"{to}\" is not allowed. | In **[!UICONTROL Administration]** > **[!UICONTROL Channels]** > **[!UICONTROL Channel builder]** > **[!UICONTROL API credentials]**, check the current status of the credentials and use an allowed transition. [Learn more](../custom-channel/custom-channel-api-credentials.md) |
| **CJMRT-081709-403** | Custom channel authentication \"{entityId}\" cannot be deleted while it is in \"{status}\" status. | In **[!UICONTROL Administration]** > **[!UICONTROL Channels]** > **[!UICONTROL Channel builder]** > **[!UICONTROL API credentials]**, check the status of the credentials, then delete them once their status allows it. [Learn more](../custom-channel/custom-channel-api-credentials.md) |

## Inbound actions {#inbound}

These errors and warnings occur when you publish a campaign or a journey that uses an inbound action (code-based experience, in-app message, content card, or web action).

See also [Troubleshoot inbound actions](../building-journeys/troubleshooting-inbound.md) and [Guardrails and limitations](../start/guardrails.md).

| Error code | Message | How to fix |
|---|---|---|
| **CJMIAS-0024-400** | Maximum number of allowed live inbound actions across campaigns and journeys has been reached. You need to stop previous inbound actions in order to activate new ones. Please contact Adobe Support for more details. | Stop the campaigns or journeys that use inbound actions you no longer need, then publish again. [Learn more](../start/guardrails.md) |
| **CJMIAS-0027-400** | The selected audience is a newly created or updated edge segment. It can take up to one hour to activate it. Until then, eligible profiles can be excluded. | Warning. Wait up to one hour for the edge audience to activate. [Learn more](../campaigns/campaign-audience.md) |
| **CJMIAS-0028-400** | The action cannot be published as no merge policy is active on the edge. You must enable Active-On-Edge option. <a href="https://experienceleague.adobe.com/docs/experience-platform/profile/merge-policies/ui-guide.html?lang=en">Learn more</a>. | No merge policy is active on the edge. Enable the Active-On-Edge option on a merge policy, then publish again. [Learn more](../code-based/code-based-prerequisites.md) |
| **CJMIAS-0029-400** | The action cannot be published as some decision policies are missing. Please check and try again. | A decision policy used by the action is missing. Check the decision policies of the action and recreate those that were deleted. [Learn more](../experience-decisioning/create-decision-policy.md) |
| **CJMIAS-0030-400** | The action cannot be published as some activity fields are invalid or missing. Please check and try again. | Some fields of the action are invalid or missing. Open the action and complete its fields. [Learn more](../campaigns/campaign-action.md) |
| **CJMIAS-0031-400** | The action cannot be published as channel configuration is missing or includes surfaces. Please fix the problem and try again. | Select a channel configuration instead of a surface. [Learn more](../configuration/channel-surfaces.md) |

## Reporting datasets {#reporting}

These errors occur when you add datasets to the reporting configuration.

See also [Reporting and experimentation prerequisites](../reports/reporting-configuration.md).

| Error code | Message | How to fix |
|---|---|---|
| **CJMRPS-1046-400** | Dataset must contain at least one supported field group. | Select or create a dataset that includes the Experience Event - Proposition Interactions field group and at least one of Application Details, Commerce Details, or Web Details. [Learn more](../reports/reporting-configuration.md#add-datasets) |
| **CJMRPS-1048-400** | Dataset schema should be event type. | Select or create an event-type dataset. [Learn more](../reports/reporting-configuration.md#add-datasets) |
| **CJMRPS-1047-409** | Conflict. Dataset has been added already. | No action is needed. To confirm, open the list of datasets in **[!UICONTROL Administration]** > **[!UICONTROL Configurations]** > **[!UICONTROL Reporting]** > **[!UICONTROL Manage]**. [Learn more](../reports/reporting-configuration.md#add-datasets) |
| **CJMRPS-1049-400** | The maximum limit of {limit} datasets has been reached. | Remove a dataset you do not use from the reporting configuration, then add the new one. [Learn more](../reports/reporting-configuration.md#add-datasets) |
| **CJMRPS-1041-404** | Provisioning is pending for sandbox. | Wait until provisioning completes, then click **[!UICONTROL Add dataset]** again from the **[!UICONTROL Dataset]** tab. [Learn more](../reports/reporting-configuration.md) |
| **CJMRPS-1045-400** | ARES provisioning is pending. Add dataset after provisioning is complete. | Wait until provisioning completes, then click **[!UICONTROL Add dataset]** again from the **[!UICONTROL Dataset]** tab. [Learn more](../reports/reporting-configuration.md) |
| **CJMRPS-1042-400** | Dataset not found. | Check that the dataset exists in the sandbox, or create it before you add it. [Learn more](../reports/reporting-configuration.md#add-datasets) |

## Related topics {#related}

* [Manage API credentials for custom channels](../custom-channel/custom-channel-api-credentials.md)
* [Troubleshoot inbound actions](../building-journeys/troubleshooting-inbound.md)
* [Reporting and experimentation prerequisites](../reports/reporting-configuration.md)
* [Error codes reference](../building-journeys/error-codes-reference.md)

{{$include /help/_includes/do-not-localize/configuration/ai-augmented-channel-reporting-errors.md}}
