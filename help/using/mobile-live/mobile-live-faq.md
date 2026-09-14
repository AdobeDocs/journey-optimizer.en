---
solution: Journey Optimizer
product: journey optimizer
title: FAQ
description: Live activities FAQ
topic: Content Management
role: User
level: Beginner
exl-id: e7e994ca-aa0c-4e86-8710-c87430b74188
TQID: https://experienceleague.adobe.com/gV4buzcc5mqsvceDj1O-5XZ3eJHtfD26h1c5g3h81Ps
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: d0a62d3c-b79e-47e4-929e-40ef3cffa037
    internal-label: Communication channels
  - id: a984631b-2bae-4860-9b15-69c41a799dcb
    internal-label: APIs and SDKs
  - id: b3538224-471e-4c63-a444-9b19d89ae29c
    internal-label: Activities
subfeature_v2:
  - id: c96d2aa5-76a2-443d-8d23-5de95577c909
    internal-label: Mobile SDK
  - id: ed2fba79-65cb-4680-96d2-2ad5d851714d
    internal-label: Live activities
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
level_v2:
  - id: e8ccd51f-da0d-4e3b-939b-e30d5ebb1ea5
    internal-label: Beginner
topic_v2:
  - id: aa2f3246-cb95-4b30-8899-fdf7d73550cc
    internal-label: Reporting
  - id: b5ce8718-c3af-4fdb-a1a9-fca32f83a87c
    internal-label: Implementation
  - id: bcc5edb5-84c3-4940-9f84-ed88b6c16274
    internal-label: Experimentation
  - id: c1579802-ddd4-4214-8a91-97b2066abe11
    internal-label: Troubleshooting
  - id: ce44533e-8ec8-4e11-a9e9-78b0fe561832
    internal-label: Content structure
---
# Frequently asked questions {#mobile-live-faq}

>[!BEGINSHADEBOX]

**On this page:** Find answers to common questions about Live activities so you can implement, deliver, and troubleshoot them more confidently across your iOS apps and campaigns.

>[!ENDSHADEBOX]

## General Questions

+++What is the difference between a Live activity and a Push notification?

A Live Update is a persistent, continuously-updating notification (delivery status, live scores, ride/ETA, etc.) that stays on the Lock Screen, in the notification shade, or as a status-bar chip, and refreshes in place without the user reopening the app. A regular push notification is a one-shot alert that disappears once dismissed. 

On iOS, this is implemented as a Live Activity. On Android, it is a promoted ongoing notification.

+++

+++How does an Android Live Update relate to an iOS Live Activity?

They are the same product concept in Journey Optimizer and use the same Headless API and campaign model. iOS renders a system widget, Android renders an ongoing notification from an FCM data message. You author campaigns the same way, only the payload block and the app-side rendering differ.
+++

+++How many Live activity instances can be active at once?

An iOS app can run multiple Live activity instances simultaneously, including several that use the same `ActivityAttributes` type.

There is no hard limit imposed by developers on how many Live activity instances of a given attribute type can exist. You can start as many as your app logic requires, for instance, one per ongoing delivery or ride. However, iOS enforces a system-level limit on how many Live activity instances can be active or visible at once.

In practice:

* iOS typically supports up to about five concurrent Live activity instances per app.

* If you exceed this number, the system may stop displaying some activity instances or terminate older ones to conserve resources.

* Each Live activity instance has a unique `Activity.id`, which lets you update or end it individually.

Android has no equivalent to iOS's ~5-instance cap. Each Android Live Update is an ongoing notification your app manages directly. A broadcast Android Live Update is a single channel that many devices subscribe to. In practice, limits come from how many notifications you want visible to users and your own tracking, not a hard OS ceiling.

+++

+++Do users need to have the app open to receive Live activity updates?

No. Start, update, and end are delivered remotely and work with the app in the background or closed. On Android, the FCM data message wakes your app briefly to (re)post the notification on each update, so Android delivery is sensitive to battery optimization / Doze.

+++

+++What iOS versions support Live activities?

* iOS 16.1+: Basic Live activities support
* iOS 17.2+: Push-to-start functionality (remotely start without opening the app)
* iOS 18+: Broadcast channel support for audience-based Live activities
+++

+++ Which Android versions are supported? 

Native Android Live Updates require Android 16. On earlier Android versions, the same campaign falls back to a standard ongoing notification, which your app posts and updates from the FCM data message. You will also need a Mobile SDK version that supports Android Live Update handling.

