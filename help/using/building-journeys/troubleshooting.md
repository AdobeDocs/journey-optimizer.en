---
solution: Journey Optimizer
product: journey optimizer
title: Journey troubleshooting
description: Learn how to troubleshoot errors in journeys
feature: Journeys
topic: Content Management
role: User
level: Intermediate
keywords: troubleshoot, troubleshooting, journey, check, errors
exl-id: 03fbc4f4-b0a8-46d5-91f9-620685b11493
---
# Troubleshoot your journey {#troubleshooting}

In this section, learn how to troubleshoot journeys before testing or publishing. All the checks listed below can be performed when the journey is in test mode or when the journey is live. The recommendation is to make all the checks below in test mode and then proceed to publication. Learn more about the test mode in [this page](../building-journeys/testing-the-journey.md).

As an administrator, you can also test your custom actions configurations by making real API calls directly from the user interface. Learn more in [this page](../action/troubleshoot-custom-action.md).
 
## Check for errors before testing {#checking-for-errors-before-testing}

Before testing and publishing your journey, verify that all the activities are properly configured. You cannot perform tests or publications if errors are still detected by the system.


### Errors in activities {#activity-errors}

Errors appear with a warning symbol displayed on the activities themselves on the canvas. Place your cursor on the exclamation mark to display the error message. If you click on the activity, you should see the line in error with a warning. For example:

* if a mandatory field is empty, an error will be displayed

    ![](assets/journey63.png)

* in the canvas, when two activities are disconnected, a warning is displayed

    ![](assets/canvas-disconnected.png)

### Errors in the journey {#canvas-errors}

Errors are also visible from the **[!UICONTROL Alerts]** button, above the canvas. This button lets you see errors detected by the system and which prevent test mode activation or journey publication. 

The system detects two kinds of issues: **errors** and **warnings**. Errors block publication and test activation. Warnings indicate potential issues that are not blocking test activation or publication. You will see a description of the issue and an issue log ID of the type ERR_XXX_XXX. This can help identify the issue.

 ![](assets/journey-error-and-warning.png)

<!--Most of the time, errors detected by the system are linked to errors visible on the activities but they can also relate to other issues. In all cases, check alerts and resolve the issue using to the error description. If you cannot identify the issue, use the **[!UICONTROL Copy details]** button to store the alerts, and send them to your administrator.-->

Errors and warnings that are global to the journey appear first in the list. Error and warnings related to specific activities are listed after, by activity order or appearance in the journey from left to right. At the bottom of the list of alerts, the **[!UICONTROL Copy details]** button lets you copy technical information about the journey which are useful to troubleshoot the issues.

### Add an alternative path {#canvas-add-path}

You can define a fallback action in case of an error for the following journey activities: **[!UICONTROL Condition]** and **[!UICONTROL Action]**.

When an error occurs in an action or a condition, the journey of an individual stops. The only way to make it continue is to solve the issue. To avoid interrupting the journey, you can also check the option **[!UICONTROL Add an alternative path in case of a timeout or an error]** in the activity's properties. Learn more in [this section](../building-journeys/using-the-journey-designer.md#paths).


## Check that events are properly sent {#checking-that-events-are-properly-sent}

The starting point of a journey is always an event. You can perform tests using tools such as Postman.

You can check if the API call you send through these tools is sent correctly or not. If you get an error back, it means that your call has an issue. Check the payload again, the header (and especially the organization ID) and the destination URL. You can ask your administrator what is the right URL to hit.

Events are not pushed directly from the source to journeys. Indeed, journeys rely on Adobe Experience Platform's streaming ingestion APIs. As a result, in case of event related issues, you can refer to [Adobe Experience Platform documentation](https://experienceleague.adobe.com/docs/experience-platform/ingestion/streaming/troubleshooting.html){target="_blank"} for Streaming ingestion APIs troubleshooting.

## Check if people enter the journey {#checking-if-people-enter-the-journey}

Journey reporting measures people's entrances in a journey in real-time.

If you're successfully sending the event but see no entrance in the journey, it means that something goes wrong between the event sending and the event reception in the journey.

You can start troubleshooting with the questions below:

* Are you sure the journey where you expect the incoming event is in test mode or live?
* Did you save your event before copying the payload from the payload preview?
* Does your event payload contain an event id?
* Did you hit the right URL?
* Did you follow the Streaming Ingestion APIs payload structure, using the payload structure preview in the event configuration pane? See [this page](../event/about-creating.md#preview-the-payload).
* Did you use the right key-value pairs in the header of your event?

    ```
    X-gw-ims-org-id - your organization's ID
    Content-type - application/json
    ```

## Check how people navigate through the journey {#checking-how-people-navigate-through-the-journey}

Journey reporting measures the progress of individuals inside a journey. It's easy to identify where and why a person got stopped.

Here are a few things to check:

* Is it due to a condition excluding the person? For example, the condition is "gender = male" and the person is a woman. This check can be performed by a business user if the condition is not too complex.
* Is it due to a call to a data source not responding? When the journey is in test, this information can be seen in test mode logs. When the journey is live, an administrator can test direct calls to the data source and check the answer received. An administrator can also duplicate the journey and test it.

## Check that messages are sent successfully {#checking-that-messages-are-sent-successfully}

If individuals flow the right way in the journey but don't receive messages they should receive, you can check if:

* [!DNL Journey Optimizer] has correctly taken into account the request to send the message. Business users can access the message supposed to be sent and check if the time of the latest execution corresponds to the execution time of your journey. They can also check the latest API calls/events received.
* [!DNL Journey Optimizer] has successfully sent the message. Check the journey reporting to make sure that there are no errors.

In case of a message sent via a custom action, the only thing that can be checked during journey test is the fact that the call of the custom action's system leads to an error or not. If the call to the external system associated with the custom action does not lead to an error but does not lead to a message sending, some investigations should be done on the external system's side.
