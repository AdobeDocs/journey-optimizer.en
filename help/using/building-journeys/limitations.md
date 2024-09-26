---
solution: Journey Optimizer
product: journey optimizer
title: Journey limitations
description: Learn more about Journey limitations
feature: Journeys, Best Practices, Guardrails
topic: Content Management
role: User
level: Intermediate
keywords: journeys, limitation
exl-id: 5d59f21c-f76e-45a9-a839-55816e39758a
---
# Limitations {#journey-limitations}

Here are limitations related to the use of journeys.

## General actions limitations {#action-limitations}

* There is no sending throttling. 
* Three retries are systematically performed in case of an error. You cannot adjust the number of retries according to the error message received. 
* The built-in **Reaction** event allows you to react to out-of-the-box actions (see this [page](../building-journeys/reaction-events.md)). If you want to react to a message sent via a custom action, you need to configure a dedicated event. 
* You cannot place two actions in parallel, you must add them one after the other.

## Journey versions limitations {#journey-versions-limitations}

* A journey starting with an event activity in v1 cannot start with something else than an event in further versions. You cannot start a journey with an **Audience Qualification** event. 
* A journey starting with an **Audience Qualification** activity in v1 must always start with an **Audience Qualification** in further versions. 
* The audience and namespace chosen in **Audience Qualification** (first node) can not be changed in new versions.
* The reentrance rule must be the same in all journey versions.
* A journey starting with a **Read Audience** cannot start with another event in next versions.

## Custom actions limitations {#custom-actions-limitations}

* The custom action URL does not support dynamic parameters. 
* Only POST and PUT call methods are supported. 
* The name of the query parameter or header must not start with "." or "$". 
* IP addresses are not allowed. 
* Internal Adobe addresses (.adobe.) are not allowed.

## Events limitations {#events-limitations}

* For system-generated events, streaming data used to initiate a customer journey must be configured within Journey Optimizer first to get a unique orchestration ID. This orchestration ID must be appended to the streaming payload coming into Adobe Experience Platform. This limitation does not apply to rule-based events.

## Data sources limitations {#data-sources-limitations}

* External data sources can be leveraged within a customer journey to lookup external data in real-time. These sources must be usable via REST API, support JSON and be able to handle the volume of requests.

## Journeys starting at the same time as a profile creation {#journeys-limitation-profile-creation}

There is a delay associated to API based profile creation/update in Adobe Experience Platform. The Service Level Target (SLT) in terms of latency is < 1 min from ingestion to Unified Profile for 95th percentile of requests, at a volume of 20K Requests per second (RPS).

If a Journey is triggered simultaneously to a profile creation and immediately checks/retrieves information from Profile Service, it might not work properly.

You can choose from one of these two solutions:

* Add a wait activity after the first event, to give Adobe Experience Platform the time it needs to perform the ingestion to Profile Service.

* Set up a journey that does not immediately leverage the profile. For example, if the journey is designed to confirm an account creation, the experience event could contain information needed to send the first confirmation message (first name, last name, email address, etc). 

## Read audience limitations {#read-audiences-limitations}

* Streamed audiences are always up-to-date but batch audiences will not be calculated at retrieval time. They are only evaluated every day at the daily batch evaluation time.
