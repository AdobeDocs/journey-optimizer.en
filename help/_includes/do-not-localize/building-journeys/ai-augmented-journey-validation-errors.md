---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** The page explains the cause and the fix for the validation errors that [!DNL Adobe Journey Optimizer] returns when you validate, test, or publish a journey, grouped by the activity or rule involved.

### Intents

* Identify what a journey validation error code such as `AJOJAS-2030-400` means.
* Find the cause and the fix of an error returned by **[!UICONTROL Validate]**, by a test, or by publication.
* Find which activity or rule an error family relates to (structure, **[!UICONTROL Read audience]**, Adobe Campaign actions, **[!UICONTROL Update profile]**, **[!UICONTROL Dataset lookup]**, **[!UICONTROL Jump]**, **[!UICONTROL Wait]**, **[!UICONTROL Condition]**, events, **[!UICONTROL Content decision]**, Select package, versions, fragments, version comparison).
* Find the limits that trigger some of the errors (fields, keys, journey size, fragment activities).

### Glossary

* **[!UICONTROL Validate]** *(product-specific)*: selected in the journey header. Selecting it, or trying to test or publish a journey, runs the journey check.
* **[!UICONTROL Alerts]** *(product-specific)*: the panel where the journey check lists the errors.
* **AJOJAS** *(product-specific)*: the prefix of journey validation errors. It stands for Journey Authoring Service.
* **Error code** format: prefix, error number, HTTP status. Example: `AJOJAS-2030-400`, a missing wait duration.
* **Fragment** *(product-specific)*: a journey fragment. Fragment errors are in the **Journey fragments** section of the page.
* **Select package** *(product-specific)*: the **Select** license package. Its errors apply to unitary journeys.

### Guardrails

* **Dataset lookup:** only leaf fields can be selected, up to 20 (error `AJOJAS-2073-400`). A lookup can use up to 50 keys (error `AJOJAS-2074-400`).
* **Journey size:** error `AJOJAS-7003-413` is returned when the journey is larger than 2 MB. The **[!UICONTROL Current journey payload size]** indicator in the journey properties shows the size.
* **Fragment size:** a fragment can contain up to 20 activities (error `AJOJAS-8005-400`).
* **Active fragments:** a sandbox can have up to 200 active fragments (error `AJOJAS-8024-429`). Errors `AJOJAS-8009-429` and `AJOJAS-8024-429` report a limit reached in the sandbox; the message gives the value in `{limit}`.
* **Read audience:** a journey can have only one **[!UICONTROL Read audience]** activity (error `AJOJAS-3003-400`).
* **Parallel paths:** only event and **[!UICONTROL Wait]** activities can be placed in parallel after an activity (error `AJOJAS-3018-400`). When events are in parallel, only one timeout can be defined (error `AJOJAS-3027-400`).
* **Version types:** all versions of a journey must start with the same type of activity as version 1: event, **[!UICONTROL Audience qualification]**, or **[!UICONTROL Read audience]** (error `AJOJAS-3024-400`).
* **Fragment names:** names must be unique in a sandbox (errors `AJOJAS-8001-409` and `AJOJAS-8008-409`).

### Terminology

* Canonical name: Journey validation errors — variants: validation errors, journey errors.
* Prefix: **AJOJAS** (Journey Authoring Service). Other error code prefixes are in the error codes reference.
* The error messages quote internal terms such as "node", "edge", "segment", "ACS", and "ACC". The "How to fix" column uses the user-facing names: activity, **[!UICONTROL Read audience]**, **[!UICONTROL Audience qualification]**, Adobe Campaign Standard, and Adobe Campaign v7/v8.
* Acronyms: ACS = Adobe Campaign Standard, ACC = Adobe Campaign Classic (v7/v8).
* The "Read segment" messages (`AJOJAS-2007-400`, `AJOJAS-3003-400`) are listed in the **Read audience and identity namespace** section, and the fix names the **[!UICONTROL Read audience]** activity.
* **Do not confuse:** an event timeout (`AJOJAS-2041-400`, **[!UICONTROL Define the event timeout]**) and the timeout or error path of an action (`AJOJAS-5001-400`, Select package).

