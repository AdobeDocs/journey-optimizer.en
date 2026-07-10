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
version: Journey Orchestration
feature_v2: []
subfeature_v2: []
---
# Limitations {#journey-limitations}

>[!BEGINSHADEBOX]

**On this page:** Review the limitations and guardrails that apply to journeys, including actions, versions, custom actions, events, and data sources.

>[!ENDSHADEBOX]

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

* For system-generated events, streaming data used to initiate a customer journey must be configured within Journey Optimizer first to get a unique orchestration ID. This orchestration ID must be appended to the streaming payload coming into [!DNL Adobe Experience Platform]. This limitation does not apply to rule-based events.

## Reaction events limitations {#reaction-limitations}

* **[!UICONTROL Reaction]** activities must be placed immediately after a [channel action activity](../building-journeys/journey-action.md) in the journey canvas. Placing a **[!UICONTROL Wait]** activity or any other activity between the channel action and the **[!UICONTROL Reaction]** activity is not supported and may result in the Reaction not working as expected. Learn more in [this section](../building-journeys/reaction-events.md).

## Data sources limitations {#data-sources-limitations}

* External data sources can be leveraged within a customer journey to lookup external data in real-time. These sources must be usable via REST API, support JSON and be able to handle the volume of requests.

## Journeys starting at the same time as a profile creation {#journeys-limitation-profile-creation}

There is a delay associated to API based profile creation/update in [!DNL Adobe Experience Platform]. The Service Level Target (SLT) in terms of latency is < 1 min from ingestion to Unified Profile for 95th percentile of requests, at a volume of 20K Requests per second (RPS).

If a Journey is triggered simultaneously to a profile creation and immediately checks/retrieves information from Profile Service, it might not work properly.

You can choose from one of these two solutions:

* Add a wait activity after the first event, to give [!DNL Adobe Experience Platform] the time it needs to perform the ingestion to Profile Service.

* Set up a journey that does not immediately leverage the profile. For example, if the journey is designed to confirm an account creation, the experience event could contain information needed to send the first confirmation message (first name, last name, email address, etc). 

## Read audience limitations {#read-audiences-limitations}

* Streamed audiences are always up-to-date but batch audiences will not be calculated at retrieval time. They are only evaluated every day at the daily batch evaluation time.

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page lists the hard technical limitations that apply to journey actions, journey versions, custom actions, events, reaction events, data sources, and audience reading in Adobe Journey Optimizer.

**Intents:**

* Understand the sending and retry limits for journey actions
* Learn which journey version transitions are allowed or blocked
* Identify restrictions on custom action URL, method, and header configuration
* Understand data source requirements for external system integration
* Avoid timing issues when starting a journey at the same moment as profile creation

**Glossary:**

* **Reaction event**: A journey activity that listens for a profile's interaction with a channel action (e.g., email open or click); must be placed immediately after the channel action activity. *(product-specific)*
* **Rule-based event**: An event type where the trigger is defined by a logical condition rather than a system-generated orchestration ID. *(product-specific)*
* **SLT (Service Level Target)**: The latency benchmark for API-based profile creation/update in Adobe Experience Platform — less than 1 minute from ingestion to Unified Profile at the 95th percentile for 20K RPS.

**Guardrails:**

* No sending throttling is applied; three retries are automatically performed on error and cannot be adjusted
* Two actions cannot run in parallel; they must be added sequentially
* A journey starting with an event activity in v1 cannot start with a non-event activity in later versions
* A journey starting with an Audience Qualification in v1 must always start with Audience Qualification in all subsequent versions; the audience and namespace cannot be changed
* A journey starting with Read Audience cannot start with a different event in next versions
* Custom action URL does not support dynamic parameters; only POST and PUT call methods are supported
* Custom action query parameter and header names must not start with "." or "$"; IP addresses and internal Adobe addresses (.adobe.) are not allowed
* Reaction activities must be placed immediately after a channel action activity; inserting a Wait or other activity between them is not supported
* External data sources must be accessible via REST API, support JSON, and handle the request volume
* Batch audiences are only evaluated once per day at the daily batch evaluation time — they are not recalculated at retrieval time
* When a journey is triggered simultaneously with a profile creation, profile data may not yet be available due to Platform ingestion latency

**Terminology:**

* Canonical name: Journey limitations — Acronym: none — variants: journey guardrails, journey restrictions
* Do not confuse: "Reaction event limitation" ≠ "general action limitation" — The Reaction event must be placed directly after a channel action; the general action limitation covers retries, parallelism, and throttling

**FAQ:**

* **Q: How many times does Journey Optimizer retry a failed action?** — Three retries are performed automatically; the number of retries cannot be configured.
* **Q: Can I place a Wait activity between a channel action and a Reaction event?** — No; the Reaction event must be placed immediately after the channel action activity. Adding any activity in between is not supported and may cause the Reaction event to not work as expected.
* **Q: Can I change the first event type when creating a new journey version?** — No; the entry mechanism set in v1 must be preserved in all subsequent versions. A journey starting with an event must continue to start with an event, and a journey starting with Audience Qualification must always start with Audience Qualification.
* **Q: Why might my journey not work when triggered at the same time as a profile is created?** — Profile creation via API has a latency before data is available in Unified Profile (SLT < 1 minute at 95th percentile). Adding a Wait activity after the first event gives Platform time to complete ingestion.
* **Q: Are streaming audiences always current in journeys?** — Yes; streaming audiences are always up-to-date. Batch audiences, however, are only evaluated once per day at the daily batch evaluation time, not at the moment of retrieval.

+++
