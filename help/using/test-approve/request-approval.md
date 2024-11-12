---
title: Request approval
description: Learn how to request approval before publishing your journeys & campaigns.
role: User
level: Beginner
feature: Approval
exl-id: 75dafecd-805d-4aa2-86c6-99e6da4d378b
---
# Request approval {#request-approval}

Access to the approval workflow is determined by your specific use case:

* **No active Approval policy exists**

    * **Campaigns**: If no approval policy is active for the Campaign object in a sandbox, campaigns will show the **[!UICONTROL Activate]** button, allowing you to activate them without needing approval.

    * **Journeys**: If no approval policy is active for the Journey object, journeys will display the **[!UICONTROL Publish]** button, allowing you to publish directly.

* **Active Approval policies exist**

    * **Campaigns**: If one or more active approval policies exist for the Campaign object in a sandbox, all campaigns in said sandbox will display the **[!UICONTROL Request Approval]** button. 
    If no approval policy applies to the selected object when the **[!UICONTROL Request Approval]** button is clicked, the auto-approval workflow will be triggered.

    * **Journeys**: If one or more active approval policies exist for the Journey object in a sandbox, all journeys will display the **[!UICONTROL Request Approval]** button. 
    If no approval policy applies to the selected object when the **[!UICONTROL Request Approval]** button is clicked, the auto-approval workflow will be triggered.

## Send Approval request

After creating your campaign or journey, click the **[!UICONTROL Request Approval]** button. This will check if there is an active approval policy in your sandbox that applies to the campaign or journey.

* If an applicable approval policy is found, your campaign or journey will be sent for review.

* If no approval policy is applicable to the campaign or journey after clicking the **[!UICONTROL Request Approval]** button, the campaign or journey will be automatically approved and either activated or published.

The **[!UICONTROL Request approval]** pane opens. Provide a message for the approver(s) if necessary and click **[!UICONTROL Send]** to submit your request.

![](assets/approval-request.png)

While the campaign or journey is **[!UICONTROL In review]** state, you have the option to cancel the approval request. By clicking the **[!UICONTROL Cancel request]** button, the campaign or journey will return to the draft stage, and a notification will be sent to the reviewers informing them that the request has been cancelled. You can then make the necessary edits and resubmit the campaign or journey for approval.

![](assets/approval-cancel.png)

## Manage Approval requests 

Once that the approval request has been sent to the approvers, they can review it and either activate the journey/campaign to make it live, or request changes if necessary. [Learn how to review & approve a request](review-approve-request.md)

If the approvers request changes, you are notified through an email and a Journey Optimizer alert, which is accessible when clicking the bell icon on top right of the screen, in the **[!UICONTROL Requests]** tab.

![](assets/changes-requested.png)

To go through the change request, open it from the email or the alert to access the journey or campaign and make the requested changes. When your journey/campaign is ready to be reviewed again, send a new approval request using the **[!UICONTROL Request approval]** button.
