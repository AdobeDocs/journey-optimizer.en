---
solution: Journey Optimizer
product: journey optimizer
title: Channel optimization
description: Learn how to use channel optimization to automatically select the best outbound channel for each customer based on their preferences or AI-predicted propensity scores.
feature: Journeys, Activities, Channels Activity
topic: Content Management, Artificial Intelligence
role: User
level: Intermediate
keywords: channel, optimization, preference, propensity, AI, outbound, email, push, SMS
badge: label="Limited Availability" type="Informative"
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: b3538224-471e-4c63-a444-9b19d89ae29c
    internal-label: Activities
  - id: d998adac-2f81-400b-a669-d07bb196e4eb
    internal-label: Journeys
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
level_v2:
  - id: b5a62a22-46f7-4f0d-b151-3fc640bef588
    internal-label: Intermediate
topic_v2:
  - id: bbbea26f-9621-49eb-9ab8-e06fb3bbce8c
    internal-label: Artificial intelligence
  - id: cdd65e7e-8839-44a2-bc21-0e03623b5dd1
    internal-label: Optimization
  - id: fd2e3797-f2ea-4b36-a9af-52acf5e90513
    internal-label: Customer profiles
---

# Channel optimization {#channel-optimization}

>[!AVAILABILITY]
>
>Channel optimization is currently available to a limited set of organizations (Limited Availability). To gain access, contact your Adobe representative.

>[!BEGINSHADEBOX]

**On this page:** Learn how to configure a journey action to deliver messages through the best outbound channel for each customer, using manual ranking, profile preferences, or AI-powered propensity scores.

>[!ENDSHADEBOX]

Channel optimization lets you add multiple outbound channels (Email, Push, SMS) to a single journey action and have Journey Optimizer automatically select the best one for each customer at send time. Instead of choosing one channel upfront or messaging customers across all channels at once, the system picks the highest-ranked channel each customer is opted into and falls back gracefully when that channel is unavailable.

