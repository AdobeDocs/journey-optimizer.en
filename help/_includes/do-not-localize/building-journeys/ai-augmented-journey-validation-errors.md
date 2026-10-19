---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** The page explains the cause and the fix for the validation errors that [!DNL Adobe Journey Optimizer] returns when you validate, test, or publish a journey, grouped by the activity or rule involved.

**Intents:**

* Identify what a journey validation error code such as `AJOJAS-2030-400` means.
* Find the cause and the fix of an error returned by **[!UICONTROL Validate]**, by a test, or by publication.
* Find which activity or rule an error family relates to (structure, **[!UICONTROL Read audience]**, Adobe Campaign actions, **[!UICONTROL Update profile]**, **[!UICONTROL Dataset lookup]**, **[!UICONTROL Jump]**, **[!UICONTROL Wait]**, **[!UICONTROL Condition]**, events, **[!UICONTROL Content decision]**, Select package, versions, fragments, version comparison).
* Find the limits that trigger some of the errors (fields, keys, journey size, fragment activities).

**Glossary:**

* **[!UICONTROL Validate]** *(product-specific)*: selected in the journey header. Selecting it, or trying to test or publish a journey, runs the journey check.
* **[!UICONTROL Alerts]** *(product-specific)*: the panel where the journey check lists the errors.
* **AJOJAS** *(product-specific)*: the prefix of journey validation errors. It stands for Journey Authoring Service.
* **Error code** format: prefix, error number, HTTP status. Example: `AJOJAS-2030-400`, a missing wait duration.
* **Fragment** *(product-specific)*: a journey fragment. Fragment errors are in the **Journey fragments** section of the page.
* **Select package** *(product-specific)*: the **Select** license package. Its errors apply to unitary journeys.

**Guardrails:**

* **Dataset lookup:** only leaf fields can be selected, up to 20 (error `AJOJAS-2073-400`). A lookup can use up to 50 keys (error `AJOJAS-2074-400`).
* **Journey size:** error `AJOJAS-7003-413` is returned when the journey is larger than the default maximum payload size of 2 MB (some organizations may have custom limits). The **[!UICONTROL Current journey payload size]** indicator in the journey properties shows the size.
* **Fragment size:** a fragment can contain up to 20 activities (error `AJOJAS-8005-400`).
* **Active fragments:** a sandbox can have up to 200 active fragments (error `AJOJAS-8024-429`). Errors `AJOJAS-8009-429` and `AJOJAS-8024-429` report a limit reached in the sandbox; the message gives the value in `{limit}`.
* **Read audience:** a journey can have only one **[!UICONTROL Read audience]** activity (error `AJOJAS-3003-400`).
* **Parallel paths:** only event and **[!UICONTROL Wait]** activities can be placed in parallel after an activity (error `AJOJAS-3018-400`). When events are in parallel, only one timeout can be defined (error `AJOJAS-3027-400`).
* **Version types:** all versions of a journey must start with the same type of activity as version 1: event, **[!UICONTROL Audience qualification]**, or **[!UICONTROL Read audience]** (error `AJOJAS-3024-400`).
* **Fragment names and IDs:** names must be unique in a sandbox (error `AJOJAS-8008-409`), and so must IDs (error `AJOJAS-8001-409`).

**Terminology:**

* Canonical name: Journey validation errors — variants: validation errors, journey errors.
* Prefix: **AJOJAS** (Journey Authoring Service). Other error code prefixes are in the error codes reference.
* The error messages quote internal terms such as "node", "edge", "segment", "ACS", and "ACC". The "How to fix" column uses the user-facing names: activity, **[!UICONTROL Read audience]**, **[!UICONTROL Audience qualification]**, Adobe Campaign Standard, and Adobe Campaign v7/v8.
* Acronyms: ACS = Adobe Campaign Standard, ACC = Adobe Campaign Classic (v7/v8).
* The "Read segment" messages (`AJOJAS-2007-400`, `2008-400`, `2009-400`, `3003-400`, `3005-400`, `3006-400`) are listed in the **Read audience and identity namespace** section, and the fix names the **[!UICONTROL Read audience]** activity.

**FAQ:**

**What does the AJOJAS prefix mean?**
Validation errors use the prefix **AJOJAS** (Journey Authoring Service), followed by an error number and an HTTP status.

