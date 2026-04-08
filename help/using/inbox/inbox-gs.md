---
title: Create an Inbox
description: Get started with Inbox in Adobe Journey Optimizer to deliver persistent, non-intrusive messages to your users.
feature: Content Cards
topic: Content Management
role: User
level: Beginner
exl-id: 60190d0b-d8e7-4a78-9924-d948f2769f6c
---
# Get started with Inbox {#inbox-gs}

Inbox delivers persistent, low-friction messages in one place inside your mobile app or website. In-app and push can disappear after a swipe or tap; Inbox keeps messages available so people can open, read, and act on them when it suits them.

Inbox builds on the Content Cards channel and adds:

* **Persistent messaging**: Content stays in the inbox until you remove it or it expires, so users can return to it after closing a notification or leaving the app.
* **Centralized location**: A single mailbox in your app or site for relevant marketing messages.
* **Flexible implementation**: Use the ready-made inbox container or tailor the experience in your own UI.
* **Read-Status**: Messages can be marked as read or unread on the device where they're opened.

## Quick start guide

Follow these steps to configure and use Inbox:

1. [Configure Adobe Journey Optimizer](inbox-configuration.md)

   Add an **Inbox** channel configuration under **Channel configurations** so Journey Optimizer knows where and how the inbox runs (web page or rule, or mobile app surface).

1. [Create your Inbox in Journey Optimizer](inbox-create.md)

   Create a campaign that uses the **Content card** action and choose **Inbox** as the delivery location—scheduled from the UI or triggered by API.

1. [Design your Inbox](inbox-design.md)

   Pick inbox templates and list or expanded layouts so messages match your brand and UX. 

1. [Create your Content card and link it to your Inbox](../content-card/create-content-card.md)

   Author the card content in the designer, finish Inbox-specific options, then activate your campaign so messages reach the inbox.

## Additional ressources

* [Fetch and Display Inbox](https://developer.adobe.com/client-sdks/edge/adobe-journey-optimizer/inbox-ui/Android/tutorial/displaying-inbox/): Load Journey Optimizer inbox messages and render the Inbox UI on Android (Adobe Developer documentation).
* [Customizing Inbox](https://developer.adobe.com/client-sdks/edge/adobe-journey-optimizer/inbox-ui/Android/tutorial/customizing-inbox/): Adjust inbox layout, styling, and interaction behavior for your Android app (Adobe Developer documentation).
* [Listening to Inbox Events](https://developer.adobe.com/client-sdks/edge/adobe-journey-optimizer/inbox-ui/Android/tutorial/listening-inbox-events/): Subscribe to inbox callbacks for user actions and lifecycle updates on Android (Adobe Developer documentation).
