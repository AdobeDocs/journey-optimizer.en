---
solution: Journey Orchestration
title: Configure a custom action
description: Learn how to configure a custom action
feature: Actions
topic: Administration
role: Admin
level: Intermediate
exl-id: 4df2fc7c-85cb-410a-a31f-1bc1ece237bb
---
# Configure a custom action {#configure-an-action}

If you are using a third-party system to send messages or if you want journeys to send API calls to a third-party system, use custom actions to configure its connection to your journey. For example you can connect to the following systems with custom actions: Epsilon, Slack, Adobe.io, Firebase, etc.

Custom actions are additional actions defined by technical users and made available to marketers. Once configured, they appear in the left palette of your journey, in the **[!UICONTROL Action]** category. Learn more in [this page](../building-journeys/about-journey-activities.md#action-activities). 

## Limitations{#custom-actions-limitations}

Custom actions come with a few limitations listed in [this page](../start/limitations.md).

In custom action parameters, you can pass a simple collection, as well as a collection of objects. Learn more about collection limitations in [this page](../building-journeys/collections.md#limitations). 

Also note that the custom actions parameters have an expected format (example: string, decimal, etc.). You must be careful to respect these expected formats. Learn more in this [use case](../building-journeys/collections.md).


## Configuration steps {#configuration-steps}

Here are the main steps required to configure a custom action:

1. In the ADMINISTRATION menu section, select **[!UICONTROL Configurations]**. In the  **[!UICONTROL Actions]** section, click **[!UICONTROL Manage]**. Click **[!UICONTROL Create Action]** to create a new action. The action configuration pane opens on the right side of the screen.

    ![](assets/custom2.png)

1. Enter a name for your action.

    >[!NOTE]
    >
    >Do not use spaces or special characters. Do not use more than 30 characters.

1. Add a description to your action. This step is optional.
1. The number of journeys that use this action is displayed in the **[!UICONTROL Used in]** field. You can click the **[!UICONTROL View journeys]** button to display the list of  journeys using this action.
1. Define the different **[!UICONTROL URL Configuration]** parameters. See [this page](../action/about-custom-action-configuration.md#url-configuration).
1. Configure the **[!UICONTROL Authentication]** section. This configuration is the same as for data sources.  See [this section](../datasource/external-data-sources.md#custom-authentication-mode).
1. Define the **[!UICONTROL Action parameters]**. See [this page](../action/about-custom-action-configuration.md#define-the-message-parameters).
1. Click **[!UICONTROL Save]**.

    The custom action is now configured and ready to be used in your journeys. See [this page](../building-journeys/about-journey-activities.md#action-activities).

    >[!NOTE]
    >
    >When a custom action is used in a journey, most parameters are read-only. You can only modify the **[!UICONTROL Name]**, **[!UICONTROL Description]**, **[!UICONTROL URL]** fields and the **[!UICONTROL Authentication]** section.

## URL configuration {#url-configuration}

When configuring a custom action, you need to define the following **[!UICONTROL URL Configuration]** parameters:

![](assets/journeyurlconfiguration.png)

1. In the **[!UICONTROL URL]** field, specify the URL of the external service:

    * If the URL is static, enter the URL in this field.

    * If the URL includes a dynamic path, enter only the static part of the URL, that is, the scheme, the host, the port, and, optionally, a static part of the path.

        Example: `https://xxx.yyy.com/somethingstatic/`

        You will specify the dynamic path of the URL when adding the custom action to a journey. [Learn more](../building-journeys/using-custom-actions.md).

    >[!NOTE]
    >
    >For security reasons, we strongly recommend that you use the HTTPS scheme for the URL. We don't allow the use of Adobe addresses that are not public and the use of IP addresses.
    >
    >Only the default ports are allowed when defining a custom action: 80 for http and 443 for https.

1. Select the call **[!UICONTROL Method]**: it can be either **[!UICONTROL POST]** or **[!UICONTROL PUT]**.
1. In the **[!UICONTROL Headers]** section, define the HTTP headers of the request message to be sent to the external service:
   1. To add a header field, click **[!UICONTROL Add a header field]**.
   1. Enter the key of the header field.
   1. To set a dynamic value for the key-value pair, select **[!UICONTROL Variable]**. Otherwise, select **[!UICONTROL Constant]**.

        For example, for a timestamp, you can set a dynamic value.

   1. If you have selected **[!UICONTROL Constant]**, then enter the constant value.

       If you have selected **[!UICONTROL Variable]**, then you will specify this variable when adding the custom action to a journey. [Learn more](../building-journeys/using-custom-actions.md).

       ![](assets/journeyurlconfiguration2.png)

   1. To delete a header field, point to the header field and click the **[!UICONTROL Delete]** icon.

    The **[!UICONTROL Content-Type]** and **[!UICONTROL Charset]** header fields are set by default. You cannot modify or delete these fields.

    After you have added the custom action to a journey, you can still add header fields to it if the journey is in draft status. If you do not want the journey to be affected by configuration changes, duplicate the custom action and add the header fields to the new custom action.

    >[!NOTE]
    >
    >Headers are validated according to field parsing rules. [Learn more](https://tools.ietf.org/html/rfc7230#section-3.2.4).

## Define the action parameters {#define-the-message-parameters}

![](assets/messageparameterssection.png)

In the **[!UICONTROL Action parameters]** section, paste an example of the JSON payload to send to the external service.

![](assets/customactionpayloadmessage.png)

>[!NOTE]
>
>Field names in the payload cannot contain a "." character. They cannot start with a "$" character.

You will be able to define the parameter type (e.g.: string, integer, etc.).

You will also have a choice between specifying if a parameter is a constant or a variable:

* Constant means that the value of the parameter is defined in the action configuration pane by a technical persona. The value will be always the same across journeys. It will not vary and the marketer won’t see it when using the custom action in the journey. It could be for example an ID the third-party system expects. In that case, the field on the right of the toggle constant/variable is the value passed.
* Variable means the value of the parameter will vary. Marketers using this custom action in a journey will be free to pass the value they wants or to specify where to retrieve the value for this parameter (e.g. from the event, from the Adobe Experience  Platform, etc.). In that case, the field on the right of the toggle constant/variable is the label marketers will see in the journey to name this parameter.

![](assets/customactionpayloadmessage2.png)
