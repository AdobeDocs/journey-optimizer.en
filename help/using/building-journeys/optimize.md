---
solution: Journey Optimizer
product: journey optimizer
title: Condition activity
description: Learn about condition activity
feature: Journeys, Activities
topic: Content Management
role: User
level: Intermediate
keywords: activity, condition, canvas, journey, optimization
badge: label="Limited availability" type="Informative"
exl-id: f6618de4-7861-488e-90c0-f299ef5897ca
---
# Optimize activity {#journey-path-optimization}

>[!CONTEXTUALHELP]
>id="ajo_journey_optimize"
>title="Optimize activity"
>abstract="The **Optimize** activity lets you define how individuals progress through your journey by creating multiple paths based on specific criteria, including experimentation, targeting, and specific conditions."

>[!AVAILABILITY]
>
>This capability is available in Limited Availability. Contact your Adobe representative to gain access.

The **Optimize** activity lets you define how individuals progress through your journey by creating multiple **paths** based on specific criteria, including experimentation, targeting, and specific conditions - ensuring maximum engagement and success to create highly customized and effective journeys.

A **journey path** can consist of any of the following:

* sequencing of communications;
* time in between them;
* number of communications;
* or any combination of these three variables.

For example, one path could contain one email, another could contain two SMS messages, and a third could contain an email, a [Wait](wait-activity.md) node of two hours, and then an SMS message.

<!--With this feature, [!DNL Journey Optimizer] empowers you with the tools to deliver personalized and optimized paths to your audience, ensuring maximum engagement and success to create highly customized and effective journeys.-->

Through the **Optimize** activity you can:

* Run [path experiments](#experimentation)
* Leverage [targeting](#targeting) rules in each journey path
* Apply [conditions](#conditions) to your paths

![](assets/journey-optimize.png)

Once the journey is live, profiles are evaluated against the defined criteria, and based on matching criteria, they are sent down the appropriate path from the journey.

## Use experimentation {#experimentation}

Experimentation allows you to test different paths based on a random split to determine which performs best based on predefined success metrics.

To set up experimentation in a journey, follow the steps below.

Let's say you want to compare three paths:

* one path with one email;
* a second path with a Wait node of two days and an email;
* a third path with an email and then an SMS message.

1. Drop the **[!UICONTROL Optimize]** activity into the journey canvas.

1. Add an optional label to identify the activity in reporting and test mode logs.

1. Select **[!UICONTROL Experiment]** from the **[!UICONTROL Method]** drop-down list.

    ![](assets/journey-optimize-experiment.png){width=85%}

1. Click **[!UICONTROL Experiment settings]**.

1. Design and configure your experiment as wanted. [Learn how](../content-management/content-experiment.md)

    <!--
    ![](../campaigns/assets/msg-optimization-create-experiment.png){width=85%}
    Replace with appropriate screenshot
    The experiment applies to all the activities in the journey.TBC
   -->

Once the journey is live, users are randomly assigned to go down different paths. [!DNL Journey Optimizer] tracks which path drives more purchases and provides actionable insights.

<!--Follow the success of your journey with the [Experimentation journey report](../reports/campaign-global-report-cja-experimentation.md). Is there a report specific to experimentation in journey?-->

### Use cases with Experiment {#uc-experiment}

The following examples show how to use the **[!UICONTROL Optimize]** activity with the **[!UICONTROL Experiment]** method to determine which path works best overall.

**Channel effectiveness**

Test whether sending the first message by email versus SMS drives higher conversions.

* Use the conversion rate as the optimization metric (for example: purchases, sign-ups).

![](assets/journey-optimize-experiment-uc.png)

**Message frequency**

Run an experiment to check if sending one email versus three emails over a week results in more purchases.

* Use purchases or the unsubscribe rate as the optimization metric.

**Wait time between communications**

Compare a 24-hour wait versus a 72-hour wait before a follow-up to determine which timing maximizes engagement.

* Use the click-through rate or revenue as the optimization metric.

## Leverage targeting {#targeting}

Targeting allows you to determine specific rules or qualifications that must be met for a customer to be eligible to enter one of the journey paths, based on specific audience segments<!-- depending on profile attributes or contextual attributes-->.

Unlike experimentation, which is a random assignment of a given path, targeting is deterministic in terms of ensuring the right audience or profile enters the specified path.

With targeting, specific rules can be defined based on:

* **User profile attributes** such as location (eg. geo-targeting), age, or preferences. For example, users in the US see a "Golden Gate" promotion, while users in France see an "Eiffel Tower" promotion.

* **Contextual data** such as device type (eg. device-targeting), time of day, or session details. For example, desktop users receive desktop-optimized content, while mobile users receive mobile-optimized content.

* **Audiences** which can be used to include or exclude profiles that have a particular audience membership.

To set up targeting in a journey, follow the steps below.

1. Drop the **[!UICONTROL Optimize]** activity into the journey canvas.

1. Add an optional label to identify the activity in reporting and test mode logs.

1. Select **[!UICONTROL Targeting]** from the **[!UICONTROL Method]** drop-down list.

    ![](assets/journey-optimize-targeting.png){width=85%}

1. Click **[!UICONTROL Create targeting rule]**.

1. Use the rule builder to define your criteria. For example, define a rule for US residents, a rule for France residents, and a rule for India residents.

    ![](assets/journey-targeting-rule.png)

1. Select the **[!UICONTROL Enable fallback content]** as needed. Fallback content allows your audience to receive a default content when no targeting rules are qualified. If you do not select this option, any audience that doesn't qualify for a targeting rule defined above will not enter a fallback path.

1. Save your targeting rule settings.

1. Back in the journey, drop specific actions to customize each path. For example, you can create a specific email for US residents, another email for France residents, and so on.

    ![](assets/journey-targeting-paths.png)

1. Design appropriate content for each group defined by your targeting rule settings. You can seamlessly navigate between the different paths.

    ![](assets/journey-targeting-design.png)

   In this example, design a specific path for US residents, a different path for French residents and another path for India residents.

Once the journey is live, the path that is specified for each segment is processed so that US residents enter a specific path, France residents enter a different path, and so on.

### Use cases with Targeting {#uc-targeting}

The following examples show how to use the **[!UICONTROL Optimize]** activity with the **[!UICONTROL Targeting]** method to personalize paths for different sub-audiences.

**Segment-specific channels**

Gold status loyalty members can receive personalized offers via email, while all other members are directed to SMS reminders.

* Use the revenue per profile or conversion rate as the optimization metric.

![](assets/journey-optimize-targeting-uc.png)

**Behavior-based targeting**

Customers who opened an email but didn't click can be sent a push notification, while those who didn't open at all receive an SMS.

* Use the click-through rate or downstream conversions as the optimization metric.

**Purchase history targeting**

Customers who have recently purchased can go into a short "Thank you + Cross-sell" path, while those with no purchase history enter a longer nurture journey.

* Use the repeat purchase rate or engagement rate as the optimization metric.

## Add a condition {#conditions}

You can add a condition to define how individuals progress through your journey by creating multiple paths based on specific criteria. You can also configure an alternate path to handle timeouts or errors, ensuring a seamless experience.

![](assets/journey-condition.png)

Learn how to define a condition in [this section](conditions.md).

The following types of conditions are available:

* [Data Source condition](condition-activity.md#data_source_condition)
* [Time condition](condition-activity.md#time_condition) 
* [Percentage split](condition-activity.md#percentage_split) 
* [Date condition](condition-activity.md#date_condition)
* [Profile cap](condition-activity.md#profile_cap)
