---
title: Monitor message execution
description: Learn monitoring guidelines
feature: Monitoring
topic: Content Management
role: User
level: Intermediate
exl-id: 950f8186-07f6-4cc1-936c-d0984fb0f988
---
# Message monitoring {#monitor-message-execution}

To make sure your messages are successfully executed, sent and delivered, [!DNL Journey Optimizer] offers capabilities to monitor the messages that are currently published and triggered. You can see how your messages are performing across journeys <!--and APIs--> in real-time from the **[!UICONTROL Executions]** list.

➡️ [Discover this feature in video](#video)

To access this list, from the **[!DNL Journey Optimizer]** home page, select **[!UICONTROL Messages]**, and click the **[!UICONTROL Executions]** tab.

This tab provides two views: **[!UICONTROL Live view]** and **[!UICONTROL Global view]**.

* The **[!UICONTROL Live view]** tab provides a **real-time overview of all the executed messages** triggered by one or more [journeys](../building-journeys/journey.md) **over the last 24 hours only**.

  ![](assets/message-execution-tab-live.png)

  This list auto-refreshes every sixty seconds. If no execution occurred in the last 24 hours for a specific message, all columns will display null values (0) for that message.

* The **[!UICONTROL Global view]** tab provides an **overview of all the executed messages** triggered by one or more [journeys](../building-journeys/journey.md) **since the message start date**.

  ![](assets/message-execution-tab-global.png)

  This list auto-refreshes every ninety minutes. The data are aggregated over time since each message start date.

If a message is published but not triggered yet by a journey, it it not listed in any of the tabs. Only the following elements are listed:
* Messages that have been triggered, but not yet started (pending).
* Messages that have been triggered and that are currently running (in progress).

>[!NOTE]
>
>If a message has been used in several journeys, one row per journey is displayed for each execution.

By default, the messages are displayed starting from the most recent execution date. Click the **[!UICONTROL Filters]** icon to search the messages according to the channel, the start date, and/or the end date. You can also choose to exclude test events from your **Executions list**.

![](assets/message-execution-tab-filters.png)

The <!--**[!UICONTROL Quick action]**-->second column enables to open the corresponding [message](../messages/create-message.md) and to access the [Live Report](../reports/live-report.md) if you are in the **[!UICONTROL Live view]**, or the [Global Report](../reports/global-report.md) if you are in the **[!UICONTROL Global view]**.

![](assets/message-execution-open-live-report.png)

For each message execution, a number of indicators are displayed:

* **[!UICONTROL Message label]**: Message title that you defined upon [creating the message](../messages/create-message.md). The execution ID, which is automatically generated, is displayed in parentheses.

  <!--**[!UICONTROL Execution ID]**: Automatically generated identifier.
  **[!UICONTROL Source]**: Name of the journey leveraging that message.-->

* **[!UICONTROL Journey - Version - Action]**: Name of the journey leveraging the message, version of the journey, and label of the action leveraging the message in the journey.

* **[!UICONTROL Status]**: Message execution status.

* **[!UICONTROL Start date]**: Date and time when the message has been executed from the journey.

* **[!UICONTROL Targeted]**: Number of targeted profiles for each message execution.

* **[!UICONTROL Excluded]**: Number of profiles that have been excluded from the initial target due to exclusion rules.

* **[!UICONTROL Sent]**: Number of messages that have been sent.

* **[!UICONTROL Delivered]**: Number of messages successfully delivered in the recipient's mailbox (email) or device (push) without generating a bounce or any other delivery error.

* **[!UICONTROL Bounces]**: Number of messages that cannot be delivered because of a delivery failure. [Learn more on bounces](suppression-list.md).

* **[!UICONTROL Opens]**: Number of messages that have been opened.

* **[!UICONTROL Clicks]**: Number of clicks on links in an email.

  >[!NOTE]
  >
  >Clicks do not exist for push notifications: when a user clicks a push notification, it opens the app, which can only be considered as an open.

* **[!UICONTROL Errors]**: Number of messages that cannot be sent because of a technical failure.

* **[!UICONTROL Spam complaints]**: Number of messages that were marked as spam by recipients. Learn more on complaints in the [Deliverability Best Practice Guide](https://experienceleague.adobe.com/docs/deliverability-learn/deliverability-best-practice-guide/metrics-for-deliverability/complaints.html#metrics-for-deliverability){target="_blank"}.

You can choose which columns to display in the table. To do so, click the **[!UICONTROL Customize table]** icon on top of the screen and select the columns you want to show.

![](assets/message-execution-customize-table.png)

In **Global view** only, you can choose if you want to display the data as numbers, percentages, or both. Click the **Data format** drop-down list to toggle between the three options.

![](assets/message-execution-data-format.png)

Clicking each hyperlink will open the corresponding message summary view. [Learn more on messages](../messages/create-message.md).

## How-to video {#video}

Learn more on live and global reports, how to access and analyze the Journey and the Message specific reports, and how to modify the report dashboards.

>[!VIDEO](https://video.tv.adobe.com/v/334108?quality=12)
