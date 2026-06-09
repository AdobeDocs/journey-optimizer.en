---
solution: Journey Optimizer
product: journey optimizer
title: Use Custom Actions to write Journey Events in AEP
description: Use Custom Actions to write Journey Events in AEP
feature: Journeys, Use Cases, Custom Actions
topic: Content Management
role: Developer
level: Experienced
exl-id: 890a194f-f54d-4230-863a-fb2b924d716a
version: Journey Orchestration
TQID: https://experienceleague.adobe.com/TbX3usHKfEM6WQPjFRjo2jCSb78rcbYEWWmV0tpGdj4
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: d998adac-2f81-400b-a669-d07bb196e4eb
    internal-label: Journeys
subfeature_v2:
  - id: b856530c-d60b-42d8-a19d-df2dfd7fe62a
    internal-label: Access control
  - id: c2beecbb-b93e-4ae3-baa9-72adcdc06781
    internal-label: Action configuration
  - id: fa683eda-48de-4558-af32-2673edcd44fe
    internal-label: Events
role_v2:
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
topic_v2:
  - id: eddd9b14-83bd-4ff4-9072-54a4a484abb7
    internal-label: Administration
---
# Use custom actions to write journey events in Experience Platform {#custom-action-aep}

This use case explains how to write custom events into [!DNL Adobe Experience Platform] from Journeys using Custom Actions and Authenticated calls.

## Configure a developer project {#custom-action-aep-IO}

1. From the Adobe Developer Console, click **Project** and open your IO project.

1. In the **Credentials** section, click **OAuth Server-to-Server**.

    ![Custom action configuration screen with action type dropdown](assets/custom-action-aep-1.png)

1. Click **View cURL command**.

    ![[!DNL Adobe Experience Platform] action type selection](assets/custom-action-aep-2.png)

1. Copy the cURL command and store the client_id, client_secret, grant_type and scope.

```
curl -X POST 'https://ims-na1.adobelogin.com/ims/token/v3' -H 'Content-Type: application/x-www-form-urlencoded' -d 'grant_type=client_credentials&client_id=1234&client_secret=5678&scope=openid,AdobeID,read_organizations,additional_info.projectedProductContext,session'
```
 
