---
solution: Journey Optimizer
product: journey optimizer
title: Email opt-out management
description: Learn how to manage opt-out with emails
feature: Email Design, Consent Management
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

The one-click list unsubscribe URL is an unsubscribe link or button displayed next to the email sender information and lets recipients instantly opt out of your mailing lists with a single click. Learn how to manage the **[!UICONTROL List unsubscribe]** option in [this section](list-unsubscribe.md).

### One-click opt-out from the email content {#one-click-opt-out}

To set a personalized unsubscribe URL, insert a one-click opt-out link into the email message content and enter the URL of your choice, as described below:

1. Access your email content and [insert a link](../email/message-tracking.md#insert-links).
1. Select **[!UICONTROL One click Opt-out]** as the type of link.

    ![](assets/message-tracking-opt-out.png)

1. Enter the URL of the landing page where the user is redirected once unsubscribed. This page is here to confirm that opting out was successful.

    >[!NOTE]
    >
    >If you enabled the **[!UICONTROL List-Unsubscribe]** option at the [channel configuration level](email-settings.md#list-unsubscribe) and have the default **[!UICONTROL One-click unsubscribe URL]** option unchecked, this landing page URL is also used when users click the unsubscribe link in the email header. [Learn more](list-unsubscribe.md)

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

