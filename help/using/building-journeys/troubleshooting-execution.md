---
solution: Journey Optimizer
product: journey optimizer
title: Troubleshoot your live journey execution
description: Learn how to troubleshoot errors in live journey execution
feature: Journeys, Monitoring
topic: Content Management
role: User
level: Intermediate
keywords: troubleshoot, troubleshooting, journey, check, errors
exl-id: fd670b00-4ebb-4a3b-892f-d4e6f158d29e
version: Journey Orchestration
---
# Troubleshoot your live journey execution {#troubleshooting-execution}

In this section, learn how to troubleshoot journey events, check if profiles entered your journey, how they navigate through it, and if messages are sent.

You can also troubleshoot errors before testing or publishing a journey. Learn how [on this page](troubleshooting.md).

If you are using inbound actions, learn how to troubleshoot them [on this page](troubleshooting-inbound.md).

## Check that events are properly sent {#checking-that-events-are-properly-sent}

The starting point of a journey is always an event. You can perform tests using tools such as Postman.

You can check if the API call you send through these tools is sent correctly or not. If you get an error back, it means that your call has an issue. Check the payload again, the header (and especially the organization ID) and the destination URL. You can ask your administrator what is the right URL to hit.

Events are not pushed directly from the source to journeys. Indeed, journeys rely on [!DNL Adobe Experience Platform]'s streaming ingestion APIs. As a result, in case of event related issues, you can refer to [[!DNL Adobe Experience Platform] documentation](https://experienceleague.adobe.com/docs/experience-platform/ingestion/streaming/troubleshooting.html){target="_blank"} for Streaming ingestion APIs troubleshooting.

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

