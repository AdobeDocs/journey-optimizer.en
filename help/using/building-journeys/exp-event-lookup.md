---
solution: Journey Optimizer
product: journey optimizer
title: Experience Events lookup in journeys 
description: Learn how to use Experience Events lookup in journeys
---


# Experience Event Lookup in journeys  {#ee-journeys}

Below is a list of general patterns and recommendations focusing on common use cases and scalable approaches. When evaluating an approach, customers are encouraged to consider their use case's latency requirements.


## Opt-out suppression 

To suppress profiles that have opted out of marketing communications, use built-in consent management. Opt-out preferences are automatically captured in the profile's consent fields; they can be referenced directly in journey conditions and are automatically enforced by Journey Optimizer during message delivery.

Learn more:

* [Manage consent](../privacy/opt-out.md)
* [Email opt-out management](../email/email-opt-out.md) 
* [Opt-out management for text messages](../sms/sms-opt-out.md)


## Bounce-Based Suppression

To exclude profiles that have experienced email bounces, leverage Adobe Journey Optimizer's automatic suppression list for bounced addresses. This built-in mechanism ensures that invalid or unreachable emails are excluded from future sends without requiring custom logic. 

Learn more:

* [Manage the suppression list](../configuration/manage-suppression-list.md)


## Generic event-based suppression

To suppress profiles that have demonstrated certain behaviors, use batch audiences with event-based logic to capture profiles that meet the suppression criteria. Reference this audience in journey conditions.

Learn more:

* Adobe Experience Platform [Segment builder - Events](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/segment-builder#events){target="_blank"}

* Adobe Experience Platform [Segment builder – Time constraints](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/segment-builder#time-constraints){target="_blank"}

* [Using audiences in conditions](../building-journeys/condition-activity.md#using-audiences-in-conditions)

* [inAudience() function](../building-journeys/functions/functioninaudience.md)


## Communications-Received Exclusion 

To prevent sending messages to profiles that have received any communications within a recent time window:

* Use batch audiences with time-based criteria and reference them in journey conditions.
* Apply frequency capping business rules to enforce daily or weekly message limits.


Learn more using audiences:

* Adobe Experience Platform [Segment builder - Events](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/segment-builder#events){target="_blank"}

* Adobe Experience Platform [Segment builder – Time constraints](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/segment-builder#time-constraints){target="_blank"}

* [Using audiences in conditions](../building-journeys/condition-activity.md#using-audiences-in-conditions)

* [inAudience() function](../building-journeys/functions/functioninaudience.md)


See also:

* [Frequency capping by channel and communication type](../conflict-prioritization/channel-capping.md)



## Message-Specific Inclusion/Exclusion

To include or exclude profiles based on whether they received a specific message, create batch audiences that encapsulate this logic and reference them in journey conditions.


Learn more:

* Adobe Experience Platform [Segment builder - Events](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/segment-builder#events){target="_blank"}

* Adobe Experience Platform [Segment builder – Time constraints](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/segment-builder#time-constraints){target="_blank"}

* [Using audiences in conditions](../building-journeys/condition-activity.md#using-audiences-in-conditions)

* [inAudience() function](../building-journeys/functions/functioninaudience.md)

## Cart or Browse Abandonment Personalization 

To personalize communications based on the latest cart or browse events across multiple cart types or product views:

* If you have access to [Adobe Experience Platform Data Distiller](https://experienceleague.adobe.com/en/docs/experience-platform/query/data-distiller/overview){target="_blank"}, configure automated queries to extract the required data from the event, manipulate it to fit the use case, and write it back to a profile-enabled dataset for activation.
* If the abandonment data can be modeled on the profile with scalar attributes, consider using Computed attributes to capture the latest information and then reference these attributes in the journey to construct the communication. [Learn more in Adobe Experience Platform documentation](https://experienceleague.adobe.com/en/docs/experience-platform/profile/computed-attributes/overview){target="_blank"}


## Behavior-Based Journey Exit 

To remove profiles from journey when they exhibit a particular behavior, utilize exit criteria to exit the profile from the journey when a particular event is received or the profile qualifies for a specific audience.

Learn more:

* [Set your journey properties - Exit criteria](journey-properties.md#exit-criteria)

## Purchase-Based Qualification with Value Thresholds

To trigger journeys based on purchases and suppress if value is above/below a threshold, define computed attributes to sum purchases over a specific time period. Create an audience that includes profiles whose spending amount meets certain criteria. 

Learn more:

* Adobe Experience Platform [Computed attributes overview](https://experienceleague.adobe.com/en/docs/experience-platform/profile/computed-attributes/overview){target="_blank"}
