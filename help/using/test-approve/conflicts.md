---
title: Identify potential conflicts in journeys & campaigns
description: Learn how to identify potential conflicts in journeys & campaigns.
role: User
level: Beginner
badge: label="Limited Availability"
hide: yes
hidefromtoc: yes
---

# Detect potential conflicts in journeys & campaigns {#conflict}

>[!BEGINSHADEBOX]

What you'll find in this documentation guide:

* [Get started with conflict management & prioritization](gs-conflict-prioritization.md)
* **[Detect potential conflicts in journeys & campaigns](conflicts.md)**
* [Assign priority scores to journeys & campaigns](priority-scores.md)
* [Journey capping & arbitration](journey-capping.md)

>[!ENDSHADEBOX]

>[!AVAILABILITY]
>
>Conflict management & prioritization tools are currently available as a Limited Availability to selected users only.

As marketers increase the volume of Campaigns and Journeys in Journey Optimizer it becomes increasingly difficult for a marketer to know if they are bombarding their customers with too many marketing interactions. it is therefore essential to easily identify when there are overlapping campaigns and journeys to ensure they are striking the right balance of marketing communications while mitigating the risk of customer fatigue. 

Key areas to monitor for potential overlap are:

* **Timeline** (start and end dates): Are too many journeys running simultaneously? 
* **Audience**: What percentage of my journey audience is also part of other journeys? 
* **Channel**: Are there other communications scheduled for the same timeframe, and if so, how many?  
* **Capping Rule Set**: Which types of journeys am I capping and is there overlap within those? 
* **Channel Configuration**: Are there other journeys or campaigns using any channel configuration that is being used in the same journey or campaign that might prevent the journey or campaign from being shown to the end user?

## How Journey Optimizer detects conflicts {#detection}

Below is a summary of how Journey Optimizer identifies potential conflicts for journeys and campaigns:

* **Conflict identification scope**: Conflicts are shown only for live or scheduled campaigns and journeys.
* **Unitary journeys**: If the selected journey is unitary, other journeys that start with the same event are displayed, as this event will trigger all such journeys.
* **Audience qualification and Read Audience/Business Event** journeys: If the selected journey is either an Audience qualification or a Read Audience/Business Event journey, all other journeys of the same type with a valid audience are displayed, as there can be overlaps between the audiences.
* **Campaigns**: Since all campaigns are targeting audiences and there is no concept of events, all campaigns potentially conflict with segment-triggered journeys (starting with a Read audience activity).
* **Live/Scheduled campaigns**: Live and scheduled campaigns may conflict with one another due to potential audience overlap. For any given campaign, all live or scheduled campaigns are listed in the conflict viewer.

## View identified conflicts for a given journey or campaign {#view}

When authoring a journey or campaign, Journey Optimizer allows you to check whenever there’s a possibility of overlap with other journeys or campaigns. To do this, follow these steps:

1. At the time of authoring a journey or campaign, click the **[!UICONTROL View Potential Conflicts]** button in the journey or campaign properties.

    ![](assets/view-conflicts.png)

    >[!NOTE]
    >
    >The **[!UICONTROL View potential conflicts]** button becomes available to select as soon as you have assigned any of the following settings: **[!UICONTROL Start / end date]**, **[!UICONTROL Audience]**, **[!UICONTROL Channel]**, **[!UICONTROL Channel configuration]**, and **[!UICONTROL Rule set]**. Ensure you select **[!UICONTROL Save]** after assigning these settings, as the button will not be selectable until changes are saved.

1. The **[!UICONTROL Potential conflicts]** window opens, allowing you to visualize all elements that are overlapping the current journey/campaign. 

    You can open an overlapping journey or campaign directly from this screen by selecting its name.

    ![](assets/potential-conflicts.png)

    >[!NOTE]
    >
    >Newly published campaigns might take upto 5 mins to show up in the conflict viewer, due to caching implemented

To further refine your search for potential overlaps, you can filter your list of campaigns and journeys based on whichever field(s) are relevant. To do this, select the filter icon in the inventory view. [Learn how to work with filters](../start/search-filter-categorize.md#filter-lists)

## Resolve conflicts {#resolve}

Here are some tips to reduce the potential conflicts once they have been identified:

* Adjust the **start/end dates** to avoid overlapping campaigns or journeys.
* Refine **audience targeting** to minimize overlap between journeys.
* Implement **frequency caps** to prevent customers from receiving too many communications.
* Reduce the number of **active journeys** to manage customer experience more effectively.
* Set **priorities** on inbound actions to ensure the most important action is displayed to customers.

By leveraging these capabilities, you can ensure your marketing efforts are aligned and that you maintain the right balance in your communications strategy.
