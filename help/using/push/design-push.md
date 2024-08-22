---
solution: Journey Optimizer
product: journey optimizer
title: Design a push notification
description: Learn how to design a push notification in Journey Optimizer
feature: Push
topic: Content Management
role: User
level: Beginner
exl-id: 6f6d693d-11f2-48b7-82a8-171829bf8045
---
# Design a push notification {#design-push-notification}

## Title and Body {#push-title-body}

>[!CONTEXTUALHELP]
>id="ajo-message-push-compose"
>title="Personalize your push notification."
>abstract="To compose your message, enter the content in the Title and Body fields. To include personalization tokens, open the personalization dialog."

To compose your message, click the **[!UICONTROL Title]** and **[!UICONTROL Body]** fields. Use the personalization editor to define content, personalize data and add dynamic content. Learn more about [personalization](../personalization/personalize.md) and [dynamic content](../personalization/get-started-dynamic-content.md) in the personalization editor.
    
Use the device preview section to visualize how the push notification displays on iOS and Android devices.

## On click behavior {#on-click-behavior}

>[!CONTEXTUALHELP]
>id="ajo-message-push-onclick"
>title="About on click behavior"
>abstract="Select the behavior when a recipient clicks on the body of the push notification."

You can select the behavior when a user clicks on the body of the push notification.

![](assets/title-body-push.png)

* To open the app, select the **[!UICONTROL Open app]** option. The app associated with the notification is defined in the [channel configuration](../configuration/channel-surfaces.md) (i.e. message preset).
* To redirect the user to a specific piece of content within an app, select the **[!UICONTROL Deeplink]** option.  The specific content can be a specific view, a particular section of a page, or a certain tab. Once the option is selected, enter the deeplink in the associated field.
* To redirect the user to an external URL, use the **[!UICONTROL Web URL]** option. Once the option is selected, enter the URL in the associated field.

## Add media {#add-media-push}

>[!CONTEXTUALHELP]
>id="ajo-message-push-media"
>title="Add media to your push notification"
>abstract="You can add an image, a video or a GIF that are displayed within your notification."

In the iOS version of your push notification, you can add an image, a video or a GIF that are displayed within your notification.

In the Android version, you can only add an image icon, and an image for expanded notifications. 

![](assets/push-config-add-media.png)

Two options are available. You can:

* Use the **[!UICONTROL Add media]** button to select an asset in **[!DNL Adobe Experience Manager Assets]**.

    Learn how to use **[!DNL Adobe Experience Manager Assets]** in [this page](../content-management/assets.md).
    
* Or enter the URL of the media in the **[!UICONTROL Add media]** field. In that case, you can add personalization to the URL.

Once added, the media displays on the right of the notification body.

## Add buttons {#add-buttons-push}

>[!CONTEXTUALHELP]
>id="ajo-message-push-buttons"
>title="Add buttons for users to interact with your push notification."
>abstract="This section will allow you to add call-to-action buttons to your message. For iOS, specify a notification category identifier. For Android, you can include custom text and targets for each button."

Create an actionable notification by adding buttons to your push content. 

If the device screen is locked, these buttons are not displayed: only the the **Title** and the **Message** of the notification are visible. If their device is unlocked, recipients will see the buttons.

In the Android version, you can add up to three buttons.

