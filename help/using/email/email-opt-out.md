---
solution: Journey Optimizer
product: journey optimizer
title: Email opt-out management
description: Learn how to manage opt-out with emails
feature: Email Design, Privacy
topic: Content Management
role: User
level: Intermediate
keywords: opt-out, email, link, unsubscribe
exl-id: 4bb51bef-5dab-4a72-8511-1a5e528f4b95
---
# Email opt-out management {#email-opt-out}

When sending messages from journeys or campaigns, you must always ensure that customers can unsubscribe from future communications. Once unsubscribed, the profiles are automatically removed from the audience of future marketing messages.  [Learn more on privacy & opt-out management](../privacy/opt-out.md)

>[!NOTE]
>
>All your marketing messages must include an opt-out link. This is not required for transactional messages. The message category - **[!UICONTROL Marketing]** or **[!UICONTROL Transactional]** - is defined at the [channel configuration](../configuration/channel-surfaces.md#email-type) level and when creating the message.

To insert an unsubscription link in your email content, you can:

* Add a one click unsubscribe URL in the email header. The **[!UICONTROL Enable List-Unsubscribe]** option at the channel configuration level adds an opt-out link to the email header. [Learn more on opt-out in email header](#unsubscribe-header)

* Enable the **one-click opt-out link** for your email.  [Learn how to add a one-click opt-out link](#one-click-opt-out)

* Insert a **link to a landing page**. [Learn how to add an opt-out landing page](#opt-out-external-lp)


## One-step opt-out {#opt-out-one-step}

With [!DNL Adobe Journey Optimizer], you can configure your [email configuration settings](email-settings.md#list-unsubscribe) with an auto-generated one-click unsubscribe URL and mailto address in the email header, or include a one-click opt-out URL in your email body.

When a recipient clicks the one-click opt-out link, that recipient's unsubscribe request is processed accordingly.

### One-click unsubscribe URL in the email header {#unsubscribe-header}

<!--Do not modify - Legal Review Done -->

>[!CONTEXTUALHELP]
>id="ajo_admin_preset_unsubscribe"
>title="Add an unsubscribe URL to your emails"
>abstract="Enable List-Unsubscribe to automatically add an unsubscribe URL to the email header. You can also set an unsubscribe URL in a message by inserting a one-click opt-out link into the email content."
>additional-url="https://experienceleague.adobe.com/en/docs/journey-optimizer/using/channels/email/email-opt-out#one-click-opt-out" text="One-click opt-out from the email content"
>additional-url="https://experienceleague.adobe.com/en/docs/journey-optimizer/using/channels/email/email-opt-out#one-click-opt-out" text="Enable List-Unsubscribe in the email configuration"

The one-click list unsubscribe URL is an unsubscribe link or button displayed next to the email sender information and lets recipients instantly opt out of your mailing lists with a single click.

In [!DNL Adobe Journey Optimizer], when the **Enable List-Unsubscribe** option is toggled on, the email header includes both a mailto and/or a URL by default that recipients can use to unsubscribe from your mailing list.

The [Enable List-Unsubscribe](email-settings.md#list-unsubscribe) toggle must be activated at the channel configuration level so that emails using this configuration include the one-click unsubscribe URL in the email header.

>[!NOTE]
>
>To display the one-click unsubscribe URL in the email header, the recipients' email client must support this feature.


For example, the one-click unsubscribe URL displays an unsubscription link as below in Gmail:

![](assets/unsubscribe-header.png)


<!--With Adobe Journey Optimizer, you can configure your email configuration settings with an auto-generated one-click unsubscribe URL and mailto address in the email header, or include a one-click opt-out URL in your email body: when a recipient clicks the one-click opt-out link, recipient's unsubscribe request is processed accordingly.-->

<!--
>[!AVAILABILITY]
>
>One-click Unsubscribe URL Header will be available in Adobe Journey Optimizer starting June 3, 2024.
>
-->

Depending on the email client, and the [email configuration unsubscription settings](email-settings.md#list-unsubscribe), clicking the unsubscribe link in the email header can have the following impacts:

* When the **Mailto (unsubscribe)** feature is enabled, the unsubscribe request is sent to the default unsubscribe address based on the subdomain you configured.
* When the **One-click unsubscribe URL** feature is enabled - or if you inserted an unsubscription URL in your email body content -, the recipient is directly opted-out, either at the channel level or at the ID level (depending on how the consent is set up), when the recipient clicks on the one-click unsubscribe URL (based on the subdomain you configured).

![](../email/assets/surface-list-unsubscribe-mailto.png){width="80%"}

In both cases, the corresponding profile for the recipient is immediately opted out and this choice is updated in Experience Platform. Learn more in the [Experience Platform documentation](https://experienceleague.adobe.com/docs/experience-platform/profile/ui/user-guide.html#getting-started){target="_blank"}.

If you have toggled on the **[!UICONTROL Enable List-Unsubscribe]** option in the [email configuration settings](email-settings.md#list-unsubscribe), we recommend that you enable both methods - **Mailto (unsubscribe)** and **One-Click Unsubscribe URL**. Not all email clients support the HTTP method. With the Mailto list-unsubscribe feature provided for you to select an alternative, your sender reputation can be better protected and all your recipients are able to have access to use the unsubscribe functionality. [Learn more](email-settings.md#list-unsubscribe)


### One-click opt-out from the email content {#one-click-opt-out}

To set a personalized unsubscribe URL, insert a one-click opt-out link into the email message content and enter the URL of your choice, as described below:

1. Access your email content and [insert a link](../email/message-tracking.md#insert-links).
1. Select **[!UICONTROL One click Opt-out]** as the type of link.

    ![](assets/message-tracking-opt-out.png)

1. Enter the URL of the landing page where the user is redirected once unsubscribed. This page is here to confirm that opting out was successful.

    >[!NOTE]
    >
    >If you enabled the **[!UICONTROL List-Unsubscribe]** option at the [channel configuration level](email-settings.md#list-unsubscribe) and have the default **[!UICONTROL One-click unsubscribe URL]** option unchecked, this landing page URL is also used when users click the unsubscribe link in the email header. [Learn more](#unsubscribe-header)

    ![](assets/message-tracking-opt-out-confirmation.png)

    You can personalize your links. Learn more on personalized URLs in [this section](../personalization/personalization-syntax.md).

1. Select how you want to apply the opting out: at the channel or identity level.

    ![](assets/message-tracking-opt-out-level.png)

    * **[!UICONTROL Channel]**: The opt-out applies to future messages sent to the profile's target (i.e. email address) for the current channel. If several targets are associated with a profile, the opt-out applies to all targets (i.e. email addresses) in the profile for that channel.
    * **[!UICONTROL Identity]**: The opt-out applies to future messages sent to the specific target (i.e. email address) being used for the current message.
    <!--* **[!UICONTROL Subscription]**: The opt-out applies to future messages associated with a specific subscription list. This option can only be selected if the current message is associated with a subscription list.-->

1. Save your changes.


## Two-step opt-out {#opt-out-external-lp}

The standard opt-out mechanism relies on two steps: the subscriber clicks the opt-out link in an email, then they are redirected to an opt-out landing page to confirm their unsubscription. 

To implement this unsubscription mode, you must create and publish an opt-out landing page, and add an unsubscription link in your email messages, with a link to the landing page. These steps are outlined below.


### Prerequisites {#prereq-lp}

To set up a two step opt-out mechanism, you must create your own unsubscription landing pages. The first landing page will be linked from your message and must contain a call-to-action button. A confirmation message should display when the user clicks on the button.

Learn how to create a landing page in Adobe Journey Optimizer to manage unsubscriptions in [this page](../landing-pages/lp-use-cases.md#opt-out).

You can also use an external landing page. In that case, configure the API to send the information to Adobe Journey Optimizer when a recipients has unsubscribed.

+++ Learn how to implement an opt-out API call

To have your recipients opted out when they submit their choice from the landing page, you must implement a **Subscription API call** through [Adobe Developer](https://developer.adobe.com){target="_blank"} to update the corresponding profiles' preferences.

This POST call is as follows:

Endpoint: https://platform.adobe.io/journey/imp/consent/preferences

Query parameters:

* **params**: contains the encrypted payload
* **pid**: encrypted profile ID

These two parameters will be included into the third-party landing page URL sent to your recipient:

![](assets/opt-out-parameters.png)

Header requirements:

* x-api-key
* x-gw-ims-org-id
* x-sandbox-name 
* authorization (user token from your technical account)

Request body:

```
{
   "marketing": [
       {
            "type": "email",           
            "choice": "no",          
            "scope": "channel"       
        }
    ],
 
}
```

[!DNL Journey Optimizer] uses these parameters to update the corresponding profile's choice through the [Adobe Developer](https://developer.adobe.com){target="_blank"} API call.

+++


### Add an unsubscribe link {#add-unsubscribe-link}

You first need to add an unsubscribe link into a message. To do this, follow the steps below:

1. Create a message and [insert a link](../email/message-tracking.md#insert-links) using the contextual toolbar.

    ![](assets/opt-out-insert-link.png)

1. Select the **[!UICONTROL Landing page]** from the **[!UICONTROL Type]** drop-down list, and select your opt-out landing page in the **[!UICONTROL Landing page]** field.

    If you are using an external landing page, select **[!UICONTROL External Opt-out/Unsubscription]** from the **[!UICONTROL Type]** drop-down list.

    ![](assets/opt-out-link-type.png)
    
    In the **[!UICONTROL Link]** field, paste the link to your third-party landing page.

    ![](assets/opt-out-link-url.png)

1. Click **[!UICONTROL Save]**.


### Send the message with unsubscribe link {#send-message-unsubscribe-link}

Once you configured the unsubscribe link to your landing page, your can create and send your message.

1. Configure your message with an unsubscription link and send it to your subscribers.

1. Once the message is received, if the recipient clicks the unsubscribe link, your landing page is displayed.

    ![](assets/opt-out-lp-example.png)

1. If the recipient submits the form - here, by hitting the **[!UICONTROL Unsubscribe]** button in your landing page - the profile data is updated through the API call.

1. The opted-out recipient is then redirected to a confirmation message screen indicating that opting out was successful.

    ![](assets/opt-out-confirmation-example.png)

    As a result, this user will not receive communication from your brand unless subscribed again.

1. To check that the corresponding profile's choice has been updated, go to Experience Platform and access the profile by selecting an identity namespace and a corresponding identity value. Learn more in the [Experience Platform documentation](https://experienceleague.adobe.com/docs/experience-platform/profile/ui/user-guide.html#getting-started){target="_blank"}.

    ![](assets/opt-out-profile-choice.png)

    In the **[!UICONTROL Attributes]** tab, you can see the value for **[!UICONTROL choice]** has changed to **[!UICONTROL no]**.

