---
solution: Journey Optimizer
product: journey optimizer
title: Configure AEM Repository Settings
description: Learn how admins configure AEM repositories, custom domains, authenticated publish, and author-only Content Fragment access in Journey Optimizer.
feature: Integrations
topic: Administration
role: Admin
level: Experienced
hide: true
keywords: AEM, Content Fragments, administration, repository, authentication, author, publish
---
# Configure Adobe Experience Manager repository access {#aem-admin-settings}

Adobe Journey Optimizer integrates with **[!DNL Adobe Experience Manager as a Cloud Service]** so you can use **Content Fragments** in Journeys and Campaigns. **Content Fragments** are read from the Adobe Experience Manager publish repository by default, administrators can switch to author-only or adjust publish access in the **[!UICONTROL AEM Integration]** menu.

➡️ When the repository is configured, continue with [Work with Experience Manager Content Fragments](../integrations/aem-fragments.md) for authoring and selection tasks in Journey Optimizer.

## Configure repositories {#configure-ui}

>[!NOTE]
>
> **[!UICONTROL AEM Integration]** saves repository settings **per sandbox**. Each sandbox keeps its own integrations and they do not apply across sandboxes.
  
Journey Optimizer stores one integration per organization, sandbox, and Adobe Experience Manager repository. If you save a new integration for that same combination, it replaces the previous settings, only the latest configuration is kept.

To configure your repository:

1. Access **[!UICONTROL Administration]** > **[!UICONTROL Channels]** > **[!UICONTROL AEM Integration]**.

1. Click **[!UICONTROL Create integration]**.

   ![](assets/aem-admin-settings-1.png)

1. Choose which repository to configure and click **[!UICONTROL Next]**.

    Additionally, you can click **[!UICONTROL View]** to access this repository.

    >[!IMPORTANT]
    >
    >Saving a new configuration for the same organization, sandbox, and repository **replaces** the default configuration, i.e **publish** repository. 

   ![](assets/aem-admin-settings-2.png)

1. Enter a **[!UICONTROL Name]** and **[!UICONTROL Description]**.

1. Choose your setup:

    +++ Author only setup

    Select **[!UICONTROL Author only setup]** when Journey Optimizer should read Content Fragments from the Adobe Experience Manager **author** environment only. Replication from author to publish and live publish updates are not supported.

    ![](assets/aem-admin-settings-3.png)
    
    +++

    +++ Publish instance setup

    1. Select **[!UICONTROL Publish instance setup]** to turn on publish instance settings.
        
        ![](assets/aem-admin-settings-4.png)

    1. Optionally enable **[!UICONTROL Send token to publish instance]** so service credentials are included with requests to the publish instance.

    1. Paste a valid **[!UICONTROL Service Credential JSON]** for authentication.

    1. Optionally provide a custom domain if your organization cannot reach the default AEM publish host (`publish-XX-XX.adobeaemcloud.com`) to fetch content.

        ![](assets/aem-admin-settings-5.png)

    +++

1. Click **[!UICONTROL Save]**.

1. To edit or disable this repository integration, access your previously created configuration from the **[!UICONTROL AEM Integration]** menu.

When you save, that sandbox uses the repository for the Content Fragment selector and **Adobe Experience Manager Content Advisor**.