+++

+++How long can a Live activity remain active?

Apple limits Live activity to **8 hours of active updates**. After that, the system automatically ends the activity, though it may remain visible in a static state for up to **12 additional hours** before removal. You can also end a Live activity sooner by setting a `dismissalDate` or explicitly calling `activity.end()` in your app.

Android has no fixed 8-hour expiry like iOS. An ongoing notification stays active until your app sends an end event or the app/user dismisses it, subject to FCM delivery and device battery/Doze behavior.

+++

+++ What are the rate limits?

Campaigns have a default rate limit of 500 transactional messages per second across all channels, including iOS Live activities. This limit applies to all channels combined, and there is no separate rate limit specifically for iOS Live activities or Android Live updates.

+++

+++ Where does an Android Live Update appear?

Android has no equivalent to Dynamic Island. Instead, an Android Live Update surfaces in the notification shade, as a status-bar chip, and, on supported devices running the Android 16 progress style, on the Always-On Display. Its appearance is defined by your app's notification, not by a separate widget extension.

+++

+++ Can a single campaign target both iOS and Android?

No. A Live Update channel configuration targets a single platform, so iOS and Android are always set up as separate campaigns, each with its own channel configuration, this applies to both unitary and broadcast. You need to create one campaign for iOS and one for Android.

+++

### Developer Questions

+++ What do I need to build in the Android app? 

There is no widget extension, this is exclusive to iOS. Instead, you implement an ongoing notification, using the Android 16 promoted/progress style where availablee, plus a service that receives the FCM data message and posts, updates, or cancels the notification. Register Android Live Update handling with the Mobile SDK so tokens are collected and events are tracked.

Requirements:

* Your app must target API level 36.
* Your Android manifest must declare the `POST_PROMOTED_NOTIFICATION` permission.
* The Android Live Update notification must use one of the following styles: Standard, BigTextStyle, CallStyle, ProgressStyle, or MetricStyle (Android 37).
+++

+++Do I need to create a separate widget extension for Live activities?

Yes. Live activities are displayed through WidgetKit, so you need to create a widget extension in your Xcode project and implement the `ActivityConfiguration`.
[Learn more about Widget configuration](mobile-live-configuration-sdk.md)

+++

+++ Do I need a foreground service and notification permission? 

