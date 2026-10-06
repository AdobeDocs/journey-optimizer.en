---
solution: Journey Optimizer
product: journey optimizer
title: Troubleshoot Live activities
description: Learn how to troubleshoot Live activities in Journey Optimizer for both unitary and broadcast use cases, including profile token issues, campaign configuration, and delivery failures
role: User
level: Intermediate
exl-id: f0f83bd2-7c2b-4d9b-b455-e1df12dfa175
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
---
# Common Live activities troubleshooting scenarios{#troubleshoot-mobile-live}

>[!BEGINSHADEBOX]

**On this page:** Systematically diagnose why your Live activities fail to appear, update, or end so you can resolve profile token, campaign configuration, payload, and delivery issues across both unitary and broadcast use cases.

>[!ENDSHADEBOX]

## Scenario 1: Profile or push token issues {#scenario-1-profile-or-push-token-issues}

[!BADGE Applies to both unitary and broadcast use cases]{type=Positive}


The API returns HTTP 200, but the Live activity does not appear. Common causes:

* Profile does not exist in Adobe Experience Platform.
* Live activity push token has not been synced to the profile.
* Live activity push details are synced but contain incorrect configuration, e.g. wrong `appId` or `attributeType`.

**Note for broadcast use cases**: If some profiles in your audience are missing tokens, only those profiles will fail to receive the Live activity. Sample several profiles from your audience to diagnose token issues. This applies only to remote start events, not update or end events.

>[!BEGINTABS]

>[!TAB iOS]

### Pre-checks

* iOS app requirements: 
   * iOS 16.1+
   * `NSSupportsLiveActivities` set to `YES` in `Info.plist`
   * `ActivityAttributes` properly implemented.
* Mobile SDK Integration: 
   * Adobe Experience Platform Mobile SDK (messaging SDK 5.11.0+)
   * `Messaging.registerLiveActivities` implemented and called with Live activity push token.

### Debugging steps

+++ 1. Verify profile exists in Adobe Experience Platform

1. In Journey Optimizer, navigate to **Customer** `>` **Profiles**.
1. Search using namespace and identity value from API request.
1. If profile is not found, the profile does not exist or ingestion is not completed. Create the profile or wait for ingestion before triggering the Live activity.
1. If profile is found, proceed to step 2 below to check if the push token is synced.

+++

+++ 2. Check if Live activity push token is synced

You can use Assurance to verify token registration:

1. In Assurance, from the **Events** list, filter or search for events `eventType = "liveActivity.pushToStart"`.
1. Select the **Event** and inspect the payload.
1. Check that the token, appId, and attributeType values are present.
1. Confirm if the event was successfully sent.

You can also check in Adobe Experience Platform profile.

1. In Adobe Experience Platform, from your **Profile**, access the **Events** tab.
1. Search for `liveActivity.pushToStart` events.
1. Check the even timestamp and payload.

If no events are found, your mobile app is not calling `Messaging.registerLiveActivity` correctly. You need to fix the SDK integration.

+++

+++ 3. Validate token details on profile

1. From your **Profile**, access the **Attributes** tab.
1. Locate `liveActivityPushNotificationDetails`.
1. Verify the token configuration:

   ```json
   {
      "liveActivityPushNotificationDetails": [
      {
         "appId": "com.example.myapp",
         "token": "abc123def456...",
         "platform": "apns",
         "denylisted": false,
         "attributeType": "OrderTrackingAttributes",
         "identity": {}
      }
      ]
   }
   ```

**Validate each field:**

| Field | Requirement | Common Issue |
|-|-|-|
| `appId` | Must exactly match iOS bundle identifier | Mismatch between dev/prod bundle IDs |
| `attributeType` | Must exactly match Swift `ActivityAttributes` struct name (case-sensitive) | Typo or incorrect struct name |
| `platform` | Must be `"apns"` or `"apnsSandbox"` | Wrong platform value |
| `denylisted` | Must be `false` | Token marked as invalid or user opted out |
| `token` | Valid APNs push token | Token expired or app reinstalled |

If any field is incorrect: Update the mobile app, re-register using `Messaging.registerLiveActivities`, wait 5-10 minutes, then re-check.

If `liveActivityPushNotificationDetails` is missing: Token has not synced yet. Wait 5-10 minutes after seeing the `liveActivity.pushToStart` event in Assurance.

+++

>[!TAB Android]

### Pre-checks

* **Android app requirements:**
   * Run the app on Android 16.1 (API level 36.1) or later, with `targetSdk` set to `36`.
   * Ensure that `POST_NOTIFICATIONS` and `POST_PROMOTED_NOTIFICATIONS` permissions are granted.
   * Create the notification channel used by the Live activity.
* **Mobile SDK integration:**
   * Integrate the Adobe Experience Platform Mobile SDK with Messaging and the Live Activities extension.
   * Forward the FCM registration token to the SDK using `MobileCore.setPushIdentifier(token)`.

### Debugging steps

+++ 1. Verify the profile exists in Adobe Experience Platform

1. In Journey Optimizer, navigate to **Customer** `>` **Profiles**.
1. Search using the namespace and identity value from your API request.
1. If the profile is not found, create it or wait for ingestion to complete before triggering the Live activity.
1. If the profile is found, proceed to step 2 to verify FCM token registration.

+++

+++ 2. Verify FCM token registration

Android uses the standard FCM registration token for Live activities. There is no `liveActivity.pushToStart` event or separate Live activity push token.

1. In Assurance, open the **Events** list and locate the standard push-token registration event.
1. Select the event and inspect its payload to verify that the FCM registration token is present.
1. Confirm that the registration event was successfully sent.
1. In Adobe Experience Platform, open your profile's **Attributes** tab and confirm that the token is present in `pushNotificationDetails`, as described in step 3.

If the registration event or profile token is missing, verify that the app forwards the FCM registration token to the SDK using `MobileCore.setPushIdentifier(token)`.

+++

+++ 3. Validate token details on the profile

1. From your profile, access the **Attributes** tab.
1. Locate `pushNotificationDetails`. Android uses this object instead of `liveActivityPushNotificationDetails` and does not require an `attributeType` field.
1. Verify that the token configuration follows this structure:

   ```json
   {
      "pushNotificationDetails": [
         {
            "appId": "com.adobe.marketing.mobile.liveupdatessample",
            "token": "fcm-registration-token...",
            "platform": "fcm",
            "denylisted": false,
            "identity": {}
         }
      ]
   }
   ```

**Validate each field:**

| Field | Requirement | Common Issue |
|---|---|---|
| `appId` | Must exactly match the Android package name | Mismatch between development and production package names |
| `platform` | Must be `"fcm"` | Wrong platform value |
| `denylisted` | Must be `false` | Token marked as invalid or user opted out |
| `token` | Must match the device's current FCM registration token | Token expired or app reinstalled |

If any field is incorrect, correct the app configuration as needed, forward the FCM token again using `MobileCore.setPushIdentifier(token)`, wait 5-10 minutes, then re-check the profile.

If `pushNotificationDetails` is missing, the token has not synced yet. After confirming token registration in Assurance, wait 5-10 minutes, then re-check the profile.

+++


>[!ENDTABS]

## Scenario 2: Campaign configuration and payload issues {#scenario-2-campaign-configuration-and-payload-issues}

[!BADGE Applies to both unitary and broadcast use cases]{type=Positive}

Profile exists with valid tokens, but Live activity does not appear. This can be caused by:

* Wrong surface or channel configuration.
* Incorrect API payload structure.
* `content-state` and `attributes` do not match iOS `ActivityAttributes` implementation.
* Stale `timestamp` (critical for update/end).

