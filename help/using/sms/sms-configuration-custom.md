---
solution: Journey Optimizer
product: journey optimizer
title: Configure your custom provider
description: Learn how to configure your environment to send text messages with Journey Optimizer with a custom provider
feature: SMS, Channel Configuration
badge: label="Beta" type="Informative"
role: Admin
level: Intermediate
exl-id: fd713864-96b9-4687-91bd-84e3533273ff
---
# Configure a custom SMS provider {#sms-configuration-custom}

>[!CONTEXTUALHELP]
>id="ajo_admin_sms_api_byop_provider_url"
>title="Provider URL"
>abstract="Specify the URL of the external API you plan to connect to. This URL serves as the endpoint for accessing the API's features and functionalities."

>[!CONTEXTUALHELP]
>id="ajo_admin_sms_api_byop_header_parameters"
>title="Header parameters"
>abstract="Specify the label, type, and value of additional headers to enable proper authentication, content formatting, and effective API communication. "

>[!CONTEXTUALHELP]
>id="ajo_admin_sms_api_byop_provider_payload"
>title="Provider payload"
>abstract="Provide the request payload to ensure the correct data is sent for processing and response generation."

>[!AVAILABILITY]
>
>Custom providers are currently available as a beta to selected users only. Please reach out to your Adobe representative to be included in the Beta.
>Note that this Beta does not support inbound messages for opt-in/opt-out consent management and delivery reporting.


This feature empowers you to integrate and configure your own SMS providers, offering flexibility beyond the default providers (Sinch, Twilio, and Infobip). This enables seamless SMS authoring, delivery, reporting, and consent management.

With the custom provider configuration for SMS, you can:

* Configure custom SMS providers directly within Journey Optimizer.
* Use advanced payload customization for dynamic messaging.
* Manage consent preferences (opt-in/opt-out) to ensure compliance.

## Create your API credential {#api-credential}

To send messages in Journey Optimizer using a custom provider not available out of the box by Adobe (e.g., Sinch, Infobip, Twilio), follow these steps:

1. In the left rail, navigate to **[!UICONTROL Administration]** `>` **[!UICONTROL Channels]**, select the **[!UICONTROL API Credentials]** menu, and click the **[!UICONTROL Create new API credentials]** button.

    ![](assets/sms_byo_1.png)

1. Configure your SMS API credentials, as detailed below:

    * **[!UICONTROL SMS vendor]**: Custom.

    * **[!UICONTROL Name]**: Enter a name for your API Credential.

    * **[!UICONTROL Provider AppId]**: Enter the application ID provided by your SMS provider.

    * **[!UICONTROL Provider Name]**: Enter the name of your SMS provider.

    * **[!UICONTROL Provider URL]**: Enter the URL of your SMS provider.

    * **[!UICONTROL Auth Type​]**: Select your authorization type and [complete the corresponding fields](#auth-options) based on the chosen authentication method.

        ![](assets/sms-byop.png)

1. In the **[!UICONTROL Headers]** section, click **[!UICONTROL Add new parameter]** to specify the HTTP headers for the request message that will be sent to the external service.

    The **Content-Type** and **Charset** header fields are set by default and cannot be deleted.

    ![](assets/sms_byo_2.png)

1. Add your **[!UICONTROL Provider Payload]** to validate and customize your request payloads. 
    
    You can dynamically personalize your payload using profile attributes, and ensure accurate data is sent for processing and response generation with the help of built-in helper functions.
<!--
1. Add your **Inbound settings** to determine how your system handles incoming messages and subscriber preferences: 

    * **[!UICONTROL Inbound Webhook URL]**: Specify the endpoint URL where inbound messages (e.g. replies or new messages from users) are sent.
    * **[!UICONTROL Opt-in Keywords]**: Enter the default or custom keywords that will automatically trigger your Opt-In Message. For multiple keywords, use comma-separated values.
    * **[!UICONTROL Opt-in Message]**: Enter the custom response that is automatically sent as your Opt-In Message.
    * **[!UICONTROL Opt-out Keywords]**: Enter the default or custom keywords that will automatically trigger your Opt-Out Message. For multiple keywords, use comma-separated values.
    * **[!UICONTROL Opt-out Message]**: Enter the custom response that is automatically sent as your Opt-Out Message.
-->

1. Click **[!UICONTROL Submit]** when you finished the configuration of your API credentials.

1. In the **[!UICONTROL API Credentials]** menu, click the bin icon to delete your API credentials.

    ![](assets/sms_byo_3.png)

1. To modify existing credentials, locate the desired API credentials and click the **[!UICONTROL Edit]** option to make the necessary changes.

    ![](assets/sms_byo_4.png)

After creating and configuring your API credential, you now need to create a channel surface for SMS messages. [Learn more](sms-configuration-surface.md)

Once configured, you can leverage all out-of-the-box channel capabilities such as message authoring, personalization, link tracking, and reporting.

### Authentication options for custom SMS Providers {#auth-options}

>[!CONTEXTUALHELP]
>id="ajo_admin_sms_api_byop_auth_type"
>title="Authentication type"
>abstract="Specify the authentication method needed to access the API, this ensures secure and authorized communication with the external service."

>[!BEGINTABS]

>[!TAB API key]

Once your API credential is created, complete the fields required for API key authentication:

* **[!UICONTROL Name]**​: Enter a name for your API key configuration.
* **[!UICONTROL API Token]**​: Enter the API Token provided by your SMS provider.

![](assets/sms-byop-api-key.png)

>[!TAB MAC authentication]

Once your API credential is created, complete the fields required for MAC authentication:

* **[!UICONTROL Name]**​: Enter a name for your MAC authentication configuration.
* **[!UICONTROL API Token]**​: Enter the API Token provided by your SMS provider.
* **[!UICONTROL API Secret Key]**: Enter the API Secret Key provided by your SMS provider. This key is used to generate the MAC (Message Authentication Code) for secure communication.
* **[!UICONTROL Mac Authorization Hash Format]**: Choose the hash format for the MAC authentication.

![](assets/sms-byop-mac.png)

>[!TAB OAuth authentication]

Once your API credential is created, complete the fields required for OAuth authentication:

* **[!UICONTROL Name]**​: Enter a name for your OAuth authentication configuration.

* **[!UICONTROL API Token]**​: Enter the API Token provided by your SMS provider.

* **[!UICONTROL OAuth URL]**​: Enter the URL for obtaining the OAuth token.

* **[!UICONTROL OAuth Body]**​: Provide the OAuth request body in JSON format, including parameters such as `grant_type`, `client_id`, and `client_secret`.

![](assets/sms-byop-oauth.png)

>[!TAB JWT authentication]

Once your API credential is created, complete the fields required for JWT authentication:

* **[!UICONTROL Name]**​: Enter a name for your JWT authentication configuration.

* **[!UICONTROL API Token]**​: Enter the API Token provided by your SMS provider.

* **[!UICONTROL JWT Payload]**​: Enter the JSON payload containing the claims required for JWT, such as the issuer, subject, audience, and expiration.

![](assets/sms-byop-jwt.png)

>[!ENDTABS]

## How-to video {#video}

>[!VIDEO](https://video.tv.adobe.com/v/3431625)
