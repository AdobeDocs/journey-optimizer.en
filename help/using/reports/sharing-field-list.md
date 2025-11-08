---
solution: Journey Optimizer
product: journey optimizer
title: Step event field list
description: Step event field list
feature: Journeys, Reporting
topic: Content Management
role: Developer, Admin
level: Experienced
exl-id: e96efa67-ee47-40b9-b680-f5119d8c3481
---
# Step event field list {#sharing-field-list}

Step event fields are organized by category.

* Debug information fields
* Journey fields
* Profile fields
* Service event fields

For the identityMap attribute, the primary identity is defined by default as "primary = true".

## debugInfo {#debuginfo-field}

|Field name|Type|Description|
|---|---|------------|
|requestId|String|The request Id used by Journey Optimizer to track the flow of a request.|

## journey {#journey-field}

This field group is used in the journey schema (in relation with journeyStepEvent). It contains the following fields:

|Field name|Type|Description|
|---|---|------------|
|ID|String|Identifier for the given Journey|
|VersionID|String|Id of the journey version. This id represents the identity of a journey|
|name|String|Name of the journey|
|description|String|Description of the journey|
|version|String|version, represented as `major`.`minor`|

## profile {#profile-field}

This field group is specific to journeyStepEvent: this event is in relation with journey, and doesn't have the identityMap, describing the profile identity, if any.

For journeyStepEvent, we need also to add fields related to the identity:

|Field name|Type|Description|
|---|---|------------|
|ID|String|Profile identifier identifies the profile sent/used in a journey. E.g: foo@adobe.com.|
|namespace|String|This field describes the Namespace referenced by the Profile used in the Journey. E.g: Email, ECID|

## serviceEvents {#servicevents-field}

This mixin contains all fields corresponding to a profile export job. These events are generated per **Read Audience** activity to track the lifecycle of audience export operations (queued, started, finished, errors). Unlike regular step events, serviceEvents are not tied to individual profiles but to the Read Audience node itself, which means they may not have an associated profile identifier. 

|Field name|Type|Description|
|---|---|------------|
|ID|String|The identifier of the audience export job triggered|
|status|String|The status of audience export job: queued, started, finished|
|exportCountTotal|Integer|The max possible value of audience export job|
|exportCountRealized|Integer|The actual number of audiences exported through the job|
|exportCountFailed|Integer|The number of audiences failed while exporting through the job|
|exportSegmentID|String|The identifier of the audience being exported|
|eventType|String|The event type indicating whether it is an error event or info event: Info, Error|
|eventCode|String|The error code indicating the reason for corresponding eventType|

Learn more about eventTypes [in this section](#discarded-events).

## stepEvents {#stepevents-field}

This category contains the original step event fields. Refer to this [section](../reports/sharing-legacy-fields.md).


## Troubleshoot discarded event types in Journey step events  {#discarded-events}

When querying journey step events for records with `eventCode = 'discard'`, you may encounter several eventTypes. 

Below are definitions, common causes, and troubleshooting steps for the most frequent discard `eventTypes`:

* **EXTERNAL_KEY_COMPUTATION_ERROR**: The system could not compute a unique identifier (external key) for the customer from the event data.

    **Common causes**: Missing or malformed customer identifiers (e.g., email, customer ID) in the event payload.
    
    **Troubleshooting**: Check event configuration for required identifiers, ensure event data is complete and correctly formatted.

* **NO_INTERESTED_JOURNEYS_FOR_SEGMENTMEMBERSHIP_EVENT**: A segment qualification event was received, but no journeys are configured to respond to this segment.

    **Common causes**: No journeys use the segment as a trigger, journeys are in draft/stopped state, or segment IDs do not match.
    
    **Troubleshooting**: Ensure at least one journey is live and configured for the segment, verify segment IDs.

* **JOURNEY_INSTANCE_ID_NOT_CREATE**: The system failed to create a journey instance for the customer.

    **Common causes**: Duplicate events, high event volume, system resource constraints.
    
    **Troubleshooting**: Implement deduplication, avoid traffic spikes, optimize journey design, contact support if persistent.

* **EVENT_WITH_NO_JOURNEY**: An event was received but no active journey is configured to respond to it

    **Common causes**: Event name/ID mismatch, journey not published, wrong sandbox/organization, test mode/profile mismatch.
    
    **Troubleshooting**: Verify event and journey configuration, check journey status, use debugging tools.

* For discards happening in paused journeys:

    * **PAUSED_JOURNEY_VERSION**: Discards that occurred at the point of journey entrance
    * **JOURNEY_IN_PAUSED_STATE**: Discards which happened when profiles are in a journey

    Learn more about these events and how to troubleshoot them in the [Pause a Journey section](../building-journeys/journey-pause.md#discards-troubleshoot).

## Additional resources

* [Dataset query samples - Journey Step Event](../data/datasets-query-examples.md#journey-step-event).
* [Examples of queries - Event-based Queries](query-examples.md#event-based-queries).
* [Built-in schemas dictionary](https://experienceleague.adobe.com/tools/ajo-schemas/schema-dictionary.html)

