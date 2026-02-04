---
solution: Journey Optimizer
product: journey optimizer
title: Copy Journey Optimizer objects between sandboxes
description: Learn how to copy journeys, content templates and fragments between sandboxes.
feature: Journeys, Sandboxes
topic: Content Management
role: User, Developer
level: Experienced
keywords: sandbox, journey, copy, environment
exl-id: 356d56a5-9a90-4eba-9875-c7ba96967da9
---
# Export objects to another sandbox {#copy-to-sandbox}

You can copy objects such as journeys, custom actions, content templates, or fragments, across multiple sandboxes by using package export and import capabilities. A package can consist of a single object or multiple objects. Any objects that are included in a package must be from the same sandbox. 

This page describes the Sandbox tooling use case in the context of Journey Optimizer. For more information on the feature itself, refer to the Adobe Experience Platform [Sandbox tooling guide](https://experienceleague.adobe.com/docs/experience-platform/sandbox/ui/sandbox-tooling.html#abobe-journey-optimizer-objects){target="_blank"}.

>[!NOTE]
>
>This feature requires the following permissions from the **Sandbox administration** capability: Manage sandboxes (or View sandboxes) and Manage packages. [Learn more](../administration/ootb-permissions.md)

The copy process is carried via a package export and import between the source and target sandboxes. Here are the general steps to copy a journey from one sandbox to another:

1. [Add the object to export as a package in the source sandbox](#export) 
1. [Publish the package](#publish)
1. [Import the package in the target sandbox](#import)

>[!NOTE]
>
>For migrating Decision management objects to Decisioning, use the dedicated [Decisioning Migration API](../experience-decisioning/decisioning-migration-api.md) which provides automated dependency resolution and rollback capabilities specifically designed for decisioning entity migration.

## Exported objects & best practices {#objects}

Journey Optimizer allows the export of journeys, custom actions, content templates, fragments and other objects to another sandbox. The following sections provide information and best practices for each type of object.

### General best practices {#global}

* When copying an object, any dependencies (such as nested fragments, journey audiences, or actions) are correctly updated in the parent object, ensuring proper mapping in the target sandbox.

* If an exported object contains profile personalization, make sure that the appropriate schema exists in the target sandbox to avoid any personalization issue.

* Landing pages are not currently supported for migration between sandboxes. When you copy a journey to another sandbox, any references to landing pages in your journey or email content will still point to the original (source) sandbox landing page IDs. After the migration, you must manually update all landing page references in your journey and email content to use the correct landing page IDs from the target (destination) sandbox. See [Create and publish landing pages](../landing-pages/create-lp.md).

+++ Journeys

* **Copied dependencies** - When exporting a journey, in addition to the journey itself, Journey Optimizer also copies most of the objects the journey depends on: audiences, custom actions, schemas, events and actions. For more details on copied objects, refer to the Adobe Experience Platform [Sandbox tooling guide](https://experienceleague.adobe.com/docs/experience-platform/sandbox/ui/sandbox-tooling.html#abobe-journey-optimizer-objects){target="_blank"}.

* **Manual validation recommended** - We do not guarantee that all linked elements are copied to the destination sandbox. We strongly recommend that you perform a thorough check, for example before publishing a journey. This allows you to identify any potential missing object. 

* **Draft mode and uniqueness** - The copied objects in the target sandbox are unique and there is no risk of overwriting existing elements. Both the journey and any messages inside the journey are brought over in draft mode. This allows you to perform a thorough validation before publication on the target sandbox.

* **Metadata** - The copy process only copies over the metadata about the journey and the objects in that Journey. No profile or dataset data is being copied as part of this process. 

* **Custom actions**

   * When exporting custom actions, URL configuration and payload parameters are copied over. However, for security reasons, authentication parameters are not copied over and, instead, are replaced by "INSERT SECRET HERE". Constant request header & query param values are also replaced by "INSERT SECRET HERE".

      This includes the special-purpose custom actions ([!DNL Adobe Campaign Standard], [!DNL Campaign Classic], [!DNL Marketo Engage]).

   * When copying a journey to another sandbox, if you select "use existing" for a custom action during the import process, the existing custom action you select must be the same as the source custom action (i.e., same configuration, parameters, etc.). Otherwise, the new journey copy will have errors that cannot be resolved in the canvas.

* **Data sources, field groups and events** - When copying a journey that uses events, data sources, or field groups, the import process automatically checks whether components with the same name and type already exist in the target sandbox. For example, a unitary event will be replaced by a unitary event in the target sandbox with the same name. The same applies to business events, custom data sources, and both API-based and schema-based field groups used in journeys. If a unitary event from source sandbox has the same name as a business event destination sandbox, it is not copied nor created - This applies to all other components too.

+++

+++ Campaigns

Campaigns are copied along with all items related to the profile, audience, schema, inline messages, and dependent objects. However, the following items are **not** copied:

* Multi-lingual variants and language settings,
* Business rules,
* Tags,
* Data Usage Labelling and Enforcement (DULE) labels.

When copying campaigns, ensure that the object listed below are validated in the target sandbox to avoid misconfigurations:

* **Channel configurations**: Channel configurations are copied along with campaigns. After campaigns are copied, channel configurations must be selected manually in the target sandbox.
* **Experimentation variants and settings**: Experiment variants and settings are included in the campaign copy process. Validate these settings in the target sandbox after import.
* **Unified decisioning**: Decision policies and decision items are supported for export and import. Ensure that decision-related dependencies are correctly mapped in the target sandbox.

+++

+++ Decisioning

* The objects below must be present in the destination sandbox before copying Decisioning objects:

   * Profile Attributes used across Decisioning objects,
   * The field group of custom Offer Attributes,
   * The schemas of Datastreams used for Context Attributes across Rules, Ranking or Capping.

* Sandbox copy for ranking formulas with AI Models is currently not supported.

* When copying a campaign, decision items (offer items) are not copied along automatically. Make sure you copy them individually using the "Add to Package" option".

* If a Decision Policy has a selection strategy, decision items must be added separately. If it has manual/fallback decision items, they are added as direct dependencies automatically.

* When copying Decisioning entities, make sure you copy decision items **before** any other object. For example, if you copy a collection first, and there are no offers in the new sandbox, then that new collection will remain empty.

* When copying entities with dependencies (e.g., schema, segments), click "Create New" against the entity to unselect it and reveal the "Use Existing" option for dependent artifacts. Additional dependencies may require repeating this step further down the hierarchy.

   Example: While importing a campaign, to reuse a datastream schema in a rule, click "Create New" against DECISIONING_STRATEGY, then again on DECISIONING_RULES, to reveal the "Use Existing" option for the datastream schema.

* For entities dependent on a datastream context schema, ensure the datastream is created beforehand and select an existing schema for that datastream.

* If you directly click "Finish" while importing, all dependencies will be created anew.

+++

+++ Content templates

* When exporting a content template, all nested fragments are also copied along with it.

* Exporting content templates can sometimes result in fragment duplication. For example, if two templates share the same fragment and are copied in separate packages, both templates will need to reuse the same fragment in the target sandbox. To avoid duplication, select the "Use existing" option during the import process. [Learn how to import a package](#import)

* To further avoid duplication, it is recommended to export content templates in a single package. This ensures the system manages deduplication efficiently.

+++

+++ Fragments

* Fragments can have multiple statuses such as Live, Draft and Live with draft in progress. When exporting a fragment, its latest Draft state is copied to the target sandbox.

* When exporting a fragment, all nested Fragments are also copied along with it.

+++

## Add objects as a package {#export}

To copy objects to another sandbox, you first need to add them as a package in the source sandbox. Follow these steps:

1. Navigate to the inventory where the first object you want to copy is stored, such as the journeys list. Click the **More actions** icon (the three dots next to the object name) and click **Add to package**.

   ![](assets/journey-sandbox1.png)

1. In the **Add to package** window, choose if you want to add the object to an existing package or create a new package:

   ![](assets/journey-sandbox2.png)

   * **Existing package**: select the package from the drop-down menu.
   * **Create a new package**: type the package name. You can also add a description.

1. Repeat these steps to add all the objects you want to export with your package.

## Publish the package to export {#publish}

Once your package is ready to be exported, follow these steps to publish it:

1. Navigate to the **[!UICONTROL Administration]** > **[!UICONTROL Sandboxes]** menu, select the **Packages** tab.

1. Open the package you want to export, select the objects you want to export and click **Publish**.

   In this example, we want to export a journey, a content template and a fragment.

   ![](assets/journey-sandbox4.png)

1. To track the status of the package's publication from the **[!UICONTROL Jobs]** tab. For more details on a job, select it from the list and click the **[!UICONTROL View import details]** button.

   ![](assets/journey-sandbox9.png)

## Import the package in the target sandbox {#import}

Once the package is published, you need to import it into the target sandbox. Follow these steps:

1. Navigate to the **[!UICONTROL Sandboxes]** menu and select the **[!UICONTROL Browse]** tab.

1. Search for the sandbox where you want to import the package, then click the + icon next to its name.

   ![](assets/journey-sandbox5.png)

   >[!NOTE]
   >
   >Only sandboxes within your organization are available.

1. In the **Target sandbox** field, check that the correct target sandboxes is selected and select the package to import from the **[!UICONTROL Package name]** drop-down list. Click **Next**. 

   ![](assets/journey-sandbox6.png)

1. Review the package objects and dependencies. This is the list of objects that have been added to the package, along with other objects journeys depend on such as audiences, schemas, events or actions. 

   For each object, you can choose to create a new one or use an existing one in the target sandbox. This allows you, for example, to avoid fragment duplication which may happen when importing content templates using common fragments.

   ![](assets/journey-sandbox7.png)

1. Click the **Finish** button, in the top-right corner to start copying the package to the target sandbox. The copying process varies based on the complexity of the objects and how many objects need to be copied over. 

1. Click the import job to review the copy result:

   * Click the **View imported objects** button to display each individual object copied. 
   * Click the **View import details** button to check the import results for each object.

   ![](assets/journey-sandbox8.png)

1. Access your target sandbox and perform a thorough check of all the copied objects.
