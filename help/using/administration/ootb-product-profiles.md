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
---
# Built-in roles {#ootb-product-profiles}

Built-in roles are a set of unitary rights which allows users access to certain functionalities or objects in the interface. Refer to [this page](ootb-permissions.md) for the list of available permissions to build your role.

## [!DNL Campaign Administrator] {#campaign-administrator}

The **[!DNL Campaign Administrator]** role allows the administration menus with the possibility to manage and publish Campaigns and Decision management. 

This role includes the following permissions:

| Resources | Permissions|
|-|-|
|Campaigns| <ul><li> **[!DNL Manage campaigns]**: read, create, edit, and delete campaigns.</li><li>**[!DNL Publish campaigns]**: publish campaigns.</li><li>**[!DNL View campaigns report]**: read and edit campaigns report.</li></ul>|
|Channel configurations|<ul><li>**[!DNL Manage subdomains delegation]**: read, create, edit, and delete subdomain delegation.</li><li>**[!DNL Manage IP pools]**: read, create, edit, and delete ip pool.</li><li>**[!DNL Manage PTR records]**: read and edit PTR records.</li><li>**[!DNL View PTR records]**: read-only access to PTR records.</li><li> **[!DNL Manage messages general settings]**: read, create, edit, and delete message general settings.</li><li>**[!DNL Manage messages presets]**: read, create, edit, and delete content branding.</li><li>**[!DNL Manage suppression rules]**: access read, create, edit and delete suppression rules.</li><li>**[!DNL Export suppression list]**: access to export suppression list as a CSV file.</li><li>**[!DNL View suppression list]**: read and export local suppression list.</li><li>**[!DNL Manage alerts]**: enable/disable alerts for campaigns, messages and entitlements.</li><li>**[!DNL Manage landing page settings]**: read, create, edit, and delete landing page settings.</li><li>**[!DNL Manage SMS settings]**: read, create, edit, and delete SMS settings.</li></ul>|
|Decision management|<ul><li>**[!DNL Manage decisions]**: read, create, edit, and delete decisions.</li><li>**[!DNL Manage ranking strategies]**: read, create, edit, and delete ranking strategies.</li></ul>|
|Adobe Experience Platform|<ul><li>**[!DNL Sandbox]**: grant access to sandboxes.</li><li>**[!DNL Manage segments]**: read, create, edit, and delete segment definitions.</li><li>**[!DNL Manage profiles]**: read, create, edit, and delete profiles.</li><li>**[!DNL Read datasets]**: read-only access to datasets.</li><li>**[!DNL Read schemas]**: read-only access to schemas.</li><li>**[!DNL Read Identity namespace]**: read-only access to identity namespace.</li><li>**[!DNL Manage merge policies]**: read, create, edit, and delete merge policies.</li></ul>|

## [!DNL Campaign Approver] {#campaign-approver}

The **[!DNL Campaign Approver]** role allows users to approve deliveries and publish them. They can later check the success of their deliveries with the **[!DNL Campaigns]** reports. 

| Resources | Permissions|
|-|-|
|Campaigns| <ul><li>**[!DNL Manage campaigns]**: read, create, edit, and delete campaigns.</li><li>**[!DNL Publish campaigns]**: publish campaigns.</li><li>**[!DNL View Campaigns report]**: read, edit journey reports.</li></ul>|
|Decision management| <ul><li>**[!DNL Manage decisions]**: read, create, edit, and delete decisioning entities.</li><li>**[!DNL Manage ranking strategies]**: read, create, edit, and delete custom messages reports and use action features.</li></ul>|
|Adobe Experience Platform| <ul><li>**[!DNL Manage segments]**: read, create, edit, and delete segment definitions.</li><li>**[!DNL Manage profiles]**: read, create, edit, and delete profiles.</li><li>**[!DNL Read datasets]**: read-only access to datasets.</li><li>**[!DNL Read schemas]**: read-only access to schemas.</li><li>**[!DNL Manage merge policies]**: read, create, edit, and delete merge policies.</li></ul>|
|Channel configurations| <ul><li>**[!DNL View messages presets]**: read-only access to messages presets.</li></ul>|

## [!DNL Campaign Manager] {#campaign-manager}

The **[!DNL Campaign Manager]** role allows users to create and edit **[!UICONTROL Campaigns]** and every capability linked to **[!UICONTROL Campaigns]** but will not be able to publish them.

This role includes the following permissions:

| Resources | Permissions|
|-|-|
|Campaigns| <ul><li>**[!DNL Manage campaigns]**: read, create, edit, and delete campaigns.</li><li>**[!DNL View campaigns report]**: read, edit journey report.</li></ul>|
|Decision management| <ul><li>**[!DNL Manage decisions]**: read, create, edit, and delete decisioning entities.</li><li>**[!DNL Manage ranking strategies]**: read, create, edit, and delete custom messages reports and use action features.</li></ul>|
|Adobe Experience Platform| <ul><li> **[!DNL Manage segments]**: read, create, edit, and delete segment definitions.</li><li>**[!DNL Manage profiles]**: read, create, edit, and delete profiles.</li><li>**[!DNL Read datasets]**: read-only access to datasets.</li><li>**[!DNL Read schemas]**: read-only access to schemas.</li><li>**[!DNL Manage merge policies]**: read, create, edit, and delete merge policies.</li></ul>|
|Channel configurations| <ul><li>**[!DNL View messages presets]**: read-only access to messages presets.</li></ul>|

