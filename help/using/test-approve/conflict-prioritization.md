---
title: Conflict management & prioritization
description: Learn how to preview and test your content.
feature: Preview, Proofs
role: User
level: Beginner
badge: label="Limited Availability"
hide: yes
hidefromtoc: yes
---

# Conflict management & prioritization {#conflict-prioritization}

>[!AVAILABILITY]
>
>Conflict management & prioritization tools are currently available as a beta to selected users only.

In Journey Optimizer, managing the volume and timing of campaigns and journeys is essential to avoid overwhelming customers with too many interactions. The following two sections introduce key tools to help you maintain balance and prioritize communications effectively

## Identify potential conflicts in journeys & campaigns {#conflict}

>[!CONTEXTUALHELP]
>id="ajo_campaigns_campaign_conflict"
>title="Conflict viewer in campaigns"
>abstract="This tool can help you determine overlap with other journeys, campaigns, or channel configurations. If you wish to identify overlap on audience, start & end date, channel configuration, channel, or rule set you can view potential conflicts here."

>[!CONTEXTUALHELP]
>id="ajo_journey_conflict"
>title="Conflit viewer in journeys"
>abstract="This tool can help you determine overlap with other journeys, campaigns, or channel configurations. If you wish to identify overlap on audience, start & end date, channel configuration, channel, or rule set you can view potential conflicts here."

As marketers increase the volume of Campaigns and Journeys in Journey Optimizer it becomes increasingly difficult for a marketer to know if they are bombarding their customers with too many marketing interactions. it is therefore essential to easily identify when there are overlapping campaigns and journeys to ensure they are striking the right balance of marketing communications while mitigating the risk of customer fatigue. 

Key areas to monitor for potential overlap are:

* **Timeline** (start and end dates): Are too many journeys running simultaneously? 
* **Audience**: What percentage of my journey audience is also part of other journeys? 
* **Channel**: Are there other communications scheduled for the same timeframe, and if so, how many?  
* **Capping Rule Set**: Which types of journeys am I capping and is there overlap within those? 
* **Channel Configuration**: Are there other journeys or campaigns using any channel configuration that is being used in the same journey or campaign that might prevent the journey or campaign from being shown to the end user?

### How Journey Optimizer detects conflicts {#detection}

Below is a summary of how Journey Optimizer identifies potential conflicts for journeys and campaigns:

* **Conflict identification scope**: Conflicts are shown only for live or scheduled campaigns and journeys.
* **Unitary journeys**: If the selected journey is unitary, other journeys that start with the same event are displayed, as this event will trigger all such journeys.
* **Audience qualification and Read Audience/Business Event** journeys: If the selected journey is either an Audience qualification or a Read Audience/Business Event journey, all other journeys of the same type with a valid audience are displayed, as there can be overlaps between the audiences.
* **Campaigns**: Since all campaigns are targeting audiences and there is no concept of events, all campaigns potentially conflict with segment-triggered journeys (starting with a Read audience activity).
* **Live/Scheduled campaigns**: Live and scheduled campaigns may conflict with one another due to potential audience overlap. For any given campaign, all live or scheduled campaigns are listed in the conflict viewer.

### View identified conflicts for a given journey or campaign {#view}

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

### Resolve conflicts {#resolve}

Here are some tips to reduce the potential conflicts once they have been identified:

* Adjust the **start/end dates** to avoid overlapping campaigns or journeys.
* Refine **audience targeting** to minimize overlap between journeys.
* Implement **frequency caps** to prevent customers from receiving too many communications.
* Reduce the number of **active journeys** to manage customer experience more effectively.
* Set **priorities** on inbound actions to ensure the most important action is displayed to customers.

By leveraging these capabilities, you can ensure your marketing efforts are aligned and that you maintain the right balance in your communications strategy.

## Assign priority scores to journeys & campaigns {#priority}

>[!CONTEXTUALHELP]
>id="ajo_journey_priority"
>title="Priority"
>abstract="Assign a priority score to the journey, ranging from 0 to 100. A higher number indicates a higher priority. The priority value inserted here is inherited by any inbound actions (such as In-App) contained in this journey. For situations where this same inbound channel configuration is used in other campaigns or journeys, the inbound action with the highest priority score is shown to the recipient. If multiple journeys or campaigns have the same score, the element that was most recently modified is chose."

>[!CONTEXTUALHELP]
>id="ajo_campaigns_campaign_priority"
>title="Priority"
>abstract="Assign a priority score to the campaign, ranging from 0 to 100. A higher number indicates a higher priority. For situations where this same inbound channel configuration (such as In-App) is used in other campaigns or journeys, the inbound action with the highest priority score is shown to the recipient. If multiple journeys or campaigns have the same score, the element that was most recently modified is chose."

Journey Optimizer allows you to assign a priority score to a journey or campaign. Priority is essential to prioritize a journey, campaign, or action when there is an imposed constraint (such as a frequency cap). In situations where a customer qualifies for many journeys, campaigns, or communications and you want to be selective as to which they should enter and receive, you should utilize this field.

>[!NOTE]
>
>Priority score is available for inbound channels: web, in-app, and code-based channels. In journey, priority score is available for the **in-app** and **code-based** channels only. 

Assigning a priority score is crucial for inbound communication such as Web, Mobile, & In-App. If you have multiple campaigns using the same channel configuration (e.g. a banner on the top of your webpage), this could be problematic as only content from one campaign can feasibly be shown. The priority score is where you will insert your preference for which campaign should be shown when the recipient may qualify for more than one campaign.  

To assign a priority score to a journey or campaign, enter a numeric value (from 0-100) in the **[!UICONTROL Priority score]** field located in the journey or campaign properties. Please note, the higher the number, the higher the priority. If you were authoring this campaign and wanted to make sure that this campaign content is shown, you would give it a score of 100.  

![](assets/priority-score.png)

For situations where two campaigns have the same priority score, the campaign which was activated first will be shown.
