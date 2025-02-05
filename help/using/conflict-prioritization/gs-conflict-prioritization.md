---
title: Conflict management & prioritization
description: Learn how to leverage Journey Optimizer conflict & prioritization tools.
role: User
level: Beginner
badge: label="Limited Availability"
exl-id: 9dc0cd89-d29a-42d2-a73f-d95f9c39c86e
---
# Conflict management & prioritization {#conflict-prioritization}

>[!AVAILABILITY]
>
>Conflict & prioritization capabilities are currently available in Limited Availability to a select group of customers. Please note that these features will be gradually rolled out to more users in the future. Reach out to your account team if interested in being added to the waitlist for these features.

In Journey Optimizer, managing the volume and timing of campaigns and journeys is essential to avoid overwhelming customers with too many interactions. Journey Optimizer offers several tools for conflict management and prioritization.

## Conflict management & prioritizations tools {#tools}

With the **conflict detection tool**, you can identify potential overlaps in journeys and campaigns. This is crucial as too many simultaneous communications can lead to customer fatigue. Journey Optimizer allows you to monitor elements such as timelines, audience overlap, and channel configurations. By identifying conflicts early, you can refine your campaigns to avoid bombarding customers with multiple messages at the same time. [Learn how to detect potential conflics in journeys & campaigns](conflicts.md)

Additionally, **priority scores** help you control which campaigns or journeys take precedence when a customer qualifies for multiple communications. This is especially useful for inbound channels such as web and mobile, where only one campaign can be shown at any given time. By assigning a priority score to each journey or campaign, you can ensure that the most important message is delivered first. [Learn how to assign priority scores to journeys & campaigns](priority-scores.md)

**Journey capping & arbitration** allows you to limit how often and how many journeys a customer can enter within a certain time frame. You can set up rules to cap the number of journey entries for a profile or limit the number of journeys a customer can be enrolled in at the same time. Additionally, you can use arbitration settings to decide which journey a customer should enter if they qualify for multiple journeys, using priority scores to determine the best fit. [Learn how to work with journey capping & arbitration](journey-capping.md)

Finally, you can also use rule sets to set **frequency capping by communication type** (e.g., Sales, Promotional) to prevent overloading customers with similar messages. You can control frequency across multiple channels, automatically excluding over-solicited profiles to ensure a better customer experience. [Learn how to work with rule sets](../configuration/rule-sets.md)</li></ul>

By leveraging these features, you can ensure smoother and more targeted marketing efforts, delivering the right message at the right time while avoiding conflicts and overload.

## Guardrails & limitations

**Frequency capping & batch audiences**

For frequency capping, both channel or journey, if the audience used is a batch audience, then the profile counter value referenced at the time of entry into the journey, or the message runtime for a channel communication is going to be from the daily snapshot that is taken.

This can be problematic as customers can exceed the frequency capping limit if they had entered into another journey or received another communication between the time of the daily snapshot and the time of the journey being entered (or message being delivered). 

**Frequency capping & streaming audiences**

For streaming audiences, it can take up to 2 hours for the system to recognize an updated counter value and as such we would recommend spacing communications and journeys at least two hours apart if possible to mitigate this risk.

**Journeys start time**

To ensure conflict management and prioritization features operate correctly, we recommend setting your journey's start time at least 10 minutes into the future, to allow the system to update the counter accordingly.

If customers have already reached their cap when entering a journey, they will still not be allowed entry, but if they haven't reached their cap, the entry counter will not get incremented.

**Journey arbitration**

For now, only read-audience journeys are supported for journey arbitration. Arbitration settings cannot be leveraged for unitary or audience qualification journeys.
