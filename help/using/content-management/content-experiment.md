---
solution: Journey Optimizer
product: journey optimizer
title: Create a Content Experiment
description: Learn how to create a content experiment in your campaigns
feature: Experimentation
topic: Content Management
role: User
level: Beginner
keywords: content, experiment, multiple, audience, treatment
exl-id: bd35ae19-8713-4571-80bc-5f40e642d121
---
# Create a content experiment {#content-experiment}

>[!CONTEXTUALHELP]
>id="ajo_campaigns_content_experiment"
>title="Content experiment"
>abstract="You can choose to vary the message content, subject, or sender in order to define multiple treatments and determine the best combination for your audiences."

>[!NOTE]
>
>Before starting with Content Experiment, make sure that your reporting configuration is set for your custom datasets. Learn more in [this section](../reports/reporting-configuration.md).

The Journey Optimizer Content Experiment enables you to define multiple delivery treatments in order to measure which one performs best for your target audience. You can choose to vary the delivery content, subject, or sender. The audience of interest is randomly allocated to each treatment to determine which one works best in terms of the specified metric.

![](../rn/assets/do-not-localize/experiment.gif)

In the example below, the delivery target has been split into two groups, each representing 45% of the targeted population, and a holdout group of 10%, who will not receive the delivery.

Each person in the targeted audience will receive one version of an email, with a subject line that is one of the following two:

* one directly promoting a 10% offer on the new collection and an image.
* the other one only advertising a special offer without specifying the 10% off without any image. 

The goal here is to see if recipients will interact with the email depending on the received experiment. We therefore will choose **[!UICONTROL Email Opens]** as the primary goal metric in this Content Experiment.

![](assets/content_experiment.png)

## Create your content {#campaign-experiment}

1. Begin by creating and configuring your Email, SMS or Push notification [campaign](../campaigns/create-campaign.md) or [journey](../building-journeys/journeys-message.md) according to your requirements.

1. From the **[!UICONTROL Edit content]** window, start personalizing the treatment A.

    For this treatment, we will specify the special offer directly in the subject line and add personalization.

    ![](assets/content_experiment_5.png)

1. Create or import your original content and personalize it as needed.

## Configure your content experiment {#configure-experiment}

>[!CONTEXTUALHELP]
>id="ajo_campaigns_content_experiment_dimension"
>title="Dimension"
>abstract="Choose the specific dimension to track for your Experiment, such as specific clicks or views of specific pages."

>[!CONTEXTUALHELP]
>id="ajo_campaigns_content_experiment_success_metric"
>title="Success metric"
>abstract="Success metric is used to track and evaluate the best performing treatment in an experiment. Be sure to set up your dataset for certain metrics before using it."

1. When your message is personalized, from the campaign summary page, click **[!UICONTROL Create experiment]** to start configuring your content experiment.

    ![](assets/content_experiment_3.png)

1. Select the **[!UICONTROL Success metric]** you want to set for your experiment.

    For this example, select **[!UICONTROL Email open]** to test if profiles open their emails if the promo code is in the subject line.

    ![](assets/content_experiment_11.png)

1. When setting up an experiment using the In-app or Web channel and choosing the **[!UICONTROL Inbound Clicks]**, **[!UICONTROL Unique Inbound Clicks]** , **[!UICONTROL Page Views]** , or **[!UICONTROL Unique Page Views metrics]** , the **[!UICONTROL Click Action]**  drop-down enables you to precisely track and monitor clicks and views on specific pages.

    ![](assets/content_experiment_20.png)

1. Click **[!UICONTROL Add treatment]** to create as many new treatment as needed.

    ![](assets/content_experiment_8.png)

1. Change the **[!UICONTROL Title]** of your treatment to better differentiate them.

1. Choose to add a **[!UICONTROL Holdout]** group to your delivery. This group will not receive any content from this campaign. 

    Switching on the toggle bar will automatically take 10% of your population, you can adjust this percentage if needed.

    >[!IMPORTANT]
    >
    >When a holdout group is used in an action for content experimentation, the holdout assignment only applies to that specific action. After the action is completed, profiles in the holdout group will continue down the journey path and can receive messages from other actions. Therefore, ensure that any subsequent messages do not rely on the receipt of a message by a profile that might be in a holdout group. If they do, you may need to remove the holdout assignment.

    ![](assets/content_experiment_12.png)

1. You can then choose to allocate a precise percentage to each **[!UICONTROL Treatment]** or simply switch on the **[!UICONTROL Distribute evenly]** toggle bar.

    ![](assets/content_experiment_13.png)

1. Click **[!UICONTROL Create]** when your configuration is set.

## Design your treatments {#treatment-experiment}

1. From the **[!UICONTROL Edit content]** window, select your treatment B to change the content.

    Here, we choose to not specify the offer in the **[!UICONTROL Subject line]**.

    ![](assets/content_experiment_18.png)

1. Click **[!UICONTROL Edit email body]** to further personalize your treatment B.

    ![](assets/content_experiment_9.png)

1. After designing your treatments, click **[!UICONTROL More actions]** to access options related to your treatments: **[!UICONTROL Rename]**, **[!UICONTROL Duplicate]** and **[!UICONTROL Delete]**.

    ![](assets/content_experiment_7.png)

1. If needed, access the **[!UICONTROL Experiment settings]** menu to change your treatments configuration.

    ![](assets/content_experiment_19.png)

1. Once your message content has been defined, click the **[!UICONTROL Simulate content]** button to control the rendering of your delivery, and check personalization settings with test profiles. [Learn more](../content-management/preview-test.md)

After configuring your experimentation, you can follow the success of your delivery with your report. [Learn more](../reports/campaign-global-report-cja-experimentation.md)
