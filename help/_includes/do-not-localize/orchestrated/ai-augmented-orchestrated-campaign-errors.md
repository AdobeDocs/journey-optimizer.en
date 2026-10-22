---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page lists the errors that [!DNL Adobe Journey Optimizer] returns when you build, test, schedule, publish, or trigger an Orchestrated campaign, grouped by feature, with the cause and the fix of each.

**Intents:**
* Know what to note and whom to contact when an error persists after the listed steps

* Find the cause and the fix of an error returned for an Orchestrated campaign
* Fix permission and access errors when creating, editing, publishing, or triggering an Orchestrated campaign
* Fix errors caused by the status of the campaign (Draft, Live, running, started)
* Fix errors returned when starting or stopping a test, or when configuring activities, the schedule, signals, or waves
* Locate the activity concerned by an error through the campaign logs and the alerts on the canvas

**Glossary:**

* **CJMOC**: Prefix of all Orchestrated campaign errors, followed by an error number and an HTTP status, for example CJMOC-1001-403 *(product-specific)*
* **Campaign logs**: Logs that show the error code and the message; open them to find the activity concerned *(product-specific)*
* **Alerts on the canvas**: Alerts that show the error code and the message *(product-specific)*
* **Channel activity**: Activity of an Orchestrated campaign with a message attached to it (CJMOC-5001-400) *(product-specific)*
* **Targeting dimension**: Dimension selected in an activity, or set by a **[!UICONTROL Change dimension]** activity *(product-specific)*
* **Signal**: Trigger of a campaign, from the API or from the **[!UICONTROL End]** activity of another campaign *(product-specific)*
* **Waves**: Sending of messages in waves *(product-specific)*

**Guardrails:**

* A campaign can contain up to 10 channel activities (hard limit). Error CJMOC-6017-400 is returned when the number is exceeded. Reduce the number of channel activities, or split the delivery across several campaigns.
* A campaign needs at least one channel activity or **[!UICONTROL Save audience]** activity (CJMOC-5002-400).
* A test can be started only while the campaign is in **[!UICONTROL Draft]** status, and not while a test is already running on the campaign (CJMOC-2001-400, CJMOC-2002-400).
* A campaign must be in **[!UICONTROL Draft]** status to be published (CJMOC-1203-400, CJMOC-6005-400); a campaign in **[!UICONTROL Live]** status must be stopped, or sent back to draft with **[!UICONTROL Back to draft]** when it is available, before it is edited and published again (CJMOC-1202-400).
* A campaign cannot be both triggered by a signal and recurring (CJMOC-6041-400).
* A recurring schedule cannot use a fixed time (CJMOC-5014-400).
* Waves are not supported for recurring campaigns or signal-triggered campaigns (CJMOC-6045-400, CJMOC-6046-400).
* A recurring campaign that already started cannot be unpublished (CJMOC-6040-500): stop it to prevent future executions, or duplicate it to make changes.
* When a side effect activity has already started (CJMOC-6039-500), stop the campaign and create a new campaign.
* A targeting dimension cannot be deleted while active channel configurations reference it (CJMOC-1226-400).
* The **[!UICONTROL Load file]** activity is not meant to be used in a scheduled campaign, due to the short data lifetime of uploaded files (warning CJMOC-5023-199).

**Prerequisites and permissions:**

* The **[!DNL Publish orchestrated campaigns]** permission in your role to publish or trigger a campaign (CJMOC-1005-403).
* A permission in your role for the action, such as **[!DNL Manage orchestrated campaigns]** to edit or **[!DNL Publish orchestrated campaigns]** to publish (CJMOC-1001-403). For CJMOC-1005-403, the permission is named in the message.
* Access to the attributes used by the campaign (CJMOC-1004-403): the attributes may carry an access label that your role does not include. Ask your administrator to add that label to your role, or remove those attributes from the campaign if access cannot be granted.
* Object-level access to the object concerned (CJMOC-1215-403, CJMOC-1216-403, "OLAC check failed"): your role must have object-level access to the resource named in the message, or to create the object (CJMOC-1216-403).

**Applicability:**

* These errors apply to Orchestrated campaigns. The page documents the prefix CJMOC only; for the other prefixes, see the error codes reference.

**Terminology:**

* Canonical name: Orchestrated campaign errors — Acronym: OLAC (Object level access control) — variants: CJMOC errors
* Do not confuse: a recurring schedule ≠ **[!UICONTROL Triggered by a signal]**

**FAQ:**
* **Q: What do I do if the error persists after the listed steps?** — Note the error code, the message, the request ID, and the campaign, journey, or activity concerned, and keep the logs or screenshots. For a permission or access error, contact your administrator; otherwise contact Adobe Support with these details. For all the support options, see the Getting support section of the error codes reference.

