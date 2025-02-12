---
solution: Journey Optimizer
product: journey optimizer
title: Personalize email configuration settings
description: Learn how to define personalized values for your settings at the email channel configuration level
feature: Subdomains, Channel Configuration
topic: Administration
role: Admin
level: Experienced
keywords: settings, email, configuration, subdomain
exl-id: 1e004a76-5d6d-43a1-b198-5c9b41f5332c
---
# Personalize email configuration settings {#surface-personalization} 

For increased flexibility and control over your email settings, [!DNL Journey Optimizer] allows you to define personalized values for subdomains and headers<!--and URL tracking parameters--> when creating email configurations.

## Add dynamic subdomains {#dynamic-subdomains}

>[!CONTEXTUALHELP]
>id="ajo_surface_perso_not_available"
>title="Personalization not available"
>abstract="This configuration was created without any personalization attributes. Refer to the documentation for steps to solve if personalization is required."

>[!CONTEXTUALHELP]
>id="ajo_surface_dynamic_subdomain"
>title="Enable dynamic subdomains"
>abstract="When creating an email configuration, you can set up dynamic subdomains based on conditions that you define using the personalization editor. You can add up to 50 dynamic subdomains."

When creating an email configuration, you can set up dynamic subdomains based on specific conditions.

For example, if you have legal constraints to send messages from a dedicated email address per country, you can use dynamic subdomains. This allows you to create a single configuration with several sending subdomains corresponding to different countries - instead of creating multiple configurations for each country. You can then target customers based in various countries consolidated into one campaign.

To define dynamic subdomains in an email channel configuration, follow the steps below.

1. Before creating a configuration, set up the subdomains you want to use for sending emails according to your use case. [Learn how](../configuration/about-subdomain-delegation.md)

    For example, let's say you want to use different subdomains for different countries: set up one subdomain specific to US, one specific to UK, etc.

1. Create a channel configuration. [Learn how](../configuration/channel-surfaces.md)

1. Select the **[!UICONTROL Email]** channel.

1. In the **Subdomain** section, enable the **[!UICONTROL Dynamic Subdomain]** option.

    ![](assets/surface-email-dynamic-subdomain.png)

1. Select the Edit icon next to the first **[!UICONTROL Condition]** field.

1. The [personalization editor](../personalization/personalization-build-expressions.md) opens. In this example, set a condition such as `Country` equals `US`.

    ![](assets/surface-email-edit-condition.png)