**Where do I see validation errors?**
When you select **[!UICONTROL Validate]** in the journey header, or try to test or publish a journey, the errors are listed in the **[!UICONTROL Alerts]** panel. Most messages name the activity concerned, so you can select it on the canvas and fix its configuration.

**The journey has no entry activity (`AJOJAS-1000-400`). What do I do?**
Add an **[!UICONTROL Event]**, **[!UICONTROL Business event]**, **[!UICONTROL Read audience]**, or **[!UICONTROL Audience qualification]** activity as the first activity.

**An Adobe Campaign action is rejected (`AJOJAS-3001-403`, `3004-403`, `3007-403`, `3009-403`, `3010-403`). Why?**
Adobe Campaign Standard and Adobe Campaign v7/v8 actions cannot be used with **[!UICONTROL Read audience]** (`AJOJAS-3001-403`, `3004-403`): remove the Campaign action, or start the journey with an event. They also cannot be used with **[!UICONTROL Audience qualification]** (`AJOJAS-3007-403`, `3009-403`): remove the Campaign action, or replace it with a built-in channel action. Use only Campaign Standard actions, or only built-in channel actions, in the same journey (`AJOJAS-3010-403`); Campaign v7/v8 actions can be used with built-in channel actions.

**Why is a [!UICONTROL Jump] activity rejected (`AJOJAS-3002-403`)?**
A **[!UICONTROL Jump]** activity cannot be used in the same journey as a **[!UICONTROL Read audience]** activity. Remove the **[!UICONTROL Jump]**, or start the journey with an event.

**Why can I not edit my journey (`AJOJAS-4001-403`, `AJOJAS-4002-403`)?**
A journey in test mode cannot be modified: turn off test mode, make your changes, then test again. Turning off test mode removes the profiles that entered the journey and clears its reporting. On a live journey, you can only change the activity labels and descriptions, and the journey name and description. To make other changes, create a new version, edit it, and publish it.

**The journey is too large (`AJOJAS-7003-413`). What do I do?**
The journey is larger than the default maximum payload size of 2 MB. Check the **[!UICONTROL Current journey payload size]** indicator in the journey properties. Simplify complex expressions and conditions, reduce data mappings, or split the journey.

**A fragment could not be activated because it has validation errors (`AJOJAS-8025-400`, `8033-400`). What do I do?**
Open the fragment, fix each error shown on its canvas, then select the **[!UICONTROL Activate]** icon again.

**Troubleshooting:**

