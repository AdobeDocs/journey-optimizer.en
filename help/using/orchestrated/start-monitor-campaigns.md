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
|[Get started with orchestrated campaigns](gs-orchestrated-campaigns.md)<br/><br/>[Configuration steps](configuration-steps.md)<br/><br/[Access and manage orchestrated campaigns](access-manage-orchestrated-campaigns.md)|[Key steps for orchestrated campaign creation](gs-campaign-creation.md)<br/><br/>[Create and schedule the campaign](create-orchestrated-campaign.md)<br/><br/>[Orchestrate activities](orchestrate-activities.md)<br/><br/>[Send messages with orchestrated campaigns](send-messages.md)<br/><br/><b>[Start and monitor the campaign](start-monitor-campaigns.md)</b><br/><br/>[Reporting](reporting-campaigns.md)|[Work with the rule builder](orchestrated-rule-builder.md)<br/><br/>[Build your first query](build-query.md)<br/><br/>[Edit expressions](edit-expressions.md)|[Get started with activities](activities/about-activities.md)<br/><br/>Activities:<br/>[And-join](activities/and-join.md) - [Build audience](activities/build-audience.md) - [Change dimension](activities/change-dimension.md) - [Combine](activities/combine.md) - [Deduplication](activities/deduplication.md) - [Enrichment](activities/enrichment.md) - [Fork](activities/fork.md) - [Reconciliation](activities/reconciliation.md) - [Split](activities/split.md) - [Wait](activities/wait.md)|

{style="table-layout:fixed"}

+++

<br/>

Once that you have created your orchestrated and designed the tasks to perform in the canvas, you can publish it and monitor how it is being executed. 

## Start an orchestrated campaign {#start}

To start an orchestrated campaign, navigate to the **[!UICONTROL Orchestration]** tab of the **[!UICONTROL Campaigns]** menu and select the campaign to start, then click the **[!UICONTROL Play]** button in the upper-right corner of the canvas.

Once the  orchestrated campaign is running, each activity in the canvas is executed in a sequential order, until the end of the  orchestrated campaign is reached.

You can track the progress of targeted profiles in real-time using a visual flow. This allows you to quickly identify the status of each activity and the number of profiles transitioning between them.

![](assets/workflow-execution.png){zoomable="yes"}

In  orchestrated campaigns, data transported from one activity to another through transitions is stored in a temporary work table. This data can be displayed for each transition. To do this, select a transition to open its properties in the right hand side of the screen.

* Click **[!UICONTROL Preview schema]** to display the schema of the work table.
* Click **[!UICONTROL Preview results]** to visualize the data transported in the selected transition.

![](assets/transition.png){zoomable="yes"}

## Monitor the campaign execution

### Monitor activity execution {#activities}

Visual indicators in the upper-right corner of each activity box allows you to check their execution:

|Visual indicator | Description | 
|-----|------------|
|![](assets/activity-status-pending.png){zoomable="yes"}{width="70%"}| The activity is currently being executed. |
|![](assets/activity-status-orange.png){zoomable="yes"}{width="70%"}| The activity requires your attention. This may involve confirming the sending of a delivery or taking a necessary action. |
|![](assets/activity-status-red.png){zoomable="yes"}{width="70%"}|The activity has encountered an error. To resolve the issue, open the  orchestrated campaign logs for more information.|
|![](assets/activity-status-green.png){zoomable="yes"}{width="70%"}|The activity has been succesfully executed. | 

### Monitor logs and tasks {#logs-tasks}

>[!CONTEXTUALHELP]
>id="ajo_campaign_logs"
>title="Logs and tasks"
>abstract="The **Logs and tasks** screen provides an history of the  orchestrated campaign execution, recording all user actions and encountered errors."

Monitoring logs and tasks is a key step to analyze your orchestrated campaigns and make sure they are running properly. They are accessible from the **[!UICONTROL Logs]** icon which is available in the action tool bar, and in each activity's properties pane.

The **[!UICONTROL Logs and tasks]** menu provides an history of the  orchestrated campaign execution, recording all user actions and encountered errors.

![](assets/workflow-logs.png){zoomable="yes"}

Two types of information are available:

* The **[!UICONTROL Log]** tab contains the execution history of all the  orchestrated campaign activities. It indexes the operations carried out and execution errors by chronological order.
* The **[!UICONTROL Tasks]** tab details the execution sequencing of the activities. 

In both tabs, you can choose the displayed columns and their order, apply filters, and use the search field to quickly find the desired information.

## Orchestrated campaign execution commands {#execution-commands}

The action bar in the upper-right corner provides commands that allow you to manage the  orchestrated campaign execution. You can:

* **[!UICONTROL Start]** / **[!UICONTROL Resume]** the execution of the   orchestrated campaign, which then takes on the In progress status. If the  orchestrated campaign was paused, it is resumed, otherwise it is started and the initial activities are then activated.

* **[!UICONTROL Pause]** the execution of the  orchestrated campaign, which then takes on the Paused status. No new activities will be activated until it is resumed, but operations in progress are not suspended.

* **[!UICONTROL Stop]** a  orchestrated campaign that is being executed, which will then take on the Finished status. The operations in progress are interrupted if possible. You cannot resume from the  orchestrated campaign from the same place that it was stopped.
