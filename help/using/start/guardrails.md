---
solution: Journey Optimizer
product: journey optimizer
title: Journey Optimizer guardrails and limitations
description: Learn more about Journey Optimizer guardrails
feature: Guardrails
role: User
level: Intermediate
mini-toc-levels: 2
exl-id: 5d59f21c-f76e-45a9-a839-55816e39758a
TQID: https://experienceleague.adobe.com/k4DqGogrTZ9QrnqyFGwdgDeUI9ivpOd1iSI0c5comuU
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: d998adac-2f81-400b-a669-d07bb196e4eb
    internal-label: Journeys
  - id: ad78185d-8f79-40ad-9bad-cbde74af74ee
    internal-label: Guardrails and limitations
subfeature_v2:
  - id: a6c67b0d-bd3e-4d5d-95a8-882e3709d632
    internal-label: Journey guardrails
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
level_v2:
  - id: b5a62a22-46f7-4f0d-b151-3fc640bef588
    internal-label: Intermediate
topic_v2:
  - id: c1579802-ddd4-4214-8a91-97b2066abe11
    internal-label: Troubleshooting
  - id: d3cdead0-685a-4489-9250-4bb709942f66
    internal-label: Data collection
  - id: e0eb8757-182f-49f3-94a4-1587d16f5094
    internal-label: Personalization
---

# Guardrails and limitations {#limitations}

>[!BEGINSHADEBOX]

**On this page:** Review the system, journey, audience, channel, and content limits of Adobe Journey Optimizer so you can plan deployments that scale without hitting failures.

>[!ENDSHADEBOX]

Below you will find guardrails and limitations when using [!DNL Adobe Journey Optimizer].

