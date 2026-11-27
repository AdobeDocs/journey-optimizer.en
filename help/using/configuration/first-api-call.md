---
solution: Journey Optimizer
product: journey optimizer
title: Make your first Journey Optimizer API call
description: Create your credentials, get an access token, and send your first request to a Journey Optimizer API.
feature: Integrations, Data Ingestion
role: Developer
level: Intermediate
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: d556b755-390a-43f0-be32-a08cf6236126
    internal-label: Configuration
  - id: fe96aceb-8194-4a8a-a6b0-75302d02804d
    internal-label: Integrations
  - id: aeebb91a-f216-4d5f-8da1-3a7e6f696ed0
    internal-label: Data management activity
subfeature_v2:
  - id: cf3fbcd7-c075-4ae4-8de5-96e736ab2ea3
    internal-label: Data ingestions
role_v2:
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
level_v2:
  - id: b5a62a22-46f7-4f0d-b151-3fc640bef588
    internal-label: Intermediate
topic_v2:
  - id: bbbea26f-9621-49eb-9ab8-e06fb3bbce8c
    internal-label: Artificial intelligence
  - id: bce87dde-a4ab-44c9-8a18-ad66e4ddb377
    internal-label: Customer experience
  - id: cdd65e7e-8839-44a2-bc21-0e03623b5dd1
    internal-label: Optimization
  - id: e0eb8757-182f-49f3-94a4-1587d16f5094
    internal-label: Personalization
  - id: eb30f47f-d87a-400f-8f78-63ce7979ff56
    internal-label: Machine learning
---
# Make your first [!DNL Journey Optimizer] API call {#first-api-call}

>[!BEGINSHADEBOX]

**On this page:** Set up credentials, get an access token, and send a first read-only request to a [!DNL Journey Optimizer] API so you can confirm that your setup works before you build an integration.

>[!ENDSHADEBOX]

## Before you start {#prerequisites}

* You have access to [Adobe Developer Console](https://developer.adobe.com/console){target="_blank"} in your organization.
* An administrator can add permissions to a product profile in the Adobe Admin Console.
* You know the name of the sandbox you want to work in. API calls run against one sandbox. Use a development sandbox for your first call. [Learn about sandboxes](https://experienceleague.adobe.com/docs/experience-platform/sandbox/home.html){target="_blank"}

## Step 1: Create credentials {#credentials}

1. In Adobe Developer Console, create a project and add the Journey Optimizer API to it with the **OAuth Server-to-Server** method. The JWT method is deprecated.
1. Ask your administrator to add the permissions that the endpoint needs to the product profile linked to your project. For example, the Journeys API requires **Journey Manage** and **Journey View** on the target sandbox.
1. From the project, copy the API key (client ID) and note your organization ID.

The detailed steps are in [Authentication](https://developer.adobe.com/journey-optimizer-apis/references/authentication){target="_blank"}. For a full walkthrough of the Developer Console project, OAuth Server-to-Server credentials, and product profiles, see [Authenticate and access Experience Platform APIs](https://experienceleague.adobe.com/en/docs/experience-platform/landing/platform-apis/api-authentication#generate-credentials){target="_blank"}.

## Step 2: Get an access token {#token}

Request an access token with your client ID and client secret. Copy the scopes from the credential details of your project in Adobe Developer Console.

```bash
curl -X POST 'https://ims-na1.adobelogin.com/ims/token/v3' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'grant_type=client_credentials&client_id={API_KEY}&client_secret={CLIENT_SECRET}&scope={SCOPES}'
```

The response contains the `access_token` value to use as `{ACCESS_TOKEN}` in the next step. Access tokens expire, so request a new token when a call returns a `401` error. For scopes and other ways to generate a token, see [Generate an access token](https://experienceleague.adobe.com/en/docs/experience-platform/landing/platform-apis/api-authentication#generate-access-token){target="_blank"}.

## Step 3: Send a read-only request {#request}

Start with a request that only reads data. This example lists journeys with the [Journeys API](https://developer.adobe.com/journey-optimizer-apis/references/journeys-retrieve){target="_blank"}. The `pageSize` parameter limits the number of results.

```bash
curl -X GET 'https://platform.adobe.io/ajo/journey?pageSize=5' \
  -H 'Authorization: Bearer {ACCESS_TOKEN}' \
  -H 'x-api-key: {API_KEY}' \
  -H 'x-gw-ims-org-id: {IMS_ORG}' \
  -H 'x-sandbox-name: {SANDBOX_NAME}' \
  -H 'Content-Type: application/json'
```

Replace each placeholder with the values from the previous steps. You can also send the request from the interactive console on the API reference page, or use the [Journey public API Postman collection](https://github.com/AdobeDocs/journey-optimizer-apis/blob/main/static/Journey_public_API_postman_collection.json){target="_blank"}.

The response is a paginated list. This abbreviated example shows the main properties:

```json
{
  "results": [
    {
      "id": "{JOURNEY_ID}",
      "name": "Welcome journey",
      "version": "1",
      "type": "unitary",
      "status": "Draft",
      "imsOrgId": "{IMS_ORG}",
      "sandboxName": "{SANDBOX_NAME}"
    }
  ],
  "page": 0,
  "limit": 5,
  "pages": 1
}
```

The `page` value starts at 0. Add `page` to the request to retrieve the next set of results. Use `fields` to return only some properties.

A `200` response with a JSON body confirms that your credentials, permissions, and sandbox are set correctly. To test your credentials without a Journey Optimizer endpoint, see [Test access credentials](https://experienceleague.adobe.com/en/docs/experience-platform/landing/platform-apis/api-authentication#test-credentials){target="_blank"}.

## Fix common errors {#errors}

| Response | Likely cause | What to do |
| -------- | ------------ | ---------- |
| `401` | The access token is missing, malformed, or expired | Generate a new token and check the `Authorization` header |
| `403` | The product profile does not include the permission the endpoint needs, or the integration is not linked to the profile | Ask your administrator to check the product profile permissions on the target sandbox |
| `404` or an empty result | The path is wrong, or the sandbox does not contain the object | Check the endpoint path and the `x-sandbox-name` value |

For errors returned by a specific API, see [Troubleshoot API calls](ajo-apis.md#troubleshooting). For error code meanings, see the [Error codes reference](../building-journeys/error-codes-reference.md).

## Step 4: Move to a real use case {#use-case}

When the read-only call works, move to the call your integration needs. For example, to send an order confirmation from your own system, create an [API-triggered campaign](../campaigns/api-triggered-campaigns.md) and call the Interactive Message Execution API. See the [code samples](https://developer.adobe.com/journey-optimizer-apis/references/messaging-samples){target="_blank"} and the [Send transactional messages](../start/onboarding-hub.md#build-transactional) use case.

## Next steps {#next-steps}

* [Work with Journey Optimizer APIs](ajo-apis.md): find the API for your task.
* [Get started for developers](../start/path/developer.md): SDKs, events, and custom actions.
