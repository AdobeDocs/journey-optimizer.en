---
solution: Journey Optimizer
product: journey optimizer
title: Journey Optimizer built-in Roles
description: Learn about the built-in Roles
feature: Access Management
topic: Administration
role: Admin, User
level: Intermediate
keywords: permissions, authoring, messages
exl-id: 5a968bd8-cf76-4242-aa80-3cfb3d551511
TQID: https://experienceleague.adobe.com/LkOCFOSH-AzwWMoteNN-XI3R2yYkO5iBrVwMtobd4iI
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: bb359667-ec7d-4d4b-8663-5850fc219d32
    internal-label: Administration
  - id: b856530c-d60b-42d8-a19d-df2dfd7fe62a
    internal-label: Access control
subfeature_v2: []
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
  - id: c66ffd68-0f65-42bb-aa23-b4020f12e0bd
    internal-label: Admin
level_v2:
  - id: b5a62a22-46f7-4f0d-b151-3fc640bef588
    internal-label: Intermediate
topic_v2:
  - id: c7d04a2c-412a-4c9d-9d7a-4456eaa5adeb
    internal-label: Governance
  - id: e1e0219c-f879-479f-8427-888ed2a6e9c2
    internal-label: Insights
  - id: ebde5b41-29c9-4f5e-9ef6-1197e85409e3
    internal-label: Data management
  - id: eddd9b14-83bd-4ff4-9072-54a4a484abb7
    internal-label: Administration
---
# Built-in roles {#ootb-product-profiles}

>[!BEGINSHADEBOX]

**On this page:** Explore the built-in roles and the permissions each one includes, so you can quickly grant users a ready-made level of access that matches their responsibilities.

>[!ENDSHADEBOX]

Built-in roles are a set of unitary rights which allows users access to certain functionalities or objects in the interface. Refer to [this page](ootb-permissions.md) for the list of available permissions to build your role.


## [!DNL Campaign Administrator] {#campaign-administrator}

The **[!DNL Campaign Administrator]** role allows the administration menus with the possibility to manage and publish Campaigns and Decision management. 

This role includes the following permissions:

| Resources | Permissions|
|-|-|
|Adobe Experience Platform|<ul> <li>**[!DNL Manage merge policies]**: read, create, edit, and delete merge policies.</li> <li>**[!DNL Manage profiles]**: read, create, edit, and delete profiles.</li> <li>**[!DNL Manage segments]**: read, create, edit, and delete segment definitions.</li> <li>**[!DNL View datasets]**: read-only access to datasets.</li> <li>**[!DNL Read Identity namespace]**: read-only access to identity namespace.</li> <li>**[!DNL View schemas]**: read-only access to schemas.</li> <li>**[!DNL Sandbox]**: grant access to sandboxes.</li> </ul>|
|Campaigns| <ul><li> **[!DNL Manage campaigns]**: read, create, edit, and delete campaigns.</li><li>**[!DNL Publish campaigns]**: publish campaigns.</li><li>**[!DNL View campaigns report]**: read and edit campaigns report.</li></ul>|
|Channel configurations|<ul> <li>**[!DNL Export suppression list]**: access to export suppression list as a CSV file.</li> <li>**[!DNL Manage alerts]**: enable/disable alerts for campaigns, messages and entitlements.</li> <li>**[!DNL Manage IP pools]**: read, create, edit, and delete ip pool.</li> <li>**[!DNL Manage landing page settings]**: read, create, edit, and delete landing page settings.</li> <li>**[!DNL Manage messages general settings]**: read, create, edit, and delete message general settings.</li> <li>**[!DNL Manage messages presets]**: read, create, edit, and delete content branding.</li> <li>**[!DNL Manage PTR records]**: read and edit PTR records.</li> <li>**[!DNL Manage SMS settings]**: read, create, edit, and delete SMS settings.</li> <li>**[!DNL Manage subdomains delegation]**: read, create, edit, and delete subdomain delegation.</li> <li>**[!DNL Manage suppression rules]**: access read, create, edit and delete suppression rules.</li> <li>**[!DNL View PTR records]**: read-only access to PTR records.</li> <li>**[!DNL View suppression list]**: read and export local suppression list.</li> </ul>|
|Decision management|<ul><li>**[!DNL Manage decisions]**: read, create, edit, and delete decisions.</li><li>**[!DNL Manage ranking strategies]**: read, create, edit, and delete ranking strategies.</li></ul>|

