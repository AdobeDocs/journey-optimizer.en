---
title: Configure Inbox Support in Web SDK
description: Learn how to build a persistent message inbox in Adobe Journey Optimizer using Content Card and Inbox campaigns with the Adobe Experience Platform Web SDK.
feature: Content Cards
topic: Content Management
role: Developer
level: Experienced
---
# Configure Inbox support in Web SDK {#inbox-configuration-sdk}

>[!BEGINSHADEBOX]

**On this page:** Set up and run a sample that combines a Content Card campaign and an Inbox campaign with the Adobe Experience Platform Web SDK, so you can deliver a persistent notification inbox on your website.

>[!ENDSHADEBOX]

A message inbox is a persistent notification inbox driven by two Adobe Journey Optimizer campaigns that target the same surface:

* A **Content Card campaign**, which delivers individual notification items to the inbox.
* An **Inbox campaign**, which delivers configuration such as the title, empty-state copy, and layout.


## Configure Adobe Journey Optimizer {#ajo-setup}

Before you implement the Web SDK, set up the datastream, channels, and campaigns in Journey Optimizer that deliver content to the inbox.

1. Configure a **datastream** configured with **Adobe Experience Platform** as a service, with **Journey Optimizer** enabled and an **event dataset** selected.

1. Create two channel configurations that share the same surface: one **Content Cards** channel and one **Inbox** channel. [Learn how to configure a content card channel](../content-card/content-card-configuration.md) and [learn how to configure an Inbox channel](inbox-configuration.md).

    Set the **Page URL** and **Location on page** of both channels to the surface you defined in the prerequisites. This location must match the surface you query for in your Web SDK code.

1. [Create a Content Card campaign](../content-card/create-content-card.md) that uses the Content Cards channel for its content card configuration.

    For messages that should be delivered based on user actions on the web page, enable **Additional delivery rules** on the relevant action and set the event and value conditions that determine when the message appears. Repeat this for each type of notification the inbox should receive.

1. [Create an Inbox campaign](inbox-create.md) that uses the Inbox channel. This campaign delivers the metadata that configures the inbox shell itself.

    Match the audience and schedule settings of the Inbox campaign to the Content Card campaign so both are active for the same users at the same time.

1. Activate both campaigns.

## Implement the Web SDK {#web-sdk-implementation}

The inbox relies on two Web SDK commands:

* `subscribeRulesetItems` registers a callback that runs each time the propositions eligible for display change.

* `sendEvent` fetches those propositions. You can send additional events later to update which messages qualify for display.

1. Define the content card and inbox schemas, and the surface that matches your AJO channel configuration:

    ```javascript
    const CONTENT_CARD_SCHEMA = "https://ns.adobe.com/personalization/message/content-card";
    const INBOX_SCHEMA        = "https://ns.adobe.com/personalization/message/inbox";
    const SURFACE             = "web://your-site.example/#message-inbox";
    ```

1. Configure the Web SDK with your datastream:

    ```javascript
    alloy("configure", {
      datastreamId: "YOUR_DATASTREAM_ID",
      orgId: "YOUR_ORG_ID@AdobeOrg",
      defaultConsent: "in", // May not be usable in your implementation, but should be used for testing
      personalizationStorageEnabled: true,
    })
    ```

1. Subscribe to ruleset items for your surface and schemas, and provide a callback that handles content card propositions as they change:

    ```javascript
    alloy("subscribeRulesetItems", {
      surfaces: [SURFACE],
      schemas: [CONTENT_CARD_SCHEMA, INBOX_SCHEMA],
      callback: (result, collectEvent) => {
        const { propositions = [] } = result;
        const notifications = propositions
          .filter((p) => p.items?.[0]?.schema === CONTENT_CARD_SCHEMA)
          .map((proposition) => {
            const content = proposition.items[0]?.data?.content ?? {};
            return {
              id: proposition.scopeDetails.activity.id,
              title: content.title?.content ?? content.title ?? "",
              description: content.body?.content ?? content.body ?? "",
              proposition,
            };
          });
        renderNotifications(notifications, collectEvent);
      },
    });
    ```

1. As users interact with your application, send events to update which content card propositions should be displayed:

    ```javascript
    alloy("sendEvent", {
      renderDecisions: true,
      personalization: { surfaces: [SURFACE] },
    });
    ```

1. Use the `collectEvent` function provided by the `subscribeRulesetItems` callback to report interactions back to AJO. This keeps campaign reporting accurate:

    ```javascript
    // When a notification is displayed in the detail view:
    collectEvent("display", [notification.proposition]);

    // When a user clicks or interacts with a notification:
    collectEvent("interact", [notification.proposition]);

    // When a user dismisses a notification without reading it:
    collectEvent("dismiss", [notification.proposition]);

    // When a user deletes a notification:
    collectEvent("interact", [notification.proposition]);
    collectEvent("delete",   [notification.proposition]);
    ```

1. For cards with additional delivery rules, for example `action = deposit-funds`, call `evaluateRulesets` with the matching `decisionContext` to trigger them, since they don't appear on `sendEvent` alone:

    ```javascript
    alloy("evaluateRulesets", {
      renderDecisions: true,
      personalization: {
        decisionContext: { action: "deposit-funds" },
      },
    });
    ```

    The `subscribeRulesetItems` callback runs again with any newly qualified cards included alongside the existing ones.

1. Install dependencies and start the sample server:

    ```bash
    npm install
    npm start
    ```

1. Open `https://localhost` in your browser.

1. Update the `datastreamId`, `orgId`, and `SURFACE` constant in `src/app/page.js` to point at your AJO environment before testing.

{{$include /help/_includes/do-not-localize/inbox/ai-augmented-inbox-configuration-sdk.md}}
