---
solution: Journey Optimizer
product: journey optimizer
title: Troubleshoot Live activities
description: Learn how to troubleshoot Live activities in Journey Optimizer for both unitary and broadcast use cases, including profile token issues, campaign configuration, and delivery failures
role: User
level: Intermediate
---
# Get started troubleshooting Live activities {#troubleshoot-mobile-live-gs}

>[!BEGINSHADEBOX]

**On this page:** Systematically diagnose why your Live activities fail to appear, update, or end so you can resolve profile token, campaign configuration, payload, and delivery issues across both unitary and broadcast use cases.

>[!ENDSHADEBOX]

Live activities in Adobe Journey Optimizer enable real-time, dynamic updates on iOS lock screens and Dynamic Islands. They can only be triggered and managed through API Triggered Campaigns.

**Use case types:**

* **Unitary**: Individually targeted, transactional (API-triggered Transactional campaigns)
* **Broadcast**: Audience-targeted, mass delivery (API-triggered Marketing campaigns)

A frequent challenge with Live activities is when the API call to trigger or update a Live activity returns a **successful response (200 OK)**, but the Live activity fails to appear or update on the user's device. This disconnect between API confirmation and actual device behavior can occur at multiple points in the delivery pipeline. This guide provides a systematic troubleshooting approach to identify where the delivery is failing, examining each stage from API request validation through device rendering.

## Most Common Issues