## [!DNL Campaign Approver] {#campaign-approver}

The **[!DNL Campaign Approver]** role allows users to approve deliveries and publish them. They can later check the success of their deliveries with the **[!DNL Campaigns]** reports. 

| Resources | Permissions|
|-|-|
|Adobe Experience Platform| <ul><li>**[!DNL Manage merge policies]**: read, create, edit, and delete merge policies.</li><li>**[!DNL Manage segments]**: read, create, edit, and delete segment definitions.</li><li>**[!DNL Manage profiles]**: read, create, edit, and delete profiles.</li><li>**[!DNL View datasets]**: read-only access to datasets.</li><li>**[!DNL View schemas]**: read-only access to schemas.</li></ul>|
|Campaigns| <ul><li>**[!DNL Manage campaigns]**: read, create, edit, and delete campaigns.</li><li>**[!DNL Publish campaigns]**: publish campaigns.</li><li>**[!DNL View campaigns report]**: read, edit campaign reports.</li></ul>|
|Channel configurations| <ul><li>**[!DNL View messages presets]**: read-only access to messages presets.</li></ul>|
|Decision management| <ul><li>**[!DNL Manage decisions]**: read, create, edit, and delete decisioning entities.</li><li>**[!DNL Manage ranking strategies]**: read, create, edit, and delete custom messages reports and use action features.</li></ul>|


## [!DNL Campaign Manager] {#campaign-manager}

The **[!DNL Campaign Manager]** role allows users to create and edit **[!UICONTROL Campaigns]** and every capability linked to **[!UICONTROL Campaigns]** but will not be able to publish them.

This role includes the following permissions:

| Resources | Permissions|
|-|-|
|Adobe Experience Platform| <ul><li>**[!DNL Manage merge policies]**: read, create, edit, and delete merge policies.</li><li>**[!DNL Manage profiles]**: read, create, edit, and delete profiles.</li><li> **[!DNL Manage segments]**: read, create, edit, and delete segment definitions.</li><li>**[!DNL View datasets]**: read-only access to datasets.</li><li>**[!DNL View schemas]**: read-only access to schemas.</li></ul>|
|Campaigns| <ul><li>**[!DNL Manage campaigns]**: read, create, edit, and delete campaigns.</li><li>**[!DNL View campaigns report]**: read, edit journey report.</li></ul>|
|Channel configurations| <ul><li>**[!DNL View messages presets]**: read-only access to messages presets.</li></ul>|
|Decision management| <ul><li>**[!DNL Manage decisions]**: read, create, edit, and delete decisioning entities.</li><li>**[!DNL Manage ranking strategies]**: read, create, edit, and delete custom messages reports and use action features.</li></ul>|

## [!DNL Campaign Viewer] {#campaign-viewer}

The **[!DNL Campaign Viewer]** role allows read-only access to the **[!UICONTROL Campaigns]** and **[!UICONTROL Decision management]** capabilities. 

Users assigned to this role will not be able to edit or publish. 

This role includes the following permissions:

| Resources | Permissions|
|-|-|
|Campaigns| <ul><li>**[!DNL View campaigns]**: read-only access to campaigns.</li><li>**[!DNL View campaigns report]**: read-only access to campaigns reports.</li></ul>|
|Decision management| <ul><li>**[!DNL View decisions]**: read-only access to decisions entities.</li></ul>|

## [!DNL Content Library Manager] {#content-library-manager}
 
