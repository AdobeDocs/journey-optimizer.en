---
solution: Journey Optimizer
product: journey optimizer
title: Send Time Optimization for mobile messaging
description: Learn how to configure and use Send Time Optimization for mobile messaging in Adobe Journey Optimizer.
feature: SMS
topic: Send Time Optimization
role: User
level: Intermediate
exl-id: 56ff1000-7799-40ff-8f03-2f5868d05e7b
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: d0a62d3c-b79e-47e4-929e-40ef3cffa037
    internal-label: Communication channels
subfeature_v2:
  - id: f03a3a13-9e99-4c7c-a1ae-0f4d07ced35c
    internal-label: SMS / MMS
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
level_v2:
  - id: b6b77c26-2a48-4a62-9ceb-5ae67f4dfde5
    internal-label: Intermediate
topic_v2:
  - id: e0eb8757-182f-49f3-94a4-1587d16f5094
    internal-label: Personalization
---

# Send Time Optimization for mobile messaging {#sms-send-time-optimization}

>[!AVAILABILITY]
>
>Send Time Optimization for mobile messaging (SMS, RCS, and WhatsApp) is available starting H2 2026 and applies to both Journeys and Campaigns.

## Overview {#overview}

Send Time Optimization (STO) for mobile messaging empowers marketers to move beyond "batch and blast" scheduling by using AI-driven insights to determine the optimal delivery time for each individual profile. Rather than dispatching messages to your entire audience at once, Adobe Journey Optimizer analyzes each profile's historical engagement patterns and predicts when that individual is most likely to open, click, or respond to an SMS, RCS, or WhatsApp message.

By delivering messages at the moment of highest predicted engagement, STO helps increase open rates, click-through rates, and overall campaign ROI — without requiring manual audience segmentation by time zone or behavioral cohort. STO for mobile messaging is supported across SMS, RCS, and WhatsApp channels and is available in both Journey and Campaign execution contexts.

## Prerequisites {#prerequisites}

Before enabling Send Time Optimization for mobile messaging, verify the following:

- Your organization is provisioned for Adobe Journey Optimizer and for at least one of the SMS, RCS, or WhatsApp channels.
- A sufficient volume of historical mobile engagement data — including send events, opens, link clicks, and replies — exists for the target audience in Adobe Experience Platform (AEP). The AI model requires prior interaction history to generate reliable per-profile predictions.
- The relevant channel surface (SMS, RCS, or WhatsApp) is configured and active in your AJO instance. Refer to [Configure SMS channel surfaces](../sms/sms-configuration.md) for setup instructions.
- For Journey-based use cases, the Journey must be designed so that the message action node is not constrained by upstream wait or event nodes whose timeouts conflict with the STO delivery window.

>[!NOTE]
>
>Profiles with insufficient historical engagement data fall back to a default send time that you define during configuration. STO predictions are generated and scored at the individual profile level.

## How it works {#how-it-works}

STO for mobile messaging relies on a purpose-built AI model that processes each profile's historical engagement signals to forecast the optimal delivery window. The following steps describe the end-to-end flow.

### 1. Data ingestion and model training

The AI model continuously ingests mobile engagement events stored in Adobe Experience Platform, including message open timestamps, link click events, reply times, and historical delivery records. These signals form the training data used to learn behavioral patterns for each profile — such as preferred interaction hours, day-of-week tendencies, and responsiveness across time zones. The model is retrained on a rolling basis to remain sensitive to shifts in engagement behavior.

### 2. Per-profile prediction scoring

Once trained, the model scores each profile in the target audience and produces an optimal send-time window. This prediction is written back to the profile in AEP as a computed attribute, making it available to both Journeys and Campaigns at execution time without requiring additional API calls or real-time lookups during message dispatch.

### 3. Journey runtime scheduling

When a Journey containing an STO-enabled SMS, RCS, or WhatsApp action node is live, the Journey runtime reads each qualifying profile's predicted send-time attribute as the profile reaches the action node. The message is held within the configured optimization window and dispatched when the predicted optimal time arrives. If the predicted time has already passed or falls outside the window, the fallback behavior you configured is applied.

### 4. Campaign send distribution

For Campaigns, STO distributes the send across the audience based on per-profile predictions rather than issuing a single bulk dispatch. AJO staggers delivery across the campaign's configured send window, respecting each profile's predicted optimal time while staying within the window boundaries you define.

>[!NOTE]
>
>If a profile's predicted optimal time falls outside the configured send window, the message is sent at the nearest boundary — either the start or end of the window — whichever is closest to the prediction.

## Configure Send Time Optimization {#configure}

### Enable STO in a Campaign {#configure-campaign}

1. In Journey Optimizer, navigate to **Campaigns** and create a new campaign or open an existing draft.
2. Select **SMS**, **RCS**, or **WhatsApp** as the channel and complete the audience and message content steps.
3. In the **Scheduling** section, select **Send time optimization** instead of a fixed send date and time.
4. Use the **Send Time Optimization** toggle to enable the feature.
5. Configure the **Send window**: set the start and end time within which AJO is permitted to deliver messages. The window must span at least one hour and can extend up to 24 hours.
6. Define a **Fallback send time** for profiles that do not have sufficient engagement history to generate a prediction. You can choose to send immediately at window open or at a fixed time within the window.
7. Complete frequency capping, review, and activation steps, then activate the campaign.

### Enable STO in a Journey {#configure-journey}

1. Open or create a Journey in the Journey canvas.
2. Add or select an **SMS**, **RCS**, or **WhatsApp** action node.
3. In the action node configuration panel, expand the **Send time** settings.
4. Toggle **Send Time Optimization** to the enabled state.
5. Set the **Optimization window**: the maximum duration (in hours) the runtime may hold a message while waiting for the predicted optimal delivery time. The default window is six hours; the maximum is 24 hours.
6. Configure the **Fallback behavior** — either send immediately when a profile enters the node or wait until the next available predicted window — for profiles that have no prediction data.
7. Save the node configuration and publish the Journey.

>[!NOTE]
>
>When STO is active on a Journey action node, the effective delivery time for a profile may differ from the moment that profile enters the node by up to the full length of the configured optimization window. Account for this delay when designing upstream wait nodes and setting Journey-level timeouts to prevent premature journey exits.

## Guardrails and limitations {#guardrails}

- STO applies to outbound SMS, RCS, and WhatsApp messages only. Inbound reply flows and two-way messaging sessions are not subject to STO scheduling.
- Each Campaign or Journey action node supports one channel surface per STO-enabled message. Cross-channel STO coordination (for example, SMS and WhatsApp within a single node) is not supported.
- The AI model requires a minimum of 30 days of historical mobile engagement data per profile to produce a prediction. Profiles below this threshold use the configured fallback send time.
- STO interacts with frequency capping rules. If a capped profile's predicted delivery window conflicts with a capping limit, the message is suppressed per the capping rule and is not rescheduled to a later window.
- Consent flags, opt-out records, and global suppression lists are always enforced regardless of STO scheduling. A message held for optimized delivery is still subject to consent checks at the moment of dispatch.
- STO is not available for transactional messages where immediate delivery is required by business or regulatory requirements.

## Related topics {#related-topics}

- [Get started with SMS, RCS, and WhatsApp in Journey Optimizer](../sms/create-sms.md)
- [Configure SMS channel surfaces](../sms/sms-configuration.md)
- [Send Time Optimization for email and push notifications](../building-journeys/send-time-optimization.md)
- [AI-powered ranking in Journey Optimizer](../offers/offer-activities/ai-ranking.md)
- [Journey Optimizer release notes](../rn/release-notes.md)
