---
title: Get Started for Developers
description: As a Developer, learn more how to work with Journey Optimizer
feature: Get Started
role: Developer
level: Experienced
exl-id: 5053dd4f-d050-415f-bc74-d6d061bdcbe1
---
# Get Started for Developers {#get-started-developers}

As a **Developer**, you are responsible for implementing and integrating [!DNL Adobe Journey Optimizer] into your applications and systems. You can start working with [!DNL Adobe Journey Optimizer] once the [System Administrator](administrator.md) and the [Data Engineer](data-engineer.md) have granted you access and prepared your environment.

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

1. **Authentication and security**: All implementations require proper authentication. Understand how to set up authentication for SDKs and APIs. Learn about [API authentication](https://developer.adobe.com/journey-optimizer-apis/references/authentication/){target="_blank"}.

## Set up mobile app integrations {#mobile-integration}

### Configure the Adobe Experience Platform Mobile SDK

To enable push notifications, in-app messages, and other mobile capabilities, integrate the Adobe Experience Platform Mobile SDK into your mobile applications.

1. **Install and configure the Mobile SDK**: Follow the [Adobe Experience Platform Mobile SDK documentation](https://developer.adobe.com/client-sdks/documentation/getting-started/){target="_blank"} to get started with SDK integration.

1. **Create a mobile property**: Set up a mobile property in [!DNL Adobe Experience Platform Data Collection]. Learn how to [create and configure a mobile property](https://developer.adobe.com/client-sdks/documentation/getting-started/create-a-mobile-property/){target="_blank"}.

1. **Configure push notifications**: 
   * For **iOS apps**: Register your app with APNs (Apple Push Notification service). Learn more in [Apple's documentation](https://developer.apple.com/documentation/usernotifications/registering_your_app_with_apns){target="_blank"}.
   * For **Android apps**: Set up Firebase Cloud Messaging for your Android app. Learn more in [Google's documentation](https://firebase.google.com/docs/cloud-messaging/android/client){target="_blank"}.

1. **Test your mobile integration**: Use the [mobile onboarding quick start workflow](../../push/mobile-onboarding-wf.md) to rapidly configure and test your mobile setup.

Detailed steps to configure push notifications are available on [this page](../../push/push-configuration.md).

### Implement code-based experiences (Mobile SDK)

For native mobile app personalization using code-based experiences:

* Follow [this tutorial](https://developer.adobe.com/client-sdks/edge/adobe-journey-optimizer/code-based/tutorial/){target="_blank"} for Mobile SDK implementation
* Review sample implementations for [iOS](https://github.com/adobe/aepsdk-messaging-ios/tree/main/TestApps/MessagingDemoAppSwiftUI){target="_blank"} and [Android](https://github.com/adobe/aepsdk-messaging-android/tree/main/code/testapp){target="_blank"}

## Implement web experiences {#web-implementation}

### Set up the Adobe Experience Platform Web SDK

For web-based implementations, the Web SDK is your primary integration point:

1. **Install the Web SDK**: Follow the [Web SDK implementation guide](https://experienceleague.adobe.com/docs/platform-learn/implement-web-sdk/overview.html){target="_blank"} to set up the SDK on your website.

1. **Configure datastreams**: Create and configure a datastream in [!DNL Adobe Experience Platform Data Collection] with Journey Optimizer enabled. Learn more in the [datastreams documentation](https://experienceleague.adobe.com/docs/experience-platform/edge/datastreams/overview.html){target="_blank"}.

1. **Enable web push notifications** (optional): Configure the [pushNotifications property](https://experienceleague.adobe.com/en/docs/experience-platform/web-sdk/commands/configure/pushnotifications){target="_blank"} in your Web SDK configuration and use the [sendPushSubscription command](https://experienceleague.adobe.com/en/docs/experience-platform/web-sdk/commands/sendpushsubscription){target="_blank"} to register push subscriptions.

### Implement code-based experiences (Web SDK)

Code-based experiences allow you to personalize any digital touchpoint:

1. **Choose your implementation method**: Client-side, server-side, or hybrid. Review [implementation samples](../../code-based/code-based-implementation-samples.md) for each approach.

1. **Define surfaces**: Identify the locations in your application where you want to deliver personalized content. Learn about [surface configuration](../../code-based/code-based-surface.md).

1. **Implement content rendering**: Use the Web SDK to fetch and apply personalization content. See [code-based implementation tutorials](../../code-based/code-based-decisioning-implementations.md).

1. **Send display and interaction events**: Track when content is displayed and when users interact with it for analytics and optimization.

Explore [sample implementations on GitHub](https://github.com/adobe/alloy-samples/tree/main/ajo){target="_blank"} to see code-based experiences in action.

Learn more about [getting started with code-based experiences](../../code-based/get-started-code-based.md).

## Implement event streaming {#event-streaming}

### Send events to trigger journeys

As a developer, you'll implement the code to send events that trigger journeys. Your [Data Engineer](data-engineer.md) will configure the event schemas and definitions in Journey Optimizer.

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

Custom actions allow journeys to call your APIs. As a developer, you'll build the API endpoints that custom actions invoke:

1. **Build your API endpoint**: Create RESTful API endpoints that Journey Optimizer will call during journey execution. Your endpoint should:
   * Accept JSON payloads
   * Authenticate requests (OAuth, API key, or JWT)
   * Process requests within appropriate timeout limits
   * Return responses in expected format

1. **Understand custom action capabilities**: Custom actions can connect to third-party systems like Epsilon, Slack, Firebase, or your own services. Learn more about [custom actions](../../action/action.md).

1. **Work with action configurations**: Your [Administrator](administrator.md) or [Data Engineer](data-engineer.md) will configure the custom action in Journey Optimizer, defining the API endpoint URL, authentication method, and parameters. You'll provide them with your API specification. Learn about [custom action configuration](../../action/about-custom-action-configuration.md).

1. **Return actionable data**: Design your API to return data that can be used in subsequent journey steps. Learn about [action responses](../../action/action-response.md).

1. **Implement rate limiting**: Ensure your endpoints can handle the expected volume. Journey Optimizer applies a 5000 calls/second limit, but your system should be resilient. Learn about [capping and throttling](../../configuration/external-systems.md).

**Example use case**: [Writing journey events to Experience Platform](../../building-journeys/custom-action-aep.md) using custom actions.

## Work with Journey Optimizer APIs {#apis}

Journey Optimizer provides comprehensive REST APIs for programmatic access:

1. **Understand API capabilities**: Journey Optimizer APIs allow you to create, read, update, and delete various resources programmatically. Learn about [Journey Optimizer APIs](../../configuration/ajo-apis.md).

1. **Authentication**: Follow [this tutorial](https://developer.adobe.com/journey-optimizer-apis/references/authentication/){target="_blank"} to set up API authentication using Adobe Developer Console.

1. **Explore API references**: Browse the complete API documentation and try APIs directly in the [Adobe Journey Optimizer API reference](https://developer.adobe.com/journey-optimizer-apis/){target="_blank"}.

1. **API-triggered campaigns**: Build transactional messaging with API-triggered campaigns. For high-volume scenarios (up to 5000 TPS), explore [High Throughput mode](../../campaigns/api-triggered-high-throughput.md) (requires add-on license).

1. **Decision Management APIs**: Use specialized APIs for offer management and decisioning. Learn more in the [Decision Management API guide](../../offers/api-reference/getting-started.md).

## Testing and debugging {#testing}

1. **Debug SDK implementation**: Use Adobe Experience Platform Assurance to inspect SDK events, validate data collection, and troubleshoot integration issues in real-time. [Learn more about Assurance](https://experienceleague.adobe.com/docs/experience-platform/assurance/home.html){target="_blank"}.

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

### Working with contextual data and enrichment

* **Iterate over arrays**: Use Handlebars syntax to display dynamic lists from events, custom action responses, and dataset lookups in messages. Learn about [iterating contextual data](../../personalization/iterate-contextual-data.md).
* **Dataset lookup**: Implement dataset lookups to enrich journey data from Adobe Experience Platform datasets. Work with your Data Engineer on configuration. Learn about [dataset lookup](../../building-journeys/dataset-lookup.md).

### Working with consent and governance

Implement data governance and consent policies in your integrations:

* **Data governance**: Apply data usage policies to custom actions. Learn more about [data governance](../../action/action-privacy.md).
* **Consent management**: Handle customer consent preferences in your implementations. Learn about [consent](../../action/consent.md).

### Optimization and best practices

* **Capping and throttling**: Understand rate limits and implement appropriate throttling. Learn about [external systems](../../configuration/external-systems.md).
* **Journey optimization**: Follow best practices for [journey optimization](../../building-journeys/optimize.md).
* **Error handling**: Implement robust error handling. Review [error codes](../../building-journeys/error-codes-reference.md) and [troubleshooting guides](../../building-journeys/troubleshooting.md).

## Additional resources {#additional-resources}

* **Developer Console**: Access the [Adobe Developer Console](https://developer.adobe.com){target="_blank"} to create integrations and manage API credentials.
* **Sample code**: Explore [sample implementations on GitHub](https://github.com/adobe/alloy-samples/tree/main/ajo){target="_blank"}.
* **Tutorial videos**: Learn through hands-on tutorials on [Experience League](https://experienceleague.adobe.com/docs/journey-optimizer-learn/tutorials/overview.html){target="_blank"}.
* **Developer community**: Connect with other developers and get support in the Adobe community forums.

## Collaborate across roles {#next-steps}

Your implementation work intersects with other team members:

>[!BEGINTABS]

>[!TAB Work with Data Engineers]

Collaborate with [Data Engineers](data-engineer.md) on data and event configurations:

* Get the XDM schemas and event structures you need to implement
* Understand which events you need to send and their required payload format
* Align on data collection requirements and data quality standards
* Test event delivery and data ingestion together

>[!TAB Work with Administrators]

Collaborate with [Administrators](administrator.md) on access and configurations:

* Provide API specifications for custom actions they'll configure
* Request necessary permissions and API credentials
* Coordinate on channel configuration requirements (e.g., push certificates)
* Align on testing environments and sandbox strategy

>[!TAB Work with Marketers]

Collaborate with [Marketers](marketer.md) on journey requirements and testing:

* Understand which user interactions should trigger events
* Implement tracking for content performance and user engagement
* Support testing of journeys with your implemented features
* Troubleshoot issues with message delivery or personalization

>[!ENDTABS]

## Stay updated

Keep up with the latest Journey Optimizer capabilities and technical changes:

* **[Release Notes](../../rn/release-notes.md)**: Review new features, API changes, SDK updates, and bug fixes released each month
* **[Documentation Updates](../../rn/documentation-updates.md)**: Track recent changes to technical documentation including new implementation guides and code examples
* **[Product Notifications](../../rn/releases.md#staying-informed)**: Learn how to subscribe to email and in-product alerts for Journey Optimizer updates, including new SDK versions, API changes, breaking changes, and critical security updates

## Start implementing

Ready to start building? Choose your first implementation area from the sections above:

1. **Mobile app?** Start with [Mobile SDK integration](#mobile-integration)
2. **Website?** Begin with [Web SDK setup](#web-implementation)  
3. **API integration?** Jump to [Working with APIs](#apis)
4. **Custom system?** Check out [Custom actions](#custom-actions)

Each section includes links to detailed technical documentation, code samples, and tutorials to guide your implementation.
