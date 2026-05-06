---
solution: Journey Optimizer
product: journey optimizer
title: Configure AEM Repository Settings
description: Learn how admins configure AEM repositories, custom domains, authenticated publish, and author-only Content Fragment access in Journey Optimizer.
feature: Integrations
topic: Administration
role: Admin
level: Experienced
keywords: AEM, Content Fragments, administration, repository, authentication, author, publish
---
# Configure Adobe Experience Manager repository access {#aem-admin-settings}

Adobe Journey Optimizer integrates with **[!DNL Adobe Experience Manager as a Cloud Service]** to support **Content Fragments** in Journeys and Campaigns. **[!UICONTROL AEM integration]**, in **[!UICONTROL Administration]** > **[!UICONTROL Channels]**, holds per-sandbox repository settings for domains, authentication, and author–publish topology, and applies to the Content Fragment selector and **Adobe Experience Manager Content Advisor**.

➡️For authoring steps after repository configuration, see [Work with Experience Manager Content Fragments](../integrations/aem-fragments.md).

## Configure repositories in the UI {#configure-ui}

>[!NOTE]
>
> Configuration is **per sandbox**. 

Saving a new configuration for the same org, sandbox, and repo **replaces** the previous record. 

1. Access **[!UICONTROL Administration]** > **[!UICONTROL Channels]** > **[!UICONTROL AEM Integration]**.

1. Click Create integration.

1. Choose which repository to configure and click Next.

    Click View to access this repository.

    >[!IMPORTANT]
    >
    >Saving a new configuration for the same organization, sandbox, and repository **replaces** the default configuration, i.e **publish** repository. 

1. Enter a Name and Description.

1. Choose your setup:    

    * Author only setup
        Enabling this option pulls content from the author instance only and disables publish instance config. Replication will not be supported and live updates will not be supported.

    * Publish instance setup
        
        1. Enable the **[!UICONTROL Send token to publish instance]** option so service Credentials are sent to authenticate requests to the publish instance. 
        
        1. You can then provide a valid Service Credential JSON.

        1. If needed, you can provide a custom domain if publish-p16552-e147195.adobeaemcloud.comis blocked from fetching content for your org

1. Click **[!UICONTROL Validate]**.

Authors in that sandbox then use the configured repository when they open the Content Fragment selector or Content Advisor. They do not edit these admin fields themselves.
