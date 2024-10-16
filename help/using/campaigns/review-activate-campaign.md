---
solution: Journey Optimizer
product: journey optimizer
title: Review and activate a campaign
description: Learn how to review and activate campaigns in Journey Optimizer
feature: Campaigns
topic: Content Management
role: User
level: Intermediate
keywords: campaign, review, validation, activation, activating, optimizer
exl-id: 7c4afc98-0d79-4e26-90f8-558bac037169
---
# Review and activate a campaign {#review-activate} 

>[!IMPORTANT]
>
>Starting September release, a new campaign and journey activation experience allows you to manage the entire approval process, ensuring that campaigns and journeys are thoroughly reviewed and approved by the appropriate stakeholders before going live. This feature is available in Limited Availability. [Learn more](../test-approve/gs-approval.md)

Once your campaign has been configured, you need to review its parameter and content before activating it. To do this, follow these steps:

1. In the campaign configuration screen, click **[!UICONTROL Review to activate]** to display a summary of the campaign.

    The summary allows you to modify your campaign if necessary, and to check if any parameter is incorrect or missing.

    >[!IMPORTANT]
    >
    >In case of errors, you cannot activate the campaign. Resolve the errors before proceeding.

    ![](assets/create-campaign-alerts.png)

1. Check that your campaign is correctly configured, then click **[!UICONTROL Activate]**.

1. The campaign is now activated. Its status is **[!UICONTROL Live]**, or **[!UICONTROL Scheduled]** if you entered a start date. [Learn more on campaigns statuses](get-started-with-campaigns.md#statuses). 
    
    The message configured in the campaign is sent immediately or on the specified date.

    >[!NOTE]
    >
    >The **[!UICONTROL Completed]** status is automatically assigned to a campaign 3 days after it has been activated or at the campaign's end date if it has a recurring execution.
    >
    >If no end date has been specified, the campaign will keep the **[!UICONTROL Live]** status. To change it, you need to stop the campaign manually. [Learn how to stop a campaign](modify-stop-campaign.md) 

1. Once a campaign has been activated, you can check at any time its information by opening it. The summary allows you to get statistics about number of targeted profiles and delivered and failed actions.

    You can also get additional statistics in dedicated reports by clicking the **[!UICONTROL Reports]** button. [Learn more](../reports/campaign-global-report-cja.md)

    ![](assets/create-campaign-summary.png)