* **Event condition and schema data types** - Ensure the data types used in your event condition (rule) match the event schema. Mismatched types (for example, string vs. integer) cause rule evaluation to fail and events to be dropped. See [Verify event identity](#verify-event-identity-and-rule-data-types).

* **Event discarded – qualification condition not met** - For rule-based events, if the **qualification condition** is not satisfied by the event payload (for example, a required field is empty or missing, or a condition such as `isNotEmpty` on a field fails), the event is **received but discarded** and the journey is not triggered. Logs and Splunk traces can show that the event was received but discarded because it did not meet the qualification condition, with discard codes such as `notSuitableInitialEvent`. This is expected behavior: if the qualification condition is not met, the event will be discarded and the journey will not be triggered for that profile. Verify your event payload contains the expected fields and values, and that the rule in the event configuration matches the data you send. If the event is triggered by a **custom action** from another journey, see [Handling discard events and idle-timeouts](../action/troubleshoot-custom-action.md#handling-discard-events-and-idle-timeouts) in custom action troubleshooting.

>
>**For Audience Qualification journeys with streaming audiences**: If you're using an Audience Qualification activity as the journey entry point, be aware that not all profiles qualifying for the audience will necessarily enter the journey due to timing factors, quick exits from the audience, or if profiles were already in the audience before publishing. Learn more about [streaming audience qualification timing considerations](audience-qualification-events.md#streaming-entry-caveats).

### Verify event identity {#verify-event-identity-and-rule-data-types}

When configuring an event-based journey, confirm that the payload's identity field matches the [namespace selected in the event](../event/about-creating.md#select-the-namespace). If the event includes fields for profile matching, verify the **letter case** and **data type** in the event condition exactly match the inbound data. For example, if the event schema defines `roStatus` as a string, the journey rule must also evaluate it as a string. Mismatched data types (for example, string vs. integer) cause rule evaluation to fail and valid events to be dropped. Similarly, if the event has a **qualification condition** (for example, a field must be non-empty), events that do not satisfy that condition are **discarded** and do not trigger the journey; logs may show discard codes such as `notSuitableInitialEvent`.

To validate your event condition in [!DNL Journey Optimizer], use the payload preview in the event configuration and ensure the types and values in the rule match the payload structure. Learn how to [preview the payload](../event/about-creating.md#preview-the-payload) and [configure rule-based events](../event/about-creating.md).

## Troubleshoot test mode transitions {#troubleshooting-test-transitions}

If test profiles fail to progress through your journey in test mode or the visual flow does not display green arrows indicating step progression, the issue may be related to transition validation. This section provides guidance on diagnosing and resolving common test mode issues.

### Test profiles not progressing

If test profiles enter the journey but do not advance past the initial step, check the following:

* **Journey start date** - The most common cause is when the journey's start date is set in the future. Test profiles are immediately discarded if the current time falls outside the journey's configured [start and end dates/time](journey-properties.md#dates) window. To resolve:
    * Verify the journey start date is not set in the future
    * Ensure the current time falls within the journey's active date window
    * If necessary, update the journey properties to adjust the start date

* **Test profile configuration** - Confirm that the profile is correctly flagged as a test profile in [!DNL Adobe Experience Platform]. See [how to create test profiles](../audience/creating-test-profiles.md) for more information.

* **Identity namespace** - Ensure the identity namespace used in the event configuration matches the namespace of your test profile.

### Null transition indicators

During technical troubleshooting, you may encounter an `isValidTransition` property set to null in the journey's technical details. This UI-only property does not impact backend processing or journey performance. However, a null value can indicate:

* **Journey misconfiguration** - The journey start date is set in the future, causing test events to be silently discarded
* **Corrupted transition** - In rare cases, journey nodes may need to be reconnected

If you encounter persistent transition issues:

1. Verify the journey start date is current
1. Deactivate and reactivate test mode
1. If the issue persists, consider duplicating the affected journey nodes and reconnecting them
1. For unresolved cases, [contact support](../start/user-interface.md#support-ticket-guidelines) with journey logs, the impacted profile IDs, and details about the null transition

>[!NOTE]
>
>Remember that events sent outside the journey's active date window are silently discarded with no error message. Always verify your journey timing configuration first when troubleshooting test profile progression.

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

## Understanding duplicate entries in Journey Step Events {#duplicate-step-events}

Use this section to understand why duplicate rows can appear in Journey Step Events.

### Why do I see multiple entries with the same journey instance, profile, node, and request IDs?

When querying Journey Step Events data, you may occasionally observe what appears to be duplicate log entries for the same journey execution. These entries share identical values for:

* `profileID` - The profile identity
* `instanceID` - The journey instance identifier  
* `nodeID` - The specific journey node
* `requestID` - The request identifier

However, these entries have **different `_id` values**, which is the key indicator that distinguishes this scenario from actual data duplication.

### What causes this behavior?

This occurs due to backend auto-scaling operations (also called "rebalancing") in [!DNL Adobe Journey Optimizer]'s microservices architecture. During periods of high load or system optimization:

1. A journey step event begins processing and is logged to the Journey Step Events dataset
2. An auto-scaling operation redistributes workload across service instances
3. The same event may be reprocessed by another service instance, creating a second log entry with a different `_id`

This is an expected system behavior and is **working as designed**.

### Is there any impact on journey execution or message delivery?

**No.** The impact is limited to logging only. [!DNL Adobe Journey Optimizer] has built-in deduplication mechanisms at the message execution layer that ensure:

* Only one message (email, SMS, push notification, etc.) is sent to each profile
* Actions are executed only once
* Journey execution proceeds correctly

You can verify this by querying the `ajo_message_feedback_event_dataset` or checking action execution logs - you'll see that only one message was actually sent, despite the duplicate journey step event entries.

### How can I identify these cases in my queries?

When analyzing Journey Step Events data:

1. **Check the `_id` field**: True system-level duplicates would have the same `_id`. Different `_id` values indicate separate log entries from the rebalancing scenario described above.

2. **Verify message delivery**: Cross-reference with message feedback data to confirm only one message was sent:

    ```sql
    SELECT
      timestamp,
      _experience.customerJourneyManagement.messageExecution.messageExecutionID,
      _experience.customerJourneyManagement.messageDeliveryfeedback.feedbackStatus
    FROM ajo_message_feedback_event_dataset
    WHERE
      _experience.customerJourneyManagement.messageExecution.journeyVersionID = '<journeyVersionID>'
      AND TO_JSON(identityMap) like '%<profileID>%'
    ORDER BY timestamp DESC;
    ```

3. **Group by unique identifiers**: When counting executions, use `_id` to get accurate counts:

    ```sql
    SELECT
      COUNT(DISTINCT _id) as unique_executions
    FROM journey_step_events
    WHERE
      _experience.journeyOrchestration.stepEvents.journeyVersionID = '<journeyVersionID>'
      AND _experience.journeyOrchestration.stepEvents.profileID = '<profileID>'
    ```

### What should I do if I observe this?

This is normal system behavior and **no action is required**. The duplicate logging does not indicate a problem with your journey configuration or message delivery. 

If you're building reports or analytics based on Journey Step Events:

* Use `_id` as the primary key for counting unique events
* Cross-reference with message feedback datasets when analyzing message delivery
* Be aware that timing analysis may show entries clustered within a few seconds of each other

For more information about querying Journey Step Events, see [Examples of queries](../reports/query-examples.md).

## Troubleshoot dashboard metric discrepancies {#dashboard-metrics}

If the metrics displayed in the **Overview** dashboard do not match the actual number of journeys in the **Browse** tab, verify the following:

* Ensure the journeys in question have had traffic in the last 24 hours, as journeys without recent activity are excluded from the dashboard.
* Check that you have the appropriate access permissions to view all journeys in your organization.
* Allow up to 30 minutes for metrics to refresh after making changes to your journeys.

If discrepancies persist, [contact Adobe Support](../start/user-interface.md#support-ticket-guidelines) with screenshots of both the Overview and Browse tabs for investigation.
