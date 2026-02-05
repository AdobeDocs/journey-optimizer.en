---
solution: Journey Optimizer
product: journey optimizer
title: FAQ
description: Live activity FAQ
topic: Content Management
role: User
level: Beginner
hide: yes
hidefromtoc: yes
exl-id: e7e994ca-aa0c-4e86-8710-c87430b74188
---
# Frequently asked questions {#mobile-live-faq}

>[!BEGINSHADEBOX]

* [Get started with Live activity](get-started-mobile-live.md)
* [Live activity configuration](mobile-live-configuration.md)
* [Live Activity integration with Adobe Experience Platform Mobile SDK](mobile-live-configuration-sdk.md)
* [Create a Live activity](create-mobile-live.md)
* **[Frequently asked questions](mobile-live-faq.md)**
* [Live activity campaign report](../reports/campaign-global-report-cja-activity.md)

>[!ENDSHADEBOX]

## General Questions

+++What is the difference between a Live Activity and a push notification?

Live Activities provide persistent, real-time updates on the Lock Screen and Dynamic Island without requiring users to unlock their device. Push notifications are temporary alerts that disappear once dismissed. Live Activities stay visible and can be updated multiple times until explicitly ended.

+++

+++How many Live Activities can be active at once?

An iOS app can run multiple Live Activities simultaneously, including several that use the same `ActivityAttributes` type.

There is no hard limit imposed by developers on how many Live Activities of a given attribute type can exist. You can start as many as your app logic requires, for instance, one per ongoing delivery or ride. However, iOS enforces a system-level limit on how many Live Activities can be active or visible at once.

In practice:

* iOS typically supports up to about five concurrent Live Activities per app.

* If you exceed this number, the system may stop displaying some activities or terminate older ones to conserve resources.

* Each Live Activity has a unique `Activity.id`, which lets you update or end it individually.

+++

+++Do users need to have the app open to receive Live Activity updates?

No. Live Activities can be started, updated, and ended remotely even when the app is completely closed, one of the key benefits of the feature.

+++

+++What iOS versions support Live Activities?

* iOS 16.1+: Basic Live Activity support
* iOS 17.2+: Push-to-start functionality (remotely start without opening the app)
* iOS 18+: Broadcast channel support for audience-based Live Activities
+++

+++How long can a Live Activity remain active?

Apple limits Live Activities to **8 hours of active updates**. After that, the system automatically ends the activity, though it may remain visible in a static state for up to **12 additional hours** before removal. You can also end a Live Activity sooner by setting a `dismissalDate` or explicitly calling `activity.end()` in your app.

+++

### Developer Questions

+++Do I need to create a separate widget extension for Live Activities?

Yes. Live Activities are displayed through WidgetKit, so you need to create a widget extension in your Xcode project and implement the `ActivityConfiguration`.
[Learn more about Widget configuration](mobile-live-configuration-sdk.md)

+++

+++Can I use the same `LiveActivityAttributes` class for both local and remote Live Activities?

Yes. The same attributes class works for both locally-started and remotely-started (push-to-start) Live Activities. You need to ensure you register it with `Messaging.registerLiveActivity()`.

+++

+++What happens if I send an update for a Live Activity that does not exist?

If you send an update or end event for a non-existent `liveActivityID` or `channelID`, the request will fail silently on the device. Always ensure you are tracking which Live Activities are active for each user.

+++

+++Can I test Live Activities in the iOS Simulator?

Yes, you can test locally-started as well as remotely-started Live Activities in the iOS Simulator.

* **Local**: This includes creating, updating, and ending Live Activities directly from your app using **ActivityKit APIs**.

* **Remote**: To test Live Activity functionality remotely, integrate our Messaging SDK into your app and use the provided execution APIs to send remote start, update and end to your test device or iOS Simulator. Similar to how push notifications can be tested currently with Adobe SDKs integration.

+++

+++How do I handle updates when the app is in the background?

The SDK handles this automatically. Once registered, Live Activities receive updates even when the app is terminated. No additional background modes are required.
+++

+++What is the difference between `liveActivityID` and `channelID`?

* `liveActivityID`: Used for individual (unitary) Live Activities targeted at specific users. Each ID represents a unique Live Activity instance.
* `channelID`: Used for broadcast Live Activities sent to audiences. All users in the audience receive the same updates on the same channel.
+++

+++Can I customize the Dynamic Island appearance separately from the Lock Screen?

Yes. The `ActivityConfiguration` has separate closures for Lock Screen content and Dynamic Island content (expanded, compact, and minimal states), each design independently.
+++

+++Do I need to store push tokens manually?

No. When you register a Live Activity type with `Messaging.registerLiveActivity()`, the SDK automatically collects and manages push tokens for you.
+++

### Marketer Questions

+++Can I personalize Live Activity content for each user in a broadcast campaign?

Broadcast campaigns send the same content to all users in the audience. For personalized content, use unitary (transactional) campaigns targeting individual users.
+++

+++How do I know if my Live Activity was successfully delivered?