* **Journey structure.** Causes: no entry activity, or activities in a layout that is not supported (`AJOJAS-1000-400`, `3018-400`, `3027-400`, `3028-403`). Fixes: `1000-400`, add an entry activity; `3018-400`, place the activities other than event and **[!UICONTROL Wait]** activities one after the other; `3027-400`, keep the timeout on one event, or place the events one after the other; `3028-403`, disable the timeout on the first event of the journey.
* **Read audience and identity namespace.** Causes: incomplete schedule (`AJOJAS-2007-400`, `2008-400`, `2009-400`), more than one **[!UICONTROL Read audience]** activity (`3003-400`), activity with more than one incoming path (`3005-400`) or placed after another activity (`3006-400`), missing identity namespace (`AJOJAS-3013-400`, `3017-400`). Fixes: in **[!UICONTROL Schedule]**, set the recurrence (`2007-400`), the time of day (`2008-400`), or the start date (`2009-400`); keep one **[!UICONTROL Read audience]** activity, and combine several audiences into a single audience first (`3003-400`); keep a single path into the activity, from the journey start or a business event (`3005-400`); move it to be the first activity of the journey, or right after a business event (`3006-400`); open the **[!UICONTROL Read audience]** activity and select an identity namespace in the **[!UICONTROL Namespace]** field (`3013-400`); for a journey that uses a profile update action (`3017-400`), open the first activity (**[!UICONTROL Read audience]**, **[!UICONTROL Audience qualification]**, or event) and select an identity namespace.
* **Activity compatibility.** Cause: a journey combines activities that cannot be used together, such as Adobe Campaign actions with **[!UICONTROL Read audience]** or **[!UICONTROL Audience qualification]**, or a **[!UICONTROL Jump]** with **[!UICONTROL Read audience]**.
* **Action activities.** Causes: a channel action with no message (`AJOJAS-2014-400`, message: "'{messageType}' message action in node '{nodeId}': missing message id"), a surface still in use (`AJOJAS-2065-400`, "Surfaces are deprecated. Please use channel configurations instead"), a custom action parameter with no value (`AJOJAS-2021-400`), Campaign Standard address or personalization parameters not mapped (`AJOJAS-2012-400`, `2013-400`), send time optimization not in the license package (`AJOJAS-6003-403`, `6004-403`). Fixes: `2014-400`, open the activity and select or create the message; `2065-400`, open each channel action that uses a surface and select a channel configuration instead; `2021-400`, set each mandatory parameter to a constant, a field, or an expression; `2012-400`, map the address to a field, constant, or expression; `2013-400`, map the personalization parameter named in the message to a field, constant, or expression; `6003-403`, turn off send time optimization on the email action, or contact your Adobe representative about upgrading; `6004-403`, turn off send time optimization on the push action, or contact your Adobe representative about upgrading.
* **Update profile.** Cause: incomplete schema, dataset, or attribute configuration (`AJOJAS-2022-400` to `2026-400`). Fixes: `2022-400` and `2023-400`, open the **[!UICONTROL Update profile]** activity and select the schema, then the profile-enabled dataset, then the attributes to update; `2024-400`, select the profile-enabled dataset, then the attributes to update; `2025-400`, select the profile field for each attribute to update; `2026-400`, set the value of each attribute as a constant, a field, or an expression.
* **Dataset lookup.** Cause: no dataset, fields, or lookup keys (`AJOJAS-2070-400` to `2074-400`). Fixes: `2070-400`, `2071-400`, and `2072-400`, open the **[!UICONTROL Dataset lookup]** activity and select the dataset and the fields to retrieve; `2073-400`, select the fields to retrieve (leaf fields only, up to 20); `2074-400`, in the **[!UICONTROL Lookup key(s)]** field of the **[!UICONTROL Dataset lookup]** activity, define the lookup keys in **[!UICONTROL Advanced mode]** (up to 50 keys).
* **Jump.** Causes: the **[!UICONTROL Jump]** activity has no target event (`AJOJAS-2027-400`) or no target journey (`2028-400`). Fix: open the activity and select the target journey. Only draft, live, or test-mode journeys with the same namespace are listed.
* **Wait, conditions, and event timeouts.** Causes: a missing value (`AJOJAS-2030-400` wait duration, `2032-400` custom wait expression, `2056-400` no condition defined, `2033-400` path without a condition, `2039-400` time condition without a day, `2041-400` event timeout without a delay). Fixes: `2030-400`, enter a duration and a unit in the **[!UICONTROL Wait]** activity; `2032-400`, in the **[!UICONTROL Custom]** option, build the expression that returns the date to wait until; `2056-400`, define at least one path with a condition in the **[!UICONTROL Condition]** activity; `2033-400`, define a condition for each path (or delete the paths you do not need); `2039-400`, select at least one day in the time condition; `2041-400`, set a duration under **[!UICONTROL Define the event timeout]** in the event properties.
* **Events and reactions.** Causes: an **[!UICONTROL Audience qualification]** or **[!UICONTROL Reaction]** activity not configured as required (`AJOJAS-2045-400`, `2046-400`, `2048-400`). Fixes: `2045-400`, select **[!UICONTROL Enter]**, **[!UICONTROL Exit]**, or both in the **[!UICONTROL Audience qualification]** activity; `2046-400`, place the **[!UICONTROL Reaction]** right after the channel action it reacts to and select that action in its properties; `2048-400`, reactions work only with built-in channel actions, so to react to a message sent through a custom action, configure a dedicated event.
* **Content decision.** Cause: no decision policy (`AJOJAS-2067-400`). Fix: open the **[!UICONTROL Content decision]** activity and select **[!UICONTROL Add decision policy]**.
* **License package limits (Select).** These errors apply to unitary journeys on the **Select** license package: only one action (`AJOJAS-5007-403`), no condition (`5006-403`), no wait (`5005-403`), and timeout and error paths of an action must lead directly to an **[!UICONTROL End]** activity (`5001-400`). Fixes: `5007-403`, keep one action activity; `5006-403`, remove the **[!UICONTROL Condition]** activity; `5005-403`, remove the **[!UICONTROL Wait]** activity; `5001-400`, connect the timeout and error paths to **[!UICONTROL End]**. To use these activities with the Select package, use a Read audience journey, or ask your Adobe representative about upgrading your package.
* **Versions, test mode, and size.** Causes: a version of another type (`AJOJAS-3024-400`), a journey in test mode (`4001-403`), a live journey (`4002-403`), a journey larger than the default maximum payload size of 2 MB (`7003-413`). Fixes: `3024-400`, start the new version with the same type of activity as version 1, or create a new journey for a different entry activity; `4001-403`, turn off test mode, make your changes, then test again; `4002-403`, create a new version, edit it, and publish it; `7003-413`, simplify complex expressions and conditions, reduce data mappings, or split the journey, and check the **[!UICONTROL Current journey payload size]** indicator.
* **Journey fragments.** Causes and fixes by group:
  * Name: required (`AJOJAS-8002-400`), ID already used in the sandbox (`8001-409`, choose a different ID, or open the existing fragment), name already used in the sandbox (`8008-409`, choose a different name, or open the existing fragment), longer than the length shown in the message (`8003-400`).
  * Structure: more than 20 activities (`8005-400`), activities not connected to the starting node (`8006-400`), a **[!UICONTROL Jump]** activity (`8007-400`), more than one entry point (`8022-400`), no valid entry point (`8023-400`), a **[!UICONTROL Wait]** right after a business event (`8035-400`).
  * Activities: identity namespace missing (`8026-400`, `8027-400`), Campaign actions in a fragment that contains **[!UICONTROL Read audience]** (`8028-400`, `8029-400`: remove the Campaign action, or replace the **[!UICONTROL Read audience]** activity) or **[!UICONTROL Audience qualification]** (`8030-400`, `8031-400`: remove the Campaign action, or remove the **[!UICONTROL Audience qualification]** activity).
  * Status: the fragment status does not allow the action (`8010-400`, `8016-400`). Check the fragment status in the **[!UICONTROL Fragment Inventory]**. Only **[!UICONTROL Draft]** fragments can be edited or activated. Only **[!UICONTROL Active]** fragments can be deactivated or archived. Only **[!UICONTROL Archived]** fragments can be unarchived. For a fragment that is already archived (`8014-400`), to use it again, select **[!UICONTROL Unarchive]** from its **[!UICONTROL More actions]** menu; it returns to **[!UICONTROL Draft]** status.
  * Limits: 200 active fragments in a sandbox (`8024-429`; archive or deactivate a fragment you do not use) and the sandbox fragment limit (`8009-429`; archive a fragment, or delete a **[!UICONTROL Draft]** fragment, that you no longer need).
  * Permission: no access to the label to apply (`AJOJAS-7104-403`). Ask your administrator for access, or choose another label.