In the iOS version, a notification category identifier is specified. Notification categories need to be preconfigured in the iOS app which will define the buttons to be displayed and actions taken. See the [Apple documentation](https://developer.apple.com/documentation/usernotifications/declaring_your_actionable_notification_types) for more details.

1. Use the **[!UICONTROL Add button]** to define settings: the label and associated action. Possible actions are the same as for [on-click behavior](#on-click-behavior). 

1. Use the **[!UICONTROL Expand view]** icon under the central preview image to preview your personalized buttons.

    ![](assets/push_buttons.png)

## Send a silent notification {#silent-notification}

>[!CONTEXTUALHELP]
>id="ajo_message_push_silent_notification"
>title="About silent notification"
>abstract="Send notifications without disturbing the user, notifications are not shown in the notification center or notification bar."

A silent push notification (or background notification) is a hidden instruction that is delivered to the application. It is used for example to notify your application about the availability of new content or initiate a download in the background.

Select the **[!UICONTROL Silent Notification]** option to silently notify the application: in this case, the notification is transferred directly to the application. No alert is displayed on the device screen.

Use the **[!UICONTROL Custom data]** section to add key-value pairs.

## Custom data {#custom-data}

>[!CONTEXTUALHELP]
>id="ajo-message-push-custom"
>title="Configure custom data for your push notification."
>abstract="Add custom variables to the payload, depending on your mobile application configuration."

In the **[!UICONTROL Custom data]** section, you can add custom variables to the payload, depending on your mobile application configuration. For more on how to set up push notifications in Adobe Experience Platform and Adobe Launch, refer to [this section](push-gs.md)

## Advanced options {#advanced-options-push}

>[!CONTEXTUALHELP]
>id="ajo-message-push-advanced"
>title="Configure Advanced options for your push notification."
>abstract="This section empowers you to enhance the personalization of your push notification."

You can configure **[!UICONTROL Advanced options]** for your push notification. Available parameters are listed below:

|Parameter | Description |
|---------|---------|
|**[!UICONTROL Collapsible]** (iOS / Android) | A collapsible message is a message that may be replaced by a new message if it has become outdated. A common use cases of collapsible messages are messages used to tell a mobile app to sync data from the server. An example would be a sports app that updates users with the latest score. Only the most recent message is relevant. On the other hand, with non-collapsible message, very message is important to the client app and needs to be delivered. |
|**[!UICONTROL Custom sound]** (iOS / Android) | The sound to be played by the mobile terminal when the notification is received. The sound needs to be bundled in the app.|
|**[!UICONTROL Badges]** (iOS / Android) | A badge is used to display directly on the application icon the number of new unread information. <br/>The badge value will disappear as soon as the user opens or reads the new content from the application. When a notification is received on a device, it can refresh or add a badge value for the related app.<br/>For example, if you are storing the number of unread articles of your customers, you can leverage personalization to send the unique unread articles badge value for each customer. For more personalization, refer to [this section](../personalization/personalize.md).|
|**[!UICONTROL Notification group]**  (iOS only) | Associate a notification group to the push notification.<br/>Starting with iOS 12, notification groups allow you to consolidate message threads and notification topics into thread IDs. For example, a brand might send marketing notifications under one group ID, while keeping more operational type notifications under one or more different IDs.<br/>To illustrate this, you can have groupID: 123 "check out the new spring collection of sweaters" and groupID: 456 "your package was delivered" notification groups. In this example, all delivery notifications would be bundled under group ID: 456.|
|**[!UICONTROL Notification channel]** (Android only) | Associate a notification channel to the push notification.<br/>Starting in Android 8.0 (API level 26), all notifications must be assigned to a channel in order to display. For more on this, refer to the [Android developer documentation](https://developer.android.com/guide/topics/ui/notifiers/notifications#ManageChannels).|
|**[!UICONTROL Add content-availability flag]** (iOS only) | Sends the content available flag in the push payload to ensure that the app is woken up as soon as it receives the push notification, meaning that the app will be able to access the payload data.<br/> This works even if the app is running in the background and without needing any user interaction (e.g. tapping on Push notification). However, this does not apply if the app is not running. For more on this, refer to the [Apple developer documentation](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CreatingtheNotificationPayload.html). |
|**[!UICONTROL Add mutable-content flag]** (iOS only) | Sends the mutable-content flag in the push payload and will allow the push notification content to be modified by a notification service application extension provided in iOS SDK. For more on this, refer to [Apple developer documentation](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/ModifyingNotifications.html).<br/>You can then leverage your mobile app extensions to further modify the content or presentation of arriving push notifications sent from [!DNL Journey Optimizer]. For example, users can leverage this option to decrypt data, change the body or title text of a notification, add a thread identifier to a notification etc.|
|**[!UICONTROL Notification visibility]** (Android only) | Defines the push notification's visibility. <br/><b>Private</b> will show the notification on all lockscreens, but conceal sensitive or private information on secure lockscreens. <br/><b>Public</b> will show the notification in its entirety on all lockscreens. <br/><b>Secret</b> will not reveal any part of the notification on a secure lockscreen. <br/>For more on this, refer the [Android developer documentation](https://developer.android.com/reference/android/app/Notification).|
|**[!UICONTROL Notification priority]** (Android only) | Defines the push notification's importance from Low to Max. This determines how "intrusive" the push notification will be when it is delivered. For more on this, refer to the [Android developer documentation](https://developer.android.com/guide/topics/ui/notifiers/notifications#importance)|
|**[!UICONTROL Delivery priority]** (Android only) | Sets up a high or normal priority for your push notifications. For more information on message priority, refer to the [Google developer documentation](https://firebase.google.com/docs/cloud-messaging/concept-options#setting-the-priority-of-a-message).|
