---
title: Create custom channel experiences
description: Learn how to use a custom channel in a journey or a campaign in Adobe Journey Optimizer.
feature: Channel Configuration
topic: Content Management
role: User
level: Experienced
badge: label="Limited Availability" type="Informative"
---

# Create custom channel experiences {#create-custom-channel}

>[!BEGINSHADEBOX]

**On this page:** Learn how to add a custom channel to a journey or a campaign in Adobe Journey Optimizer, and author personalized message payloads using the expression editor.

>[!ENDSHADEBOX]

>[!AVAILABILITY]
>
>This capability is available in Limited Availability. Contact your Adobe representative to gain access.

In [!DNL Journey Optimizer], you can deliver messages using custom channels in campaigns and journeys. Follow the steps below to set up your custom channel experience.

>[!NOTE]
>
>Before creating a custom channel experience, ensure that a custom channel has been configured by your administrator. [Learn more](configure-custom-channel.md)

## Add a custom action through a journey or a campaign {#create-custom-channel-experience}

>[!CONTEXTUALHELP]
>id="ajo_journey_action_custom_channel"
>title="Custom channel action"
>abstract="A custom channel action delivers a message to profiles when they reach this step of the journey. The label identifies the activity in the journey canvas, and the action references a custom channel configuration that defines the endpoint, payload, and credentials used to deliver the message. The **Optimization** section can include content experiments or targeting rules, and the **Timeout or error** section can define an alternative path if the action fails."
>additional-url="https://experienceleague.adobe.com/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/journey-action#add-action" text="Get started with custom channels"



>[!BEGINTABS]

>[!TAB Add a custom channel to a journey]

Custom channels appear in the **[!UICONTROL Actions]** section of the journey canvas palette, listed by their display name and custom icon as defined in the Channel Builder.

To add a custom channel action to a journey:

1. [Create a journey](../building-journeys/journey-gs.md).

1. Start your journey with an [Event](../building-journeys/general-events.md) or a [Read Audience](../building-journeys/read-audience.md) activity.

1. Drag and drop an **[!UICONTROL Action]** activity from the **[!UICONTROL Actions]** section of the palette. Learn more about the [Action activity](../building-journeys/journey-action.md).

1. In the **[!UICONTROL Action]** drop-down, select the custom channel you want to use. Custom channels are listed by the name and icon assigned in the Channel Builder.

    ![Custom channel action selection in journey canvas](assets/custom_channel_journey_action.png){width="80%"}

