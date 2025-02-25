---
solution: Journey Optimizer
product: journey optimizer
title: Journey Optimizer guardrails and limitations
description: Learn more about Journey Optimizer guardrails
feature: Journeys
topic: Content Management
role: User
level: Intermediate
exl-id: 5d59f21c-f76e-45a9-a839-55816e39758a
---
# Guardrails and limitations {#limitations}

You will find below additional guardrails and limitations when using [!DNL Adobe Journey Optimizer]. 

Entitlements, product limitations and performance guardrails are listed in [Adobe Journey Optimizer product description page](https://helpx.adobe.com/legal/product-descriptions/adobe-journey-optimizer.html){target="_blank"}. 

You also need to be aware of [Guardrails for Real-time Customer Profile data](https://experienceleague.adobe.com/docs/experience-platform/profile/guardrails.html){target="_blank"} before starting.


>[!NOTE]
>
>In rare circumstances, temporary outages in a specific region can result in valid profiles being excluded from journeys, or mails wrongly marked as bounces. Once services are restored, re-check journey logs, verify consent profile fields, and re-publish the journey if needed. In the case of an ISP outage, learn how to remove profiles from the suppression list in [this section](../configuration/manage-suppression-list.md#remove-from-suppression-list).
>

## Supported browsers {#browsers}

Adobe [!DNL Journey Optimizer] interface is designed to work optimally in the latest version of Google Chrome. You might have trouble using certain features on older versions or other browsers.

## Message guardrails {#message-guardrails}

* You cannot add attachments to an email with [!DNL Journey Optimizer].
* You cannot use the same sending domain to send out messages from [!DNL Adobe Journey Optimizer] and from another product, such as [!DNL Adobe Campaign] or [!DNL Adobe Marketo Engage] for example.

## Datasets guardrails {#datasets-guardrails}

As of February 2025, a time-to-live (TTL) guardrail is rolled out to Journey Optimizer system-generated datasets in **new sandboxes and new organizations** as follows:

* 90 days for data in the profile store,
* 13 months for data in the data lake.

This change will be rolled out to **existing customer sandboxes** in a subsequent phase. [Learn more on datasets Time-To-Leave (TTL) guardrails](../data/datasets-ttl.md)

## Landing pages guardrails {#lp-guardrails}

* Only one **Form** component can be used in a single primary page.
* The **Form** component cannot be used in subpages.
* You cannot add a preheader to a landing page.
* You cannot select the **Code your own** option when designing a landing primary page.

## SMS guardrails {#sms-guardrails}

* Media files for MMS can be included through a supported URL. Please ensure that the media file is uploaded separately.
* Message feedback syncing is not currently available for MMS.
* Consent management operates at the SMS channel level for MMS.

### Web channel guardrails {#web-guardrails}

[!DNL Journey Optimizer] web campaigns target new profiles that have not been engaged before on other channels. This will increase your total engageable profile count, which may have cost implications if the contractual number of engageable profiles you purchased is exceeded. Licence metrics for each package are listed on the [Journey Optimizer Product Description](https://helpx.adobe.com/legal/product-descriptions/adobe-journey-optimizer.html){target="_blank"} page.

### Code-based channel guardrails {#code-based-guardrails}

To use code-based experience actions in [!DNL Journey Optimizer] and deliver code content payload that can be used by your applications, follow the prerequisites detailed in [this page](../code-based/code-based-prerequisites.md).

## Subdomains guardrails {#subdomain-guardrails}

By default, [!DNL Journey Optimizer] allows you to delegate up to 10 subdomains in total (covering both email and web channels).

However, depending on your license contract, you may be able to delegate up to 100 subdomains. Reach out to your Adobe contact to learn more about the number of subdomains you are entitled to.

## Fragments guardrails {#fragments-guardrails}

* Visual fragments are only available for the Email channel.
* Expression fragments are not available for the In-app channel.

## Audiences guardrails {#audience}

You can publish up to 10 audience compositions in a given sandbox. If you have reached this threshold, you need to delete a composition to free up space and publish a new one.

## Decisioning & Decision management guardrails {#decisioning}

Guardrails and limitations to keep in mind when working with Decisioning or Decision Management are detailed in these the Decisioning & Decision management sections:

* [Decisioning guardrails & limitations](../experience-decisioning/decisioning-guardrails.md)
* [Decision management guardrails & limitations](../offers/decision-management-guardrails.md)


## Journey guardrails {#journeys-guardrails}

### General journey guardrails {#journeys-guardrails-journeys}

* The number of activities in a journey is limited to 50. The number of activities is displayed on the upper left section of the journey canvas. This will help in readability, QA and troubleshooting. 
* As you publish journeys, we automatically scale and adjust to ensure maximum throughput and stability. As you near the milestone of 100 live journeys at one time, you will see a notification appear in the UI on this achievement. If you see this notification and have a need to extend your journeys beyond 100 live journeys at a time, please create a ticket for customer care and we will help you reach your goals. 
<!-- DOCAC-10977 * As you publish journeys, we automatically scale and adjust to ensure maximum throughput and stability. As you near the milestone of 500 live journeys at one time, you will see a notification appear in the UI on this achievement. If you see this notification and have a need to extend your journeys beyond 500 live journeys at a time, please create a ticket for customer care and we will help you reach your goals.-->
* When using an audience qualification in a journey, that audience qualification activity may take up to 10 minutes to be active and listen to profiles entering or exiting the audience.
* A journey instance for a profile has a maximum size of 1MB. All data gathered as part of the journey execution is stored in that journey instance. Therefore, data from an incoming event, profile information retrieved from Adobe Experience Platform, custom action responses, etc. are stored in that journey instance and impact the journey size. It is advised, when a journey starts with an event, to limit the maximum size of that event payload (eg: below 800 KB) to avoid reaching that limit after a few activities, in the journey execution. When that limit is reached, the profile is in error status and will be excluded from the journey.
* In addition to the timeout used in journey activities, there is also a global journey timeout which is not displayed in the interface and cannot be changed. This global timeout stops the progress of individuals in the journey 91 days after they enter. [Read more](../building-journeys/journey-properties.md#global_timeout)

### General actions {#general-actions-g}

* Three retries are systematically performed in case of an error. You cannot adjust the number of retries according to the error message received. Retries are performed for all HTTP errors except for HTTP 401, 403 and 404.
* The built-in **Reaction** event allows you to react to out-of-the-box actions. Learn more in [this page](../building-journeys/reaction-events.md). If you want to react to a message sent via a custom action, you must configure a dedicated event.
* You cannot place two actions in parallel, you must add them one after the other.
* A profile cannot be present multiple times in the same journey, at the same time. If reentrance is enabled, a profile can reenter a journey, but cannot do it until he fully exited that previous instance of the journey. [Read more](../building-journeys/end-journey.md)

### Journey versions {#journey-versions-g}

* A journey starting with an event activity in v1 cannot start with something else than an event in further versions. You cannot start a journey with a **Audience Qualification** event. 
* A journey starting with a **Audience Qualification** activity in v1 must always start with a **Audience Qualification** in further versions. 
* The audience and namespace chosen in **Audience Qualification** (first node) cannot be changed in new versions.
* The reentrance rule must be the same in all journey versions.
* A journey starting with a **Read Audience** cannot start with another event in next versions.
* You cannot create a new version of a read audience journey with incremental read. You must duplicate the journey.

### Custom actions {#custom-actions-g}

* A capping limit of 300,000 calls over one minute is defined for all custom actions, per host and per sandbox. Refer to [this page](../action/about-custom-action-configuration.md). This limit has been set based on customers usage, to protect external endpoints targeted by custom actions. You must consider this in your audience-based journeys by defining an appropriate reading rate (5,000 profiles/s when custom actions are used). If needed, you can override this setting by defining a greater capping or throttling limit through our Capping/Throttling APIs. See [this page](../configuration/external-systems.md).
* The custom action URL does not support dynamic parameters.
* POST, PUT and GET call methods are supported
* The name of the query parameter or header must not start with "." or "$"
* IP addresses are not allowed
* Internal Adobe addresses (`.adobe.*`) are not allowed in URLs and APIs.
* Built-in custom actions cannot be removed.
* Custom actions support JSON format only when using request or response payloads. See [this page](../action/about-custom-action-configuration.md#custom-actions-limitations).
* When choosing an endpoint to target using a custom action, be sure that:

    * This endpoint can support journey's throughput, using configurations from the [Throttling API](../configuration/throttling.md) or [Capping API](../configuration/capping.md) to limit it. Be cautious that a throttling configuration cannot go below 200 TPS. Any endpoint targeted must support at least 200 TPS.
    * This endpoint needs to have a response time as low as possible. Depending of your expected throughput, having a high response time could impact the actual throughput.

### Events {#events-g}

* Journey Optimizer supports a peak volume of 5,000 inbound journey events per second.
* Event-triggered journeys may take up to 5 minutes to process the first action in the journey.
* For system-generated events, streaming data used to initiate a customer journey must be configured within Journey Optimizer first to get a unique orchestration ID. This orchestration ID must be appended to the streaming payload coming into Adobe Experience Platform. This limitation does not apply to rule-based events.
* Business events cannot be used in conjunction with unitary events or audience qualification activities.
* Unitary journeys (starting with an event or an audience qualification) include a guardrail that prevents journeys from being erroneously triggered multiple times for the same event. Profile reentrance is temporally blocked by default for 5 minutes. For instance, if an event triggers a journey at 12:01 for a specific profile and another one arrives at 12:03 (whether it is the same event or a different one triggering the same journey) that journey will not start again for this profile.
* Journey Optimizer requires events to be streamed to Data Collection Core Service (DCCS) to be able to trigger a journey. Events ingested in batch or events from internal Journey Optimizer datasets (Message Feedback, Email Tracking, etc.) cannot be used to trigger a journey. For use cases where you cannot get streamed events, you must build an audience based on those events and use the **Read Audience** activity instead. Audience qualification can technically be used, bu is not recommended as it can cause downstream challenges based on the actions used.

### Data sources {#data-sources-g}

* External data sources can be leveraged within a customer journey to lookup external data in real time. These sources must be usable via REST API, support JSON and be able to handle the volume of requests.
* Internal Adobe addresses (`.adobe.*`) are not allowed in URLs and APIs.

>[!NOTE]
>
>As the responses are now supported, you should use custom actions instead of data sources for external data sources use-cases.

### Journeys and profile creation {#journeys-limitation-profile-creation}
 
There is a delay associated to API based profile creation/update in Adobe Experience Platform. The Service Level Target (SLT) in terms of latency is < 1 min from ingestion to Unified Profile for 95th percentile of requests, at a volume of 20K Requests per second (RPS).

If a journey is triggered simultaneously to a profile creation and immediately checks/retrieves information from Profile Service, it might not work properly.

You can choose from one of these two solutions:

* Add a wait activity after the first event, to give Adobe Experience Platform the time it needs to perform the ingestion to Profile Service.

* Set up a journey that does not immediately leverage the profile. For example, if the journey is designed to confirm an account creation, the experience event could contain information needed to send the first confirmation message (first name, last name, email address, etc.). 

### Update profile {#update-profile-g}

Specific guardrails apply to the **[!UICONTROL Update profile]** activity. They are listed in [this page](../building-journeys/update-profiles.md).

### Read audience {#read-segment-g}

The following guardrails apply to the **[!UICONTROL Read Audience]** activity:

* Streamed audiences are always up-to-date but batch audiences will not be calculated at retrieval time. They are only evaluated every day at the daily batch evaluation time.
* For journeys using a **Read Audience** activity, there is a maximum number of journeys that can start at the exact same time. Retries will be performed by the system but please avoid having more than five journeys (with **Read Audience**, scheduled or starting "as soon as possible") starting at the exact same time by spreading them over time, for example 5 to 10 minutes apart.
* The **Read Audience** activity cannot be used with Adobe Campaign activities.
* The **Read Audience** activity can only be used as a first activity in a journey, of after a business event activity.
* A journey can only have one **Read Audience** activity.
* See also recommendations about how to use the **Read Audience** activity in [this page](../building-journeys/read-audience.md).
* Retries are applied by default on audience-triggered journeys (starting with a **Read Audience** or a **Business Event**) while retrieving the export job. If an error occurs during the export job creation, retries will be made every 10mn, for 1 hour max. After that, we will consider it as a failure. Those types of journeys can therefore be executed up to 1 hour after the scheduled time.

### Audience qualification {#audience-qualif-g}

The following guardrail applies to the **[!UICONTROL Audience Qualification]** activity:

* The Audience qualification activity cannot be used with Adobe Campaign activities.

### Expression editor {#expression-editor}

* Experience event field groups can not be used in journeys starting with a Read audience, an Audience qualification or a business event activity. You must create a new audience and use an inaudience condition in the journey.

### In-app activity {#in-app-activity-limitations}

* This feature is currently not available for Healthcare customers.

* Personalization can only contain profile attributes.

* The In-app activity cannot be used with Adobe Campaign activities.

* In-app display is tied to the journey lifespan, meaning that when the journey ends for a profile, all In-app messages within that journey will cease to be displayed for that profile.  Consequently, it is not possible to stop an In-app message directly from a journey activity. Instead, you must end the entire journey to stop the In-app messages from being displayed to the profile.

* In test mode, the In-app display depends on the journey's lifespan. To prevent the journey from ending too early during testing, adjust the **[!UICONTROL Wait time]** value for your **[!UICONTROL Wait]** activities. 

* **[!UICONTROL Reaction]** activities can not be used to react to an In-app open or click.

* An activation delay may happen between the moment a user profile reaches an In-app activity in the canvas and the time they start seeing that In-app message.

* In-app message content size is limited to 2Mb. Including large images can hinder the publishing process.

### Jump activity {#jump-g}

Specific guardrails apply to the **[!UICONTROL Jump]** activity. They are listed in [this page](../building-journeys/jump.md#jump-limitations).

### Campaign activities {#ac-g}

The following guardrails apply to the **[!UICONTROL Campaign v7/v8]** and the **[!UICONTROL Campaign Standard]** activities:

* Adobe Campaign activities cannot be used with a Read audience, or an Audience qualification activity.
* These activities cannot be used with In-app activities.