The **[!DNL Content Library Manager]** role only allows access to the **[!UICONTROL Content templates]** menu. Users assigned to this role will only be able to access the template library to create content without accessing the journeys or campaigns.

This permission includes the following permissions:

| Capability | Permissions|
|-|-|
|Adobe Experience Platform| <ul><li>**[!DNL Manage merge policies]**: read, create, edit, and delete merge policies.</li><li>**[!DNL Manage profiles]**: read, create, edit, and delete profiles.</li><li> **[!DNL Manage segments]**: read, create, edit, and delete segment definitions.</li><li>**[!DNL View datasets]**: read-only access to datasets.</li><li>**[!DNL View schemas]**: read-only access to schemas.</li></ul>|
|Decision management|<ul><li>**[!DNL Manage decisions]**: read, create, edit, and delete decisioning entities.</li><li>**[!DNL Manage ranking strategies]**: read, create, edit, and delete custom reports and use action features.</li></ul>|
|Journey Optimizer Library| <ul><li>**[!DNL Manage library items]**: read, create, edit, and delete Journey Optimizer Library items, including content templates and fragments.</li><li>**[!DNL Manage simulate content]**: access to the **[!UICONTROL Simulate content]** option for preview and proof.</li><li>**[!DNL Publish Fragment]**: publish content fragments.</li></ul>|

## [!DNL Decisioning manager] {#decisioning-manager}

The **[!DNL Decisioning manager]** role only allows access to the **[!UICONTROL Decision management]** menu. Users assigned to this role will only be able to manage, view and publish decisions. 

This permission includes the following permissions:

| Capability | Permissions|
|-|-|
|Decision management| <ul><li>**[!DNL Manage decisions]**: read, create, edit, and delete decisioning entities.</li><li>**[!DNL Manage ranking strategies]**: read, create, edit, and delete custom reports and use action features.</li><li>**[!DNL View decisions]**:  read-only access to decisioning entities.</li><li>**[!DNL Publish decisions]**: activate or deactivate decisioning activities.</li><!--li>**[!DNL Manage Experience decisions]**: read, create, edit, and delete Decisioning entities.</li--></ul>|

## [!DNL Journey Administrator] {#journey-administrator}

The **[!DNL Journey Administrator]** role allows the administration menus with the possibility to manage and publish Journeys and Decision management. 

This role includes the following permissions:

| Resources | Permissions|
|-|-|
| Adobe Experience Platform |<ul> <li>**[!DNL Manage merge policies]**: read, create, edit, and delete merge policies.</li> <li>**[!DNL Manage profiles]**: read, create, edit, and delete profiles.</li> <li>**[!DNL Manage segments]**: read, create, edit, and delete segment definitions.</li> <li>**[!DNL View datasets]**: read-only access to datasets.</li> <li>**[!DNL Read Identity namespace]**: read-only access to identity namespace.</li> <li>**[!DNL View schemas]**: read-only access to schemas.</li> <li>**[!DNL Sandbox]**: grant access to sandboxes.</li> </ul> |
| Channel configurations |<ul> <li>**[!DNL Manage alerts]**: enable/disable alerts for journeys and entitlements.</li> <li>**[!DNL Manage IP pools]**: read, create, edit, and delete ip pool.</li> <li>**[!DNL Manage Landing page settings]**: create, edit and delete Landing page subdomains and Landing page presets.</li> <li>**[!DNL Manage messages general settings]**: read, create, edit, and delete message general settings.</li> <li>**[!DNL Manage messages presets]**: read, create, edit, and delete content branding.</li> <li>**[!DNL Manage PTR records]**: read and edit PTR records.</li> <li>**[!DNL Manage SMS settings]**: create, edit and delete API credentials and SMS channel configurations required to enable SMS channel.</li> <li>**[!DNL Manage subdomains delegation]**: read, create, edit, and delete subdomain delegation.</li> <li>**[!DNL Manage suppression rules]**: access read, create, edit and delete suppression rules.</li> <li>**[!DNL View PTR records]**: read-only access to PTR records.</li> <li>**[!DNL View suppression list]**: read and export local suppression list.</li> </ul> |
| Data Governance |<ul> <li>**[!DNL Manage data usage policies]**: read, create, edit, and delete data usage policies.</li> <li>**[!DNL Manage usage label]**: read, create, and delete usage labels.</li> <li>**[!DNL View data usage policies]**: read-only access to data usage policies.</li> <li>**[!DNL View user activity log]**: read-only access to view recorded audit logs of Experience Platform activities..</li> </ul> |
| Decision management |<ul> <li>**[!DNL Manage decisions]**: read, create, edit, and delete decisions.</li> <li>**[!DNL Manage ranking strategies]**: read, create, edit, and delete ranking strategies.</li> </ul> |
| Journeys |<ul> <li>**[!DNL Manage journeys]**: read, create, edit, stop (live, test mode and dry run) and delete journeys. </li> <li>**[!DNL Manage journeys events, data sources and actions]**: read, create, edit, and delete events, sources or actions.</li> <li>**[!DNL Publish journeys]**: publish, start test mode, start dry run, pause and resume journeys. </li> <li>**[!DNL View journeys report]**: read and edit journeys report.</li> </ul> |
| Journey Optimizer Library |<ul> <li>**[!DNL Manage Library Items]**: add and delete saved expressions in the [!DNL Journey Optimizer] Library.</li> </ul> |

