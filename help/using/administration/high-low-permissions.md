---
solution: Journey Optimizer
product: journey optimizer
title: Permission levels
description: Learn about high and low level permissions allowing users to access the different features.
topic: Administration
feature: Access Management
role: Admin, Architect, Developer
level: Experienced
keywords: permission, high level, low level, profile, admin console
exl-id: 1b286f9d-43ef-4b80-b4ee-136da857bb95
---
# Permission levels {#high-low-permissions}

![](assets/do-not-localize/permissions.png)

Each role is composed of permissions allowing users to access the different features. 
They can be divided into two types:

* **High-level permission**: represents the different permissions that can be assigned to **[!UICONTROL Role]**, such as **[!DNL Publish journeys]** and **[!DNL Manage subdomains delegation]**. High level permissions encompass low level permissions. High level permissions are detailed in [this page](ootb-permissions.md).

* **Low-level permission**: represents the different permissions that come from the high level permission.

For example, the **[!DNL Journey administrator]** role is assigned the **[!DNL Manage journeys]** permission. From this permission results the low-level permissions which will allow the Journey administrator to write, read and delete journeys.

## Journey resource {#journey-capability}

* **[!DNL Manage journeys]** high-level permission allows users to create new and edit/delete existing Journeys, as well as access to the objects that are used in the journey canvas to build the journey flow.

  +++ It includes the following low-level permissions:  

    * Journey Optimizer specific:

      * journeys.read
      * journeys.write
      * journeys.delete
      * messages.read

    * Adobe Experience Platform specific:

      * segments.read
      * profiles.read
      * datasets.read
      * schemas.read

  +++

* **[!DNL Publish journeys]** high-level permission allows users to publish journeys.

  +++ It includes the following low-level permissions:  
    * Journey Optimizer specific:
      * journeys.publish
      * journeys.read

  +++

* **[!DNL View journeys]** high-level permission allows users to browse and view journeys.

  +++ It includes the following low-level permissions:  

    * Journey Optimizer specific:
      * journeys.read

    * Adobe Experience Platform specific:
      * segments.read
      * profiles.read

  +++

* **[!DNL Manage journeys events, data sources and actions]** high-level permission allows users to configure event and data configurations.

  +++ It includes the following low-level permissions:  

  * Journey Optimizer specific:
    * journeys_events.read
    * journeys_events.write
    * journeys_events.delete
    * journeys_data_sources.read
    * journeys_data_sources.write
    * journeys_data_sources.delete 
    * journeys_actions.read
    * journeys_actions.write
    * journeys_actions.delete

  * Adobe Experience Platform specific:
    * schemas.read
    * datasets.read
    * identity_namespace.read

  +++

* **[!DNL View journeys events, data sources and actions]** high-level permission allows users to use event and data in the journey flow.

  +++ It includes the following low-level permissions:  

  * Journey Optimizer specific: 
    * journeys_events.read
    * journeys_data_sources.read
    * journeys_actions.read

  * Adobe Experience Platform specific:
    *  schemas.read
    * datasets.read
    * identity_namespace.read

  +++

* **[!DNL View journeys report]** high-level permission allows users to read-only journey report.

  +++ It includes the following low-level permissions:  

  * Journey Optimizer specific: 
    * journeys_report.read
    * messages_report.read

  * Adobe Experience Platform specific:
    * datasets.read
    * queries.read
    * queries.write
    * queries.delete

  +++

## Journey Optimizer rules resource {#journey-rules-capability}

* **[!DNL Manage frequency rules]** high-level permission allows users to read, create, edit, delete and activate/deactivate frequency rules.

  +++ It includes the following low-level permissions:  

  * Journey Optimizer specific: 
    * frequency_rules.read
    * frequency_rules.write
    * frequency_rules.delete

  +++

* **[!DNL View frequency rules]** high-level permission allows users to view frequency rules. 

  +++ It includes the following low-level permissions:  

  * Journey Optimizer specific: 
    * frequency_rules.read

  +++

## Campaign resource {#campaign-capability}

* **[!DNL Export suppression list]** high-level permission allows users to download the suppression list as a CSV file.

  +++ It includes the following low-level permissions: 

  * Journey Optimizer specific: 
    * suppression_list.export

  * Adobe Experience Platform specific:
    * profiles.read
    * datasets.read

  +++

