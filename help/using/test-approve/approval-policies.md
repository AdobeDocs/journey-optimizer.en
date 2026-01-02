---
title: Create & manage approval policies
description: Learn how create and manage approval policies.
role: User
level: Beginner
feature: Approval
exl-id: e518cb3c-f361-43a4-b9a5-ec070c612e75
---
# Create & manage approval policies {#approval-policies}

>[!CONTEXTUALHELP]
>id="ajo_approval_policy_request_approval"
>title="Request approval"
>abstract="Request approval"

>[!CONTEXTUALHELP]
>id="ajo_approval_policy_request_change"
>title="Request change"
>abstract="Request change"

>[!NOTE]
>
>To create approval policies, you must have system or product administrator privileges in Adobe Experience Platform. [Learn more](https://experienceleague.adobe.com/en/docs/experience-platform/access-control/home)

Approval policies allow administrators to establish a validation process for journeys and campaigns. This system outlines specific conditions that determine whether a journey or campaign requires approval. These policies can vary in complexity. They can simply require all campaigns to be reviewed by a particular user or team, or establish criteria based on who created the campaign.

You can target approval policies using flexible criteria such as tags, campaign/journey names, channel types, or requestor information. For example, you can require approval for all objects tagged with "high-risk", or for any campaign matching a specific naming pattern.

## Create approval policies {#create-policies}

>[!CONTEXTUALHELP]
>id="ajo_permissions_approval_policy"
>title="New approval policy"
>abstract="In this screen, enter the name and select the context for the approval policy, then build the conditions to determine who can initiate the approval request and who can validate it."

To create an approval policy, follow these steps:

1. From the **[!UICONTROL Administration]** menu in [!DNL Journey Optimizer], access **[!UICONTROL Permissions]** then **[!UICONTROL Policies]**.

    ![Create approval policy button in Permissions menu](assets/policy_create_1.png)

1. Click **[!UICONTROL Create]** in the **[!UICONTROL Approval Policy]** tab, choose **[!UICONTROL Approval Policy]**, and click **[!UICONTROL Confirm]**.

1. Enter a **[!UICONTROL Name]** and **[!UICONTROL Description]** for the policy.

1. Select whether the policy will apply to **[!UICONTROL Journeys]** or **[!UICONTROL Campaigns]**.

<!--
1. Enable the **[!UICONTROL Block self-approval]** to prevent Journey/Campaign creators from approving their own objects.

    ![](assets/policy_create_2.png)
-->

You can now refine the conditions to specify who can initiate the approval request and who can validate it.

## Set conditions for approval policies {#conditions}

Approval policies offer flexible targeting options to match your governance needs. You can create approval policies based on various criteria, including:

* **Campaign/Journey names**: Target specific objects by name
* **Tags**: Apply policies to all campaigns or journeys with a specific tag
* **Channel types**: Require approval for specific actions (email, SMS, push, etc.)
* **Campaign types**: Set different rules for [Action vs. API-triggered campaigns](../campaigns/get-started-with-campaigns.md#campaign-types)
* **Requestors**: Define policies based on who creates the campaign or journey

To define the conditions associated to an approval policy, follow these steps:

1. Access your **[!UICONTROL Approval policy]**.

1. Under the **[!UICONTROL If]** menu, click **[!UICONTROL Add condition]** to define which object or user will trigger an approval request.

1. Choose the appropriate **[!UICONTROL Category]**, **[!UICONTROL Matching Rule]**, and **[!UICONTROL Options]**.

    For example, "if Action matches any Direct Mail" or "If Requestor Username matches John Doe."
  
    ![Approval policy condition builder interface](assets/policy_condition_1.png)

    +++ Learn more about available categories and options
    <table>
    <tr>
      <th>Category</th>
      <th>Option</th>
    </tr>
    <tr>
      <td rowspan="3">Campaign type</td>
      <td>Scheduled (Marketing)</td>
    </tr>
    <tr>
    <td>API-triggered (Marketing)</td>
    </tr>
    <tr>
    <td>API-triggered (Transactional)</td>
    </tr>
    <tr>
    <td rowspan="8">Action</td>
    <td>In-app</td>
    </tr>
    <tr>
    <td>Push notification</td>
   </tr>
    <tr>
    <td>SMS</td>
    </tr>
    <tr>
    <td>Email</td>
    </tr>
    <tr>
    <td>Direct mail</td>
    </tr>
    <tr>
    <td>Web</td>
    </tr>
    <tr>
    <td>Code-based</td>
    </tr>
    <tr>
    <td>Content card</td>
    </tr>
    <tr>
    <td>Tags</td>
    <td>Name of the tag used to organize your audiences. </td>
    </tr>
    <tr>
    <td>Object name</td>
    <td>Name of your object.</td>
    </tr>
    <tr>
    <td>Requestor username</td>
    <td>Name and email address of designated requestor</td>
    </tr>
    <tr>
    <td>Requestor user group</td>
    <td>Name of the user group of designated requestors</td>
    </tr>
    </table>

1. To add more criteria, click **[!UICONTROL Add condition]** to define additional rules and select either **[!UICONTROL And]** or **[!UICONTROL Or]** to specify how the conditions are connected.

1. Under the **[!UICONTROL Then, send approval request to]** menu, click **[!UICONTROL Add condition]** to define which user can accept the approval request.

1. From the **[!UICONTROL Category]** drop-down, select whether you want to choose a User Group or an individual User.

1. Then, from the **[!UICONTROL Option]** drop-down, select the specific user group or user.

    The selected user or user group will be responsible for validating the approval request.

    ![Approval request recipient selection interface](assets/policy_condition_2.png)

1. To add more criteria, click **[!UICONTROL Add condition]** to define additional rules and select either **[!UICONTROL And]** or **[!UICONTROL Or]** to specify how the conditions are connected.

1. Once your policy is fully configured, click **[!UICONTROL Save]**.

You can now activate your approval policy to apply it.

## Activate and manage approval policies {#activate-policies}

To apply your approval policy, you must activate it. To perform this, follow these steps:

1. Access your **[!UICONTROL Approval policy]**.

1. Then, click **[!UICONTROL Activate]** to apply the configured conditions to your environment.

    >[!NOTE]
    >
    >Once activated, policies cannot be edited. To modify conditions, deactivate the policy first.

    ![Activate approval policy button](assets/policy_activate_1.png)

1. From the **[!UICONTROL Policy]** menu, open the advanced options to **[!UICONTROL Edit]**, **[!UICONTROL Deactivate]**, or **[!UICONTROL Duplicate]** the policy as needed.

    ![Approval policy management options menu](assets/policy_activate_2.png)
