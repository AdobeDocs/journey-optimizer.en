---
title: Publish and manage code-based experiences
description: Learn how to publish and stop code-based experiences in Journey Optimizer
feature: Code-based Experiences
topic: Content Management
role: User
level: Experienced

---
# Manage code-based experiences {#publish-code-based}

## Make your code-based experience live {#code-based-experience-live}

>[!IMPORTANT]
>
> If your campaign is subject to an approval policy, you will need to request approval in order to be able to activate your code-based experiences. [Learn more](../test-approve/gs-approval.md)

Once you defined your code-based experience and edited your content as desired using the [code-based editor](create-code-based.md#edit-code), you can activate your journey or campaign to make your changes visible to your audience.

You can also preview your code-based experience content before making it live. [Learn more](test-code-based.md)

>[!NOTE]
>
>If you activate a code-based journey/campaign impacting the same pages as another journey or campaign which is already live, all the changes will be applied to your content.
>
>If multiple code-based journeys or campaigns update the same element(s) of your content, the highest priority journey/campaign takes precedence.

Once your code-based journey or campaign is live, your app implementation team is responsible for making explicit API or SDK calls to fetch content for the surfaces defined in the selected [code-based experience configuration](code-based-configuration.md). Learn more on the different customer implementations in [this section](code-based-implementation-samples.md).

### Publish a code-based journey {#publish-code-based-journey}

To make your code-based experience live from a journey, follow the steps below.

1. Verify that your journey is valid and that there is no error. [Learn more](../building-journeys/troubleshooting.md#checking-for-errors-before-testing)

1. From the journey, select the **[!UICONTROL Publish]** option, located in the top right drop-down menu.

    ![](assets/code-based-journey-publish.png)

    >[!NOTE]
    >
    >Learn more on publishing journeys in [this section](../building-journeys/publishing-the-journey.md).

Your code-based journey takes the **[!UICONTROL Live]** status and is now visible to the selected audience. Each recipient of your journey can see your modifications.

>[!NOTE]
>
>After you click **[!UICONTROL Publish]**, it can take up to 15 minutes for the changes to be available live.

### Activate a code-based campaign {#activate-code-based-campaign}

1. From your code-based campaign, select **[!UICONTROL Review to activate]**.

    ![](assets/code-based-campaign-review.png)

1. Check and edit if needed the content, properties, configuration, audience and schedule.

1. Select **[!UICONTROL Activate]**.

    ![](assets/code-based-campaign-activate.png)

    >[!NOTE]
    >
    >Learn more on activating campaigns in [this section](../campaigns/review-activate-campaign.md).

Your code-based campaign takes the **[!UICONTROL Live]** status and is now visible to the selected audience. Each recipient of your campaign can see the modifications you added to your content.

>[!NOTE]
>
>After you click **[!UICONTROL Activate]**, it can take up to 15 minutes for your changes to be available live.
>
>If you defined a schedule for your code-based campaign, it has the **[!UICONTROL Scheduled]** status until the start date and time are reached.

## Stop a code-based journey or campaign {#stop-code-based-experience}

When a code-based experience is live, you can stop it to prevent your audience from seeing your modifications. Follow the steps below.

1. Select a live journey or campaign from the respective list.

1. Perform the relevant action according to your case:

    * From the campaign top menu, select **[!UICONTROL Stop campaign]**.

        ![](assets/code-based-campaign-stop.png)

    * From the journey top menu, click the **[!UICONTROL More]** button and select **[!UICONTROL Stop]**.

        ![](assets/code-based-journey-stop.png)

1. The modifications you added will not be visible anymore to the audience you defined.

>[!NOTE]
>
>Once a code-based journey or campaign is stopped, you cannot edit or activate it again. You can only duplicate it and activate the duplicated journey/campaign.

<!--Reporting TBC

## Check the code-based experience reports {#check-code-based-reports}

Once your code-based experience is live, you can check the **[!UICONTROL Code-based]** tab of the  [Journey report](../reports/journey-global-report-cja.md#web-cja) and [Campaign report](../reports/campaign-global-report-cja.md#web) to compare elements such as the number of experiences delivered to your audience, and the number of engagements with your content.-->

<!--## Code-based reports

You can access code-based journey or campaign reports from the summary screen.

Global reports display events that occurred at least two hours ago and cover events over a selected time period. In comparison, Live reports focus on events that took place within the past 24 hours, with a minimum time interval of two minutes from the event occurrence.

### Code-based live report {#live-report-code-based}

From your campaign **[!UICONTROL Live report]**, the **[!UICONTROL Code-based experience]** tab details the main information relative to your apps or web pages. [Learn more on live report](../reports/campaign-live-report.md)

+++Learn more on the different metrics and widgets available for the Code-based experience report.

The **[!UICONTROL Code-based experience performance]** KPIs detail the main information relative to your visitors' engagement with your code-based experiences, such as:

* **[!UICONTROL Impressions]**: total number of experiences delivered to all users.

* **[!UICONTROL Interactions]**:  total number of engagements with your app/page. This includes any actions taken by the users, such as clicks or any other interactions.

The **[!UICONTROL Code-based experience summary]** graph shows the evolution of your experiences (impressions, unique impressions and interactions) for the last 24 hours.

TBC: The **[!UICONTROL Interactions by element]** table details the main information relative to your visitors' engagement with the various elements on your app/pages.
+++

### Code-based global report {#global-report-code-based}

Code-based campaign global report can be accessed directly from your journey or campaign with the **[!UICONTROL View report]** button. [Learn more on global report](../reports/campaign-global-report-cja.md)

From your Campaign **[!UICONTROL Global report]**, the **[!UICONTROL Code-based experience]** tab details the main information relative to your apps or web pages.

![](assets/code-based-campaign-global-report.png)

Add image TBC

+++Learn more on the different metrics and widgets available for the Code-based experience report.

The **[!UICONTROL Code-based experience performance]** KPIs detail the main information relative to your visitors' engagement with your experiences, such as:

* **[!UICONTROL Unique impressions]**: number of unique users to whom the experience was delivered.

* **[!UICONTROL Impressions]**: total number of experiences delivered to all users.

* **[!UICONTROL Interactions]**: percentage of engagements with your app/page. This includes any actions taken by the users, such as clicks or any other interactions.

The **[!UICONTROL Code-based experience summary]** graph shows the evolution of your experiences (unique impressions, impressions and interactions) for the concerned period.

TBC: The **[!UICONTROL Interactions by element]** table details the main information relative to your visitors' engagement with the various elements on your apps/pages.
+++

-->

