---
solution: Journey Optimizer
product: journey optimizer
title: Configure the Live activities channel
description: Learn how to configure your Adobe Experience Platform Mobile SDK integration
feature: Channel Configuration
role: Admin
level: Intermediate
exl-id: 02ca7c8e-105a-4e77-9aad-2381904255d0
---
# Live activity integration with Adobe Experience Platform Mobile SDK {#mobile-live-config-sdk}


The Adobe Experience Platform Mobile SDK provides built-in support for Apple's Live activities. This allows your app to display real-time, dynamic updates directly on the Lock Screen and Dynamic Island without opening the app.

1. [Import required modules](#import)

    Import the following modules: **[!DNL AEPMessaging]**, **[!DNL AEPMessagingLiveActivity]**, **[!DNL ActivityKit]**.

1. [Define attributes](#attributes) 

    Conform to `LiveActivityAttributes`, include `LiveActivityData` and a `ContentState` attributes.

1. [Register Live activity](#register)

    Use `Messaging.registerLiveActivity()` after SDK initialization.

1. [Create widget configuration](#widget)

    Implement `ActivityConfiguration` for both Lock Screen and Dynamic Island interface.

1. [Start a Live activity locally (optional)](#local)

    Live activity can be initiated either remotely through Journey Optimizer or locally within the application code.

1. [Add debug support (optional)](#debug)
    
    Implement `LiveActivityAssuranceDebuggable` for Assurance.

Verify that the following minimum versions are installed to ensure correct configuration and compatibility.

>[!BEGINSHADEBOX]

**Prerequisites:**

* **iOS:** 
    * **iOS16.1 or later**: Basic Live activity functionality
    * **iOS 17.2+**: Push-to-start support
    * **iOS 18+**: Broadcast channel support
* **Xcode:** 14.0 or later
* **Swift:** 5.7 or later
* **Dependencies:** AEPCore, AEPMessaging, AEPMessagingLiveActivity, ActivityKit
* **AEP Mobile SDK version**: iOS Messaging 5.11.0 or later

>[!ENDSHADEBOX]

## Step 1: Import required modules {#import}

To get started, you first need to import the following modules: **[!DNL AEPMessaging]**, **[!DNL AEPMessagingLiveActivity]**, **[!DNL ActivityKit]**.

```swift
import AEPMessaging
import AEPMessagingLiveActivity
import ActivityKit
```

## Step 2: Define your Live activity Attributes {#attributes}

Create a struct that conforms to the `LiveActivityAttributes` protocol. This defines both the static data and dynamic content state for your Live activity.

The key components include:

* **`liveActivityData`** (required) which contains Adobe Experience Platform-specific data.
  * For individual users: Use `LiveActivityData(liveActivityID: "unique-id")`
  * For broadcast: Use `LiveActivityData(channelID: "channel-id")`
  
* Static Attributes, custom properties specific to your use case, e.g. `restaurantName`.

* **`ContentState`** which defines dynamic data that can be updated during the Live activity lifecycle. It must conform to `Codable` and `Hashable`.

* `LiveActivityOrigin` enumeration specifies whether an activity was initiated locally within the app or remotely via a push-to-start notification, supported in iOS 17.2 and later. This value allows the SDK to differentiate between locally initiated and remotely triggered Live activity during data collection.

**Examples**

```swift
@available(iOS 16.1, *)
struct FoodDeliveryLiveActivityAttributes: LiveActivityAttributes {
    // Mandatory: AEP Integration Data
    var liveActivityData: LiveActivityData
    
    // Static Attributes: Custom properties that do not change
    var restaurantName: String
    
    // Dynamic Content State: Data that can be updated
    struct ContentState: Codable, Hashable {
        var orderStatus: String
    }
}
```

```swift

@available(iOS 16.1, *)
public struct LiveActivityData: Codable {
    /// Unique identifier for broadcast Live activity channels
    public let channelID: String?
     
    /// Unique identifier for individual Live activity
    public let liveActivityID: String?
     
    /// Indicates local vs remote creation
    public let origin: LiveActivityOrigin?
     
    // Initializers
    public init(channelID: String)        // For broadcast Live activity
    public init(liveActivityID: String)   // For individual Live activity
}
```

You can also register multiple Live activity types for your app:

```swift
if #available(iOS 16.1, *) {
    Messaging.registerLiveActivity(AirplaneTrackingAttributes.self)
    Messaging.registerLiveActivity(FoodDeliveryLiveActivityAttributes.self)
    Messaging.registerLiveActivity(GameScoreLiveActivityAttributes.self)
}
```

## Step 3: Register Live activity {#register}

Register your Live activity types in your `AppDelegate` after SDK initialization, this allows you to:

* Enables automatic push-to-start token collection (iOS 17.2+)
* Automatically collects Live activity update tokens
* Enables lifecycle management and event tracking

**Example for a food delivery Live activity:**

```swift
if #available(iOS 16.1, *) {
    Messaging.registerLiveActivity(FoodDeliveryLiveActivityAttributes.self)
}
```

## Step 4: Create Live activity widgets {#widgets}

A Live activity is displayed through widgets. You need to create a widget bundle and configuration:

**Example for a food delivery Live activity:**

```swift
@main
struct FoodDeliveryWidgetBundle: WidgetBundle {
    var body: some Widget {
        FoodDeliveryLiveActivityWidget()
    }
}

@available(iOS 16.1, *)
struct FoodDeliveryLiveActivityWidget: Widget {
    var body: some WidgetConfiguration {
        ActivityConfiguration(for: FoodDeliveryLiveActivityAttributes.self) { context in
            // Lock Screen UI
            VStack {
                Text("Order from \(context.attributes.restaurantName)")
                Text("Status: \(context.state.orderStatus)") // possible status may include "Ordered", "Order accepted", "Preparing", "On the Way","Delivered"
            }
        } dynamicIsland: { context in
            // Dynamic Island UI
            DynamicIsland {
                // Expanded UI
            } compactLeading: {
                // Compact leading UI
            } compactTrailing: {
                // Compact trailing UI
            } minimal: {
                // Minimal UI
            }
        }
    }
}
```

## Step 5: Start a Live activity locally (optional) {#local}

While Journey Optimizer can remotely start Live activities, you can also start them locally:

**Example for a food delivery Live activity:**

```swift
let attributes = FoodDeliveryLiveActivityAttributes(
    liveActivityData: LiveActivityData(liveActivityID: "order123"),
    restaurantName: "Pizza Palace"
)

let contentState = FoodDeliveryLiveActivityAttributes.ContentState(
    orderStatus: "Ordered"
)

let activity = try Activity<FoodDeliveryLiveActivityAttributes>.request(
    attributes: attributes,
    contentState: contentState,
    pushType: .token
)
```

## Step 6: Add debug support (optional) {#debug}

If needed, you can debug Live activity schemas in Adobe Assurance:

**Example for a food delivery Live activity:**

```swift
@available(iOS 16.1, *)
extension FoodDeliveryLiveActivityAttributes: LiveActivityAssuranceDebuggable {
    static func getDebugInfo() -> (attributes: FoodDeliveryLiveActivityAttributes, state: ContentState) {
        return (
            FoodDeliveryLiveActivityAttributes(
                liveActivityData: LiveActivityData(liveActivityID: "debug-order-123"),
                restaurantName: "Debug Restaurant"
            ),
            ContentState(orderStatus: "Ordered")
        )
    }
}
```

## Additional resources

For comprehensive SDK documentation and implementation details:

* [Live activities Developer Guide](https://developer.adobe.com/client-sdks/edge/adobe-journey-optimizer/live-activities)
* [API Reference](https://developer.adobe.com/client-sdks/edge/adobe-journey-optimizer/live-activities/api-reference/)
* [Live activity Tutorial](https://developer.adobe.com/client-sdks/edge/adobe-journey-optimizer/live-activities/tutorial/)
* [Public Classes](https://developer.adobe.com/client-sdks/edge/adobe-journey-optimizer/live-activities/public-classes/live-activity-attributes/)

>[!TIP]
>
>If you are experiencing issues with token registration, payload alignment, or Live activity delivery, see [Troubleshoot Live activities](troubleshoot-mobile-live.md) for detailed debugging guidance.
