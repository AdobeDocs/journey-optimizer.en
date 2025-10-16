---
solution: Journey Optimizer
product: journey optimizer
title: Use and assign sandboxes
description: Learn how to manage sandboxes
feature: Sandboxes
topic: Administration
role: Admin, Architect, Developer
level: Experienced
keywords: sandboxes, virtual, environments, organization, platform
exl-id: 14f80d5d-0840-4b79-9922-6d557a7e1247
---
# Use and assign sandboxes {#sandboxes}

## Use sandboxes {#using-sandbox}

[!DNL Journey Optimizer] allows you to partition your instance into separate virtual environments called sandboxes. Sandboxes are assigned through roles in Permissions. [Learn how to assign sandboxes](permissions.md#create-product-profile).

[!DNL Journey Optimizer] reflects Adobe Experience Platform sandboxes created for a given organization. Adobe Experience Platform sandboxes can be created or reset from your Adobe Experience Platform instance. [Learn more in the Sandbox user guide](https://experienceleague.adobe.com/docs/experience-platform/sandbox/ui/user-guide.html){target="_blank"}.

You can find the sandbox switcher control at the top-right of your screen, next to your organization's name. To switch from one sandbox to another, click the currently active sandbox in the switcher and select another sandbox from the drop-down list.

![](assets/sandbox_5.png)

➡️ [Learn more about sandboxes in this video](#video)

## Assign sandboxes {#assign-sandboxes}

>[!IMPORTANT]
>
> Sandbox management can only be carried out by a **[!UICONTROL Product]** or **[!UICONTROL System]** administrator.

You can choose to assign different sandboxes to out-of-the-box or custom **[!UICONTROL Roles]**.

To assign sandboxes:

1. In [!DNL Permissions], from the **[!UICONTROL Roles]** tab, select a **[!UICONTROL Role]**.
    
    ![](assets/sandbox_1.png)

1. Click **[!UICONTROL Edit]**.

1. From the **[!UICONTROL Sandboxes]** resource drop-down, select the sandbox which will be assigned to your role.

    ![](assets/sandbox_3.png)

1. If needed, click the X icon next to it to remove sandbox access from your **[!UICONTROL Role]**.

    ![](assets/sandbox_4.png)

1. Click **[!UICONTROL Save]**.

## Access to Content {#content-access}

To configure content accessibility, assign a content shared folder to each of your sandboxes. You can create and configure shared folders in the **[!UICONTROL Storage]** tab displayed in the [!DNL Admin Console] for administrators. If you have access to the [!DNL Admin Console] as a system administrator, you can create shared folders and add delegates with different access levels to your shared folders.

![](assets/do-not-localize/content_access.png)

Note that for your content to sync with the correct sandbox, you must follow the same syntax as the sandbox. For example, if your sandbox is called "development," your shared folder should have the same name.

[Learn how to manage shared folders](https://helpx.adobe.com/enterprise/admin-guide.html/enterprise/using/manage-adobe-storage.ug.html){target="_blank"}.

## How-to video{#video}

Understand what sandboxes are and how to distinguish between development and production sandboxes. Learn how to create, reset, and delete sandboxes.

>[!VIDEO](https://video.tv.adobe.com/v/334355?quality=12)