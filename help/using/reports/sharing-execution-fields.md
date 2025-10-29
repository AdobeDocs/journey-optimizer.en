---
solution: Journey Optimizer
product: journey optimizer
title: journeyStep events action execution fields
description: journeyStep events action execution fields
feature: Journeys, Reporting
topic: Content Management
role: Developer, Admin
level: Experienced
exl-id: 273cda84-0261-4c5b-b5f4-0202e8874d05
---
# journeyStep events action execution fields {#sharing-execution-fields}

This field group will be shared by the journeyStepEvent and journeyStepProfileEvent.

If the step has an action to be processed, those fields will be added to the event payload. 

## actionID {#actionid-field}

ID of the action that is being executed.

Type: string

## actionName {#actionname-field}

Name of the action. If no name has been set, the stepName will be taken.

Type: string

## actionType {#actionType-field}

Type of the action.

Type: string

## actionParameterized {#actionparameterized-field}

Indicates if the action is parameterized or not.

Type: boolean

## actionExecutionTime {#actionexecutiontime-field}

The amount of time (in milliseconds) taken to execute a current action.

Type: long

The `actionExecutionTime` field represents the total time (in milliseconds) taken to execute the action, including both the time the request spent waiting in the queue (if throttling is configured and the rate limit is reached) and the actual execution time (including network latency to the external endpoint). 

The `Timestamp` field indicates the end time of the action execution. To determine when the profile entered the custom action node, subtract `actionExecutionTime` from `Timestamp`.

For example if `Timestamp` is "2025-02-04 09:39:03 UTC" and `actionExecutionTime` is 1,813,227 ms (~31 minutes), the profile entered the node at approximately "2025-02-04 09:08:32 UTC".


## actionExecutionError {#actionexecutionerror-field}

Type of error that happens when the action is called.

Type: string

Values:

* http
* capping
* timeout
* error

## actionExecutionErrorCode {#actionexecutionerrorcode-field}

Code for action execution error. Present if the error has a code, such as an HTTP one. 

Type: string

## actionExecutionOriginError {#actionexecutionoriginerror-field}

A timeout can occur, in two cases:

* at the first attempt an action is executed. In this case, the execution is not finished, so there is no underlying error
* on a retry: in this case, the actionExecOrigError/actionExecOrigErrorCode describes the error encountered on the attempt before the retry.

For instance, an email is being sent and an HTTP 500 error is returned at the first attempt. The fetch is retried, but the duration of the 2 attempts exceeds the timeout. Then the action execution is tagged as timedout. The action part will look like:

```
    ...
    "actionId": "myActionId",
    "actionName": "My mail sending",
    "actionType": "acsRestAction",
    "actionParameterized": true,
    "actionExecError": "timedout",
    "actionExecOrigError": "http",
    "actionExecOrigErrorCode": "500"
```

Type: string

## actionExecutionOriginCode {#actionexecutionorigincode-field}

Error code of the actionExecOrigError.

Type: string

## actionOriginEndpoint {#actionoriginendpoint}

URI of the custom action endpoint used in the action.

Type: string

## actionOriginMethod {#actionoriginmethod}

This describes the method used in the HTTP request (GET or POST).

Type: string

## actionOriginIsMTLS {#actionoriginismtls}

This describes whether MTLS is enabled for the endpoint.

Type: boolean

## actionIsProxy {#actionisproxy}

This describes whether an HTTP proxy with defined IP address range is used for the call.

Type: boolean

## actionExecutionOriginStartTime {#actionexecutionoriginstarttime}

This describes the timestamp at which the HTTP request is initiated. In case of a retry, this is the timestamp at which the final retry attempt is initiated. The timestamp uses ISO8601 format in UTC time zone.

Note that this timestamp will typically be slightly after the profile enters the custom action node, or significantly after it enters the node in case of throttling.

Type: timestamp

## actionExecutionOriginTime {#actionexecutionorigintime}

This describes the response time of the HTTP call. In case of retry, this is the time taken by the final retry attempt. It measures the time from when the HTTP request is initiated to when the complete response is returned from the server. Note that this excludes any time spent waiting in the queue in case of throttling.

Type: long

## actionIsThrottled {#actionisthrottled}

This describes whether throttling is enabled for the endpoint.

Type: boolean

## actionWaitTime {#actionwaittime}

This describes when the configured rate limit is hit for a throttled endpoint, calls are queued and processed at the configured rate. This field reports the amount of time the call spent waiting in the queue before being executed. Only specified if actionIsThrottled == true.

Type: long

## actionBusinessType {#actionbusinesstype-field}

Indicates the type of action. 

Values:

* builtin
  * ACS Email
  * ACS SMS
  * ACS Push
* customer
  * Epsilon
  * ...

Type: string

## deliveryJobID {#deliveryjobid-field}

This describes the delivery Job Id for the batch Journey.

Type: string

## batchDeliveryID {#batchdeliveryid-field}

This describes the delivery Id for the batch Journey.

Type: string

## fromSegmentTrigger {#fromsegmenttrigger-field}

This describes if the Batch Journey is triggered from Audience Segment.

Type: boolean

## actionSchedulerCount {#actionschedulercount-field}

Count of scheduler notification requests sent to the scheduler service during the step processing.

Type: long