**Note for broadcast use cases**: Campaign must be **API-triggered Marketing** (not Transactional). Payload uses `audience` instead of individual `profile`. Refer to [this section](#broadcast-config) for broadcast-specific payload structure and to [Adobe Developer documentation](https://developer.adobe.com/journey-optimizer-apis/references/messaging#operation/postIMAudienceMessageExecution) for complete API specifications.

>[!BEGINTABS]

>[!TAB iOS]

### Pre-checks

* Campaign is **API-triggered Transactional** (unitary) or **API-triggered Marketing** (broadcast) and **High Throughput** option must be **not** be enabled since it is incompatible with Live activity.
* Ensure that profile exists and tokens are synced correctly using the [above scenario](#scenario-1-profile-or-push-token-issues).

### Debugging steps

+++ 1. Verify campaign surface configuration

1. In Journey Optimizer, open your **Campaign** and navigate to the **Actions** menu.
1. Check your **Live activity configuration**. The surface must be configured for the iOS app with a bundle identifier that matches the `appId` in your profile's `liveActivityPushNotificationDetails`. For example, if your profile has `"appId": "com.example.myapp"`, the surface must target that same app.
1. Check that the **Activity type** in your campaign configuration matches exactly the `attributeType` in your profile's `liveActivityPushNotificationDetails`. For example, if your profile has `"attributeType": "FoodDeliveryLiveActivityAttributes"`, the campaign must specify this same Activity type.

+++

+++ 2. Validate API payload structure

When executing the campaign via API, ensure the payload follows the correct structure.

**Unitary payload:**

```json
{
   "campaignId": "your-campaign-id",
   "recipients": [{
      "type": "aep",
      "userId": "user@example.com",
      "namespace": "email",
      "context": {
      "requestPayload": {
         "aps": {
            "content-available": 1,
            "timestamp": 1756984054,
            "event": "start",
            "attributes-type": "FoodDeliveryLiveActivityAttributes",
            "content-state": { ... },
            "attributes": { ... }
         }
      }
      }
   }]
}
```

**Common payload issues:**

| Field | Requirement | Common Issue |
|-|-|-|
| `attributes-type` | Must match campaign Activity type and profile `attributeType` | Mismatch or typo |
| `campaignId` | Must match the activated campaign ID | Wrong or missing campaign ID |
| `content-available` | Must be `1` | Missing or wrong value |
| `event` | Must be `"start"`, `"update"`, or `"end"` | Invalid event type |
| `timestamp` | Must always be the current/latest Unix epoch time in seconds | Using old/cached timestamp |
| `userId` / `namespace` | Must match an existing profile in AEP | Profile identifier mismatch |

**Critical: Always use the latest timestamp**

* The `timestamp` field must **always** be the **current Unix epoch time** (in seconds) at the moment each API call is made.
* This applies to **all event types**: `start`, `update`, and **especially `end`**.
* **Impact on updates/end requests**: Using a stale or old timestamp will cause update and end requests to fail or be ignored by the device.
* Do **NOT** reuse timestamps from previous requests or use cached values.
* Generate a fresh timestamp for every API call.

**Optional fields (all event types):**

* `requestId`: Unique identifier for tracking (recommended).
* `alert`: Object with `title` and `body` for notification (useful for drawing attention to updates).

**About `dismissal-date`:**

* Optional field containing Unix epoch time (seconds).
* **Only relevant when `event: "end"`**.
* Specifies when the Live activity should automatically be removed from the device.
* If not provided on end event, Live activity remains visible until user dismisses it.
* Must be a future timestamp (later than `timestamp`).

+++

+++ 3. Align payload with iOS implementation

Ensure your API payload matches your iOS app's `ActivityAttributes` implementation. The Adobe SDK's `LiveActivityAttributes` protocol extends iOS `ActivityAttributes` and requires a `liveActivityData` property.

**Validate the mapping:**

1. Your `ActivityAttributes` must implement Adobe's `LiveActivityAttributes` protocol. Example:

   ```swift
   struct FoodDeliveryLiveActivityAttributes: LiveActivityAttributes {
      public struct ContentState: Codable, Hashable {
         var orderStatus: String
         var estimatedDeliveryTime: String
      }
      
      // Adobe SDK requirement
      var liveActivityData: LiveActivityData
      
      // Your custom attributes
      var restaurantName: String
   }
   ```

   **Note** that the `liveActivityData` field is required by Adobe SDK and must be included in all implementations.

1. Your API payload must mirror the iOS structure:

   ```json
   {
      "aps": {
         "event": "start",
         "timestamp": 1756984054,
         "attributes-type": "FoodDeliveryLiveActivityAttributes",
         "content-state": {
         "orderStatus": "Preparing",
         "estimatedDeliveryTime": "20 mins"
      },
      "attributes": {
         "liveActivityData": {
         "liveActivityID": "order-12345"
         },
         "restaurantName": "Pizza Palace"
      }
      }
   }
   ```

**Validation checklist:**

* Include all `ContentState` fields in `content-state` (required for all event types).
* Include all `LiveActivityAttributes` fields in `attributes` (start events only), including:
   * `liveActivityData` (required; typically contains `liveActivityID` or similar identifier)
   * All custom fields from your struct
* Match field names exactly (case-sensitive).
* Match data types (String, Int, Bool, nested objects).
* Preserve nested object structure.

**Common mistakes:**

| Issue | Impact | Fix |
|---|---|---|
| Missing `liveActivityData` in attributes | Live activity will not start | Always include `liveActivityData` object in start event |
| Missing required field in start event | Live activity will not start | Add all fields from iOS struct |
| Wrong field name (typo/case) | Field ignored or parsing error | Match iOS field names exactly |
| Wrong data type | Parsing error | Match iOS data types |
| Missing nested object | Incomplete data | Include all nested structures |
| Including `attributes` in update/end | Unnecessary, but usually ignored | Only include `attributes` in start event |
| Stale timestamp on update/end | Update/end ignored by device | Always generate fresh timestamp |

For more examples, refer to [Create Live activity page](create-mobile-live.md).

+++

+++ 4. Test with Assurance

Verify API execution and payload delivery using Assurance:

1. Open your Assurance session.
1. Execute the API call to trigger the Live activity.
1. In the **Event List**, check for:
   * Campaign execution events.
   * Live activity delivery events.
   * Payload validation error events.
1. Review event payloads to verify:
   * Payload was processed correctly.
   * No validation errors occurred.
   * Live activity was sent to APNs.

+++ 

>[!TAB Android]

### Pre-checks

* Confirm that the campaign is **API-triggered Transactional** (unitary) or **API-triggered Marketing** (broadcast). Keep **High Throughput** disabled because it is incompatible with Live activities.
* Verify that the profile exists and its FCM token is synced using the Android checks in [Scenario 1](#scenario-1-profile-or-push-token-issues).

### Debugging steps

+++ 1. Verify campaign surface configuration

1. In Journey Optimizer, open your **Campaign** and navigate to the **Actions** menu.
1. Check your **Live activity configuration**. The surface must target the Android app with a package name that matches the `appId` in the profile's `pushNotificationDetails`.
1. Verify that the surface uses the FCM credentials for that app. The profile's token platform must be `"fcm"`.
1. Confirm that `notification_channel_id` in the payload matches a notification channel created by the app.

+++

+++ 2. Validate API payload structure

Place Android Live activity fields under `context.requestPayload.fcm`.

**Unitary start payload:**

```json
{
   "requestId": "your-request-id",
   "campaignId": "your-campaign-id",
   "recipients": [
      {
         "type": "aep",
         "userId": "your-device-ECID",
         "namespace": "ECID",
         "context": {
            "requestPayload": {
               "fcm": {
                  "notification_id": "flight-DL-321",
                  "timestamp": 1756984054,
                  "notification_channel_id": "live_updates_channel",
                  "priority": "PRIORITY_HIGH",
                  "event_type": "start",
                  "title": "Flight DL-321",
                  "body": "Boarding starts shortly",
                  "critical_text": "25 min",
                  "content_state": {
                     "custom_key_template_type": "progress",
                     "custom_key_journey_start": "DEL",
                     "custom_key_journey_progress": 10,
                     "custom_key_journey_end": "MUM"
                  }
               }
            }
         }
      }
   ]
}
```

Replace the sample timestamp with the current Unix epoch time in seconds. The `content_state` keys are examples and must match your app's style provider.

For broadcasts, use an API-triggered Marketing campaign with `audience.id` and place the `fcm` object under `context.requestPayload`. Set `topic_name` to the FCM topic subscribed to by the target devices. Keep the topic and `notification_id` unchanged across start, update, and end events. See the [Android broadcast payload examples](create-mobile-live.md).

**Common payload issues:**

| Field | Requirement | Common Issue |
|---|---|---|
| `campaignId` | Must match the activated campaign ID | Wrong or missing campaign ID |
| `notification_id` | Keep the same value for the Live activity's start, update, and end events | Changed ID targets a different notification |
| `notification_channel_id` | Must match a channel created by the Android app | Missing or mismatched channel |
| `event_type` | Must be `"start"`, `"update"`, or `"end"` | Invalid lifecycle event |
| `timestamp` | Epoch seconds; must strictly increase for each event targeting the same instance or broadcast topic | Older or equal timestamps are ignored |
| `content_state` | Use `custom_key_*` fields supported by the app's style provider | Unsupported keys or incorrect value types |
| `userId` / `namespace` | For unitary delivery, use the device's ECID with the `ECID` namespace | Profile identifier mismatch |
| `topic_name` | For broadcasts, use the topic subscribed to by the target devices | Incorrect topic or devices not subscribed |

**Timestamp and lifecycle checks:**

* Use a fresh `timestamp` in epoch seconds for every start, update, and end event. Ensure that it is greater than the previous value for the same `notification_id` (or `topic_name` for broadcasts), even when requests are made within the same second.
* Older or equal timestamps are ignored. Do not reuse cached timestamps.
* The optional `when` field controls the notification's displayed time, not message ordering. Keep it reasonably current and express it in epoch seconds.
* To update or end an activity, change `event_type` while keeping `notification_id` unchanged. Android uses the same FCM registration token for all three lifecycle events; no separate update token is required.

**End-event dismissal:**

For `event_type: "end"`, optionally set `dismiss_after` to the number of seconds the completed Live activity should remain visible before removal. This is a duration, not an epoch timestamp.

+++

+++ 3. Align the payload with the Android implementation

The app's style provider determines how `content_state` values render in the Live activity notification.

1. Confirm that Messaging and the Live Activities extension are integrated in the app.
1. Verify that each `custom_key_*` field in `content_state` matches a key handled by the style provider, including its expected value type.
1. Check that `title`, `body`, and `critical_text` contain the intended display text. `critical_text` is used for the status-bar chip.
1. Confirm that notification permissions are granted and that the channel identified by `notification_channel_id` exists.

**Common mistakes:**

| Issue | Impact | Fix |
|---|---|---|
| Unsupported `content_state` key or value type | Content is missing or rendered incorrectly | Match the app's style-provider mapping |
| Notification channel missing or mismatched | Notification cannot post to the intended channel | Create the channel and use its exact ID |
| Notification permissions not granted | Live activity may not appear as expected | Verify `POST_NOTIFICATIONS` and `POST_PROMOTED_NOTIFICATIONS` permissions |
| Changed `notification_id` | Update or end does not target the original notification | Keep the ID unchanged throughout the lifecycle |
| Older or equal `timestamp` | Event is ignored | Use a value greater than the last processed timestamp |

For more examples, refer to [Create Live activities](create-mobile-live.md).

+++

+++ 4. Test with Assurance

Use standard Assurance on a connected Android test device. There is no dedicated Live Activities plugin view for Android.

1. Open an Assurance session and confirm that the FCM token registration is visible.
1. Execute the API call to start the Live activity, then send update and end events with the same `notification_id` and increasing timestamps.
1. Review the available SDK events and payloads for processing or validation errors. Confirm that the Android payload uses `fcm` and the intended lifecycle values.
1. In the profile's **Events** tab, inspect matching `message.feedback` events. Check that `serviceProvider` is `fcm`, and review `feedbackStatus`, `errorCode`, and `errorMessage` for delivery failures.
1. If delivery succeeds but the Live activity does not render, inspect app logs, style-provider mappings, notification permissions, and channel configuration on the device.

+++ 

>[!ENDTABS]

## Scenario 3: Delivery failures and error analysis {#scenario-3-delivery-failures-and-error-analysis}

[!BADGE Applies to both unitary and broadcast use cases]{type=Positive}

In this scenario, all previous checks have passed:

* Profile exists with [valid Live activity push tokens](#scenario-1-profile-or-push-token-issues)
* Campaign is correctly [configured with proper payload](#scenario-2-campaign-configuration-and-payload-issues)
* [Update tokens are synced](#scenario-4-live-activity-update-token-not-synced) (for update/end events, unitary use case only)

But the Live activity still does not appear, update, or end as expected. The issue may be at the Adobe delivery system level or with the push notification service provider (APNs).

**Note for broadcast use cases**: Reports show metrics across all audience members. Some profiles may succeed while others fail.

>[!BEGINTABS]

>[!TAB iOS]

**Pre-checks**

* **Previous Scenarios Validated:**
   * Profile exists with valid `pushNotificationDetails`, including the current FCM token, Android package name, and `platform: "fcm"`.
   * Campaign surface targets the correct Android app and uses the matching FCM credentials.
   * The `fcm` payload is valid and its `timestamp` is newer than the previous event for the same `notification_id` (or `topic_name` for broadcasts).
   * Start, update, and end events use the same `notification_id`. Unitary events use the same FCM registration token; no separate update token is required.

* **API Call Confirmed:**

   * The API call returned HTTP 202 (accepted). This confirms request acceptance, not delivery or device rendering.
   * Campaign ID and recipient details are correct. For broadcasts, verify the audience ID and FCM topic.

### Debugging steps

+++ 1. Check campaign reports

1. Navigate to your **Live activity Campaign**.
1. Click the **Reports** button.
1. Select **View all time report**.
1. Review the following sections:

   1. Check the **Sending Statistics** metrics to understand delivery success:

         | Metric | What it means | What to look for |
         |---|---|---|
         | Targeted | Number of profiles qualified for the audience | Should include your test profile |
         | Sends | Total push notifications attempted | Should match your API calls |
         | Delivered | Reported delivery metric | Compare with Sends; verify device rendering separately |
         | Send errors | Push notifications that failed to send | Investigate the error reasons |
         | Send exclusions | Profiles excluded by Adobe Journey Optimizer | Check if your profile was excluded |

   1. If **Send errors** > 0, check the **Error Reasons** table for FCM errors:

         | Common Error | Meaning | Resolution |
         |---|---|---|
         | Invalid / unregistered token | FCM token is invalid or the app was uninstalled | Obtain the current device token and forward it using `MobileCore.setPushIdentifier(token)` |
         | Token not found | No valid FCM token is associated with the profile | Verify that `pushNotificationDetails` contains the current token |
         | Sender ID mismatch | Token was issued for a different Firebase project | Align the FCM credentials with the app's Firebase project |
         | Invalid argument | Payload was rejected by FCM | Validate the `fcm` payload structure |
         | Network timeout | Unable to reach FCM | Transient issue; retry the API call |

   1. If **Send exclusions** > 0, check the **Excluded Reasons** table:

         | Common Exclusion | Meaning | Resolution |
         |---|---|---|
         | Profile opted out | User has opted out of notifications | Check profile consent status |
         | Token denylisted | Token marked as invalid | Forward the current FCM token or check denylist status |
         | Profile not eligible | Profile does not meet campaign criteria | Review campaign audience rules |

Learn more in the [Live activity campaign report page](../reports/campaign-global-report-cja-activity.md).

+++

+++ 2. Check message feedback events in profile

1. Navigate to **Customer** > **Profiles** in Journey Optimizer.
1. Search for and open the profile.
1. Select the **Events** tab.
1. Filter or search for events with `eventType = "message.feedback"`.
1. Locate feedback events for the campaign and API call timestamps you are investigating.
1. Review the following key fields:

   | Field | Possible Values | What it means |
   |---|---|---|
   | `feedbackStatus` | `sent`, `error`, `denylist` | Delivery outcome from service provider |
   | `serviceProvider` | `fcm` | FCM handled Android push delivery |
   | `errorCode` | Provider error code or `null` | FCM-specific error code if delivery failed |
   | `errorMessage` | Error description or `null` | Human-readable error message |

1. **If `feedbackStatus: "error"`:**
   * Inspect `errorCode` and `errorMessage` and apply the corresponding FCM resolution from step 1.

1. **If no feedback event is found:**
   * The push notification may not have been attempted or feedback may not yet be available.
   * Check whether the profile was excluded in campaign reports, as described in step 1.

**If `feedbackStatus` is `sent`:** FCM accepted the notification. This does not confirm that the device rendered the Live activity. Continue with the device-side checks below.

+++

+++ 3. Inspect FCM delivery in Assurance

Use standard Assurance on a connected Android test device. There is no dedicated Live Activities plugin view for Android.

1. Open an Assurance session and keep it active during the API call.
1. Execute the API call with `event_type` set to `start`, `update`, or `end`.
1. In the **Events** list, inspect available push-delivery events for the request to FCM and its response.
1. Check whether FCM accepted or rejected the request, and inspect any reported error details.
1. For rejected requests, use the FCM error reasons in step 1 to check the token, Firebase project credentials, and payload. If provider events are unavailable in the session, use `message.feedback` events and campaign reports.

+++

+++ 4. Proceed to additional diagnostic checks

1. Check the **Live activity lifecycle** section in the campaign report:

   | Metric | What to check |
   |---|---|
   | Remote starts | Should show count of API-triggered starts |
   | Updates | Should show count of update events |
   | Ends | Should show count of end events |
   | Totals count | Overall Live activity event volume |

   If these metrics are zero or do not match your API calls, investigate campaign processing and FCM delivery using reports and feedback events.

1. If Adobe shows successful delivery but the device does not display or update the Live activity:

   * Inspect Android app logs for push-handling and Live activity rendering errors.
   * Confirm that notifications are allowed and that promoted notifications are permitted using `canPostPromotedNotifications()`.
   * Verify that `POST_NOTIFICATIONS` and `POST_PROMOTED_NOTIFICATIONS` permissions are granted and the channel identified by `notification_channel_id` exists.
   * Ensure that `timestamp` is newer than the last processed event and that `notification_id` has not changed. For broadcasts, also verify the device's subscription to `topic_name`.
   * Confirm that the app is not force-stopped.
   * Confirm device has network connectivity.
   * Test on multiple devices to rule out device-specific issues.
   * Verify that the device runs Android 16.1 (API level 36.1) or later and the app uses `targetSdk 36`.
   * Check that `content_state` keys and value types match the app's style provider.

+++

+++ 5. Escalation to Adobe Support

If you have completed all steps and the issue remains unresolved, contact Adobe Customer Care with:

**Required information:**

* Campaign ID and name
* Profile namespace and ID
* `notification_id` and `event_type` from the API payload; for broadcasts, also include `topic_name` and the audience ID
* Timestamps of API calls
* Campaign report screenshots showing Sending Statistics, Error Reasons, and Excluded Reasons
* Relevant profile `message.feedback` events, including FCM error codes and messages
* Assurance session details and relevant event screenshots
* API request payload and response, with credentials and device tokens redacted
* Android package name, Firebase project and sender ID, and FCM credential configuration details; do not include private keys
* Android OS version, device model, notification permission status, and relevant app logs
    
+++

>[!TAB Android]

**Pre-checks**

* **Previous Scenarios Validated:**
   * Profile exists with correct `liveActivityPushNotificationDetails`
   * Campaign surface and Activity type are correct
   * API payload is valid with current timestamp
   * Update tokens are synced (for update/end events)

* **API Call Confirmed:**

   * The API call returned HTTP 200 (success)
   * Campaign ID and recipient details are correct

### Debugging steps

+++ 1. Check campaign reports

1. Navigate to your **Live activity Campaign**.
1. Click the **Reports** button.
1. Select **View all time report**.
1. Review the following sections:

   1. Check the **Sending Statistics** metrics to understand delivery success:

         | Metric | What it means | What to look for |
         |-|-|-|
         | Targeted | Number of profiles qualified for the audience | Should include your test profile |
         | Sends | Total push notifications attempted | Should match your API calls |
         | Delivered | Successfully delivered to devices | Compare with Sends to see success rate |
         | Send errors | Push notifications that failed to send | High numbers|
         | Send exclusions | Profiles excluded by Adobe Journey Optimizer | Check if your profile was excluded |

   1. If Send errors > 0, check the **Error Reasons** table for specific error codes and messages:

         | Common Error | Meaning | Resolution |
         |-|-|-|
         | Invalid token | Push token is invalid or expired | Re-register Live activity tokens from device |
         | Token not found | No valid token associated with profile | Verify `liveActivityPushNotificationDetails` exists |
         | APNs rejected | Apple Push Notification service rejected the push | Check APNs certificate, bundle ID, environment |
         | Network timeout | Unable to reach APNs | Transient issue; retry the API call |

   1. If **Send exclusions** > 0, check the **Excluded Reasons** table:

         | Common Exclusion | Meaning | Resolution |
         |-|-|-|
         | Profile opted out | User has opted out of notifications | Check profile consent status |
         | Token denylisted | Token marked as invalid | Re-register token or check denylist status |
         | Profile not eligible | Profile does not meet campaign criteria | Review campaign audience rules |

Learn more in the [Live activity campaign report page](../reports/campaign-global-report-cja-activity.md).

+++

+++ 2. Check message feedback events in profile

1. Navigate to **Customer** > **Profiles** in Journey Optimizer.
1. Search for and open the profile.
1. Select the **Events** tab.
1. Filter or search for events with `eventType = "message.feedback"`.
1. Look for feedback events matching your Live activity's `liveActivityID` and `event` type.
1. Review the following key fields:

   | Field | Possible Values | What it means |
   |---|---|---|
   | `feedbackStatus` | `sent`, `error`, `denylist` | Delivery outcome from service provider |
   | `serviceProvider` | `apns/apnsSandbox` | Should be APNs for iOS Live activities |
   | `errorCode` | Numeric code or `null` | APNs-specific error code if failed |
   | `errorMessage` | Error description or `null` | Human-readable error message |

1. **If `feedbackStatus: "error"`:**
   * Check the `errorCode` and `errorMessage` for specific APNs errors
   * Common APNs errors include expired token, invalid certificate, wrong bundle ID

1. **If no feedback event found:**
   * The push notification may not have been attempted
   * Check if profile was excluded in Campaign Reports as detailed in Step 1 above.

+++

+++ 3. Verify Live activity delivery to APNs in Assurance

1. Open your Assurance session, it must be active during the API call.
1. Execute the API call (start, update, or end).
1. In the **Event List**, look for Live activity delivery events.
1. Search for events related to APNs push delivery.
1. Check for the following indicators:
   * **Push request to APNs**: Confirms Adobe sent the push to Apple's servers
   * **APNs response**: Shows whether APNs accepted or rejected the push
   * **Delivery status**: Success or failure indication
1. If issues are found, refer to the following common APNs delivery issues:

   | Issue | Symptom in Assurance | Resolution |
   |-|-|-|
   | APNs certificate expired | Authentication error | Renew and upload new APNs certificate |
   | Wrong environment (dev vs prod) | Token mismatch error | Ensure certificate matches app build type |
   | Bundle ID mismatch | Invalid bundle identifier | Verify certificate bundle ID matches app |
   | Token expired | InvalidToken error from APNs | Re-register Live activity tokens |
   | Rate limiting | Too many requests | Reduce API call frequency |

+++
  
+++ 4. Proceed to additional diagnostic checks

1. Check Live activity Lifecycle metrics in Campaign Report.

   In the campaign report, review the **Live activity lifecycle** section:

   | Metric | What to check |
   |-|-|
   | Remote starts | Should show count of API-triggered starts |
   | Updates | Should show count of update events |
   | Ends | Should show count of end events |
   | Totals count | Overall Live activity event volume |

   If these metrics are zero or do not match your API calls, there is a delivery issue between Adobe and APNs.

1. If Adobe shows successful delivery but device does not show the Live activity:

   * Check iOS device logs for Live activity errors.
   * Verify app is in foreground or background (not terminated).
   * Confirm device has network connectivity.
   * Test on multiple devices to rule out device-specific issues.
   * Verify iOS version is 16.1 or later.

+++

+++ 5. Escalation to Adobe Support

If you have completed all steps and the issue remains unresolved, contact Adobe Customer Care with:

**Required information:**

* Campaign ID and name
* Profile namespace and ID
* `liveActivityID` from API payload
* Timestamps of API calls
* Screenshots of:
* Campaign Reports (Sending Statistics, Error Reasons, Excluded Reasons)
* Profile Events (`liveActivity.updateToken`, `message.feedback`)
* Assurance session showing delivery events
* Complete API request payload
* APNs certificate details (expiration, environment, bundle ID)
    
+++


>[!ENDTABS] 

## Unitary-specific scenarios

>[!NOTE]
>
> * [Scenario 4](#scenario-4-live-activity-update-token-not-synced) applies to iOS only. Android uses the same FCM registration token to start, update, and end a unitary Live activity; no per-instance update token is required. 
> * For Android update or end issues, follow [Scenario 1](#scenario-1-profile-or-push-token-issues), [Scenario 2](#scenario-2-campaign-configuration-and-payload-issues), and [Scenario 3](#scenario-3-delivery-failures-and-error-analysis).
> * [Scenario 5](#scenario-5-checking-execution-status-via-the-api), which covers execution status checks, applies to both iOS and Android.

### Scenario 4: Live activity update token not synced {#scenario-4-live-activity-update-token-not-synced}

[!BADGE Applies to iOS only]{type=Positive}

The Live activity starts successfully on the device, but subsequent `update` or `end` API calls (returning HTTP 200) fail to update or dismiss the Live activity. This occurs when the **Live activity update token** is not properly synced to Adobe's system.

**Understanding update tokens**

When a Live activity starts on a device, iOS generates a unique update token for that specific Live activity instance. This token is required for:

* Sending updates to the Live activity
* Ending the Live activity remotely

Each Live activity instance has its own unique update token. Adobe needs this token to deliver update and end events.

**Expected behavior**

For update and end events to work, the following must occur:

1. Live activity starts successfully on the device.
1. Device generates an update token for that Live activity instance.
1. Mobile SDK captures and sends the update token to Adobe.
1. Update token is synced and stored in Adobe's system.
1. Subsequent API calls for update/end use this token for delivery.

**Pre-checks:**

* **User Permission**: The first time a Live activity starts on a device, iOS displays a system prompt: "Allow [App Name] to provide Live activity updates?" The user **must tap "Allow"** for update tokens to be generated and synced. If the user taps "Do not Allow", no update tokens are created and update/end requests will fail. This is a one-time permission per app.
* **Profile and Campaign Validation**: Complete [Scenario 1](#scenario-1-profile-or-push-token-issues) and [Scenario 2](#scenario-2-campaign-configuration-and-payload-issues) checks to ensure profile, tokens, and campaign configuration are correct.

### Debugging steps

+++ Verify update token sync in Assurance

1. Open your Assurance session.
1. Ensure the session was active when the Live activity started on the device.
1. Filter or search for events with `eventType = "liveActivity.updateToken"`.
1. Select the event and inspect the payload:

   * Verify the `token` field contains a valid update token string.
   * Check the `liveActivityID` matches your Live activity instance.
   * Confirm the `activityType` matches your `attributes-type`.

1. If event is not found:

   * The update token was not generated or captured by the SDK.
   * Check if user granted Live activity permissions.
   * Verify the Live activity actually started successfully on the device.
   * Confirm the mobile SDK is properly integrated to capture update tokens.

1. If event is found, proceed to Step 2.

+++

+++ 2. Verify update token in profile events

1. Navigate to **Customer** > **Profiles** in Journey Optimizer.
1. Search for and open the profile.
1. Select the **Events** tab.
1. Look for `liveActivity.updateToken` events.
1. Check the event details:

   * Verify the timestamp is recent (matches when Live activity started).
   * Confirm the `token` and `liveActivityID` are present.
   * Ensure the `activityType` is correct.

1. If event is not found in profile:

   * The update token event may not have been ingested to the profile yet.
   * Wait 5-10 minutes and re-check.
   * If still missing after 15 minutes, there may be an event ingestion issue.

1. If event is found, the update token has been synced. You can proceed to Step 3.

+++

+++ 3. Check Live activity delivery events in Assurance

1. In your Assurance session, execute an update or end API call.
1. In the **Event List**, look for Live activity delivery events (APNs push events).
1. Check for events indicating:
   * Push notification sent to APNs.
   * Response from APNs (success or error).
   * Delivery confirmation.
1. If APNs delivery event is present: The push notification was sent. If the device still does not update, the issue may be on the device side (app not handling the push, network issues, etc.).
1. If APNs delivery event is missing: The update token may not be properly stored or associated with the profile in Adobe's system.
1. If error events are present: Inspect the error details for specific failure reasons (invalid token, APNs rejected, etc.).

+++

## Scenario 5: Checking execution status via the API {#scenario-5-checking-execution-status-via-the-api}

[!BADGE Applies to unitary (1:1) use cases only]{type=Informative}

After triggering a unitary Live activity, the **GET Message Execution API** returns the current state of the execution. Use it to confirm whether an execution is queued, in progress, completed, or failed — without waiting for the feedback event to land in the dataset.

The `executionId` is the message ID returned in the trigger response. For unitary executions, it is prefixed with `HUOC-`.

### Endpoint and example request

**Endpoint**: `GET https://cjm.adobe.io/imp/message/executions/{executionId}`

```bash
curl --location 'https://cjm.adobe.io/imp/message/executions/HUOC-123456' \
  --header 'x-gw-ims-org-id: <IMS_ORG_ID>' \
  --header 'Authorization: Bearer <ACCESS_TOKEN>' \
  --header 'x-sandbox-name: <SANDBOX_NAME>' \
  --header 'x-sandbox-id: <SANDBOX_UUID>' \
  --header 'x-api-key: <API_KEY>'
```

### HTTP response codes

| Code | Meaning |
|------|---------|
| 200 OK | Execution found and returned successfully |
| 401 Unauthorized | Missing or invalid Bearer token |
| 403 Forbidden | Valid token but insufficient permissions |
| 404 Not Found | Execution ID does not exist |

### Execution status values

The `status` field in a 200 response indicates execution progress:

| Status | Description |
|--------|-------------|
| `PENDING` | Execution queued but not yet started |
| `INPROGRESS` | Execution is currently being processed |
| `COMPLETED` | Execution finished successfully |
| `FAILED` | Execution encountered an error |

The 200 response also returns `executionType` (`unitary` or `batch`), `executionRunMode` (`default` or `test`), and a `source` block with metadata (`campaignId`, `journeyId`, `batchInstanceId`, asset info) tying the execution back to the triggering campaign or journey.

## Broadcast-specific scenarios

>[!NOTE]
>
> Broadcast delivery differs by platform:
>
> * **iOS** uses an Apple push channel (`input-push-channel`) that must match `liveActivityData.channelID` in the start payload.
> * **Android** uses an FCM topic (`topic_name`) that the device must subscribe to.

### Scenario 6: Broadcast campaign configuration and payload issues{#broadcast-config}

[!BADGE Applies to Broadcast use cases only]{type=Informative}

This section covers troubleshooting scenarios specific to broadcast Live activities, which require different debugging approaches than unitary campaigns.

When profiles have valid tokens but the Live activity does not appear, update, or behave as expected for audience members, the issue typically stems from one of the following:

* The campaign is not configured as API-triggered Marketing.
* The API payload uses an incorrect broadcast structure (missing `audience` or `input-push-channel`).
* The `content-state` and `attributes` fields do not match the iOS `ActivityAttributes` implementation.
* The `input-push-channel` was not created correctly on the Apple Developer Portal.

This troubleshooting scenario applies to all Live activity events in broadcast campaigns: `start`, `update`, and `end`.

>[!BEGINTABS]

>[!TAB iOS]

**Pre-checks:**

* **Campaign Type**: 
   * Verify that the campaign is created as API-triggered Marketing (required for broadcast/audience-based campaigns). 
   * Confirm that an audience is defined in the campaign configuration.
* **Profile and Token Validation**: Sample multiple profiles from the audience to verify they have valid `liveActivityPushNotificationDetails`. For detailed validation steps, follow [Scenario 1](#scenario-1-profile-or-push-token-issues).

### Debugging steps

+++ 1. Verify campaign audience configuration

1. Open your **API Triggered Marketing Campaign** in Journey Optimizer.
1. Navigate to the **Audience** section and verify:
   * An audience is selected for the campaign.
   * The audience ID matches the one used in your API payload.
   * The audience contains the expected profiles.
1. Navigate to the **Actions** section.
1. Check the **Live activity configuration**:
   * The configuration must be set for the iOS app with the correct bundle identifier.
   * The Activity type must match the `attributes-type` in your API payload. For example, if your payload contains `"attributes-type": "AirplaneTrackingAttributes"`, the campaign must specify this same Activity type.

+++

+++ 2. Validate broadcast API payload structure

The broadcast payload structure differs from unitary campaigns. Verify that your payload follows the correct broadcast format.

**Required fields for broadcast:**

```json
{
   "campaignId": "878a11d4-b519-47bd-8313-fecfee19857b",
   "audience": {
      "id": "8c3dbdea-2957-401f-acf0-3966fba1601e"
   },
   "context": {
      "requestPayload": {
      "aps": {
         "input-push-channel": "FEt0NgvLEfEAAOqA6AXdIQ==",
         "content-available": 1,
         "timestamp": 1771829292,
         "event": "update",
         "attributes-type": "AirplaneTrackingAttributes",
         "content-state": { ... },
         "attributes": { ... }
      }
      }
   }
}
```

**Common payload issues:**

| Field | Requirement | Common Issue |
|-|-|-|
| `campaignId` | Must match the activated Marketing campaign ID | Wrong campaign ID or using Transactional campaign |
| `audience.id` | Must match an existing audience in AEP | Wrong audience ID or audience does not exist |
| `input-push-channel` | Required for broadcast - Unique identifier for this broadcast instance | Missing or does not match `channelID` in `liveActivityData` |
| `timestamp` | Must always be the current/latest Unix epoch time in seconds | Using old/cached timestamp |
| `event` | Must be `"start"`, `"update"`, or `"end"` | Invalid event type |
| `attributes-type` | Must match campaign Activity type | Mismatch or typo |
| `content-available` | Must be `1` | Missing or wrong value |

**Critical broadcast-specific fields:**

* **`input-push-channel`**:
   * Required for all broadcast Live activities.
   * Serves as a unique identifier for this specific broadcast instance.
   * All profiles in the audience receive Live activities linked to this channel.
   * Must match the `channelID` in `liveActivityData.channelID` (see Step 3).
   * Must be created for the `appID` on the Apple Developer Portal by the client.
   * Only channels created for the specific `appID` can be used for broadcasting Live activity on that app.

* **`audience.id`**:
   * Must reference a valid audience segment created in Adobe Experience Platform.
   * All profiles in this audience are targeted for the Live activity.
   * The audience must be activated and contain profiles with valid `liveActivityPushNotificationDetails`.

**Always use the latest timestamp:**

* The `timestamp` field must always be the current Unix epoch time (in seconds) for every API call.
* This requirement applies to all event types: `start`, `update`, and `end`.
* **Critical for updates/end**: Using stale timestamps causes update and end requests to fail.
* Generate a fresh timestamp for every broadcast API call.

**Optional fields:**

* `dismissal-date`: Unix epoch time for auto-dismissal (only relevant for `end` events)
* `alert`: Object with `title` and `body` for notification

Refer to the [Adobe Journey Optimizer Messaging API documentation](https://developer.adobe.com/journey-optimizer-apis/references/messaging) for complete API specifications.

+++

+++ 3. Align content-state, attributes, and input-push-channel with iOS implementation

Ensure that the payload fields match your iOS app's `ActivityAttributes` implementation, and that the `input-push-channel` matches the `channelID` in `liveActivityData`.

   1. Review your iOS ActivityAttributes definition.

   Your custom `ActivityAttributes` struct must implement Adobe's `LiveActivityAttributes` protocol:

   ```swift
   struct AirplaneTrackingAttributes: LiveActivityAttributes {
      public struct ContentState: Codable, Hashable {
         var journeyProgress: Int
      }
      
      // Adobe SDK requirement
      var liveActivityData: LiveActivityData
      
      // Your custom attributes
      var arrivalAirport: String
      var departureAirport: String
      var arrivalTerminal: String
   }
   ```

   1. Map iOS fields to broadcast API payload.
   
   For all events, include both `attributes` and `content-state`:

   ```json
         {
         "aps": {
            "input-push-channel": "FEt0NgvLEfEAAOqA6AXdIQ==",
            "event": "start",
            "timestamp": 1771829292,
            "attributes-type": "AirplaneTrackingAttributes",
            "content-state": {
            "journeyProgress": 0
            },
            "attributes": {
            "arrivalAirport": "DEL",
            "departureAirport": "MUM",
            "arrivalTerminal": "T1",
            "liveActivityData": {
               "channelID": "FEt0NgvLEfEAAOqA6AXdIQ=="
            }
            }
         }
         }
   ```

**Critical: `input-push-channel` must match `channelID`**

* The `input-push-channel` value at the root of `aps` must exactly match the `channelID` in `liveActivityData`.
* In the example above, both values are `"FEt0NgvLEfEAAOqA6AXdIQ=="`.
* This matching links the broadcast instance to the Live activity data.
* A mismatch causes delivery failures.

**Key validation points:**

* Include all `ContentState` fields in `content-state` for all event types.
* Include all custom `LiveActivityAttributes` fields in `attributes` for start events only.
* For start events, `liveActivityData.channelID` must match `input-push-channel`.
* Field names are case-sensitive and must match exactly.
* Data types must match (String, Int, Bool, nested objects, etc.).
* For update/end events, use the same `input-push-channel` as the original start event.

**Common mistakes:**

| Issue | Impact | Fix |
|-|-|-|
| Missing `input-push-channel` | Broadcast will not work | Add unique channel ID for each broadcast |
| `input-push-channel` does not match `channelID` | Live activity will not start | Ensure both values are identical |
| Different `input-push-channel` for update/end | Update/end will not reach the Live activities | Use same channel ID throughout lifecycle |
| Missing `liveActivityData.channelID` | Live activity will not link to broadcast | Include `channelID` in attributes for start event |
| Missing required field in start event | Live activity will not start | Add all fields from iOS struct |
| Wrong field name (typo/case) | Field ignored or parsing error | Match iOS field names exactly |
| Stale timestamp on update/end | Update/end ignored by devices | Always generate fresh timestamp |

+++

+++ 4. Test with Assurance

Verify API execution and payload delivery using Assurance:

1. Open your Assurance session on a test device that is part of the audience.
1. Execute the broadcast API call.
1. In the **Event List**, look for:
   * Campaign execution events.
   * Live activity delivery events.
   * Error events indicating payload validation failures.
1. Inspect event payloads to confirm:
   * The payload was processed correctly.
   * The `input-push-channel` is present.
   * No validation errors occurred.
   * Live activities were sent to APNs for audience members.

+++

>[!TAB Android]

**Pre-checks:**

* **Campaign type:** Verify that the campaign is **API-triggered Marketing** and has an audience defined.
* **Profile and token validation:** Sample several audience profiles to verify that they have valid `pushNotificationDetails` with `platform: "fcm"`. Follow the Android checks in [Scenario 1](#scenario-1-profile-or-push-token-issues).
* **Topic subscription:** Confirm that the test device is subscribed to the FCM topic used for the broadcast.

### Debugging steps

+++ 1. Verify campaign audience configuration

1. Open your **API-triggered Marketing campaign** in Journey Optimizer.
1. Navigate to the **Audience** section and verify:
   * An audience is selected for the campaign.
   * The audience ID matches the one used in your API payload.
   * The audience contains the expected profiles.
1. Navigate to the **Actions** section.
1. Check that the **Live activity configuration** targets the correct Android package and uses the matching FCM credentials. Android does not use an Activity type or `attributes-type` field.

+++

+++ 2. Validate broadcast API payload structure

Android broadcasts use an FCM topic. Include `audience.id` and place the `fcm` object under `context.requestPayload`, rather than under an individual recipient.

**Broadcast start payload example:**

```json
{
   "requestId": "your-request-id",
   "campaignId": "your-marketing-campaign-id",
   "audience": {
      "id": "your-audience-id"
   },
   "context": {
      "requestPayload": {
         "fcm": {
            "topic_name": "flight_DL321",
            "notification_id": "flight-DL-321",
            "notification_channel_id": "live_updates_channel",
            "timestamp": 1771829292,
            "priority": "PRIORITY_HIGH",
            "event_type": "start",
            "title": "Flight DL-321",
            "body": "Boarding starts shortly",
            "critical_text": "25 min",
            "content_state": {
               "custom_key_template_type": "progress",
               "custom_key_journey_start": "DEL",
               "custom_key_journey_progress": 10,
               "custom_key_journey_end": "MUM"
            }
         }
      }
   }
}
```

Replace the sample timestamp with the current Unix epoch time in seconds. Adapt the `content_state` keys to your app's style provider.

**Common payload issues:**

| Field | Requirement | Common Issue |
|---|---|---|
| `campaignId` | Must match the activated Marketing campaign ID | Wrong campaign ID or using Transactional campaign |
| `audience.id` | Must match the audience configured in the campaign | Wrong audience ID or missing audience |
| `topic_name` | Must be non-empty and unchanged across start, update, and end | Missing topic is rejected as malformed; changed topic breaks update/end targeting |
| `notification_id` | Must remain unchanged across the activity lifecycle | Update or end targets a different notification |
| `notification_channel_id` | Must match a notification channel created by the app | Missing or mismatched channel |
| `timestamp` | Epoch seconds; must be greater than the previous value for the same topic | Older or equal timestamps are ignored |
| `event_type` | Must be `"start"`, `"update"`, or `"end"` | Invalid lifecycle event |
| `content_state` | Must use keys and value types supported by the app's style provider | Unsupported keys or incorrect types |

**Critical broadcast-specific fields:**

* **`topic_name`:** Identifies the FCM topic subscribed to by the target devices. Include the same non-empty value in every start, update, and end request.
* **`audience.id`:** Identifies the campaign's audience in Adobe Experience Platform. Verify its membership and sample profiles for valid `pushNotificationDetails`.

**Timestamp and optional fields:**

* Generate a fresh `timestamp` in epoch seconds for every event, and ensure that it is strictly greater than the last value for the same topic. Older or equal values are ignored.
* `when` optionally sets the notification's displayed time in epoch seconds. It does not control message ordering.
* For `event_type: "end"`, `dismiss_after` optionally specifies how many seconds the completed activity remains visible before removal. It is a duration, not an epoch timestamp.

Refer to the [Adobe Journey Optimizer Messaging API documentation](https://developer.adobe.com/journey-optimizer-apis/references/messaging) for complete API specifications.

+++

+++ 3. Verify topic subscription and app rendering

1. Confirm that the test device subscribes to the exact topic specified in `topic_name`, using `FirebaseMessaging.getInstance().subscribeToTopic(topic)`.
1. Verify that the subscription succeeds and that the app reports it through the topic-subscription tracking API supported by its installed Adobe Live Activities extension.
1. Keep `topic_name` and `notification_id` unchanged across start, update, and end events.
1. Verify that `content_state` keys and value types match the app's style provider.
1. Check that notification permissions are granted and that `notification_channel_id` matches a channel created by the app.

**Common mistakes:**

| Issue | Impact | Fix |
|---|---|---|
| Missing or empty `topic_name` | Request is rejected as malformed | Include a non-empty topic in every lifecycle request |
| Device not subscribed to the topic | Device does not receive broadcast events | Subscribe to the exact topic and verify subscription success |
| Changed topic or notification ID | Update/end does not target the original activity | Keep both values unchanged throughout the lifecycle |
| Unsupported `content_state` keys or types | Content is missing or rendered incorrectly | Match the app's style-provider mapping |
| Older or equal `timestamp` | Event is ignored | Use a value greater than the last processed timestamp |

See the [Android broadcast payload example](create-mobile-live.md) for additional fields and examples.

+++

+++ 4. Test with Assurance

Use standard Assurance on a connected Android test device that is part of the audience and subscribed to the broadcast topic. There is no dedicated Live Activities plugin view for Android.

1. Open your Assurance session before executing the broadcast API call.
1. Send start, update, and end requests with the same `topic_name` and `notification_id` and increasing timestamps.
1. In the **Events** list, inspect available SDK and delivery events for payload-processing errors.
1. Confirm that the payload contains the intended `fcm` object, `topic_name`, and `event_type` values.
1. Review campaign reports and available `message.feedback` events to confirm FCM delivery outcomes. The Android `serviceProvider` value is `fcm`.
1. If FCM accepts the message but the device does not render the activity, inspect topic subscription, notification permissions, channel configuration, and app logs. Provider acceptance does not confirm device rendering.

+++

>[!ENDTABS]

## Scenario 7: Profile not in audience or stale audience snapshot {#scenario-7-profile-not-in-audience-or-stale-audience-snapshot}

In this scenario, the campaign and payload are correctly configured, but specific profiles are not receiving the Live activity. This typically occurs when:

* The profile is not a member of the audience linked to the campaign.
* The audience is a batch audience and contains an outdated snapshot of profile data.
* The profile's push-token details (`liveActivityPushNotificationDetails` on iOS or `pushNotificationDetails` on Android) were updated recently but have not been reflected in the audience snapshot yet.

This troubleshooting scenario applies specifically to broadcast campaigns using audience-based targeting.

**Understanding audience evaluation**

Adobe Experience Platform uses different audience evaluation methods that determine when profile updates are reflected in the audience:

| Method | Evaluation Frequency | Data Freshness | Best For |
|-|-|-|--|
| Batch | Once daily (scheduled) | May be up to 24 hours stale | Large audiences, non-time-sensitive |
| Streaming | Real-time (on profile changes) | Near real-time for updated profiles | Time-sensitive, requires profile updates |
| Edge | Real-time at edge locations | Near real-time | Edge-evaluated use cases |

>[!BEGINTABS]

>[!TAB iOS]

**Pre-checks:**

* **Campaign and Payload Validation**:
   * Complete the checks in [this scenario](#broadcast-config) to ensure the campaign and payload are correct. 
   * Verify that the `audience.id` in the API payload matches the campaign configuration.
* **Profile Exists**: Confirm that the profile exists in AEP with valid `liveActivityPushNotificationDetails`.

### Debugging steps

+++ 1. Verify profile is in audience

First, confirm whether the profile that should receive the Live activity is actually part of the audience.

1. Navigate to **Audiences** in Adobe Experience Platform.
1. Search for and open the audience using the `audience.id` from your campaign.
1. Click **Browse** or **Sample profiles** to view audience members.
1. Search for your test profile using the namespace and identity value.
1. **If profile is not found in the audience:**
   * The profile does not meet the audience criteria or segment rules.
   * Review the audience definition to understand the membership requirements.
   * Update the profile data or audience definition to include the profile.
   * Wait for audience evaluation to complete (see Step 2).
1. **If profile is found in the audience:** Proceed to Step 2 to check data freshness.

+++

+++ 2. Check audience evaluation type and schedule

Identify whether the audience uses batch or streaming evaluation, as this determines data freshness.

1. On the **Audience details** page, check the **Evaluation method**:
   * **Batch**: Evaluated once daily on a schedule.
   * **Streaming**: Evaluated in real-time when profile updates occur.
   * **Edge**: Evaluated at edge locations in real-time.

Follow the appropriate troubleshooting steps based on the evaluation method:

**If the audience uses Batch evaluation:**

1. **Understand batch audience limitations:**
   * Batch audiences are evaluated once per day (typically overnight).
   * The audience snapshot may be up to 24 hours old.
   * If a profile recently registered Live activity tokens, those tokens may not be in the current snapshot.
   * Updates to profiles will not be reflected until the next batch evaluation.

1. **Check when last evaluation occurred:**
   * In the audience details, look for the **Last evaluation** timestamp.
   * If the profile's `liveActivityPushNotificationDetails` were updated after this timestamp, the audience has stale data.

1. **Resolve stale data:**
   1. **Option 1: Wait for scheduled batch evaluation**
      * The next batch evaluation will include the updated profile data.
      * This happens automatically once per day.
      * Best for non-urgent scenarios.

   1. **Option 2: Trigger on-demand audience evaluation**
      1. Navigate to **Audiences** in AEP.
      1. Select your audience.
      1. Click **Evaluate now** or **Activate on demand**.
      1. Wait for evaluation to complete (this can take several minutes to hours depending on audience size).
      1. Verify that the profile now has updated data in the audience snapshot.
      1. Retry the broadcast API call.

**If the audience uses Streaming evaluation:**

1. **Understand streaming audience behavior:**
   * Streaming audiences evaluate in real-time when profile updates occur.
   * **New profiles**: Qualify shortly after creation if they meet segment criteria.
   * **Updated profiles**: Qualify or disqualify shortly after being updated.
   * **Existing unchanged profiles**: Are not re-evaluated unless an update occurs.

1. **Identify the issue:**
   * If a profile already exists and meets the segment criteria, but no update occurs on that profile, it may not be added to a newly created streaming audience.
   * The profile must receive an update (any attribute change) to trigger re-evaluation.

1. **Resolve the issue:**
   * **For new profiles**: They automatically qualify if criteria are met. No action needed.
   * **For existing profiles without recent updates:**
      * Make a minor update to the profile (e.g., update a timestamp field).
      * This triggers streaming evaluation and adds the profile to the audience.
      * Alternative: Use a batch audience or edge audience for existing profiles.

+++

>[!TAB Android]

**Pre-checks:**

* **Campaign and Payload Validation**:
   * Complete the Android checks in [Scenario 6](#broadcast-config) to ensure the campaign and payload are correct.
   * Verify that the `audience.id` in the API payload matches the campaign configuration.
* **Profile Exists**: Confirm that the profile exists in AEP with valid `pushNotificationDetails`, including the current FCM registration token, an `appId` matching the Android package name, `platform: "fcm"`, and `denylisted: false`. Follow the Android checks in [Scenario 1](#scenario-1-profile-or-push-token-issues).
* **Topic Subscription**: Confirm that the device is subscribed to the exact FCM topic specified in `topic_name`. Audience membership does not subscribe the device to the topic. Follow the Android topic-subscription checks in [Scenario 6](#broadcast-config).

### Debugging steps

+++ 1. Verify profile is in audience

First, confirm whether the profile associated with the Android device is actually part of the audience.

1. Navigate to **Audiences** in Adobe Experience Platform.
1. Search for and open the audience using the `audience.id` from your campaign.
1. Click **Browse** or **Sample profiles** to view audience members.
1. Search for your test profile using the namespace and identity value.
1. **If profile is not found in the audience:**
   * The profile does not meet the audience criteria or segment rules.
   * Review the audience definition to understand the membership requirements.
   * Update the profile data or audience definition to include the profile.
   * Wait for audience evaluation to complete (see Step 2).
1. **If profile is found in the audience:** Proceed to Step 2 to check data freshness.

+++

+++ 2. Check audience evaluation type and schedule

Identify whether the audience uses batch, streaming, or edge evaluation, as this determines data freshness. Audience evaluation does not register FCM tokens or subscribe devices to topics.

1. On the **Audience details** page, check the **Evaluation method**:
   * **Batch**: Evaluated once daily on a schedule.
   * **Streaming**: Evaluated in real-time when profile updates occur.
   * **Edge**: Evaluated at edge locations in real-time.

Follow the appropriate troubleshooting steps based on the evaluation method:

**If the audience uses Batch evaluation:**

1. **Understand batch audience limitations:**
   * Batch audiences are evaluated once per day (typically overnight).
   * The audience snapshot may be up to 24 hours old.
   * If a profile recently registered or refreshed its FCM registration token, the updated `pushNotificationDetails` may not be in the current snapshot.
   * Updates to profiles will not be reflected until the next batch evaluation.

1. **Check when last evaluation occurred:**
   * In the audience details, look for the **Last evaluation** timestamp.
   * If the profile's `pushNotificationDetails` were updated after this timestamp, the audience snapshot may not include the current FCM registration token.

1. **Resolve stale data:**
   1. **Option 1: Wait for scheduled batch evaluation**
      * The next batch evaluation will include the updated profile data.
      * This happens automatically once per day.
      * Best for non-urgent scenarios.

   1. **Option 2: Trigger on-demand audience evaluation**
      1. Navigate to **Audiences** in AEP.
      1. Select your audience.
      1. Click **Evaluate now** or **Activate on demand**.
      1. Wait for evaluation to complete (this can take several minutes to hours depending on audience size).
      1. Verify that the profile now has updated data in the audience snapshot.
      1. Retry the broadcast API call.

**If the audience uses Streaming evaluation:**

1. **Understand streaming audience behavior:**
   * Streaming audiences evaluate in real-time when profile updates occur.
   * **New profiles**: Qualify shortly after creation if they meet segment criteria.
   * **Updated profiles**: Qualify or disqualify shortly after being updated.
   * **Existing unchanged profiles**: Are not re-evaluated unless an update occurs.

1. **Identify the issue:**
   * If a profile already exists and meets the segment criteria, but no update occurs on that profile, it may not be added to a newly created streaming audience.
   * The profile must receive an update (any attribute change) to trigger re-evaluation.

1. **Resolve the issue:**
   * **For new profiles**: They automatically qualify if criteria are met. No action needed.
   * **For existing profiles without recent updates:**
      * Make a minor update to the profile (e.g., update a timestamp field).
      * This triggers streaming evaluation and adds the profile to the audience.
      * Alternative: Use a batch audience or edge audience for existing profiles.

+++


>[!ENDTABS]

 
## Advanced: Debugging via dataset queries {#advanced-debugging-via-dataset-queries}

>[!NOTE]
>
> These queries apply to both iOS and Android. Both platforms use `message.feedback` events in the **AJO Message Feedback Event Dataset**, with the same schema paths and `feedbackStatus` values shown below. 
>
>A `sent` status indicates hand-off to the push provider: APNs on iOS or FCM on Android. 

>[!BEGINSHADEBOX]

**Audience**: Developers and data engineers. Requires SQL access to Journey Optimizer datasets via Adobe Experience Platform Query Service.

**When to use**: Assurance is limited to test devices connected during an active session. Use dataset queries to investigate issues reported by production end-users, or to audit delivery history after the fact. The dataset exposes the same lifecycle and failure information as the Assurance plugin.

>[!ENDSHADEBOX]

## Locating the dataset

1. In Journey Optimizer navigate to **Data Management** `>` **Datasets**.

1. Enable the **Show system datasets** toggle, and open **AJO Message Feedback Event Dataset**. 

Note the exact table name shown on the detail page. The queries below use `ajo_message_feedback_event_dataset`,  replace it with your actual table name if it differs.

## Query by Live Activity ID

Use this when you know the Live Activity ID (for example, an order UUID or shipment tracking ID) and want every feedback event tied to it across the full lifecycle.

```sql
SELECT
  timestamp,
  identitymap,
  _experience.customerJourneyManagement
    .messageDeliveryfeedback.feedbackStatus AS status,
  _experience.customerJourneyManagement
    .messageDeliveryfeedback.messageFailure.reason AS failure_reason,
  _experience.customerJourneyManagement
    .pushChannelContext.liveActivity.event AS la_event,
  _experience.customerJourneyManagement
    .messageExecution.campaignID AS campaign_id,
  _experience.customerJourneyManagement
    .messageExecution.batchInstanceID AS batch_id,
  _id
FROM ajo_message_feedback_event_dataset
WHERE
  _experience.customerJourneyManagement
    .pushChannelContext.liveActivity.liveActivityID
    = '<YOUR_LIVE_ACTIVITY_ID>'
  AND eventtype = 'message.feedback'
ORDER BY timestamp ASC
```

## Query by ECID

Use this when the affected profile's ECID is known. Replace `<YOUR_ECID>` with the ECID value retrieved from the profile.

```sql
SELECT
  timestamp,
  _experience.customerJourneyManagement
    .messageDeliveryfeedback.feedbackStatus AS status,
  _experience.customerJourneyManagement
    .messageDeliveryfeedback.messageFailure.reason AS failure_reason,
  _experience.customerJourneyManagement
    .pushChannelContext.liveActivity.event AS la_event,
  _experience.customerJourneyManagement
    .pushChannelContext.liveActivity.liveActivityID AS la_id,
  _experience.customerJourneyManagement
    .messageExecution.campaignID AS campaign_id,
  _id
FROM ajo_message_feedback_event_dataset
WHERE
  identityMap['ECID'][0].id = '<YOUR_ECID>'
  AND eventtype = 'message.feedback'
ORDER BY timestamp ASC
```

>[!NOTE]
>
> `identityMap` is a structured MAP type, not a string. Use the array and struct accessor syntax shown above. String functions such as `LIKE` will return a `DATATYPE_MISMATCH` error.
>
></br>
> The Message Feedback Event Dataset stores only ECID in its `identityMap`. If the affected profile is identified by a custom namespace rather than ECID, resolve the ECID first: navigate to **Profiles** in AEP, search for the profile using the custom namespace and identity value, and retrieve the ECID from the profile's identity details. Use that ECID value in the query above.

## feedbackStatus values

| Value | Meaning |
|-------|---------|
| `sent` | Handed off to the push provider (APNs on iOS, FCM on Android); does not confirm device rendering (see below) |
| `error` | Delivery error — inspect `failure_reason` for details |
| `denylist` | Token is invalid, unregistered, or denylisted (for example, an uninstalled app); re-register the device token |
| `exclude` | Profile excluded before send (missing token, consent issue, or typology rules) |
| `delay` | Delivery delayed; will be retried |
| `duplicate` | A repeated send was suppressed by delivery-level deduplication |
| `bounce` | Delivery bounced by the push provider (for example, a hard failure returned for the token) |

>[!NOTE]
>
> For `la_event` field, the dataset records `remotestart`, not `start`, for initial delivery events. Filter accordingly when querying by event type.

## Interpreting the sent status {#interpreting-the-sent-status}

>[!IMPORTANT]
>
>The 8-hour Live activity duration limit applies to iOS only, not Android.


A `feedbackStatus` of `sent` confirms that Journey Optimizer successfully handed the notification to the push provider (APNs on iOS, FCM on Android). It does **not** confirm that the Live activity was rendered on the device.

The dataset does not confirm device rendering after hand-off to the push provider. Device-side failures, such as an OS restriction, a network drop between the provider and the device, or the 8-hour Live activity duration limit being reached on iOS, are not observable from the dataset. This duration limit does not apply to Android.

If `feedbackStatus` is `sent` but no Live activity appears on the device, investigate behavior outside the Journey Optimizer delivery pipeline. Use Assurance or app-level logging, including `logcat` on Android, to diagnose device-side behavior.

{{$include /help/_includes/do-not-localize/mobile-live/ai-augmented-troubleshoot-mobile-live.md}}

