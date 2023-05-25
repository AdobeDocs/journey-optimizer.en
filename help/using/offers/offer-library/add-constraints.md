---
title: Add constraints to an offer
description: Learn how to define the conditions for an offer to be displayed
feature: Offers
topic: Integrations
role: User
level: Intermediate
exl-id: 7234a8e8-4ab0-4f17-a833-5e452fadac35
---
# Add constraints to an offer {#add-constraints}

>[!CONTEXTUALHELP]
>id="od_offer_constraints"
>title="About offer constraints"
>abstract="With constraints, you can specify how the offer is prioritized and presented to the user compared to other offers."

>[!CONTEXTUALHELP]
>id="ajo_decisioning_constraints"
>title="About offer constraints"
>abstract="With constraints, you can specify how the offer is prioritized and presented to the user compared to other offers."

>[!CONTEXTUALHELP]
>id="od_offer_priority"
>title="About offer priority"
>abstract="In this field, you can specify priority settings for the offer. Priority is a number used to rank offers that meet all constraints such as eligibility, dates, and capping."

>[!CONTEXTUALHELP]
>id="ajo_decisioning_priority"
>title="Set priority"
>abstract="The priority helps define the priority of the offer compared to other ones if the user qualifies for more than one offer. The higher an offer's priority will be, the higher its priority will be compared to other offers."

Constraints allow you to define the conditions under which an offer will be displayed.