## [!DNL Journey Approver] {#journey-approver}

The **[!DNL Journey Approver]** role allows users to approve deliveries and publish them. They can later check the success of their deliveries with the **[!DNL Journey]** reports. 

This role includes the following permissions:

| Resources| Permissions|
|-|-|
|Adobe Experience Platform| <ul><li>**[!DNL Manage merge policies]**: read, create, edit, and delete merge policies.</li><li>**[!DNL Manage profiles]**: read, create, edit, and delete profiles.</li><li>**[!DNL Manage segments]**: read, create, edit, and delete segment definitions.</li><li>**[!DNL View datasets]**: read-only access to datasets.</li><li>**[!DNL View schemas]**: read-only access to schemas.</li></ul>|
|Channel configurations| <ul><li>**[!DNL View channel configurations]**: read-only access to channel configurations.</li></ul>|
|Decision management| <ul><li>**[!DNL Manage decisions]**: read, create, edit, and delete decisioning entities.</li><li>**[!DNL Manage ranking strategies]**: read, create, edit, and delete custom reports and use action features.</li></ul>|
|Journeys| <ul><li>**[!DNL Manage journeys]**: read, create, edit, stop (live, test mode and dry run) and delete journeys. </li><li>**[!DNL Publish journey]**: publish, start test mode, start dry run, pause and resume journeys. </li><li>**[!DNL View journeys events, data sources and actions]**: read-only access to journey events, journey custom actions and journey data sources sources.</li><li>**[!DNL View journeys report]**: read, edit journey reports.</li></ul>|

## [!DNL Journey Manager] {#journey-manager}

The **[!DNL Journey Manager]** role allows users to create and edit **[!UICONTROL Journeys]** and every capability linked to **[!UICONTROL Journeys]** but will not be able to publish them.

This role includes the following permissions:

| Resources | Permissions|
|-|-|
|Adobe Experience Platform| <ul><li>**[!DNL Manage merge policies]**: read, create, edit, and delete merge policies.</li><li>**[!DNL Manage profiles]**: read, create, edit, and delete profiles.</li><li> **[!DNL Manage segments]**: read, create, edit, and delete segment definitions.</li><li>**[!DNL View datasets]**: read-only access to datasets.</li><li>**[!DNL View schemas]**: read-only access to schemas.</li></ul>|
|Channel configurations| <ul><li>**[!DNL View channel configurations]**: read-only access to channel configurations.</li></ul>|
|Decision management| <ul><li>**[!DNL Manage decisions]**: read, create, edit, and delete decisioning entities.</li><li>**[!DNL Manage ranking strategies]**: read, create, edit, and delete custom reports and use action features.</li></ul>|
|Journeys| <ul><li>**[!DNL Manage journeys]**: read, create, edit, stop (live, test mode and dry run) and delete journeys.</li><li>**[!DNL View journeys events]**: read-only access to journey events, journey custom actions and journey data sources sources.</li><li>**[!DNL View journeys report]**: read, edit journey report.</li></ul>|