| Symptom | Use case | Go to |
| --- | --- | --- |
| API returns 200 OK but Live activity never appears on device | Both | [Scenario 1: Profile or push token issues](troubleshoot-mobile-live.md#scenario-1-profile-or-push-token-issues) |
| Payload configuration or API structure unclear | Both | [Scenario 2: Campaign configuration and payload issues](troubleshoot-mobile-live.md#scenario-2-campaign-configuration-and-payload-issues) |
| Campaign and tokens look correct but delivery still fails | Both | [Scenario 3: Delivery failures and error analysis](troubleshoot-mobile-live.md#scenario-3-delivery-failures-and-error-analysis) |
| Live activity appears but won't update or end | Unitary (1:1) | [Scenario 4: Update token not synced](troubleshoot-mobile-live.md#scenario-4-live-activity-update-token-not-synced) |
| Need to confirm execution status programmatically | Unitary (1:1) | [Scenario 5: Checking execution status via API](troubleshoot-mobile-live.md#scenario-5-checking-execution-status-via-the-api) |
| Specific audience members not receiving broadcast | Broadcast | [Scenario 7: Profile not in audience or stale snapshot](troubleshoot-mobile-live.md#scenario-7-profile-not-in-audience-or-stale-audience-snapshot) |
| No Assurance access; need production-level debugging | Both | [Advanced: Debugging via dataset queries](troubleshoot-mobile-live.md#advanced-debugging-via-dataset-queries) |

## Understanding the Two Use Cases

Before debugging, confirm which use case applies to your campaign. The root cause and debugging path differ significantly between them.

>[!BEGINTABS]

>[!TAB iOS]

On iOS, unitary Live activities use a push-to-start token to start and a per-instance update token to update or end. Broadcast events reach subscribed devices through the shared channel identified by `input-push-channel`.

| Aspect | Unitary (1:1) | Broadcast |
| --- | --- | --- |
| **AJO campaign type** | API-triggered Transactional | API-triggered Marketing |
| **Targeting** | Individual profile via `recipients[].userId` | Audience segment via `audience.id` |
| **Token or channel to start** | Push-to-start token (per profile) | `input-push-channel` (per broadcast instance) |
| **Token or channel to update/end** | Update token (per Live activity instance) | Same `input-push-channel` as start |
| **Audience freshness risk** | Not applicable | Up to 24 hours stale (batch evaluation) |

>[!TAB Android]

On Android, unitary Live activities use the same regular FCM push token to start, update, and end. No separate activity tokens are required. Broadcast events reach subscribed devices through the shared FCM topic identified by `topic_name`.

| Aspect | Unitary (1:1) | Broadcast |
| --- | --- | --- |
| **AJO campaign type** | API-triggered Transactional | API-triggered Marketing |
| **Targeting** | Individual profile via `recipients[].userId` | Audience segment via `audience.id` |
| **Token or topic to start** | Regular FCM push token (per profile) | FCM topic (per broadcast instance) |
| **Token or topic to update/end** | Same regular FCM push token | Same FCM topic |
| **Audience freshness risk** | Not applicable | Up to 24 hours stale (batch evaluation) |

>[!ENDTABS]

## Terminology Glossary

>[!BEGINTABS]

>[!TAB iOS]

| Term | Definition |
| --- | --- |
| **APS payload** | The JSON structure sent inside the API request under `context.requestPayload.aps`. Contains the Live activity event, `content-state`, `attributes`, and control fields. |
| **Assurance** | Adobe Experience Platform Assurance, a real-time debugging tool for connected test devices. Not available for production end-user devices. |
| **`attributeType` / `attributes-type`** | The name of the Swift `ActivityAttributes` struct. Stored as `attributeType` (camelCase) in AEP profile attributes and sent as `attributes-type` (hyphenated) in APS JSON payloads. These are the same value in different representations. |
| **Broadcast Channel ID** | The value of `input-push-channel`. Must exactly match `liveActivityData.channelID` in the broadcast payload. |
| **`input-push-channel`** | A unique channel identifier created on the Apple Developer Portal for broadcast Live activities. Acts as the broadcast update token. All devices subscribed to this channel receive the same Live activity events. |
| **`liveActivityData`** | A required property on the Adobe SDK's `LiveActivityAttributes` protocol. For unitary Live activities, contains `liveActivityID`; for broadcast Live activities, contains `channelID`. Must be included in the `attributes` field of start event payloads. |
| **`liveActivityPushNotificationDetails`** | The AEP profile attribute that stores a device's push-to-start token, `appId`, `platform`, and `attributeType`. Must be present and valid for remote start to work. |
| **Push-to-start token** | An APNs token generated by iOS 17+ that allows AJO to remotely start a Live activity on a device without the app being open. Registered by the mobile SDK and stored on the AEP profile. |
| **Update token** | A per-instance APNs token generated when a Live activity starts on a device. Required for unitary `update` and `end` events. Each Live activity instance has its own unique update token. |

>[!TAB Android] 

| Term | Definition |
| --- | --- |
| **`action_type` / `action_uri`** | The tap action and its deep-link target. *Not read by the current Android SDK.* |
| **Broadcast** | Audience-targeted Live activity sent via an API-triggered Marketing campaign. |
| **`content_state`** | Dynamic values (fields defined by your app) consumed by the app's style provider to render the notification. |
| **`critical_text`** | Short text rendered in the status-bar chip. |
| **`dismiss_after`** | Used only for end events. Specifies how many seconds the completed Live activity remains visible before removal. |
| **ECID** | Experience Cloud ID, the identifier used as the unitary target with the `ECID` namespace. |
| **`event_type`** | The lifecycle event: `start`, `update`, or `end`. |
| **`message.feedback`** | The event recording the delivery outcome for each message, including `feedbackStatus`, `serviceProvider = fcm`, `errorCode`, and `errorMessage`. |
| **`notification_channel_id`** | The Android notification channel the Live activity posts to. Must match a channel created by the app. |
| **`notification_id`** | Client-generated identifier for a Live activity instance. Keep it unchanged across start, update, and end events to target the same instance. |
| **`priority`** | FCM delivery priority, for example, `PRIORITY_HIGH`. |
| **Push token (FCM registration token)** | The device's Firebase Cloud Messaging token, synced to the profile and used to deliver unitary Live activities. |
| **`timestamp`** | Message ordering key, expressed in epoch seconds. Must strictly increase for every event with the same `notification_id` (or `topic_name` for broadcasts). Updates are displayed only if their timestamp is newer than the last processed value. Older or equal timestamps are ignored. |
| **`topic_name`** | The shared FCM topic through which subscribed devices receive broadcast events. The Android equivalent of iOS `input-push-channel`. |
| **Unitary** | Individually targeted Live activity sent via an API-triggered Transactional campaign. |
| **`when`** | Optional notification display time, expressed in epoch seconds. Maps to Android's `setWhen` method and does not control message ordering, which is handled by `timestamp`. Keep the value reasonably current to avoid display issues. |

>[!ENDTABS]

## Prerequisites

Before troubleshooting, ensure you have:

>[!BEGINTABS]

>[!TAB iOS]

+++ Assurance

The Live Activities view in Adobe Experience Platform Assurance validates your app's setup, inspects activity events, and lets you remotely start, update, or end activities from a test session.

>[!IMPORTANT]
>
> Assurance sessions are for test and QA devices only. End-user production devices are not connected to Assurance. For production diagnostics, use the [Advanced: Debugging via dataset queries](#advanced-debugging-via-dataset-queries) section at the end of this guide.

**Requirements**

| Requirement | Details |
| --- | --- |
| iOS device | Physical device running iOS 16.1 or later |
| Xcode Simulator | iOS 16.1 or later. **Local start only**; remote push via APNs is not supported on the simulator. |
| Remote start from Assurance | iOS 17.1 or later, valid push-to-start token, and valid channel configuration |
| Mobile SDK | Adobe Experience Platform Mobile SDK 5.11.0 or later |
| Session | An active Assurance session |

**Three tabs**

| Tab | What it shows |
| --- | --- |
| **Client Info** | Device, profile, and App Store credentials. A green check indicates correct configuration; an inline alert indicates an issue and suggests a fix. Maps directly to the pre-checks in the troubleshooting scenarios. |
| **Activities** | Live activities for the selected client: type (Unitary/Broadcast), ID, status, and event count. Sub-tabs: **Overview** (basic information and **Send Update** button), **Activity Flow** (lifecycle timeline with inspectable payloads), and **Event Details** (full payload inspection per event). |
| **Events** | All Assurance events for the client, including Live activity start, update, and end events. |

**Starting, updating, and ending from Assurance**

**Start Live Activity**. opens a dialog to pick the registered activity type, choose Unitary or Broadcast, enter a Broadcast Channel ID (broadcast only), and edit a pre-filled APS JSON payload. Button is disabled or returns an error if push-to-start token, iOS version, or channel configuration requirements are not met.

**Send Update**. from the Overview tab of an existing activity, sends either an Update (push new content) or End event. For unitary, the plugin uses the activity's update token automatically. For broadcast, it targets all devices subscribed to the same Broadcast Channel ID. Payloads must be valid JSON and match the activity's attribute schema; the request is rejected otherwise.

See the [Adobe Experience Platform Assurance documentation](https://experienceleague.adobe.com/en/docs/experience-platform/assurance/home.html) for setup and session-connection steps.

+++

+++ Gather API Triggered Campaign details

Navigate to your API Triggered Campaign in Journey Optimizer and retrieve:

* Campaign name and ID
* Campaign version (if applicable)
* Campaign type: **Transactional** (unitary) or **Marketing** (broadcast)
* Surface configuration: the iOS app surface used for the Live activity
* Activity type: the `AttributeType` struct name configured in the campaign

+++

+++ Collect API request information

When making the API call to trigger the Live activity, save:

* API request payload, including profile identifiers and Live activity data
* API response including status code, message ID, request ID
* Timestamp of when the API was called
* Endpoint used, e.g., `/campaign/{CAMPAIGN_ID}/execute`

+++

+++ Identify the test profile

From your API request, retrieve:

* Profile namespace, e.g., ECID, email, customer ID
* Profile ID used in the API call

Ensure you can look up this profile in Adobe Experience Platform. Learn how to [look up a profile in the Experience Platform documentation](https://experienceleague.adobe.com/en/docs/experience-platform/profile/ui/user-guide.html).

+++

+++ Device and app information

Collect the following from your test device:

* Device model, e.g., iPhone 14 Pro
* iOS version
* App bundle identifier
* APNs push token
* Network connectivity status at the time of testing

+++

>[!TAB Android]


+++ Assurance

On Android, use Assurance on a physical device or emulator running Android 16.1 (API level 36.1) or later. An Assurance session captures SDK events and lets you inspect the delivery pipeline: Edge Network requests and responses, profile qualification, push-token registration, and delivery events. Learn how to set up [Assurance](https://experienceleague.adobe.com/en/docs/experience-platform/assurance/home.html).

>[!IMPORTANT]
>
> Assurance sessions are for test and QA devices only. End-user production devices are not connected to Assurance. For production diagnostics, use the [Advanced: Debugging via dataset queries](#advanced-debugging-via-dataset-queries) section at the end of this guide.

+++

+++ Gather API Triggered Campaign details

Navigate to your API Triggered Campaign in Journey Optimizer and retrieve:

* Campaign name and ID
* Campaign version (if applicable)
* Campaign type: **Transactional** (unitary) or **Marketing** (broadcast)
* Surface configuration: the iOS app surface used for the Live activity
* Activity type: the `AttributeType` struct name configured in the campaign

+++

+++ Collect API request information

When making the API call to trigger the Live activity, save:

* API request payload, including profile identifiers and Live activity data
* API response including status code, message ID, request ID
* Timestamp of when the API was called
* Endpoint used, e.g., `/campaign/{CAMPAIGN_ID}/execute`

+++

+++ Identify the test profile

From your API request, retrieve:

* Profile namespace, e.g., ECID, email, customer ID
* Profile ID used in the API call

Ensure you can look up this profile in Adobe Experience Platform. Learn how to [look up a profile in the Experience Platform documentation](https://experienceleague.adobe.com/en/docs/experience-platform/profile/ui/user-guide.html).

+++

+++ Device and app information

Collect the following from your test device:

* Device model, e.g., iPhone 14 Pro
* Android version
* App package name
* FCM registration token
* Network connectivity status at the time of testing

+++


>[!ENDTABS]

{{$include /help/_includes/do-not-localize/mobile-live/ai-augmented-troubleshoot-mobile-live.md}}

