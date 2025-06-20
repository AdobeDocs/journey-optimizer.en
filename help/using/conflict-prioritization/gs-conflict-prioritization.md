---
title: Conflict management & prioritization
description: Learn how to leverage Journey Optimizer conflict & prioritization tools.
role: User
level: Beginner
exl-id: 9dc0cd89-d29a-42d2-a73f-d95f9c39c86e
---
# Conflict management & prioritization {#conflict-prioritization}

## Conflict management & prioritizations tools {#tools}

In Journey Optimizer, managing the volume and timing of campaigns and journeys is essential to avoid overwhelming customers with too many interactions. Journey Optimizer offers several tools for conflict management and prioritization.

These tools are available for campaigns and unitary, Audience Qualification, and Read audience journeys.

By leveraging these tools, you can ensure smoother and more targeted marketing efforts, delivering the right message at the right time while avoiding conflicts and overload.

### Conflict detection tool

With the **conflict detection tool**, you can identify potential overlaps in journeys and campaigns. This is crucial as too many simultaneous communications can lead to customer fatigue. Journey Optimizer allows you to monitor elements such as timelines, audience overlap, and channel configurations. By identifying conflicts early, you can refine your campaigns to avoid bombarding customers with multiple messages at the same time.

➡️ [Learn how to detect potential conflics in journeys & campaigns](conflicts.md)

### Priority scores

**Priority scores** help you control which campaigns or journeys take precedence when a customer qualifies for multiple communications. This is especially useful for inbound channels such as web and mobile, where only one campaign can be shown at any given time. By assigning a priority score to each journey or campaign, you can ensure that the most important message is delivered first.

➡️ [Learn how to assign priority scores to journeys & campaigns](priority-scores.md)

### Rule sets

Rule sets allow you to **group together multiple rules into rule sets** and apply them to the journeys and campaigns of your choice. This provides improved granularity to limit how often and how many journeys a customer can enter within a certain time frame or control how often users will receive a message depending on the type of communication.

* **Journey capping & arbitration**

    Rule sets allow you to limit how often and how many journeys a customer can enter within a certain time frame. You can also set up rules to cap the number of journey entries for a profile or limit the number of journeys a customer can be enrolled in at the same time. 

    Additionally, you can use arbitration settings to decide which journey a customer should enter if they qualify for multiple journeys, using priority scores to determine the best fit.
    
    ➡️ [Learn how to work with journey capping & arbitration](journey-capping.md)

* **Frequency capping by channel and communication type**

    You can also use rule sets to set frequency capping by communication type (e.g., Sales, Promotional) to prevent overloading customers with similar messages. You can control frequency across multiple channels, automatically excluding over-solicited profiles to ensure a better customer experience.
    
    ➡️ [Learn how to set frequency capping by channel and communication type](../conflict-prioritization/channel-capping.md)

## Guardrails & limitations

* **Campaigns & priority scores** - In campaigns, priority score is available for the **web**, **in-app**, and **code-based** inbound channels only.

* **Profile counter update latency**
    
    It can take up to 10 minutes after a customer has entered a journey for the profile counter value to be updated.

    If a profile enters two journeys within a short window, the second journey may not correctly recognize that the frequency cap has already been reached, potentially allowing the profile to enter both journeys.

* **Namespace priority for journey entry capping**

    Entry capping is only supported if the namespace selected in the journey is the highest priority namespace defined in the sandbox. If namespace priority hasn't been explicitly configured, the default highest priority is email.

* **Simultaneous activations in audience qualification journeys**

    When multiple audience qualification journeys are activated by the same audience qualification event, then counts for entry capping will not be accurate. If counts are below the cap, journey will continue to arbitrate, but it will not be able to get the most up-to-date counts with simultaneous activations.  
