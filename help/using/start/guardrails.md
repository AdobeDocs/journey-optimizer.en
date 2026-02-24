---
solution: Journey Optimizer
product: journey optimizer
title: Journey Optimizer guardrails and limitations
description: Learn more about Journey Optimizer guardrails
feature: Guardrails
role: User
level: Intermediate
mini-toc-levels: 1
exl-id: 5d59f21c-f76e-45a9-a839-55816e39758a
---
# Guardrails and limitations {#limitations}

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

* 90 days for data in the profile store,
* 13 months for data in the data lake.

This change will be rolled out to **existing customer sandboxes** in a subsequent phase. [Learn more about datasets Time-To-Live (TTL) guardrails](../data/datasets-ttl.md)

## Channels & Messaging {#channel-guardrails}

This section covers guardrails for all communication channels including email, SMS, inbound channels (web, in-app, code-based, content cards), and transactional messages.

>[!NOTE]
>
>In rare circumstances, temporary outages in a specific region can result in valid profiles being excluded from journeys, or mails wrongly marked as bounces. Once services are restored, re-check journey logs, verify consent profile fields, and re-publish the journey if needed. In the case of an ISP outage, learn how to remove profiles from the suppression list in [this section](../configuration/manage-suppression-list.md#remove-from-suppression-list).

### Email guardrails {#message-guardrails}

<!--The following guardrails apply to the [email channel](../../rp_landing_pages/email-landing-page.md):-->

The following guardrails apply to the [email channel](../email/get-started-email.md):

* You cannot use the same sending domain to send out email messages from [!DNL Adobe Journey Optimizer] and from another product, such as [!DNL Adobe Campaign] or [!DNL Adobe Marketo Engage] for example.

When designing email messages, the system checks for key settings and displays alerts for warnings (recommendations and best practices) and errors (blocking issues that prevent testing or activation). Learn more about email alerts and validation requirements in [this section](../email/create-email.md#check-email-alerts).

#### Message content size for journey publication {#message-content-size}

When publishing journeys that contain email messages, the total message content size must not exceed **2MB** after backend processing. During publication, the system automatically processes message content by patching links, images, and applying transformations, which increases the payload size beyond the authored content size.

>[!CAUTION]
>
>If the final processed message content exceeds 2MB, journey publication will fail. To avoid publication failures, keep your authored message content well below 2MB — ideally under **1MB** — to allow a buffer of 300-400KB for backend processing overhead.

**Best practices to prevent publication failures:**

* Keep authored email content under 1MB
* Minimize the number of content variants
* Optimize and compress images before adding them to messages
* Remove unused assets and unnecessary HTML elements
* Test message size before publishing journeys to production

If journey publication fails due to content size, reduce your message content and republish the journey.

### SMS guardrails {#sms-guardrails}

The following guardrails apply to the [SMS channel](../sms/get-started-sms.md):

* Media files for MMS can be included through a supported URL. Please ensure that the media file is uploaded separately.
* Message feedback syncing is not currently available for MMS.
* Consent management operates at the SMS channel level for MMS.

### Inbound channel guardrails {#inbound-guardrails}

* To use [code-based experience](../code-based/get-started-code-based.md) actions in [!DNL Journey Optimizer] and deliver code content payload that can be used by your applications, follow the prerequisites detailed on [this page](../code-based/code-based-prerequisites.md).

* To be able to access and author [web pages](../web/get-started-web.md) in the [!DNL Journey Optimizer] user interface, follow the prerequisites listed on [this page](../web/web-prerequisites.md).

* To send In-app messages in your journeys and campaigns with [!DNL Journey Optimizer], follow the delivery prerequisites listed on [this page](../in-app/inapp-configuration.md).

* For Adobe Journey Optimizer to correctly display content cards, you must configure the Adobe Experience Platform settings listed on [this page](../content-card/content-card-configuration-prereq.md).

* Journey Optimizer supports a peak volume of 5,000 inbound requests per second. This guardrail applies to all inbound requests, which can originate from any of the Journey Optimizer supported inbound channels ([web](../web/get-started-web.md), [In-app](../in-app/get-started-in-app.md), [code-based experiences](../code-based/get-started-code-based.md), [content cards](../../rp_landing_pages/content-card-landing-page.md)).

    Journey Optimizer inbound channels target new profiles that might have not been engaged before on other channels. This will increase your total [Engageable Profiles](../audience/license-usage.md) count, which may have cost implications if the contractual number of Engageable Profiles you purchased is exceeded.

    Licence metrics for each package are listed on the [Journey Optimizer Product Description](https://helpx.adobe.com/legal/product-descriptions/adobe-journey-optimizer.html){target="_blank"} page. You can check the number of Engageable Profiles in the [license usage dashboard](../audience/license-usage.md).

* Journey Optimizer supports a maximum of 500 active inbound actions at any moment in time. These inbound actions are counted if they are part of a live campaign or if they are a node used in a live journey. Once you reach this number, you need to deactivate older campaigns or journeys that are using inbound actions before being able to launch new ones.

#### Profile management with inbound channels {#profile-management-inbound}

[!DNL Journey Optimizer] inbound channels can target pseudonymous profiles, meaning profiles that are not authenticated or not known yet because they have not been engaged before on other channels. This is the case for example when targeting all visitors or audiences based on temporary IDs like ECID.

This increases your total engageable profile count, which may have cost implications if the contractual number of engageable profiles you purchased is exceeded. License metrics for each package are listed on the [Journey Optimizer Product Description](https://helpx.adobe.com/legal/product-descriptions/adobe-journey-optimizer.html){target="_blank"} page. You can check the number of engageable profiles in the [license usage dashboard](../audience/license-usage.md).

To keep your engageable profiles within reasonable limits, Adobe recommends setting a Time-To-Live (TTL) to automatically delete pseudonymous profiles from the Real-Time Customer Profile if they haven't been seen or engaged within a specific time window.

>[!NOTE]
>
>Learn how to configure data expiration for pseudonymous profiles in the [Experience Platform documentation](https://experienceleague.adobe.com/en/docs/experience-platform/profile/pseudonymous-profiles){target="_blank"}.

Adobe recommends setting the TTL value to 14 days to match the current Edge profile TTL.

### Transactional message guardrails {#transactional-message-guardrails}

Journey Optimizer supports a peak volume of 500 transactional messages per second in campaigns.

## Content & Assets {#content-assets}

This section covers guardrails for content creation and management, including landing pages, subdomains, and fragments.

### Landing pages guardrails {#lp-guardrails}

The following guardrails apply to the [landing pages](../landing-pages/get-started-lp.md):

* Only one **Form** component can be used in a single primary page.
* The **Form** component cannot be used in subpages.
* You cannot add a preheader to a landing page.
* You cannot select the **Code your own** option when designing a landing primary page.

### Subdomains guardrails {#subdomain-guardrails}

The guardrails and limitations applying to subdomain delegation in Journey Optimizer are detailed on [this page](../configuration/delegate-subdomain.md#guardrails).

### Fragments guardrails {#fragments-guardrails}

The following guardrails apply to the [fragments](../content-management/fragments.md):

* To create, edit, archive, and publish fragments you need the **[!DNL Manage library items]** and **[Publish Fragment]** permissions included in the **[!DNL Content Library Manager]** product profile. [Learn more](../administration/ootb-product-profiles.md#content-library-manager)
* Visual fragments are only available for the Email channel.
* Expression fragments are not available for the In-app channel.
* Visual fragments cannot exceed 100KB. Expression fragments cannot exceed 200KB.
* To use a fragment in a journey or campaign, it must be in the **Live** status. 
* [Contextual attributes](../personalization/personalization-build-expressions.md) are not supported within fragments.
* Visual fragments are not cross-compatible between the Use Themes and Manual Styling modes. To be able to use a fragment in a content where you want to apply a theme, this fragment must be created in Use Themes mode. [Learn more on themes](../email/apply-email-themes.md)
* When tracking is enabled in a journey or a campaign, if you add links to a fragment and if this fragment is used in a message, these links are tracked such as all other links included in the message. [Learn more on links and tracking](../email/message-tracking.md)

## Audiences & Profiles {#audiences-profiles}

This section covers guardrails for audience management, profile handling, and engageable profile considerations.

### Audience and profile guardrails {#audience}

* You can publish up to 10 audience compositions in a given sandbox. If you have reached this threshold, you need to delete a composition to free up space and publish a new one.

    Learn more about audience compositions on [this page](../audience/get-started-audience-orchestration.md).

* When ingesting data, emails are case-sensitive. It means that duplicate profiles may be created (for example, one profile for John.Greene@luma.com, another profile for john.greene@luma.com) and used when targeting the corresponding recipient in your [!DNL Journey Optimizer] journeys and campaigns.

* When targeting pseudonymous profiles (unauthenticated visitors) with inbound channels, consider setting a Time-To-Live (TTL) for automatic profile deletion to manage your engageable profile count and associated costs. [Learn more](#profile-management-inbound)

## Decision Management {#decision-management}

### Decisioning & Decision management guardrails {#decisioning-guardrails}

Guardrails and limitations to keep in mind when working with Decisioning or Decision management are detailed in these the Decisioning & Decision management sections:

* [Decisioning guardrails & limitations](../experience-decisioning/decisioning-guardrails.md)
* [Decision management guardrails & limitations](../offers/decision-management-guardrails.md)

## Journeys {#journeys-guardrails}

This section covers guardrails and limitations for journeys, including general journey limitations, journey components (actions, events, data sources), journey activities, and specific features like custom actions and expression editor.

### General journey guardrails {#journeys-guardrails-journeys}

* The number of activities in a journey is limited to 50. The number of activities is displayed on the upper left section of the journey canvas. This will help in readability, QA and troubleshooting. 
* By default, the number of live/paused/dry run journeys at one time is limited to 100.  The current number of journeys is displayed above the journey canvas.
* As you publish journeys, we automatically scale and adjust to ensure maximum throughput and stability. As you near the milestone of 100 live journeys at one time, you will see a notification appear in the UI on this achievement. If you see this notification and have a need to extend your journeys beyond 100 live journeys at a time, please create a ticket for customer care and we will help you reach your goals. 
* When using an audience qualification in a journey, that audience qualification activity may take up to 10 minutes to be active and listen to profiles entering or exiting the audience.
* A journey instance for a profile has a maximum size of 1MB. All data gathered as part of the journey execution is stored in that journey instance. Therefore, data from an incoming event, profile information retrieved from Adobe Experience Platform, custom action responses, etc. are stored in that journey instance and impact the journey size. It is advised, when a journey starts with an event, to limit the maximum size of that event payload (eg: below 800 KB) to avoid reaching that limit after a few activities, in the journey execution. When that limit is reached, the profile is in error status and will be excluded from the journey.
* In addition to the timeout used in journey activities, there is also a global journey timeout which is not displayed in the interface and cannot be changed. This global timeout stops the progress of individuals in the journey 91 days after they enter. [Read more](../building-journeys/journey-properties.md#global_timeout)


#### Journey payload size validation {#journey-payload-size}

When you save or publish a journey, Journey Optimizer validates the total journey payload size to preserve stability and performance.

**Default configuration**

* **Default maximum request size**: 2 MB (2,000,000 bytes). Some organizations may have custom limits configured by Adobe.
* **Warning threshold**: 90% of the maximum limit.
* **Error threshold**: 100% of the maximum limit. Saving or publishing is blocked and the request returns **HTTP 413 Request Entity Too Large**.

**User experience scenarios**

* **Payload < 90% of limit**: Journey saves and publishes successfully. No warnings or errors are displayed.
* **Payload 90-99% of limit**: Journey saves and publishes successfully, with a warning to optimize. Warning message: **Warning**: Journey payload size is close to the limit. Largest node: '[NodeName]' (type: '[NodeType]', size: [N] bytes).
* **Payload >= 100% of limit**: Journey save or publish is blocked with an error. Error message: **Error**: Journey payload size exceeds limit. Largest node: '[NodeName]' (type: '[NodeType]', size: [N] bytes).

**Error response details**

If the request exceeds the maximum allowed size, the response includes **Request Entity Too Large**. The journey payload exceeds the maximum allowed size. Review the error details and optimize your journey.

**Troubleshooting and recommendations**

* Review the largest node highlighted in the warning or error.
* Simplify conditions, reduce data mappings, and remove unnecessary steps or parameters.
* Consider splitting the journey into smaller journeys if needed.
* If you believe your organization needs a higher limit, contact your Adobe representative.

### Select package limitations for unitary journeys {#select-package-limitations}

>[!NOTE]
>
>These limitations do not apply to Read Audience or Business Event journeys with the **Select** package. If you need more complex journey logic with multiple actions, conditions, or wait activities, consider upgrading your license package or using Read Audience journeys where applicable.

For customers using the **Select** license package, the following additional limitations apply specifically to unitary journeys, journeys starting with an event or an audience qualification:

* **SELECT package: only one action allowed in unitary journey (ERR_PKG_SELECT_8)**: Unitary journeys can contain only one action activity. You cannot add multiple email, push, SMS, or other action activities within the same journey.

* **SELECT package: no condition allowed in unitary journey (ERR_PKG_SELECT_7)**: Condition activities cannot be used in unitary journeys. The journey must follow a single, linear path without branching logic.

* **SELECT package: no wait allowed in unitary journey (ERR_PKG_SELECT_6)**: Wait activities cannot be added to unitary journeys. Actions must execute immediately without delays.

* **SELECT package: timeout/error transition from node must point to end node only (ERR_PKG_SELECT_2)**: If you configure timeout or error transitions for an action, such as an email action, these paths must point directly to an end node. They cannot connect to other activities or actions in the journey.


### General actions {#general-actions-g}

The following guardrails apply to the [Actions](../building-journeys/about-journey-activities.md) in your journeys:

* Three retries are systematically performed in case of an error. You cannot adjust the number of retries according to the error message received. Retries are performed for all HTTP errors except for HTTP 401, 403 and 404.
* The built-in **Reaction** event allows you to react to out-of-the-box actions. Learn more on [this page](../building-journeys/reaction-events.md). If you want to react to a message sent via a custom action, you must configure a dedicated event.
* You cannot place two actions in parallel, you must add them one after the other.
* A profile cannot be present multiple times in the same journey, at the same time, for all active [versions of the journey](../building-journeys/publish-journey.md#journey-create-new-version). If reentrance is enabled, a profile can reenter a journey, but cannot do it until he fully exited that previous instance of the journey. [Read more](../building-journeys/end-journey.md)

### Journey versions {#journey-versions-g}

The following guardrails apply to the [Journey versions](../start/user-interface.md):

* A journey starting with an event activity in v1 cannot start with something else than an event in further versions. You cannot start a journey with a **Audience Qualification** event. 
* A journey starting with a **Audience Qualification** activity in v1 must always start with a **Audience Qualification** in further versions. 
* The audience and namespace chosen in **Audience Qualification** (first node) cannot be changed in new versions.
* The reentrance rule must be the same in all journey versions.
* A journey starting with a **Read Audience** cannot start with another event in next versions.
* You cannot create a new version of a read audience journey with incremental read. You must duplicate the journey.

### Custom actions {#custom-actions-g}

The following guardrails apply to the [Custom Actions](../action/action.md) in your journeys:

* A capping limit of 300,000 calls over one minute is defined for all custom actions, per host and per sandbox. The "per host" limit applies at the domain level (e.g., example.com). This cap is enforced as a sliding window per sandbox and per endpoint for endpoints with response times less than 0.75 seconds. For endpoints with response times greater than 0.75 seconds, a separate limit of 150,000 calls per 30 seconds (also a sliding window) applies. Refer to [this page](../action/about-custom-action-configuration.md). This limit has been set based on customers usage, to protect external endpoints targeted by custom actions. If needed, you can override this setting by defining a greater capping or throttling limit through our Capping/Throttling APIs. See [this page](../configuration/external-systems.md).
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

The following guardrails apply to the [Events](../event/about-events.md) in your journeys:

* Journey Optimizer supports a peak volume of 5,000 inbound journey events per second, across all sandboxes. Learn more about this limitation [on this page](../event/about-events.md#event-thoughput).
* Event-triggered journeys may take up to 5 minutes to process the first action in the journey.
* For system-generated events, streaming data used to initiate a customer journey must be configured within Journey Optimizer first to get a unique orchestration ID. This orchestration ID must be appended to the streaming payload coming into Adobe Experience Platform. This limitation does not apply to rule-based events.
* Business events cannot be used in conjunction with unitary events or audience qualification activities.
* Unitary journeys (starting with an event or an audience qualification) include a guardrail that prevents journeys from being erroneously triggered multiple times for the same event. Profile reentrance is temporally blocked by default for 5 minutes. For instance, if an event triggers a journey at 12:01 for a specific profile and another one arrives at 12:03 (whether it is the same event or a different one triggering the same journey) that journey will not start again for this profile.
* Journey Optimizer requires events to be streamed to Data Collection Core Service (DCCS) to be able to trigger a journey. Events ingested in batch, events inserted via **Query Service**, or events from internal Journey Optimizer datasets (Message Feedback, Email Tracking, etc.) cannot be used to trigger a journey. For use cases where you cannot get streamed events, you must build an audience based on those events and use the **Read Audience** activity instead. Audience qualification can technically be used, but is not recommended as it can cause downstream challenges based on the actions used.

### Data sources {#data-sources-g}

The following guardrails apply to the [Data Sources](../datasource/about-data-sources.md) in your journeys:

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


### Supplemental identifiers {#supplemental}

Specific guardrails apply to the use of supplemental identifiers in journeys. They are listed in [this page](../building-journeys/supplemental-identifier.md#guardrails).

### Expression editor {#expression-editor}

The following guardrails apply to the [journey expression editor](../building-journeys/expression/expressionadvanced.md):

* Experience event field groups can not be used in journeys starting with a Read audience, an Audience qualification or a business event activity. You must create a new audience and use an `inaudience` condition in the journey.
* `timeSeriesEvents` attributes cannot be used in the expression editor. To access Experience Events at a profile level, please create a new field group based on a `XDM ExperienceEvent` schema.

### Journey activities {#activities}

#### Audience Qualification activity {#audience-qualif-g}

The following guardrail applies to the [Audience Qualification](../building-journeys/audience-qualification-events.md) journey activity:

* The Audience qualification activity cannot be used with Adobe Campaign activities.
* Supplemental identifiers are not supported for Audience qualification journeys.

Learn more about journey processing rates and throughput limits in [this section](../building-journeys/entry-management.md#journey-processing-rate).

#### Campaign activities {#ac-g}

The following guardrails apply to the **[!UICONTROL Campaign v7/v8]** and the **[!UICONTROL Campaign Standard]** activities:

* Adobe Campaign activities cannot be used with a Read audience, or an Audience qualification activity.
* **[!UICONTROL Campaign Standard]** activities cannot be used with other channel activities: Card, Code-based Experience, Email, Push, SMS, In-app messages, Web.
* **[!UICONTROL Campaign v7/v8]** activities can be used alongside native channel activities in the same journey.

#### In-app activity {#in-app-activity-limitations}

The following guardrails apply to the **[!UICONTROL In-app message]** action. Learn more about In-app messages on [this page](../in-app/create-in-app.md).

* This feature is currently not available for Healthcare customers.

* Personalization can only contain profile attributes.

* The In-app activity cannot be used with **[!UICONTROL Campaign Standard]** activities.

* In-app display is tied to the journey lifespan, meaning that when the journey ends for a profile, all In-app messages within that journey will cease to be displayed for that profile.  Consequently, it is not possible to stop an In-app message directly from a journey activity. Instead, you must end the entire journey to stop the In-app messages from being displayed to the profile.

* In test mode, the In-app display depends on the journey's lifespan. To prevent the journey from ending too early during testing, adjust the **[!UICONTROL Wait time]** value for your **[!UICONTROL Wait]** activities. 

* **[!UICONTROL Reaction]** activities can not be used to react to an In-app open or click.

* An activation delay may happen between the moment a user profile reaches an In-app activity in the canvas and the time they start seeing that In-app message.

* In-app message content size is limited to 2Mb. Including large images can hinder the publishing process.

#### Jump activity {#jump-g}

Specific guardrails apply to the **[!UICONTROL Jump]** activity. They are listed on [this page](../building-journeys/jump.md#jump-limitations).

#### Read audience activity {#read-segment-g}

The following guardrails apply to the [Read Audience](../building-journeys/read-audience.md) journey activity:

* Streamed audiences are always up-to-date but batch audiences will not be calculated at retrieval time. They are only evaluated every day at the daily batch evaluation time.
* At journey entry, profiles use attribute values from the batch audience snapshot. However, when a profile reaches a **Wait** activity, the journey automatically refreshes profile attributes by fetching the latest data from Unified Profile Service (UPS). This means profile attributes may change during journey execution.
* For journeys using a **Read Audience** activity, there is a maximum number of journeys that can start at the exact same time. Retries will be performed by the system but please avoid having more than five journeys (with **Read Audience**, scheduled or starting "as soon as possible") starting at the exact same time by spreading them over time, for example 5 to 10 minutes apart. Learn more about journey processing rates in [this section](../building-journeys/entry-management.md#journey-processing-rate).
* The **Read Audience** activity cannot be used with Adobe Campaign activities.
* The **Read Audience** activity can only be used as a first activity in a journey, of after a business event activity.
* A journey can only have one **Read Audience** activity.
* See also recommendations about how to use the **Read Audience** activity on [this page](../building-journeys/read-audience.md).
* Retries are applied by default on audience-triggered journeys (starting with a **Read Audience** or a **Business Event**) while retrieving the export job. If an error occurs during the export job creation, retries will be made every 10mn, for 1 hour max. After that, we will consider it as a failure. Those types of journeys can therefore be executed up to 1 hour after the scheduled time.
* For journeys using supplemental IDs, the reading rate of the read audience activity for each journey instance is limited to a maximum of 500 profiles per second.

See also [this page](../building-journeys/read-audience.md#must-read).

#### Update profile activity {#update-profile-g}

Specific guardrails apply to the **[!UICONTROL Update profile]** activity. They are listed on [this page](../building-journeys/update-profiles.md).

## Campaign Orchestration {#campaign-orchestration}

### Campaign Orchestration guardrails {#orchestration-guardrails}

Guardrails and limitations to keep in mind when working with Campaign Orchestration are detailed in this section: [Guardrails & limitations](../orchestrated/guardrails.md).