[Monitor your campaign analytics](../reports/campaign-global-report-cja-activity.md) in Adobe Journey Optimizer. You can track delivery rates, failures, and engagement metrics. Also consider implementing custom analytics events in your app.
+++

+++Can I schedule Live Activities in advance?

The API call triggers the Live Activity immediately. However, you can schedule your API calls through your backend systems or use Journey Optimizer's orchestration capabilities to time them appropriately.
+++

+++What happens if I send a "start" event for a Live Activity that already exists?

When remotely starting Live Activities through Adobe’s Execution APIs:

* You can include an `x-request-id` header in your request. Ideally, there should be a one-to-one relationship between each `liveActivityID` and its corresponding `x-request-id`. This ensures that if multiple requests are made with the same `x-request-id` and `liveActivityID` combination, only one Live Activity will be started on the device, and duplicate requests will be ignored.

* If the `x-request-id` header is omitted, each request is treated independently, which can result in multiple Live Activities being created with the same `liveActivityID`. In such cases, future updates may fail or apply to only one of the active instances.

* The `x-request-id` value should not be reused across different `liveActivityIDs` in separate API requests.

+++

+++Can I A/B test different Live Activity experiences?

Yes. Create multiple campaigns with different content structures and use Adobe Journey Optimizer's experimentation features to test which performs better. Ensure your app supports all content state variations.

+++

+++How often should I update a Live Activity?

Update only when meaningful information changes since too-frequent updates can drain battery and reduce user experience quality. For real-time scenarios, such as delivery tracking, every 30-60 seconds is typically acceptable. For slower-changing content, such as sports scores, update on significant events only.

+++

+++Can I target users based on whether they have Live Activities enabled?

You will need to work with your development team to track and pass this preference to Adobe Experience Platform as a user attribute, then segment based on that attribute.

+++

### API Questions

+++What's the difference between `timestamp` and `dismissal-date`?

* `timestamp`: The current epoch time when the event occurs, required for all events.
* `dismissal-date`: A future epoch time when the Live Activity should auto-dismiss, required only for "end" events.

+++

+++Do I need to send all `attributes` fields in every update call?

Yes, based on you `LiveActivityAttribute` class.

* All fields from your attributes object, including `liveActivityData` should be included in every call, for start, updates or end.
* Only the `content-state` fields represent what actually changes dynamically on a running live activity.
* Include an alert object as well, it ensures that the push is treated as a user-visible notification, not as a silent background one. Required only for 'start' cases and otherwise optional.

+++

+++What format should epoch timestamps be in?

Use Unix epoch time in **seconds** not milliseconds. For example: `1759937682`

+++

+++Can I use the same `requestId` for multiple API calls?

No. Each API request should have a unique `requestId` to ensure idempotency and proper tracking. Use UUIDs or similar unique identifiers.

+++

+++What authentication is required for the Headless API?

Refer to the [API Triggered Campaigns Documentation](https://developer.adobe.com/journey-optimizer-apis/references/messaging/) for authentication requirements, including OAuth tokens and API keys.

+++

+++What happens if my API call fails?

Implement retry logic with exponential backoff. Check the API response for error codes and messages to diagnose issues. Common failures include invalid campaign IDs, malformed payloads, or authentication issues.

+++

+++Can I send Live Activity updates from my own backend servers?

Yes, that is the intended behavior. Your backend calls the Adobe Journey Optimizer Headless API to trigger Live Activity events when your business logic requires it.

+++

+++Do I need a different campaign for start, update, and end events?

No. You can use the same campaign and change the `event` field in the payload. However, some organizations prefer separate campaigns for better analytics tracking.

+++

### Troubleshooting Questions

+++My Live Activity starts but does not update. What could be the issue?

Common causes:

* Mismatched `liveActivityID` or `channelID` between start and update calls.
* `content-state` fields don't match your `ContentState` struct.
* The Live Activity has already ended.
* Network connectivity issues on the device.

+++

+++The `attributes-type` field is not being recognized. What should I check?

* Ensure the class name matches **exactly** (case-sensitive) with your Swift struct name
* Verify the struct is properly defined and registered
* Check for typos in the JSON payload
* Confirm the app version installed has the Live Activity implementation

+++

+++Users only see the Live Activity update and not the alert notification, is this a known issue?

No. The `alert` field is optional and may be suppressed by iOS in certain conditions, for example Do Not Disturb mode. Live Activities can update silently, which is often the intended behavior. The alert field is mandatory for sending remote starts otherwise apple treats it like a silent background notification.

+++

+++Can I delete or clear all Live Activities for a user?

You need to send an "end" event for each active Live Activity. Track which Live Activities are active for each user in your systems so you can properly clean them up.

+++

+++My widget shows “No data” even though I sent an update. What could be the issue?

* Verify your widget implementation properly accesses `context.state` and `context.attributes`.
* Check that default values or error states are handled in your widget interface.
* Use the `LiveActivityAssuranceDebuggable` protocol to debug the schema.
* Test with Adobe Assurance to see if data is being received.
+++
