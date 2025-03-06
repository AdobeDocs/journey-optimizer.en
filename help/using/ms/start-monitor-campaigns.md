---
solution: Journey Optimizer
product: journey optimizer
title: Start and monitor multi-step campaigns with Adobe Journey Optimizer
description: Learn how to start and monitor multi-step campaigns with Adobe Journey Optimizer
hide: yes
hidefromtoc: yes
---
# Start and monitor your multi-step campaigns {#start-monitor}

Once that you have created your workflow and designed the tasks to perform in the canvas, you can launch it and monitor how it is being executed. 

## Start a multi-step campaign {#start}

To start a multi-step campaign, navigate to the **[!UICONTROL Multi-step]** tab of the **[!UICONTROL Campaign]** menu and select the campaign to start, then click the **[!UICONTROL Start]** button in the upper-right corner of the canvas.

Once the  multi-step campaign is running, each activity in the canvas is executed in a sequential order, until the end of the  multi-step campaign is reached.

You can track the progress of targeted profiles in real-time using a visual flow. This allows you to quickly identify the status of each activity and the number of profiles transitioning between them.

![](assets/workflow-execution.png){zoomable="yes"}

## Multi-step campaign transitions {#transitions}

In  multi-step campaigns, data transported from one activity to another through transitions is stored in a temporary work table. This data can be displayed for each transition. To do this, select a transition to open its properties in the right hand side of the screen.

* Click **[!UICONTROL Preview schema]** to display the schema of the work table.
* Click **[!UICONTROL Preview results]** to visualize the data transported in the selected transition.

![](assets/transition.png){zoomable="yes"}

## Monitor activity execution {#activities}

Visual indicators in the upper-right corner of each activity box allows you to check their execution:

|Visual indicator | Description | 
|-----|------------|
|![](assets/activity-status-pending.png){zoomable="yes"}{width="70%"}| The activity is currently being executed. |
|![](assets/activity-status-orange.png){zoomable="yes"}{width="70%"}| The activity requires your attention. This may involve confirming the sending of a delivery or taking a necessary action. |
|![](assets/activity-status-red.png){zoomable="yes"}{width="70%"}|The activity has encountered an error. To resolve the issue, open the  multi-step campaign logs for more information.|
|![](assets/activity-status-green.png){zoomable="yes"}{width="70%"}|The activity has been succesfully executed. | 

## Monitor logs and tasks {#logs-tasks}

Monitoring workflows logs and tasks is a key step to analyze your  multi-step campaigns and make sure they are running properly. They are accessible from the **[!UICONTROL Logs]** icon which is available in the action tool bar, and in each activity's properties pane.

The **[!UICONTROL Logs and tasks]** menu provides an history of the  multi-step campaign execution, recording all user actions and encountered errors.
![](assets/workflow-logs.png){zoomable="yes"}

Two types of information are available:

* The **[!UICONTROL Log]** tab contains the execution history of all the  multi-step campaign activities. It indexes the operations carried out and execution errors by chronological order.
* The **[!UICONTROL Tasks]** tab details the execution sequencing of the activities. 

In both tabs, you can choose the displayed columns and their order, apply filters, and use the search field to quickly find the desired information.

## Multi-step campaign execution commands {#execution-commands}

The action bar in the upper-right corner provides commands that allow you to manage the  multi-step campaign execution. You can:

* **[!UICONTROL Start]** / **[!UICONTROL Resume]** the execution of the   multi-step campaign, which then takes on the In progress status. If the  multi-step campaign was paused, it is resumed, otherwise it is started and the initial activities are then activated.

* **[!UICONTROL Pause]** the execution of the  multi-step campaign, which then takes on the Paused status. No new activities will be activated until it is resumed, but operations in progress are not suspended.

* **[!UICONTROL Stop]** a  multi-step campaign that is being executed, which will then take on the Finished status. The operations in progress are interrupted if possible. You cannot resume from the  multi-step campaign from the same place that it was stopped.
