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
hide: yes
hidefromtoc: yes
---
# Get started with Guided channel setup {#set-mobile-config}

>[!CONTEXTUALHELP]
>id="ajo_mobile_web_setup_name"
>title="Mobile and web configuration name"
>abstract="Enter the name of your mobile or web configuration. This name will be used for every resource automatically created with the Guided Channel Setup."

>[!CONTEXTUALHELP]
>id="ajo_mobile_web_setup_validate_assurance"
>title="Validate with Assurance"
>abstract="Ensure the quality of your mobile app's data collection and user experience with Assurance. This tool offers thorough analysis, validation, and optimization. Additionally, you can directly connect your app to verify accurate SDK integration."
>additional-url="https://experienceleague.adobe.com/en/docs/platform-learn/implement-mobile-sdk/app-implementation/assurance" text="See Assurance documentation"


This set up facilitates the expeditious configuration of marketing channels, ensuring all required resources are readily available within Experience Platform, Journey Optimizer, and Data Collection. This enables your marketing team to immediately start with campaign and journey creation.

To effectively implement this, it is essential that a member of the organization with the authority and technical ability to modify website or mobile code oversees the setup.

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

<table style="table-layout:fixed"><tr style="border: 0;">
<td>
<a href="set-mobile-android.md">
<img alt="Lead" src="assets/do-not-localize/config-android.jpeg">
</a>
<div><a href="set-mobile-android.md"><strong>Set up Android mobile configuration</strong>
</div>
<p>
</td>
<td>
<a href="set-mobile-ios.md">
<img alt="Infrequent" src="assets/do-not-localize/config-ios.jpeg">
</a>
<div>
<a href="set-mobile-ios.md"><strong>Set up iOS mobile configuration</strong></a>
</div>
<p></td>
<td>
<a href="set-mobile-web.md">
<img alt="Validation" src="assets/do-not-localize/config-web.jpeg">
</a>
<div>
<a href="set-mobile-web.md"><strong>Set up Web configuration</strong></a>
</div>
<p>
</td>
</tr></table>