### FAQ

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
A journey in test mode cannot be modified: turn off test mode, make your changes, then test again. Turning off test mode removes the profiles that entered the journey and clears its reporting. A live journey is read-only: you can only change the activity labels and descriptions, and the journey name and description. To make other changes, create a new version, edit it, and publish it.

**The journey is too large (`AJOJAS-7003-413`). What do I do?**
The journey is larger than 2 MB. Simplify complex expressions and conditions, reduce data mappings, or split the journey.

**A fragment could not be activated because it has validation errors (`AJOJAS-8025-400`, `8033-400`). What do I do?**
Fix the errors shown on the fragment canvas, then activate again.

### Troubleshooting

* **Journey structure.** Causes: no entry activity, or activities in a layout that is not supported (`AJOJAS-1000-400`, `3018-400`, `3027-400`, `3028-403`). Fix: add an entry activity, place activities one after the other, keep one timeout on parallel events, and disable the timeout on the first event of the journey.
* **Read audience and identity namespace.** Causes: incomplete schedule (`AJOJAS-2007-400`, `2008-400`, `2009-400`), more than one **[!UICONTROL Read audience]** activity (`3003-400`), activity not first or not right after a business event (`3005-400`, `3006-400`), missing identity namespace (`AJOJAS-3013-400` to `3017-400`). Fix: in **[!UICONTROL Schedule]**, set the recurrence, the time of day, and the start date; keep one activity placed first or right after a business event; select the identity namespace in the first activity of the journey. A namespace is required for journeys that use **[!UICONTROL Read audience]**, **[!UICONTROL Audience qualification]**, message actions, jump actions, or profile updates.
* **Activity compatibility.** Cause: a journey combines activities that cannot be used together, such as Adobe Campaign actions with **[!UICONTROL Read audience]** or **[!UICONTROL Audience qualification]**, or a **[!UICONTROL Jump]** with **[!UICONTROL Read audience]**.
* **Action activities.** Causes: a channel action with no message (`AJOJAS-2014-400`, message: "'{messageType}' message action in node '{nodeId}': missing message id"), a surface still in use (`AJOJAS-2065-400`, "Surfaces are deprecated. Please use channel configurations instead"), a custom action parameter with no value (`AJOJAS-2021-400`), Campaign Standard address or personalization parameters not mapped (`AJOJAS-2012-400`, `2013-400`), send time optimization not in the license package (`AJOJAS-6003-403`, `6004-403`). Fix: select or create the message, select a channel configuration, set each mandatory parameter to a constant, a field, or an expression, map the Campaign Standard parameters, or turn off send time optimization or contact your Adobe representative about upgrading.
* **Update profile.** Cause: incomplete schema, dataset, or attribute configuration (`AJOJAS-2022-400` to `2026-400`). Fix: select the schema, then the profile-enabled dataset, then the attributes to update, and set each attribute value as a constant, a field, or an expression.
* **Dataset lookup.** Cause: no dataset, fields, or lookup keys (`AJOJAS-2070-400` to `2074-400`). Fix: select the dataset and the fields to retrieve (leaf fields only, up to 20), and define the lookup keys in advanced mode (up to 50).
* **Jump.** Cause: no target journey (`AJOJAS-2027-400`, `2028-400`). Fix: select the target journey. Only draft, live, or test-mode journeys with the same namespace are listed.
* **Wait, conditions, and event timeouts.** Causes: a missing value (`AJOJAS-2030-400` wait duration, `2032-400` custom wait expression, `2056-400` no condition defined, `2033-400` path without a condition, `2039-400` time condition without a day, `2041-400` event timeout without a delay). Fix: enter a duration and a unit; build the expression in the **[!UICONTROL Custom]** option; define at least one path with a condition, and a condition for each path (or delete the paths you do not need); select at least one day; set a duration under **[!UICONTROL Define the event timeout]**.
* **Events and reactions.** Causes: an **[!UICONTROL Audience qualification]** or **[!UICONTROL Reaction]** activity not configured as required (`AJOJAS-2045-400`, `2046-400`, `2048-400`). Fix: select **[!UICONTROL Enter]**, **[!UICONTROL Exit]**, or both; place the **[!UICONTROL Reaction]** right after the channel action it reacts to and select that action in its properties. Reactions work only with built-in channel actions; to react to a message sent through a custom action, configure a dedicated event.
* **Content decision.** Cause: no decision policy (`AJOJAS-2067-400`). Fix: open the **[!UICONTROL Content decision]** activity and select **[!UICONTROL Add decision policy]**.
* **License package limits (Select).** These errors apply to unitary journeys on the **Select** license package: only one action (`AJOJAS-5007-403`), no condition (`5006-403`), no wait (`5005-403`), and timeout and error paths of an action must lead directly to an **[!UICONTROL End]** activity (`5001-400`). Fix: keep one action, remove the **[!UICONTROL Condition]** or **[!UICONTROL Wait]** activity, or connect the paths to **[!UICONTROL End]**. To use these activities with the Select package, use a Read audience journey, or ask your Adobe representative about upgrading your package.
* **Versions, test mode, and size.** Causes: a version of another type (`AJOJAS-3024-400`), a journey in test mode (`4001-403`), a live journey (`4002-403`), a journey larger than 2 MB (`7003-413`). Fix: create a new journey instead of changing the entry activity; turn off test mode; create a new version; reduce the journey size.
* **Journey fragments.** Causes and fixes by group:
  * Name: required (`AJOJAS-8002-400`), already used in the sandbox (`8001-409`, `8008-409`), longer than the length shown in the message (`8003-400`).
  * Structure: more than 20 activities (`8005-400`), activities not connected to the starting node (`8006-400`), a **[!UICONTROL Jump]** activity (`8007-400`), more than one entry point (`8022-400`), no valid entry point (`8023-400`), a **[!UICONTROL Wait]** right after a business event (`8035-400`).
  * Activities: identity namespace missing (`8026-400`, `8027-400`), Campaign actions with **[!UICONTROL Read audience]** or **[!UICONTROL Audience qualification]** (`8028-400` to `8031-400`).
  * Status: the fragment status does not allow the action (`8010-400`, `8016-400`). Only **[!UICONTROL Draft]** fragments can be edited or activated. Only **[!UICONTROL Active]** fragments can be deactivated or archived. Only **[!UICONTROL Archived]** fragments can be unarchived. A fragment that is already archived (`8014-400`) needs no action; unarchiving it returns it to **[!UICONTROL Draft]** status.
  * Limits: 200 active fragments in a sandbox (`8024-429`; archive or deactivate a fragment you do not use) and the sandbox fragment limit (`8009-429`; archive a fragment, or delete a **[!UICONTROL Draft]** fragment, that you no longer need).
  * Permission: no access to the label to apply (`AJOJAS-7104-403`). Ask your administrator for access, or choose another label.
* **Compare journey versions.** Causes: the same version selected twice, one version only, versions not in chronological order (`AJOJAS-11001-400`, `11004-400`, `11005-400`), or disconnected activities (`11007-400`). Fix: select two different versions in chronological order, and connect all activities (or delete the unused ones).

### Related pages

* Other error code prefixes and best practices to avoid common errors: Error codes reference (building-journeys/error-codes-reference.md)
* Validating and publishing a journey: Validate and publish a journey (building-journeys/publish-journey.md)
* Test mode: Test your journey (building-journeys/testing-the-journey.md)
* Canvas and activity errors: Troubleshoot journey errors (building-journeys/troubleshooting.md)
* Execution issues: Troubleshoot journey execution (building-journeys/troubleshooting-execution.md)
* Common questions: Journey FAQs (building-journeys/journey-faq.md)
* Limits and guardrails: Guardrails and limitations (start/guardrails.md)
* Fragment guardrails and statuses: Fragment guardrails and limitations (building-journeys/journey-fragments.md)

+++

<!-- ai-section-version: 1 | source-hash: 034410e5 -->
