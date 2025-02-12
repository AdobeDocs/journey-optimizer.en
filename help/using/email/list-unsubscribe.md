---
solution: Journey Optimizer
product: journey optimizer
title: Configure List unsubscribe
description: Learn how to include a one-click unsubscribe URL into the header of your emails when setting your channel configuration
feature: Email, Surface
topic: Administration
role: Admin
level: Experienced
keywords: settings, email, configuration
exl-id: c6c77975-ec9c-44c8-a8d8-50ca6231fea6
---
# List unsubscribe{#list-unsubscribe}

<!--Do not modify - Legal Review Done -->

When configuring a new email channel configuration, upon [selecting a subdomain](email-settings.md#subdomains-and-ip-pools) from the list, the **[!UICONTROL Enable List-Unsubscribe]** option displays.

![](assets/preset-list-unsubscribe.png)

## Enable List unsubscribe {#enable-list-unsubscribe}

This option is enabled by default to include a one-click unsubscribe URL into the email header, such as:

![](assets/preset-list-unsubscribe-header.png)

>[!NOTE]
>
>If you disable this option, no one-click unsubscribe URL is displayed in the email header.

The List unsubscribe header offers two options, which are enabled by default unless you uncheck one or both:

![](assets/surface-list-unsubscribe.png){width="80%"}

* A **[!UICONTROL Mailto (unsubscribe)]** address, which is the destination address where unsubscribe requests are routed to for auto-processing.

    In [!DNL Journey Optimizer], the unsubscribe email address is the default **[!UICONTROL Mailto (unsubscribe)]** address displayed in the channel configuration, based on your [selected subdomain](#subdomains-and-ip-pools). <!--With this method, clicking the Unsubscribe link sends a pre-filled email to the unsubscribe address specified in the email header.-->

* The **[!UICONTROL One-click unsubscribe URL]**, which by default is the one-click opt-out URL generated List unsubscribe header, based on the subdomain you set and configured in the channel configuration settings. <!--With this method, clicking the Unsubscribe link directly unsubscribes the user, requiring only a single action to unsubscribe.-->

You can select the **[!UICONTROL Consent level]** from the corresponding drop-down list. It can be specific to the channel or to the profile identity. Based on this setting, when a user unsubscribes using the list unsubscribe URL in the header of an email, the consent gets updated in [!DNL Adobe Journey Optimizer], either at the channel level or ID level.

The **[!UICONTROL Mailto (unsubscribe)]** feature and the **[!UICONTROL One-click unsubscribe URL]** feature are optional.

If you do not want to use the default generated one-click unsubscribe URL, you can uncheck the feature. In the scenario where the **[!UICONTROL Enable List-Unsubscribe]** option is toggled on and the **[!UICONTROL One-click Unsubscribe URL]** feature is unchecked, if you add a [one-click opt-out link](../email/email-opt-out.md#one-click-opt-out) to a message created using this configuration, the List unsubscribe header picks up the one-click opt-out link you have inserted in the body of the email and uses that as the one-click unsubscribe URL value.
 
![](assets/preset-list-unsubscribe-opt-out-url.png)

>[!NOTE]
>
>If you do not add a one-click opt-out link into your message content and the default **[!UICONTROL One-click unsubscribe URL]** is unchecked in the channel configuration settings, no URL is passed into the email header as part of the List unsubscribe header.

Learn more on managing unsubscribe capabilities within your messages in [this section](../email/email-opt-out.md#unsubscribe-header).

## Manage unsubscribe data externally {#custom-managed}

>[!CONTEXTUALHELP]
>id="ajo_email_config_unsubscribe_custom"
>title="Define how unsubscribe data is managed"
>abstract="**Adobe managed**: Consent data is managed by you within the Adobe system.<br>**Customer managed**: Consent data is managed by you in an external system and no synchronization of consent data is updated in the Adobe system unless initiated by you."

>[!AVAILABILITY]
>
>This capability is released in Limited Availability (LA) for a small set of customers.

If you are managing consent outside of Adobe, select the **[!UICONTROL Customer managed]** option to enter a custom unsubscribe email address and your own one-click unsubscribe URL.

![](assets/surface-list-unsubscribe-custom.png){width="80%"}

>[!WARNING]
>
>If you are using the **[!UICONTROL Customer managed]** option, Adobe is not storing any unsubscribe or consent data. With the **[!UICONTROL Customer managed]** option, organizations are electing to use an external system and will be responsible for managing their consent data in such external system. There is no auto synchronization of consent data between the external system and  [!DNL Journey Optimizer]. Any synching of consent data, which is sourced from the external system to update user consent data in [!DNL Journey Optimizer], must be initiated by the organization as a data transfer to push the consent data back into [!DNL Journey Optimizer].

### Configure the decrypt API {#configure-decrypt-api}

With the **[!UICONTROL Customer managed]** option selected, if you enter custom endpoints and use them in a campaign or journey, [!DNL Journey Optimizer] appends some default profile specific parameters to the consent update event <!--sent to the custom endpoint -->when your recipients click the Unsubscribe link.

These parameters are sent to the endpoint in an encrypted manner. Thus, the external consent system needs to implement a specific API through [Adobe Developer](https://developer.adobe.com){target="_blank"} to decrypt the parameters sent by Adobe.

The GET call to retrieve these parameters depends on the List unsubscribe option you are using - **[!UICONTROL One-click unsubscribe URL]** or **[!UICONTROL Mailto (unsubscribe)]**.

<!--To configure the API to send back the information to [!DNL Adobe Journey Optimizer] when a recipient has unsubscribed using the List unsubscribe option with custom endpoints, follow the steps below.-->

+++ One-click unsubscribe URL

With the **[!UICONTROL One-click unsubscribe URL]** option, clicking the Unsubscribe link directly unsubscribes the user.

The GET call is as follows:

Endpoint: https://platform.adobe.io/journey/imp/consent/decrypt

Query parameters:

* **params**: contains the encrypted payload
* **pid**: encrypted profile ID

These two parameters will be included into the consent update event sent to the custom endpoints.

Header requirements:

* x-api-key
* x-gw-ims-org-id
* authorization (user token from your technical account)

+++

+++ Mailto (unsubscribe)

With the **[!UICONTROL Mailto (unsubscribe)]** option, clicking the Unsubscribe link sends a pre-filled email to the unsubscribe address specified.

The GET call is as follows.

Endpoint: https://platform.adobe.io/journey/imp/consent/decrypt

Query parameters:

* **emailParams**: string that contains the **params** (encrypted payload) and **pid** (encrypted profile ID) parameters.

The **params** and **pid** parameters will be included into the consent update event sent to the custom endpoints.

Header requirements:

* x-api-key
* x-gw-ims-org-id
* authorization (user token from your technical account)

+++
