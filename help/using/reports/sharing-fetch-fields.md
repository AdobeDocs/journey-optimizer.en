---
solution: Journey Optimizer
product: journey optimizer
title: journeyStep events data fetch fields
description: journeyStep events data fetch fields
feature: Journeys, Reporting
topic: Content Management
role: Developer, Admin
level: Experienced
exl-id: 948fe843-47cf-4b20-976a-48069eb9cf5c
---
# journeyStep events data fetch fields {#sharing-fetch-fields}

This field group will be shared by the journeyStepEvent and journeyStepProfileEvent.

During a step processing, we can have N data fetch on field groups.

## fetchTotalTime {#fetchtotaltime-field}

Total amount of time spent in data fetch in millis during the step processing.

Type: long

## fetchTypeInError {#fetchtypeinerror-field}

Defines if the fetch in error is on Adobe Experience Platform or on a custom data source.

Type: string

Values:

* aep
* custom
  
## fetchError {#fetcherror-field}

Type of error that happens when the data fetch is processed.

Type: string

Values: 

* http
* capping
* timedout
* error
  
## fetchErrorCode {#fetcherrorcode-field}
  
Code for fetch error. Present if the error has a code, such as an HTTP one. For instance, if the actionExecError is http, the code 404 represents the HTTP 404 error.

Type: string

## fetchOriginError {#fetchoriginerror-field}
  
A timeout can occur, in two cases:

* at the first attempt the action is executed. In this case, the execution is not finished, so there is no underlying error
* on a retry: in this case, the actionExecOrigError/actionExecOrigErrorCode describes the error encountered on the attempt before the retry.

For instance, data is being fetched from Unified Profile Service and an HTTP 500 error is returned at the first attempt. The fetch is retried, but the duration of the 2 attempts exceeds the timeout. Then the action execution is tagged as timedout. The action part will look like:

```
    ...
    "fetchTypeInError": "aep",
    "fieldgroupIdInError": "MyProfileFieldgroup",
    "fetchError": "timedout",
    "fetchOrigError": "http",
    "fetchOrigErrorCode": "500"
```

Type: string

## fetchOriginErrorCode {#fetchoriginerrorcode-field}

The Error code provided by the system [!DNL Journey Optimizer] is querying. For example it can be a 404, 500, etc.

Type: string
  
## fetchCount {#fetchcount-field}

How many times the data is fetched, regardless of the type of source.

Type: long

## fetchPlatformTotalTime {#fetchplatformtotaltime-field}

The total amount of time taken to fetch the data from Adobe Experience Platform in millis. Remark: this amount of time is computed from the time the engine sends the enrichment event to the enrichment service and receives the response.

Type: long

## fetchPlatformCount {#fetchplatformcount-field}

How many times the data is fetched from Adobe Experience Platform.

Type: long

## fetchCustomTotalTime {#fetchcustomtotaltime-field}

Amount of time to fetch the custom data in millis. Remark: this amount of time is computed from the time the engine sends the enrichment event to the enrichment service and receives the response

Type: long

## fetchCustomCount {#fetchcustomcount-field}

How many times the custom data is fetched from external systems.

Type: long