Entitlements, product limitations and performance guardrails are listed in [Adobe Journey Optimizer product description page](https://helpx.adobe.com/legal/product-descriptions/adobe-journey-optimizer.html){target="_blank"}.

>[!CAUTION]
>
>* [Guardrails for Real-time Customer Profile data and segmentation](https://experienceleague.adobe.com/en/docs/experience-platform/profile/guardrails){target="_blank"} also apply to Adobe Journey Optimizer.
>
>* See also [Guardrails for Data Ingestion in Real-time Customer Profile](https://experienceleague.adobe.com/en/docs/experience-platform/ingestion/guardrails){target="_blank"}


## System & Platform {#system-platform}

### Supported browsers {#browsers}

Adobe [!DNL Journey Optimizer] interface is designed to work optimally in the latest version of Google Chrome. You might have trouble using certain features on older versions or other browsers.

### Datasets guardrails {#datasets-guardrails}

As of February 2025, a time-to-live (TTL) guardrail is rolled out to Journey Optimizer system-generated datasets in **new sandboxes and new organizations** as follows:

* **90 days** for data in the profile store
* **13 months** for data in the data lake

This change will be enforced on **existing customer sandboxes** starting **October 1, 2026**. [Learn more about datasets Time-To-Live (TTL) guardrails](../data/datasets-ttl.md)

## Journeys {#journeys-guardrails}

This section covers guardrails and limitations for journeys, including general journey limitations, journey components (actions, events, data sources), journey activities, and specific features like custom actions and expression editor.

### General journey guardrails {#journeys-guardrails-journeys}

* The number of activities in a journey is limited to **50**. The number of activities is displayed on the upper left section of the journey canvas.

  As journeys near this limit, editing and publishing performance may degrade, and save or validation failures can occur. If this happens, split your journey into smaller sub-journeys using [jump activities](../building-journeys/jump.md) or recreate it in a new version. The activity limit cannot be increased.

* The number of live, closed, paused, and dry run journeys that can be active at one time is limited to **200** in production sandboxes and **100** in development sandboxes. This limit is enforced when you publish a journey. The current number of journeys is displayed above the journey canvas.

  As you publish journeys, we automatically scale and adjust to ensure maximum throughput and stability. Closed journeys are counted only if they are created after this guardrail is rolled out.

>[!NOTE]
>
>For publication-time guardrails, organizations that already exceed a limit when the guardrail is introduced receive an exception. Existing journeys are not impacted.

* When using an audience qualification in a journey, that audience qualification activity may take up to **10 minutes** to be active and listen to profiles entering or exiting the audience.

* A journey instance for a profile has a maximum size of **1 MB**. All data gathered as part of the journey execution is stored in that journey instance. Therefore, data from an incoming event, profile information retrieved from Adobe Experience Platform, custom action responses, etc. are stored in that journey instance and impact the journey size. It is advised, when a journey starts with an event, to limit the maximum size of that event payload (e.g., below **800 KB**) to avoid reaching that limit after a few activities, in the journey execution. This 800 KB guidance does not apply to business events or unitary events, which are subject to the stricter 64 KB limit described below. When the 1 MB limit is reached, the profile is in error status and will be excluded from the journey.

* Any event that starts or enters a journey, including business events and unitary events, is subject to an additional, stricter guardrail: the event payload is limited to a maximum of **64 KB of uncompressed, minified JSON**. Events exceeding this size are dropped and do not trigger the journey. This is separate from, and stricter than, the 1 MB journey instance limit above. [Learn more about configuring business events](../event/about-creating-business.md).

* For each profile and journey version, the journey runtime keeps an internal queue of up to **10 pending events** while one is being processed. If this limit is reached, additional events are discarded with the `maxInstanceStackEventsReached` reason until the stack drains. See [Events discarded due to a blocked journey instance](../building-journeys/troubleshooting-execution.md#max-instance-stack-events-reached).

* In addition to the timeout used in journey activities, there is also a global journey timeout which is not displayed in the interface and cannot be changed. This global timeout stops the progress of individuals in the journey **91 days** after they enter. [Read more](../building-journeys/journey-properties.md#global_timeout)

>[!TIP]
>
>**What this means for you:** The **50-activity limit** and **active journey limit** are the two guardrails most teams encounter first when scaling. Plan for journey splitting early, and spread Read Audience start times at least 5–10 minutes apart to avoid sandbox throughput contention.

#### Journey payload size validation {#journey-payload-size}

When you save or publish a journey, Journey Optimizer validates the total journey payload size to preserve stability and performance.

| Scenario | Threshold | Behavior |
|---|---|---|
| Payload < 90% of limit | Below warning | Journey saves and publishes successfully. No warnings or errors displayed. |
| Payload 90–99% of limit | Warning (soft) | Journey saves and publishes with a warning: **Warning**: Journey payload size is close to the limit. Largest node: '[NodeName]' (type: '[NodeType]', size: [N] bytes). |
| Payload ≥ 100% of limit | **Error (hard)** | Save or publish is blocked. Returns **HTTP 413 Request Entity Too Large**. Error: Journey payload size exceeds limit. Largest node: '[NodeName]' (type: '[NodeType]', size: [N] bytes). |

**Default configuration**

* **Default maximum request size**: **2 MB** (2,000,000 bytes). Some organizations may have custom limits configured by Adobe.
* **Warning threshold**: 90% of the maximum limit.
* **Error threshold**: 100% of the maximum limit.

**Troubleshooting and recommendations**

* Review the largest node highlighted in the warning or error.
* Simplify conditions, reduce data mappings, and remove unnecessary steps or parameters.
* Consider splitting the journey into smaller journeys if needed.
* If you believe your organization needs a higher limit, contact your Adobe representative.

To monitor the current payload size of your journey before publishing, use the **[!UICONTROL Current journey payload size]** indicator in the journey properties panel. [Learn how to check the size of your journey payload](../building-journeys/journey-properties.md#journey-payload-size)

### License package comparison {#select-package-limitations}

>[!NOTE]
>
>The Select package limitations below do not apply to Read Audience or Business Event journeys. If you need more complex journey logic with multiple actions, conditions, or wait activities, consider upgrading your license package or using Read Audience journeys where applicable.

For customers using the **Select** license package, the following additional limitations apply specifically to unitary journeys (journeys starting with an event or an audience qualification):

| Limitation | Error code | Description |
|---|---|---|
| Only one action allowed | `ERR_PKG_SELECT_8` | Unitary journeys can contain only **one** action activity. Multiple email, push, SMS, or other action activities are not permitted within the same journey. |
| No conditions allowed | `ERR_PKG_SELECT_7` | Condition activities cannot be used in unitary journeys. The journey must follow a single, linear path without branching logic. |
| No wait activities | `ERR_PKG_SELECT_6` | Wait activities cannot be added to unitary journeys. Actions must execute immediately without delays. |
| Timeout/error transitions must go to end node | `ERR_PKG_SELECT_2` | If you configure timeout or error transitions for an action (e.g., an email action), these paths must point directly to an end node. They cannot connect to other activities or actions in the journey. |

>[!TIP]
>
>**What this means for you:** If you're on the Select package and need branching logic, wait activities, or multiple actions, you must use a Read Audience journey instead, or contact your Adobe representative about upgrading your package.

### Journey versions {#journey-versions-g}

The following guardrails apply to the [Journey versions](../start/user-interface.md):

* A journey starting with an event activity in v1 cannot start with something else than an event in further versions. You cannot start a journey with a **Audience Qualification** event.
* A journey starting with a **Audience Qualification** activity in v1 must always start with a **Audience Qualification** in further versions.
* The audience and namespace chosen in **Audience Qualification** (first activity) cannot be changed in new versions.
* The reentrance rule must be the same in all journey versions.
* A journey starting with a **Read Audience** cannot start with another event in next versions.
* You cannot create a new version of a read audience journey with incremental read. You must duplicate the journey.

### Journeys and profile creation {#journeys-limitation-profile-creation}

There is a delay associated to API based profile creation/update in Adobe Experience Platform. The Service Level Target (SLT) in terms of latency is < 1 min from ingestion to Unified Profile for 95th percentile of requests, at a volume of **20K Requests per second (RPS)**.

If a journey is triggered simultaneously to a profile creation and immediately checks/retrieves information from Profile Service, it might not work properly.

You can choose from one of these two solutions:

* Add a wait activity after the first event, to give Adobe Experience Platform the time it needs to perform the ingestion to Profile Service.

* Set up a journey that does not immediately leverage the profile. For example, if the journey is designed to confirm an account creation, the experience event could contain information needed to send the first confirmation message (first name, last name, email address, etc.).

### Events {#events-g}

The following guardrails apply to the [Events](../event/about-events.md) in your journeys:

* Journey Optimizer supports a peak volume of **5,000 inbound journey events per second** for unitary events, and **5,000 inbound journey events per second** for Read Audience based journey events, across all sandboxes. Learn more about this limitation [on this page](../event/about-events.md#event-thoughput).
* Event-triggered journeys may take up to **5 minutes** to process the first action in the journey.
* For system-generated events, streaming data used to initiate a customer journey must be configured within Journey Optimizer first to get a unique orchestration ID. This orchestration ID must be appended to the streaming payload coming into Adobe Experience Platform. This limitation does not apply to rule-based events.
* Business events cannot be used in conjunction with unitary events or audience qualification activities.
* A single event can be referenced by a maximum of **25** journeys at any one time, across all live, closed, paused, test mode, and dry run journeys. When this limit is reached, publishing any additional journey that uses that event is blocked.
* A single XDM schema can be referenced by a maximum of **100** events across all live, closed, paused, test mode, and dry run journeys at one time. When this limit is reached, publishing any journey with an event node that references that schema is blocked.
* Unitary journeys (starting with an event or an audience qualification) include a guardrail that prevents journeys from being erroneously triggered multiple times for the same event. Profile reentrance is temporally blocked by default for **5 minutes**. For instance, if an event triggers a journey at 12:01 for a specific profile and another one arrives at 12:03 (whether it is the same event or a different one triggering the same journey) that journey will not start again for this profile.
* Journey Optimizer requires events to be streamed to Data Collection Core Service (DCCS) to be able to trigger a journey. Events ingested in batch, events inserted via **Query Service**, or events from internal Journey Optimizer datasets (Message Feedback, Email Tracking, etc.) cannot be used to trigger a journey. For use cases where you cannot get streamed events, you must build an audience based on those events and use the **Read Audience** activity instead. Audience qualification can technically be used, but is not recommended as it can cause downstream challenges based on the actions used.

### Data sources {#data-sources-g}

The following guardrails apply to the [Data Sources](../datasource/about-data-sources.md) in your journeys:

* External data sources can be leveraged within a customer journey to lookup external data in real time. These sources must be usable via REST API, support JSON and be able to handle the volume of requests.
* Internal Adobe addresses (`.adobe.*`) are not allowed in URLs and APIs.

>[!NOTE]
>
>As the responses are now supported, you should use custom actions instead of data sources for external data sources use-cases.

### General actions {#general-actions-g}

The following guardrails apply to the [Actions](../building-journeys/about-journey-activities.md) in your journeys:

* Three retries are systematically performed in case of an error. You cannot adjust the number of retries according to the error message received. Retries are performed for all HTTP errors except for HTTP 401, 403 and 404.
* The built-in **Reaction** event allows you to react to out-of-the-box actions. Learn more on [this page](../building-journeys/reaction-events.md). If you want to react to a message sent via a custom action, you must configure a dedicated event.
* You cannot place two actions in parallel, you must add them one after the other.
* A profile cannot be present multiple times in the same journey, at the same time, for all active [versions of the journey](../building-journeys/publish-journey.md#journey-create-new-version). If reentrance is enabled, a profile can reenter a journey, but cannot do it until he fully exited that previous instance of the journey. [Read more](../building-journeys/end-journey.md)

### Custom actions {#custom-actions-g}

The following guardrails apply to the [Custom Actions](../action/action.md) in your journeys:

* A capping limit of **300,000 calls over one minute** is defined for all custom actions, per host and per sandbox. This cap is enforced as a sliding window per sandbox and per endpoint for endpoints with response times less than 0.75 seconds. For endpoints with response times greater than 0.75 seconds, a separate limit of **150,000 calls per 30 seconds** (also a sliding window) applies.
* The custom action URL does not support dynamic parameters.
* POST, PUT and GET call methods are supported.
* The name of the query parameter or header must not start with "." or "$".
* IP addresses are not allowed in URLs. Use hostnames instead.
* Internal Adobe addresses (`.adobe.*`) are not allowed in URLs and APIs.
* Built-in custom actions cannot be removed.
* Custom actions support JSON format only when using request or response payloads. See [this page](../action/about-custom-action-configuration.md#custom-actions-limitations).
* Any endpoint targeted by a custom action must support at least **200 TPS**. Be cautious that a throttling configuration cannot go below 200 TPS. Depending on your expected throughput, having a high response time could impact the actual throughput.

>[!TIP]
>
>**What this means for you:** The default 300,000 calls/min cap protects your external endpoints from being overwhelmed by journey throughput. If your endpoint can handle more load, you can raise this limit using the [Capping API](../configuration/capping.md) or [Throttling API](../configuration/throttling.md). For a broader overview of how Journey Optimizer connects to external systems, see [this page](../configuration/external-systems.md). Contact your Adobe representative if you need a higher organizational limit.

### Supplemental identifiers {#supplemental}

Specific guardrails apply to the use of supplemental identifiers in journeys. They are listed in [this page](../building-journeys/supplemental-identifier.md#guardrails).

### Expression editor {#expression-editor}

The following guardrails apply to the [journey expression editor](../building-journeys/expression/expressionadvanced.md):

* Experience event field groups can not be used in journeys starting with a Read audience, an Audience qualification or a business event activity. You must create a new audience and use an `inaudience` condition in the journey.
* `timeSeriesEvents` attributes cannot be used in the expression editor. To access Experience Events at a profile level, please create a new field group based on a `XDM ExperienceEvent` schema.

### Journey activities {#activities}

#### Audience Qualification activity {#audience-qualif-g}

The following guardrails apply to the [Audience Qualification](../building-journeys/audience-qualification-events.md) journey activity:

* The Audience qualification activity cannot be used with Adobe Campaign activities.
* Supplemental identifiers are not supported for Audience qualification journeys.
* A sandbox can include a maximum of **300** Audience Qualification activities across all live, closed, paused, test mode, and dry run journeys. This limit also applies to Audience Qualification activities used as exit criteria. When this limit is reached, publishing journeys with additional Audience Qualification activities is blocked.

Learn more about journey processing rates and throughput limits in [this section](../building-journeys/entry-management.md#journey-processing-rate).

Additional guardrails — including recommendations on streaming vs. batch audiences and composition audience limitations — are listed on [this page](../building-journeys/audience-qualification-events.md#audience-qualification-guardrails).

#### Campaign activities {#ac-g}

The following guardrails apply to the **[!UICONTROL Campaign v7/v8]** and the **[!UICONTROL Campaign Standard]** activities:

* Adobe Campaign activities cannot be used with a Read audience, or an Audience qualification activity.
* **[!UICONTROL Campaign Standard]** activities cannot be used with other channel activities: Card, Code-based Experience, Email, Push, SMS, In-app messages, Web.
* **[!UICONTROL Campaign v7/v8]** activities can be used alongside native channel activities in the same journey.

#### Reaction events {#reaction-events-g}

Specific guardrails apply to **[!UICONTROL Reaction]** events, including the requirement to place the activity immediately after a channel action and the inability to track messages sent in a different journey. They are listed on [this page](../building-journeys/reaction-events.md#guardrails-limitations).

#### In-app activity {#in-app-activity-limitations}

The following guardrails apply to the **[!UICONTROL In-app message]** action. Learn more about In-app messages on [this page](../in-app/create-in-app.md).

* This feature is currently not available for Healthcare customers.

* Personalization can only contain profile attributes.

* The In-app activity cannot be used with **[!UICONTROL Campaign Standard]** activities.

* In-app display is tied to the journey lifespan, meaning that when the journey ends for a profile, all In-app messages within that journey will cease to be displayed for that profile. Consequently, it is not possible to stop an In-app message directly from a journey activity. Instead, you must end the entire journey to stop the In-app messages from being displayed to the profile.

* In test mode, the In-app display depends on the journey's lifespan. To prevent the journey from ending too early during testing, adjust the **[!UICONTROL Wait time]** value for your **[!UICONTROL Wait]** activities.

* **[!UICONTROL Reaction]** activities can not be used to react to an In-app open or click.

* An activation delay may happen between the moment a user profile reaches an In-app activity in the canvas and the time they start seeing that In-app message.

* In-app message content size is limited to **2 MB**. Including large images can hinder the publishing process.

#### Content decision activity {#content-decision-g}

Specific guardrails apply to the **[!UICONTROL Content decision]** activity, including a 48-hour delay before updated consent policies take effect in decision policies. They are listed on [this page](../building-journeys/content-decision.md#guardrails).

#### Jump activity {#jump-g}

Specific guardrails apply to the **[!UICONTROL Jump]** activity. They are listed on [this page](../building-journeys/jump.md#jump-limitations).

#### Read audience activity {#read-segment-g}

The following guardrails apply to the [Read Audience](../building-journeys/read-audience.md) journey activity:

* Streamed audiences are always up-to-date but batch audiences will not be calculated at retrieval time. They are only evaluated every day at the daily batch evaluation time.
* At journey entry, profiles use attribute values from the batch audience snapshot. However, when a profile reaches a **Wait** activity, the journey automatically refreshes profile attributes by fetching the latest data from Unified Profile Service (UPS). This means profile attributes may change during journey execution.
* The **Read Audience** activity cannot be used with Adobe Campaign activities.
* The **Read Audience** activity can only be used as a first activity in a journey, or after a business event activity.
* A journey can only have one **Read Audience** activity.
* The **Read Audience** activity can target only one audience per journey. If multiple audiences are required, merge them into a single audience first. [Learn how to combine audiences using composition workflows](../audience/get-started-audience-orchestration.md).
* Each organization can run up to **five** **Read Audience** instances concurrently (scheduled or business-event triggered), across all sandboxes and journeys. Avoid having more than five journeys with **Read Audience** starting at the exact same time; spread them 5 to 10 minutes apart. Learn more about journey processing rates in [this section](../building-journeys/entry-management.md#journey-processing-rate).
* Sandbox throughput: the system manages processing per sandbox with a maximum of **20,000 profiles per second** shared across all **Read Audience** activities. Individual activities can be configured from **500 to 20,000 profiles per second**. If sandbox limits are reached, jobs may be queued.
* Job processing timeout: **Read Audience** jobs that cannot be processed within **12 hours** are automatically cleaned up and will not execute.
* Retries are applied by default on audience-triggered journeys while retrieving the export job. If an error occurs during export job creation, retries will be made every 10 minutes, for a maximum of **1 hour**. After that, the journey is considered failed and can therefore be executed up to 1 hour after the scheduled time.
* For journeys using supplemental IDs, the reading rate of the **Read Audience** activity for each journey instance is limited to a maximum of **500 profiles per second**.

>[!TIP]
>
>**What this means for you:** The 5-concurrent-instance limit is a hard ceiling across your entire organization. If you have multiple teams scheduling Read Audience journeys, coordinate start times carefully. Jobs that miss the 12-hour processing window are silently dropped — always confirm successful execution in the journey logs.

See also [recommendations and configuration](../building-journeys/read-audience.md#must-read) for the Read Audience activity.

#### Update profile activity {#update-profile-g}

Specific guardrails apply to the **[!UICONTROL Update profile]** activity. They are listed on [this page](../building-journeys/update-profiles.md).

#### Journey Pause {#pause-g}

Specific guardrails apply to **pausing journeys**, including a maximum pause duration of **14 days** and a **10-million-profile cap** across all paused journeys in your organization. They are listed on [this page](../building-journeys/journey-pause.md#journey-pause-guardrails).

#### Journey Dry run {#dry-run-g}

Specific guardrails apply to **Journey Dry run**, including counting toward engageable profile and live journey quotas. They are listed on [this page](../building-journeys/journey-dry-run.md#journey-dry-run-limitations).

#### Journey Fragments {#fragments-journey-g}

Specific guardrails apply to **Journey Fragments**, including a maximum of **20 nodes per fragment** and **200 active fragments per sandbox**. They are listed on [this page](../building-journeys/journey-fragments.md#guardrails).

#### Send using waves {#waves-g}

Specific guardrails apply to **wave sending in journeys**, including a 2–10 wave range and a **30-minute minimum interval** between waves. They are listed on [this page](../delivery/send-using-waves.md#limitations-guardrails).

#### Journey simulation {#simulation-g}

Specific guardrails apply to **journey simulation**. They are listed on [this page](../building-journeys/simulate-journey.md#limitations).

## Audiences & Profiles {#audiences-profiles}

This section covers guardrails for audience management, profile handling, and engageable profile considerations.

### Audience and profile guardrails {#audience}

* You can publish up to **10 audience compositions** in a given sandbox. If you have reached this threshold, you need to delete a composition to free up space and publish a new one.

    Learn more about audience compositions on [this page](../audience/get-started-audience-orchestration.md).

* When ingesting data, emails are case-sensitive. It means that duplicate profiles may be created (for example, one profile for John.Greene@luma.com, another profile for john.greene@luma.com) and used when targeting the corresponding recipient in your [!DNL Journey Optimizer] journeys and campaigns.

* When targeting pseudonymous profiles (unauthenticated visitors) with inbound channels, consider setting a Time-To-Live (TTL) for automatic profile deletion to manage your engageable profile count and associated costs. [Learn more](#profile-management-inbound)

## Channels & Messaging {#channel-guardrails}

This section covers guardrails for all communication channels including email, SMS, inbound channels (web, in-app, code-based, content cards), and transactional messages.

>[!NOTE]
>
>In rare circumstances, temporary outages in a specific region can result in valid profiles being excluded from journeys, or mails wrongly marked as bounces. Once services are restored, re-check journey logs, verify consent profile fields, and re-publish the journey if needed. In the case of an ISP outage, learn how to remove profiles from the suppression list in [this section](../configuration/manage-suppression-list.md#remove-from-suppression-list).

### Email guardrails {#message-guardrails}

The following guardrails apply to the [email channel](../email/get-started-email.md):

* You cannot use the same sending domain to send out email messages from [!DNL Adobe Journey Optimizer] and from another product, such as [!DNL Adobe Campaign] or [!DNL Adobe Marketo Engage] for example.

* When designing email messages, the system checks for key settings and displays alerts for warnings (recommendations and best practices) and errors (blocking issues that prevent testing or activation). Learn more about email alerts and validation requirements in [this section](../email/create-email.md#check-email-alerts).

#### Message content size for journey publication {#message-content-size}

When publishing journeys that contain email messages, the total message content size must not exceed **2 MB** after backend processing. During publication, the system automatically processes message content by patching links, images, and applying transformations, which increases the payload size beyond the authored content size.

>[!CAUTION]
>
>If the final processed message content exceeds **2 MB**, journey publication will fail. Keep your authored message content well below 2 MB — ideally under **1 MB** — to allow a buffer of 300–400 KB for backend processing overhead.

**Best practices to prevent publication failures:**

* Keep authored email content under **1 MB**
* Minimize the number of content variants
* Optimize and compress images before adding them to messages
* Remove unused assets and unnecessary HTML elements
* Test message size before publishing journeys to production

If journey publication fails due to content size, reduce your message content and republish the journey.

### SMS guardrails {#sms-guardrails}

The following guardrails apply to the [SMS channel](../mobile/get-started-mobile.md):

* Media files for MMS can be included through a supported URL. Please ensure that the media file is uploaded separately.
* Message feedback syncing is not currently available for MMS.
* Consent management operates at the SMS channel level for MMS.

### Inbound channel guardrails {#inbound-guardrails}

* To use [code-based experience](../code-based/get-started-code-based.md) actions in [!DNL Journey Optimizer] and deliver code content payload that can be used by your applications, follow the prerequisites detailed on [this page](../code-based/code-based-prerequisites.md).

* To be able to access and author [web pages](../web/get-started-web.md) in the [!DNL Journey Optimizer] user interface, follow the prerequisites listed on [this page](../web/web-prerequisites.md).

* To send In-app messages in your journeys and campaigns with [!DNL Journey Optimizer], follow the delivery prerequisites listed on [this page](../in-app/inapp-configuration.md).

* For Adobe Journey Optimizer to correctly display content cards, you must configure the Adobe Experience Platform settings listed on [this page](../content-card/content-card-configuration-prereq.md).

* Journey Optimizer supports a peak volume of **5,000 inbound requests per second**. This guardrail applies to all inbound requests, which can originate from any of the Journey Optimizer supported inbound channels ([web](../web/get-started-web.md), [In-app](../in-app/get-started-in-app.md), [code-based experiences](../code-based/get-started-code-based.md), [content cards](../../rp_landing_pages/content-card-landing-page.md)).

* Journey Optimizer supports a maximum of **500 active inbound actions** at any moment in time. These inbound actions are counted if they are part of a live campaign or if they are a node used in a live journey. Once you reach this number, you need to deactivate older campaigns or journeys that are using inbound actions before being able to launch new ones.

#### Profile management with inbound channels {#profile-management-inbound}

[!DNL Journey Optimizer] inbound channels can target pseudonymous profiles, meaning profiles that are not authenticated or not known yet because they have not been engaged before on other channels. This is the case for example when targeting all visitors or audiences based on temporary IDs like ECID.

This increases your total engageable profile count, which may have cost implications if the contractual number of engageable profiles you purchased is exceeded. License metrics for each package are listed on the [Journey Optimizer Product Description](https://helpx.adobe.com/legal/product-descriptions/adobe-journey-optimizer.html){target="_blank"} page. You can check the number of engageable profiles in the [license usage dashboard](../audience/license-usage.md).

To keep your engageable profiles within reasonable limits, Adobe recommends setting a Time-To-Live (TTL) to automatically delete pseudonymous profiles from the Real-Time Customer Profile if they haven't been seen or engaged within a specific time window. Adobe recommends setting the TTL value to **14 days** to match the current Edge profile TTL.

>[!NOTE]
>
>Learn how to configure data expiration for pseudonymous profiles in the [Experience Platform documentation](https://experienceleague.adobe.com/en/docs/experience-platform/profile/pseudonymous-profiles){target="_blank"}.

### Transactional message guardrails {#transactional-message-guardrails}

Journey Optimizer supports a peak volume of **500 transactional messages per second** in campaigns.

### Subdomains guardrails {#subdomain-guardrails}

The guardrails and limitations applying to subdomain delegation in Journey Optimizer are detailed on [this page](../configuration/delegate-subdomain.md#guardrails).

## Content & Assets {#content-assets}

This section covers guardrails for content creation and management, including landing pages and fragments.

### Content authoring guardrails {#content-authoring}

The recommended size limits for content types are as follows:

| Content type | Recommended size limit |
|---|---|
| Template | 1200 KB |
| Fragment | 700 KB |
| Message | 1200 KB |
| Landing page | 1000 KB |

A warning is surfaced when a content variant exceeds its recommended size threshold. This applies to all content types and channels, and does not block saving or publishing.

### Generate Content guardrails {#ai-assistant-g}

Guardrails and limitations for **Generate Content** — including supported channels (email, push, web, SMS) and personalization editor limitations — are listed on [this page](../content-management/gs-generative.md#generative-guardrails).

### Landing pages guardrails {#lp-guardrails}

The following guardrails apply to the [landing pages](../landing-pages/get-started-lp.md):

* Only one **Form** component can be used in a single primary page.
* The **Form** component cannot be used in subpages.
* You cannot add a preheader to a landing page.
* You cannot select the **Code your own** option when designing a landing primary page.

### Fragments guardrails {#fragments-guardrails}

The following guardrails apply to the [fragments](../content-management/fragments.md):

* To create, edit, archive, and publish fragments you need the **[!DNL Manage library items]** and **[Publish Fragment]** permissions included in the **[!DNL Content Library Manager]** product profile. [Learn more](../administration/ootb-product-profiles.md#content-library-manager)
* Visual fragments are only available for the Email channel.
* Expression fragments are not available for the In-app channel.
* Fragments cannot exceed **700 KB**. This is a system guardrail for fragment size storage and processing. To stay below this threshold, split large content into multiple reusable fragments, reduce heavy markup, and optimize linked assets.

  >[!NOTE]
  >
  >If a visual fragment exceeds **100 KB** or an expression fragment exceeds **200 KB**, this can cause truncation issues in email delivery.

* **Fragment count limits**: the number of unique fragments used within a piece of content is validated during authoring. Only fragments (including AEM fragments) referenced directly are counted — fragments nested inside other fragments are not counted separately.

  * **Per variant**: up to 60 unique fragments per content variant. A warning is shown when usage reaches 45 (75% of the limit); publishing is blocked at 60.
  * **Across variants**: up to 120 unique fragments across all variants of a single message. A warning is shown when usage reaches 90 (75% of the limit); publishing is blocked at 120.

* To use a fragment in a journey or campaign, it must be in the **Live** status.
* [Contextual attributes](../personalization/personalization-build-expressions.md) are not supported within fragments.
* Visual fragments are not cross-compatible between the Use Themes and Manual Styling modes. To be able to use a fragment in a content where you want to apply a theme, this fragment must be created in Use Themes mode. [Learn more on themes](../email/apply-email-themes.md)
* When tracking is enabled in a journey or a campaign, if you add links to a fragment and if this fragment is used in a message, these links are tracked such as all other links included in the message. [Learn more on links and tracking](../email/message-tracking.md)

## Decision Management {#decision-management}

### Decisioning & Decision management guardrails {#decisioning-guardrails}

Guardrails and limitations to keep in mind when working with Decisioning or Decision management are detailed in these the Decisioning & Decision management sections:

* [Decisioning guardrails & limitations](../experience-decisioning/decisioning-guardrails.md)
* [Decision management guardrails & limitations](../offers/decision-management-guardrails.md)

## Campaign Orchestration {#campaign-orchestration}

### Campaign Orchestration guardrails {#orchestration-guardrails}

Guardrails and limitations to keep in mind when working with Campaign Orchestration are detailed in this section: [Guardrails & limitations](../orchestrated/guardrails.md).
