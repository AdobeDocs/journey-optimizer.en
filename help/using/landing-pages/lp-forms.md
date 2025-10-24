---
solution: Journey Optimizer
product: journey optimizer
title: Create and use forms for you landing pages
description: Learn how to create and use forms for you landing pages in Journey Optimizer
feature: Landing Pages
topic: Content Management
role: User
level: Beginner
keywords: landing, landing page, creation, page, form
badge: label="Limited availability" type="Informative"
exl-id: c688ac5e-eb09-445b-a3f0-1627b40cddc8
---
# Use forms in your landing pages {#lp-forms}

>[!AVAILABILITY]
>
>This capability is currently in Limited Availability for customers in the United States and Australia. Contact your Adobe representative to gain access.

To capture profile data with your [!DNL Journey Optimizer] landing pages and enrich your [!DNL Experience Platform] datasets, you can leverage forms in your landing pages.

## Create a form preset {#create-form-preset}

>[!CONTEXTUALHELP]
>id="ajo_lp_form_connection"
>title="Select the endpoint to use"
>abstract="Define the streaming endpoint where data is sent upon submitting the form."
>additional-url="https://experienceleague.adobe.com/en/docs/experience-platform/sources/ui-tutorials/create/streaming/http" text="Create an HTTP API streaming connection"

>[!CONTEXTUALHELP]
>id="ajo_lp_form_dataset"
>title="Select a dataset"
>abstract="Define a dataset where the form responses will be stored and reflected. You can type to search a specific dataset or select it from the list."

Before being able to create a form, you need to create a dedicated preset where you select the connection endpoint where form submission data is sent, and the dataset where the data captured through the form will be stored.

Once data lands on the streaming endpoint, it is linked with the dataset information. Using the generated source/target connections and source flow, the data is then pushed into the dataset.

When creating a preset:

* You can set up multiple presets using different combinations of datasets and streaming connections.
* The same dataset or streaming connection can be reused across multiple presets.
* Each streaming connection automatically generates resources such as:
    * **Source connection** – where the data originates.
    * **Target connection** – where the data is stored or consumed.
    * **Source flow** – the pipeline that moves data from the source connection into [!DNL Experience Platform], handling mapping, transformation, and validation.

