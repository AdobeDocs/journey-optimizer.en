---
solution: Journey Optimizer
product: journey optimizer
title: Set up mobile and web
description: Learn how to configure and monitor mobile and web channels
feature: Surface, Channel Configuration
topic: Administration
role: Admin
level: Experienced
keywords: channel, surface, technical, parameters, optimizer
exl-id: 846e0d11-798b-4f3b-80db-848a17d32830
---
# Get started with Guided channel setup {#set-mobile-config}

>[!CONTEXTUALHELP]
>id="ajo_mobile_web_setup_name"
>title="Mobile and web configuration name"
>abstract="Enter the name of your mobile or web configuration. This name will be used for every resource automatically created with the Guided Channel Setup."

>[!CONTEXTUALHELP]
>id="ajo_mobile_web_setup_validate_assurance"
>title="Validate with Assurance"
>abstract="Adobe Experience Platform Assurance is embedded into this workflow to help you inspect your SDK implementation, as well as simulate and validate application events."
>additional-url="https://experienceleague.adobe.com/en/docs/experience-platform/assurance/home" text="Adobe Experience Platform Assurance Overview"

This set up facilitates the expeditious configuration of marketing channels, ensuring all required resources are readily available within Experience Platform, Journey Optimizer, and Data Collection. This enables your marketing team to start with campaign and journey creation.

The Guided Channel setup supports the following platforms and channels.

* Platforms and SDKs:

  * Swift by Apple, iOS

  * Kotlin, Android

  * Javascript, Web

* Channels:

  * Mobile In-App

  * Mobile Push Message

  * Web Basic


Note that for each platform that you would like to setup, it is required to create a separate configuration. This is because each app requires a unique Channel Configuration, and this provides the flexibility to determine which channels you would like for each platform.

## Prerequisites {#prereq}

* To effectively implement this, it is essential that a member of the organization with the authority and technical ability to modify website or mobile code oversees the setup.

  Below are the permissions required to run the Guided Channel Setup.

  +++ Required permissions

  <table>
    <thead>
      <tr>
        <th><strong>Solution</strong></th>
        <th><strong>Permissions</strong></th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>
          <p>Data collection</p>
        </td>
        <td>
          <ul>
            <li>Company Rights > Properties</li>
            <li>Property Rights: Develop, publish, manage extensions and environments</li>
            <li>App Surfaces: Manage app Configuration</li>
         </ul>
        </td>
      </tr>
      <tr>
        <td>
          <p>Adobe Experience Platform</p>
        </td>
        <td>
        <ul>
            <li>Data Collection: Manage datastreams</li>
           <li>Sandbox: grant access to sandboxes</li>
            <li>Manage segments: read, create, edit, and delete segment definitions</li>
            <li>Manage profiles: read, create, edit, and delete profiles</li>
            <li>Read datasets: read-only access to datasets</li>
            <li>Read schemas: read-only access to schemas</li>
            <li>Read Identity namespace: read-only access to identity namespace</li>
          </ul>
        </td>
      </tr>
      <tr>
        <td>
         <p>Adobe Journey Optimizer</p>
        </td>
        <td>
          <p>Campaigns: Manage and publish campaigns</p>
        </td>
      </tr>
    </tbody>
  </table>

  +++

* If you are using the Existing configuration option, please ensure that you are using the following Adobe Experience Platform Mobile SDK extension versions. For more details on the SDK setup including the required dependencies and initialization code, please refer to the [following documentation](https://experienceleague.adobe.com/en/docs/platform-learn/implement-mobile-sdk/app-implementation/install-sdks).
  
  For Android

    * Mobile Core v3.1.0 or later
    * Adobe Journey Optimizer v3.1.0 or later

  For iOS

    * Mobile Core v5.2.0 or later
    * Adobe Journey Optimizer v5.1.1 or later

## Auto-created resources {#auto-create-resources}

The Guided Channel Setup simplifies the rapid configuration of marketing channels, making all essential resources readily available in the Experience Platform, Journey Optimizer, and Data Collection apps. This allows your marketing team to quickly start creating campaigns and journeys. Below is a list of the resources that are auto generated and configured as a part of the Guided Channel Setup.

Browse through the tabs below to access the comprehensive lists of all the resources that are auto generated:

>[!BEGINTABS]

>[!TAB iOS]

For the **Initial configuration**, below is a comprehensive list of all the resources created on the **Configuration Details** screen when you click **Auto-Create Resources**.

  <table>
  <thead>
  <tr>
  <th><strong>Solution</strong></th>
  <th><strong>Auto-created resources</strong></th>
  </tr>
  </thead>
  <tbody>
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

  For the **Channel setup**, below is a comprehensive list of all the resources created on the **Add Channels** screen.

  <table>
  <thead>
  <tr>
  <th><strong>Solution</strong></th>
  <th><strong>Auto-created resources</strong></th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td>
  <p>Journey Optimizer</p>
  </td>
  <td>
  <ul>
  <li>Channel Configuration</li>
  <li>Upload Push Credential (mobile push message only)</li>
  </ul>
  </td>
  </tr>
  </tbody>
  </table>

>[!TAB Android]

For the **Initial configuration**, below is a comprehensive list of all the resources created on the **Configuration Details** screen when you click **Auto-Create Resources**.

  <table>
  <thead>
  <tr>
  <th><strong>Solution</strong></th>
  <th><strong>Auto-created resources</strong></th>
  </tr>
  </thead>
  <tbody>
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

  For the **Channel setup**, below is a comprehensive list of all the resources created on the **Add Channels** screen.

  <table>
  <thead>
  <tr>
  <th><strong>Solution</strong></th>
  <th><strong>Auto-created resources</strong></th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td>
  <p>Journey Optimizer</p>
  </td>
  <td>
  <ul>
  <li>Channel Configuration</li>
  <li>Upload Push Credential (mobile push message only)</li>
  </ul>
  </td>
  </tr>
  </tbody>
  </table>

>[!TAB Web]

For the **Initial configuration**, below is a comprehensive list of all the resources created on the **Configuration Details** screen when you click **Auto-Create Resources**.

  <table>
  <thead>
  <tr>
  <th><strong>Solution</strong></th>
  <th><strong>Auto-created resources</strong></th>
  </tr>
  </thead>
  <tbody>
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

>[!ENDTABS]