## [!DNL Campaign Viewer] {#campaign-viewer}

The **[!DNL Campaign Viewer]** role allows read-only access to the **[!UICONTROL Campaigns]** and **[!UICONTROL Decision management]** capabilities. 

Users assigned to this role will not be able to edit or publish. 

This role includes the following permissions:

| Resources | Permissions|
|-|-|
|Campaigns| <ul><li>**[!DNL View campaigns]**: read-only access to campaigns.</li><li>**[!DNL View campaigns report]**: read-only access to campaigns reports.</li></ul>|
|Decision management| <ul><li>**[!DNL View decisions]**: read-only access to decisions entities.</li></ul>|

## [!DNL Journey Administrator] {#journey-administrator}

The **[!DNL Journey Administrator]** role allows the administration menus with the possibility to manage and publish Journeys and Decision management. 

This role includes the following permissions:

| Resources | Permissions|
|-|-|
|Journeys| <ul><li> **[!DNL Manage journeys]**: read, create, edit, and delete journeys.</li><li>**[!DNL Publish journeys]**: publish journeys.</li><li>**[!DNL Manage journeys events, data sources and actions]**: read, create, edit, and delete events, sources or actions.</li><li>**[!DNL View journeys report]**: read and edit journeys report.</li></ul>|
|Channel configurations|<ul><li>**[!DNL Manage subdomains delegation]**: read, create, edit, and delete subdomain delegation.</li><li>**[!DNL Manage IP pools]**: read, create, edit, and delete ip pool.</li><li>**[!DNL Manage PTR records]**: read and edit PTR records.</li><li>**[!DNL View PTR records]**: read-only access to PTR records.</li><li>**[!DNL Manage messages presets]**: read, create, edit, and delete content branding.</li><li>**[!DNL Manage Landing page settings]**: create, edit and delete Landing page subdomains and Landing page presets.</li><li> **[!DNL Manage messages general settings]**: read, create, edit, and delete message general settings.</li><li>**[!DNL Manage SMS settings]**: create, edit and delete API credentials and SMS channel configurations required to enable SMS channel.</li><li>**[!DNL Manage suppression rules]**: access read, create, edit and delete suppression rules.</li><li>**[!DNL View suppression list]**: read and export local suppression list.</li><li>**[!DNL Manage alerts]**: enable/disable alerts for journeys and entitlements.</li></ul>|
|Decision management|<ul><li>**[!DNL Manage decisions]**: read, create, edit, and delete decisions.</li><li>**[!DNL Manage ranking strategies]**: read, create, edit, and delete ranking strategies.</li></ul>|
|Adobe Experience Platform|<ul><li>**[!DNL Sandbox]**: grant access to sandboxes.</li><li>**[!DNL Manage segments]**: read, create, edit, and delete segment definitions.</li><li>**[!DNL Manage profiles]**: read, create, edit, and delete profiles.</li><li>**[!DNL Read datasets]**: read-only access to datasets.</li><li>**[!DNL Read schemas]**: read-only access to schemas.</li><li>**[!DNL Read Identity namespace]**: read-only access to identity namespace.</li><li>**[!DNL Manage merge policies]**: read, create, edit, and delete merge policies.</li></ul>|
|Journey Optimizer Library|<ul><li>**[!DNL Manage Library Items]**: add and delete saved expressions in the [!DNL Journey Optimizer] Library.</li></ul>|
|Data Governance|<ul><li>**[!DNL Manage usage label]**: read, create, and delete usage labels.</li><li>**[!DNL Manage data usage policies]**: read, create, edit, and delete data usage policies.</li><li>**[!DNL View data usage policies]**: read-only access to data usage policies.</li><li>**[!DNL View user activity log]**: read and export audit logs.</li></ul>|

## [!DNL Journey Approver] {#journey-approver}

The **[!DNL Journey Approver]** role allows users to approve deliveries and publish them. They can later check the success of their deliveries with the **[!DNL Journey]** reports. 

This role includes the following permissions:

| Resources| Permissions|
|-|-|
|Journeys| <ul><li>**[!DNL Manage journeys]**: read, create, edit, and delete journeys.</li><li>**[!DNL Publish journey]**: publish journeys.</li><li>**[!DNL View journeys events, data sources and actions]**: read-only access to journey events, journey custom actions and journey data sources sources.</li><li>**[!DNL View journeys report]**: read, edit journey reports.</li></ul>|
|Decision management| <ul><li>**[!DNL Manage decisions]**: read, create, edit, and delete decisioning entities.</li><li>**[!DNL Manage ranking strategies]**: read, create, edit, and delete custom reports and use action features.</li></ul>|
|Adobe Experience Platform| <ul><li>**[!DNL Manage segments]**: read, create, edit, and delete segment definitions.</li><li>**[!DNL Manage profiles]**: read, create, edit, and delete profiles.</li><li>**[!DNL Read datasets]**: read-only access to datasets.</li><li>**[!DNL Read schemas]**: read-only access to schemas.</li><li>**[!DNL Manage merge policies]**: read, create, edit, and delete merge policies.</li></ul>|
|Channel configurations| <ul><li>**[!DNL View channel configurations]**: read-only access to channel configurations.</li></ul>|

## [!DNL Journey Manager] {#journey-manager}

The **[!DNL Journey Manager]** role allows users to create and edit **[!UICONTROL Journeys]** and every capability linked to **[!UICONTROL Journeys]** but will not be able to publish them.

This role includes the following permissions:

| Resources | Permissions|
|-|-|
|Journeys| <ul><li>**[!DNL Manage journeys]**: read, create, edit, and delete journeys.</li><li>**[!DNL View journeys events]**: read-only access to journey events, journey custom actions and journey data sources sources.</li><li>**[!DNL View journeys report]**: read, edit journey report.</li></ul>|
|Decision management| <ul><li>**[!DNL Manage decisions]**: read, create, edit, and delete decisioning entities.</li><li>**[!DNL Manage ranking strategies]**: read, create, edit, and delete custom reports and use action features.</li></ul>|
|Adobe Experience Platform| <ul><li> **[!DNL Manage segments]**: read, create, edit, and delete segment definitions.</li><li>**[!DNL Manage profiles]**: read, create, edit, and delete profiles.</li><li>**[!DNL Read datasets]**: read-only access to datasets.</li><li>**[!DNL Read schemas]**: read-only access to schemas.</li><li>**[!DNL Manage merge policies]**: read, create, edit, and delete merge policies.</li></ul>|
|Channel configurations| <ul><li>**[!DNL View channel configurations]**: read-only access to channel configurations.</li></ul>|

## [!DNL Journey Viewer] {#journey-viewer}

The **[!DNL Journey viewer]** role allows read-only access to the **[!UICONTROL Journeys]** and **[!UICONTROL Decision management]** capabilities. 

Users assigned to this role will not be able to edit or publish. 

This role includes the following permissions:

| Resources | Permissions|
|-|-|
|Journeys| <ul><li>**[!DNL View journeys]**: read-only access to journeys.</li><li>**[!DNL View journeys event, data sources, actions]**: read-only access to journeys events and data sources.</li><li>**[!DNL View journeys report]**: read-only access to journeys reports.</li></ul>|
|Decision management| <ul><li>**[!DNL View decisions]**: read-only access to decisions entities.</li></ul>|

## [!DNL Decisioning manager] {#decisioning-manager}

The **[!DNL Decisioning manager]** role only allows access to the **[!UICONTROL Decision management]** menu. Users assigned to this role will only be able to manage, view and publish decisions. 

This role includes the following permissions:

| Capability | Permissions|
|-|-|
|Decision management| <ul><li>**[!DNL Manage decisions]**: read, create, edit, and delete decisioning entities.</li><li>**[!DNL View decisions]**:  read-only access to decisioning entities.</li><li>**[!DNL Manage ranking strategies]**: read, create, edit, and delete custom reports and use action features.</li><li>**[!DNL Publish decisions]**: activate or deactivate decisioning activities.</li><!--li>**[!DNL Manage Experience decisions]**: read, create, edit, and delete Experience decisioning entities.</li--></ul>|

## [!DNL Content Library Manager] {#content-library-manager}
 
The **[!DNL Content Library Manager]** role only allows access to the **[!UICONTROL Content templates]** menu. Users assigned to this role will only be able to access the template library to create content without accessing the journeys or campaigns.

This role includes the following permissions:

| Capability | Permissions|
|-|-|
|Journey Optimizer Library| <ul><li>**[!DNL Manage library items]**: read, create, edit, and delete Journey Optimizer Library items, including content templates and fragments.</li><li>**[!DNL Manage simulate content]**: access to the **[!UICONTROL Simulate content]** option for preview and proof.</li><li>**[!DNL Publish Fragment]**: publish content fragments.</li></ul>|
|Decision management|<ul><li>**[!DNL Manage decisions]**: read, create, edit, and delete decisioning entities.</li><li>**[!DNL Manage ranking strategies]**: read, create, edit, and delete custom reports and use action features.</li></ul>|
|Adobe Experience Platform| <ul><li> **[!DNL Manage segments]**: read, create, edit, and delete segment definitions.</li><li>**[!DNL Manage profiles]**: read, create, edit, and delete profiles.</li><li>**[!DNL Read datasets]**: read-only access to datasets.</li><li>**[!DNL Read schemas]**: read-only access to schemas.</li><li>**[!DNL Manage merge policies]**: read, create, edit, and delete merge policies.</li></ul>|