## [!DNL Journey Viewer] {#journey-viewer}

The **[!DNL Journey viewer]** role allows read-only access to the **[!UICONTROL Journeys]** and **[!UICONTROL Decision management]** capabilities. 

Users assigned to this role will not be able to edit or publish. 

This role includes the following permissions:

| Resources | Permissions|
|-|-|
|Decision management| <ul><li>**[!DNL View decisions]**: read-only access to decisions entities.</li></ul>|
|Journeys| <ul><li>**[!DNL View journeys]**: read-only access to journeys.</li><li>**[!DNL View journeys event, data sources, actions]**: read-only access to journeys events and data sources.</li><li>**[!DNL View journeys report]**: read-only access to journeys reports.</li></ul>|

## [!DNL Orchestrated Campaign Administrators] {#orchestrated-campaign-administrator}

The **[!DNL Orchestrated Campaign Administrator]** role allows the administration menus with the possibility to manage and publish Orchestrated campaigns. 

This role includes the following permissions:

| Resources | Permissions|
|-|-|
|Adobe Experience Platform|<ul> <li>**[!DNL Enable AI Assistant]**: enable or access AI-powered campaign and audience features.</li> <li>**[!DNL Manage merge policies]**: read, create, edit, and delete merge policies.</li> <li>**[!DNL Manage profiles]**: read, create, edit, and delete profiles.</li> <li>**[!DNL Manage segments]**: read, create, edit, and delete segment definitions.</li> <li>**[!DNL View datasets]**: read-only access to datasets.</li> <li>**[!DNL Read Identity namespace]**: read-only access to identity namespace.</li> <li>**[!DNL View schemas]**: read-only access to schemas.</li> <li>**[!DNL Sandbox]**: grant access to sandboxes.</li> <li>**[!DNL View operational insights]**: read-only access to system-level insights and monitoring dashboards.</li></ul>|
|Channel configurations|<ul><li>**[!DNL Export suppression list]**: access to export suppression list as a CSV file.</li> <li>**[!DNL Manage alerts]**: enable/disable alerts for campaigns, messages and entitlements.</li> <li>**[!DNL Manage custom dashboards]**: read, create, edit, and delete custom dashboards.</li><li>**[!DNL Manage IP pools]**: read, create, edit, and delete ip pool.</li> <li>**[!DNL Manage landing page settings]**: read, create, edit, and delete landing page settings.</li> <li>**[!DNL Manage messages general settings]**: read, create, edit, and delete message general settings.</li> <li>**[!DNL Manage messages presets]**: read, create, edit, and delete content branding.</li><li>**[!DNL Manage PTR records]**: read and edit PTR records.</li> <li>**[!DNL Manage SMS settings]**: read, create, edit, and delete SMS settings.</li> <li>**[!DNL Manage subdomains delegation]**: read, create, edit, and delete subdomain delegation.</li> <li>**[!DNL Manage suppression rules]**: access read, create, edit and delete suppression rules.</li> <li>**[!DNL View PTR records]**: read-only access to PTR records.</li> <li>**[!DNL View suppression list]**: read and export local suppression list.</li> </ul>|
|Dashboard|<ul> <li>**[!DNL Manage standard dashboard]**: read, create, edit and delete custom widgets and widget schema through the Widget library.</li> </ul>|
|Data governance|<ul> <li>**[!DNL View user activity log]**: read-only access to view recorded audit logs of Experience Platform activities. </li> </ul>|
|Data ingestion|<ul> <li>**[!DNL Manage sources]**: read, create, edit, and disable sources.</li> </ul>|
|Data management|<ul> <li>**[!DNL Manage datasets]**: read, create, edit, and delete datasets.</li> </ul>|
|Data modelling|<ul> <li>**[!DNL Manage schemas]**: read, create, edit, and delete schemas and related resources.</li> </ul>|
|Decision management|<ul><li>**[!DNL Manage decisions]**: read, create, edit, and delete decisions.</li><li>**[!DNL Manage ranking strategies]**: read, create, edit, and delete ranking strategies.</li></ul>|
|Journey Optimizer rules|<ul> <li>**[!DNL View frequency rules]**: read-only access to frequency rules.</li><li>**[!DNL Manage frequency rules]**:  read, create, edit, or delete frequency rules.</li> </ul>|
|Messages |<ul><li> **[!DNL Manage Messages]**: read, create, edit, and delete messages. </li> **[!DNL Manage Messages Preview and Test]**: approve and publish messages when a policy is applied.</li><li>**[!DNL Publish Messages]**: publish messages. </li><li>**[!DNL View Messages Report]**: read and edit message reports. <li></ul>|
|Orchestrated campaigns| <ul><li> **[!DNL Manage orchestrated campaigns]**: read, create, edit, and delete Orchestrated campaigns.</li> <li>**[!DNL Manage orchestrated campaigns admin]**: read, create, edit and delete links and reconciliations between Adobe Experience Platform Profiles and Relational store entities.</li><li>**[!DNL Publish orchestrated campaigns]**: publish Orchestrated campaigns.</li><li>**[!DNL View orchestrated campaigns report]**: read and edit Orchestrated campaigns report.</li></ul>|

