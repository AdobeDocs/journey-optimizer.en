---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to access, search, filter and organize campaigns, what each campaign status means, how to use the campaigns calendar, and how to modify, stop, archive, delete and duplicate campaigns.

**Intents:**

* Access the lists of Action, API-triggered and Orchestrated campaigns, and search, filter or organize them with folders
* Understand each campaign status and the next actions available
* Use the campaigns calendar, including external calendars
* Modify a recurring Action campaign by creating a new version, or stop it
* Edit a campaign message that is already published
* Archive, delete or duplicate a campaign

**Glossary:**

* **Campaigns menu**: Entry point to the campaigns lists, with tabs **Action** campaigns, **API-triggered** campaigns, **Orchestrated** campaigns, and **Folders**
* **Campaigns inventory**: The list of campaigns, where the More actions button gives access to the operations
* **Draft version**: New version of an activated campaign that has not been activated yet; it has its own version ID, and activating it replaces the live version *(product-specific)*
* **Live version**: The current activated version of the campaign, available while you work on the draft version
* **Modify campaign**: Button that creates a new version of a recurring Action campaign
* **Open draft version** / **Open live version**: Actions to open the draft version or the live version of a campaign
* **Bulk actions**: Operations applied at once to multiple selected campaigns, such as adding items to a package, moving them to a folder, editing tags, managing access, and deleting
* **External calendars**: Calendars of events added from CSV files, shown on both Journey and Campaign calendars

**Guardrails:**

* By default, the Action and API triggered lists show the campaigns with the **Draft**, **Scheduled**, and **Live** statuses. To display stopped, completed, and archived campaigns, you need to clear the filter.
* **Archive** is available for all campaigns except **Draft** campaigns. All archived campaigns are deleted on a rolling schedule 30 days after their last modified date.
* **Delete** is available for **Draft** campaigns only.
* Activating the draft version replaces the live version of the campaign.
* Stopping a campaign does not stop an ongoing sending, but it stops a scheduled sending or the next occurrences if sending is already ongoing.
* For Action and API-triggered campaigns, a published message cannot be updated directly. A new version can only be created from a published (**Live**) message; a message that is still a draft is edited directly. A published message cannot be set back to **Draft**; create a new version instead.
* For a campaign with a decision policy that includes a content experiment, treatment assignments, including test and control group membership, may be re-segmented between versions. Do not assume assignments or results are continuous across versions.
* The calendar shows live and scheduled campaigns for the selected week by default. Draft campaigns are not displayed. Campaigns are displayed as 1-hour timespans, but this does not reflect actual send or completion time. If no start time is specified, the closest manual activation time is used to position the campaign.
* Up to three external calendars can be added. Uploaded events appear for all users in your organization and display on both Journey and Campaign calendars. CSV format: event name, start date in mm/dd/yy format, end date in mm/dd/yy format.
* Assets and images are accessible in delivered content for up to 2 years (730 days) since their first publication in any fragment or inline message. Re-publishing is required after this expiry period to keep them accessible for another 2 years. A re-publication done within 730 days of the first publication does not extend the expiry.
* Folders for journeys and campaigns are in limited availability.

**Prerequisites and permissions:**

* Available campaign types depend on your license agreement and your permissions.

**Applicability:**

* **Subscribe to alerts**, **Add to package** and **Open draft version**: Action and API triggered campaigns only.
* **Back to draft**: Orchestrated campaigns only.
* **View all time report** / **View last 24 hours report**, **Edit tags**, **Duplicate**, **Delete** and **Archive**: all campaign types.
* Statuses: **Draft**, **Scheduled**, **Live**, **Stopped**, **Completed** and **Archived** apply to Action, API-triggered and Orchestrated campaigns. **In review** and **Failed** apply to Action and API-triggered campaigns. **Publishing** applies to Orchestrated campaigns only.

**Terminology:**

* Canonical name: Campaign status — variants: lifecycle status
* Canonical name: Action campaigns — variants: Action campaigns tab (Action tab)
* Do not confuse: **Stopped** (manually stopped, cannot reactivate) ≠ **Completed** (execution complete, auto-assigned 3 days after activation or at end date for recurring campaigns) ≠ **Archived** (auto-deleted after 30 days)
* Do not confuse: **Scheduled** (configured for a specific start date) ≠ **Live** (activated and running) ≠ **Draft** (being edited, not activated)
* Do not confuse: **In review** (submitted for approval) ≠ **Publishing** (being published, Orchestrated campaigns)

**FAQ:**

* **Q: What does each campaign status mean?** — **Draft**: being edited, not activated. **Scheduled**: configured for a specific start date. **Live**: activated and running. **In review**: submitted for approval. **Stopped**: manually stopped, cannot reactivate. **Completed**: execution complete, auto-assigned 3 days after activation or at the end date for recurring campaigns. **Failed**: execution failed. **Archived**: archived, auto-deleted after 30 days. **Publishing**: being published.
* **Q: How do I reuse a stopped campaign?** — A stopped campaign cannot be reactivated. Duplicate it with **Duplicate**, enter the name of the campaign and confirm.
* **Q: How do I modify a recurring Action campaign?** — Open the campaign and click **Modify campaign**. A new version is created; check the live version with **Open live version**. Activate the new version when your changes are ready.
* **Q: How do I stop a recurring campaign?** — Open it, then click the **Stop campaign** button.
* **Q: Why can I not delete my campaign?** — **Delete** is available for **Draft** campaigns only.
* **Q: Why can I not see my completed, stopped or archived campaigns?** — By default the list shows the **Draft**, **Scheduled**, and **Live** statuses. Clear the filter to display them. Archived campaigns can be retrieved using the dedicated filter in the list.
* **Q: Can I see a draft campaign in the calendar?** — No. Draft campaigns are not displayed in the calendar.

**Troubleshooting:**

* A warning icon appears alongside the campaign's status — an error occurred within the campaign. Alerts may occur in various situations, such as when the campaign message has not been published or if the chosen configuration is incorrect. Click the icon to display information regarding the alert.

**Related pages:**

* Choose a campaign type: Choose your campaign type (campaigns/get-started-with-campaigns.md#campaign-types)
* Create an Action campaign: Create Action campaign (campaigns/create-campaign.md)
* Create an API-triggered campaign: Create API-triggered campaign (campaigns/api-triggered-campaigns.md)
* Create an Orchestrated campaign: Create Orchestrated campaign (orchestrated/gs-orchestrated-campaigns.md)
* Folders: Learn how to work with folders (start/search-filter-categorize.md#organize-folders)
* Tags: Learn how to use tags (start/search-filter-categorize.md#add-tags)
* Bulk actions: Learn more about bulk actions (start/search-filter-categorize.md#bulk-actions)
* Campaign reports: Campaign reports (reports/campaign-global-report-cja.md)
* System alerts: Learn more about system alerts (reports/alerts.md#subscribe-alerts)
* Export a campaign to another sandbox: Learn how to export objects (configuration/copy-objects-to-sandbox.md)
* Back to draft for Orchestrated campaigns: Learn more about reverting campaigns (orchestrated/start-monitor-campaigns.md#back-to-draft)
* Approval: approval (test-approve/gs-approval.md)
* Activating the new version: Review and activate a campaign (campaigns/review-activate-campaign.md)
* Journey Optimizer release status: Journey Optimizer release cycle (rn/releases.md)
* Conflict management: Conflict management guide (conflict-prioritization/gs-conflict-prioritization.md)

+++

<!-- ai-section-version: 1 | source-hash: 25b537a1 -->