1. Configure the **[!UICONTROL Offer eligibility]**. [Learn more](#eligibility)

   ![](../assets/offer-eligibility.png)

1. Define the **[!UICONTROL Priority]** of the offer compared to other ones if the user qualifies for more than one offer. The higher an offer's priority will be, the higher its priority will be compared to other offers.

   ![](../assets/offer-priority.png)

1. Specify the offer's **[!UICONTROL Capping]**, meaning the number of times the offer will be presented. [Learn more](#capping)

   ![](../assets/offer-capping.png)

1. Click **[!UICONTROL Next]** to confirm all the constraints you defined.
        
For example, if you set the following constraints:

![](../assets/offer-constraints-example.png)

* The offer will be considered for users that match the "Gold Loyalty Customers" decision rule only.
* The offer's priority is set to "50", meaning the offer will be presented before offers with a priority between 1 and 49, and after the ones with a priority of at least 51.
* The offer will be presented only once a month per user accross all placements.

## Eligibility {#eligibility}

>[!CONTEXTUALHELP]
>id="ajo_decisioning_eligibility"
>title="Define eligibility"
>abstract="By default, any profile will be eligible to be presented the offer, but you can use segments or decision rules to restrict the offer to specific profiles."

>[!CONTEXTUALHELP]
>id="od_offer_eligibility"
>title="About offer eligibility"
>abstract="In this section, you can use decision rules to determine which users are eligible to the offer."
>additional-url="https://video.tv.adobe.com/v/329373" text="Watch demo video"

>[!CONTEXTUALHELP]
>id="ajo_decisioning_total_profile_estimate"
>title="Total profile estimate"
>abstract="When you select segments or decision rules, you can see information on the estimated qualified profiles."

The **[!UICONTROL Offer eligibility]** section allows you to restrict the offer to specific profiles that you define using segments or decision rules.

>[!NOTE]
>
>Learn more on using **segments** versus **decision rules** in [this section](#segments-vs-decision-rules).

* By default, the **[!UICONTROL All visitors]** option is selected, meaning that any profile will be eligible to be presented the offer.

    ![](../assets/offer-eligibility-default.png)

* You can also limit the presentation of the offer to the members of one or several [Adobe Experience Platform segments](../../segment/about-segments.md).

    To do this, activate the **[!UICONTROL Visitors who fall into one or multiple segments]** option, then add one or several segments from the left pane and combine them using the **[!UICONTROL And]** / **[!UICONTROL Or]** logical operators.
    
    ![](../assets/offer-eligibility-segment.png)

* If you want to associate a specific [decision rule](../offer-library/creating-decision-rules.md) to the offer, select **[!UICONTROL By defined decision rule]**, then drag the desired rule from the left pane into the **[!UICONTROL Decision rule]** area.

    ![](../assets/offer_rule.png)

    >[!CAUTION]
    >
    >Event-based offers are currently not supported in [!DNL Journey Optimizer]. If you create a decision rule based on an [event](https://experienceleague.adobe.com/docs/experience-platform/segmentation/ui/segment-builder.html#events){target="_blank"}, you will not be able to leverage it in an offer.

When you select segments or decision rules, you can see information on the estimated qualified profiles. Click **[!UICONTROL Refresh]** to update data.

![](../assets/offer-eligibility-segment-estimate.png)

>[!NOTE]
>
>Profile estimates are unavailable when rule parameters include data not in the profile such as context data. For example, an eligibility rule that requires the current weather to be ≥80 degrees.

### Using segments vs decision rules {#segments-vs-decision-rules}

To apply a constraint, you can restrict the selection of offers to the members of one or several **Adobe Experience Platform segments**, or you can use a **decision rule**, both solutions corresponding to different usages.

Basically, the output of a segment is a list of profiles, whereas a decision rule is a function executed on demand against a single profile during the decisioning process. The difference between those two usages are detailed below.

* **Segments**

    On one hand, segments are a group of Adobe Experience Platform profiles that match a certain logic based on profile attributes and experience events. However, Offer Management does not recompute the segment, which may not be up-to-date when presenting the offer.

    Learn more on segments in [this section](../../segment/about-segments.md).

* **Decision rules**
    
    On the other hand, a decision rule is based on data available in Adobe Experience Platform and determines to whom an offer can be shown. Once selected in an offer or a decision for a given placement, the rule is executed every single time a decision is made, which ensures that each profile gets the latest and the best offer.

    Learn more on decision rules in [this section](creating-decision-rules.md).

## Capping {#capping}

>[!CONTEXTUALHELP]
>id="od_offer_globalcap"
>title="About offer capping"
>abstract="In this field, you can specify how many times the offer can be presented."

>[!CONTEXTUALHELP]
>id="ajo_decisioning_capping"
>title="Use capping"
>abstract="To avoid over-solicitating your customers, use capping to define the maximum number of times an offer can be presented."
>additional-url="https://experienceleague.adobe.com/docs/journey-optimizer/using/offer-decisioning/managing-offers-in-the-offer-library/configure-offers/add-constraints.html#capping-change-date" text="Changing dates can impact capping"

>[!CONTEXTUALHELP]
>id="ajo_decisioning_frequency_capping"
>title="Set the capping frequency"
>abstract="You can choose to reset the offer capping counter on a daily, weekly or monthly basis. Note that after saving your offer, you will not be able to change the selected frequency."

>[!CONTEXTUALHELP]
>id="ajo_decisioning_frequency_capping_impression"
>title="Impression"
>abstract="The use of impressions as capping events is available for inbound channels only."

Capping is used as a constraint to define the maximum number of times an offer can be presented.

Limiting the number of times users get specific offers allows you to avoid over-solicitating your customers and thus to optimize each touchpoint with the best offer.

To set capping, follow the main steps below.

1. Make sure the **[!UICONTROL Include capping]** toggle button is selected. Capping is included by default.

    >[!CAUTION]
    >
    >It is not possible to enable or disable frequency capping for previously created offers. To do so, you need to duplicate the offer or create a new one.

1. Define which **[!UICONTROL Capping event]** will be taken into account to increase the counter. [Learn more](#capping-event)

1. Set the number of times the offer can be presented. [Learn more](#capping-count)

1. Choose if you want the capping to be applied to all users or just one profile. [Learn more](#capping-type)

1. Set the **[!UICONTROL Frequency]** to define how often the capping count is reset. [Learn more](#frequency-capping)

1. If you have defined several [representations](add-representations.md) for your offer, specify whether you want to apply capping **[!UICONTROL Across all placements]** or **[!UICONTROL For each placement]**. [Learn more](#placements)

1. Once saved and approved, if the offer has been presented the number of times you have specified in this field according to the criteria and the timeframe you defined, its delivery will stop.

The number of times an offer is proposed is calculated at email preparation time. For example, if you prepare an email with a number of offers, those numbers count towards your max cap regardless of whether or not the email is sent.

<!--If an email delivery is deleted or if the preparation is done again before being sent, the capping value for the offer is automatically updated.-->

>[!NOTE]
>
>Capping counters will reset when the offer expires or 2 years after the offer start date, whichever comes first. Learn how to define an offer's date in [this section](creating-personalized-offers.md#create-offer).

### Capping event {#capping-event}

The **[!UICONTROL Capping event]** field allows you to define which **[!UICONTROL Capping event]** will be taken into account to increase the counter:

![](../assets/offer-capping-event.png)

* **[!UICONTROL Decision event]** (default value): Maximum number of times an offer can be presented.
* **[!UICONTROL Impression]**: Maximum number of times the offer can be displayed to a user.

    >[!NOTE]
    >
    >The use of impressions as capping events is available for **inbound channels** only.

* **[!UICONTROL Clicks]**: Maximum number of times the offer can be clicked by a user.
* **[!UICONTROL Custom event]**: You can define a custom event that will be used to cap the number of offers sent. For example, you can cap on the number of redemptions until they equal 10000, or until a given profile has redeemed 1 time. To do so, use [Adobe Experience Platform XDM](https://experienceleague.adobe.com/docs/experience-platform/xdm/home.html){target="_blank"} schemas to build a custom event rule.
        
    <!--For example, you can cap on the number of redemptions so that the offer can be shown until redemptions equal 10000. You can only select XDM ExperienceEvents. -->

    In the example below, you want to cap on the number of checkouts.

    1. Select **[!UICONTROL Custom event]** from the list and use the **[!UICONTROL Add custom event]** button.
    
        ![](../assets/offer-capping-custom-event-add.png)
        
    1. Use the **[!UICONTROL Create custom event rules]** builder to select the relevant event. You can choose any user action that you want to cap offers on.
    
        Here choose **[!UICONTROL Commerce]** > **[!UICONTROL Checkouts]** > **[!UICONTROL Value]** and select **[!UICONTROL exists]** from the drop-down list.

        ![](../assets/offer-capping-custom-event.png)

    1. Once the rule is created, it displays in the **[!UICONTROL Custom event query]** field.

        ![](../assets/offer-capping-custom-event-query.png)

>[!CAUTION]
>
>For all capping events except decision event, the decision management feedback may not be automatically collected, which could result in the capping counter not being correctly incremented. [Learn more](../data-collection/data-collection.md)
>
>To make sure each capping event is tracked and accounted for in the capping counter, ensure that the schema used to collect experience events includes the correct field group for that event. [Learn more](../data-collection/schema-requirement.md)

### Capping count {#capping-count}

The **[!UICONTROL Capping count]** field allows you to specify the number of times the offer can be presented.

![](../assets/offer-capping-times.png)

>[!NOTE]
>
>The number must be an integer greater than 0.

For example, you defined a custom capping event such as the number of checkouts is taken into account. If you enter 10 in the **[!UICONTROL Capping count]** field, no more offers will be sent after 10 checkouts.

### Capping type {#capping-type}

You can also specify if you want the capping to be applied accross all users or to one specific profile:

![](../assets/offer-capping-total.png)

* Select **[!UICONTROL In total]** to define how many times an offer can be proposed across the combined target audience, meaning across all users.

    For example, if you are an electronics retailer having a 'TV doorbuster deal', you want the offer to be only returned 200 times across all profiles.

* Select **[!UICONTROL Per profile]** to define how many times an offer can be proposed to the same user.

    For example, if you are a bank with a 'Platinum credit card' offer, you don't want this offer to be shown more than 5 times per profile. Indeed, you believe that if the user has seen the offer 5 times and not acted on it, they have a higher chance to act on the next best offer.

### Frequency capping {#frequency-capping}

The **[!UICONTROL Frequency]** section allows you to define how often the capping count is reset. To do so, define the time period for the counting (daily, weekly or monthly) and enter the number of days/weeks/months of your choice.

![](../assets/offer-capping-frequency.png)

>[!NOTE]
>
>The reset happens at 12am UTC, on the day that you defined or on the first day of the week/month when applicable. The week start day is Sunday. Any duration you choose cannot exceed 2 years (i.e. the corresponding number of months, weeks or days).
    
For example, if you want the capping count to be reset every 2 weeks, select **[!UICONTROL Weekly]** from the **[!UICONTROL Repeat]** drop-down list and type **2** in the other field. The reset will happen every other Sunday at 12pm UTC.

>[!CAUTION]
>
>After saving your offer, you will not be able to change the time period (monthly, weekly or daily) you selected for the frequency.

### Capping and placements {#placements}

If you have defined several [representations](add-representations.md) for your offer, specify whether you want to apply capping **[!UICONTROL Across all placements]** or **[!UICONTROL For each placement]**.

![](../assets/offer-capping-placement.png)

* **[!UICONTROL Across all placements]**: capping counts will total all decisions across the placements associated with the offer.
    
    For example, if an offer has an **Email** placement and a **Web** placement, and you set the capping at **2 per profile across all placements**, then each profile could receive the offer up to 2 times in total, regardless of the placement mix.

* **[!UICONTROL For each placement]**: capping counts will apply decision counts for each placement separately.
    
    For example, if an offer has an **Email** placement and a **Web** placement, and you set the capping at **2 per profile for each placement**, then each profile could receive the offer up to 2 times for the email placement, and an additional 2 times for the web placement.

### Impact of changing dates on capping {#capping-change-date}

>[!CONTEXTUALHELP]
>id="ajo_decisioning_offer_change_date"
>title="Changing dates can impact capping"
>abstract="If capping is applied to this offer, it can be impacted when you change the start or end date."

You must proceed with care when changing the date of an offer, because this can have an impact on capping if the following conditions are met:

* The offer is [approved](#review).
* [Capping](#capping) is already applied to the offer.
* Capping is defined per profile.

>[!NOTE]
>
>Learn how to define an offer's date in [this section](creating-personalized-offers.md#create-offer).

Capping per profile stores the capping counts on each profile. When you change the start and end date of an approved offer, the capping count for some profiles could be impacted according to the different scenarios described below.

![](../assets/offer-capping-change-date.png)

Here are the possible scenarios when **changing an offer start date**:

| Scenario:<br>If... | What happens:<br>then... | Possible impact on the capping count |
|--- |--- |--- |
| ... the offer start date is updated before the original offer start date has begun, | ... the capping count will begin on the new start date. | No |
| ... the new start date is before the current end date, | ... the capping will continue with a new start date and the previous capping count for each profile will carry forward. | No |
| ... the new start date is after the current end date, | ... the current capping will expire and the new capping count will start again from 0 for all profiles on the new start date. | Yes |

Here are the possible scenarios when **extending an offer end date**:

| Scenario:<br>If... | What happens:<br>then... | Possible impact on the capping count |
|--- |--- |--- |
| ... a decisioning request occurs before the original offer end date, | ... the capping count will be updated and the previous capping count for each profile will carry forward. | No |
| ... no decisioning request occurs before the original end date, | ... the capping count will reset on the original end date for each profile. The new capping count will then start again from 0 for any new decisioning requests that will occur after the original end date. | Yes |

**Example**

Let's say you have an offer with an original start date set to **January, 1**, expiring on **January, 31**.

1. Profiles X, Y and Z are presented the offer.
1. On **January, 10**, the offer's end date is changed to **February, 15**.
1. **From January 11 to January 31**, only profile Z is presented the offer.       
    
    * Because a decisioning request occurred before the original end date **for profile Z**, the offer's end date can be extended to **February, 15**.
    * However, as no activity occurred before the original end date for **profiles X and Y**, their counters will expire and their capping counts will be reset to 0 on **January, 31**.

![](../assets/offer-capping-change-date-ex.png)
