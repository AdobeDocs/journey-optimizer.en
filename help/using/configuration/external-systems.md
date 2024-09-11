---
solution: Journey Optimizer
product: journey optimizer
title: Integrate Journey Optimizer with external systems
description: Learn the best practices when integrating Journey Optimizer with external systems
feature: Integrations
role: User
level: Beginner
keywords: external, API, optimizer, capping
exl-id: 27859689-dc61-4f7a-b942-431cdf244455
---
# Integrate with external systems {#external-systems}

This page presents the different guardrails provided by Journey Optimizer when integrating an external system, as well as best practices: how to optimize the protection of your external system using the capping API, how to configure journey timeout, and how retries work. 

Journey Optimizer allows you to configure connections to external systems via custom data sources and custom actions. This allows you, for example, to enrich your journeys with data coming from an external reservation system, or send messages using a third-party system such as Epsilon or Facebook.

When integrating an external system, you can encounter several issues, the system can be slow, can stop responding, or it might not be able to handle a large volume. Journey Optimizer offers several guardrails to protect your system from over-loading.

All external systems are different in terms of performance. You need to adapt the configuration to your use cases.

When Journey Optimizer executes a call to an external API, the technical guardrails are executed as follows:

1. Capping or throttling rules are applied: if the maximum rate is reached, remaining calls are discarded or queued.

2. Timeout and retry: if the capping or throttling rule is fulfilled, Journey Optimizer tries to perform the call until the end of the timeout duration is reached. 

## Capping & throttling APIs {#capping}

### About Capping & Throttling APIs

When configuring a datasource or an action, you establish a connection to a system to either retrieve additional information to use in your journeys or send messages or API calls.

Journeys APIs support up to 5000 event per second but some external systems or API may not have an equivalent throughput. To prevent overloading these systems, you can use the **Capping** and **Throttling** APIs to limit the number of events sent per second.

Every time an API call is performed by journeys, it passes through the API engine. If the limit set in the API is reached, the call is either rejected if you are using the Capping API, or queued for up to 6 hours and processed as soon as possible in the order they were received if you are using the Throttling API.

For example, let's say that you have defined a capping or throttling rule of 200 calls per second for your external system. Your system is called by a custom action in 10 different journeys. If one journey receives 300 calls per second, it will use the 200 slots available and discard or queue the 100 remaining slots. Since the maximum rate has exceeded, the other 9 journeys will not have any slot left. This granularity helps to protect the external system from over-loading and crashing. 

>[!IMPORTANT]
>
>**Capping rules** are configured at sandbox level, for a specific endpoint (the URL called) but global to all journeys of that sandbox. Capping is available on both data sources and custom actions.
>
>**Throttling rules** are configured on production sandboxes only, for a specific endpoint but global to all journeys across all sandboxes. You can have only one throttling configuration per organization. Throttling is only available on custom actions.
>
>The **maxCallsCount** value has to be greater than 1.

For more information on how to work with the APIs, refer to these sections:

* [Capping API](capping.md)
* [Throttling API](throttling.md)

A detailed description of the APIs is available in [Adobe Journey Optimizer APIs documentation](https://developer.adobe.com/journey-optimizer-apis/references/journeys/)

### Data sources & custom actions capacity {#capacity}

For **external data sources**, the maximum number of calls per second is limited to 15. If this limit is exceeded, any additional calls are either discarded or queued depending on the API in use. It is possible to increase this limit for private external data sources by contacting Adobe to include the endpoint in the allowlist, but this is not an option for public external data sources. * [Learn how to configure data sources](../datasource/about-data-sources.md).

>[!NOTE]
>
>If a datasource uses a custom authentication with a different endpoint than the one used for the datasource, you need to contact Adobe to also include that endpoint in the allowlist.

For **custom actions**, you need to evaluate the capacity of your external API. For example, if Journey Optimizer sends 1000 calls per second and your system can only support 200 calls per second, you need to define a capping or throtlling configuration so that your system does not saturate. [Learn how to configure actions](../action/action.md)

>[!NOTE]
>
>As the responses are now supported, you should use custom actions instead of data sources for external data sources use-cases. For more information on responses, see this [section](../action/action-response.md)

## Timeout and retries{#timeout}

If the capping or throttling rule is fulfilled, then the timeout rule is applied.

In each journey, you can define a timeout duration. This allows you to set a maximum duration when calling an external system. Timeout duration is configured in the properties of a journey. Refer to [this page](../building-journeys/journey-properties.md#timeout_and_error).

This timeout is global to all external calls (external API calls in custom actions and custom data sources). By default, it is set to 30 seconds. 

During the defined timeout duration, Journey Optimizer tries to call the external system. After the first call, a maximum of three retries can be performed until the end of timeout duration is reached. The number of retries cannot be changed. 

Each retry uses one slot. If you have a capping of 100 calls per second and each of your calls require two retries, the rate drops to 30 calls per second (each call uses 3 slots: the first call and two retries). 

The timeout duration value depends on the use case. If you want to send your message quickly, for example when the client enters the store, then you do not want to set up a long timeout. Also, the longer the timeout is, the more items will be placed in queue. This can greatly impact performance. If Journey Optimizer performs 1000 calls per seconds, keeping 5 or 15 seconds of data can quickly overwhelm the system.

Let's take an example for a timeout of 5 seconds.

* The first call lasts less than 5 seconds: the call is successful, no retry is performed.
* The first call lasts longer 5 seconds: the call is cancelled and there is no retry. It is counted as a timeout error in reporting. 
* The first call fails after 2 seconds (the external system returns an error): 3 seconds are left for retries, if capping slots are available.
    * If one of the three retries is successful before the end of the 5 seconds, the call is performed, and there is no error.
    * If the end of the timeout duration is reached during the retries, the call is cancelled and counted as a timeout error in reporting. 

## Frequently asked questions{#faq}

**How can I configure a capping or throttling rule? Is there a default rule?**

To create capping or throttling rules, please refer to [this section](../configuration/external-systems.md#capping). By default, there is no throttling rule but a capping limit of 300,000 calls over one minute defined for all custom actions, per host and per sandbox. This limit has been set based on customers usage, to protect external endpoints targeted by custom actions. You must consider this in your audience-based journeys by defining an appropriate reading rate (5000 profiles/s when custom actions are used). If needed, you can override this setting by defining a greater capping or throttling limit through our Capping/Throttling APIs.

**How many retries are performed? Can I change the number of retries or define a minimum wait period between retries?**

For a given call, a maximum of three retries can be performed after the first call, until the end of timeout duration is reached. The number of retries and the time between each retry cannot be changed. Refer to [this section](../configuration/external-systems.md#timeout). 

**Where can I configure the timeout? Is there a maximum value?**

In each journey, you can define a timeout duration. Timeout duration is configured in the properties of a journey. Timeout duration must be between 1 second and 30 seconds. Refer to [this section](../configuration/external-systems.md#timeout) and [this page](../building-journeys/journey-properties.md#timeout_and_error). 