1. Select the subdomain you want to associate with this condition. [Learn more on subdomains](../configuration/about-subdomain-delegation.md)

    >[!NOTE]
    >
    >Certain subdomains are currently unavailable for selection due to pending [feedback loop](../reports/deliverability.md#feedback-loops) registration. This process may take up to 10 business days. Once complete, you can choose from all available subdomains. <!--where FL registration happens? is it when delegating a subdomain and you're awaiting from subdomain validation? or is it on ISP side only?-->

    ![](assets/surface-email-select-subdomain.png)

    All recipients based in the US will receive messages using the selected subdomain for that country, meaning that all URLs involved (such as mirror page, tracking URL or unsubscribe link) will be populated based on that subdomain.

1. Set other dynamic subdomains as wanted. You can add up to 50 items.

    ![](assets/surface-email-add-dynamic-subdomain.png)

    <!--Select the [IP pool](../configuration/ip-pools.md) to associate with the configuration. [Learn more](email-settings.md#subdomains-and-ip-pools)-->

1. Define all other [email settings](email-settings.md) and [submit](../configuration/channel-surfaces.md#create-channel-surface) your configuration.

Once you have added one or more dynamic subdomains to a configuration, the following items will be populated based on the resolved dynamic subdomain for this configuration:

* All URLs (resource URL, mirror page URL and tracking URL)

* The [unsubscribe URL](email-settings.md#list-unsubscribe)

* The **From email** and **Error email** suffixes

>[!NOTE]
>
>If you set up dynamic subdomains and then disable the **[!UICONTROL Dynamic Subdomain]** option, all dynamic values are removed. Select a subdomain and submit the configuration for the changes to take effect.

## Personalize your header {#personalize-header}

You can also use personalization for all the header parameters defined in a configuration.

For example, if you have multiple brands, you can create a single configuration and use personalized values for your email headers. This allows you to make sure that all emails sent from your different brands are addressed to each of your customers with the correct **From** names and emails. Similarly, when your recipients hit the **Reply** button in their email client software, you want the **Reply to** names and emails correspond to the correct brand for the right user.

To use personalized variables for your configuration header parameters, follow the steps below.

>[!NOTE]
>
>You can personalize all **[!UICONTROL Header parameters]** fields, except the **[!UICONTROL Error email prefix]** field.


1. Define your header parameters as you would usually do. [Learn how](email-settings.md#email-header)

1. For each field, select the Edit icon.

    ![](assets/surface-email-personalize-header.png)

1. The [personalization editor](../personalization/personalization-build-expressions.md) opens. Define your condition as wanted and save your changes.

    <!--For example, set a condition such as each recipient receives an email from their own brand representative.-->

    >[!NOTE]
    >
    >You can only select **[!UICONTROL Profile attributes]** and **[!UICONTROL Helper functions]**.

    For example, you want to handle dynamically emails sent on behalf of a relationship manager, whose details are stored in the customer profile, so that every customer is linked to a relationship manager. In a [journey](../building-journeys/journey-gs.md), the email header (sender name, sender email, reply to address) can be personalized with the relationship manager's parameters, taken from the profile attributes.
    
    <!--The examples below use event parameters, which are currently not available.
    
    Let's say you want to handle dynamically emails sent on behalf of a sales assistant, where the sales assistant is retrieved from an event or campaign contextual parameters. For example: In a [journey](../building-journeys/journey-gs.md), when a purchase event is linked to the sales assistant of a specific shop, the email header (sender name, sender email, reply to address) can be personalized with the sales assistant parameters, taken from the event attributes. In an [API-triggered campaign](../campaigns/api-triggered-campaigns.md), initiated externally by a sales assistant, the triggered email can be sent on behalf of the sales assistant and the header personalization values taken from campaign contextual parameters.-->

1. Repeat the steps above for each parameter you want to add personalization to.

>[!NOTE]
>
>If you added one or more dynamic subdomains to your configuration, the **From email** and **Error email** suffixes will be populated based on the resolved [dynamic subdomain](#dynamic-subdomains).

<!--
## Use personalized URL tracking {#personalize-url-tracking}

To use personalized URL tracking prameters, follow the steps below.

1. Select the profile attribute of your choice from the personalization editor.

1. Repeat the steps above for each tracking parameter you want to personalize.

Now when the email is sent out, this parameter will be automatically appended to the end of the URL. You can then capture this parameter in web analytics tools or in performance reports.
-->

## View configuration details {#view-surface-details}

When using a configuration with personalized settings in a campaign or a journey, you can display the configuration details directly within the campaign or the journey. Follow the steps below.

1. Create an email [campaign](../campaigns/create-campaign.md) or [journey](../building-journeys/journey-gs.md).

1. Select the **[!UICONTROL Edit content]** button.

1. Click the **[!UICONTROL View configuration details]** button.

    ![](assets/campaign-view-surface-details.png)

1. The **[!UICONTROL Delivery settings]** window displays. You can view all the configuration settings, including the dynamic subdomains and personalized header parameters.

    >[!NOTE]
    >
    >All information on this screen are read-only.

1. Select **[!UICONTROL Expand]** to display the dynamic subdomains' details.

    ![](assets/campaign-delivery-settings-subdomain-expand.png)

## Check your configuration {#check-configuration}

When using a personalized configuration in a campaign or a journey, you can preview your email content using test profiles to check for potential errors with the dynamic settings you defined. Follow the steps below.

>[!NOTE]
>
>In addition to test profiles, [!DNL Journey optimizer] also allows you to test different variants of your content by previewing it and sending proofs using sample input data uploaded from a CSV / JSON file, or added manually. [Learn how to test your content using sample input data](../test-approve/simulate-sample-input.md)

To preview your content using test profiles, follow these steps: 

1. From the edit content screen of your message or in the Email Designer, click the **[!UICONTROL Simulate content]** button. [Learn more](../content-management/preview.md)

1. Select a [test profile](../content-management/test-profiles.md).

1. If an error is displayed, click the **[!UICONTROL View configuration details]** button.

    ![](assets/campaign-simulate-config-error.png)

1. Check the **[!UICONTROL Delivery settings]** screen for the errror details.

    ![](assets/campaign-simulate-config-details.png)

Possible errors can be as follows:

* The **subdomain** did not resolve for the selected test profile. For example, your configuration uses several sending subdomains corresponding to different countries, but the selected profile has no value defined for the `Country` attribute, or the attribute is set to `France` but this value is not associated with any subdomain in that configuration.

* The selected profile has no associated values for one or more **header parameters**.

With any of these errors, email is not sent to the selected test profile.

To avoid this type of error, make sure the header parameters you define use personalized attributes with values for most of your profiles. Missing values can impact your email deliverability.

>[!NOTE]
>
>Learn more on deliverability in [this section](../reports/deliverability.md)
