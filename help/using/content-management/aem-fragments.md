---
solution: Journey Optimizer
product: journey optimizer
title: AEM Content Fragments
description: Learn how to access & manage AEM Content Fragments
topic: Content Management
role: User
level: Beginner
hide: yes
hidefromtoc: yes
---
# Adobe Experience Manager Content Fragments {#aem-fragments}

By integrating Adobe Experience Manager with Adobe Journey Optimizer, you can now seamlessly incorporate your AEM Content Fragments into your Journey Optimizer email content. This streamlined connection simplifies the process of accessing and leveraging AEM content, enabling the creation of personalized and dynamic campaigns and journeys.

To learn more on AEM Content Fragment, refer to [Experience Manager documentation](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/sites/authoring/fragments/content-fragments).

## Limitations {#limitations}

* Only available for Email channel.

* Users are currently unable to switch the AEM instance they are connected to, as each sandbox is limited to a single instance.

* It is recommended to limit the number of users with access to publish Content Fragments to reduce the risk of accidental errors in emails.

* For multilingual content, only the manual flow is supported.

* Variants are not currently supported.

* You need to create a tag specifically for Journey Optimizer.

    +++ Learn how to create your Journey Optimizer tag

    1. Access your **Experience Manager** environment.

    1. From the **Tools** menu, navigate to the **General** tab and select **Tagging**.

    1. Click **Create a New Tag**.

    1. Ensure the ID adheres to the following syntax: `ajo-enabled:{AJO-OrgId}/{AJO-SandboxName}`.

    1. Click **Create**. 

    You can now assign this Journey Optimizer Tag to your Content Fragments.
    +++

## Add AEM Content Fragments {#aem-add}

After creating and personalizing your [AEM Content Fragments](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/sites/authoring/fragments/content-fragments), you can now import it to your Journey optimizer campaign or journey.

1. After creating your [Campaign](../email/create-email.md) or [Journey](../email/create-email.md) with an email action, access the email designer to configure the email content. [Learn more](../email/get-started-email-design.md)

1. Click inside a text block or in the subject line and select **[!UICONTROL Add Personalization]** from the contextual toolbar.

    ![](assets/aem_campaign_2.png)

1. From the **[!UICONTROL AEM Content Fragment]** menu in the left-pane, click **[!UICONTROL Open AEM CF selector]**.

    ![](assets/aem_campaign_3.png)

1. Select a **[!UICONTROL Content Fragment]** from the available list to import into your Journey Optimizer content. 

    >[!IMPORTANT]
    >
    >Only published **[!UICONTROL Content Fragments]** can be used. 

1. Click **[!UICONTROL Show filters]** to fine tune your Content Fragments list. 

    The Content Fragment selector includes pre-configured filters:

    * **[!UICONTROL Status]**: Published, Modified
    * **[!UICONTROL Tag]**: Automatically defined based on your Journey Optimizer environment (Organizational ID and Sandbox)

    ![](assets/aem_campaign_4.png)

1. After selecting your **[!UICONTROL Content Fragment]**, click **[!UICONTROL Select]** to open it.

    ![](assets/aem_campaign_5.png)

1. Choose the desired fields from your **[!UICONTROL Content Fragment]** to add to your content.

    ![](assets/aem_campaign_6.png)

1. Click **[!UICONTROL Save]** and check your message in the preview. You can now test and check your message content as detailed in [this section](preview.md).

Once you have performed your tests and validated the content, you can send your email to your audience with your [Campaign](../campaigns/review-activate-campaign.md) or [Journey](../building-journeys/publishing-the-journey.md).