* **[!DNL Manage campaigns]** high-level permission allows users to create new and edit/delete Campaigns

  +++ It includes the following low-level permissions:  

    * Journey Optimizer specific:

      * campaign.read
      * campaign.write
      * campaign.delete
      <!--* experiments.read
      * experiments.write
      * experiments.delete-->

  +++

* **[!DNL Publish campaigns]** high-level permission allows users to publish campaigns.

  +++ It includes the following low-level permissions:

    * Journey Optimizer specific:

      * campaign-read
      * campaign-publish
      <!--* experiments.activate-->

  +++

* **[!DNL View campaigns report]** high-level permission allows users to read and edit campaigns report.

  +++ It includes the following low-level permissions:  

    * Journey Optimizer specific:
      * campaign.read
      * campaign-report.read
      <!--* experiments.read
      * experiments_report.read-->

  +++

## Decision management resource {#decisions-permissions}

* **[!DNL Manage decisions]** high-level permission allows users to create new and edit/delete existing **[!DNL Activity entities]**, as well as manage the objects that are used in those activities to make the decisions.

  +++ It includes the following low-level permissions:  

  * Decision management specific:
    * activities.read
    * activities.write
    * activities.delete
    * offers.read
    * offers.write
    * offers.delete
    * placements.read
    * placements.write
    * placements.delete
    * ranking_strategy.read

  * Adobe Experience Platform specific:
    * datasets.read
    * datasets.write
    * datasets.delete
    * schemas.read
    * profile.read
    * segments.read

  +++

* **[!DNL View decisions]** high-level permission allows users to use an existing Activity and related business objects to make the decisions. 

  +++ It includes the following low-level permissions:  

  * Decision management specific: 
    * activities.read
    * offers.read
    * placements.read
    * ranking_strategy.read

  * Adobe Experience Platform specific:
    * schemas.read
    * segment.read
    * datasets.read
    * datasets.write
    * datasets.delete

  +++

* **[!DNL Manage offers]** high-level permission allows users to create, edit and delete all offers, components, read decisions and collections.

  +++ It includes the following low-level permissions:  

  * Decision management specific:
    * offers_activity.read
    * offers.read
    * offers.Write
    * offers.Delete
    * placements.Read
    * placements.Write
    * placements.Delete
    * ranking_strategy.read

  * Adobe Experience Platform specific:
    * schemas.read
    * segment.read 
    * datasets.read
    * profiles.read

  +++

* **[!DNL Manage ranking strategies]** high-level permission allows users to read, create, edit, and delete ranking strategies.

  +++ It includes the following low-level permissions:  

  * Decision management specific:
    * ranking_strategy.read
    * ranking_strategy.write
    * ranking_strategy.delete
    * activities.read
    * offers.read
    * placements.read

  +++

## Channel configurations resource {#administration-permissions} 

<!--
* **[!DNL Manage Experience decisions]** high-level permission allows users to read, create, edit, and delete Experience decisioning entities.

  +++ It includes the following low-level permissions:  

  * Experience decisions specific:
    * ranking_strategy.read
    * offeritem.read
    * offeritem.write
    * offeritem.delete
    * itemCollection.read
    * itemCollection.write
    * itemCollection.delete
    * SelectionStrategy.read
    * SelectionStrategy.write
    * SelectionStrategy.delete
    * Decisionpolicy.read
    * Decisionpolicy.write
    * Decisionpolicy.delete
  +++
-->

* **[!DNL Manage file routing]** high-level permission allows users to create, edit and delete file routing configurations.

  +++ It includes the following low-level permissions:  
  * Journey Optimizer specific: 

    * file_routing.read
    * file_routing.write
    * file_routing.delete

  +++

* **[!DNL Manage IP pools]** high-level permission allows users to create, edit and delete the affinity definition.

  +++ It includes the following low-level permissions:  
  * Journey Optimizer specific: 
    * IP_pools.read
    * IP_pools.write
    * IP_pools.delete

  +++

* **[!DNL Manage landing page settings]** high-level permission allows users to read, create and edit landing page subdomains and preset settings.

  +++ It includes the following low-level permissions: 

  * Journey Optimizer specific:

    * landing_page_subdomain.read
    * landing_page_subdomain.write
    * landing_page_subdomain.delete
    * landing_page_preset.read
    * landing_page_preset.write
    * landing_page_preset.delete

  +++

* **[!DNL Manage messages general settings]** high-level permission allows users to create, edit and delete global settings at the sandbox level.

  +++ It includes the following low-level permissions:  

  * Journey Optimizer specific: 
    * messages_general_settings.read
    * messages_general_settings.write
    * messages_general_settings.delete

  * Adobe Experience Platform specific:
    * schemas.read

  +++

