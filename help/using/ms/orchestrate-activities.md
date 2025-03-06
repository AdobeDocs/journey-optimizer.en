---
solution: Journey Optimizer
product: journey optimizer
title: Create multi-step campaigns with Adobe Journey Optimizer
description: Learn how to build multi-step campaigns with Adobe Journey Optimizer
hide: yes
hidefromtoc: yes
---
# Orchestrate multi-step campaign activities {#orchestrate}

Once that you have [created a multi-step campaign](gs-campaign-creation.md), wether from the multi-step campaign menu or within a campaign, you can start orchestrating the differents tasks it will perform. To do this, a visual canvas is provided, allowing you to construct a multi-step campaign diagram. Within this diagram, you can add various activities and connect them in a sequential order.

## Add activities {#add}

At this stage of the configuration, the diagram is displayed with a start icon, representing the beginning of your multi-step campaign. To add your first activity, click the **+** button connected to the start icon.

A list of activities that can be added to the diagram appears. The available activities depend on your position within the multi-step campaign diagram. For example, when adding your first activity, you can start your multi-step campaign by targeting an audience, splitting the multi-step campaign path, or setting a **Wait** activity to delay the multi-step campaign execution. On the other hand, after a **Build audience** activity, you can refine your target with targeting activities, send a delivery to your audience with channel activities, or organize the multi-step campaign process with flow control activities.

![](assets/workflow-start.png){zoomable="yes"}

Once an activity has been added to the diagram, a right pane appears, allowing you to configure the newly added activity with specific settings. Detailed information on how to configure each activity is available in [this section](activities/about-activities.md).

![](assets/workflow-configure-activities.png){zoomable="yes"}

Repeat this process to add as many activities as desired depending on the tasks that you want your multi-step campaign to perform. Note that you can also insert a new activity between two activities. To do this, click the **+** button on the transition between the activities, select the desired activity and configure it in the right pane.

To remove an activity, select it in the canvas and click the **Delete** icon in the activity properties.

>[!TIP]
>
>You have the option to personalize the name of the transitions between each activity. To do this, select the transition and change its label in the right pane.

## The toolbar {#toolbar}

The toolbar located in the upper-right corner of the canvas provides options to easily manipulate the activities and navigate in the canvas:

* **Multiple selection mode**: Select multiple activities to delete them all at once or copy and paste them. See [this section](#copy).
* **Rotate**: Switch the canvas vertically.
* **Fit to screen**: Adapt the canvas zoom level to your screen.
* **Zoom out** / **Zoom in**: Zoom out or in the canvas.
* **Display map**: Opens a snapshot of the canvas showing you are located.

![](assets/workflow-toolbar.png){zoomable="yes"}{width="50%"}

## Manage activities {#manage}

When adding activities, action buttons are available in the properties pane, allowing you to perform multiple operations.

![](assets/activity-action.png){zoomable="yes"}

You can:

* **Delete** the activity from the canvas.
* **Disable/Enable** the activity. When the multi-step campaign is executed, disabled activities and the following activities on the same path are not executed and the multi-step campaign is stopped.
* **Pause/Resume** the activity. When the multi-step campaign is executed, it pauses at the paused activity. The corresponding task as well as all those that follow it in the same path are not executed.
* **Copy** the activity. See [this section](#copy).
* **Move** an activity and all its child nodes to another transition. See [this section](#move)
* Access the activity's **Execution options**.
* Access the activity's **Logs and tasks**.

Several **Targeting** activities, such as **Combine** or **Deduplication**, allow you to process the remaining population and include it into an additional outbound transition. For example, if you're using a **Split** activity, the complement consists of the population that did not match any of the previously defined subsets. To use this capability, activate the **Generate complement** option. 

![](assets/workflow-split-complement.png)

## Move or copy activities {#move-copy}

### Copy-paste activities {#copy}

You can copy multi-step campaign activities and paste them in any worflow. The destination multi-step campaign can be in a different browser tab. 

To copy activities, you have two choices:

* copy one activity using the action button.

    ![](assets/workflow-copy.png){zoomable="yes"}{width="70%"}

* copy multiple activities using the toolbar button.

    ![](assets/workflow-copy-2.png){zoomable="yes"}{width="70%"}

To paste the copied activities, click the **+** button on a transition and select "Paste X activity". 

![](assets/workflow-copy-3.png){zoomable="yes"}{width="50%"}

### Move activities and their child nodes {#move}

Journey Optimizer allows you to move an activity, along with the entire content of its child nodes (including all transitions and activities within it) to the end of another transition within the same multi-step campaign.

This process disconnects the activity and everything in its outbound transition from the initial location, moving it to the new target transition.

To move an activity:

1. Select the activity you wish to move.
1. In the activity's properties pane, click the **Move** button.
1. Select the transition where you want to place the activity and its outbound transition, then confirm.

![](assets/activity-move.png)

## Execution options {#execution}

All activities allow you to manage their execution options. Select an activity and click on the **Execution options** button. This lets you define the activity's execution mode and behavior in case of errors.

![](assets/workflow-execution-options.png){zoomable="yes"}{width="70%"}

### Properties

The **Execution** field allows you to define the action to be carried out when the task is started.

The **Maximum execution duration** field allows you to specify a duration such as "30s" or "1h". If the activity is not finished after the duration specified has been elapsed, an alert is triggered. This has no impact on how the multi-step campaign functions.

The **Time zone** field allows you to select the time zone of the activity. Adobe Journey Optimizer allows you to manage the time differences between multiple countries on the same instance. The setting applied is configured when the instance is created.

**The Affinity** field allows you to force a multi-step campaign or a multi-step campaign activity to execute on a particular machine. To do this, you must specify one or several affinities for the multi-step campaign or activity in question.

The **Behavior** field allows you to define the procedure to follow if asynchronous tasks are used.

### Error management

The **In case of error** field allows you to specify the action to be carried out should the activity encounter an error.

### Initialization script

The **Initialization script** lets you initialize variables or modify activity properties. Click the **Edit code** button and type the snippet of code to execute. The script is called when the activity executes. 

## Example {#example}

Here is a multi-step campaign example designed to send an email to all customers (other than VIP customers) with an email who are interested in coffee machines.

![](assets/workflow-example.png){zoomable="yes"}{zoomable="yes"}

To achieve this, activities below have been added:

* A **[!UICONTROL Fork]** activity that divides the multi-step campaign into three paths (one for each set of customer),
* **[!UICONTROL Build audience]** activities to target the three sets of customers:

    * Customers with an email,
    * Customers belonging to the pre-existing "Interrested in Coffee Machine(s)" audience,
    * Customers belonging to the pre-existing "VIP ro reward" audience.

* A **[!UICONTROL Combine]** activity that groups together customers with an email and those interested in coffee machines,
* A **[!UICONTROL Combine]** activity that excludes VIP customers,
* An **[!UICONTROL Email delivery]** activity that sends an email to the resulting customers. 

Once you have completed the multi-step campaign, add en **[!UICONTROL End]** activity at the end of the diagram. This activity allow you to visually mark the end of a workflow and has no functional impact.

After successfully designing the multi-step campaign diagram, you can execute the multi-step campaign and track the progress of its various tasks. [Learn how to start a multi-step campaign and monitor its execution](start-monitor-campaigns.md)
