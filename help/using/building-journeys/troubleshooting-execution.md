---
solution: Journey Optimizer
product: journey optimizer
title: Troubleshoot your live journey execution
description: Learn how to troubleshoot errors in live journey execution
feature: Journeys
topic: Content Management
role: User
level: Intermediate
keywords: troubleshoot, troubleshooting, journey, check, errors
exl-id: fd670b00-4ebb-4a3b-892f-d4e6f158d29e
version: Journey Orchestration
---
# Troubleshoot your live journey execution {#troubleshooting-execution}

In this section, learn how to troubleshoot journey events, check if profiles entered your journey, how they navigate through it, and if messsages are sent.

You can also troubleshoot errors before testing or publishing a journey. Learn how [on this page](troubleshooting.md).

If you are using inbound actions, learn how to troubleshoot them [on this page](troubleshooting-inbound.md).

## Check that events are properly sent {#checking-that-events-are-properly-sent}

The starting point of a journey is always an event. You can perform tests using tools such as Postman.

You can check if the API call you send through these tools is sent correctly or not. If you get an error back, it means that your call has an issue. Check the payload again, the header (and especially the organization ID) and the destination URL. You can ask your administrator what is the right URL to hit.

Events are not pushed directly from the source to journeys. Indeed, journeys rely on Adobe Experience Platform's streaming ingestion APIs. As a result, in case of event related issues, you can refer to [Adobe Experience Platform documentation](https://experienceleague.adobe.com/docs/experience-platform/ingestion/streaming/troubleshooting.html){target="_blank"} for Streaming ingestion APIs troubleshooting.

If your journey fails to enable test mode with error `ERR_MODEL_RULES_16`, ensure the event used includes an [identity namespace](../audience/get-started-identity.md) when using a channel action.

The identity namespace is used to uniquely identify the test profiles. For example, if email is used to identify the test profiles, the identity namespace **Email** should be selected. If the unique identifier is the phone number, then the identity namespace **Phone** should be selected.

## Check if people enter the journey {#checking-if-people-enter-the-journey}

Journey reporting measures people's entrances in a journey in real-time.

If you are successfully sending the event but see no entrance in the journey, it means that something goes wrong between the event sending and the event reception in the journey.

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

If individuals flow the right way in the journey but do not receive messages they should receive, you can check if:

* [!DNL Journey Optimizer] has correctly taken into account the request to send the message. Business users can access the message supposed to be sent and check if the time of the latest execution corresponds to the execution time of your journey. They can also check the latest API calls/events received.
* [!DNL Journey Optimizer] has successfully sent the message. Check the journey reporting to make sure that there are no errors.

In case of a message sent via a custom action, the only thing that can be checked during journey test is the fact that the call of the custom action's system leads to an error or not. If the call to the external system associated with the custom action does not lead to an error but does not lead to a message sending, some investigations should be done on the external system's side.
