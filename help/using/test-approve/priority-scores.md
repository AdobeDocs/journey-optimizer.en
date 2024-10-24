---
title: Assign priority scores to journeys & campaigns
description: Learn how to assign priority scores to journeys & campaigns.
role: User
level: Beginner
badge: label="Limited Availability"
hide: yes
hidefromtoc: yes
---

# Assign priority scores to journeys & campaigns {#priority}

>[!BEGINSHADEBOX]

What you'll find in this documentation guide:

* [Get started with conflict management & prioritization](gs-conflict-prioritization.md)
* [Detect potential conflicts in journeys & campaigns](conflicts.md)
* **[Assign priority scores to journeys & campaigns](priority-scores.md)**
* [Journey capping & arbitration](journey-capping.md)

>[!ENDSHADEBOX]

>[!AVAILABILITY]
>
>Conflict management & prioritization tools are currently available as a Limited Availability to selected users only.

Journey Optimizer allows you to assign a priority score to a journey or campaign. Priority is essential to prioritize a journey, campaign, or action when there is an imposed constraint (such as a frequency cap). In situations where a customer qualifies for many journeys, campaigns, or communications and you want to be selective as to which they should enter and receive, you should utilize this field.

>[!NOTE]
>
>Priority score is available for inbound channels: web, in-app, and code-based channels. In journey, priority score is available for the **in-app** and **code-based** channels only. 

➡️ [Discover this feature in video](#video)

Assigning a priority score is crucial for inbound communication such as Web, Mobile, & In-App. If you have multiple campaigns using the same channel configuration (e.g. a banner on the top of your webpage), this could be problematic as only content from one campaign can feasibly be shown. The priority score is where you will insert your preference for which campaign should be shown when the recipient may qualify for more than one campaign.  

To assign a priority score to a journey or campaign, enter a numeric value (from 0-100) in the **[!UICONTROL Priority score]** field located in the journey or campaign properties. Please note, the higher the number, the higher the priority. If you were authoring this campaign and wanted to make sure that this campaign content is shown, you would give it a score of 100.  

![](assets/priority-score.png)

For situations where two campaigns have the same priority score, the campaign which was activated first will be shown.

## How-to video {#video}

>[!VIDEO](https://video.tv.adobe.com/v/3435529?quality=12)
