---
solution: Journey Optimizer
product: journey optimizer
title: Troubleshoot Live Activities
description: Learn how to troubleshoot Live Activities in Journey Optimizer for both unitary and broadcast use cases, including profile token issues, campaign configuration, and delivery failures
role: User
level: Intermediate
hide: yes
hidefromtoc: yes
---

# Troubleshoot Live Activities {#troubleshoot-mobile-live}

Live Activities in Adobe Journey Optimizer enable real-time, dynamic updates on iOS lock screens and Dynamic Islands. They can only be triggered and managed through API Triggered Campaigns.

**Use case types:**

* **Unitary**: Individually targeted, transactional (API-triggered Transactional campaigns)
* **Broadcast**: Audience-targeted, mass delivery (API-triggered Marketing campaigns)

A frequent challenge with Live Activities is when the API call to trigger or update a Live Activity returns a **successful response (200 OK)**, but the Live Activity fails to appear or update on the user's device. This disconnect between API confirmation and actual device behavior can occur at multiple points in the delivery pipeline. This guide provides a systematic troubleshooting approach to identify where the delivery is failing, examining each stage from API request validation through device rendering.

## Prerequisites

Before troubleshooting, ensure you have:

* +++ Set up an Assurance session

  Set up an **Assurance session** to capture SDK events and inspect the delivery pipeline. Assurance provides visibility into:

  * Edge Network requests and responses
  * Profile qualification events
  * Push token registration
  * Live Activity lifecycle events

  Learn how to set up Assurance in the [Adobe Experience Platform Assurance documentation](https://experienceleague.adobe.com/en/docs/platform-learn/implement-mobile-sdk/app-implementation/assurance).

  **Note**: For iOS Live Activity, ensure your app is running on a physical iOS device (iOS 16.1 or later) or Xcode Simulator (iOS 16.1 or later).

  +++

* +++ Gather API Triggered Campaign details

  Navigate to your API Triggered Campaign in Journey Optimizer and retrieve:

  * Campaign name
  * Campaign ID found in the URL or campaign properties
  * Campaign version if applicable
  * Surface configuration, iOS app surface used for Live Activity

  +++

* +++ Collect API request information

  When making the API call to trigger the Live Activity, save:

  * API request payload, including profile identifiers and Live Activity data
  * API response including status code, message ID, request ID
  * Timestamp of when the API was called
  * Endpoint used, e.g., `/campaign/{CAMPAIGN_ID}/execute`

  +++

* +++ Identify the test profile

  From your API request, retrieve:

  * Profile namespace, e.g., ECID, email, customer ID
  * Profile ID used in the API call

  Ensure you can look up this profile in Adobe Experience Platform. Learn how to [look up a profile in the Experience Platform documentation](https://experienceleague.adobe.com/en/docs/experience-platform/profile/ui/user-guide.html).

  +++

* +++ Device and app information

  Collect the following from your test device:

  * Device model, e.g., iPhone 14 Pro
  * iOS version
  * App bundle identifier
  * APNs push token
  * Network connectivity status at the time of testing

  +++

## Common scenarios

### Profile or push token issues {#profile-issue}

[!BADGE Applies to both unitary and broadcast use cases]{type=Positive}

The API returns HTTP 200, but the Live Activity does not appear. Common causes:

* Profile does not exist in Adobe Experience Platform.
* Live Activity push token has not been synced to the profile.
* Live Activity push details are synced but contain incorrect configuration, e.g. wrong `appId` or `attributeType`.

**Note for broadcast use cases**: If some profiles in your audience are missing tokens, only those profiles will fail to receive the Live Activity. Sample several profiles from your audience to diagnose token issues. This applies only to remote start events, not update or end events.

#### Pre-checks

* iOS app requirements: 
   * iOS 16.1+
   * `NSSupportsLiveActivities` set to `YES` in `Info.plist`
   * `ActivityAttributes` properly implemented.
* Mobile SDK Integration: 
   * Adobe Experience Platform Mobile SDK (messaging SDK 5.11.0+)
   * `Messaging.registerLiveActivities` implemented and called with Live Activity push token.

#### Debugging steps

1. +++ Verify profile exists in Adobe Experience Platform

   1. In Journey Optimizer, navigate to **Customer** `>` **Profiles**.
   1. Search using namespace and identity value from API request.
   1. If profile is not found, the profile does not exist or ingestion is not completed. Create the profile or wait for ingestion before triggering the Live activity.
   1. If profile is found, proceed to step 2 below to check if the push token is synced.
  
      +++

1. +++ Check if Live Activity push token is synced

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

1. +++ Validate token details on profile

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

### Campaign configuration and payload issues {#payload-issues}

[!BADGE Applies to both unitary and broadcast use cases]{type=Positive}

Profile exists with valid tokens, but Live Activity does not appear. This can be caused by:

* Wrong surface or channel configuration.
* Incorrect API payload structure.
* `content-state` and `attributes` do not match iOS `ActivityAttributes` implementation.
* Stale `timestamp` (critical for update/end).

**Note for broadcast use cases**: Campaign must be **API-triggered Marketing** (not Transactional). Payload uses `audience` instead of individual `profile`. Refer to [this section](#broadcast-config) for broadcast-specific payload structure and to [Adobe Developer documentation](https://developer.adobe.com/journey-optimizer-apis/references/messaging#operation/postIMAudienceMessageExecution) for complete API specifications.

#### Pre-checks

* Campaign is **API-triggered Transactional** (unitary) or **API-triggered Marketing** (broadcast) and **High Throughput** option must be **not** be enabled since it is incompatible with Live Activity.
* Ensure that profile exists and tokens are synced correctly using the [above scenario](#profile-issue).

#### Debugging steps

1. +++ Verify campaign surface configuration

   1. In Journey Optimizer, open your **Campaign** and navigate to the **Actions** menu.
   1. Check your **Live activity configuration**. The surface must be configured for the iOS app with a bundle identifier that matches the `appId` in your profile's `liveActivityPushNotificationDetails`. For example, if your profile has `"appId": "com.example.myapp"`, the surface must target that same app.
   1. Check that the **Activity type** in your campaign configuration matches exactly the `attributeType` in your profile's `liveActivityPushNotificationDetails`. For example, if your profile has `"attributeType": "FoodDeliveryLiveActivityAttributes"`, the campaign must specify this same Activity type.

      +++

1. +++Validate API payload structure
  
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
   * Specifies when the Live Activity should automatically be removed from the device.
   * If not provided on end event, Live Activity remains visible until user dismisses it.
   * Must be a future timestamp (later than `timestamp`).

      +++

1. +++ Align payload with iOS implementation

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
   |-------|--------|-----|
   | Missing `liveActivityData` in attributes | Live Activity will not start | Always include `liveActivityData` object in start event |
   | Missing required field in start event | Live Activity will not start | Add all fields from iOS struct |
   | Wrong field name (typo/case) | Field ignored or parsing error | Match iOS field names exactly |
   | Wrong data type | Parsing error | Match iOS data types |
   | Missing nested object | Incomplete data | Include all nested structures |
   | Including `attributes` in update/end | Unnecessary, but usually ignored | Only include `attributes` in start event |
   | Stale timestamp on update/end | Update/end ignored by device | Always generate fresh timestamp |

   For more examples, refer to [Create Live activity page](create-mobile-live.md).

      +++

1. +++ Test with Assurance

   Verify API execution and payload delivery using Assurance:

   1. Open your Assurance session.
   1. Execute the API call to trigger the Live Activity.
   1. In the **Event List**, check for:
      * Campaign execution events.
      * Live Activity delivery events.
      * Payload validation error events.
   1. Review event payloads to verify:
      * Payload was processed correctly.
      * No validation errors occurred.
      * Live Activity was sent to APNs.

      +++

### Delivery failures and error analysis

[!BADGE Applies to both unitary and broadcast use cases]{type=Positive}

In this scenario, all previous checks have passed:

* Profile exists with [valid Live Activity push tokens](#profile-issue)
* Campaign is correctly [configured with proper payload](#payload-issues)
* [Update tokens are synced](#token-not-synced) (for update/end events, unitary use case only)

But the Live Activity still does not appear, update, or end as expected. The issue may be at the Adobe delivery system level or with the push notification service provider (APNs).

**Note for broadcast use cases**: Reports show metrics across all audience members. Some profiles may succeed while others fail.

**Pre-checks**

* **Previous Scenarios Validated:**
   * Profile exists with correct `liveActivityPushNotificationDetails`
   * Campaign surface and Activity type are correct
   * API payload is valid with current timestamp
   * Update tokens are synced (for update/end events)

* **API Call Confirmed:**

   * The API call returned HTTP 200 (success)
   * Campaign ID and recipient details are correct

#### Debugging steps

1. +++ Check campaign reports

   1. Navigate to your **Live Activity Campaign**.
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
          | Invalid token | Push token is invalid or expired | Re-register Live Activity tokens from device |
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

1. +++ Check message feedback events in profile

   1. Navigate to **Customer** > **Profiles** in Journey Optimizer.
   1. Search for and open the profile.
   1. Select the **Events** tab.
   1. Filter or search for events with `eventType = "message.feedback"`.
   1. Look for feedback events matching your Live Activity's `liveActivityID` and `event` type.
   1. Review the following key fields:

      | Field | Possible Values | What it means |
      |-|-|-|
      | `feedbackStatus` | `sent`, `error`, `denylist` | Delivery outcome from service provider |
      | `serviceProvider` | `apns/apnsSandbox` | Should be APNs for iOS Live Activities |
      | `errorCode` | Numeric code or `null` | APNs-specific error code if failed |
      | `errorMessage` | Error description or `null` | Human-readable error message |

   1. **If `feedbackStatus: "error"`:**
      * Check the `errorCode` and `errorMessage` for specific APNs errors
      * Common APNs errors include expired token, invalid certificate, wrong bundle ID

   1. **If no feedback event found:**
      * The push notification may not have been attempted
      * Check if profile was excluded in Campaign Reports as detailed in Step 1 above.

      +++

1. +++ Verify Live Activity delivery to APNs in Assurance

   1. Open your Assurance session, it must be active during the API call.
   1. Execute the API call (start, update, or end).
   1. In the **Event List**, look for Live Activity delivery events.
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
      | Token expired | InvalidToken error from APNs | Re-register Live Activity tokens |
      | Rate limiting | Too many requests | Reduce API call frequency |

      +++
  
1. +++ Proceed to additional diagnostic checks

   1. Check Live Activity Lifecycle metrics in Campaign Report.

      In the campaign report, review the **Live activity lifecycle** section:

      | Metric | What to check |
      |-|-|
      | Remote starts | Should show count of API-triggered starts |
      | Updates | Should show count of update events |
      | Ends | Should show count of end events |
      | Totals count | Overall Live Activity event volume |

      If these metrics are zero or do not match your API calls, there is a delivery issue between Adobe and APNs.

   1. If Adobe shows successful delivery but device does not show the Live Activity:

      * Check iOS device logs for Live Activity errors.
      * Verify app is in foreground or background (not terminated).
      * Confirm device has network connectivity.
      * Test on multiple devices to rule out device-specific issues.
      * Verify iOS version is 16.1 or later.

      +++

1. +++ Escalation to Adobe Support

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

## Unitary-specific scenarios

### Live Activity update token not synced{#token-not-synced}

The Live Activity starts successfully on the device, but subsequent `update` or `end` API calls (returning HTTP 200) fail to update or dismiss the Live Activity. This occurs when the **Live Activity update token** is not properly synced to Adobe's system.

**Understanding update tokens**

When a Live Activity starts on a device, iOS generates a unique update token for that specific Live Activity instance. This token is required for:

* Sending updates to the Live Activity
* Ending the Live Activity remotely

Each Live Activity instance has its own unique update token. Adobe needs this token to deliver update and end events.

**Expected behavior**

For update and end events to work, the following must occur:

1. Live Activity starts successfully on the device.
1. Device generates an update token for that Live Activity instance.
1. Mobile SDK captures and sends the update token to Adobe.
1. Update token is synced and stored in Adobe's system.
1. Subsequent API calls for update/end use this token for delivery.

**Pre-checks:**

* **User Permission**: The first time a Live Activity starts on a device, iOS displays a system prompt: "Allow [App Name] to provide Live Activity updates?" The user **must tap "Allow"** for update tokens to be generated and synced. If the user taps "Do not Allow", no update tokens are created and update/end requests will fail. This is a one-time permission per app.
* **Profile and Campaign Validation**: Complete [Scenario 1](#profile-issue) and [Scenario 2](#payload-issues) checks to ensure profile, tokens, and campaign configuration are correct.

#### Debugging steps

1. +++ Verify update token sync in Assurance

   1. Open your Assurance session.
   1. Ensure the session was active when the Live Activity started on the device.
   1. Filter or search for events with `eventType = "liveActivity.updateToken"`.
   1. Select the event and inspect the payload:
  
      * Verify the `token` field contains a valid update token string.
      * Check the `liveActivityID` matches your Live Activity instance.
      * Confirm the `activityType` matches your `attributes-type`.

   1. If event is not found:

      * The update token was not generated or captured by the SDK.
      * Check if user granted Live Activity permissions.
      * Verify the Live Activity actually started successfully on the device.
      * Confirm the mobile SDK is properly integrated to capture update tokens.

   1. If event is found, proceed to Step 2.

      +++

2. +++ Verify update token in profile events

   1. Navigate to **Customer** > **Profiles** in Journey Optimizer.
   1. Search for and open the profile.
   1. Select the **Events** tab.
   1. Look for `liveActivity.updateToken` events.
   1. Check the event details:

      * Verify the timestamp is recent (matches when Live Activity started).
      * Confirm the `token` and `liveActivityID` are present.
      * Ensure the `activityType` is correct.

   1. If event is not found in profile:

      * The update token event may not have been ingested to the profile yet.
      * Wait 5-10 minutes and re-check.
      * If still missing after 15 minutes, there may be an event ingestion issue.

   1. If event is found, the update token has been synced. You can proceed to Step 3.

      +++

3. +++ Check Live Activity delivery events in Assurance

   1. In your Assurance session, execute an update or end API call.
   1. In the **Event List**, look for Live Activity delivery events (APNs push events).
   1. Check for events indicating:
      * Push notification sent to APNs.
      * Response from APNs (success or error).
      * Delivery confirmation.
   1. If APNs delivery event is present: The push notification was sent. If the device still does not update, the issue may be on the device side (app not handling the push, network issues, etc.).
   1. If APNs delivery event is missing: The update token may not be properly stored or associated with the profile in Adobe's system.
   1. If error events are present: Inspect the error details for specific failure reasons (invalid token, APNs rejected, etc.).

      +++

## Broadcast-specific scenarios

### Broadcast campaign configuration and payload issues{#broadcast-config}

This section covers troubleshooting scenarios specific to broadcast Live Activities, which require different debugging approaches than unitary campaigns.

When profiles have valid tokens but the Live Activity does not appear, update, or behave as expected for audience members, the issue typically stems from one of the following:

* The campaign is not configured as API-triggered Marketing.
* The API payload uses an incorrect broadcast structure (missing `audience` or `input-push-channel`).
* The `content-state` and `attributes` fields do not match the iOS `ActivityAttributes` implementation.
* The `input-push-channel` was not created correctly on the Apple Developer Portal.

This troubleshooting scenario applies to all Live Activity events in broadcast campaigns: `start`, `update`, and `end`.

**Pre-checks:**

* **Campaign Type**: 
   * Verify that the campaign is created as API-triggered Marketing (required for broadcast/audience-based campaigns). 
   * Confirm that an audience is defined in the campaign configuration.
* **Profile and Token Validation**: Sample multiple profiles from the audience to verify they have valid `liveActivityPushNotificationDetails`. For detailed validation steps, follow [Scenario 1](#profile-issue).

#### Debugging steps

1. +++ Verify campaign audience configuration

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

1. +++ Validate broadcast API payload structure

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
     * Required for all broadcast Live Activities.
     * Serves as a unique identifier for this specific broadcast instance.
     * All profiles in the audience receive Live Activities linked to this channel.
     * Must match the `channelID` in `liveActivityData.channelID` (see Step 3).
     * Must be created for the `appID` on the Apple Developer Portal by the client.
     * Only channels created for the specific `appID` can be used for broadcasting Live Activity on that app.

   * **`audience.id`**:
     * Must reference a valid audience segment created in Adobe Experience Platform.
     * All profiles in this audience are targeted for the Live Activity.
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

1. +++ Align content-state, attributes, and input-push-channel with iOS implementation

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
   * This matching links the broadcast instance to the Live Activity data.
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
   | `input-push-channel` does not match `channelID` | Live Activity will not start | Ensure both values are identical |
   | Different `input-push-channel` for update/end | Update/end will not reach the Live Activities | Use same channel ID throughout lifecycle |
   | Missing `liveActivityData.channelID` | Live Activity will not link to broadcast | Include `channelID` in attributes for start event |
   | Missing required field in start event | Live Activity will not start | Add all fields from iOS struct |
   | Wrong field name (typo/case) | Field ignored or parsing error | Match iOS field names exactly |
   | Stale timestamp on update/end | Update/end ignored by devices | Always generate fresh timestamp |

      +++

1. +++ Test with Assurance

   Verify API execution and payload delivery using Assurance:

   1. Open your Assurance session on a test device that is part of the audience.
   1. Execute the broadcast API call.
   1. In the **Event List**, look for:
      * Campaign execution events.
      * Live Activity delivery events.
      * Error events indicating payload validation failures.
   1. Inspect event payloads to confirm:
      * The payload was processed correctly.
      * The `input-push-channel` is present.
      * No validation errors occurred.
      * Live Activities were sent to APNs for audience members.

      +++

### Profile not in audience or stale audience snapshot

In this scenario, the campaign and payload are correctly configured, but specific profiles are not receiving the Live Activity. This typically occurs when:

* The profile is not a member of the audience linked to the campaign.
* The audience is a batch audience and contains an outdated snapshot of profile data.
* The profile's Live Activity tokens were added recently but have not been reflected in the audience snapshot yet.

This troubleshooting scenario applies specifically to broadcast campaigns using audience-based targeting.

**Understanding audience evaluation**

Adobe Experience Platform uses different audience evaluation methods that determine when profile updates are reflected in the audience:

| Method | Evaluation Frequency | Data Freshness | Best For |
|-|-|-|--|
| Batch | Once daily (scheduled) | May be up to 24 hours stale | Large audiences, non-time-sensitive |
| Streaming | Real-time (on profile changes) | Near real-time for updated profiles | Time-sensitive, requires profile updates |

**Pre-checks:**

* **Campaign and Payload Validation**:
   * Complete the checks in [this scenario](#broadcast-config) to ensure the campaign and payload are correct. 
   * Verify that the `audience.id` in the API payload matches the campaign configuration.
* **Profile Exists**: Confirm that the profile exists in AEP with valid `liveActivityPushNotificationDetails`.

#### Debugging steps

1. +++ Verify profile is in audience

   First, confirm whether the profile that should receive the Live Activity is actually part of the audience.

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

2. +++ Check audience evaluation type and schedule

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
      * If a profile recently registered Live Activity tokens, those tokens may not be in the current snapshot.
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