<!--
>[!NOTE]
>
> To access and edit form presets, you must have the **[!UICONTROL Manage form presets]** permission on the production sandbox. Learn more about permissions in [this section](../administration/high-low-permissions.md#administration-permissions).TBC
-->

To create a form preset, follow the steps below.

1. To access the **[!UICONTROL Form presets]** inventory, select **[!UICONTROL Administration]** > **[!UICONTROL Channels]** >**[!UICONTROL Form settings]** from the left menu.

1. Click **[!UICONTROL Create form preset]**.

1. Update the name to retrieve it more easily and add a description if needed.

    ![](assets/lp_create-form-preset.png){width=80%}

1. Select the **[!UICONTROL Streaming connection]** to use for that form. This is the streaming endpoint where data is sent upon submitting the form.

    >[!NOTE]
    >
    >Learn more on creating a streaming source connection in the [Experience Platform documentation](https://experienceleague.adobe.com/en/docs/experience-platform/sources/ui-tutorials/create/streaming/http){target="_blank"}.

1. Select a **[!UICONTROL Dataset]** to link with the form. This is where the form responses will be stored and reflected. You can type to search a specific dataset or select it from the list.

    >[!NOTE]
    >
    >Currently only [!DNL Adobe Experience Platform] datasets are available for selection. One dataset can be selected at a time. [Learn more on datasets](../data/get-started-datasets.md)

1. Click **[!UICONTROL Publish]**. Your preset is now ready to be used in a form.

## Access and manage forms {#access-forms}

To access the form list, select **[!UICONTROL Content Management]** > **[!UICONTROL Forms]** from the left menu.

All the existing forms are displayed. You can filter forms based on their status, creation or modification date.

![](assets/lp_form-list.png)
    
## Create and design a form {#create-form}

>[!CONTEXTUALHELP]
>id="ajo_lp_form_preset"
>title="Select a preset"
>abstract="Choose a predefined preset that contains the connection to be used and a predefined dataset for your form."
>additional-url="https://experienceleague.adobe.com/en/docs/journey-optimizer/using/content-management/landing-pages/lp-forms#create-form-preset" text="Create a form preset"

To create a form, follow the steps below.

1. From the **[!UICONTROL Forms]** list, click **[!UICONTROL Create form]**.

1. Add a name. You can add a description if needed.

    ![](assets/lp_create-form.png)

1. Select a **[!UICONTROL Preset]** that contains the connection to be used and a predefined dataset for your form. [Learn how to create a form preset](#create-form-preset)

1. Click **[!UICONTROL Create]**. The form designer opens, which enables you to add structures and content [components](../email/content-components.md#add-content-components) to build your content. You can use [Text](../email/content-components.md#text) and **[!UICONTROL Field]** components.

1. To capture profile data and attributes, add specific fields to your form. [Learn more](#define-fields)

1. Configure and design these fields. [Learn more](#configure-fields)

1. You can adjust the form's layout, styling and dimensions as needed using the **[!UICONTROL Styles]** pane. [Learn more on styling](../email/get-started-email-style.md)

1. Once you configured all the fields, click **[!UICONTROL Save & close]**.

1. Configure the Thank you page. [Learn how](#thank-you-page)

1. **[!UICONTROL Publish]** the form to make it available for selection in landing pages.

### Define specific fields {#define-fields}

To add specific fields to your form, drag and drop a structure into the canvas, and drag a **[!UICONTROL Field]** component inside.<!--**[!UICONTROL Select field attribute]** or **[!UICONTROL Add custom field]**.-->

![](assets/lp_create-form-field.png)

Then select one of the following options:

>[!BEGINTABS]

>[!TAB Select field attribute]

Use this option to select an attribute based on the dataset schema linked to your form.
    
>[!NOTE]
>
>The dataset is defined in the preset selected for your form. [Learn more](#create-form-preset)

![](assets/lp_select-field-attribute.png){width=100%}

For example, you can set the Email and Person ID. When users fill in these fields, the information entered is saved to the selected dataset.

![](assets/lp_create-form-field-attributes.png){width=55%}

To map the collected data with a Profile, select a profile identity field. The identity fields are marked as **[!UICONTROL Required]** in the attribute list - you can filter on them.
    
![](assets/lp_create-form-required-attributes.png){width=65%}

>[!TAB Add custom field]

With this option, you can just define a free field without mapping it to a field in the linked dataset.

![](assets/lp_create-form-custom-field.png){width=85%}

>[!ENDTABS]

### Configure and design a field {#configure-fields}

Once you selected a field attribute or added a custom field, you can further adjust its details as well as its behavior upon submitting the form.

1. In the **[!UICONTROL Field details]** section of the **[!UICONTROL Content]** tab on the right, you can specify the following elements as needed:

    * Adjust the **[!UICONTROL Label]** to make it clear for the recipients of your form.
    * Change the **[!UICONTROL Field type]** according to your needs. It can be a checkbox, currency, date, slider, URL, etc.

        >[!NOTE]
        >
        >The other field details may vary according to the selected field type.

    * Add a **[!UICONTROL Placeholder]**.<!--To explain-->
    * Specify **[!UICONTROL Instructions]**.<!--How will they be displayed in the form? To explain-->
    * Enter a **[!UICONTROL Default value]** which will be displayed before the users of your form fill in the field.
    * You can define a custom **[!UICONTROL Validation message]**.
    * Set a **[!UICONTROL Maximum length]**. An error message displays if the recipients of the form exceeds the limit when filling in the field.

    ![](assets/lp_create-form-field-details.png){width=85%}

1. In the **[!UICONTROL Field behaviors]** section, you can define the following:

    * Select **[!UICONTROL Required]** to make this field compulsory. If users do not fill in the field, they cannot submit the form.
    * Select **[!UICONTROL Sensitive]** to make the field case-sensitive. <!--To confirm - do you mean retain capitalization when added to the dataset?-->
    * Select **[!UICONTROL Prefilled Enabled]** to populate the field from the profile information if available.<!--Even for a custom field, or a field not mapped to a profile? What happens if no data is available?-->
    * Select **[!UICONTROL Enable input mask]** to replace users' input with generic characters. You can use *9* to mean any number, *a* to mean any letter, or * to mean any number or letter.<!--Not sure how you define that in the form-->

    ![](assets/lp_create-form-field-behaviors.png){width=75%}

### Configure the Thank you page {#thank-you-page}

>[!CONTEXTUALHELP]
>id="ajo_lp_forms_thankyou_page"
>title="Thank you page"
>abstract="Configure what happens when someone fills out or forwards the form."

Back in the form details, from the **[!UICONTROL Thank you page]** section, configure what happens when a user fills out the form.

![](assets/lp_create-form-thank-you.png){width=70%}

Set up one of the following actions:

* **[!UICONTROL Stay on page]** - This option keeps the visitor on the same page when the form has been submitted.
* **[!UICONTROL Landing page]** - Select a published [landing page](create-lp.md) to which the user is redirected after submitting the form.
* **[!UICONTROL External URL]** - Enter the full URL you want as the follow-up page. Once the user has submitted the form, they are directed to the URL specified.
* **[!UICONTROL Conditional redirect]** - Set up rules to dynamically show different follow-up actions based on the form responses.

    You can define a rule for each specific audience. For example, you can display a specific landing page for US residents, another page for Canada residents, and so on. Finally, set up a default action for users who do not fall in any rule that you defined.

    >[!NOTE]
    >
    >The conditions defined in a rule are read sequentially.

    ![](assets/lp_create-form-thank-you-conditional.png){width=40%}

## Edit a published form {#edit-form}

Once a form is published, you can still edit it. Follow the steps below.

1. Access the [form list](#access-forms) and select a published form.

1. Click the **[!UICONTROL Edit form]** button.

    ![](assets/lp_edit-form-button.png){width=90%}

1. A new version of the form is created with the draft status. Click **[!UICONTROL Create draft version]**.

1. Update the form as needed and click **[!UICONTROL Save]**. The form has now the **[!UICONTROL Published (with draft)]** status:

    * The current version continues to have the **[!UICONTROL Published]** status, until you publish the updated version.

    * The updated version has the **[!UICONTROL Draft]** status.

1. Back in the form summary, you can navigate between the two versions of the form.

    ![](assets/lp_published-with-draft-form.png){width=70%}

1. In the **[!UICONTROL Draft]** section, you can either publish or discard the draft, as well as edit the details or content of the form.

    ![](assets/lp_edit-draft-form.png){width=75%}

## Leverage the form in a landing page {#leverage-form-in-lp}

You can now embed this form into a landing page in order to capture data corresponding to the attributes you defined in the form, and save it into the selected dataset. Follow the steps below.

1. Create a landing page. [Learn how](create-lp.md#create-landing-page)

1. Select **[!UICONTROL Data Capture]** as the landing page type and click **[!UICONTROL Create]**.

    ![](assets/lp_create-lp-data-capture.png){width=65%}

1. Configure the primary page. [Learn how](create-lp.md#configure-primary-page)

1. Open the [landing page designer](design-lp.md).

1. Drag and drop a **[!UICONTROL Structure component]** into your content. Drag and drop a **[!UICONTROL Form]** component into that structure.

    >[!NOTE]
    >
    >Only published forms can be selected in a landing page.

1. In the **[!UICONTROL Embed form]** section, select the form that you created.

    ![](assets/lp_embed-form.png)

    >[!NOTE]
    >
    >You can update the selected form using the **[!UICONTROL Edit form]** button. The form opens in a new tab. The steps to edit the form content are detailed in [this section](#create-form).

1. In the **[!UICONTROL Follow up type]** section, configure what happens when a user fills out the form:

    * Choose **[!UICONTROL Form defined]** to select the action that was defined in the embeded form. [Learn more](#thank-you-page)

    * You can also select a published [landing page](create-lp.md) to which the user is redirected after submitting the form.

    * Or define an **[!UICONTROL External URL]** as the follow-up page where users are directed when they submit the form.

1. Save and test your landing page. [Learn how](create-lp.md#test-landing-page)

Once your landing page is [published](create-lp.md#publish-landing-page) and used in a journey, when users fills in the form, the information entered is ingested into the selected dataset.

>[!NOTE]
>
>If you unpublish a form that is used in a landing page, edit this form and publish it again, the landing page is always using the latest published version of the form.
