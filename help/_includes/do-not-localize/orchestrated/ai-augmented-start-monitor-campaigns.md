---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to test, publish, revert, confirm sending, and monitor Orchestrated campaigns in Adobe Journey Optimizer, including the campaign lifecycle, execution logs, activity status indicators, and alerts.

**Intents:**

* Test an Orchestrated campaign in Draft status before publishing.
* Test a channel activity with Run test, without sending the message.
* Publish a campaign and understand the internal publication-time execution sequence.
* Revert a published campaign back to draft status using Back to draft.
* Confirm message sending for non-recurring campaigns after publishing.
* Monitor campaign execution through the visual flow, activity status indicators, and logs and tasks.
* Set up system alerts or an Alert activity to be notified of issues.

**Glossary:**

* **Draft**: the default status when a campaign is created, in which the campaign is being built and tested and is not yet active *(product-specific)*
* **Live**: the status after a campaign has been published and is executing *(product-specific)*
* **Completed**: the status once campaign execution has finished *(product-specific)*
* **Back to draft**: a feature that unpublishes and reverts an orchestrated campaign to draft status in specific situations, designed as a recovery mechanism to fix issues before any messages are sent *(product-specific)*
* **Confirm sending**: the explicit approval step required, by default, before a non-recurring campaign's channel activity sends messages after publishing *(product-specific)*
* **Logs and tasks**: the screen providing a complete history of campaign execution, recording all user actions and encountered errors, with separate Log and Tasks tabs *(product-specific)*
* **Alert activity**: a canvas activity that fires a custom alert when campaign execution reaches it *(product-specific)*

**Guardrails:**

* When testing a campaign in Draft status, all activities in the canvas are executed except **Save audience** activities and channel activities; there is no functional impact on your data or audience.
* In test mode, the workflow stops when it reaches a channel activity, so activities that follow a channel activity are not reached; test each channel activity with Run test. The logic that follows a message activity can only be validated by publishing the campaign and monitoring live execution.
* The test does not include the message rendering step; profiles can be excluded at send time on a rendering error even when the content is valid, and these exclusions might not appear in the test report.
* For triggered orchestrated campaigns, testing requires sending an API call signal to continue the test; the system waits for this call to start the campaign.
* The **Publish** button is disabled (greyed out) if there are unresolved errors; all errors must be fixed before publishing.
* On successful publishing, the campaign moves from Draft to Live status and becomes "Read only".
* By default, for non-recurring orchestrated campaigns, message delivery is paused after publishing until the send is explicitly confirmed from the channel activity's properties pane; until confirmed, the channel activity stays pending and no message is sent.
* Back to draft is available for scheduled campaigns awaiting execution only while the scheduled time has not yet been reached; if the campaign is recurring and at least one execution has already occurred, this option is no longer available.
* Back to draft is available for live campaigns with execution errors only when the campaign is paused due to the error and no campaign executions have been completed yet.
* During publication, Save Audience activities execute before message activities.
* During publication, profile data is resolved against a snapshot taken at publication time, not the real-time profile, to ensure consistency across the entire execution.
* During publication, consent is honored directly from the profile record for matching profiles and is not re-evaluated at send time.
* During publication, profiles that do not match an existing record are created on the fly during execution.
* Delivery events are recorded in the `ajo_message_feedback_event` dataset, the primary source for delivery logs and post-send validation.
* The Logs button, giving access to Logs and tasks, is available in both test and live mode in the canvas toolbar.

**Applicability:**

* Applies to: Orchestrated campaigns.
* Testing restriction (Save audience and channel activities not executed during test) applies to: Orchestrated campaign test mode in Draft status.
* Confirm sending (paused delivery pending explicit approval) applies to: non-recurring orchestrated campaigns.

**Terminology:**

* Canonical name: Orchestrated campaign — status values: Draft, Live, Completed (see also Scheduled, Stopped, Archived on the linked statuses page).
* Do not confuse: "Draft" (campaign being built and tested, not yet active) ≠ "Live" (published and executing) ≠ "Completed" (execution has finished).
* Do not confuse: "Stop" (stop execution at any time during test) ≠ "Restart" (reset and re-run the workflow in a single action) ≠ "Resume" (continue execution if previously paused).
* Do not confuse: "Preview schema" (view the work table schema for a transition) ≠ "Preview results" (see the transported data for a transition).

**FAQ:**

