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
hide: true
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
| **AJOJAS-1000-400** | No initial node found in node graph | The journey has [no entry activity](journey-types-selection.md). Add an **[!UICONTROL Event]**, **[!UICONTROL Business event]**, **[!UICONTROL Read audience]**, or **[!UICONTROL Audience qualification]** activity as the first activity. |
| **AJOJAS-3018-400** | Unsupported transitions configuration in node '{nodeId}': only events can be put in parallel | Only event and **[!UICONTROL Wait]** activities can be [placed in parallel](using-the-journey-designer.md#paths) after an activity. Place the other activities one after the other. |
| **AJOJAS-3027-400** | Event timeout already defined in node '{nodeId}': timeout defined in node '{timeoutNodeId}' not supported: only one timeout can be defined for events in parallel | When events are in parallel, [only one timeout can be defined](general-events.md#events-specific-time). Keep the timeout on one event, or place the events one after the other. |
| **AJOJAS-3028-403** | Timeout on initial event '{eventId}' is not allowed | [Disable the timeout](general-events.md#events-specific-time) on the first event of the journey. |

## Read audience and identity namespace {#read-audience}

These errors occur when the Read audience activity is incomplete or misplaced, or when the journey has no identity namespace.

See also [Guardrails and recommendations](read-audience.md#must-read), [Troubleshooting](read-audience.md#audience-count-mismatch), and [Read audience limitations](limitations.md#read-audiences-limitations).

| Error code | Message | How to fix |
|---|---|---|
| **AJOJAS-2007-400**, **2008-400**, **2009-400** | Read segment: missing recurrence policy definition<br/>Read segment: missing timeOfDay in recurrence policy<br/>Read segment: missing startDate for recurring journey | The schedule of the [**[!UICONTROL Read audience]**](read-audience.md) activity is incomplete. Open the activity, go to [**[!UICONTROL Schedule]**](read-audience.md#schedule), and set the recurrence, the time of day, and the start date. |
| **AJOJAS-3003-400** | Multiple read segment nodes detected. Only one allowed, after start or business event | A journey can have only one [**[!UICONTROL Read audience]**](read-audience.md) activity. Keep one. To target several audiences, combine them into a single audience first. |
| **AJOJAS-3005-400**, **3006-400** | Read segment node can only have one parent node: start or a business event<br/>Read segment node only allowed after start or business event | Move the [**[!UICONTROL Read audience]**](read-audience.md) activity so it is the first activity of the journey, or right after a business event. Remove any other path that leads into it. |
| **AJOJAS-3013-400** to **3017-400** | Missing identity namespace, required for read segment journey<br/>Missing identity namespace, required for journey using segment qualification events<br/>Missing identity namespace, required for journey using message action<br/>Missing identity namespace, required for journey using jump action<br/>Missing identity namespace, required for journey using profile update action | Select the [identity namespace](read-audience.md) in the first activity of the journey (**[!UICONTROL Read audience]**, **[!UICONTROL Audience qualification]**, or event). A namespace is required for journeys that use these activities, message actions, jump actions, or profile updates. |

## Activity compatibility {#compatibility}

These errors occur when a journey combines activities that cannot be used together, such as Adobe Campaign actions with Read audience or Audience qualification.

See also [General actions limitations](limitations.md#action-limitations) and [Adobe Campaign guardrails](../start/guardrails.md#ac-g).

| Error code | Message | How to fix |
|---|---|---|
| **AJOJAS-3001-403**, **3004-403** | ACS action not allowed in read segment journey<br/>ACC action not allowed in read segment journey | [Adobe Campaign Standard](using-adobe-campaign-standard.md) and [Adobe Campaign v7/v8](using-adobe-campaign-v7-v8.md) actions cannot be used with **[!UICONTROL Read audience]**. Remove the Campaign action, or start the journey with an event. |
| **AJOJAS-3007-403**, **3009-403** | ACS action and segment qualification can't be used in the same journey<br/>ACC action and segment qualification can't be used in the same journey | [Adobe Campaign Standard](using-adobe-campaign-standard.md) and [Adobe Campaign v7/v8](using-adobe-campaign-v7-v8.md) actions cannot be used with **[!UICONTROL Audience qualification]**. Remove the Campaign action, or replace it with a built-in channel action. |
| **AJOJAS-3010-403** | ACS and message actions can't be mixed in the same journey | Use only [Campaign Standard](using-adobe-campaign-standard.md) actions, or only built-in channel actions, in the same journey. [Campaign v7/v8](using-adobe-campaign-v7-v8.md) actions can be used with built-in channel actions. |
| **AJOJAS-3002-403** | Jump action not allowed in read segment journey | A **[!UICONTROL Jump]** activity [cannot be used in the same journey](jump.md#jump-limitations) as a **[!UICONTROL Read audience]** activity. Remove the Jump, or start the journey with an event. |

## Action activities {#actions}

These errors occur when a channel action, a custom action, or an Adobe Campaign Standard action is incomplete or uses an option that is no longer supported.

See also [Troubleshoot errors in activities](troubleshooting.md#activity-errors), [Troubleshoot your custom actions](../action/troubleshoot-custom-action.md), and [Custom actions limitations](limitations.md#custom-actions-limitations).

| Error code | Message | How to fix |
|---|---|---|
| **AJOJAS-2014-400** | '{messageType}' message action in node '{nodeId}': missing message id | The channel action has no message. Open the activity and [select or create the message](journey-action.md). |
| **AJOJAS-2065-400** | Surfaces are deprecated. Please use channel configurations instead | Open each channel action that uses a surface and select a [channel configuration](../configuration/channel-surfaces.md) instead. |
| **AJOJAS-6003-403**, **6004-403** | Send time optimization for email is not included in the '{packageName}' package. To use this feature, upgrade to a package that supports it.<br/>Send time optimization for push channel is not included in the '{packageName}' package. To use this feature, upgrade to a package that supports it. | Your license package does not include [send time optimization](send-time-optimization.md) for email or push. Turn it off on the action, or contact your Adobe representative about upgrading. |
| **AJOJAS-2021-400** | Custom action in node '{nodeId}': missing expression mapping | A parameter of the [custom action](using-custom-actions.md) has no value. Open the activity and set each mandatory parameter to a constant, a field, or an expression. |
| **AJOJAS-2012-400**, **2013-400** | ACS message action in node '{nodeId}': address parameter '{addressParam}' can't be mapped (no expression defined)<br/>ACS message action in node '{nodeId}': personalization parameter '{personalizationParam}' can't be mapped (no expression defined) | Open the [Campaign Standard action](using-adobe-campaign-standard.md) and map the address and every personalization parameter to a field, constant, or expression. |

## Update profile {#update-profile}

These errors occur when the Update profile activity does not have a complete schema, dataset, and attribute configuration.

See also [Guardrails and limitations](update-profiles.md#guardrails).

| Error code | Message | How to fix |
|---|---|---|
| **AJOJAS-2022-400**, **2023-400**, **2024-400** | Profile update action in node '{nodeId}': missing fields / XDM information<br/>Profile update action in node '{nodeId}': missing schema id in XDM information<br/>Profile update action in node '{nodeId}': missing dataset id | Open the [**[!UICONTROL Update profile]**](update-profiles.md) activity. Select the schema, then the profile-enabled dataset, then the attributes to update. |
| **AJOJAS-2025-400**, **2026-400** | Profile update action in node '{nodeId}': missing path of profile attribute to be updated<br/>Profile update action in node '{nodeId}': missing expression for profile attribute update | For each attribute, select the [profile field](update-profiles.md) and set its value as a constant, a field, or an expression. |

## Dataset lookup {#dataset-lookup}

These errors occur when the Dataset lookup activity does not have a dataset, fields, or lookup keys.

See also [Troubleshooting](dataset-lookup.md#troubleshooting).

| Error code | Message | How to fix |
|---|---|---|
| **AJOJAS-2070-400**, **2071-400**, **2072-400** | Dataset lookup action in node '{nodeId}': missing fields / XDM information<br/>Dataset lookup action in node '{nodeId}': missing schema id in XDM information<br/>Dataset lookup action in node '{nodeId}': missing dataset id | Open the [**[!UICONTROL Dataset lookup]**](dataset-lookup.md) activity and select the dataset and the fields to retrieve. |
| **AJOJAS-2073-400** | Dataset lookup action in node '{nodeId}': missing selected fields for dataset lookup | Select the fields to retrieve. Only [leaf fields](dataset-lookup.md) can be selected, up to 20. |
| **AJOJAS-2074-400** | Dataset lookup action in node '{nodeId}': missing expression for dataset lookup primary keys | Define the [lookup keys](dataset-lookup.md) in advanced mode. A lookup can use up to 50 keys. |

## Jump {#jump}

These errors occur when the Jump activity does not have a target journey.

See also [Jump best practices and limitations](jump.md#jump-limitations) and [Troubleshooting](jump.md#jump-troubleshoot).

| Error code | Message | How to fix |
|---|---|---|
| **AJOJAS-2027-400**, **2028-400** | Jump action in node '{nodeId}': missing event id<br/>Jump action in node '{nodeId}': missing target journey | Open the [**[!UICONTROL Jump]**](jump.md) activity and select the target journey. Only draft, live, or test-mode journeys with the same namespace are listed. |

## Wait, conditions, and event timeouts {#wait-conditions}

These errors occur when a Wait, Condition, or event timeout is missing a value.

See also [Wait recommendations](wait-activity.md#wait-recommendations), [Events limitations](limitations.md#events-limitations), and [Troubleshoot errors in activities](troubleshooting.md#activity-errors).

| Error code | Message | How to fix |
|---|---|---|
| **AJOJAS-2030-400** | Delay wait in node '{nodeId}': missing duration | Open the [**[!UICONTROL Wait]**](wait-activity.md) activity and enter a duration and a unit. |
| **AJOJAS-2032-400** | Custom wait in node '{nodeId}': missing expression | In the **[!UICONTROL Custom]** option, [build the expression](wait-activity.md) that returns the date to wait until. |
| **AJOJAS-2056-400** | Condition node '{nodeId}' has no conditions defined | Open the [**[!UICONTROL Condition]**](condition-activity.md) activity and define at least one path with a condition. |
| **AJOJAS-2033-400** | Data source condition in node '{nodeId}' on edge '{edgeId}' ({context}): missing expression | Define a condition for each path of the [**[!UICONTROL Condition]**](condition-activity.md) activity, or delete the paths you do not need. |
| **AJOJAS-2039-400** | Time condition in node '{nodeId}' on edge '{edgeId}' ({context}): empty days list | Select at least one day in the [time condition](condition-activity.md#time_condition). |
| **AJOJAS-2041-400** | Event timeout in node '{nodeId}': missing timeout delay | In the event properties, set a duration under [**[!UICONTROL Define the event timeout]**](general-events.md#events-specific-time). |

## Events and reactions {#events}

These errors occur when an Audience qualification or Reaction activity is not configured as the journey requires.

See also [Audience qualification best practices](audience-qualification-events.md#best-practices-segments), [Audience qualification guardrails](audience-qualification-events.md#audience-qualification-guardrails), and [Reaction events guardrails](reaction-events.md#guardrails-limitations).

| Error code | Message | How to fix |
|---|---|---|
| **AJOJAS-2045-400** | Segment qualification event in node '{nodeId}': invalid verb '{verb}'. Must be in 'realized', 'existing' or 'exited' | In the [**[!UICONTROL Audience qualification]**](audience-qualification-events.md) activity, select **[!UICONTROL Enter]**, **[!UICONTROL Exit]**, or both. |
| **AJOJAS-2046-400** | Reaction event in node '{nodeId}': missing related action | Place the [**[!UICONTROL Reaction]**](reaction-events.md) right after the channel action it reacts to, and select that action in its properties. |
| **AJOJAS-2048-400** | Reaction event in node '{nodeId}': unsupported related action type '{actionType}' | [Reactions](reaction-events.md) work only with built-in channel actions. To react to a message sent through a custom action, configure a dedicated event. |

## Content decision {#content-decision}

This error occurs when a Content decision activity does not have a decision policy.

See also [Guardrails and limitations](content-decision.md#guardrails).

| Error code | Message | How to fix |
|---|---|---|
| **AJOJAS-2067-400** | Content decision node '{nodeId}': missing decision policy | Open the [**[!UICONTROL Content decision]**](content-decision.md) activity and select **[!UICONTROL Add decision policy]**. |

## License package limits (Select) {#select-package}

These errors apply to unitary journeys on the **Select** license package. They match the `ERR_PKG_SELECT_*` codes described in [License package comparison](../start/guardrails.md#select-package-limitations).

| Error code | Message | How to fix |
|---|---|---|
| **AJOJAS-5007-403** | SELECT package: only one action allowed in unitary journey | The [Select package](../start/guardrails.md#select-package-limitations) allows only one action in a unitary journey. Keep one action activity, or use a Read audience journey. |
| **AJOJAS-5006-403** | SELECT package: no condition allowed in unitary journey | The [Select package](../start/guardrails.md#select-package-limitations) does not allow conditions in a unitary journey, which must follow a single path. Remove the **[!UICONTROL Condition]** activity. |
| **AJOJAS-5005-403** | SELECT package: no wait allowed in unitary journey | The [Select package](../start/guardrails.md#select-package-limitations) does not allow waits in a unitary journey. Remove the **[!UICONTROL Wait]** activity. |
| **AJOJAS-5001-400** | SELECT package: timeout/error transition from node '{nodeId}' must point to end node only | On the [Select package](../start/guardrails.md#select-package-limitations), the timeout and error paths of an action in a unitary journey must lead directly to an **[!UICONTROL End]** activity. Connect them to it. |

To use these activities with the Select package, use a Read audience journey, or ask your Adobe representative about upgrading your package.

## Versions, test mode, and size {#versions}

These errors occur when you edit a journey in a state that does not allow changes (test mode or live), use an unsupported version type, or save a journey that is too large.

See also [Journey versions limitations](limitations.md#journey-versions-limitations), [Troubleshoot test mode](testing-the-journey.md#troubleshoot-test-mode), and the [publication FAQ](publish-journey.md#faq).

| Error code | Message | How to fix |
|---|---|---|
| **AJOJAS-3024-400** | Journey version typed as '{versionType}' can't be saved, as the other versions in the journey are typed as '{otherVersionType}': all versions in a journey must have the same type | All versions of a journey must start with the [same type of activity as version 1](../start/guardrails.md#journey-versions-g) (event, Audience qualification, or Read audience). Create a new journey instead of changing the entry activity. |
| **AJOJAS-4001-403** | Current journey is already in test mode: can't update a journey in test mode | A journey in [test mode](testing-the-journey.md) cannot be modified. Turn off test mode, make your changes, then test again. Turning off test mode removes the profiles that entered the journey and clears its reporting. |
| **AJOJAS-4002-403** | Can't update a deployed journey | A live journey is [read-only](publish-journey.md): you can only change the activity labels and descriptions, and the journey name and description. To make other changes, create a new version, edit it, and publish it. |
| **AJOJAS-7003-413** | The request is too large to be processed. Reduce the size of the content and retry. | The journey is [larger than 2 MB](../start/guardrails.md#journey-payload-size). Simplify complex expressions and conditions, reduce data mappings, or split the journey. Check the **[!UICONTROL Current journey payload size]** indicator in the journey properties. |

## Journey fragments {#fragments}

These errors occur when you create, edit, activate, or archive a journey fragment.

See also [Fragment guardrails and limitations](journey-fragments.md#guardrails) and the [Fragments FAQ](journey-fragments.md#faq).

| Error code | Message | How to fix |
|---|---|---|
| **AJOJAS-8002-400** | A fragment name is required. Enter a name for the fragment and try again. | Enter a [name for the fragment](journey-fragments.md). |
| **AJOJAS-8001-409**, **8008-409** | A fragment with ID '{fragmentId}' already exists in this sandbox. Retrieve the existing fragment or choose a different ID and retry.<br/>A fragment named '{name}' already exists in this sandbox. Choose a different name and retry. | Choose a different name, or open the existing fragment. [Names must be unique in a sandbox](journey-fragments.md#guardrails). |
| **AJOJAS-8003-400** | The fragment name must be {maxLength} characters or fewer. Shorten the name and try again. | [Shorten the name](journey-fragments.md#guardrails) to the length shown in the message. |
| **AJOJAS-8005-400** | This fragment exceeds the maximum of {maxNodes} nodes. Remove some nodes and try again. | A fragment can contain [up to 20 activities](journey-fragments.md#guardrails). Remove activities, or split the logic across several fragments. |
| **AJOJAS-8006-400** | One or more nodes in this fragment are not connected to the starting node. Connect all nodes to the fragment path and try again. | [Connect every activity to the fragment path](journey-fragments.md#guardrails), or delete the unused activities. |
| **AJOJAS-8007-400** | Jump activities are not supported in Journey Fragments. Remove all Jump activities before saving. | [Fragments cannot contain](journey-fragments.md#guardrails) a **[!UICONTROL Jump]** activity. Remove it from the fragment. |
| **AJOJAS-8022-400** | This fragment has more than one entry point. A journey fragment must have exactly one entry path with no incoming connections so it can be embedded into a journey at a single point. | A fragment must have [exactly one entry path](journey-fragments.md#guardrails), and no path can lead into its first activity. |
| **AJOJAS-8023-400** | This fragment has no valid entry point. Check that it contains at least one activity and that its nodes do not form a closed loop. | [Add at least one activity](journey-fragments.md#guardrails), and remove loops so the fragment has a first activity. |
| **AJOJAS-8035-400** | A Wait activity cannot immediately follow a Business Event in a journey fragment. Remove the Wait activity or insert another activity between the Business Event and the Wait. | Remove the **[!UICONTROL Wait]**, or [insert another activity](journey-fragments.md) between the business event and the Wait. |
| **AJOJAS-8026-400**, **8027-400** | An identity namespace is required when using a Read Audience activity in a journey fragment. Add an identity namespace to the activity configuration and try again.<br/>An identity namespace is required when using an Audience Qualification activity in a journey fragment. Add an identity namespace to the activity configuration and try again. | Fragments with a **[!UICONTROL Read audience]** or **[!UICONTROL Audience qualification]** activity [need an identity namespace](read-audience.md). Open the activity and select it. |
| **AJOJAS-8028-400**, **8029-400**, **8030-400**, **8031-400** | Adobe Campaign Standard actions cannot be used in a journey fragment that contains a Read Audience activity. To activate this fragment, remove the Campaign Standard action or replace the Read Audience activity with a different activity type.<br/>Adobe Campaign Classic actions cannot be used in a journey fragment that contains a Read Audience activity. To activate this fragment, remove the Campaign Classic action or replace the Read Audience activity with a different activity type.<br/>Adobe Campaign Standard actions and Audience Qualification activities cannot be used together in the same journey fragment. To activate this fragment, remove either the Campaign Standard action or the Audience Qualification activity.<br/>Adobe Campaign Classic actions and Audience Qualification activities cannot be used together in the same journey fragment. To activate this fragment, remove either the Campaign Classic action or the Audience Qualification activity. | [Adobe Campaign Standard](using-adobe-campaign-standard.md) and [Adobe Campaign v7/v8](using-adobe-campaign-v7-v8.md) actions cannot be used in a fragment that contains **[!UICONTROL Read audience]** or **[!UICONTROL Audience qualification]**. Remove the Campaign action, or remove that activity. |
| **AJOJAS-8025-400**, **8033-400** | This fragment has one or more validation errors. Fix all errors on the fragment canvas and try again.<br/>Fragment '{fragmentId}' could not be activated because it has validation errors. Fix all errors on the fragment canvas and try again. | [Fix the errors](publish-journey.md#validate) shown on the fragment canvas, then activate again. |
| **AJOJAS-8010-400**, **8016-400** | This action cannot be performed on fragment '{fragmentId}' in its current state. Check the fragment's status and try a different action.<br/>Fragment '{fragmentId}' is currently in '{currentState}' status and does not support this action. Try a different action. | The fragment [status](journey-fragments.md#fragment-statuses) does not allow this action. Only **[!UICONTROL Draft]** fragments can be edited or activated. Only **[!UICONTROL Active]** fragments can be deactivated or archived. Only **[!UICONTROL Archived]** fragments can be unarchived. |
| **AJOJAS-8014-400** | Fragment '{fragmentId}' is already archived. | The fragment is already archived, so no action is needed. To use it again, [unarchive it](journey-fragments.md#fragment-statuses). It returns to **[!UICONTROL Draft]** status. |
| **AJOJAS-8024-429** | The '{sandboxName}' sandbox has reached the limit of {limit} active fragments. To activate another fragment, archive or deactivate an existing active fragment first. | A sandbox can have [up to 200 active fragments](journey-fragments.md#guardrails). Archive or deactivate a fragment you do not use. |
| **AJOJAS-8009-429** | The '{sandboxName}' sandbox has reached the fragment limit of {limit}. To create a new fragment, archive or delete an existing one. | [Archive a fragment, or delete a **[!UICONTROL Draft]** fragment](journey-fragments.md#guardrails), that you no longer need before creating a new one. |
| **AJOJAS-7104-403** | You do not have permission to apply label '{labelName}' to fragment '{fragmentId}'. Contact your administrator to request access. | You do not have [access to the label](journey-fragments.md). Ask your administrator for access, or choose another label. |

## Compare journey versions {#compare-versions}

These errors occur when you compare two versions of a journey.

| Error code | Message | How to fix |
|---|---|---|
| **AJOJAS-11001-400**, **11004-400**, **11005-400** | The selected versions are the same. Choose two different versions to compare.<br/>Comparison requires two versions. Select both versions, then try again.<br/>The selected versions are not in chronological order. Swap them and try again. | [Select two different versions](journeys-coworker-skills.md), in chronological order. |
| **AJOJAS-11007-400** | A journey has disconnected activities, which prevents comparison. Connect all activities and try again. | Connect all activities (or delete the unused ones) in the version, then [compare again](journeys-coworker-skills.md). |

## Related topics {#related}

* [Error codes reference](error-codes-reference.md)
* [Validate and publish a journey](publish-journey.md)
* [Test your journey](testing-the-journey.md)
* [Troubleshoot journey errors](troubleshooting.md)
* [Troubleshoot journey execution](troubleshooting-execution.md)
* [Journey FAQs](journey-faq.md)
* [Best practices to avoid common errors](error-codes-reference.md#best-practices)
* [Guardrails and limitations](../start/guardrails.md)
