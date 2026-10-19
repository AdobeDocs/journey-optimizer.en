---
solution: Journey Optimizer
product: journey optimizer
title: Journey validation errors
description: Learn what common journey validation errors mean in Adobe Journey Optimizer and how to fix them
feature: Journeys, Monitoring
topic: Content Management
role: User
level: Intermediate
keywords: error, validation, journey, publish, troubleshooting, AJOJAS
---
# Journey validation errors {#journey-validation-errors}

>[!BEGINSHADEBOX]

**On this page:** Find the cause and the fix for the validation errors that [!DNL Adobe Journey Optimizer] returns when you validate, test, or publish a journey, grouped by the activity or rule involved.

>[!ENDSHADEBOX]

When you select **[!UICONTROL Validate]** in the journey header, or try to test or publish a journey, [!DNL Journey Optimizer] checks the journey and lists any errors in the **[!UICONTROL Alerts]** panel. [Learn more about journey validation](publish-journey.md#validate)

Validation errors use the prefix **AJOJAS** (Journey Authoring Service), followed by an error number and an HTTP status. For example, `AJOJAS-2030-400` is a missing wait duration. Most messages name the activity concerned, so you can select it on the canvas and fix its configuration. For the other error code prefixes, see the [error codes reference](error-codes-reference.md).

## Journey structure {#structure}

These errors occur when the journey has no entry activity or has activities in a layout that is not supported.

See also [Troubleshoot journey errors](troubleshooting.md#canvas-errors) and [Best practices before journey activation](error-codes-reference.md#journey-best-practices).

| Error code | Message | How to fix |
|---|---|---|
| **AJOJAS-1000-400** | No initial node found in node graph | The journey has no entry activity. Add an **[!UICONTROL Event]**, **[!UICONTROL Business event]**, **[!UICONTROL Read audience]**, or **[!UICONTROL Audience qualification]** activity as the first activity. [Learn more](journey-types-selection.md) |
| **AJOJAS-3018-400** | Unsupported transitions configuration in node '{nodeId}': only events can be put in parallel | Only event and **[!UICONTROL Wait]** activities can be placed in parallel after an activity. Place the other activities one after the other. [Learn more](using-the-journey-designer.md#paths) |
| **AJOJAS-3027-400** | Event timeout already defined in node '{nodeId}': timeout defined in node '{timeoutNodeId}' not supported: only one timeout can be defined for events in parallel | When events are in parallel, only one timeout can be defined. Keep the timeout on one event, or place the events one after the other. [Learn more](general-events.md#events-specific-time) |
| **AJOJAS-3028-403** | Timeout on initial event '{eventId}' is not allowed | Disable the timeout on the first event of the journey. [Learn more](general-events.md#events-specific-time) |

## Read audience and identity namespace {#read-audience}

These errors occur when the Read audience activity is incomplete or misplaced, or when the journey has no identity namespace.

See also [Guardrails and recommendations](read-audience.md#must-read), [Troubleshooting](read-audience.md#audience-count-mismatch), and [Read audience limitations](limitations.md#read-audiences-limitations).

| Error code | Message | How to fix |
|---|---|---|
| **AJOJAS-2007-400** | Read segment: missing recurrence policy definition | The schedule of the **[!UICONTROL Read audience]** activity has no recurrence. Open the activity, go to **[!UICONTROL Schedule]**, and set the recurrence. [Learn more](read-audience.md#schedule) |
| **AJOJAS-2008-400** | Read segment: missing timeOfDay in recurrence policy | The schedule of the **[!UICONTROL Read audience]** activity has no time of day. Open the activity, go to **[!UICONTROL Schedule]**, and set the time of day. [Learn more](read-audience.md#schedule) |
| **AJOJAS-2009-400** | Read segment: missing startDate for recurring journey | The schedule of the **[!UICONTROL Read audience]** activity has no start date. Open the activity, go to **[!UICONTROL Schedule]**, and set the start date. [Learn more](read-audience.md#schedule) |
| **AJOJAS-3003-400** | Multiple read segment nodes detected. Only one allowed, after start or business event | A journey can have only one **[!UICONTROL Read audience]** activity. Keep one. To target several audiences, combine them into a single audience first. [Learn more](read-audience.md) |
| **AJOJAS-3005-400** | Read segment node can only have one parent node: start or a business event | The **[!UICONTROL Read audience]** activity has more than one incoming path. Keep a single path into it, from the journey start or a business event, and remove any other path that leads into it. [Learn more](read-audience.md) |
| **AJOJAS-3006-400** | Read segment node only allowed after start or business event | The **[!UICONTROL Read audience]** activity is placed after another activity. Move it so it is the first activity of the journey, or right after a business event. [Learn more](read-audience.md) |
| **AJOJAS-3013-400** | Missing identity namespace, required for read segment journey | The journey has no identity namespace. Open the **[!UICONTROL Read audience]** activity and select one in the **[!UICONTROL Namespace]** field. [Learn more](read-audience.md) |
| **AJOJAS-3017-400** | Missing identity namespace, required for journey using profile update action | The journey uses a profile update action, so it needs an identity namespace. Open the first activity (**[!UICONTROL Read audience]**, **[!UICONTROL Audience qualification]**, or event) and select it. [Learn more](read-audience.md) |

## Activity compatibility {#compatibility}

These errors occur when a journey combines activities that cannot be used together, such as Adobe Campaign actions with Read audience or Audience qualification.

See also [General actions limitations](limitations.md#action-limitations) and [Adobe Campaign guardrails](../start/guardrails.md#ac-g).

| Error code | Message | How to fix |
|---|---|---|
| **AJOJAS-3001-403** | ACS action not allowed in read segment journey | [Adobe Campaign Standard](using-adobe-campaign-standard.md) actions cannot be used with **[!UICONTROL Read audience]**. Remove the Campaign Standard action, or start the journey with an event. |
| **AJOJAS-3004-403** | ACC action not allowed in read segment journey | [Adobe Campaign v7/v8](using-adobe-campaign-v7-v8.md) actions cannot be used with **[!UICONTROL Read audience]**. Remove the Campaign Classic action, or start the journey with an event. |
| **AJOJAS-3007-403** | ACS action and segment qualification can't be used in the same journey | [Adobe Campaign Standard](using-adobe-campaign-standard.md) actions cannot be used with **[!UICONTROL Audience qualification]**. Remove the Campaign Standard action, or replace it with a built-in channel action. |
| **AJOJAS-3009-403** | ACC action and segment qualification can't be used in the same journey | [Adobe Campaign v7/v8](using-adobe-campaign-v7-v8.md) actions cannot be used with **[!UICONTROL Audience qualification]**. Remove the Campaign Classic action, or replace it with a built-in channel action. |
| **AJOJAS-3010-403** | ACS and message actions can't be mixed in the same journey | Use only [Campaign Standard](using-adobe-campaign-standard.md) actions, or only built-in channel actions, in the same journey. [Campaign v7/v8](using-adobe-campaign-v7-v8.md) actions can be used with built-in channel actions. |
| **AJOJAS-3002-403** | Jump action not allowed in read segment journey | A **[!UICONTROL Jump]** activity cannot be used in the same journey as a **[!UICONTROL Read audience]** activity. Remove the Jump, or start the journey with an event. [Learn more](jump.md#jump-limitations) |

## Action activities {#actions}

These errors occur when a channel action, a custom action, or an Adobe Campaign Standard action is incomplete or uses an option that is no longer supported.

See also [Troubleshoot errors in activities](troubleshooting.md#activity-errors), [Troubleshoot your custom actions](../action/troubleshoot-custom-action.md), and [Custom actions limitations](limitations.md#custom-actions-limitations).

| Error code | Message | How to fix |
|---|---|---|
| **AJOJAS-2014-400** | '{messageType}' message action in node '{nodeId}': missing message id | The channel action has no message. Open the activity and select or create the message. [Learn more](journey-action.md) |
| **AJOJAS-2065-400** | Surfaces are deprecated. Please use channel configurations instead | Open each channel action that uses a surface and select a channel configuration instead. [Learn more](../configuration/channel-surfaces.md) |
| **AJOJAS-6003-403** | Send time optimization for email is not included in the '{packageName}' package. To use this feature, upgrade to a package that supports it. | Your license package does not include send time optimization for email. Turn it off on the email action, or contact your Adobe representative about upgrading. [Learn more](send-time-optimization.md) |
| **AJOJAS-6004-403** | Send time optimization for push channel is not included in the '{packageName}' package. To use this feature, upgrade to a package that supports it. | Your license package does not include send time optimization for push. Turn it off on the push action, or contact your Adobe representative about upgrading. [Learn more](send-time-optimization.md) |
| **AJOJAS-2021-400** | Custom action in node '{nodeId}': missing expression mapping | A parameter of the custom action has no value. Open the activity and set each mandatory parameter to a constant, a field, or an expression. [Learn more](using-custom-actions.md) |
| **AJOJAS-2012-400** | ACS message action in node '{nodeId}': address parameter '{addressParam}' can't be mapped (no expression defined) | Open the Campaign Standard action and map the address to a field, constant, or expression. [Learn more](using-adobe-campaign-standard.md) |
| **AJOJAS-2013-400** | ACS message action in node '{nodeId}': personalization parameter '{personalizationParam}' can't be mapped (no expression defined) | Open the Campaign Standard action and map the personalization parameter named in the message to a field, constant, or expression. [Learn more](using-adobe-campaign-standard.md) |

## Update profile {#update-profile}

These errors occur when the Update profile activity does not have a complete schema, dataset, and attribute configuration.

See also [Guardrails and limitations](update-profiles.md#guardrails).

| Error code | Message | How to fix |
|---|---|---|
| **AJOJAS-2022-400** | Profile update action in node '{nodeId}': missing fields / XDM information | Open the **[!UICONTROL Update profile]** activity. Select the schema, then the profile-enabled dataset, then the attributes to update. [Learn more](update-profiles.md) |
| **AJOJAS-2023-400** | Profile update action in node '{nodeId}': missing schema id in XDM information | The schema is missing from the profile update. Open the **[!UICONTROL Update profile]** activity. Select the schema, then the profile-enabled dataset, then the attributes to update. [Learn more](update-profiles.md) |
| **AJOJAS-2024-400** | Profile update action in node '{nodeId}': missing dataset id | The dataset is missing from the profile update. Open the **[!UICONTROL Update profile]** activity and select the profile-enabled dataset, then the attributes to update. [Learn more](update-profiles.md) |
| **AJOJAS-2025-400** | Profile update action in node '{nodeId}': missing path of profile attribute to be updated | For each attribute to update, select the profile field. [Learn more](update-profiles.md) |
| **AJOJAS-2026-400** | Profile update action in node '{nodeId}': missing expression for profile attribute update | For each attribute to update, set its value as a constant, a field, or an expression. [Learn more](update-profiles.md) |

## Dataset lookup {#dataset-lookup}

These errors occur when the Dataset lookup activity does not have a dataset, fields, or lookup keys.

See also [Troubleshooting](dataset-lookup.md#troubleshooting).

| Error code | Message | How to fix |
|---|---|---|
| **AJOJAS-2070-400** | Dataset lookup action in node '{nodeId}': missing fields / XDM information | Open the **[!UICONTROL Dataset lookup]** activity and select the dataset and the fields to retrieve. [Learn more](dataset-lookup.md) |
| **AJOJAS-2071-400** | Dataset lookup action in node '{nodeId}': missing schema id in XDM information | The schema information of the lookup is missing. Open the **[!UICONTROL Dataset lookup]** activity and select the dataset and the fields to retrieve. [Learn more](dataset-lookup.md) |
| **AJOJAS-2072-400** | Dataset lookup action in node '{nodeId}': missing dataset id | The dataset is missing. Open the **[!UICONTROL Dataset lookup]** activity and select the dataset and the fields to retrieve. [Learn more](dataset-lookup.md) |
| **AJOJAS-2073-400** | Dataset lookup action in node '{nodeId}': missing selected fields for dataset lookup | Select the fields to retrieve. Only leaf fields can be selected, up to 20. [Learn more](dataset-lookup.md) |
| **AJOJAS-2074-400** | Dataset lookup action in node '{nodeId}': missing expression for dataset lookup primary keys | Define the lookup keys in advanced mode. A lookup can use up to 50 keys. [Learn more](dataset-lookup.md) |

## Jump {#jump}

These errors occur when the Jump activity does not have a target journey.

See also [Jump best practices and limitations](jump.md#jump-limitations) and [Troubleshooting](jump.md#jump-troubleshoot).

| Error code | Message | How to fix |
|---|---|---|
| **AJOJAS-2027-400** | Jump action in node '{nodeId}': missing event id | The **[!UICONTROL Jump]** activity has no target event. Open it and select the target journey: the activity sends an internal event to the first event of that journey. [Learn more](jump.md) |
| **AJOJAS-2028-400** | Jump action in node '{nodeId}': missing target journey | The **[!UICONTROL Jump]** activity has no target journey. Open it and select one. Only draft, live, or test-mode journeys with the same namespace are listed. [Learn more](jump.md) |

## Wait, conditions, and event timeouts {#wait-conditions}

These errors occur when a Wait, Condition, or event timeout is missing a value.

See also [Wait recommendations](wait-activity.md#wait-recommendations), [Events limitations](limitations.md#events-limitations), and [Troubleshoot errors in activities](troubleshooting.md#activity-errors).

| Error code | Message | How to fix |
|---|---|---|
| **AJOJAS-2030-400** | Delay wait in node '{nodeId}': missing duration | Open the **[!UICONTROL Wait]** activity and enter a duration and a unit. [Learn more](wait-activity.md) |
| **AJOJAS-2032-400** | Custom wait in node '{nodeId}': missing expression | In the **[!UICONTROL Custom]** option, build the expression that returns the date to wait until. [Learn more](wait-activity.md) |
| **AJOJAS-2056-400** | Condition node '{nodeId}' has no conditions defined | Open the **[!UICONTROL Condition]** activity and define at least one path with a condition. [Learn more](condition-activity.md) |
| **AJOJAS-2033-400** | Data source condition in node '{nodeId}' on edge '{edgeId}' ({context}): missing expression | Define a condition for each path of the **[!UICONTROL Condition]** activity, or delete the paths you do not need. [Learn more](condition-activity.md) |
| **AJOJAS-2039-400** | Time condition in node '{nodeId}' on edge '{edgeId}' ({context}): empty days list | Select at least one day in the time condition. [Learn more](condition-activity.md#time_condition) |
| **AJOJAS-2041-400** | Event timeout in node '{nodeId}': missing timeout delay | In the event properties, set a duration under **[!UICONTROL Define the event timeout]**. [Learn more](general-events.md#events-specific-time) |

## Events and reactions {#events}

These errors occur when an Audience qualification or Reaction activity is not configured as the journey requires.

See also [Audience qualification best practices](audience-qualification-events.md#best-practices-segments), [Audience qualification guardrails](audience-qualification-events.md#audience-qualification-guardrails), and [Reaction events guardrails](reaction-events.md#guardrails-limitations).

| Error code | Message | How to fix |
|---|---|---|
| **AJOJAS-2045-400** | Segment qualification event in node '{nodeId}': invalid verb '{verb}'. Must be in 'realized', 'existing' or 'exited' | In the **[!UICONTROL Audience qualification]** activity, select **[!UICONTROL Enter]**, **[!UICONTROL Exit]**, or both. [Learn more](audience-qualification-events.md) |
| **AJOJAS-2046-400** | Reaction event in node '{nodeId}': missing related action | Place the **[!UICONTROL Reaction]** right after the channel action it reacts to, and select that action in its properties. [Learn more](reaction-events.md) |
| **AJOJAS-2048-400** | Reaction event in node '{nodeId}': unsupported related action type '{actionType}' | Reactions work only with built-in channel actions. To react to a message sent through a custom action, configure a dedicated event. [Learn more](reaction-events.md) |

## Content decision {#content-decision}

This error occurs when a Content decision activity does not have a decision policy.

See also [Guardrails and limitations](content-decision.md#guardrails).

| Error code | Message | How to fix |
|---|---|---|
| **AJOJAS-2067-400** | Content decision node '{nodeId}': missing decision policy | Open the **[!UICONTROL Content decision]** activity and select **[!UICONTROL Add decision policy]**. [Learn more](content-decision.md) |

## License package limits (Select) {#select-package}

These errors apply to unitary journeys on the **Select** license package. They match the `ERR_PKG_SELECT_*` codes described in [License package comparison](../start/guardrails.md#select-package-limitations).

| Error code | Message | How to fix |
|---|---|---|
| **AJOJAS-5007-403** | SELECT package: only one action allowed in unitary journey | The Select package allows only one action in a unitary journey. Keep one action activity, or use a Read audience journey. [Learn more](../start/guardrails.md#select-package-limitations) |
| **AJOJAS-5006-403** | SELECT package: no condition allowed in unitary journey | The Select package does not allow conditions in a unitary journey, which must follow a single path. Remove the **[!UICONTROL Condition]** activity. [Learn more](../start/guardrails.md#select-package-limitations) |
| **AJOJAS-5005-403** | SELECT package: no wait allowed in unitary journey | The Select package does not allow waits in a unitary journey. Remove the **[!UICONTROL Wait]** activity. [Learn more](../start/guardrails.md#select-package-limitations) |
| **AJOJAS-5001-400** | SELECT package: timeout/error transition from node '{nodeId}' must point to end node only | On the Select package, the timeout and error paths of an action in a unitary journey must lead directly to an **[!UICONTROL End]** activity. Connect them to it. [Learn more](../start/guardrails.md#select-package-limitations) |

To use these activities with the Select package, use a Read audience journey, or ask your Adobe representative about upgrading your package.

## Versions, test mode, and size {#versions}

These errors occur when you edit a journey in a state that does not allow changes (test mode or live), use an unsupported version type, or save a journey that is too large.

See also [Journey versions limitations](limitations.md#journey-versions-limitations), [Troubleshoot test mode](testing-the-journey.md#troubleshoot-test-mode), and the [publication FAQ](publish-journey.md#faq).

| Error code | Message | How to fix |
|---|---|---|
| **AJOJAS-3024-400** | Journey version typed as '{versionType}' can't be saved, as the other versions in the journey are typed as '{otherVersionType}': all versions in a journey must have the same type | All versions of a journey must start with the same type of activity as version 1 (event, Audience qualification, or Read audience). Create a new journey instead of changing the entry activity. [Learn more](../start/guardrails.md#journey-versions-g) |
| **AJOJAS-4001-403** | Current journey is already in test mode: can't update a journey in test mode | A journey in test mode cannot be modified. Turn off test mode, make your changes, then test again. Turning off test mode removes the profiles that entered the journey and clears its reporting. [Learn more](testing-the-journey.md) |
| **AJOJAS-4002-403** | Can't update a deployed journey | A live journey is read-only: you can only change the activity labels and descriptions, and the journey name and description. To make other changes, create a new version, edit it, and publish it. [Learn more](publish-journey.md) |
| **AJOJAS-7003-413** | The request is too large to be processed. Reduce the size of the content and retry. | The journey is larger than 2 MB. Simplify complex expressions and conditions, reduce data mappings, or split the journey. Check the **[!UICONTROL Current journey payload size]** indicator in the journey properties. [Learn more](../start/guardrails.md#journey-payload-size) |

## Journey fragments {#fragments}

These errors occur when you create, edit, activate, or archive a journey fragment.

See also [Fragment guardrails and limitations](journey-fragments.md#guardrails) and the [Fragments FAQ](journey-fragments.md#faq).

| Error code | Message | How to fix |
|---|---|---|
| **AJOJAS-8002-400** | A fragment name is required. Enter a name for the fragment and try again. | Enter a name for the fragment. [Learn more](journey-fragments.md#create-journey-fragment) |
| **AJOJAS-8001-409** | A fragment with ID '{fragmentId}' already exists in this sandbox. Retrieve the existing fragment or choose a different ID and retry. | Choose a different fragment ID, or open the existing fragment. IDs must be unique in a sandbox. [Learn more](journey-fragments.md#create-journey-fragment) |
| **AJOJAS-8008-409** | A fragment named '{name}' already exists in this sandbox. Choose a different name and retry. | Choose a different fragment name, or open the existing fragment. Names must be unique in a sandbox. [Learn more](journey-fragments.md#create-journey-fragment) |
| **AJOJAS-8003-400** | The fragment name must be {maxLength} characters or fewer. Shorten the name and try again. | Shorten the name to the length shown in the message. [Learn more](journey-fragments.md#create-journey-fragment) |
| **AJOJAS-8005-400** | This fragment exceeds the maximum of {maxNodes} nodes. Remove some nodes and try again. | A fragment can contain up to 20 activities. Remove activities, or split the logic across several fragments. [Learn more](journey-fragments.md#guardrails) |
| **AJOJAS-8006-400** | One or more nodes in this fragment are not connected to the starting node. Connect all nodes to the fragment path and try again. | Connect every activity to the fragment path, or delete the unused activities. [Learn more](journey-fragments.md#guardrails) |
| **AJOJAS-8007-400** | Jump activities are not supported in Journey Fragments. Remove all Jump activities before saving. | Fragments cannot contain a **[!UICONTROL Jump]** activity. Remove it from the fragment. [Learn more](journey-fragments.md#guardrails) |
| **AJOJAS-8022-400** | This fragment has more than one entry point. A journey fragment must have exactly one entry path with no incoming connections so it can be embedded into a journey at a single point. | A fragment must have exactly one entry path, and no path can lead into its first activity. [Learn more](journey-fragments.md#guardrails) |
| **AJOJAS-8023-400** | This fragment has no valid entry point. Check that it contains at least one activity and that its nodes do not form a closed loop. | Add at least one activity, and remove loops so the fragment has a first activity. [Learn more](journey-fragments.md#guardrails) |
| **AJOJAS-8035-400** | A Wait activity cannot immediately follow a Business Event in a journey fragment. Remove the Wait activity or insert another activity between the Business Event and the Wait. | Remove the **[!UICONTROL Wait]**, or insert another activity between the business event and the Wait. [Learn more](journey-fragments.md) |
| **AJOJAS-8026-400** | An identity namespace is required when using a Read Audience activity in a journey fragment. Add an identity namespace to the activity configuration and try again. | The fragment has a **[!UICONTROL Read audience]** activity without an identity namespace. Open the activity and select it. [Learn more](read-audience.md) |
| **AJOJAS-8027-400** | An identity namespace is required when using an Audience Qualification activity in a journey fragment. Add an identity namespace to the activity configuration and try again. | The fragment has an **[!UICONTROL Audience qualification]** activity without an identity namespace. Open the activity and select it. [Learn more](read-audience.md) |
| **AJOJAS-8028-400** | Adobe Campaign Standard actions cannot be used in a journey fragment that contains a Read Audience activity. To activate this fragment, remove the Campaign Standard action or replace the Read Audience activity with a different activity type. | [Adobe Campaign Standard](using-adobe-campaign-standard.md) actions cannot be used in a fragment that contains **[!UICONTROL Read audience]**. Remove the Campaign Standard action, or replace the **[!UICONTROL Read audience]** activity. |
| **AJOJAS-8029-400** | Adobe Campaign Classic actions cannot be used in a journey fragment that contains a Read Audience activity. To activate this fragment, remove the Campaign Classic action or replace the Read Audience activity with a different activity type. | [Adobe Campaign v7/v8](using-adobe-campaign-v7-v8.md) actions cannot be used in a fragment that contains **[!UICONTROL Read audience]**. Remove the Campaign Classic action, or replace the **[!UICONTROL Read audience]** activity. |
| **AJOJAS-8030-400** | Adobe Campaign Standard actions and Audience Qualification activities cannot be used together in the same journey fragment. To activate this fragment, remove either the Campaign Standard action or the Audience Qualification activity. | [Adobe Campaign Standard](using-adobe-campaign-standard.md) actions cannot be used in a fragment that contains **[!UICONTROL Audience qualification]**. Remove the Campaign Standard action, or remove the **[!UICONTROL Audience qualification]** activity. |
| **AJOJAS-8031-400** | Adobe Campaign Classic actions and Audience Qualification activities cannot be used together in the same journey fragment. To activate this fragment, remove either the Campaign Classic action or the Audience Qualification activity. | [Adobe Campaign v7/v8](using-adobe-campaign-v7-v8.md) actions cannot be used in a fragment that contains **[!UICONTROL Audience qualification]**. Remove the Campaign Classic action, or remove the **[!UICONTROL Audience qualification]** activity. |
| **AJOJAS-8025-400** | This fragment has one or more validation errors. Fix all errors on the fragment canvas and try again. | Fix the errors shown on the fragment canvas, then activate again. [Learn more](publish-journey.md#validate) |
| **AJOJAS-8033-400** | Fragment '{fragmentId}' could not be activated because it has validation errors. Fix all errors on the fragment canvas and try again. | Fix the errors shown on the fragment canvas, then activate again. [Learn more](publish-journey.md#validate) |
| **AJOJAS-8010-400** | This action cannot be performed on fragment '{fragmentId}' in its current state. Check the fragment's status and try a different action. | The fragment status does not allow this action. Only **[!UICONTROL Draft]** fragments can be edited or activated. Only **[!UICONTROL Active]** fragments can be deactivated or archived. Only **[!UICONTROL Archived]** fragments can be unarchived. [Learn more](journey-fragments.md#fragment-statuses) |
| **AJOJAS-8016-400** | Fragment '{fragmentId}' is currently in '{currentState}' status and does not support this action. Try a different action. | The fragment is in the status named in the message, which does not allow this action. Only **[!UICONTROL Draft]** fragments can be edited or activated. Only **[!UICONTROL Active]** fragments can be deactivated or archived. Only **[!UICONTROL Archived]** fragments can be unarchived. [Learn more](journey-fragments.md#fragment-statuses) |
| **AJOJAS-8014-400** | Fragment '{fragmentId}' is already archived. | The fragment is already archived, so no action is needed. To use it again, unarchive it. It returns to **[!UICONTROL Draft]** status. [Learn more](journey-fragments.md#fragment-statuses) |
| **AJOJAS-8024-429** | The '{sandboxName}' sandbox has reached the limit of {limit} active fragments. To activate another fragment, archive or deactivate an existing active fragment first. | A sandbox can have up to 200 active fragments. Archive or deactivate a fragment you do not use. [Learn more](journey-fragments.md#guardrails) |
| **AJOJAS-8009-429** | The '{sandboxName}' sandbox has reached the fragment limit of {limit}. To create a new fragment, archive or delete an existing one. | Archive a fragment, or delete a **[!UICONTROL Draft]** fragment, that you no longer need before creating a new one. [Learn more](journey-fragments.md#guardrails) |
| **AJOJAS-7104-403** | You do not have permission to apply label '{labelName}' to fragment '{fragmentId}'. Contact your administrator to request access. | You do not have access to the label. Ask your administrator for access, or choose another label. [Learn more](journey-fragments.md) |

## Compare journey versions {#compare-versions}

These errors occur when you compare two versions of a journey.

| Error code | Message | How to fix |
|---|---|---|
| **AJOJAS-11001-400** | The selected versions are the same. Choose two different versions to compare. | Select two different versions to compare. [Learn more](journeys-coworker-skills.md) |
| **AJOJAS-11004-400** | Comparison requires two versions. Select both versions, then try again. | Select both versions to compare. [Learn more](journeys-coworker-skills.md) |
| **AJOJAS-11005-400** | The selected versions are not in chronological order. Swap them and try again. | Swap the two versions so that they are in chronological order. [Learn more](journeys-coworker-skills.md) |
| **AJOJAS-11007-400** | A journey has disconnected activities, which prevents comparison. Connect all activities and try again. | Connect all activities (or delete the unused ones) in the version, then compare again. [Learn more](journeys-coworker-skills.md) |

## Related topics {#related}

* [Error codes reference](error-codes-reference.md)
* [Validate and publish a journey](publish-journey.md)
* [Test your journey](testing-the-journey.md)
* [Troubleshoot journey errors](troubleshooting.md)
* [Troubleshoot journey execution](troubleshooting-execution.md)
* [Journey FAQs](journey-faq.md)
* [Best practices to avoid common errors](error-codes-reference.md#best-practices)
* [Guardrails and limitations](../start/guardrails.md)

{{$include /help/_includes/do-not-localize/building-journeys/ai-augmented-journey-validation-errors.md}}
