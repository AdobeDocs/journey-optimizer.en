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
>All you marketing messages must include an opt-out link. This is not required for transactional messages. The message category - **[!UICONTROL Marketing]** or **[!UICONTROL Transactional]** - is defined at the [channel surface](../configuration/channel-surfaces.md#email-type) level and when creating the message.

To insert an unsubscription link in your email content, you can:

* Insert a **link to a landing page**. It can be:

    * A **[!DNL Journey Optimizer] landing page**. [Learn how to add an opt-out landing page](../landing-pages/lp-use-cases.md#opt-out)
    
    * A **an external landing page**. [Learn how to add an external opt-out link](#opt-out-external-lp)

* Add an unsubscribe link in the email header. Enabling the **[!UICONTROL List-Unsubscribe]** option at the channel surface level adds an opt-out link in the email header. [Learn more on opt-out in email header](#unsubscribe-header)

* Enable the **one-click opt-out link** for your email. Instead of message recipients scrolling the email to follow an unsubscribe link and process manually, they can unsubscribe directly from their mailbox interface, if that mailbox provider supports this capability. [Learn how to add a one-click opt-out link](#one-click-opt-out)


## External opt-out {#opt-out-external-lp}

### Add an unsubscribe link {#add-unsubscribe-link}

You first need to add an unsubscribe link into a message. To do this, follow the steps below:

1. Build your own unsubscription landing page.

1. Host it on the third-party system of your choice.

1. Create a message in a journey.

1. Select text in your content and [insert a link](../email/message-tracking.md#insert-links) using the contextual toolbar.

    ![](assets/opt-out-insert-link.png)

1. Select **[!UICONTROL External Opt-out/Unsubscription]** from the **[!UICONTROL Link type]** drop-down list.

    ![](assets/opt-out-link-type.png)

1. In the **[!UICONTROL Link]** field, paste the link to your third-party landing page.

    ![](assets/opt-out-link-url.png)

1. Click **[!UICONTROL Save]**.

### Implement an API call for opt-out {#opt-out-api}

To have your recipients opted out when they submit their choice from the landing page, you must implement a **Subscription API call** through [Adobe Developer](https://developer.adobe.com){target="_blank"} to update the corresponding profiles' preferences.

This POST call is as follows:

Endpoint: https://platform.adobe.io/journey/imp/consent/preferences

Query parameters:

* **params**: contains the encrypted payload
* **pid**: encrypted profile ID

These three parameters will be included into the third-party landing page URL sent to your recipient:

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

[!DNL Journey Optimizer] will use these parameters to update the corresponding profile's choice through the [Adobe Developer](https://developer.adobe.com){target="_blank"} API call.

### Send the message with unsubscribe link {#send-message-unsubscribe-link}

Once you configured the unsubscribe link to your landing page and implemented the API call, your message is ready to be sent.

1. Send the message including the link through a [journey](../building-journeys/journey.md).

1. Once the message is received, if the recipient clicks the unsubscribe link, your landing page is displayed.

    ![](assets/opt-out-lp-example.png)

1. If the recipient submits the form (here, by hitting the **Unsubscribe** button in your landing page), the profile data is updated through the [API call](#opt-out-api).

1. The opted-out recipient is then redirected to a confirmation message screen indicating that opting out was successful.

    ![](assets/opt-out-confirmation-example.png)

    As a result, this user will not receive communication from your brand unless subscribed again.

1. To check that the corresponding profile's choice has been updated, go to Experience Platform and access the profile by selecting an identity namespace and a corresponding identity value. Learn more in the [Experience Platform documentation](https://experienceleague.adobe.com/docs/experience-platform/profile/ui/user-guide.html#getting-started){target="_blank"}.

    ![](assets/opt-out-profile-choice.png)

    In the **[!UICONTROL Attributes]** tab, you can see the value for **[!UICONTROL choice]** has changed to **[!UICONTROL no]**.

## One-click opt-out {#one-click-opt-out}

>[!AVAILABILITY]
>
>One-click opt-out will be available in Adobe Journey Optimizer starting June 3, 2024.
>

One-click unsubscribe is a user-friendly capability which is embedded directly within the email user interface and lets recipients instantly opt out of your mailing lists with a single click. 

To add an opt-out link in your email, follow the steps below:

1. [Insert a link](../email/message-tracking.md#insert-links) and select **[!UICONTROL One click Opt-out]** as the type of link.

    ![](assets/message-tracking-opt-out.png)

1. Enter the URL of the landing page where the user will be redirected once unsubscribed. This page is only here to confirm that opting out was successful.

    >[!NOTE]
    >
    >If you enabled the **List-Unsubscribe** option at the [channel surface level](email-settings.md#list-unsubscribe), this URL is also used when users click the unsubscribe link in the email header. [Learn more](#unsubscribe-header)

    ![](assets/message-tracking-opt-out-confirmation.png)

    You can personalize your links. Learn more on personalized URLs in [this section](../personalization/personalization-syntax.md).

1. Select how you want to apply the opting out: at the channel, identity, or subscription level.

    ![](assets/message-tracking-opt-out-level.png)

    * **[!UICONTROL Channel]**: The opt-out applies to future messages sent to the profile's target (i.e. email address) for the current channel. If several targets are associated with a profile, the opt-out applies to all targets (i.e. email addresses) in the profile for that channel.
    * **[!UICONTROL Identity]**: The opt-out applies to future messages sent to the specific target (i.e. email address) being used for the current message.
    * **[!UICONTROL Subscription]**: The opt-out applies to future messages associated with a specific subscription list. This option can only be selected if the current message is associated with a subscription list.

1. Save your changes.

Once your message is sent, if a recipient clicks the opt-out link, their profile is immediately opted out.

## Unsubscribe link in email header {#unsubscribe-header}

>[!CONTEXTUALHELP]
>id="ajo_admin_preset_unsubscribe"
>title="Add unsubscribe link to email header"
>abstract="Enable List-Unsubscribe to add an unsubscribe link to the email header. To set an unsubscribe URL, insert a one-click opt-out link into the email content."
>additional-url="https://experienceleague.adobe.com/docs/journey-optimizer/using/privacy/consent/opt-out.html#one-click-opt-out" text="One-click opt-out"

If the [List-Unsubscribe option](email-settings.md#list-unsubscribe) is enabled at the channel surface level, the corresponding emails sent with [!DNL Journey Optimizer] will include an unsubscribe link in the email header.

For example, the unsubscribe link will display like this in Gmail:

![](assets/unsubscribe-header.png)

>[!NOTE]
>
>To display the unsubscribe link in the email header, the recipients' email client must support this feature.

<!--
The unsubscribe address is the default **[!UICONTROL Mailto (unsubscribe)]** address as well as the  **One-click Unsubscribe URL** displayed in the corresponding channel surface. 
-->

In regards to List Unsubscribe header, we recommend that you include both methods - Mailto & Unsubscribe URL. Not all email clients support the HTTP method. With Mailto list-unsubscribe provided as an alternative, your sender reputation is better protected and your recipients are all able to use the unsubscribe function. [Learn more](email-settings.md#list-unsubscribe)

To set a personalized unsubscribe URL, insert a one-click opt-out link into the email message content and enter the URL of your choice. [Learn more](#one-click-opt-out)

Depending on the email client, clicking the unsubscribe link from the header can have the following impacts:

* The unsubscribe request is sent to the default unsubscribe address.

* The recipient will be directly opted-out, either at the channel level or at the ID level (depending on how the consent is set up), when they click on the Unsubscribe URL.

<!--
    >[!NOTE]
    >
    >If you do not add a one-click opt-out link into your message content, no landing page will be displayed.
-->

* The corresponding profile is immediately opted out and this choice is updated in Experience Platform. Learn more in the [Experience Platform documentation](https://experienceleague.adobe.com/docs/experience-platform/profile/ui/user-guide.html#getting-started){target="_blank"}.
