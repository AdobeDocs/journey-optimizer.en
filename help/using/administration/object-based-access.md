---
solution: Journey Optimizer
product: journey optimizer
title: Object level access control
description: Learn about Object level access control that lets you define authorizations to manage data access to a selection of objects
feature: Access Management
topic: Administration
role: Admin, Developer, Architect
level: Experienced
keywords: object, level, access, control, labels, olac, authorization
exl-id: 02ccdd95-426c-4b61-9834-7f2dcd5abdbb
---
# Object level access control {#object-level-access}

>[!CONTEXTUALHELP]
>id="ajo_olac_manage_access"
>title="Object level access control"
>abstract="To maintain access to this object, only apply labels you have permission for."

Object level access control (OLAC) lets you define authorizations to manage data access to a selection of objects:

* Journey
* Campaign
* Template
* Fragment
* Landing page
* Offer
* Static offer collection
* Offer decision
* Channel surface
* IP warmup plan

Its purpose is to protect sensitive digital assets from unauthorized users allowing further protection of personal data. 

In Adobe Journey Optimizer, OLAC allows you to protect data and grant specific access to specific objects.

## Create labels {#create-assign-labels}

>[!IMPORTANT]
>
>To be able to create labels, you must be part of a role with the **[!UICONTROL Manage usage labels]** permission.

**[!UICONTROL Labels]** allow you to categorize datasets and fields according to usage policies that apply to that data. **[!UICONTROL Labels]** can be applied at any time, providing flexibility in how you choose to govern data. 

You can create labels in the [!DNL Permissions] product. For more on this, refer to [this page](https://experienceleague.adobe.com/docs/experience-platform/access-control/abac/permissions-ui/labels.html). 

**[!UICONTROL Labels]** can also be created directly in Journey Optimizer:

1. From an Adobe Journey Optimizer object, here a newly created **[!UICONTROL Campaign]**, click the **[!UICONTROL Manage access]** button.

    ![](assets/olac_1.png)

1. From the **[!UICONTROL Manage access]** window, click **[!UICONTROL Create label]**.

    ![](assets/olac_2.png)

1. Configure your label, you must specify:
    * **[!UICONTROL Name]**
    * **[!UICONTROL Friendly name]**
    * **[!UICONTROL Description]**

    ![](assets/olac_3.png)

1. Click **[!UICONTROL Create]** to save your **[!UICONTROL Label]**.

Your newly created **[!UICONTROL Label]** is now available in the list. If needed, you can modify it in the [!DNL Permissions] product.

## Assign labels {#assign-labels}

>[!IMPORTANT]
>
>To be able to assign labels, you must be a part of a role with a Manage permission i.e., [!DNL Manage journeys], [!DNL Manage Campaigns] or [!DNL Manage decisions]. Without this permission, the **[!UICONTROL Manage access]** button will be greyed out.

To assign custom or core data usage labels to your Journey Optimizer objects: 

1. From an Adobe Journey Optimizer object, here a newly created **[!UICONTROL Campaign]**, click the **[!UICONTROL Manage access]** button.

    ![](assets/olac_1.png)

1. From the **[!UICONTROL Manage access]** window, select your custom or core data usage label(s) to manage access to this object. 

    For more information on core data usage labels, refer to [this page](https://experienceleague.adobe.com/docs/experience-platform/data-governance/labels/reference.html).

    ![](assets/olac_4.png)

1. Click **[!UICONTROL Save]** to apply this label restriction. 

To have access to this object, users will need to have the specific **[!UICONTROL Label]** included to their **[!UICONTROL Roles]**. 
For example, a user with the C1 label will only have access to C1 labeled or unlabeled objects.

For more information on how to assign **[!UICONTROL Label]** to a **[!UICONTROL Role]**, refer to [this page](https://experienceleague.adobe.com/docs/experience-platform/access-control/abac/permissions-ui/permissions.html#manage-labels-for-a-role).