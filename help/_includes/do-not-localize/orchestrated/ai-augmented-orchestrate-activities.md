---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to build an Orchestrated campaign by adding, configuring, connecting, and managing activities on the visual canvas, including the canvas toolbar, activity action buttons, copy-paste, and a canvas example.

**Intents:**

* Add activities to the Orchestrated campaign canvas and configure them in the right pane.
* Insert a new activity between two existing activities and customize transition labels.
* Use the canvas toolbar to select multiple activities (to delete or copy them), rotate the canvas, zoom in or out, or open a snapshot showing your current location in the canvas.
* Delete, disable/enable, pause/resume, or copy an activity using the action buttons in the properties pane.
* Copy-paste one or multiple activities within or across Orchestrated campaign canvases.
* Use a breaking point activity to pause campaign execution and preview transported data.

**Glossary:**

* **Orchestrated campaign canvas**: the visual canvas used to construct an Orchestrated campaign by adding and connecting activities *(product-specific)*
* **Fork**: an activity that divides the Orchestrated campaign into separate paths, as shown in the canvas example, which uses a Fork activity to create three paths *(product-specific)*
* **Combine**: a targeting activity that groups together or excludes populations from different paths *(product-specific)*
* **Generate complement**: an option on activities such as Combine or Deduplication that includes the remaining, unmatched population into an additional outbound transition *(product-specific)*
* **Breaking point**: any activity used in the canvas to make campaign execution run only until that activity, then pause, keeping segmentation engine temporary data available for preview *(product-specific)*
* **End activity**: an activity added at the end of a branch to mark completion on the canvas, which can also be configured to send a signal to another Orchestrated campaign set to Triggered by a signal, passing parameters in the payload *(product-specific)*

**Guardrails:**

* The available activities to add depend on your position within the Orchestrated campaign canvas: when adding the first activity, you can define an audience (Build audience, Read audience, or Load file), split the path, or set a Wait activity; after a Build audience activity, you can use targeting activities, channel activities to send a delivery, or flow control activities to organize the process.
* When an Orchestrated campaign is executed, disabled activities and the following activities on the same path are not executed and the Orchestrated campaign is stopped.
* When an Orchestrated campaign is executed, it pauses at a paused activity; that activity and all those that follow it in the same path are not executed.
* Several targeting activities, such as Combine or Deduplication, allow processing of the remaining population into an additional outbound transition when the Generate complement option is activated.
* When using a Split activity, the complement consists of the population that did not match any of the previously defined subsets.

**Terminology:**

* Canonical name: Orchestrated campaign canvas
* Canonical name: Activity
* Do not confuse: "Disable/Enable" (disabled activities and following activities on the same path are not executed, and the Orchestrated campaign is stopped) ≠ "Pause/Resume" (execution pauses at the paused activity; that activity and all following activities on the same path are not executed)

**FAQ:**

* **Q: What determines which activities I can add at a given point?** — The available activities depend on your position within the Orchestrated campaign canvas: for example, the first activity can define an audience, split the path, or set a Wait activity, while activities after a Build audience activity can refine the target, send a delivery, or organize the process.
* **Q: What happens when I disable an activity?** — The disabled activity and the following activities on the same path are not executed, and the Orchestrated campaign is stopped.
* **Q: What happens when I pause an activity?** — Execution pauses at the paused activity; that activity and all those that follow it in the same path are not executed.
* **Q: What can I do with a breaking point during execution?** — You can use any activity as a breaking point so the campaign runs only until that activity, then pauses; while paused, the segmentation engine keeps temporary data available for you to preview by selecting the inbound transition just before the paused activity.
* **Q: Can I copy activities to a different campaign?** — Yes, you can copy one or multiple activities and paste them in any Orchestrated campaign canvas, including one in a different browser tab.
* **Q: What does the Generate complement option do?** — It includes the remaining population that was not otherwise processed into an additional outbound transition, available on targeting activities such as Combine or Deduplication.

**Examples:**

* Canvas example: a Fork activity divides the Orchestrated campaign into three paths; Build audience activities target customers with an email, customers who made a purchase of at least 100$, and customers with less than 50 loyalty points; a Combine activity groups customers with an email and those with a purchase of at least 100$; a second Combine activity excludes customers with less than 50 loyalty points; an Email delivery activity then sends an email to the resulting customers.

**Related pages:**

* For detailed configuration of each activity type: Work with Orchestrated campaign activities (orchestrated/activities/about-activities.md)
* For sending a signal from an End activity to another Orchestrated campaign: Trigger an Orchestrated campaign using a signal (orchestrated/trigger-orchestrated-campaign.md)
* For adding personalization to channel activities after building the canvas: learn how to add personalization (orchestrated/add-personalization.md)
* For reviewing transported data at a breaking point during execution: Visual flow monitoring (orchestrated/start-monitor-campaigns.md)
* For starting and monitoring the Orchestrated campaign after the canvas is ready: Learn how to start an Orchestrated campaign and monitor its execution (orchestrated/start-monitor-campaigns.md)

**Personas:**

* **marketer:** Can add activities to the Orchestrated campaign canvas by selecting the + button, then configure each activity in the right pane. Can insert a new activity between two existing activities and customize transition labels. The page states that disabled activities and the following activities on the same path are not executed, and the campaign is stopped. Where: "Add activities".

**Onboarding:**

* **Level:** Intermediate
* **First minimal step:** Select the + button connected to the start icon to add your first activity.
* **Success check:** A right pane appears, allowing you to configure the activity with specific settings.
* **Previous:** After creating an Orchestrated campaign: Key steps to create an Orchestrated campaign (orchestrated/gs-campaign-creation.md)
* **Next:** After adding channel activities to the canvas: Add personalization in Orchestrated campaigns (orchestrated/add-personalization.md); When the canvas is ready: Start and monitor Orchestrated campaigns with Adobe Journey Optimizer (orchestrated/start-monitor-campaigns.md)

+++

<!-- ai-section-version: 1 | source-hash: 4233cab5 -->