Yes. You need the runtime `POST_NOTIFICATIONS` permission (Android 13+), and, depending on how you keep the notification alive, an appropriately declared service. Refer to the [SDK's Android Live Updates guidance](https://developer.android.com/design/ui/mobile/guides/home-screen/live-updates) for the exact service type and foreground-service requirements.
+++

+++ Does my app code run on every update? How does Doze/battery optimization affect it?

On Android, yes: each update is an FCM data message that wakes your service to re-post the notification. On iOS, the system handles this and your app code never runs. As a result, Android updates are subject to battery optimization, Doze, and manufacturer-specific restrictions, which can delay or drop them. Use high-priority delivery for time-sensitive updates, and if reliability matters, encourage users to exempt your app from battery optimization.
+++

+++Can I use the same `LiveActivityAttributes` class for both local and remote Live activities?

Yes. The same attributes class works for both locally-started and remotely-started (push-to-start) Live activities. You need to ensure you register it with `Messaging.registerLiveActivity()`.

+++

+++What happens if I send an update for a Live activity that does not exist?

If you send an update or end event for a non-existent `liveActivityID` or `channelID`, the request will fail silently on the device. Always ensure you are tracking which Live activity instances are active for each user.

+++

+++Can I test Live activities in the iOS Simulator?

Yes, you can test locally-started as well as remotely-started Live activities in the iOS Simulator.

* **Local**: This includes creating, updating, and ending a Live activity directly from your app using **ActivityKit APIs**.

* **Remote**: To test Live activity functionality remotely, integrate our Messaging SDK into your app and use the provided execution APIs to send remote start, update and end to your test device or iOS Simulator. Similar to how push notifications can be tested currently with Adobe SDKs integration.

+++

+++How do I handle updates when the app is in the background?

The SDK handles this automatically. Once registered, a Live activity receives updates even when the app is terminated. No additional background modes are required.
+++

+++What is the difference between `liveActivityID` and `channelID`?

* `liveActivityID`: Used for individual (unitary) Live activity targeted at specific users. Each ID represents a unique Live activity instance.
* `channelID`: Used for broadcast Live activity sent to audiences. All users in the audience receive the same updates on the same channel.
+++

+++Can I customize the Dynamic Island appearance separately from the Lock Screen?

Yes. The `ActivityConfiguration` has separate closures for Lock Screen content and Dynamic Island content (expanded, compact, and minimal states), each design independently.
+++

+++Do I need to store push tokens manually?

No. The Mobile SDK collects and manages the device's FCM token automatically once Android Live Updates are registered, you do not store tokens manually. On Android, the token lives in the standard push token field on the profile. iOS uses a separate Live Activity token field, while Android reuses the standard push token.
+++

+++Are there limits on remote starts of Live activities?

Yes. Remote starts via `ActivityKit` are subject to system-enforced limits. If you attempt multiple start requests in quick succession, iOS may reject further starts due to Live activity quotas or budget constraints. After about 5 consecutive start attempts, subsequent requests begin failing until a brief cooldown period passes.

+++

+++What is the budget for high-priority updates?

Apple does not specify an exact numerical cap for high-priority `(priority: 10)` Live activity updates. The system maintains a dynamic internal budget that limits how frequently such updates can be sent. If too many high-priority updates are issued in a short span, iOS may throttle or delay subsequent ones.

To minimize throttling: 

* **Balance priority levels**: Combine both standard `(priority: 5)` and high `(priority: 10)` updates depending on importance.
* **Use high priority sparingly**: Reserve high priority for time-critical updates, such as delivery progress, order status, or live sports scores.
* **Support frequent updates**: Include `NSSupportsLiveActivitiesFrequentUpdates` in your app's `Info.plist` and set it to **YES** if you need frequent updates.

Android Live Updates are sent as high-priority FCM messages so they wake the app promptly. There is no Apple-style per-app budget; instead, FCM enforces quotas on high-priority data messages, and the OS may throttle a misbehaving app. Send high priority only for genuinely time-sensitive updates.

+++

+++What is the difference between the Android Live Update ID and the channel ID?

The channel ID, sent as `topic_name`, identifies the broadcast channel that all devices subscribe to. Unitary sends also carry a notification ID. Since Android has no OS-level "activity ID," that notification ID, together with the channel, is used to correlate the notification on the device.
+++

+++ What happens if I send update/end for an Android Live Update that was never started or does not exist?

It depends on unitary vs. broadcast:

* **Broadcast**: `update`/`end` are sent to the broadcast channel, and a device only subscribes to that channel when it receives `start`. So an `update`/`end` for a channel that was never started has no subscribers and reaches no devices, always send `start` first. Also, if you use a brand-new `requestId`, the request is treated as a `start` rather than an `update`, so it will not error but will not behave as the update you intended.
* **Unitary**: `update`/`end` target the recipient's device directly, so an update can physically reach the device even without a prior `start`. Whether the app renders an Android Live Update that was never started is SDK/app-dependent, best practice is still to start first.
* **Already ended**: An `update` is rejected with an error, while an `end` is idempotent (a no-op that returns success).
++++

+++ Are there limits on how much content an Android Live Update can carry?

Yes. Android Live Updates are delivered through Firebase Cloud Messaging, which caps each message at roughly 4 KB. Keep your content compact: long text or large data can exceed the limit and prevent delivery.
+++

### Marketer Questions

+++ Unitary vs broadcast — which should I use?

Use unitary to target and, optionally, personalize an Android Live Update per individual recipient. 

Use broadcast to push one shared Android Live Update to everyone subscribed to a channel, e.g. all fans of a match, highly scalable. 

This choice is identical to iOS.

+++

+++Can I personalize Live activity content for each user in a broadcast campaign?

No. Broadcast sends identical content to every subscriber of the channel. If you need per-user personalization, use a unitary campaign that targets individual recipients. The same rule applies to iOS.
+++

+++ Can a broadcast Android Live Update be transactional (non-marketing)?

No. Broadcast Android Live Updates are supported only for marketing campaigns. For a transactional, e.g. order- or account-triggered, Android Live Update, use a unitary campaign that targets an individual recipient, unitary supports transactional use cases.
+++

+++ Does push consent affect Android Live Updates?

Yes. Android Live Updates are marketing messages, so a recipient's push-marketing consent is respected in both unitary and broadcast. Recipients who have opted out of push marketing are excluded at start, so they are not subscribed and will not receive it.

+++

+++How do I know if my Live activity was successfully delivered?

[Monitor your campaign analytics](../reports/campaign-global-report-cja-activity.md) in Adobe Journey Optimizer. You can track delivery rates, failures, and engagement metrics. Also consider implementing custom analytics events in your app.

Note that broadcast update/end events do not provide per-recipient reporting, since a single message is fanned out to the whole channel. You get campaign-level metrics rather than per-device delivery status. Unitary sends, on the other hand, report per recipient, just like standard push notifications.

+++

+++Can I schedule Live activities in advance?

The API call triggers the Live activity immediately. However, you can schedule your API calls through your backend systems or use Journey Optimizer's orchestration capabilities to time them appropriately.
+++

+++What happens if I send a "start" event for a Live activity that already exists?

When remotely starting a Live activity through Adobe's Execution APIs:

* You can include an `x-request-id` header in your request. Ideally, there should be a one-to-one relationship between each `liveActivityID` and its corresponding `x-request-id`. This ensures that if multiple requests are made with the same `x-request-id` and `liveActivityID` combination, only one Live activity instance will be started on the device, and duplicate requests will be ignored.

* If the `x-request-id` header is omitted, each request is treated independently, which can result in multiple Live activity instances being created with the same `liveActivityID`. In such cases, future updates may fail or apply to only one of the active instances.

* The `x-request-id` value should not be reused across different `liveActivityIDs` in separate API requests.

+++

+++Can I A/B test different Live activity experiences?

Yes. Create multiple campaigns with different content structures and use Adobe Journey Optimizer's experimentation features to test which performs better. Ensure your app supports all content state variations.

+++

+++How often should I update a Live activity?

Update only on meaningful changes. Because every Android update wakes your app to re-post the notification, avoid unnecessarily frequent updates, they cost battery and can be throttled/deferred under Doze. A cadence tied to real events, score change, status change, ETA milestone, is better than a fixed short interval.

+++

+++Can I target users based on whether they have Live activities enabled?

You will need to work with your development team to track and pass this preference to Adobe Experience Platform as a user attribute, then segment based on that attribute.

+++

### API Questions

+++What does an Android Live Update start request look like?

It is a POST to the audience execution endpoint, containing the campaign, a unique request ID, the target audience (broadcast), and an `fcm` provider block.
+++

+++ What does an update or end request look like? 

It has the same shape as the start request, but reuses the same `requestId` so it resolves to the running Android Live Update, with `event_type` set to `update` or `end`. No separate "operation" field is needed, the action is inferred from `event_type`.
+++

+++ What is `event_type` and what values does it take?

`event_type` drives the lifecycle: start: begin the Android Live Update, update: change its content, end: terminate it. This is the Android analog of the iOS event field.

+++

+++ What is `topic_name` / `notification_id` / `notification_channel_id`?

* `topic_name`: The broadcast channel devices subscribe to. Mandatory for broadcast update/end.
* `notification_id`: Correlates the ongoing notification on the device.
* `notification_channel_id`: The Android notification channel your app posts on. Governs importance, sound, and DND behavior.
+++

+++What is the difference between `timestamp` and `dismissal-date`?

* `timestamp`: The current epoch time when the event occurs, required for all events.
* `dismissal-date`: A future epoch time when the Live activity should auto-dismiss, required only for "end" events.

Android does not use `timestamp` and `dismissal-date`.
+++

+++ Do I need to send all content fields on every update? 

Send the fields your app needs to render the current state. Android reads the Android Live Update content from the `data` block in your FCM payload. Unlike iOS, there is no strict "all attributes every call" contract, but you should still include everything your notification needs, since your app re-posts the whole notification and it must be able to render completely each time.

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

The `requestId` must be unique per new Android Live Update, and it is what ties `update`/`end` requests back to the running Android Live Update. A new `requestId` starts a new Android Live Update, while reusing the existing one is how you update or end the current one. Sending `start` again with the same `requestId` is safely ignored, so no duplicate is created.

+++

+++ What if my request includes both an iOS and an Android payload block?

The platform configured for the campaign's channel determines which block is used, for example, the Android `fcm` block for an Android campaign, and the other block is ignored. To avoid confusion, send only the block that matches your campaign's platform.
+++

+++ Does a successful API response mean the update reached devices?

Not necessarily. A success response confirms that the event was accepted and recorded. Delivery to devices is then attempted on a best-effort basis and can be affected by network conditions, Firebase Cloud Messaging, or device state. For broadcast, there is no per-recipient delivery receipt, so treat success as "accepted," not "delivered to every device."
+++

+++For a broadcast, is starting handled differently from updating or ending?

Yes. For a broadcast, starting is processed per recipient across your audience, since that is what subscribes each device to the broadcast channel, so it does more work and can take a little longer. Updates and ends, on the other hand, are sent once and fan out to all subscribed devices, making them lighter and usually faster.

+++

+++What authentication is required for the Headless API?

Refer to the [API Triggered Campaigns Documentation](https://developer.adobe.com/journey-optimizer-apis/references/messaging) for authentication requirements, including OAuth tokens and API keys.

+++

+++What happens if my API call fails?

Check the HTTP status and error body, then retry with backoff for transient errors. Common client-side causes include a missing `topic_name` for a broadcast, a malformed `fcm` block, invalid or expired auth, or an unknown campaign.

+++

+++Can I send Live activity updates from my own backend servers?

Yes, that is the intended behavior. Your backend calls the Adobe Journey Optimizer Headless API to trigger Live activity events when your business logic requires it.

+++

+++Do I need a different campaign for start, update, and end events?

No. You can use the same campaign and change the `event` field in the payload. However, some organizations prefer separate campaigns for better analytics tracking.

+++

### Troubleshooting Questions

>[!TIP]
>
>For comprehensive troubleshooting guidance, see [Troubleshoot Live activities](troubleshoot-mobile-live.md).

+++My Live activity starts but does not update. What could be the issue?

Common causes:

* Mismatched `liveActivityID` or `channelID` between start and update calls.
* `content-state` fields do not match your `ContentState` struct.
* The Live activity has already ended.
* Network connectivity issues on the device.
* The epoch time used as timestamp is not up-to-date.

On Android, verify the following:

* The update reuses the same `requestId` as the start.
* `topic_name` matches the broadcast channel used at start.
* The app is receiving the FCM data message and re-posting the notification, battery optimization/Doze can suppress this.
* `event_type` is exactly `update`.
* The FCM token is still valid.

+++

+++The `attributes-type` field is not being recognized. What should I check?

* Ensure the class name matches **exactly** (case-sensitive) with your Swift struct name
* Verify the struct is properly defined and registered
* Check for typos in the JSON payload
* Confirm the app version installed has the Live activity implementation

+++

+++Users only see the Live activity update and not the alert notification, is this a known issue?

No. The `alert` field is optional and may be suppressed by iOS in certain conditions, for example Do Not Disturb mode. A Live activity can update silently, which is often the intended behavior. The alert field is mandatory for sending remote starts otherwise apple treats it like a silent background notification.

On Android, alert vs. silent behavior is governed by the notification channel's (`notification_channel_id`) importance and the user's settings, such as DND or a muted channel. Ongoing/updating notifications are often intentionally low-intrusion, so configure the channel importance appropriately.

+++

+++Can I delete or clear all Live activity instances for a user?

Send an `end` event. For broadcast, a single `end` to the channel terminates it for all subscribers. For unitary, end each active Android Live Update individually. There is no bulk "clear all," so track active Android Live Updates in your systems so you can end them cleanly.

+++

+++My widget shows "No data" even though I sent an update. What could be the issue?

* Verify your widget implementation properly accesses `context.state` and `context.attributes`.
* Check that default values or error states are handled in your widget interface.
* Use the `LiveActivityAssuranceDebuggable` protocol to debug the schema.
* Test with Adobe Assurance to see if data is being received.

On Android, this is usually an app-side issue: the service is not reading the Android Live Update data block, a field the notification expects is missing, or the notification channel is not created. Verify the payload the device receives, provide sensible defaults, and test with Adobe Assurance or logcat.

+++

+++ A broadcast update/end was rejected as malformed. Why? 

For broadcast `update`/`end` requests, `topic_name` is mandatory. A missing or empty value makes the Android Live Update invalid, so it will not be sent. Make sure every broadcast `start`, `update`, and `end` request carries a non-empty `topic_name`.

+++

{{$include /help/_includes/do-not-localize/mobile-live/ai-augmented-mobile-live-faq.md}}
