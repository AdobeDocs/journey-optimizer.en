---
solution: Journey Optimizer
product: journey optimizer
title: Create multi-step campaigns with Journey Optimizer
description: Learn how to create a multi-step campaign with Adobe Journey Optimizer
hide: yes
hidefromtoc: yes
exl-id: 13da680d-fef8-4749-9190-8ca3d77b060a
---
# Create an orchestrated campaign {#create-first-campaign}

>[!CONTEXTUALHELP]
>id="ajo_campaign_creation_workflow"
>title="List of multi-step campaigns"
>abstract="The **multi-step** tab lists all multi-step campaign. Click the name of a multi-step campaign to edit it. Use the **Create multi-step campaign** button to add a new multi-step campaign."

## Prerequisites

### Permissions

### Settings

Overview of new admin settings> schemas, execution fields, merge policy. [Learn more](ms-schemas.md)


## Creation steps

To create a multi-step campaign, follow these steps:

1. To create a **multi-step campaign**, browse to the **Campaigns** menu.  

1. Click the **[!UICONTROL Create multi-step campaign]** button in the upper-right corner of the screen.

1. In multi-step campaign **Properties** dialog, select the template to use to create the multi-step campaign (you can also use the default built-in template). [Learn more about multi-step campaign templates](#campaign-templates).

1. Enter a label for the multi-step campaign. In addition, we strongly recommend you to add a description to your multi-step campaign, in the dedicated field of the **[!UICONTROL Additional options]** section of the screen.

1. Expand the **[!UICONTROL Additional options]** section to configure more settings for the multi-step campaign. 

1. Click the **[!UICONTROL Create multi-step campaign]** button to confirm the creation of your multi-step campaign.

Your multi-step campaign is now created and available in the list of worklows. You can now access its visual canvas and start adding, configuring, and orchestrating the tasks it will perform. [Learn how to orchestrate multi-step campaign activities](orchestrate-activities.md).

## Work with multi-step campaign templates {#campaign-templates}

>[!CONTEXTUALHELP]
>id="ajo_workflow_template_for_campaign"
>title="Multi-step campaign templates"
>abstract="Multi-step campaign templates contain pre-configured settings and activities which can be reused for creating new multi-step campaign."

>[!CONTEXTUALHELP]
>id="ajo_workflow_template_creation_properties"
>title="Multi-step campaign properties"
>abstract="Multi-step campaign templates contain pre-configured settings and activities which can be reused for creating new multi-step campaigns. In this screen, enter the label of the multi-step campaign template and configure its settings such as its internal name, folder and execution folders, timezone, and supervisor group."

Multi-step campaign templates contain pre-configured settings and activities which can be reused for creating new multi-step campaigns. You can select the template of your multi-step campaign from the multi-step campaign properties, when creating a multi-step campaign. An empty template is provided by default.

You can create a template from an existing multi-step campaign, or create a new template from scratch. Both methods are detailed below.

>[!BEGINTABS]

>[!TAB Create a template from an existing multi-step campaign]

To create a multi-step campaign template from an existing multi-step campaign, follow these steps:

1. Open to the **Campaign** menu and browse to the multi-step campaign to save as a template.
1. Click the three dots on the right of the name of the multi-step campaign, and choose **Copy as template**.
1. In the popup window, confirm the template creation.
1. In the multi-step campaign template canvas, check, add, and configure the activities as needed.
1. Browse to the settings, from the **Settings** button, to change the name of the multi-step campaign template, and enter a description.
1. Select the **folder** and **execution folder** of the template. The folder is the location where the multi-step campaign template is saved. The execution folder is the folder where multi-step campaigns created based on this template are saved.
1. Save your changes. 

The multi-step campaign template is now available in the template list. You can create a multi-step campaign based on this template. This multi-step campaign will be pre-configured with the settings and activities defined in the template.


>[!TAB Create a template from scratch]


To create a multi-step campaign template from scratch, follow these steps:

1. Open to the **Campaign** menu and browse to the **Templates** tab. You can see the list of available multi-step campaign templates.
1. Click the **[!UICONTROL Create template]** button in the upper-right corner of the screen.
1. Enter the label and open the additional options to enter a description of your multi-step campaign template.
1. Select the folder and execution folder of the template. The folder is the location where the multi-step campaign template is saved. The execution folder is the folder where multi-step campaigns created based on this template are saved.
1. Click the **Create** button to confirm your settings.
1. In the multi-step campaign template canvas, add and configure the activities as needed.

     ![](assets/wf-template-activities.png){zoomable="yes"}

1. Save your changes. 

The multi-step campaign template is now available in the template list. You can create a multi-step campaign based on this template. This multi-step campaign will be pre-configured with the settings and activities defined in the template.

>[!ENDTABS]