➡️ [Learn more about channel optimization in this video](#video)

## Guardrails and limitations {#limitations}

* **Supported channels**: Only native Email, Push, and SMS (mobile messaging) channels are supported. Other outbound channels such as WhatsApp are not supported. Channel optimization requires the use of AJO's native email, push, and mobile messaging capabilities; execution through custom actions is not supported.

* **AI optimization metric**: The AI model optimizes for engagement (clicks) only. It does not optimize for orders, revenue, or other business metrics. If optimization for orders or revenue is required, a custom model can be trained offline by your data science team and applied via the customer profile attribute feature.

* **Click tracking required for AI ranking**: When using AI model-based ranking, click tracking must be enabled for all configured channels. The model relies on click data to compute propensity scores; if tracking is disabled, the AI ranking mode cannot function correctly. [Learn how to enable click tracking in email](../email/message-tracking.md)

* **Quiet hours**: All channels within a single channel optimization action must share the same quiet hours rule. If different quiet hours settings are required per channel, create separate journey actions instead of combining channels into a single action. In campaigns, the form validates that the same quiet hours rule is applied to all actions.

* **Send-Time Optimization incompatibility**: Currently [Send-Time Optimization](send-time-optimization.md) and channel optimization cannot be used together — choose one or the other. The UI prevents enabling both features simultaneously on the same action.

* **Reaction events**: Reaction events on the journey canvas currently reference only the first channel in a multi-channel action. Support for selecting any valid reaction event when multiple channels are present is planned for GA.

## Use channel optimization in a journey or a campaign {#configure}

To add multiple outbound channels with channel optimization, follow the steps below.

>[!BEGINTABS]

>[!TAB In a journey]

1. Start your journey with an [Event](general-events.md) or a [Read Audience](read-audience.md) activity.

1. From the **[!UICONTROL Actions]** section of the palette, drag and drop an **[!UICONTROL Action]** activity into the canvas.

1. Select an outbound channel (Email, Push, or SMS) and click **[!UICONTROL Add]**.

    ![Add an outbound channel to a journey action](assets/journey-channel-optimization-add-outbound.png){width="60%"}

1. Enter a label for your action and click **[!UICONTROL Configure action]**.

>[!TAB In a campaign]

1. [Create an Action campaign](../campaigns/create-campaign.md) and navigate to the **[!UICONTROL Actions]** tab.

1. Click the **[!UICONTROL Add action]** button and select an outbound channel (Email, Push, or SMS).

>[!ENDTABS]

Once an outbound action is selected in the **[!UICONTROL Actions]** tab, continue with the following steps:

1. Select a channel configuration and click **[!UICONTROL Add action]** to select another outbound channel.

    ![Add another outbound channel to a journey action](assets/journey-channel-optimization-add-outbound-action.png){width="1000%"}

    >[!NOTE]
    >
    >Only one action per channel type is supported in a single multi-channel action. For example, you cannot add two separate Email actions with different configurations.

    You can add up to three outbound channels (**[!UICONTROL Email]**, **[!UICONTROL Push]**, **[!UICONTROL SMS]**) to a single action.

1. In the **[!UICONTROL Channel optimization]** section, set the method to determine how the system selects the best channel for each customer. [Learn more](#optimization-modes)

    ![Select a channel optimization mode](assets/journey-channel-optimization-modes.png){width="100%"}

1. Set your fallback channel order (for manual ranking and customer preference modes). [Learn more](#fallback)

1. Save and publish your journey, or review and activate your campaign.

## Set the channel optimization method {#optimization-modes}

>[!CONTEXTUALHELP]
>id="ajo_channel_optimization_method"
>title="Define how channel selection works"
>abstract="The customer's first available channel, based on the selected prioritization method, is used for this action. Availability is determined by the customer's subscription preferences and marketing consent rules for the selected channel configurations, as well as any business rules — such as frequency capping — configured for the campaign or journey."

Channel optimization supports three modes, each using a different method to select the best channel for each customer at send time.

### Manual ranking {#manual-ranking}

You define the preferred channel order directly in the journey action. Journey Optimizer delivers through the first channel in your list that the customer is opted into and is not frequency-capped, then falls back to the next channel if needed.

![Manual ranking channel optimization](assets/journey-channel-optimization-manual.png){width="90%"}

Use this mode when you have a clear, consistent channel preference and do not need per-profile personalization.

### Customer preference {#customer-preference}

Journey Optimizer reads the customer's declared preferred channel from their profile, using the `preferred` attribute in the [Consents and Preferences XDM field group](https://experienceleague.adobe.com/en/docs/experience-platform/xdm/field-groups/profile/consents). Supported values are `email`, `push`, and `sms`.

![Customer preference channel optimization](assets/journey-channel-optimization-profile.png){width="90%"}

If the preferred channel is unavailable (not configured, not opted-in, or frequency-capped), Journey Optimizer falls back to the next channel in your configured fallback list.

Use this mode when customers have explicitly stated their preferred communication channel.

### AI model-based ranking {#ai-ranking}

Journey Optimizer uses a machine learning model that computes a per-channel propensity score for each customer based on their historical engagement (opens, clicks). Scores are stored in the customer's profile and the channel with the highest predicted propensity is selected at send time.

![AI model-based ranking channel optimization](assets/journey-channel-optimization-ai.png){width="90%"}

When a customer has insufficient engagement history, the system falls back to a randomly available channel.

Use this mode to let AI infer the most effective channel for each customer without any manual configuration.

## Fallback behavior {#fallback}

Regardless of the optimization mode, Journey Optimizer falls back to the next available channel when the top-ranked channel cannot be used. A channel is considered unavailable when any of the following conditions apply:

* The customer is not opted into the channel.
* The channel is not configured in the journey action.
* The channel has reached its frequency cap.
* The customer's profile preference or AI model score for that channel is not populated.

Under **manual ranking** and **customer preference** modes, fallback follows the marketer's configured channel priority list. Under **AI model-based ranking**, fallback selects a random available channel.

## How-to video {#video}

Learn how Adobe Journey Optimizer's channel optimization feature helps you reach customers on the most effective channel using manual priority, profile attributes, or Adobe's AI model.

>[!VIDEO](https://video.tv.adobe.com/v/3492132?quality=12)

<!--
**Related topics**

* [Use the Action activity](journey-action.md)
* [Send-Time optimization](send-time-optimization.md)
* [Content optimization](../content-management/gs-message-optimization.md)
-->
