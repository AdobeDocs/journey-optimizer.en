---
solution: Journey Optimizer
product: journey optimizer
title: Experience events lookup in journeys
description: Learn how to use Experience Events lookup in journeys
exl-id: 35e2e347-0669-44a3-92ba-aee52e54c219
---
# Experience event lookup in journeys {#ee-journeys}

>[!CAUTION]
>
>Starting July 8 2025, in new customer organizations, creating expressions using experience events is no longer supported in the expression editor used in journey conditions. As a result, experience events in the [Experience Platform data source](../datasource/adobe-experience-platform-data-source.md) cannot be used for creating expressions. Alternative approaches and best practices for creating expressions/logic with experience events are referenced below.
>
>Need more details? [Read out the FAQ](#faq-ee).

This page outlines common patterns and scalable approaches to help you make the most of Experience Events in Adobe Journey Optimizer. These use cases are designed to help you solve frequent challenges such as managing opt-outs, controlling message frequency, personalizing content based on user behavior, and reacting to real-time signals.

By leveraging these strategies, you can turn behavioral data into meaningful actions—suppressing, qualifying, or excluding profiles based on the events they trigger or the attributes they carry. Whether you're building logic for purchase thresholds, abandonment triggers, or bounce handling, these examples offer practical guidance you can adapt to your needs.

As you evaluate which approach fits best, consider the latency requirements of your use case to ensure your journeys remain responsive and effective.

## Opt-out suppression 

To suppress profiles that have opted out of marketing communications, use built-in consent management. Opt-out preferences are automatically captured in the profile's consent fields; they can be referenced directly in journey conditions and are automatically enforced by Journey Optimizer during message delivery.

Learn more:

* [Manage consent](../privacy/opt-out.md)
* [Email opt-out management](../email/email-opt-out.md) 
* [Opt-out management for text messages](../sms/sms-opt-out.md)


## Bounce-based suppression

To exclude profiles that have experienced email bounces, leverage Adobe Journey Optimizer's automatic suppression list for bounced addresses. This built-in mechanism ensures that invalid or unreachable emails are excluded from future sends without requiring custom logic. 

Learn more:

* [Manage the suppression list](../configuration/manage-suppression-list.md)


## Generic suppression

To suppress profiles that have demonstrated certain behaviors, use batch audiences with event-based logic to capture profiles that meet the suppression criteria. Reference this audience in journey conditions.

Learn more:

* Adobe Experience Platform [Segment builder - Events](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/segment-builder#events){target="_blank"}

* Adobe Experience Platform [Segment builder – Time constraints](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/segment-builder#time-constraints){target="_blank"}

* [Using audiences in conditions](../building-journeys/condition-activity.md#using-audiences-in-conditions)

* [inAudience() function](../building-journeys/functions/functioninaudience.md)


## Communications-received exclusion 

To prevent sending messages to profiles who have received any communications within a recent time window:

* Use batch audiences with time-based criteria and reference them in journey conditions.
* Apply frequency capping business rules to enforce daily or weekly message limits.


Learn more using audiences:

* Adobe Experience Platform [Segment builder - Events](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/segment-builder#events){target="_blank"}

* Adobe Experience Platform [Segment builder – Time constraints](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/segment-builder#time-constraints){target="_blank"}

* [Using audiences in conditions](../building-journeys/condition-activity.md#using-audiences-in-conditions)

* [inAudience() function](../building-journeys/functions/functioninaudience.md)


See also:

* [Frequency capping by channel and communication type](../conflict-prioritization/channel-capping.md)



## Message-specific inclusion/exclusion

To include or exclude profiles based on whether they received a specific message, create batch audiences that encapsulate this logic and reference them in journey conditions.


Learn more:

* Adobe Experience Platform [Segment builder - Events](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/segment-builder#events){target="_blank"}

* Adobe Experience Platform [Segment builder – Time constraints](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/segment-builder#time-constraints){target="_blank"}

* [Using audiences in conditions](../building-journeys/condition-activity.md#using-audiences-in-conditions)

* [inAudience() function](../building-journeys/functions/functioninaudience.md)

## Cart or browse abandonment personalization 

To personalize communications based on the latest cart or browse events across multiple cart types or product views:

* If you have access to [Adobe Experience Platform Data Distiller](https://experienceleague.adobe.com/en/docs/experience-platform/query/data-distiller/overview){target="_blank"}, configure automated queries to extract the required data from the event, manipulate it to fit the use case, and write it back to a profile-enabled dataset for activation.
* If the abandonment data can be modeled on the profile with scalar attributes, consider using Computed attributes to capture the latest information and then reference these attributes in the journey to construct the communication. [Learn more in Adobe Experience Platform documentation](https://experienceleague.adobe.com/en/docs/experience-platform/profile/computed-attributes/overview){target="_blank"}


## Behavior-based journey exit 

To remove profiles from journey when they exhibit a particular behavior, utilize exit criteria to exit the profile from the journey when a particular event is received or the profile qualifies for a specific audience.

Learn more:

* [Set your journey properties - Exit criteria](journey-properties.md#exit-criteria)

## Purchase-based qualification with value thresholds

To trigger journeys based on purchases and suppress if value is above/below a threshold, define computed attributes to sum purchases over a specific time period. Create an audience that includes profiles whose spending amount meets certain criteria. 

Learn more:

* Adobe Experience Platform [Computed attributes overview](https://experienceleague.adobe.com/en/docs/experience-platform/profile/computed-attributes/overview){target="_blank"}



## Frequently Asked Questions {#faq-ee}

Using experience events in journey expressions/conditions is no longer supported. Impacts are listed in the FAQ below:

+++What specific capabilities are impacted? 

Only the lookup of experience events in the expression editor is impacted. The following capabilities are **not** impacted and remain the same: 

* Observing the experience events associated with a specific profile in the profile UI 

* Using experience events in computed attribute rules and accessing the computed attributes in a journey 

* Triggering a journey with a unitary or business event 

* Using journey context data from the events that trigger the journey in the expression and personalization editors 

* Listening to an event within a journey  

* Configuring events to trigger a journey 

* Detecting end user reaction events to marketing communications (e.g., email open) 

+++

+++Are my existing Adobe Organization impacted by this update? 

Your Adobe Organization are only affected if you were not already using experience event lookup. If you are already utilizing experience events in the [Experience Platform data source](../datasource/adobe-experience-platform-data-source.md), your Adobe Organization continues to have support for experience event lookup. 

+++

+++I have a new Adobe Organization. How can I solve my use case requiring experience event data? 

Alternative approaches and best practices involving experience events are available above to achieve desired use cases. 

+++

+++ What if alternative approaches do not work for my use case?

If your use case cannot be solved using one of the alternative approaches listed above, please reach out to your Adobe representative. 

+++
