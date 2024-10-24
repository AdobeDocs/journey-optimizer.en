---
solution: Journey Optimizer
product: journey optimizer
title: Journey ending
description: Learn how a journey ends in Journey Optimizer
feature: Journeys
role: User
level: Intermediate
keywords: reenter, journey, end, live, stop
exl-id: ea1ecbb0-12b5-44e8-8e11-6d3b8bff06aa
---
# End a journey{#journey-ending}

A journey can end for an individual in two specific contexts:

* The person arrives at the last activity of a path.
* The person arrives at a **Condition** activity (or a **Wait** activity with a condition) and does not match any of the conditions.

The person can then reenter the journey if reentrance is allowed. See [this page](../building-journeys/journey-properties.md#entrance)

To terminate a live journey, we recommend that you close it. The arrival of new customers in the journey will then be blocked. Customers who already entered in the journey are able to experience it to the end. See [this section](../building-journeys/journey.md#close-journey)

You can stop a journey only if an emergency occurred and all processing needs to be ended immediately on a journey. People who already entered a journey are all stopped in their progress. See [this section](../building-journeys/journey.md#stop-journey)

>[!NOTE]
>
>Note that you cannot resume a closed or stopped journey.

## Journey end tag{#end-tag}

While authoring a journey, an "end tag" is displayed at the end of each path. This node cannot be added by a user, cannot be removed and only its label can be changed. It marks the end of each path of the journey. If the journey has several paths, we recommend that you add a label to each end to make reports easier to read. See [this page](../reports/live-report.md).

![](assets/journey-end.png)

<!--

### End activity{#journey-end-activity}

The **[!UICONTROL End]** activity allows you to mark the end of each path of the journey. It is not mandatory but recommended for visual clarity. See [this page](../building-journeys/end-activity.md)

![](assets/journey54.png)

-->

## Close a journey{#close-journey}

A journey can close because of the following reasons:

* The journey is closed manually via the **[!UICONTROL Close to new entrances]** button. 
* A one-shot segment based journey that has finished executing, and reached the global timeout of 91 days.
* After the last occurrence of a recurring audience based journey.

Closing a journey manually ensures that customers who already entered the journey can finish their path but new users are not able to enter the journey. When a journey is closed (for any of the reasons above), it will have the status **[!UICONTROL Closed]**. The journey stops letting new individuals enter the journey. Persons already in the journey can finish the journey normally. After the default global timeout of 91 days, the journey will switch to the Finished status. See [this section](journey-properties.md#timeout).

After the 91-day [global timeout](journey-properties.md#timeout), a Read audience journey switches to the **Finished** status. This behavior is set for 91 days only (i.e. [journey global timeout value](journey-properties.md#global_timeout)) as all information about profiles who entered the journey is removed 91 days after they entered. Persons still in the journey automatically are impacted. They exit the journey after the 91-day timeout. 

See this [section](../building-journeys/journey-properties.md#global_timeout).

A closed journey version cannot be restarted or deleted. You can create a new version of it or duplicate it. Only finished journeys can be deleted.

To close a journey from the list of journeys, click the **[!UICONTROL Ellipsis]** button that is located to the right of the journey name and select **[!UICONTROL Close to new entrances]**.

![](assets/journey-finish-quick-action.png)

You can also:

1. In the **[!UICONTROL Journeys]** list, click on the journey you want to close.
1. On the top-right, click the down arrow.

    ![](assets/finish_drop_down_list.png)

1. Click **[!UICONTROL Close to new entrances]**, and confirm in the dialog box.

## Stop a journey{#stop-journey}

In case you need to stop the progress of all individuals in the journey, you can stop it. Stopping the journey will timeout all individuals in the journey. However, stopping a journey involves that people who already entered a journey are all stopped in their progress. The journey is basically switched off. If you want to put an end to a journey we recommend that you close it. 

A stopped journey version cannot be restarted.

When stopped, the journey status is set to **[!UICONTROL Stopped]**. 

You can stop a journey, for example, if a marketer realizes that the journey targets the wrong audience or a custom action supposed to deliver messages is not working correctly. To stop a journey from the list of journeys, click the **[!UICONTROL Ellipsis]** button that is located to the right of the journey name and select **[!UICONTROL Stop]**.

![](assets/journey-finish-quick-action.png)

You can also:

1. In the **[!UICONTROL Journeys]** list, click on the journey you want to stop.
1. On the top-right, click on the down arrow.

   ![](assets/finish_drop_down_list2.png)

1. Click **[!UICONTROL Stop]**, and confirm in the dialog box.
