---
title: Getting started
description: Learn how to start using the Offer Library API to perform key operations using the decisioning engine.
feature: Decision Management, API
topic: Integrations
role: Data Engineer
level: Experienced
exl-id: 773bee50-849f-4b07-9423-67de5279ad28
---
# Decision Management API developer guide {#decision-management-api-developer-guide}

>[!CONTEXTUALHELP]
>id="od_api_support"
>title="New decision management APIs"
>abstract="New APIs for creation and management of decision management objects are now available. The legacy apis will be supported until 03/27/2024."

>[!CONTEXTUALHELP]
>id="ajo_decisioning_api_support"
>title="New decision management APIs"
>abstract="New APIs for creation and management of decision management objects are now available. The legacy apis will be supported until 03/27/2024."

This developer guide provides steps to help you start using the [!DNL Offer Library] API. The guide then provides sample API calls for performing key operations using the decisioning engine.

➡️ [Learn more on the components of Decision Management in this video](#video)

## Prerequisites {#prerequisites}

This guide requires a working understanding of the following components of Adobe Experience Platform:

* [[!DNL Experience Data Model (XDM) System]](https://experienceleague.adobe.com/docs/experience-platform/xdm/home.html){target="_blank"}: The standardized framework by which [!DNL Experience Platform] organizes customer experience data.
    * [Basics of schema composition](https://experienceleague.adobe.com/docs/experience-platform/xdm/schema/composition.html){target="_blank"}: Learn about the basic building blocks of XDM schemas.
* [Decision Management](../../../using/offers/get-started/starting-offer-decisioning.md): Explains the concepts and components used for Decisioning in general and decision management in particular. Illustrates the strategies used for choosing the best option to present during a customer's experience.
* [[!DNL Profile Query Language (PQL)]](https://experienceleague.adobe.com/docs/experience-platform/segmentation/pql/overview.html){target="_blank"}: PQL is a powerful language to write expressions over XDM instances. PQL is used to define decision rules.

## Reading sample API calls {#reading-sample-api-calls}

This guide provides example API calls to demonstrate how to format your requests. These include paths, required headers, and properly formatted request payloads. Sample JSON returned in API responses is also provided. For information on the conventions used in documentation for sample API calls, see the section on [how to read example API calls](https://experienceleague.adobe.com/docs/experience-platform/landing/troubleshooting.html#how-do-i-format-an-api-request){target="_blank"} in the [!DNL Experience Platform] troubleshooting guide.

## Gather values for required headers {#gather-values-for-required-headers}

In order to make calls to [!DNL Adobe Experience Platform] APIs, you must first complete the [authentication tutorial](https://experienceleague.adobe.com/docs/experience-platform/landing/platform-apis/api-authentication.html){target="_blank"}. Completing the authentication tutorial provides the values for each of the required headers in all [!DNL Experience Platform] API calls, as shown below:

* `Authorization: Bearer {ACCESS_TOKEN}`
* `x-api-key: {API_KEY}`
* `x-gw-ims-org-id: {IMS_ORG}`
* `x-sandbox-name: {SANDBOX_NAME}`

All requests that contain a payload (POST, PUT, PATCH) require an additional header:

* `Content-Type: application/json`

## Next steps {#next-steps}

This document covered the prerequisite knowledge required to make calls to the [!DNL Offer Library] API. You can now proceed to the sample calls provided in this developer guide and follow along with their instructions.
<!--
>[!NOTE]
>
> The In-app messaging channel in Adobe Journey Optimizer uses decision management objects. If your organization uses the in-app messaging channel, then API list requests for objects will include objects created by the in-app messaging service and can be ignored for decision management use cases. Objects created for in-app messages will have `createdBy = "Mobile_Sheliak"`.
-->

<!-- ## How-to video {#video}

The following video is intended to support your understanding of the components of Decision Management.

>[!VIDEO](https://video.tv.adobe.com/v/329919?quality=12) -->

