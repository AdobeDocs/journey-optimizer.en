---
solution: Journey Optimizer
product: journey optimizer
title: Start and monitor orchestrated campaigns with Adobe Journey Optimizer
description: Learn how to start and monitor orchestrated campaigns with Adobe Journey Optimizer.
hide: yes
hidefromtoc: yes
exl-id: 5fc2d1d6-75c3-4b45-bb2b-09982b9bd5ed
---
# Start and monitor your orchestrated campaigns {#start-monitor}

>[!CONTEXTUALHELP]
>id="ajo_campaign_publication"
>title="Publish orchestrated campaign"
>abstract="To start your campaign, you must publish it. Ensure all warnings are cleared before publication."

+++ Table of Contents

| Welcome to orchestrated campaigns | Launch your first orchestrated campaign | Query the database | Ochestrated campaigns activities|
|---|---|---|---|
|[Get started with orchestrated campaigns](gs-orchestrated-campaigns.md)<br/><br/>[Configuration steps](configuration-steps.md)<br/><br/>[Access and manage orchestrated campaigns](access-manage-orchestrated-campaigns.md)|[Key steps for orchestrated campaign creation](gs-campaign-creation.md)<br/><br/>[Create and schedule the campaign](create-orchestrated-campaign.md)<br/><br/>[Orchestrate activities](orchestrate-activities.md)<br/><br/><b>[Start and monitor the campaign](start-monitor-campaigns.md)</b><br/><br/>[Reporting](reporting-campaigns.md)|[Work with the rule builder](orchestrated-rule-builder.md)<br/><br/>[Build your first query](build-query.md)<br/><br/>[Edit expressions](edit-expressions.md)|[Get started with activities](activities/about-activities.md)<br/><br/>Activities:<br/>[And-join](activities/and-join.md) - [Build audience](activities/build-audience.md) - [Change dimension](activities/change-dimension.md) - [Channel activities](channels.md) - [Combine](activities/combine.md) - [Deduplication](activities/deduplication.md) - [Enrichment](activities/enrichment.md) - [Fork](activities/fork.md) - [Reconciliation](activities/reconciliation.md) - [Split](activities/split.md) - [Wait](activities/wait.md)|

{style="table-layout:fixed"}

+++

<br/>

Once that you have created your orchestrated and designed the tasks to perform in the canvas, you can publish it and monitor how it is being executed. 

You can also execute the campaign in test mode to check its execution and the result of the different activities.

## Test your campaign before publishing {#test}

Journey Optimizer allows you to test orchestrated campaigns before going live. In test mode, all activities in the canvas are executed except **[!UICONTROL Save audience]** activities and channel activities. There is no functional impact on your data or audience.

To test a campaign:

1. Open the orchestrated campaign.
2. Click **[!UICONTROL Start]**.

![](assets/campaign-start.png){zoomable="yes"}

Each activity in the campaign is executed sequentially until the end of the diagram is reached. During test execution, you can manage the campaign using the action bar in the canvas. From there, you can:

* **Stop** the execution at any time.
* **Start** the execution again.
* **Resume** the execution if it was previously paused due to an issue.

If an error or warning occurs during execution, you are notified via the **[!UICONTROL Alerts]** / **[!UICONTROL Warning]** icon in the canvas toolbar.  

![](assets/campaign-warning.png){zoomable="yes"}

You can also quickly identify failed activities using the [visual status indicators](#activities) displayed directly on each activity. For detailed troubleshooting, open the [campaign’s logs](#logs-tasks), which provide in-depth information about the error and its context.

## Publish the campaign {#publish}

Once your campaign is tested and ready, click **[!UICONTROL Publish]** to make it live.

![](assets/campaign-publish.png){zoomable="yes"}

The visual flow restarts, and real profiles begin flowing through the journey in real-time.

## Monitor campaign execution {#monitor}

### Visual flow monitoring {#flow}

While running (in test or live mode), the visual flow shows how profiles move through the journey in real time. The number of profiles transitioning between tasks is displayed.

![](assets/workflow-execution.png){zoomable="yes"}

Data transported from one activity to another through transitions is stored in a temporary work table. This data can be displayed for each transition. To inspect data passed between activities:

1. Select a transition.
1. In the properties pane, click **[!UICONTROL Preview schema]** to view the work table schema. Select **[!UICONTROL Preview results]** to see the transported data.

![](assets/transition.png){zoomable="yes"}

### Activity execution indicators {#activities}

Visual status indicators help you understand how each activity is performing:

|Visual indicator | Description | 
|-----|------------|
|![](assets/activity-status-pending.png){zoomable="yes"}{width="70%"}| The activity is currently being executed. |
|![](assets/activity-status-orange.png){zoomable="yes"}{width="70%"}| The activity requires your attention. This may involve confirming the sending of a delivery or taking a necessary action. |
|![](assets/activity-status-red.png){zoomable="yes"}{width="70%"}|The activity has encountered an error. To resolve the issue, open the  orchestrated campaign logs for more information.|
|![](assets/activity-status-green.png){zoomable="yes"}{width="70%"}|The activity has been succesfully executed. | 

### Logs and tasks {#logs-tasks}

>[!CONTEXTUALHELP]
>id="ajo_campaign_logs"
>title="Logs and tasks"
>abstract="The **Logs and tasks** screen provides an history of the orchestrated campaign execution, recording all user actions and encountered errors."

Monitoring logs and tasks is a key step to analyze your orchestrated campaigns and make sure they are running properly. Logs and tasks are accessible from the **[!UICONTROL Logs]** button which is available in both test and live mode in the canvas toolbar or in each activity's properties pane.

The **[!UICONTROL Logs and tasks]** screen provides a complete history of your campaign execution, recording all user actions and encountered errors.

![](assets/workflow-logs.png){zoomable="yes"}

Two types of information are available:

* The **[!UICONTROL Log]** tab contains the chronological history of all operations and errors.
* The **[!UICONTROL Tasks]** tab details the step-by-step execution sequence of activities.

In both tabs, you can choose the displayed columns and their order, apply filters, and use the search field to quickly find the desired information.