>[!CAUTION]
>
>After creating your project on the Adobe Developer Console, be sure to grant developer and API access control with the right permissions. Learn more in the [[!DNL Adobe Experience Platform] documentation](https://experienceleague.adobe.com/en/docs/experience-platform/landing/platform-apis/api-authentication#grant-developer-and-api-access-control){target="_blank"}

## Configure the source using HTTP API Inlet

1. Create an endpoint in [!DNL Adobe Experience Platform] to write the data from journeys.

1. In [!DNL Adobe Experience Platform], click **Sources**, under **Connections** in the left menu. Under **HTTP API**, click **Add data**.

    ![Sandbox selection dropdown for [!DNL Adobe Experience Platform]](assets/custom-action-aep-3.png)

1. Select **New account** and enable authentication. Select **Connect to Source**.

    ![Dataset selection interface for streaming data](assets/custom-action-aep-4.png)

1. Select **Next** and the Dataset where you want to write the data. Click **Next** and **Finish**.

    ![XDM schema fields mapped to action parameters](assets/custom-action-aep-5.png)

1. Open the newly created dataflow. Copy the schema payload and save it in your notepad.

```
{
"header": {
"schemaRef": {
"id": "https://ns.adobe.com/<your_org>/schemas/<schema_id>",
"contentType": "application/vnd.adobe.xed-full+json;version=1.0"
},
"imsOrgId": "<org_id>",
"datasetId": "<dataset_id>",
"source": {
"name": "Custom Journey Events"
}
},
"body": {
"xdmMeta": {
"schemaRef": {
"id": "https://ns.adobe.com/<your_org>/schemas/<schema_id>",
"contentType": "application/vnd.adobe.xed-full+json;version=1.0"
}
},
"xdmEntity": {
"_id": "test1",
"<your_org>": {
"journeyVersionId": "",
"nodeId": "", "customer_Id":""
},
"eventMergeId": "",
"eventType": "",
"producedBy": "self",
"timestamp": "2018-11-12T20:20:39+00:00"
}
}
}
```

## Configure the custom action {#custom-action-config}

Custom action configuration is detailed on [this page](../action/about-custom-action-configuration.md).

For this example, follow these steps:

1. Open [!DNL Adobe Journey Optimizer], and click **Configurations**, under **Administration** in the left menu. Under **Actions**, click **Manage** and click **Create Action**.

1. Set the URL and select the Post method. 

    `https://dcs.adobedc.net/collection/<collection_id>?syncValidation=false`

1. Make sure that the Headers (Content-Type, Charset, sandbox-name) are configured.

    ![Custom action in journey canvas with configuration pane](assets/custom-action-aep-7bis.png)

### Set up the authentication {#custom-action-aep-authentication}

1. Select the **Type** as **Custom** with the following Payload.

1. Paste the client_secret, client_id, scope and grant_type (from the IO project payload used before).

    ```
    {
    "type": "customAuthorization",
    "authorizationType": "Bearer",
    "endpoint": "https://ims-na1.adobelogin.com/ims/token/v3",
    "method": "POST",
    "headers": {},
    "body": {
    "bodyType": "form",
    "bodyParams": {
    "grant_type": "client_credentials",
    "client_secret": "********",
    "client_id": "<client_id>",
    "scope": "openid,AdobeID,read_organizations,additional_info.projectedProductContext,session"
    }
    },
    "tokenInResponse": "json://access_token",
    "cacheDuration": {
    "duration": 28000,
    "timeUnit": "seconds"
    }
    }
    ```

1. Use the **Click to test the authentication** button to test the connection.

    ![Parameter mapping interface with expression editor](assets/custom-action-aep-8.png)

### Set up the payload {#custom-action-aep-payload}

1. In the **Request** and **Response** fields, paste the payload from the source connection used before.

    ```
    {
    "xdmMeta": {
    "schemaRef": {
    "id": "https://ns.adobe.com/<your_org>/schemas/<schema_id>",
    "contentType": "application/vnd.adobe.xed-full+json;version=1.0"
    }
    },
    "xdmEntity": {
    "_id": "/uri-reference",
    "<your_org>": {
    "journeyVersionId": "Sample value",
    "nodeId": "Sample value",
    "customer_Id":""
    },
    "eventMergeId": "Sample value",
    "eventType": "advertising.completes,
    "producedBy": "self",
    "timestamp": "2018-11-12T20:20:39+00:00"
    }
    }
    ```

1. Change the Field Configuration from **Constant** to **Variable** for fields which will be populated dynamically. 

1. Save the Custom Action.

## Journey

1. Finally, use this custom action in a journey to write the custom journey events.

1. Populate the Journey Version Id, Node Id, Node Name and other attributes according to your use case.

    ![Advanced mode editor for complex field mapping](assets/custom-action-aep-9.png)

+++AI Assistant — Page context

- **TL;DR:** This use case explains how to configure a custom action in Journey Optimizer that writes journey event data into Adobe Experience Platform using an HTTP API inlet and OAuth Server-to-Server authenticated calls.

**Intents:**
- Set up an Adobe Developer Console IO project with OAuth Server-to-Server credentials for AEP API authentication
- Create an HTTP API inlet source in Adobe Experience Platform to receive streaming journey event data
- Configure a custom action in Journey Optimizer with the correct URL, headers, and custom Bearer token authentication
- Map journey fields (journey version ID, node ID, customer ID) dynamically as variables in the custom action payload
- Use the custom action in a journey to write custom events to an AEP dataset

**Glossary:**
- **HTTP API Inlet**: An Adobe Experience Platform source connector that creates a streaming endpoint for ingesting data via HTTP POST requests *(product-specific)*
- **OAuth Server-to-Server**: An authentication credential type in Adobe Developer Console that generates Bearer tokens for server-to-server API calls without user interaction *(product-specific)*
- **Custom authorization**: A Journey Optimizer custom action authentication type that fetches a Bearer token from a specified endpoint and caches it for a configured duration *(product-specific)*
- **XDM entity**: The data payload structure conforming to the Experience Data Model schema, used as the body when writing events to AEP via the HTTP API inlet *(product-specific)*
- **cacheDuration**: The token cache setting in custom authorization configuration that controls how long the fetched Bearer token is reused before a new one is requested *(product-specific)*

**Guardrails:**
- After creating the Adobe Developer Console project, developer and API access control permissions must be explicitly granted before the credentials can be used
- The HTTP API inlet source must be created with authentication enabled; the connection endpoint URL and schema payload must be copied and stored for use in the custom action configuration
- Custom action headers must include Content-Type, Charset, and sandbox-name
- Fields intended to be populated dynamically at runtime must be changed from Constant to Variable in the custom action payload configuration

**Terminology:**
- Canonical name: Custom action — Acronym: none — variants: custom action configuration, Journey Optimizer custom action
- Canonical name: Adobe Experience Platform — Acronym: AEP — variants: Experience Platform, Platform
- Synonyms: "HTTP API Inlet" = "streaming endpoint" = "DCS collection endpoint"
- Do not confuse: "OAuth Server-to-Server" ≠ "OAuth user authentication" (Server-to-Server does not require a user login; it uses client credentials)

**FAQ:**
- **Q: What type of authentication is used to call the AEP HTTP API Inlet from a Journey Optimizer custom action?** — Custom Bearer token authentication using OAuth Server-to-Server client credentials fetched from the Adobe IMS token endpoint.
- **Q: Where do I find the client_id, client_secret, grant_type, and scope values?** — From the OAuth Server-to-Server credentials section of your Adobe Developer Console IO project, by clicking "View cURL command."
- **Q: How do I make journey-specific fields (e.g., journeyVersionId, nodeId) dynamic in the payload?** — Change their field configuration from Constant to Variable in the custom action payload setup so they are populated from the journey context at runtime.
- **Q: What permissions are required on the Adobe Developer Console project?** — Developer and API access control must be granted with the right permissions after the project is created, as described in the AEP API authentication documentation.
- **Q: What is the purpose of the cacheDuration setting in the authentication payload?** — It controls how long the fetched Bearer token is cached and reused (28,000 seconds in the example) before the custom action requests a new token.

+++
