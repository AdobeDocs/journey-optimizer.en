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
exl-id: a3f2b8c1-9d4e-4f7a-b6e5-2c1d8a0f3e9b
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

## Optimization modes {#optimization-modes}

Three modes are available to determine which channel to use for each customer.

### Manual ranking {#manual-ranking}

You define the preferred channel order directly in the journey action. Journey Optimizer delivers through the first channel in your list that the customer is opted into and under frequency cap.

Use this mode when you have a clear, consistent channel preference and do not need per-profile personalization.

### Customer preference {#customer-preference}

Journey Optimizer reads the customer's declared preferred channel from their profile, using the `preferred` attribute in the [Consents and Preferences XDM field group](https://experienceleague.adobe.com/en/docs/experience-platform/xdm/field-groups/profile/consents). Supported values are `email`, `push`, and `sms`.

If the preferred channel is unavailable (not configured, not opted-in, or frequency-capped), Journey Optimizer falls back to the next channel in your configured fallback list.

Use this mode when customers have explicitly stated their preferred communication channel.

### AI model-based ranking {#ai-ranking}

Journey Optimizer uses a machine learning model that computes a per-channel propensity score for each customer based on their historical engagement (opens, clicks). Scores are stored in the customer's profile and the channel with the highest predicted propensity is selected at send time.

When a customer has insufficient engagement history, the system falls back to a randomly available channel.

Use this mode to let AI infer the most effective channel for each customer without any manual configuration.

## Fallback behavior {#fallback}

Regardless of the optimization mode, Journey Optimizer falls back to the next available channel when the top-ranked channel cannot be used. A channel is considered unavailable when any of the following conditions apply:

* The customer is not opted into the channel.
* The channel is not configured in the journey action.
* The channel has reached its frequency cap.
* The customer's profile preference or AI model score for that channel is not populated.

Under **manual ranking** and **customer preference** modes, fallback follows the marketer's configured channel priority list. Under **AI model-based ranking**, fallback selects a random available channel.

## Configure channel optimization in a journey {#configure}

To add multiple outbound channels with channel optimization to a journey action:

1. Open your journey and drag an **[!UICONTROL Action]** activity onto the canvas.

1. In the configuration panel, expand the **[!UICONTROL Channel optimization]** section and select the optimization mode.

1. Add the outbound channels (Email, Push, SMS) you want to include and configure the content for each.

1. Set your fallback channel order (for manual ranking and customer preference modes).

1. Save and publish your journey.

>[!NOTE]
>
>Only one action per channel type is supported in a single multi-channel action. For example, you cannot add two separate Email actions with different configurations.

**Related topics**

* [Use the Action activity](journey-action.md)
* [Send-Time optimization](send-time-optimization.md)
* [Content optimization](../content-management/gs-message-optimization.md)
