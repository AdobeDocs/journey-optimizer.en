---
solution: Journey Optimizer
product: journey optimizer
title: Set up web 
description: Learn how to configure and monitor web configurations
feature: Surface, Channel Configuration
topic: Administration
role: Admin
level: Experienced
keywords: channel, surface, technical, parameters, optimizer
hide: yes
hidefromtoc: yes
---
# Set up web configuration {#set-mobile-web}

>[!CONTEXTUALHELP]
>id="ajo_mobile_web_setup_javascript_code"
>title="Javascript code"
>abstract="TBC"

>[!CONTEXTUALHELP]
>id="ajo_mobile_web_setup_javascript_site"
>title="Launch site and validate"
>abstract="TBC"

This set up facilitates the expeditious configuration of marketing channels, ensuring all required resources are readily available within Experience Platform, Journey Optimizer, and Data Collection. This enables your marketing team to immediately start with campaign and journey creation.

## Create a new Web set up {#new-setup}

1. From Journey Optimizer homepage, click **[!UICONTROL Begin]** from the **[!UICONTROL Set up mobile and web channels]** card.

    ![](assets/guided-setup-config-1.png)

1. Create a **[!UICONTROL New]** configuration.

    If you already have existing configurations, you can choose to select one, or create a new configuration.

    ![](assets/guided-setup-config-2.png)

1. Enter a **[!UICONTROL Name]** for your new configuration and select or create your **[!UICONTROL Datastream]**. This **[!UICONTROL Name]** will be used for every auto-created resources.

1. If your organization has multiple datastreams, please select one from the existing options. If you do not have a Datastream, one will be auto-created for you.

1. Select the Web platform and click **[!UICONTROL Auto-create resources]**.

    ![](assets/guided-setup-config-5.png)

1. To streamline the setup process, the necessary resources are automatically created to help you get started.

    Below is a comprehensive list of all the resources that are auto generated:

    +++ Created resources

    <table>
    <thead>
    <tr>
    <th><strong>Solution</strong></th>
    <th><strong>Auto-created resources</strong></th>
    </tr>
    </thead>
    <tbody>
    <tr>
    </tr>
    <tr>
    <td>
    <p>Tags</p>
    </td>
    <td>
    <ul>
    <li>Mobile Tag Property</li>
    <li>Rules</li>
    <li>Data Elements</li>
    <li>Library</li>
    <li>Environments (staging, production, development)</li>
    </ul>
    </td>
    </tr>
    <tr>
    <td>
    <p>Tags Extensions</p>
    </td>
    <td>
    <ul>
    <li>Adobe Experience Platform Edge Network</li>
    <li>Adobe Journey Optimizer</li>
    <li>AEP Assurance</li>
    <li>Consent (with default consent policies enabled)</li>
    <li>Identity (with default ECID, with default stitching rules)</li>
    <li>Mobile Core</li>
    </ul>
    </td>
    </tr>
    <tr>
    <td>
    <p>Assurance</p>
    </td>
    <td>
    <p>Assurance Session</p>
    </td>
    </tr>
    <tr>
    <td>
    <p>Datastreams</p>
    </td>
    <td>
    <p>Datastream with Services</p>
    </td>
    </tr>
    <tr>
    <td>
    <p>Experience Platform</p>
    </td>
    <td>
    <ul>
    <li>Dataset</li>
    <li>Schema</li>
    </ul>
    </td>
    </tr>
    </tbody>
    </table>

    +++

1. Once resources generation is done, click **[!UICONTROL Set up]** to start configuring your SDK.

    ![](assets/guided-setup-config-web-1.png)

1. Paste the code displayed on screen in the `<head>` tag of your document.

    ![](assets/guided-setup-config-web-2.png){zoomable="yes"}

1. To validate your SDK directly on your mobile application, simply paste your base URL.

    ![](assets/guided-setup-config-web-3.png){zoomable="yes"}

1. Select **[!UICONTROL Launch site & validate]** to connect your site.

    ![](assets/guided-setup-config-web-4.png){zoomable="yes"}

1. After completing the configuration, share the auto-generated **[!UICONTROL Mobile Web Property]** with the team members responsible for creating Journeys and Campaigns. 

    The **[!UICONTROL Mobile Web Property]** should be referenced in the Campaigns or Journeys interface, enabling a seamless connection between your setup and the execution of targeted journeys and campaigns for your audience.

    ![](assets/guided-setup-config-ios-8.png)

You can now create Web pages using the previously configured **[!UICONTROL Mobile Web Property]**. [Learn how to create Web page](../web/create-web.md)

## Modify an existing configuration {#reconnect}

After creating your configuration, you can easily revisit it at any time to add additional channels or make further adjustments to suit your needs

1. From Journey Optimizer homepage, click **[!UICONTROL Begin]** from the **[!UICONTROL Set up mobile and web channels]** card.

    ![](assets/guided-setup-config-1.png)

1. Select **[!UICONTROL Existing]** and choose your existing **[!UICONTROL Tag property]** from the drop-down.

    ![](assets/guided-setup-config-web-5.png)

1. You can now update your configuration as needed.