## [!DNL Orchestrated Campaign Approver] {#orchestrated-campaign-approver}

The **[!DNL Orchestrated Campaign Approver]** role allows users to publish Orchestrated campaigns.

| Resources | Permissions|
|-|-|
|Adobe Experience Platform|<ul> <li>**[!DNL Manage segments]**: read, create, edit, and delete segment definitions.</li> <li>**[!DNL Manage profiles]**: read, create, edit, and delete profiles.</li> <li>**[!DNL View datasets]**: read-only access to datasets.</li> <li>**[!DNL View schemas]**: read-only access to schemas.</li> <li>**[!DNL Manage merge policies]**: read, create, edit, and delete merge policies.</li> <li>**[!DNL Enable AI Assistant]**: enable or access AI-powered campaign and audience features.</li>  <li>**[!DNL View operational insights]**: read-only access to system-level insights and monitoring dashboards.</li></ul>|
|Channel configurations|<ul><li>**[!DNL View messages presets]**: read-only access to messages presets.</li> <li>**[!DNL Manage custom dashboards]**: create, edit, and delete custom dashboards.</li></ul>|
|Dashboard|<ul> <li>**[!DNL Manage standard dashboard]**: read, create, edit and delete custom widgets and widget schema through the Widget library.</li> </ul>|
|Data governance|<ul> <li>**[!DNL View user activity log]**: read-only access to view recorded audit logs of Experience Platform activities.</li> </ul>|
|Decision management| <ul><li>**[!DNL Manage decisions]**: read, create, edit, and delete decisioning entities.</li><li>**[!DNL Manage ranking strategies]**: read, create, edit, and delete custom messages reports and use action features.</li></ul>|
|Journey Optimizer rules|<ul> <li>**[!DNL View frequency rules]**: read-only access to frequency rules.</li></ul>|
|Messages |<ul><li> **[!DNL Manage Messages]**: read, create, edit, and delete messages. </li> **[!DNL Manage Messages Preview and Test]**: approve and publish messages when a policy is applied.</li><li>**[!DNL Publish Messages]**: publish messages. </li><li>**[!DNL View Messages Report]**: read and edit message reports. <li></ul>|
|Orchestrated campaigns| <ul><li>**[!DNL Manage orchestrated campaigns]**: read, create, edit, and delete Orchestrated campaigns.</li><li>**[!DNL Publish orchestrated campaigns]**: publish Orchestrated campaigns.</li><li>**[!DNL View orchestrated campaigns admin]**: read-only access to links and reconciliations between Adobe Experience Platform Profiles and Relational store entities.</li><li>**[!DNL View orchestrated campaigns report]**: read, edit Orchestrated campaign reports.</li></ul>|

