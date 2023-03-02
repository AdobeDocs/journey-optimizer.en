---
solution: Journey Optimizer
product: journey optimizer
title: Work with AEM templates
description: Learn how to create templates in AEM and export them into Journey Optimizer
hide: yes
hidefromtoc: yes
feature: Overview
topic: Content Management
role: User
level: Beginner
badge: label="Beta" type="Informative"
hide: yes
hidefromtoc: yes
---
# Work with Adobe Experience Manager templates {#aem-templates}

>[!AVAILABILITY]
>
>Integration with Adobe Experience Manager is currently available as a beta to select users only.
> As a beta user, use [this form](https://forms.office.com/pages/responsepage.aspx?id=Wht7-jR7h0OUrtLBeN7O4Wf0cbVTQ3tCpW_unE-w8-JUN1FaNlAzNkhPSUdaSkJXVFRCNTRJNVRFSy4u){target="_blank"} to share feedback.

With Adobe Journey Optimizer, you can create custom-tailored messages through Adobe Experience Manager sites. Start by designing your templates using Adobe Experience Manager's content sources, then send them to Adobe Journey Optimizer. Once shared, these templates can be accessed in Adobe Journey Optimizer's email designer, simplifying the process of crafting and sending messages to your desired audience.

## Prerequisites {#prerequisites}

Before starting using this capability, make sure you are aligned with the following requirements:

* **Experience Manager settings**

    This capability is available starting Adobe Experience Manager 6.5.14. You must connect to Adobe Experience Manager Sites on your Managed Services Author environment.

    As a part of the beta program, the Cloud Service configuration was performed by Adobe in Adobe Experience Manager to connect to Adobe Journey Optimizer. 

* **Permissions**

    To create, edit and delete content templates in Adobe Journey Optimizer, you must have the **[!DNL Manage Library Items]** permission included in the **[!DNL Content Library Manager]** product profile. [Learn more](../administration/ootb-product-profiles.md#content-library-manager)


## Guardrails and limitations{#aem-templates-limitations}

To further optimize your use of Adobe Experience Manager with Adobe Journey Optimizer, it's important to be aware of the following additional guardrails and limitations:

* The Experience Manager template must not contain personalization. Personalization should only be performed in Journey Optimizer.

* Bulk template export is not currently supported, templates must be exported individually.

* Syncing between Experience Manager and Journey Optimizer is currently not available. If changes are made to an Experience Manager template after it has been sent to Journey Optimizer, the user will need to re-export the template and re-send it to Journey Optimizer.

## Send a template to Journey Optimizer{#aem-templates-send}

To export an Adobe Experience Manager template to Adobe Journey Optimizer, follow the steps below:

1. From your Adobe Experience Manager homepage, select the **[!UICONTROL Outbound Marketing]**.

    ![](assets/aem-outbound-menu.png)

1. Access your content library and select the template you want to export to Journey Optimizer.

    You can also create a new page from scratch. [Learn more](https://experienceleague.adobe.com/docs/experience-manager-65/authoring/authoring/managing-pages.html?lang=en#creating-a-new-page)

    ![](assets/aem-send-template.png)

1. After selecting your template, select **[!UICONTROL Send to]** from the advanced menu. 

    ![](assets/aem-advanced-menu.png)

1. Enter the **[!UICONTROL Name]** of the Content template and select the target **[!UICONTROL Sandbox]**.

    ![](assets/aem-send-template-settings.png)
    
1. After you have clicked the **[!UICONTROL Send]** button, the export process will begin. Once the export is complete, you will see the following message in the user interface: "Template "XX" sent successfully to AJO".

The template is added to Adobe Journey Optimizer content templates of the selected sandbox.

## Use and personalize an Adobe Experience Manager template{#aem-templates-perso}

Once the Experience Manager template is available in Journey Optimizer as a content template, you can identify and incorporate the necessary content for the email, including personalization.

1. In Journey Optimizer, from the **[!UICONTROL Content template]** menu, access your imported template.

    ![](assets/aem_ajo_1.png)

1. By clicking the **[!UICONTROL Alert]** button, you can quickly check if any important settings are missing. This will help ensure that your messages are properly configured and prevent any potential errors or issues.

    ![](assets/aem_ajo_2.png)

1. In the Template properties window, click the **[!UICONTROL Manage access]** button to assign custom or core data usage labels to your template. [Learn more on Object Level Access Control (OLAC)](../administration/object-based-access.md)

1. To further personalize your AEM template and add custom personalization to your content, click **[!UICONTROL Edit content]**. This will allow you to easily make changes and tailor the template to your specific needs. [Learn more](get-started-email-design.md)

    >[!NOTE]
    >
    > If you want to edit and personalize your template, you will only be able to use the compatibility mode. 

1. When your content template is ready, [test and validate it](content-templates.md#test-template).

1. Once your content has been defined, you can use it when creating new email by browsing the **[!UICONTROL Saved templates]** collection. Then, select **[!UICONTROL Use this template]**.

    Learn how to edit and personalize an email content in [this section](content-from-scratch.md).

    ![](assets/aem_ajo_3.png)

When your email is ready, complete the configuration of your [journey](../building-journeys/journey-gs.md) or [campaign](../campaigns/create-campaign.md), and activate it to send the message.