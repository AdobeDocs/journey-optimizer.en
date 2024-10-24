---
solution: Journey Optimizer
product: journey optimizer
title: journeysteps events common fields
description: journeysteps events common fields
feature: Journeys, Reporting
topic: Content Management
role: Data Engineer, Data Architect, Admin
level: Experienced
exl-id: 42aec986-2352-456a-a725-7f1585ae01f8
---
# journeysteps events common fields {#sharing-common-fields}

This field group will be shared by the following events: **journeyStepEvent** and **journeyStepProfileEvent**.

These are the common XDM fields that [!DNL Journey Optimizer] sends to Adobe Experience Platform. Common fields will be sent for every step that is processed in a journey. More specific fields are used for custom actions and enrichments.

Some of those fields are only available in specific processing patterns (action execution, data fetch, etc.) in order to limit the size of events.


>[!NOTE]
>
>Learn more about journey properties attributes [in this section](../building-journeys/expression/journey-properties.md#journey-propertoes-fields).


## entrance {#entrance-field}

Indicates if the user has entered the journey. If not present, we assume that the value is false.

Type: boolean

Values: true/false

## reentrance {#reentrance-field}

Indicates if the user has reentered the journey with the same instance. If not present, we assume that the value is false.

Type: boolean

Values: true/false

## instanceEnded {#instance-ended-field}

Indicates if the instance has ended (successfully or not).

Type: boolean

## eventID {#eventid-field}

Event id in processing, for the step processing. If the event is an external one, the value is its eventId. If the event is an internal one, the value is the internal eventId (such as scheduledNotificationReceived, executedAction, etc.).

Type: string

## nodeID {#nodeid-field}

Client node id (from the canvas). 

Type: string

## stepID {#stepdid-field}

Unique id of the step that is currently being processed.

Type: string

## stepName {#stepname-field}

Name of the step that is currently being processed.

Type: string

## stepType {#steptype-field}

Type of the step.

Type: string

Possible values:

* Condition
* Action
* Scheduler
* Timer

## stepStatus {#stepstatus-field}

Status of the step, representing the status of the step, when its processing has been done (and the step event fired).

Type: string

The status can be:

* ended: the step has no transition and its processing has ended successfully.
* error: the step processing has raised an error.
* transitions: the step is waiting for an event to transition to another step.
* capped: the step has failed on a capping error, raised during an action or enrichment.
* timedout: the step has failed on a timeout error, raised during an action or enrichment.
* instanceTimedout: the step has stopped its processing, because the instance has reached its timeout.

## journeyID {#journeyid-field}

ID of the journey.

Type: string

## journeyVersionID {#journeyversionid-field}

ID of the journey version. This id represents the identity reference to the journey, in the case of the journeyStepEvent.

Type: string

>[!NOTE]
>
>For troubleshooting purposes, we recommend using journeyVersionID instead of journeyVersionName when querying journeys.

## journeyVersionName {#journeyversionname-field}

Name of the journey version.

Type: string

>[!NOTE]
>
>For troubleshooting purposes, we recommend using journeyVersionID instead of journeyVersionName when querying journeys.

## journeyVersion {#journeyversion-field}

Version of the journey version.

Type: string

## instanceID {#instanceid-field}

Internal ID of the journey instance.

Type: string

## externalKey {#externalkey-field}

External key extracted from the event to process it.

Type: string

## parentStepID {#parenstepid-field}

Step ID of the parent of the current processed step in the instance.

Type: string

## parentStepName {#parentstepname-field}

Step name of the parent of the current step.

Type: string

## parentTransitionID {#parenttransitionid-field}

Id of the transition which has brought the instance to the processed step.

Type: string

## parentTransitionName {#parenttransitionname-field}

Name of the transition which has brought the instance to the processed step.

Type: string

## inTest {#intest-field}

Indicated if this journey is in test mode or not.

Type: boolean

## processingTime {#processingtime-field}

Total amount of time in milliseconds from the instance step entrance to the end of the processing.

Type: long

## instanceType {#instancetype-field}

Indicates the instance type, if it is batch or unitary.

Type: string

Values: batch/unitary

## recurrenceIndex {#recurrenceindex-field}

Index of the recurrence if the journey is batch and recurring (first run has recurrenceIndex = 1).

Type: long

## isBatchToUnitary {#isbatchtounitary-field}

Indicates if this unitary instance has been triggered from a batch instance.

Type: boolean

## batchExternalKey {#batchexternalkey-field}

External Key for batch event.

Type: string

## batchInstanceID {#batchinstanceid-field}

this is the batch instance ID.

Type: string

## batchUnitaryBranchID {#batchunitarybranchid-field}

if the instance has been triggered from a batch instance, unitary branch ID.

Type: string

## exitCriteriaID

ID of the exitCriteria

Type: string

## exitCriteriaName

Name of the exitCriteria

Type: string