* **Q: How is an Orchestrated campaign error code structured?** — The prefix CJMOC, an error number, and an HTTP status.
* **Q: Where do I find the activity concerned by an error?** — The campaign logs and the alerts on the canvas show the error code and the message. Open the campaign logs to find the activity concerned.
* **Q: Which error is a warning?** — CJMOC-5023-199, about the **[!UICONTROL Load file]** activity in a scheduled campaign. Use another data source for scheduled campaigns, or run the campaign once.
* **Q: Which permission do I need to publish or trigger a campaign?** — **[!DNL Publish orchestrated campaigns]** (CJMOC-1005-403). For CJMOC-1005-403, check the permission named in the message against the permissions of your role. For CJMOC-1001-403, check that your role includes the permission for the action, such as **[!DNL Manage orchestrated campaigns]** to edit. In both cases, ask your administrator to add the missing permission to your role.
* **Q: Why can I not publish or edit my campaign?** — The campaign is not in **[!UICONTROL Draft]** status, or its ID is not set (CJMOC-1201-400), it cannot be published because it is not in **[!UICONTROL Draft]** status (CJMOC-1203-400), or its current version is not in **[!UICONTROL Draft]** status (CJMOC-6005-400): check the campaign status, and duplicate the campaign to start again from a Draft. The current version is in **[!UICONTROL Live]** status (CJMOC-1202-400): stop the campaign, or click **[!UICONTROL Back to draft]** when it is available, then edit the campaign and publish it again. The campaign is still running (CJMOC-6006-400): stop it, or wait for it to finish, then publish the campaign again.
* **Q: Why can I not start a test?** — The campaign is not in **[!UICONTROL Draft]** status (CJMOC-2001-400: check the campaign status, or duplicate the campaign), a test is already running (CJMOC-2002-400: stop it or restart it, then start a new test), or the campaign has no orchestration defined (CJMOC-2006-400: add activities to the canvas and save the campaign).
* **Q: Why do I get a schedule error?** — The campaign has no schedule (CJMOC-5012-400: define a schedule), no execution in the future (CJMOC-5013-400: update the start date, or extend the validity period of the schedule), a fixed time with a recurring schedule (CJMOC-5014-400: remove the fixed time, or use a one-time schedule), or a fixed time in the past (CJMOC-5015-400: set a date and time in the future).
* **Q: Why can I not publish a campaign chained from an End activity?** — The downstream campaign must be live (CJMOC-6042-400) and set to **[!UICONTROL Triggered by a signal]** (CJMOC-6043-400), and it must exist and be accessible (CJMOC-6044-400).

**Troubleshooting:**

* **CJMOC-1001-403**, "Unauthorized access to the resource." — Check that your role includes the permission for this action, such as **[!DNL Manage orchestrated campaigns]** to edit or **[!DNL Publish orchestrated campaigns]** to publish, and ask your administrator to add the missing one.
* **CJMOC-1005-403** — Check the permission named in the message against the permissions of your role, and ask your administrator to add it. Publishing or triggering a campaign requires **[!DNL Publish orchestrated campaigns]**.
* **CJMOC-1004-403** — Check whether the attributes used in the campaign carry an access label that your role does not include, and ask your administrator to add that label to your role. If access cannot be granted, remove those attributes from the campaign.
* **CJMOC-1215-403** and **CJMOC-1216-403** ("OLAC check failed") — Ask your administrator to check that your role has object-level access to the resource named in the message (CJMOC-1215-403) or to create this object (CJMOC-1216-403).
* **CJMOC-5008-400** — The activity named in the message is disabled. Enable the activity again, then retry.
* **CJMOC-5009-400** — The activity named in the message is paused. Enable the activity again, then retry.
* **CJMOC-5003-400** — The activity has an empty query. Open the activity and build the rule, or select an audience.
* **CJMOC-5016-400** — Open the **[!UICONTROL Read audience]** activity and select an audience.
* **CJMOC-5022-400** — The **[!UICONTROL Read audience]** activity has a merge policy that does not match the one of the campaign. Select an audience that uses the merge policy of the campaign, or change the merge policy of the campaign.
* **CJMOC-5011-400** — Select a targeting dimension in the activity, or add a **[!UICONTROL Change dimension]** activity before it.
* **CJMOC-5001-400** — The activity has no campaign associated. Open the channel activity and create or select the message.
* **CJMOC-5026-400** — Enter both a title and a message in the **[!UICONTROL Alert]** activity.
* **CJMOC-5000-400** — Connect each outgoing transition of the activity to another activity, or delete the empty transition.
* **CJMOC-2009-400** — The activity must have been executed at least once. Run the campaign in test so that the activity executes, then check its data again.

**Related pages:**

* Campaign logs, test, lifecycle, and Back to draft: Start and monitor the campaign (orchestrated/start-monitor-campaigns.md)
* Activity limits: Guardrails and limitations (orchestrated/guardrails.md)
* Questions about Orchestrated campaigns: Orchestrated campaigns FAQ (orchestrated/orchestrated-campaigns-faq.md)
* Permissions: Built-in permissions (administration/ootb-permissions.md)
* Signals and chained campaigns: Trigger Orchestrated campaigns using a signal (orchestrated/trigger-orchestrated-campaign.md)
* Other error code prefixes: Error codes reference (building-journeys/error-codes-reference.md)
* Support options when an error persists: Getting support (building-journeys/error-codes-reference.md)
* Contacting Adobe Support: Support ticket guidelines (start/user-interface.md)

+++

<!-- ai-section-version: 1 | source-hash: f4f02562 -->
