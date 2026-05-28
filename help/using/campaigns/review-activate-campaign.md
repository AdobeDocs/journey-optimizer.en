---
solution: Journey Optimizer
product: journey optimizer
title: Review and activate an Action campaign
description: Learn how to review and activate Action campaigns in [!DNL Journey Optimizer].
feature: Campaigns
topic: Content Management
role: User
level: Intermediate
keywords: campaign, review, validation, activation, activating, optimizer
exl-id: 7c4afc98-0d79-4e26-90f8-558bac037169
TQID: https://experienceleague.adobe.com/BKGXccq-kwZJA-cZ4SAyf3zJBIvyJnr5V01xmbQgwmo
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: d556b755-390a-43f0-be32-a08cf6236126
    internal-label: Configuration
  - id: a653cc2e-bc85-4353-a306-399e5b247978
    internal-label: Journey Optimizer campaigns
subfeature_v2:
  - id: f7479fa1-474b-479d-8c98-f6cee5865a38
    internal-label: API triggered campaigns
  - id: ee67bd4a-25ee-4cdd-9eab-0d7549fde0c6
    internal-label: Campaign management
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
level_v2:
  - id: b5a62a22-46f7-4f0d-b151-3fc640bef588
    internal-label: Intermediate
topic_v2:
  - id: aa2f3246-cb95-4b30-8899-fdf7d73550cc
    internal-label: Reporting
---
# Review and activate the Action campaign {#action-campaign-review}

Once your Action campaign has been configured, you need to review its parameter and content before activating it. To do this, follow the steps below.

>[!IMPORTANT]
>
> If your campaign is subject to an approval policy, you need to request approval in order to be able to send your campaign. [Learn more](../test-approve/gs-approval.md)

1. In the campaign configuration screen, click **[!UICONTROL Review to activate]** to display a summary of the campaign.

    ![](assets/campaign-review.png)

1. A summary of the campaign configuration displays, allowing you to check if any parameter is incorrect or missing and to modify your campaign if necessary.

    In case of errors, you cannot activate the campaign. Resolve the errors before proceeding.

    ![](assets/create-campaign-alerts.png)

1. When a campaign uses [decision policies](../experience-decisioning/decisioning-policies.md) in its content, you can review each policy's structure and copy technical details directly from the campaign summary. [Learn how](../experience-decisioning/use-decision-policy.md#decision-policy-summary)

1. Check that your campaign is correctly configured, then click **[!UICONTROL Activate]**.

1. The campaign is activated. Its status is **[!UICONTROL Live]**, or **[!UICONTROL Scheduled]** if you entered a start date. The message configured in the campaign is sent immediately or on the specified date. 

    The **[!UICONTROL Completed]** status is automatically assigned to the campaign 3 days after it has been activated or at the campaign's end date if it has a recurring execution. [Learn more about campaigns statuses](manage-campaigns.md#statuses).

    If no end date has been specified, the campaign keeps the **[!UICONTROL Live]** status. To change it, you need to stop the campaign manually. [Learn how to stop a campaign](manage-campaigns.md) 

1. Once a campaign has been activated, you can check at any time its information by opening it. The summary allows you to get statistics about number of targeted profiles and delivered and failed actions.

    You can also get additional statistics in dedicated reports by clicking the **[!UICONTROL Reports]** button. [Learn more](../reports/campaign-global-report-cja.md)

    ![](assets/create-campaign-summary.png)