* **[!DNL Manage messages presets]** high-level permission allows users to read, create, edit, and delete channel configurations across channels at the sandbox level.

  +++ It includes the following low-level permissions: 

  * Journey Optimizer specific: 
    * messages_presets.read
    * messages_presets.write
    * messages_presets.delete
    * subdomains_delegation.read
    * IP_pools.read

  * Data Collection specific:
    * Mobile_setting.read <!--(from Adobe Experience Platform Launch)-->

  +++

* **[!DNL Manage PTR records]** high-level permission allows users to read and edit PTR records that have been configured based on the subdomain.

  +++ It includes the following low-level permissions: 

  * Journey Optimizer specific: 
    * PTR_records.read
    * PTR_records.write
    * subdomains_delegation.read

  +++

* **[!DNL Manage Seedlist]** high-level permission allows users to read, create, edit and delete Seedlist.

  +++ It includes the following low-level permissions: 

  * Journey Optimizer specific: 
    * seedlist.read
    * seedlist.write
    * seedlist.delete

  +++

* **[!DNL Manage SMS subdomains]** high-level permission allows users to read, create, edit and delete SMS subdomains.

  +++ It includes the following low-level permissions: 

  * Journey Optimizer specific: 
    * sms_subdomains.read
    * sms_subdomains.write
    * sms_subdomains.delete

  +++

* **[!DNL Manage subdomains delegations]** high-level permission allows users to create, edit and delete subdomain delegations (including IP pool).

  +++ It includes the following low-level permissions:  
  * Journey Optimizer specific: 

    * subdomains_delegation.read
    * subdomains_delegation.write
    * subdomains_delegation.delete

  +++

* **[!DNL Manage suppression]** high-level permission allows users to define the number of bounces before an email address is added to the suppression list, as well as to add and delete entries to/from the suppression list.

  +++ It includes the following low-level permissions:  
  * Journey Optimizer specific: 
    * suppression_rules.read
    * suppression_rules.write
    * suppression_rules.delete
    * suppression_list.write
    * suppression_list.delete

  +++

* **[!DNL View file routing]** high-level permission allows users to view file routing configurations.

  +++ It includes the following low-level permissions:  
  * Journey Optimizer specific: 

    * file_routing.read

  +++

* **[!DNL View messages general settings]** high-level permission allows users to view messages general settings such as the execution address.

  +++ It includes the following low-level permissions: 

  * Journey Optimizer specific: 
    * messages_general_settings.read

  * Adobe Experience Platform specific: 
    * schemas.read

  +++

* **[!DNL View messages presets]** high-level permission allows users to view messages presets.

  +++ It includes the following low-level permissions: 

  * Journey Optimizer specific: 
    * messages_presets.read
    * subdomains_delegation.read
    * IP_pools.read

  * Data Collection specific:
    * Mobile_setting.read

  +++

* **[!DNL View PTR records]** high-level permission allows users to view PTR records that have been configured based on the subdomain.

  +++ It includes the following low-level permissions: 
  * Journey Optimizer specific: 

    * PTR_records.read
    * subdomains_delegation.read

  +++

<!--
### [!DNL View channel configuration] permission {#view-channel-surface}

The **[!DNL View channel configuration]** high-level permission allows users to view channel configurations in order to know which channel configurations to use. 
  +++ It includes the following low-level permissions:  

* messages_presets.read
* subdomains_delegation.read
* IP_pools.read
* mobile_setting.read (from Adobe Experience Platform Data Collection)
-->


* **[!DNL View suppression list]** high-level permission allows users to view the suppression list content and settings.

  +++ It includes the following low-level permissions:  

  * Journey Optimizer specific: 
    * suppression_list.view

  * Adobe Experience Platform specific:
    * profiles.read
    * datasets.read

  +++

<!--
### Manage web subdomain permission {#web-subdomain}

The **[!DNL Manage web subdomain]** high-level permission allows users to read, create, edit, and delete web subdomains.

  +++ It includes the following low-level permissions: 
-->

## AI assistance resource {#ai-permissions} 

* **[!DNL Generate content]** high-level permission allows users to access to the AI assistant in Journey Optimizer for Content acceleration.

  +++ It includes the following low-level permission:  

  * Journey Optimizer specific: 
    * ai-assistant-generated-content.generate

  +++
