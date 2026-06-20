---
title: Get Started for Developers
description: As a Developer, learn more how to work with Journey Optimizer
feature: Get Started
role: Developer
level: Intermediate
exl-id: 5053dd4f-d050-415f-bc74-d6d061bdcbe1
TQID: https://experienceleague.adobe.com/7fRI-CPkIeBAPjtXmDgFdyNKgB4WwEc01yKrGUXnc3U
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: d998adac-2f81-400b-a669-d07bb196e4eb
    internal-label: Journeys
  - id: fe96aceb-8194-4a8a-a6b0-75302d02804d
    internal-label: Integrations
subfeature_v2:
  - id: b3a93754-a8b8-46eb-9421-7eccaeeb3dff
    internal-label: Best practices
  - id: c2beecbb-b93e-4ae3-baa9-72adcdc06781
    internal-label: Action configuration
  - id: d08afb72-92f6-4856-88e3-11ec34313c2f
    internal-label: Event configuration
  - id: e30b0a1a-b594-47b8-af94-1e3a2be6df11
    internal-label: Get started
role_v2:
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
topic_v2:
  - id: b4dd41a7-ccf8-4e9d-918e-acaab534a307
    internal-label: Data quality
  - id: b5ce8718-c3af-4fdb-a1a9-fca32f83a87c
    internal-label: Implementation
  - id: c1579802-ddd4-4214-8a91-97b2066abe11
    internal-label: Troubleshooting
  - id: c7d04a2c-412a-4c9d-9d7a-4456eaa5adeb
    internal-label: Governance
  - id: d095671a-1355-40aa-8b5f-06c33c68080b
    internal-label: Security
  - id: d3cdead0-685a-4489-9250-4bb709942f66
    internal-label: Data collection
  - id: e9001ce2-5245-4a8e-8601-dd958009072f
    internal-label: Web experience
  - id: f4e6943a-c91a-4134-a2c7-f4f20cfff2f0
    internal-label: Privacy
---
# Get started for developers {#get-started-developers}

>[!BEGINSHADEBOX]

**On this page:** Implement the SDKs, event streaming, custom action endpoints, and APIs that connect your applications to Adobe Journey Optimizer so your journeys can run on live data.

>[!ENDSHADEBOX]

As a **Developer**, you are responsible for implementing and integrating [!DNL Adobe Journey Optimizer] into your applications and systems. You can start working with [!DNL Adobe Journey Optimizer] once the [System Administrator](administrator.md) and the [Data Engineer](data-engineer.md) have granted you access and prepared your environment.

>[!NOTE]
>
>**Implementation order:** [Administrator](administrator.md) → [Data Engineer](data-engineer.md) → You are here: **Developer** → [Marketer](marketer.md)
>
>Ensure [data schemas and events](data-engineer.md) are configured before implementing your mobile and web integrations.

## Your role in the Journey Optimizer ecosystem

While other team members configure Journey Optimizer through the user interface, you'll focus on:

* **Implementing SDKs** in mobile and web applications
* **Sending events** from your applications to trigger journeys
* **Building API endpoints** that Journey Optimizer can call via custom actions  
* **Integrating** Journey Optimizer with your existing systems and infrastructure
* **Testing and debugging** your implementations

Your [Data Engineer](data-engineer.md) will handle data schemas, event configurations, and data sources. Your [Administrator](administrator.md) will set up permissions and channel configurations. [Marketers](marketer.md) will design the journeys and content that use your implementations.

This guide covers the essential technical implementation steps to get you started with Journey Optimizer. Whether you're building mobile apps, web experiences, or API integrations, follow the sections below to set up your implementation.

## Prerequisites {#prerequisites}

Before starting your implementation, ensure you have:

| Category | Requirements |
|----------|-------------|
| **Technical skills** | * Experience with JavaScript (for Web SDK) or Swift/Kotlin (for Mobile SDK)<br>* Understanding of RESTful APIs and JSON<br>* Familiarity with asynchronous programming and event-driven architectures<br>* Knowledge of your organization's application architecture |
| **Access and tools** | * Access to [Adobe Developer Console](https://developer.adobe.com){target="_blank"} for API credentials<br>* Development environment with access to your application's codebase<br>* Testing tools like Postman for API testing<br>* Browser developer tools or mobile debugging tools |
| **From other team members** | * Environment access granted by your [Administrator](administrator.md)<br>* XDM schemas and event definitions from your [Data Engineer](data-engineer.md)<br>* Requirements and use cases from your [Marketers](marketer.md) |

## Understand the technical foundation {#technical-foundation}

Before diving into implementation, familiarize yourself with the core technical concepts:

1. **Adobe Experience Platform integration**: Journey Optimizer is built natively on Adobe Experience Platform. Understanding the underlying architecture will help you build more effective implementations. Learn more about [how Journey Optimizer works](../understanding-ajo.md).

1. **XDM data models**: Journey Optimizer uses Experience Data Model (XDM) to structure event and profile data. As a developer, you'll need to understand how to send data that conforms to the schemas configured by your [Data Engineer](data-engineer.md). Learn about [XDM schemas](../../data/get-started-schemas.md).

1. **Authentication and security**: All implementations require proper authentication. Understand how to set up authentication for SDKs and APIs. Learn about [API authentication](https://developer.adobe.com/journey-optimizer-apis/references/authentication){target="_blank"}.

## Set up mobile app integrations {#mobile-integration}

### Configure the Adobe Experience Platform Mobile SDK

The Mobile SDK is a collection of libraries you embed directly in your iOS or Android app. It acts as the communication layer between your app and Adobe Experience Platform: it identifies users, collects behavioral events, and delivers instructions from Journey Optimizer — including push notifications, in-app messages, and personalized content. Without it, Journey Optimizer has no visibility into what your app users are doing and no way to reach them.

1. **Install and configure the Mobile SDK**: Follow the [Adobe Experience Platform Mobile SDK documentation](https://developer.adobe.com/client-sdks/documentation/getting-started){target="_blank"} to get started with SDK integration.

1. **Create a mobile property**: Set up a mobile property in [!DNL Adobe Experience Platform Data Collection]. Learn how to [create and configure a mobile property](https://developer.adobe.com/client-sdks/documentation/getting-started/create-a-mobile-property){target="_blank"}.

1. **Configure push notifications**: 
   * For **iOS apps**: Register your app with APNs (Apple Push Notification service). Learn more in [Apple's documentation](https://developer.apple.com/documentation/usernotifications/registering_your_app_with_apns){target="_blank"}.
   * For **Android apps**: Set up Firebase Cloud Messaging for your Android app. Learn more in [Google's documentation](https://firebase.google.com/docs/cloud-messaging/android/client){target="_blank"}.

1. **Test your mobile integration**: Use the [mobile onboarding quick start workflow](../../push/mobile-onboarding-wf.md) to rapidly configure and test your mobile setup.

Detailed steps to configure push notifications are available on [this page](../../push/push-configuration.md).

### Implement code-based experiences (Mobile SDK)

Code-based experiences let you deliver personalized content to any surface in your native mobile app — from onboarding screens and product detail pages to in-app banners and feature flags — without requiring a new app release. Use the Mobile SDK to fetch and render personalized content at runtime, giving your team full control over placement and presentation:

* Follow [this tutorial](https://developer.adobe.com/client-sdks/edge/adobe-journey-optimizer/code-based/tutorial){target="_blank"} for Mobile SDK implementation
* Review sample implementations for [iOS](https://github.com/adobe/aepsdk-messaging-ios/tree/main/TestApps/MessagingDemoAppSwiftUI){target="_blank"} and [Android](https://github.com/adobe/aepsdk-messaging-android/tree/main/code/testapp){target="_blank"}

## Implement web experiences {#web-implementation}

### Set up the Adobe Experience Platform Web SDK

The Web SDK (`alloy.js`) is a single JavaScript library that replaces the patchwork of separate Adobe tags your site might otherwise need. It collects behavioral data, streams it to Adobe Experience Platform through a datastream you configure, and receives personalization instructions back — all in one network round-trip. Once it's in place, Journey Optimizer can identify visitors, trigger journeys from their actions, and deliver tailored content to your pages immediately.

1. **Install the Web SDK**: Follow the [Web SDK implementation guide](https://experienceleague.adobe.com/docs/platform-learn/implement-web-sdk/overview.html){target="_blank"} to set up the SDK on your website.

1. **Configure datastreams**: Create and configure a datastream in [!DNL Adobe Experience Platform Data Collection] with Journey Optimizer enabled. Learn more in the [datastreams documentation](https://experienceleague.adobe.com/docs/experience-platform/edge/datastreams/overview.html){target="_blank"}.

1. **Enable web push notifications** (optional): Web push notifications are now generally available. Configure the [pushNotifications property](https://experienceleague.adobe.com/en/docs/experience-platform/web-sdk/commands/configure/pushnotifications){target="_blank"} in your Web SDK configuration and use the [sendPushSubscription command](https://experienceleague.adobe.com/en/docs/experience-platform/web-sdk/commands/sendpushsubscription){target="_blank"} to register push subscriptions. [Learn about web push configuration](../../push/push-configuration-web.md).

### Implement code-based experiences (Web SDK)

Unlike visual channels where marketers control the layout entirely, code-based experiences give you full ownership of how personalized content is rendered on the page. Journey Optimizer returns a JSON payload with the personalization data; your code decides where and how to display it. This model works for any web surface — hero banners, recommendation carousels, search result rankings, A/B test variants — without needing a visual editor or page publishing workflow.

1. **Choose your implementation method**: Client-side, server-side, or hybrid. Review [implementation samples](../../code-based/code-based-implementation-samples.md) for each approach.

1. **Define surfaces**: Identify the locations in your application where you want to deliver personalized content. Learn about [surface configuration](../../code-based/code-based-surface.md).

1. **Implement content rendering**: Use the Web SDK to fetch and apply personalization content. See [code-based implementation tutorials](../../code-based/code-based-decisioning-implementations.md).

1. **Send display and interaction events**: Track when content is displayed and when users interact with it for analytics and optimization.

Explore [sample implementations on GitHub](https://github.com/adobe/alloy-samples/tree/main/ajo){target="_blank"} to see code-based experiences in action.

Learn more about [getting started with code-based experiences](../../code-based/get-started-code-based.md).

## Implement event streaming {#event-streaming}

### Send events to trigger journeys

Journeys run on events — a user logs in, adds an item to a cart, completes a purchase, abandons a form. Your job is to emit those events from your application at exactly the right moment. Each event is an XDM-structured JSON payload sent to the Experience Platform Streaming Ingestion API; Journey Optimizer picks it up within milliseconds and routes the profile into any matching journey. The event schema and payload structure are defined by your [Data Engineer](data-engineer.md) — coordinate with them before you start coding.

1. **Understand the event payload**: Work with your Data Engineer to get the event schema and required payload structure. The payload must conform to the XDM schema they've configured. Learn about [event schema requirements](../../event/experience-event-schema.md).

1. **Implement event streaming**: Send events to Adobe Experience Platform using the [Streaming Ingestion APIs](https://experienceleague.adobe.com/docs/experience-platform/ingestion/streaming/overview.html){target="_blank"}. Learn the [steps to send events](../../event/additional-steps-to-send-events-to-journey.md).

1. **Handle event types**:
   * **Unitary events**: Implement event sending for person-specific actions (e.g., button click, purchase completion)
   * **Business events**: Send business-related events (e.g., inventory updates, price changes)

1. **Test event delivery**: Verify that events are properly received and trigger journeys as expected. Learn about [event troubleshooting](../../building-journeys/troubleshooting-inbound.md).

**Example implementation** for sending an event via API:

```javascript
POST https://{DATACOLLECTION_ENDPOINT}/collection/{DATASTREAM_ID}
Content-Type: application/json

{
  "header": {
    "datasetId": "{DATASET_ID}",
    "imsOrgId": "{ORG_ID}",
    "source": {
      "name": "Web SDK"
    }
  },
  "body": {
    "xdmMeta": {
      "schemaRef": {
        "id": "{SCHEMA_ID}"
      }
    },
    "xdmEntity": {
      "_id": "unique-event-id",
      "eventType": "purchase",
      "timestamp": "2024-01-01T12:00:00Z",
      // ... your event data
    }
  }
}
```

Learn more about [working with journey events](../../event/about-events.md).

## Develop custom action endpoints {#custom-actions}

When a journey reaches a custom action step, Journey Optimizer makes an outbound HTTP call to a URL you provide — your backend, a CRM, a loyalty platform, any REST endpoint. Your job is to build and expose that endpoint: define the request contract (payload shape, authentication method, response format), implement the business logic behind it, and make sure it can handle the call volume Journey Optimizer will generate. Your [Administrator](administrator.md) then registers the endpoint in Journey Optimizer so marketers can use it as a step in their journeys.

1. **Build your API endpoint**: Create RESTful API endpoints that Journey Optimizer will call during journey execution. Your endpoint should:
   * Accept JSON payloads
   * Authenticate requests (OAuth, API key, or JWT)
   * Process requests within appropriate timeout limits
   * Return responses in expected format

1. **Understand custom action capabilities**: Custom actions can connect to third-party systems like Epsilon, Slack, Firebase, or your own services. Learn more about [custom actions](../../action/action.md).

1. **Work with action configurations**: Your [Administrator](administrator.md) or [Data Engineer](data-engineer.md) will configure the custom action in Journey Optimizer, defining the API endpoint URL, authentication method, and parameters. You'll provide them with your API specification. Learn about [custom action configuration](../../action/about-custom-action-configuration.md). You can define an optional **error response payload** for richer fallback logic in timeout/error branches.

1. **Return actionable data**: Design your API to return data that can be used in subsequent journey steps. Learn about [action responses](../../action/action-response.md).

1. **Monitor custom action health**: Use the custom action monitoring dashboard to track successful calls, errors, throughput, response times, and queue wait times. Learn about [custom action reporting](../../action/reporting.md).

1. **Implement rate limiting**: Ensure your endpoints can handle the expected volume. Journey Optimizer applies a 5000 calls/second limit, but your system should be resilient. Learn about [capping and throttling](../../configuration/external-systems.md).

**Example use case**: [Writing journey events to Experience Platform](../../building-journeys/custom-action-aep.md) using custom actions.

## Work with Journey Optimizer APIs {#apis}

Not everything needs to happen through the Journey Optimizer UI. Sometimes you need to trigger a campaign from your own backend, suppress an email address after a privacy request, or sync content templates from an external CMS. Journey Optimizer's REST APIs give you programmatic access to the platform's core capabilities. All calls use OAuth Server-to-Server authentication — the older JWT method is deprecated.

1. **Understand API capabilities**: Journey Optimizer APIs allow you to create, read, update, and delete various resources programmatically. Learn about [Journey Optimizer APIs](../../configuration/ajo-apis.md).

1. **Authentication**: Follow [this tutorial](https://developer.adobe.com/journey-optimizer-apis/references/authentication){target="_blank"} to set up API authentication using Adobe Developer Console.

1. **Explore API references**: Browse the complete API documentation and try APIs directly in the [Adobe Journey Optimizer API reference](https://developer.adobe.com/journey-optimizer-apis){target="_blank"}.

1. **API-triggered campaigns**: Build transactional messaging with API-triggered campaigns. For high-volume scenarios (up to 5000 TPS), explore [High Throughput mode](../../campaigns/api-triggered-high-throughput.md) (requires add-on license).

1. **Decision Management APIs**: Use specialized APIs for offer management and decisioning. Learn more in the [Decision Management API guide](../../offers/api-reference/getting-started.md).

1. **Decisioning migration APIs**: Programmatically migrate Decision Management entities to Decisioning with flexible scopes, automated validation, and rollback support. Learn more in the [Decisioning migration API guide](../../experience-decisioning/decisioning-migration-api.md).

1. **SMS Webhooks**: Configure inbound webhooks to capture incoming messages and feedback webhooks to receive delivery receipts and status updates. [Learn more](../../mobile/mobile-webhook.md).

## Testing and debugging {#testing}

Before your implementation goes live, you need confidence that events fire at the right moment, journeys trigger as expected, custom actions behave under realistic load, and personalized content renders correctly. This section covers the tools and techniques to catch issues early — from low-level SDK logging to end-to-end journey test runs with real profiles.

1. **Debug SDK implementation**: Use Adobe Experience Platform Assurance to inspect SDK events, validate data collection, and troubleshoot integration issues as they happen. [Learn more about Assurance](https://experienceleague.adobe.com/docs/experience-platform/assurance/home.html){target="_blank"}.

1. **Test event delivery**: Verify that events from your application are correctly received by Adobe Experience Platform and trigger journeys as expected. Monitor event ingestion and validate payload structure.

1. **Validate API integrations**: Test your custom action endpoints to ensure they handle Journey Optimizer requests correctly, respond within timeout limits, and return expected data formats.

1. **Use test mode with test profiles**: Work with your [Data Engineer](data-engineer.md) to get access to test profiles, then validate your implementation using journey test mode. Learn how to [test journeys](../../building-journeys/testing-the-journey.md).

1. **Monitor SDK logs**: Enable debug logging in your SDK implementation to troubleshoot issues during development:
   * **Mobile SDK**: Enable logging to see SDK events and API calls
   * **Web SDK**: Use browser console to monitor SDK activity
   
1. **Verify datastream configuration**: Ensure your datastream is correctly configured to send data to Journey Optimizer. Check that events flow through the datastream to the correct destinations.

1. **Query journey data for analysis**: Use SQL queries on the Data Lake to analyze journey step events, debug issues, and monitor custom action performance. Explore [query examples for journey analysis](../../reports/query-examples.md) including:
   * Profile entry/exit tracking and discard reasons
   * Custom action performance metrics (latency, throughput, errors)
   * Event delivery and error patterns
   * Journey instance states

## Advanced developer topics {#advanced-topics}

Once your core SDKs, events, and APIs are in place, these topics help you go further: enriching journey data at runtime without bloating the profile, handling consent signals so opt-outs propagate through every integration, and tuning your implementation for the throughput and reliability that production scale demands.

### Working with contextual data and enrichment

Journeys often need more data than what arrives in the triggering event — a product name, a loyalty tier, an order line-item list. Rather than pre-loading all of this into every profile, contextual enrichment lets your journey look it up at runtime from AEP datasets or carry it forward from a custom action response. Your messages and branch conditions can then reference that data without it ever being stored permanently on the profile.

* **Iterate over arrays**: Use Handlebars syntax to display dynamic lists from events, custom action responses, and dataset lookups in messages. Learn about [iterating contextual data](../../personalization/iterate-contextual-data.md).
* **Dataset lookup**: Implement dataset lookups to enrich journey data from Adobe Experience Platform datasets. Work with your Data Engineer on configuration. Learn about [dataset lookup](../../building-journeys/dataset-lookup.md).

### Working with consent and governance

Journey Optimizer enforces data governance and consent policies at the platform level, but your integration needs to respect them too. When a customer opts out of marketing communications, or when a data usage label restricts how a field can be used, those rules need to propagate through your custom actions and dataset lookups — not just block actions in the UI.

* **Data governance**: Apply data usage policies to custom actions. Learn more about [data governance](../../action/action-privacy.md).
* **Consent management**: Handle customer consent preferences in your implementations. Learn about [consent](../../action/consent.md).

### Optimization and best practices

Production Journey Optimizer implementations regularly handle millions of events and thousands of journey executions per second. These resources help you tune your integration for that scale — understanding rate limits before you hit them, avoiding common journey design pitfalls that silently drop profiles, and building error handling that degrades gracefully rather than failing opaquely.

* **Capping and throttling**: Understand rate limits and implement appropriate throttling. Learn about [external systems](../../configuration/external-systems.md).
* **Journey optimization**: Follow best practices for [journey optimization](../../building-journeys/optimize.md).
* **Error handling**: Implement robust error handling. Review [error codes](../../building-journeys/error-codes-reference.md) and [troubleshooting guides](../../building-journeys/troubleshooting.md).

## Call Journey Optimizer REST APIs {#rest-apis}

Beyond implementing SDKs and event streaming, you can also drive Journey Optimizer programmatically from your own systems. The full API reference, OpenAPI specs, and code samples are on the [Journey Optimizer developer portal](https://developer.adobe.com/journey-optimizer-apis){target="_blank"}.

>[!NOTE]
>
>All integrations must use OAuth Server-to-Server authentication — the JWT method is deprecated. [Set up authentication](https://developer.adobe.com/journey-optimizer-apis/references/authentication){target="_blank"}

### Execute API-triggered campaigns {#api-triggered}

Trigger transactional or marketing messages from an external system using the Interactive Message Execution REST API. Before calling the endpoint:

* The campaign must be **activated** before the endpoint accepts calls.
* Calls have a **timeout of 60 seconds**; internal retries handle unexpected timeouts.
* If campaign start/end dates are configured, API calls outside those dates will fail.
* To build your payload, retrieve the generated sample cURL request from the **cURL request** section of your live campaign in the Journey Optimizer UI — it includes all personalization variables for that campaign.
* Standard and [high-throughput campaigns](../../campaigns/api-triggered-high-throughput.md) use different endpoints.

[API reference](https://developer.adobe.com/journey-optimizer-apis/references/messaging){target="_blank"} · [Code samples](https://developer.adobe.com/journey-optimizer-apis/references/messaging-samples){target="_blank"} · [Work with API-triggered campaigns](../../campaigns/api-triggered-campaigns.md)

### Capping and throttling for external endpoints {#capping-throttling}

When journeys call external systems via custom actions or data sources, the Capping and Throttling APIs protect those systems from overload. Capping rejects calls that exceed the configured limit; throttling queues them for up to 6 hours (production sandboxes, custom actions only).

[Capping API reference](https://developer.adobe.com/journey-optimizer-apis/references/journeys-throttling){target="_blank"} · [Work with the Capping API](../../configuration/capping.md) · [Work with the Throttling API](../../configuration/throttling.md)

### More REST APIs {#more-rest-apis}

Beyond messaging and capping, Journey Optimizer exposes REST endpoints for suppression management, content templating, campaign retrieval, proofing, and orchestrated campaign execution. Use these when you need to automate operations that would otherwise require manual steps in the UI — for example, bulk-suppressing addresses after a data pull, or syncing templates from an external content pipeline.

| What you need to do | API reference |
| ------------------- | ------------- |
| Programmatically exclude email addresses or domains from sending | [Suppression API](https://developer.adobe.com/journey-optimizer-apis/references/suppression){target="_blank"} · [Manage the suppression list](../../configuration/manage-suppression-list.md) |
| Retrieve journey metadata for auditing or external sync | [Journeys API](https://developer.adobe.com/journey-optimizer-apis/references/journeys-retrieve){target="_blank"} |
| Create and manage content templates and fragments from an external pipeline | [Content API](https://developer.adobe.com/journey-optimizer-apis/references/content){target="_blank"} · [Templates](../../content-management/content-templates.md) · [Fragments](../../content-management/fragments.md) |
| Retrieve and filter Action campaigns | [Campaigns API](https://developer.adobe.com/journey-optimizer-apis/references/campaigns-retrieve){target="_blank"} |
| Preview campaigns and send proofs programmatically | [Simulations API](https://developer.adobe.com/journey-optimizer-apis/references/simulations){target="_blank"} |
| Validate datasets and trigger Orchestrated campaign execution | [Dataset validation](https://developer.adobe.com/journey-optimizer-apis/references/orchestrated-campaign-dataset){target="_blank"} · [Trigger](https://developer.adobe.com/journey-optimizer-apis/references/oc-trigger){target="_blank"} · [Enable datasets](../../orchestrated/manual-schema.md) |

## Additional resources {#additional-resources}

* **Developer Console**: Access the [Adobe Developer Console](https://developer.adobe.com){target="_blank"} to create integrations and manage API credentials.
* **Sample code**: Explore [sample implementations on GitHub](https://github.com/adobe/alloy-samples/tree/main/ajo){target="_blank"}.
* **Tutorial videos**: Learn through hands-on tutorials on [Experience League](https://experienceleague.adobe.com/docs/journey-optimizer-learn/tutorials/overview.html){target="_blank"}.
* **Developer community**: Connect with other developers and get support in the Adobe community forums.

## Collaborate across roles {#next-steps}

Your implementation work intersects with other team members:

>[!BEGINTABS]

>[!TAB Work with Data Engineers]

Collaborate with [Data Engineers](data-engineer.md) on data and event configurations. Every journey that reacts to user behavior depends on events you send — the Data Engineer defines the schemas, you implement the code that produces them.

* Get the [XDM schemas](../../data/get-started-schemas.md) and event structures you need to implement
* Understand which events you need to send and their required payload format — see [working with journey events](../../event/about-events.md)
* Confirm which fields are required vs. optional in each event payload, and what happens in journeys when expected fields are missing or malformed — see [schema requirements](../../event/experience-event-schema.md#schema-requirements)
* Test event delivery and data ingestion together using [Adobe Experience Platform Assurance](https://experienceleague.adobe.com/docs/experience-platform/assurance/home.html){target="_blank"}

>[!TAB Work with Administrators]

Collaborate with [Administrators](administrator.md) on access and channel configurations. Journeys can only reach users through channels the Administrator has set up — coordinate early so your SDK work and their configuration stay in sync.

* Provide API specifications for [custom actions](../../action/about-custom-action-configuration.md) they'll configure in Journey Optimizer
* Request necessary permissions and API credentials via [Adobe Developer Console](https://developer.adobe.com){target="_blank"}
* Coordinate on channel configuration requirements — push certificates for [iOS](../../push/push-configuration.md) and Android, [web push](../../push/push-configuration-web.md) settings, [SMS webhook](../../mobile/mobile-webhook.md) endpoints
* Align on sandbox strategy and testing environments before running [journey test mode](../../building-journeys/testing-the-journey.md)

>[!TAB Work with Marketers]

Collaborate with [Marketers](marketer.md) on journey design and testing. Marketers build the journeys and content that depend entirely on the events you send and the surfaces you expose — the closer you align, the faster journeys go live.

* Review journey designs in [Journey Optimizer](../../building-journeys/journey.md) together to understand which user interactions must trigger events and which surfaces need personalization
* Implement tracking so Marketers can measure [content performance and user engagement](../../reports/report-gs-cja.md)
* Run [journey test mode](../../building-journeys/testing-the-journey.md) together using test profiles to validate the full flow end-to-end
* Troubleshoot issues with message delivery, personalization rendering, or [custom action](../../action/action.md) responses

>[!ENDTABS]

## Start implementing

Ready to start building? Choose your first implementation area from the sections above:

1. **Mobile app?** Start with [Mobile SDK integration](#mobile-integration)
2. **Website?** Begin with [Web SDK setup](#web-implementation)  
3. **API integration?** Jump to [Working with APIs](#apis)
4. **Custom system?** Check out [Custom actions](#custom-actions)

Each section includes links to detailed technical documentation, code samples, and tutorials to guide your implementation.

## Other role guides {#other-role-guides}

| Role | Guide |
|------|-------|
| Administrator | [Get started for administrators](administrator.md) |
| Data Engineer | [Get started for data engineers](data-engineer.md) |
| Developer | [Get started for developers](developer.md) |
| Marketer | [Get started for marketers](marketer.md) |

Back to [Roles and responsibilities overview](../quick-start.md) · Back to [Get started](../../../rp_landing_pages/get-started-landing-page.md)
