---
solution: Journey Optimizer
product: journey optimizer
title: AEM Content Fragments
description: Learn how to access & manage AEM Content Fragments
topic: Content Management
role: User
level: Beginner
exl-id: 57d7c25f-7e39-46ad-85c1-65e2c18e2686
---
# # Work with Adobe Experience Manager Content Fragments {#aem-fragments}

The integration between Adobe Experience Manager and Journey Optimizer follows this data flow:

1. **[Configure the Dispatcher](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/sites/administering/content-fragments/content-fragments-with-journey-optimizer#dispatcher-configuration)**: To enable Journey Optimizer to access Adobe Experience Manager Content Fragments via the Content Fragment Management API, you must first configure the Dispatcher. This is a prerequisite for the integration.

1. **[Create and author](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/sites/administering/content-fragments/managing#creating-a-content-fragment)**: Content is created and configured in Adobe Experience Manager as Content Fragments.

1. **[Tagging](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/sites/administering/content-fragments/managing#manage-tags)**: Content Fragments must be tagged with the Journey Optimizer-specific tag (`ajo-enabled:{OrgId}/{SandboxName}`).

1. **[Publish](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/sites/administering/content-fragments/managing#publishing-and-previewing-a-fragment)**: Content Fragments are published in Adobe Experience Manager, making them available to Journey Optimizer.

1. **[Access](#aem-add)**: Journey Optimizer fetches and displays available Content Fragments from Adobe Experience Manager publish instance in real-time.

1. **[Integration](#aem-add)**: Content Fragments are selected and integrated into campaigns or journeys.

When a Content Fragment is published in Adobe Experience Manager, an event is sent to update the content on the Journey Optimizer side. If the update is successful, the Content Fragment becomes available within approximately 5 minutes for Unitary journeys, and in the next processing batch for batch use cases. Once the update is available in Journey Optimizer, the latest published content is used across all applicable campaigns and journeys.

>[!AVAILABILITY]
>
>For Healthcare customers, the integration is enabled only upon licensing the Journey Optimizer Healthcare Shield and Adobe Experience Manager Extended Security for Healthcare add-on offerings.

## Create and assign a tag in Experience Manager

>[!IMPORTANT]
>
>To enable Journey Optimizer to access Adobe Experience Manager Content Fragments via the Content Fragment Management API, you must first [configure the Dispatcher](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/sites/administering/content-fragments/content-fragments-with-journey-optimizer#dispatcher-configuration).

Before using your Content fragment in Journey Optimizer, you need to create a tag specifically for Journey Optimizer:

1. Access your **Experience Manager** environment.

1. From the **Tools** menu, select **Tagging**.

    ![](assets/do-not-localize/aem_tag_1.png)

1. Click **Create Tag**.

1. Ensure the ID adheres to the following syntax: `ajo-enabled:{AJO-OrgId}/{AJO-SandboxName}`.

1. Click **Create**. 

1. Define your Content Fragment Model as detailed in [Experience Manager documentation](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/sites/administering/content-fragments/content-fragment-models){target="_blank"} and assign your newly created Journey Optimizer tag.

This real-time connection ensures that your content is always up-to-date but also means that any changes to published fragments will immediately affect active campaigns and journeys.

You can now begin creating and configuring your Content Fragment for later use in Journey Optimizer. Learn more in [Experience Manager documentation](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/sites/administering/content-fragments/managing){target="_blank"}.

## Add Experience Manager Content fragments {#aem-add}

After creating and personalizing your AEM Content Fragments, you can now import it to your Journey optimizer campaign or journey.

1. Create your [Campaign](../campaigns/create-campaign.md) or [Journey](../building-journeys/journey-gs.md).

1. To access your AEM content fragment, click ![Personalization icon](assets/do-not-localize/Smock_PersonalizationField_18_N.svg) within any text field, or open the source code through an HTML content component.

    ![](assets/aem_campaign_2.png)

1. From the **[!UICONTROL AEM Content Fragment]** menu in the left-pane, click **[!UICONTROL Open AEM CF selector]**.

    ![](assets/aem_campaign_3.png)

1. Select a **[!UICONTROL Content Fragment]** from the available list to import into your Journey Optimizer content. 

1. Click **[!UICONTROL Show filters]** to fine tune your Content Fragments list. 

    By default, the Content Fragment filter is preset to display only approved Content.

    ![](assets/aem_campaign_4.png)

1. After selecting your **[!UICONTROL Content Fragment]**, click **[!UICONTROL Select]** to open it.

    ![](assets/aem_campaign_5.png)

1. Click **[!UICONTROL View fragment]** to display your Fragment information. Note that opening the **[!UICONTROL Fragment Info]** menu places the editor in read-only mode.

    Select **[!UICONTROL Preview]** from the right-hand menu to view your fragment in Adobe Experience Manager.

    ![](assets/aem_campaign_7.png)

1. Click ![More actions icon](assets/do-not-localize/Smock_MoreSmallList_18_N.svg) to access the advanced menu of your Fragment:

    * **[!UICONTROL Swap fragment]**
    * **[!UICONTROL Explore references]**
    * **[!UICONTROL Open in AEM]**

    ![](assets/aem_campaign_8.png)

1. Choose the desired fields from your **[!UICONTROL Fragment]** to add to your content.

    <!--
    Note that if you choose to copy the value, any future updates to the Content Fragment will not be reflected in your campaign or journey. However, using dynamic placeholders ensures real-time updates.-->

    ![](assets/aem_campaign_6.png)

1. Select **Pills: Off** to enable the pills experience to improve readability by hiding long attribute paths. 

    ![](assets/aem_campaign_10.png)

1. To enable real-time personalization, all placeholders used within a **[!UICONTROL Content fragment]** must be explicitly declared by the user as parameters in the fragment helper tag. You can map these placeholders to profile attributes, contextual attributes, static strings, or predefined variables using the following methods:

    1. **Profile or Contextual Attribute Mapping**: Assign the placeholder to a profile or contextual attribute, e.g. name = profile.person.name.firstName.

    1. **Static String Mapping**: Assign a fixed string value by placing it within double quotes, e.g. name = "John".

    1. **Variable Mapping**: Reference a variable declared earlier within the same HTML, e.g. name = 'variableName'.
    In this case, ensure **_variableName_** is declared before adding the fragment ID, using following syntax:

        ```html
        {% let variableName = attribute name %} 
        ```

    In the example below, the **_month_** placeholder is mapped to the **_profile.person.birthDate_** attribute within the fragment.

    ![](assets/aem_campaign_9.png){zoomable="yes"}


1. Click **[!UICONTROL Save]**. You can now test and check your message content as detailed in [this section](../content-management/preview.md).

Once you have performed your tests and validated the content, you can [send your campaign](../campaigns/review-activate-campaign.md) or [publish your journey](../building-journeys/publishing-the-journey.md) to your audience.

Adobe Experience Manager allows you to identify the Journey Optimizer campaigns or journeys where a Content Fragment is being used. Learn more in [Adobe Experience Manager documentation](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/sites/administering/content-fragments/extension-content-fragment-ajo-external-references).