* **Q: What happens when I test an Orchestrated campaign in Draft status?** — All activities in the canvas are executed except Save audience activities and channel activities, with no functional impact on your data or audience.
* **Q: Why does the workflow stop during a test?** — In test mode, the workflow stops when it reaches a channel activity and does not continue to the activities that follow it; use Run test on the channel activity to simulate its execution without sending the message.
* **Q: Why does nothing happen after I click Run test?** — The button remains available even if the message content contains an error; check the Alerts / Warning icon in the canvas toolbar for a content-related error, fix it, and run the test again.
* **Q: What must be true before I can publish a campaign?** — All errors must be fixed; if the Publish button is disabled, you must check the error messages in the logs.
* **Q: Are messages sent immediately after publishing a non-recurring campaign?** — No, by default message delivery is paused until you explicitly confirm the send from the channel activity's properties pane.
* **Q: When can I use Back to draft?** — For scheduled campaigns awaiting execution before the scheduled time is reached (unless recurring with at least one execution already completed), or for live campaigns paused due to an execution error with no completed executions yet.
* **Q: Where are delivery events recorded?** — In the `ajo_message_feedback_event` dataset, the primary source for delivery logs and post-send validation.
* **Q: Where can I set up alerts for my Orchestrated campaign?** — From Administration > Alerts for system alerts, or by adding an Alert activity to the campaign canvas for custom alerts fired when execution reaches it.

**Best practices:**

* Before clicking Publish, confirm the campaign ran successfully in test mode with no errors in the logs, that message content has been previewed using Simulate Content, that the schedule is configured if applicable, and that you have reviewed the sending confirmation behavior.

**Related pages:**

* For all campaign statuses (including Scheduled, Stopped, Archived) and available actions at each stage: Understanding campaign statuses (campaigns/manage-campaigns.md)
* For testing signal-triggered campaigns: Learn how to test signal-triggered campaigns (orchestrated/trigger-orchestrated-campaign.md)
* For working with channel activities and simulating message content: Learn how to work with channel activities and simulate content (orchestrated/activities/channels.md)
* For configuring a campaign schedule: schedule is configured (orchestrated/create-orchestrated-campaign.md)
* For details on the Save audience activity: Save audience (orchestrated/activities/save-audience.md)
* For the Audience Portal where audience shells are created: Audience Portal (audience/about-audiences.md)
* For consent management during publication: Learn more about consent management (action/consent.md)
* For querying the delivery events dataset: `ajo_message_feedback_event` (data/datasets-query-examples.md)
* For Orchestrated campaigns reporting: Learn more on Orchestrated campaigns reporting (orchestrated/reporting-campaigns.md)
* For accessing and subscribing to system alerts: Access and subscribe to system alerts (reports/alerts.md)
* For configuring the Alert activity: Learn how to configure the Alert activity (orchestrated/activities/alert.md)
* For a list of error codes: Orchestrated campaign errors (orchestrated/orchestrated-campaign-errors.md)
* For disabling sending confirmation before publishing: Confirm message sending (orchestrated/activities/channels.md)
* For common questions from practitioners: Orchestrated campaigns FAQ (orchestrated/orchestrated-campaigns-faq.md)
* For duplicating a recurring campaign that can no longer be reverted to draft: duplicate the campaign (campaigns/manage-campaigns.md)

**Personas:**

* **marketer:** Can test an Orchestrated campaign in Draft status by selecting Start, then control the test using Stop, Start, Restart, or Resume. Can publish the campaign by selecting Publish to move it from Draft to Live status. Can monitor execution through the visual flow, activity status indicators, and the Logs and tasks screen. The page states that the Publish button is disabled until all errors are fixed. Where: "Publish the campaign".

**Onboarding:**

* **Level:** Intermediate
* **First minimal step:** Open the campaign and select Start to test it in Draft status.
* **Success check:** Each activity in the campaign is executed sequentially until the end of the canvas is reached or until the workflow reaches a channel activity, where it stops so that you can run a test of that activity.
* **Previous:** Create and schedule the Orchestrated campaign before testing and publishing it: Create and schedule Orchestrated campaigns with Journey Optimizer (orchestrated/create-orchestrated-campaign.md)
* **Next:** Get insights on audience behavior and measure step performance after starting the campaign: Reporting for Orchestrated campaigns with Adobe Journey Optimizer (orchestrated/reporting-campaigns.md); Find answers to common questions about Orchestrated campaigns: Orchestrated campaigns Frequently Asked Questions (orchestrated/orchestrated-campaigns-faq.md)

+++

<!-- ai-section-version: 1 | source-hash: 3d09748a -->
