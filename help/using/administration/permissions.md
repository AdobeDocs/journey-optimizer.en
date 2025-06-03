---
solution: Journey Optimizer
product: journey optimizer
title: Manage users and roles
description: Learn how to manage users and roles
exl-id: 85fd386a-45fa-4f9a-89d1-cecc0749b90d
feature: Access Management
topic: Administration
role: Admin
level: Intermediate
keywords: product, profiles, sandbox
---
# Manage users & roles {#manage-permissions}

**[!UICONTROL Roles]** refer to a collection of users who share the same permissions and sandboxes. These roles allow you to easily manage access and permissions for different groups of users within your organization.

With the [!DNL Journey Optimizer] product, you can choose from a range of pre-existing **[!UICONTROL Roles]**, each with varying levels of permissions, to assign to your users. For more information on the available **[!UICONTROL Roles]**, refer to this [page](ootb-product-profiles.md).

When a user belongs to a **[!UICONTROL Role]**, they gain access to the Adobe apps and services contained within the product.

If the pre-existing roles do not meet your organization's specific needs, you can also create custom **[!UICONTROL Roles]** to fine-tune access to certain functionalities or objects in the interface. This way, you ensure that each user has access to only the resources and tools they require to perform their tasks efficiently.


>[!IMPORTANT]
>
>Steps and procedures detailed below can only be carried out by a **[!UICONTROL Product]** or **[!UICONTROL System]** administrator.


## Assign a role {#assigning-role}

You can assign an out-of-the-box or custom **[!UICONTROL Role]** to your users.

The list of all out-of-the-box roles with assigned permissions is available in the [Built-in roles](ootb-product-profiles.md) section.

To assign a **[!UICONTROL Role]**:

1. To assign a role to a user in the [!DNL Permissions] product, navigate to the **[!UICONTROL Roles]** tab and select the desired role.

    ![](assets/do-not-localize/access_control_2.png)

1. From the **[!UICONTROL Users]** tab, click **[!UICONTROL Add user]**.

    ![](assets/do-not-localize/access_control_3.png)

1. Type in your user's name or email address or select the user from the list, and click **[!UICONTROL Save]**.

   If the user was not previously created in the [!DNL Admin Console], refer to the [Add users documentation](https://experienceleague.adobe.com/docs/experience-platform/access-control/ui/users.html){target="_blank"}.

    ![](assets/do-not-localize/access_control_4.png)

Your user receives an email redirecting them to your instance.

For more information on user management, refer to the [Access control documentation](https://experienceleague.adobe.com/docs/experience-platform/access-control/home.html){target="_blank"}.

When accessing the instance, your user sees a specific view depending on the assigned permissions in the **[!UICONTROL Role]**. If the user does not have the right access to a feature, the following message appears: 

`You don't have permission to access this feature. Permission needed: XX.`

## Edit an existing role {#edit-product-profile}

For built-in or custom **[!UICONTROL Roles]**, you can decide at any time to add or delete permissions.

In the example below, we want to add **[!UICONTROL Permissions]** related to the **[!UICONTROL Journeys]** resource for users assigned to the Journey viewer **[!UICONTROL Role]**. The users will then be able to publish journeys.

>[!IMPORTANT]
>
>Changes made to a built-in or custom role will affect all users assigned to that role.

1. To edit a role in the [!DNL Permissions] product, navigate to the **[!UICONTROL Roles]** tab and select the desired role, here the Journey viewer **[!UICONTROL Role]**.
    ![](assets/do-not-localize/access_control_5.png)

1. From your **[!UICONTROL Role]** dashboard, click **[!UICONTROL Edit]**.

    ![](assets/do-not-localize/access_control_6.png)

1. The **[!UICONTROL Resources]** menu displays the list of resources that apply to the **[!UICONTROL Experience Cloud - Platform powered applications]** product. Drag and drop resources to assign permissions.

    From the **[!UICONTROL Journeys]** resource drop-down, we choose here the Publish journey **[!UICONTROL Permission]**.

    ![](assets/do-not-localize/access_control_14.png)

1. If needed, under **[!UICONTROL Included Permission Items]**, click the X icon to remove permissions or resources from your role.

1. When finished, click **[!UICONTROL Save]**.

If needed, you can also create a new role with specific permissions.

## Create a new role {#create-product-profile}

[!DNL Journey Optimizer] allows you to create your own **[!UICONTROL Roles]** and assign a set of permissions and sandboxes to your users. With **[!UICONTROL Roles]**, you can authorize or deny access to certain functionalities or objects in the interface.

For more information on how to create and manage sandboxes, refer to [Adobe Experience Platform documentation](https://experienceleague.adobe.com/docs/experience-platform/sandbox/ui/user-guide.html){target="_blank"}.

In this example, we create a role named **Journeys read-only**, where we grant read-only rights to the Journey feature. Users will only be able to access and view journeys and will not be able to access other features such as **[!DNL Decision management]** in [!DNL Journey Optimizer].

To create our **Journeys read-only** **[!UICONTROL Role]**:

1. To assign a role to a user in the [!DNL Permissions] product, navigate to the **[!UICONTROL Roles]** tab and click **[!UICONTROL Create role]**.

    ![](assets/do-not-localize/access_control_9.png)

1. Add a **[!UICONTROL Name]** and **[!UICONTROL Description]** for your new **[!UICONTROL Role]**. Then, click **[!UICONTROL Confirm]**.

    ![](assets/do-not-localize/access_control_10.png)

1. From the **[!UICONTROL Sandbox]** resource drop-down, choose which sandbox(es) to assign to your **[!UICONTROL Role]**. [Learn more about sandboxes](sandboxes.md).

    ![](assets/do-not-localize/access_control_13.png)

1. Select from the different resources such as **[!DNL Journeys]**, **[!DNL Segments]**, or **[!DNL Decision management]** available in [!DNL Journey Optimizer] listed in the left-hand menu. 

    Here we select the **[!UICONTROL Journeys]** resource.

    ![](assets/do-not-localize/access_control_11.png)

1. From the **[!UICONTROL Journeys]** drop-down, select the permissions to assign to your **[!UICONTROL Role]**.

    Here we select **[!DNL View journeys]**, **[!DNL View journeys report]**  and **[!DNL View journeys event, data sources, actions]**.

    ![](assets/do-not-localize/access_control_12.png)

1. When finished, click **[!UICONTROL Save]**.

Your **[!UICONTROL Role]** is now created and configured. You now need to assign it to users.

For more information on role creation and management, refer to the [Adobe Admin Console documentation](https://experienceleague.adobe.com/docs/experience-platform/access-control/abac/permissions-ui/roles.html){target="_blank"}.
