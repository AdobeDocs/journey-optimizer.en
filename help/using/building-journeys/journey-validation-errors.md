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

If the error persists after you follow the steps, note the error code, the message, the request ID, and the campaign, journey, or activity concerned, and keep the logs or screenshots. Then contact your administrator for a permission or access error, or [contact Adobe Support](../start/user-interface.md#support-ticket-guidelines) with these details. For all the support options, see [Getting support](error-codes-reference.md#getting-support).

## Journey structure {#structure}

These errors occur when the journey has no entry activity or has activities in a layout that is not supported.

See also [Troubleshoot journey errors](troubleshooting.md#canvas-errors) and [Best practices before journey activation](error-codes-reference.md#journey-best-practices).

| Error code | Message | How to fix |
|---|---|---|
| **AJOJAS-1000-400** | No initial node found in node graph | Add an **[!UICONTROL Event]**, **[!UICONTROL Business event]**, **[!UICONTROL Read audience]**, or **[!UICONTROL Audience qualification]** activity as the first activity of the journey. [Learn more](journey-types-selection.md) |
| **AJOJAS-3018-400** | Unsupported transitions configuration in node '{nodeId}': only events can be put in parallel | Keep only event and **[!UICONTROL Wait]** activities in parallel after an activity, and place the other activities one after the other. [Learn more](using-the-journey-designer.md#paths) |
| **AJOJAS-3027-400** | Event timeout already defined in node '{nodeId}': timeout defined in node '{timeoutNodeId}' not supported: only one timeout can be defined for events in parallel | Disable **[!UICONTROL Define the event timeout]** on all but one of the parallel events, or place the events one after the other. [Learn more](general-events.md#events-specific-time) |
| **AJOJAS-3028-403** | Timeout on initial event '{eventId}' is not allowed | Disable the **[!UICONTROL Define the event timeout]** option in the properties of the first event of the journey. [Learn more](general-events.md#events-specific-time) |

## Read audience and identity namespace {#read-audience}

These errors occur when the Read audience activity is incomplete or misplaced, or when the journey has no identity namespace.

See also [Guardrails and recommendations](read-audience.md#must-read), [Troubleshooting](read-audience.md#audience-count-mismatch), and [Read audience limitations](limitations.md#read-audiences-limitations).

| Error code | Message | How to fix |
|---|---|---|
| **AJOJAS-2007-400** | Read segment: missing recurrence policy definition | Open the **[!UICONTROL Read audience]** activity, go to **[!UICONTROL Schedule]**, and set the recurrence. [Learn more](read-audience.md#schedule) |
| **AJOJAS-2008-400** | Read segment: missing timeOfDay in recurrence policy | Open the **[!UICONTROL Read audience]** activity, go to **[!UICONTROL Schedule]**, and set the time of day. [Learn more](read-audience.md#schedule) |
| **AJOJAS-2009-400** | Read segment: missing startDate for recurring journey | Open the **[!UICONTROL Read audience]** activity, go to **[!UICONTROL Schedule]**, and set the start date. [Learn more](read-audience.md#schedule) |
| **AJOJAS-3003-400** | Multiple read segment nodes detected. Only one allowed, after start or business event | Keep one **[!UICONTROL Read audience]** activity. To target several audiences, combine them into a single audience first. [Learn more](read-audience.md) |
| **AJOJAS-3005-400** | Read segment node can only have one parent node: start or a business event | Keep a single path into the **[!UICONTROL Read audience]** activity, from the journey start or a business event, and remove any other path that leads into it. [Learn more](read-audience.md) |
| **AJOJAS-3006-400** | Read segment node only allowed after start or business event | Move the **[!UICONTROL Read audience]** activity so it is the first activity of the journey, or right after a business event. [Learn more](read-audience.md) |
| **AJOJAS-3013-400** | Missing identity namespace, required for read segment journey | Open the **[!UICONTROL Read audience]** activity and select an identity namespace in the **[!UICONTROL Namespace]** field. [Learn more](read-audience.md) |
| **AJOJAS-3017-400** | Missing identity namespace, required for journey using profile update action | Open the first activity (**[!UICONTROL Read audience]**, **[!UICONTROL Audience qualification]**, or event) and select an identity namespace. [Learn more](read-audience.md) |

## Activity compatibility {#compatibility}

These errors occur when a journey combines activities that cannot be used together, such as Adobe Campaign actions with Read audience or Audience qualification.

See also [General actions limitations](limitations.md#action-limitations) and [Adobe Campaign guardrails](../start/guardrails.md#ac-g).

| Error code | Message | How to fix |
|---|---|---|
| **AJOJAS-3001-403** | ACS action not allowed in read segment journey | Remove the [Adobe Campaign Standard](using-adobe-campaign-standard.md) action, or start the journey with an event instead of **[!UICONTROL Read audience]**. |
| **AJOJAS-3004-403** | ACC action not allowed in read segment journey | Remove the [Adobe Campaign v7/v8](using-adobe-campaign-v7-v8.md) action, or start the journey with an event instead of **[!UICONTROL Read audience]**. |
| **AJOJAS-3007-403** | ACS action and segment qualification can't be used in the same journey | Remove the [Adobe Campaign Standard](using-adobe-campaign-standard.md) action, or replace it with a built-in channel action. |
| **AJOJAS-3009-403** | ACC action and segment qualification can't be used in the same journey | Remove the [Adobe Campaign v7/v8](using-adobe-campaign-v7-v8.md) action, or replace it with a built-in channel action. |
| **AJOJAS-3010-403** | ACS and message actions can't be mixed in the same journey | Keep only [Campaign Standard](using-adobe-campaign-standard.md) actions or only built-in channel actions in the journey. [Campaign v7/v8](using-adobe-campaign-v7-v8.md) actions can be combined with built-in channel actions. |
| **AJOJAS-3002-403** | Jump action not allowed in read segment journey | Remove the **[!UICONTROL Jump]** activity, or start the journey with an event instead of **[!UICONTROL Read audience]**. [Learn more](jump.md#jump-limitations) |

## Action activities {#actions}

These errors occur when a channel action, a custom action, or an Adobe Campaign Standard action is incomplete or uses an option that is no longer supported.

See also [Troubleshoot errors in activities](troubleshooting.md#activity-errors), [Troubleshoot your custom actions](../action/troubleshoot-custom-action.md), and [Custom actions limitations](limitations.md#custom-actions-limitations).

| Error code | Message | How to fix |
|---|---|---|
| **AJOJAS-2014-400** | '{messageType}' message action in node '{nodeId}': missing message id | Open the channel action activity and select or create the message. [Learn more](journey-action.md) |
| **AJOJAS-2065-400** | Surfaces are deprecated. Please use channel configurations instead | Open each channel action that uses a surface and select a channel configuration instead. [Learn more](../configuration/channel-surfaces.md) |
| **AJOJAS-6003-403** | Send time optimization for email is not included in the '{packageName}' package. To use this feature, upgrade to a package that supports it. | Turn off send time optimization on the email action, or contact your Adobe representative about upgrading your license package. [Learn more](send-time-optimization.md) |
| **AJOJAS-6004-403** | Send time optimization for push channel is not included in the '{packageName}' package. To use this feature, upgrade to a package that supports it. | Turn off send time optimization on the push action, or contact your Adobe representative about upgrading your license package. [Learn more](send-time-optimization.md) |
| **AJOJAS-2021-400** | Custom action in node '{nodeId}': missing expression mapping | Open the custom action activity and set each mandatory parameter to a constant, a field, or an expression. [Learn more](using-custom-actions.md) |
| **AJOJAS-2012-400** | ACS message action in node '{nodeId}': address parameter '{addressParam}' can't be mapped (no expression defined) | Open the Campaign Standard action and map the address to a field, constant, or expression. [Learn more](using-adobe-campaign-standard.md) |
| **AJOJAS-2013-400** | ACS message action in node '{nodeId}': personalization parameter '{personalizationParam}' can't be mapped (no expression defined) | Open the Campaign Standard action and map the personalization parameter named in the message to a field, constant, or expression. [Learn more](using-adobe-campaign-standard.md) |

## Update profile {#update-profile}

These errors occur when the Update profile activity does not have a complete schema, dataset, and attribute configuration.

See also [Guardrails and limitations](update-profiles.md#guardrails).

| Error code | Message | How to fix |
|---|---|---|
| **AJOJAS-2022-400** | Profile update action in node '{nodeId}': missing fields / XDM information | Open the **[!UICONTROL Update profile]** activity. Select the schema, then the profile-enabled dataset, then the attributes to update. [Learn more](update-profiles.md) |
| **AJOJAS-2023-400** | Profile update action in node '{nodeId}': missing schema id in XDM information | Open the **[!UICONTROL Update profile]** activity. Select the schema, then the profile-enabled dataset, then the attributes to update. [Learn more](update-profiles.md) |
| **AJOJAS-2024-400** | Profile update action in node '{nodeId}': missing dataset id | Open the **[!UICONTROL Update profile]** activity and select the profile-enabled dataset, then the attributes to update. [Learn more](update-profiles.md) |
| **AJOJAS-2025-400** | Profile update action in node '{nodeId}': missing path of profile attribute to be updated | Open the **[!UICONTROL Update profile]** activity and select the profile field for each attribute to update. [Learn more](update-profiles.md) |
| **AJOJAS-2026-400** | Profile update action in node '{nodeId}': missing expression for profile attribute update | Open the **[!UICONTROL Update profile]** activity and set the value of each attribute to update as a constant, a field, or an expression. [Learn more](update-profiles.md) |

## Dataset lookup {#dataset-lookup}

These errors occur when the Dataset lookup activity does not have a dataset, fields, or lookup keys.

See also [Troubleshooting](dataset-lookup.md#troubleshooting).

| Error code | Message | How to fix |
|---|---|---|
| **AJOJAS-2070-400** | Dataset lookup action in node '{nodeId}': missing fields / XDM information | Open the **[!UICONTROL Dataset lookup]** activity and select the dataset and the fields to retrieve. [Learn more](dataset-lookup.md) |
| **AJOJAS-2071-400** | Dataset lookup action in node '{nodeId}': missing schema id in XDM information | Open the **[!UICONTROL Dataset lookup]** activity and select the dataset and the fields to retrieve. [Learn more](dataset-lookup.md) |
| **AJOJAS-2072-400** | Dataset lookup action in node '{nodeId}': missing dataset id | Open the **[!UICONTROL Dataset lookup]** activity and select the dataset, then the fields to retrieve. [Learn more](dataset-lookup.md) |
| **AJOJAS-2073-400** | Dataset lookup action in node '{nodeId}': missing selected fields for dataset lookup | In the **[!UICONTROL Dataset lookup]** activity, select the fields to retrieve: only leaf fields can be selected, up to 20. [Learn more](dataset-lookup.md) |
| **AJOJAS-2074-400** | Dataset lookup action in node '{nodeId}': missing expression for dataset lookup primary keys | In the **[!UICONTROL Lookup key(s)]** field of the **[!UICONTROL Dataset lookup]** activity, define the lookup keys in **[!UICONTROL Advanced mode]**, up to 50 keys. [Learn more](dataset-lookup.md) |

## Jump {#jump}

These errors occur when the Jump activity does not have a target journey.

See also [Jump best practices and limitations](jump.md#jump-limitations) and [Troubleshooting](jump.md#jump-troubleshoot).

| Error code | Message | How to fix |
|---|---|---|
| **AJOJAS-2027-400** | Jump action in node '{nodeId}': missing event id | Open the **[!UICONTROL Jump]** activity and select the target journey. [Learn more](jump.md) |
| **AJOJAS-2028-400** | Jump action in node '{nodeId}': missing target journey | Open the **[!UICONTROL Jump]** activity and select a target journey. Only draft, live, or test-mode journeys with the same namespace are listed. [Learn more](jump.md) |

## Wait, conditions, and event timeouts {#wait-conditions}

These errors occur when a Wait, Condition, or event timeout is missing a value.

See also [Wait recommendations](wait-activity.md#wait-recommendations), [Events limitations](limitations.md#events-limitations), and [Troubleshoot errors in activities](troubleshooting.md#activity-errors).

| Error code | Message | How to fix |
|---|---|---|
| **AJOJAS-2030-400** | Delay wait in node '{nodeId}': missing duration | Open the **[!UICONTROL Wait]** activity and enter a duration and a unit. [Learn more](wait-activity.md) |
| **AJOJAS-2032-400** | Custom wait in node '{nodeId}': missing expression | In the **[!UICONTROL Custom]** option, build the expression that returns the date to wait until. [Learn more](wait-activity.md) |
| **AJOJAS-2056-400** | Condition node '{nodeId}' has no conditions defined | Open the **[!UICONTROL Condition]** activity and define at least one path with a condition. [Learn more](condition-activity.md) |
| **AJOJAS-2033-400** | Data source condition in node '{nodeId}' on edge '{edgeId}' ({context}): missing expression | Define a condition for each path of the **[!UICONTROL Condition]** activity, or delete the paths you do not need. [Learn more](condition-activity.md) |
| **AJOJAS-2039-400** | Time condition in node '{nodeId}' on edge '{edgeId}' ({context}): empty days list | Open the **[!UICONTROL Condition]** activity and select at least one day in the time condition. [Learn more](condition-activity.md#time_condition) |
| **AJOJAS-2041-400** | Event timeout in node '{nodeId}': missing timeout delay | In the event properties, set a duration under **[!UICONTROL Define the event timeout]**. [Learn more](general-events.md#events-specific-time) |

## Events and reactions {#events}

These errors occur when an Audience qualification or Reaction activity is not configured as the journey requires.

See also [Audience qualification best practices](audience-qualification-events.md#best-practices-segments), [Audience qualification guardrails](audience-qualification-events.md#audience-qualification-guardrails), and [Reaction events guardrails](reaction-events.md#guardrails-limitations).

| Error code | Message | How to fix |
|---|---|---|
| **AJOJAS-2045-400** | Segment qualification event in node '{nodeId}': invalid verb '{verb}'. Must be in 'realized', 'existing' or 'exited' | In the **[!UICONTROL Audience qualification]** activity, select **[!UICONTROL Enter]**, **[!UICONTROL Exit]**, or both. [Learn more](audience-qualification-events.md) |
| **AJOJAS-2046-400** | Reaction event in node '{nodeId}': missing related action | Place the **[!UICONTROL Reaction]** right after the channel action it reacts to, and select that action in its properties. [Learn more](reaction-events.md) |
| **AJOJAS-2048-400** | Reaction event in node '{nodeId}': unsupported related action type '{actionType}' | Place the **[!UICONTROL Reaction]** after a built-in channel action. To react to a message sent through a custom action, configure a dedicated event. [Learn more](reaction-events.md) |

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
| **AJOJAS-5007-403** | SELECT package: only one action allowed in unitary journey | Keep one action activity, or use a **[!UICONTROL Read audience]** journey. [Learn more](../start/guardrails.md#select-package-limitations) |
| **AJOJAS-5006-403** | SELECT package: no condition allowed in unitary journey | Remove the **[!UICONTROL Condition]** activity, or use a **[!UICONTROL Read audience]** journey. [Learn more](../start/guardrails.md#select-package-limitations) |
| **AJOJAS-5005-403** | SELECT package: no wait allowed in unitary journey | Remove the **[!UICONTROL Wait]** activity, or use a **[!UICONTROL Read audience]** journey. [Learn more](../start/guardrails.md#select-package-limitations) |
| **AJOJAS-5001-400** | SELECT package: timeout/error transition from node '{nodeId}' must point to end node only | Connect the timeout and error paths of the action directly to an **[!UICONTROL End]** activity. [Learn more](../start/guardrails.md#select-package-limitations) |

To use these activities with the Select package, use a Read audience journey, or ask your Adobe representative about upgrading your package.

## Versions, test mode, and size {#versions}

These errors occur when you edit a journey in a state that does not allow changes (test mode or live), use an unsupported version type, or save a journey that is too large.

See also [Journey versions limitations](limitations.md#journey-versions-limitations), [Troubleshoot test mode](testing-the-journey.md#troubleshoot-test-mode), and the [publication FAQ](publish-journey.md#faq).

| Error code | Message | How to fix |
|---|---|---|
| **AJOJAS-3024-400** | Journey version typed as '{versionType}' can't be saved, as the other versions in the journey are typed as '{otherVersionType}': all versions in a journey must have the same type | Start the new version with the same type of activity as version 1 (event, **[!UICONTROL Audience qualification]**, or **[!UICONTROL Read audience]**), or create a new journey for a different entry activity. [Learn more](../start/guardrails.md#journey-versions-g) |
| **AJOJAS-4001-403** | Current journey is already in test mode: can't update a journey in test mode | Turn off test mode, make your changes, then test again. Turning off test mode removes the profiles that entered the journey and clears its reporting. [Learn more](testing-the-journey.md) |
| **AJOJAS-4002-403** | Can't update a deployed journey | Create a new version, edit it, and publish it. Only activity labels and descriptions, and the journey name and description, can be changed on a live journey. [Learn more](publish-journey.md) |
| **AJOJAS-7003-413** | The request is too large to be processed. Reduce the size of the content and retry. | Simplify complex expressions and conditions, reduce data mappings, or split the journey. Check the **[!UICONTROL Current journey payload size]** indicator in the journey properties. [Learn more](../start/guardrails.md#journey-payload-size) |

## Journey fragments {#fragments}

These errors occur when you create, edit, activate, or archive a journey fragment.

See also [Fragment guardrails and limitations](journey-fragments.md#guardrails) and the [Fragments FAQ](journey-fragments.md#faq).

| Error code | Message | How to fix |
|---|---|---|
| **AJOJAS-8002-400** | A fragment name is required. Enter a name for the fragment and try again. | Enter a unique name for the fragment before you save it. [Learn more](journey-fragments.md#create-journey-fragment) |
| **AJOJAS-8001-409** | A fragment with ID '{fragmentId}' already exists in this sandbox. Retrieve the existing fragment or choose a different ID and retry. | Choose a different fragment ID, or open the existing fragment. [Learn more](journey-fragments.md#create-journey-fragment) |
| **AJOJAS-8008-409** | A fragment named '{name}' already exists in this sandbox. Choose a different name and retry. | Choose a different fragment name, or open the existing fragment. [Learn more](journey-fragments.md#create-journey-fragment) |
| **AJOJAS-8003-400** | The fragment name must be {maxLength} characters or fewer. Shorten the name and try again. | Shorten the name in the fragment properties to the length shown in the message. [Learn more](journey-fragments.md#create-journey-fragment) |
| **AJOJAS-8005-400** | This fragment exceeds the maximum of {maxNodes} nodes. Remove some nodes and try again. | Remove activities from the fragment, or split the logic across several fragments. [Learn more](journey-fragments.md#guardrails) |
| **AJOJAS-8006-400** | One or more nodes in this fragment are not connected to the starting node. Connect all nodes to the fragment path and try again. | Connect every activity to the fragment path, or delete the unused activities. [Learn more](journey-fragments.md#guardrails) |
| **AJOJAS-8007-400** | Jump activities are not supported in Journey Fragments. Remove all Jump activities before saving. | Remove the **[!UICONTROL Jump]** activity from the fragment. [Learn more](journey-fragments.md#guardrails) |
| **AJOJAS-8022-400** | This fragment has more than one entry point. A journey fragment must have exactly one entry path with no incoming connections so it can be embedded into a journey at a single point. | Remove the paths that lead into the first activity of the fragment, so that only one entry path remains. [Learn more](journey-fragments.md#guardrails) |
| **AJOJAS-8023-400** | This fragment has no valid entry point. Check that it contains at least one activity and that its nodes do not form a closed loop. | Add at least one activity, and remove loops so the fragment has a first activity. [Learn more](journey-fragments.md#guardrails) |
| **AJOJAS-8035-400** | A Wait activity cannot immediately follow a Business Event in a journey fragment. Remove the Wait activity or insert another activity between the Business Event and the Wait. | Remove the **[!UICONTROL Wait]**, or insert another activity between the business event and the Wait. [Learn more](journey-fragments.md) |
| **AJOJAS-8026-400** | An identity namespace is required when using a Read Audience activity in a journey fragment. Add an identity namespace to the activity configuration and try again. | Open the **[!UICONTROL Read audience]** activity of the fragment and select an identity namespace. [Learn more](read-audience.md) |
| **AJOJAS-8027-400** | An identity namespace is required when using an Audience Qualification activity in a journey fragment. Add an identity namespace to the activity configuration and try again. | Open the **[!UICONTROL Audience qualification]** activity of the fragment and select an identity namespace. [Learn more](read-audience.md) |
| **AJOJAS-8028-400** | Adobe Campaign Standard actions cannot be used in a journey fragment that contains a Read Audience activity. To activate this fragment, remove the Campaign Standard action or replace the Read Audience activity with a different activity type. | Remove the [Adobe Campaign Standard](using-adobe-campaign-standard.md) action from the fragment, or replace the **[!UICONTROL Read audience]** activity with another activity type. |
| **AJOJAS-8029-400** | Adobe Campaign Classic actions cannot be used in a journey fragment that contains a Read Audience activity. To activate this fragment, remove the Campaign Classic action or replace the Read Audience activity with a different activity type. | Remove the [Adobe Campaign v7/v8](using-adobe-campaign-v7-v8.md) action from the fragment, or replace the **[!UICONTROL Read audience]** activity with another activity type. |
| **AJOJAS-8030-400** | Adobe Campaign Standard actions and Audience Qualification activities cannot be used together in the same journey fragment. To activate this fragment, remove either the Campaign Standard action or the Audience Qualification activity. | Remove the [Adobe Campaign Standard](using-adobe-campaign-standard.md) action from the fragment, or remove the **[!UICONTROL Audience qualification]** activity. |
| **AJOJAS-8031-400** | Adobe Campaign Classic actions and Audience Qualification activities cannot be used together in the same journey fragment. To activate this fragment, remove either the Campaign Classic action or the Audience Qualification activity. | Remove the [Adobe Campaign v7/v8](using-adobe-campaign-v7-v8.md) action from the fragment, or remove the **[!UICONTROL Audience qualification]** activity. |
| **AJOJAS-8025-400** | This fragment has one or more validation errors. Fix all errors on the fragment canvas and try again. | Open the fragment, fix each error shown on its canvas, then select the **[!UICONTROL Activate]** icon again. [Learn more](publish-journey.md#validate) |
| **AJOJAS-8033-400** | Fragment '{fragmentId}' could not be activated because it has validation errors. Fix all errors on the fragment canvas and try again. | Open the fragment, fix each error shown on its canvas, then select the **[!UICONTROL Activate]** icon again. [Learn more](publish-journey.md#validate) |
| **AJOJAS-8010-400** | This action cannot be performed on fragment '{fragmentId}' in its current state. Check the fragment's status and try a different action. | Check the fragment status in the **[!UICONTROL Fragment Inventory]**, then use an action that status allows: edit or activate a **[!UICONTROL Draft]** fragment, deactivate or archive an **[!UICONTROL Active]** fragment, or unarchive an **[!UICONTROL Archived]** fragment. [Learn more](journey-fragments.md#fragment-statuses) |
| **AJOJAS-8016-400** | Fragment '{fragmentId}' is currently in '{currentState}' status and does not support this action. Try a different action. | Use an action that the status named in the message allows: edit or activate a **[!UICONTROL Draft]** fragment, deactivate or archive an **[!UICONTROL Active]** fragment, or unarchive an **[!UICONTROL Archived]** fragment. [Learn more](journey-fragments.md#fragment-statuses) |
| **AJOJAS-8014-400** | Fragment '{fragmentId}' is already archived. | To use the fragment again, select **[!UICONTROL Unarchive]** from its **[!UICONTROL More actions]** menu. It returns to **[!UICONTROL Draft]** status. [Learn more](journey-fragments.md#fragment-statuses) |
| **AJOJAS-8024-429** | The '{sandboxName}' sandbox has reached the limit of {limit} active fragments. To activate another fragment, archive or deactivate an existing active fragment first. | Archive or deactivate an active fragment that you do not use. [Learn more](journey-fragments.md#guardrails) |
| **AJOJAS-8009-429** | The '{sandboxName}' sandbox has reached the fragment limit of {limit}. To create a new fragment, archive or delete an existing one. | Archive a fragment, or delete a **[!UICONTROL Draft]** fragment, that you no longer need before creating a new one. [Learn more](journey-fragments.md#guardrails) |
| **AJOJAS-7104-403** | You do not have permission to apply label '{labelName}' to fragment '{fragmentId}'. Contact your administrator to request access. | Ask your administrator to add the label named in the message to your role, or select a label that you have access to in the fragment properties. [Learn more](journey-fragments.md) |

## Compare journey versions {#compare-versions}

These errors occur when you compare two versions of a journey.

| Error code | Message | How to fix |
|---|---|---|
| **AJOJAS-11001-400** | The selected versions are the same. Choose two different versions to compare. | In Coworker Chat, select two different journey versions to compare. [Learn more](journeys-coworker-skills.md) |
| **AJOJAS-11004-400** | Comparison requires two versions. Select both versions, then try again. | In Coworker Chat, select both journey versions to compare. [Learn more](journeys-coworker-skills.md) |
| **AJOJAS-11005-400** | The selected versions are not in chronological order. Swap them and try again. | Switch the order of the two selected versions so that the older one comes first. [Learn more](journeys-coworker-skills.md) |
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