1. Add a label to your action, click **[!DNL Configure action]** in the right panel, and select the **[!UICONTROL Channel configuration]** to use. [Learn how to create a custom channel configuration](custom-channel-configuration.md#create-channel-config)

1. In the **[!UICONTROL Message]** section, click **[!UICONTROL Edit content]** to open the payload editor and author your message. [Learn how to author content](#author-content)

1. Complete your journey flow by adding additional steps as needed, then publish the journey. [Learn more](../building-journeys/journey-gs.md)

>[!TAB Create a custom channel campaign]

To use a custom channel in a campaign:

1. [Create a campaign](../campaigns/create-campaign.md).

1. Select the campaign type:

   * **[!UICONTROL Scheduled - Marketing]** – Executed immediately or on a specified date. Designed for marketing messages, configured from the UI.
   * **[!UICONTROL API-triggered - Marketing/Transactional]** – Executed via an API call. Designed for event-triggered messaging (for example, order confirmations or password resets). [Learn more](../campaigns/api-triggered-campaigns.md)

1. Complete the campaign setup: campaign properties, [audience](../audience/about-audiences.md), and [schedule](../campaigns/create-campaign.md#schedule).

1. In the **[!UICONTROL Actions]** section, select the custom channel from the channel selector. All the custom channels configured on your sandbox appear alongside native channels.

    ![Campaign custom action selection](assets/custom_channel_campaign_action.png){width="80%"}

1. Select or create the **[!UICONTROL Channel configuration]** to use. [Learn how to create a channel configuration](custom-channel-configuration.md#create-channel-config)

    ![Custom channel configuration selection](assets/custom_channel_campaign_action_config.png){width="80%"}

1. Optionally, enable **[!UICONTROL Action tracking]** to automatically track links included in your message payload (requires a subdomain configured for custom channels). [Learn how to delegate a subdomain for custom channels](custom-channel-subdomains.md#subdomain-delegation)

1. In the **[!UICONTROL Optimization]** section, you can:

    * **[!UICONTROL Create targeting rules]** to send different messages to different segments of your audience. [Learn more](../campaigns/create-campaign.md#targeting)
    * Click **[!UICONTROL Create experiment]** to run A/B tests on your custom channel messages. [Learn more](../campaigns/create-campaign.md#content-experiment)

1. Click **[!UICONTROL Edit content]** to open the payload editor and author your message. [Learn how to author content](#author-content)

1. Review and activate the campaign. [Learn more](../campaigns/create-campaign.md)

<!--
>[!TAB Add a custom channel to an orchestrated campaign]

Custom channels appear in the channel selection list in the orchestrated Campaigns canvas, below the native channels, with their custom icon and display name.

To add a custom channel in an orchestrated campaign:

1. Open or create an orchestrated campaign.

1. In the canvas, add a channel action node and select your custom channel from the list.

1. Select the **[!UICONTROL Channel configuration]** to use. Ensure the configuration includes the **[!UICONTROL Execution details]** section required for orchestrated campaigns.

1. Click **[!UICONTROL Edit content]** to open the payload editor and author your message. [Learn how to author content](#author-content)
-->

>[!ENDTABS]

## Author your custom channel content {#author-content}

The content editor reflects the payload structure you defined when configuring the custom channel. Click **[!UICONTROL Edit code]** to open the payload editor and enter your message content.

![Custom channel payload editor](assets/custom_channel_payload_editor.png){width="80%"}

The fields you can author and personalize are displayed. You can leverage the [!DNL Journey Optimizer] personalization editor with all its personalization and authoring capabilities. [Learn more](../personalization/personalization-build-expressions.md)

>[!NOTE]
>
>Only JSON payloads are supported. If your custom channel payload is not JSON, you can use a JSON wrapper to encapsulate your content. For example, if your payload is XML, you can wrap it in a JSON object like this:
>
>```json
>{
>  "payload": "<xml>...</xml>"
>}
>```

### Personalize the payload {#personalize}

[!DNL Journey Optimizer]'s full personalization capabilities are available in the payload editor:

* **Profile attributes** – Inject any XDM profile attribute, such as `{{profile.person.name.firstName}}` or a custom identity like a messaging platform user ID stored in a custom namespace.
* **Contextual attributes** – Use journey event attributes or campaign contextual data resolved at send time.
* **Helper functions** – Format values using built-in string, date, or arithmetic functions. [Learn more](../personalization/functions/helpers.md)
* **Expression fragments** – Reuse shared personalization logic across multiple channels and campaigns. [Learn more](../content-management/customizable-fragments.md)

>[!CAUTION]
>
>Currently there is no validation of the payload at authoring time. You can use the **[!UICONTROL Simulate content]** feature to validate that your payload is well-formed JSON and that all personalization expressions resolve correctly for your test profiles. [Learn more](test-custom-channel.md#simulate-content)

The following examples show JSON payloads with profile personalization:

```json
{
  "message": {
    "template": "Limited offer just for you, {{profile.person.name.firstName}}!",
    "header": "You have a FREE drink when you buy a King menu!"
  },
  "campaign_ref": {
    "id": "2grjya",
    "type": "loyalty",
    "url": "/companies/wNmRsLbu/campaigns/wallet/2grjya"
  }
}
```

```json
{
  "messaging_product": "mess",
  "recipient_type": "individual",
  "to": "{{profile.mobilePhone.number}}",
  "zipCode": 4001,
  "type": "image",
  "image": {
    "id": "1479537139650973",
    "caption": "The best succulent ever?"
  }
}
```

### Track links in the payload {#track-links}

To include a tracked link in your custom channel payload—so that clicks are automatically tracked and visible in the channel's reporting dashboards—wrap the URL using the following handlebar syntax:

```
{{url trackedUrl='' originalUrl='https://example.com/' type='TRACKED'}}
```

* `originalUrl` – The destination URL you want to redirect the recipient to.
* `trackedUrl` – Leave this empty; [!DNL Journey Optimizer] automatically populates it with the tracking-enabled redirect URL at send time.
* `type` – Must be set to `TRACKED`.

>[!NOTE]
>
>Link tracking requires a subdomain configured for custom channels. [Learn how to delegate a subdomain for custom channels](custom-channel-subdomains.md#subdomain-delegation)

**Example – tracked link in a payload:**

```json
{
  "receiver": "{{profile.mobilePhone.number}}",
  "min_api_version": 1,
  "sender": {
    "name": "Luma Rewards",
    "avatar": "https://avatar.example.com"
  },
  "tracking_data": "{{profile.person.name.firstName}}",
  "type": "text",
  "text": "Hello {{profile.person.name.firstName}}! Discover our new collection: {{url trackedUrl='' originalUrl='https://luma.com/collection' type='TRACKED'}}"
}
```

<!--
### Strict JSON mode {#strict-json}

The editor supports a **[!UICONTROL Strict JSON]** toggle:

* **Strict JSON: Off (default)** – The editor accepts any payload content, including personalization helpers and functions that may temporarily produce non-JSON syntax. A warning is displayed at the **Review to Activate** step if the payload is not well-formed JSON, prompting you to simulate and proof before publishing.
* **Strict JSON: On** – The editor validates that the payload is well-formed JSON as you type. At the **Review to Activate** step, [!DNL Journey Optimizer] validates the payload against the channel schema and flags missing required fields or type mismatches as errors that must be resolved before activation.
-->

## Activate your custom channel experience {#activate}

>[!IMPORTANT]
>
>Preview and test your custom channel payload before activating. [Learn how](test-custom-channel.md#preview-test)
>
>If your campaign or journey is subject to an approval policy, you must request approval before activation. [Learn more](../test-approve/gs-approval.md)

* **From a journey** – Click **[!UICONTROL Publish]** in the top-right area. The journey goes live and starts calling your external endpoint for qualifying profiles. Learn more about [publishing journeys](../building-journeys/journey-gs.md#publish-journey).
* **From a campaign** – Click **[!UICONTROL Review to activate]**, review your settings, then click **[!UICONTROL Activate]**. The campaign takes the **[!UICONTROL Live]** status (or **[!UICONTROL Scheduled]** if a future start date was defined). Learn more about [activating campaigns](../campaigns/create-campaign.md#review-activate).
