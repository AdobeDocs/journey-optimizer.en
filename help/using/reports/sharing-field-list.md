---
solution: Journey Optimizer
product: journey optimizer
title: Step event field list
description: Step event field list
feature: Journeys, Reporting
topic: Content Management
role: Data Engineer, Data Architect, Admin
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

This field group is specific to journeyStepEvent: this event is in relation with journey, and doesn’t have the identityMap, describing the profile identity, if any.

For journeyStepEvent, we need also to add fields related to the identity:

|Field name|Type|Description|
|---|---|------------|
|ID|String|Profile identifier identifies the profile sent/used in a journey. E.g: foo@adobe.com.|
|namespace|String|This field describes the Namespace referenced by the Profile used in the Journey. E.g: Email, ECID|

## serviceEvents {#servicevents-field}

This mixin contains all fields corresponding to a profile export job. 

|Field name|Type|Description|
|---|---|------------|
|ID|String|The identifier of the audience export job triggered|
|status|String|The status of audience export job: queued, started, finished|
|exportCountTotal|Integer|The max possible value of audience export job|
|exportCountRealized|Integer|The actual number of audiences exported through the job|
|exportCountFailed|Integer|The number of audiences failed while exporting through the job|
|exportSegmentID|String|The identifier of the audience being exported|
|eventType|String|The event type indicating whether it is an error event of info event: Info, Error|
|eventCode|String|The error code indicating the reason for corresponding eventType|

## stepEvents {#stepevents-field}

This category contains the original step event fields. Refer to this [section](../reports/sharing-legacy-fields.md).