## [!DNL Orchestrated Campaign Manager] {#orchestrated-campaign-manager}

The **[!DNL Orchestrated Campaign Manager]** role allows users to create and edit **[!UICONTROL Orchestrated campaigns]** and every capability linked to **[!UICONTROL Orchestrated campaigns]** but will not be able to publish them.

This role includes the following permissions:

| Resources | Permissions|
|-|-|
|Adobe Experience Platform| <ul><li>**[!DNL Enable AI Assistant]**: enable or access AI-powered campaign and audience features.</li> <li>**[!DNL Manage merge policies]**: read, create, edit, and delete merge policies.</li><li>**[!DNL Manage profiles]**: read, create, edit, and delete profiles.</li><li> **[!DNL Manage segments]**: read, create, edit, and delete segment definitions.</li><li>**[!DNL View datasets]**: read-only access to datasets.</li>  <li>**[!DNL View operational insights]**: read-only access to system-level insights and monitoring dashboards.</li><li>**[!DNL View schemas]**: read-only access to schemas.</li></ul>|
|Channel configurations| <ul><li>**[!DNL Manage custom dashboards]**: create, edit, and delete custom dashboards.</li><li>**[!DNL View messages presets]**: read-only access to messages presets.</li></ul>|
|Dashboard|<ul> <li>**[!DNL Manage standard dashboard]**: read, create, edit and delete custom widgets and widget schema through the Widget library.</li> </ul>|
|Data governance|<ul> <li>**[!DNL View user activity log]**: read-only access to view recorded audit logs of Experience Platform activities.</li> </ul>|
|Decision management| <ul><li>**[!DNL Manage decisions]**: read, create, edit, and delete decisioning entities.</li><li>**[!DNL Manage ranking strategies]**: read, create, edit, and delete custom messages reports and use action features.</li></ul>|
|Journey Optimizer rules|<ul> <li>**[!DNL View frequency rules]**: read-only access to frequency rules. </li></ul>|
|Messages |<ul><li> **[!DNL Manage Messages]**: read, create, edit, and delete messages. </li> **[!DNL Manage Messages Preview and Test]**: approve and publish messages when a policy is applied.</li><li>**[!DNL View Messages Report]**: read and edit message reports. </li></ul>|
|Orchestrated campaigns| <ul><li>**[!DNL Manage orchestrated campaigns]**: read, create, edit, and delete Orchestrated campaigns.</li><li>**[!DNL View orchestrated campaigns report]**: read, edit Orchestrated campaigns.</li><li>**[!DNL View orchestrated campaigns admin]**: read-only access to links and reconciliations between Adobe Experience Platform Profiles and Relational store entities.</li></ul>|

## [!DNL Orchestrated Campaign Viewer] {#orchestrated-campaign-viewer}

The **[!DNL Campaign Viewer]** role allows read-only access to the **[!UICONTROL Orchestrated campaigns]** capabilities. 

Users assigned to this role will not be able to edit or publish. 

This role includes the following permissions:

