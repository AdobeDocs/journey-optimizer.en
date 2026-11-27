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

**On this page:** Get credentials and an access token, then send a read-only request to confirm that your setup works.

>[!ENDSHADEBOX]

## Before you start {#prerequisites}

* You have access to [Adobe Developer Console](https://developer.adobe.com/console){target="_blank"}, and an administrator can update your product profile.
* You know the sandbox to use. API calls run against one sandbox, so use a development sandbox for your first call.

## Step 1: Create credentials {#credentials}

1. In Adobe Developer Console, create a project and add the Journey Optimizer API with the **OAuth Server-to-Server** method.
1. Ask your administrator to add the endpoint permissions to the product profile linked to your project. The Journeys API requires **Journey Manage** and **Journey View** on the target sandbox.
1. Copy the API key (client ID) and note your organization ID.

For the detailed steps, see [Authentication](https://developer.adobe.com/journey-optimizer-apis/references/authentication){target="_blank"} and [Authenticate and access Experience Platform APIs](https://experienceleague.adobe.com/en/docs/experience-platform/landing/platform-apis/api-authentication#generate-credentials){target="_blank"}.

## Step 2: Get an access token {#token}

Copy the scopes from the credential details of your project, then request a token:

```bash
curl -X POST 'https://ims-na1.adobelogin.com/ims/token/v3' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'grant_type=client_credentials&client_id={API_KEY}&client_secret={CLIENT_SECRET}&scope={SCOPES}'
```

Use the `access_token` value from the response as `{ACCESS_TOKEN}`. Tokens expire, so request a new one after a `401` error. [Learn more about access tokens](https://experienceleague.adobe.com/en/docs/experience-platform/landing/platform-apis/api-authentication#generate-access-token){target="_blank"}

## Step 3: Send a read-only request {#request}

This example lists journeys with the [Journeys API](https://developer.adobe.com/journey-optimizer-apis/references/journeys-retrieve){target="_blank"}:

```bash
curl -X GET 'https://platform.adobe.io/ajo/journey?pageSize=5' \
  -H 'Authorization: Bearer {ACCESS_TOKEN}' \
  -H 'x-api-key: {API_KEY}' \
  -H 'x-gw-ims-org-id: {IMS_ORG}' \
  -H 'x-sandbox-name: {SANDBOX_NAME}'
```

A `200` response confirms that your credentials, permissions, and sandbox are set correctly. The response looks like this (abbreviated):

```json
{
  "results": [
    { "id": "{JOURNEY_ID}", "name": "Welcome journey", "status": "Draft" }
  ],
  "page": 0,
  "limit": 5,
  "pages": 1
}
```

## Fix common errors {#errors}

| Response | Cause and fix |
| -------- | ------------- |
| `401` | The access token is missing or expired. Request a new token. |
| `403` | The product profile lacks the endpoint permission. Ask your administrator to check it on the target sandbox. |

For other errors, see [Troubleshoot API calls](ajo-apis.md#troubleshooting).

## Next steps {#next-steps}

* [Work with Journey Optimizer APIs](ajo-apis.md): find the API for your task.
* [Send transactional messages](../start/onboarding-hub.md#build-transactional): trigger a message from your system with an API-triggered campaign.
