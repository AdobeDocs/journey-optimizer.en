---
solution: Journey Optimizer
product: journey optimizer
title: Configure URL tracking
description: Learn how to set up URL tracking at the email channel configuration level
feature: Email, Surface
topic: Administration
role: Admin
level: Experienced
keywords: settings, email, configuration

---

# URL tracking {#url-tracking}

>[!CONTEXTUALHELP]
>id="ajo_admin_preset_utm"
>title="Define URL tracking parameters"
>abstract="Use this section to automatically append tracking parameters to the URLs present in your email content. This feature is optional."

>[!CONTEXTUALHELP]
>id="ajo_admin_preset_url_preview"
>title="Preview URL tracking parameters"
>abstract="Review how tracking parameters will be appended to the URLs present in your email content."

When configuring a new [email channel configuration](email-settings.md), you can define **[!UICONTROL URL tracking parameters]** to measure the effectiveness of your marketing efforts across channels.

>[!NOTE]
>
>This feature is optional.

The parameters defined in the corresponding section will be appended to the end of the URLs included in your email message content. You can then capture these parameters in web analytics tools such as Adobe Analytics or Google Analytics, and create various performance reports.

You can add up to 10 tracking parameters using the **[!UICONTROL Add new parameter]** button.

![](assets/preset-url-tracking.png){width="80%"}

To configure a URL tracking parameter, you can directly enter the desired values in the **[!UICONTROL Name]** and **[!UICONTROL Value]** fields.

You can also edit each **[!UICONTROL Value]** field using the [personalization editor](../personalization/personalization-build-expressions.md). Click the edition icon to open the editor. From there, you can select the available contextual attributes and/or directly edit the text.

![](assets/preset-url-tracking-editor.png)

The following predefined values are available through the personalization editor:

* **Source action id**: ID of the Email action added to the journey or campaign.

* **Source action name**: name of the Email action added to the journey or campaign.

* **Source id**: ID of the journey or campaign the email was sent with.

* **Source name**: name of the journey or campaign the email was sent with.

* **Source version id**: ID of the journey or campaign version the email was sent with.

* **Offer id**: ID of the offer used in the email.

>[!NOTE]
>
>You can combine typing text values and using contextual attributes from the personalization editor. Each **[!UICONTROL Value]** field can contain a number of characters up to the limit of 5 KB.

<!--You can drag and drop the parameters to reorder them.-->

Below are examples of Adobe Analytics and Google Analytics compatible URLs.

* Adobe Analytics compatible URL: `www.YourLandingURL.com?cid=email_AJO_{{context.system.source.id}}_image_{{context.system.source.name}}`

* Google Analytics compatible URL: `www.YourLandingURL.com?utm_medium=email&utm_source=AJO&utm_campaign={{context.system.source.id}}&utm_content=image`

You can dynamically preview the resulting tracking URL. Each time you add, edit or remove a parameter, the preview is automatically updated.

![](assets/preset-url-tracking-preview.png)

>[!NOTE]
>
>You can also add dynamic personalized tracking parameters to the links present in your email content, but this is not possible at the configuration level. You need to do this when authoring your message using the email designer. [Learn more](message-tracking.md#url-tracking)