| Resources | Permissions|
|-|-|
|Adobe Experience Platform| <ul><li>**[!DNL Enable AI Assistant]**: enable or access AI-powered campaign and audience features.</li> <li>**[!DNL View operational insights]**: read-only access to system-level insights and monitoring dashboards.</li></ul>|
|Channel configurations| <ul><li>**[!DNL Manage custom dashboards]**: create, edit, and delete custom dashboards.</li></ul>|
|Dashboard|<ul> <li>**[!DNL Manage standard dashboard]**: read, create, edit and delete custom widgets and widget schema through the Widget library.</li> </ul>|
|Data governance|<ul> <li>**[!DNL View user activity log]**: read-only access to view recorded audit logs of Experience Platform activities.</li> </ul>|
|Decision management| <ul><li>**[!DNL View decisions]**: read-only access to decisions entities.</li></ul>|
|Journey Optimizer rules|<ul> <li>**[!DNL View frequency rules]**: read-only access to frequency rules.</li></ul>|
|Orchestrated campaigns| <ul><li>**[!DNL View orchestrated campaigns]**: read-only access to Orchestrated campaigns.</li><li>**[!DNL View orchestrated campaigns report]**: read-only access to Orchestrated campaigns reports.</li></ul>|

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** Journey Optimizer ships with built-in roles — from Campaign Administrator to Orchestrated Campaign Viewer — each bundling a ready-made permission set, so administrators can quickly grant users a level of access that matches their responsibilities without building a role from scratch.

**Intents:**

* Identify which built-in role best fits a user's job responsibilities
* Understand what each built-in role can and cannot do (including publish rights)
* Compare roles across journey, campaign, and orchestrated campaign domains
* Assign a ready-made role instead of creating a custom one
* Understand which roles include AI Assistant access

**Glossary:**

* **Built-in role**: A pre-defined set of permissions and resource rights ready to assign to users without custom configuration *(product-specific)*
* **Journey Administrator**: Built-in role enabling management and publication of Journeys and Decision management, including channel configuration and data governance permissions *(product-specific)*
* **Campaign Administrator**: Built-in role enabling management and publication of Campaigns and Decision management, including channel configurations *(product-specific)*
* **Decisioning manager**: Built-in role providing access exclusively to the Decision management menu; can manage, view, and publish decisions *(product-specific)*
* **Content Library Manager**: Built-in role providing access only to the Content templates menu; cannot access journeys or campaigns *(product-specific)*
* **Test mode**: A journey execution mode referenced in Manage journeys and Publish journeys permissions (Journey Administrator can stop journeys in test mode; Publish journeys permission includes starting test mode) *(product-specific)*
* **Dry run**: A journey execution mode referenced in Manage journeys and Publish journeys permissions alongside test mode *(product-specific)*

**Terminology:**

* Canonical name: Built-in roles — variants: out-of-the-box roles, OOTB roles, product profiles
* Do not confuse: "Campaign Approver" (can approve and publish campaigns) ≠ "Campaign Manager" (can create and edit campaigns but cannot publish them)
* Do not confuse: "Journey Approver" (can approve and publish journeys) ≠ "Journey Manager" (can create and edit journeys but cannot publish them)
* Do not confuse: "Journey Viewer" (read-only access to journeys and decision management) ≠ "Campaign Viewer" (read-only access to campaigns and decision management)
* Do not confuse: "Orchestrated Campaign Administrator" (manages orchestrated campaigns, includes AI Assistant and data ingestion/management) ≠ "Campaign Administrator" (manages standard campaigns; does not include orchestrated campaign permissions)
* Do not confuse: "Test mode" (referenced as a journey execution state that can be stopped or started via Manage journeys / Publish journeys) ≠ "Dry run" (a separate journey execution mode also referenced in those same permissions)

**FAQ:**

* **Q: Which built-in roles can publish journeys?** — Journey Administrator and Journey Approver can publish journeys.
* **Q: Can a Journey Manager publish journeys?** — No; Journey Manager can create and edit journeys but the Publish journeys permission is not included in that role.
* **Q: Which role grants access only to the Decision management menu?** — Decisioning manager.
* **Q: Which role provides access only to content templates?** — Content Library Manager.
* **Q: Which built-in roles include the Enable AI Assistant permission?** — Orchestrated Campaign Administrator, Orchestrated Campaign Approver, Orchestrated Campaign Manager, and Orchestrated Campaign Viewer.

+++
<!-- ai-accordion-version: 1 | source-hash: b9740765 -->




