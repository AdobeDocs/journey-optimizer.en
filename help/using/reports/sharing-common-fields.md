---
solution: Journey Optimizer
product: journey optimizer
title: journeysteps events common fields
description: journeysteps events common fields
feature: Journeys, Reporting
topic: Content Management
role: Developer, Admin
level: Experienced
exl-id: 42aec986-2352-456a-a725-7f1585ae01f8
TQID: https://experienceleague.adobe.com/MWcV6FkgtiFJd9Y7q8CvTXQsL68cD5JcvqjmoEyiYhI
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: a9f73820-6899-47c2-a597-3fec28ab756a
    internal-label: Reporting
  - id: b49ca41f-eb7a-4f4b-abeb-a97c06fd0c04
    internal-label: Track and monitor
subfeature_v2:
  - id: d145add9-d5b9-481b-aa8a-e15e6bb7f813
    internal-label: Performance monitoring
  - id: a7289281-9ae4-47b1-b8cf-4028b98af776
    internal-label: Deliverability
  - id: b5afe8bf-bda6-41b5-ba06-922638872d63
    internal-label: Metrics catalog
role_v2:
  - id: c66ffd68-0f65-42bb-aa23-b4020f12e0bd
    internal-label: Admin
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
topic_v2:
  - id: aa2f3246-cb95-4b30-8899-fdf7d73550cc
    internal-label: Reporting
  - id: c1579802-ddd4-4214-8a91-97b2066abe11
    internal-label: Troubleshooting
---
# journeysteps events common fields {#sharing-common-fields}

>[!BEGINSHADEBOX]

**On this page:** Reference the common journey step event fields that Journey Optimizer sends to Adobe Experience Platform for every step processed in a journey.

>[!ENDSHADEBOX]

This field group will be shared by the following events: **journeyStepEvent** and **journeyStepProfileEvent**.

These are the common XDM fields that [!DNL Journey Optimizer] sends to Adobe Experience Platform. Common fields will be sent for every step that is processed in a journey. More specific fields are used for custom actions and enrichments.

Some of those fields are only available in specific processing patterns (action execution, data fetch, etc.) in order to limit the size of events.


>[!NOTE]
>
>Learn more about journey properties attributes [in this section](../building-journeys/expression/journey-properties.md#journey-properties-fields).


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