* **Compare journey versions.** Causes: the same version selected twice, one version only, versions not in chronological order (`AJOJAS-11001-400`, `11004-400`, `11005-400`), or disconnected activities (`11007-400`). Fixes: `11001-400`, in Coworker Chat, select two different versions; `11004-400`, in Coworker Chat, select both versions; `11005-400`, switch the order of the two selected versions so that the older one comes first; `11007-400`, connect all activities (or delete the unused ones) in the version, then compare again.

**Related pages:**

* Other error code prefixes and best practices to avoid common errors: Error codes reference (building-journeys/error-codes-reference.md)
* Validating and publishing a journey: Validate and publish a journey (building-journeys/publish-journey.md)
* Test mode: Test your journey (building-journeys/testing-the-journey.md)
* Canvas and activity errors: Troubleshoot journey errors (building-journeys/troubleshooting.md)
* Execution issues: Troubleshoot journey execution (building-journeys/troubleshooting-execution.md)
* Common questions: Journey FAQs (building-journeys/journey-faq.md)
* Limits and guardrails: Guardrails and limitations (start/guardrails.md)
* Fragment guardrails and statuses: Fragment guardrails and limitations (building-journeys/journey-fragments.md)

+++

<!-- ai-section-version: 1 | source-hash: 74164b82 -->
