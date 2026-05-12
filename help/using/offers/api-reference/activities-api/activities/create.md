---
solution: Journey Optimizer, Experience Platform
product: Journey Optimizer
title: Create a decision
description: A decision contains the logic that informs the selection of an offer.
feature: Decision Management, API
badge: label="Legacy" type="Informative"
topic: Integrations
role: Developer
level: Experienced
exl-id: 553501b0-30a9-4795-9a9d-f42df5f4f2ea
version: Journey Orchestration
TQID: https://experienceleague.adobe.com/-57HbAxL7djYDOGFu3K2exAml8pes6WiYVfwW-dGCeE
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
  - id: edbd1a0e-46c8-49da-8c10-dba9ec80bba9
    internal-label: Experience Platform
feature_v2:
  - id: b3538224-471e-4c63-a444-9b19d89ae29c
    internal-label: Activities
  - id: c132d929-fa62-4271-803e-b823be07b914
    internal-label: Profile
  - id: ed0d8d0e-04b9-4326-be72-a0fbca265377
    internal-label: Integrations
  - id: fe338112-e2ce-4876-8989-fc4d497613f1
    internal-label: Email
  - id: fe96aceb-8194-4a8a-a6b0-75302d02804d
    internal-label: Integrations
role_v2:
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
---
# Create a decision {#create-decision}

>[!TIP]
>
>Decisioning, [!DNL Adobe Journey Optimizer]'s new decisioning capability, is now available via the code-based experience and email channels! [Learn more](../../../../experience-decisioning/gs-experience-decisioning.md)


You can create a decision by making a POST request to the [!DNL Offer Library] API.

## Accept and Content-Type headers {#accept-and-content-type-headers}

The following table shows the valid values which comprise the *Content-Type* and *Accept* fields in the request header:

| Header name | Value |
| ----------- | ----- |
| Content-Type | `application/json` |

**API format**

```http
POST /{ENDPOINT_PATH}/offer-decisions
```

| Parameter | Description | Example |
| --------- | ----------- | ------- |
| `{ENDPOINT_PATH}` | The endpoint path for persistence APIs. | `https://platform.adobe.io/data/core/dps/` |

**Request**

```shell
curl -X POST 'https://platform.adobe.io/data/core/offer-decisions' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer {ACCESS_TOKEN}' \
-H 'x-api-key: {API_KEY}' \
-H 'x-gw-ims-org-id: {IMS_ORG}' \
-H 'x-sandbox-name: {SANDBOX_NAME}' \
-d '{
    "name": "Test Offer Decision",
    "description": "Offer Decision description",
    "status": "live",
    "startDate": "2021-08-23T07:00:00.000+00:00",
    "endDate": "2021-08-25T07:00:00.000+00:00",
    "fallback": "fallbackOffer1234",
    "criteria": [
        {
            "placements": [
                "offerPlacement1234",
                "offerPlacement5678"
            ],
            "rank": {
                "priority": 0,
                "order": {
                    "orderEvaluationType": "ranking-strategy",
                    "rankingStrategy": "123456789123"
                }
            },
            "profileConstraint": {
                "profileConstraintType": "none"
            },
            "optionSelection": {
                "filter": "offerCollection1234"
            }
        }
    ]
}'
```

**Response**

A successful response returns information on the newly created decision, including its unique `id`. You can use the `id` in later steps to update or delete your decision.

```json
{
  "etag": 1,
    "createdBy": "{CREATED_BY}",
    "lastModifiedBy": "{MODIFIED_BY}",
    "id": "{ID}",
    "sandboxId": "{SANDBOX_ID}",
    "createdDate": "2023-05-31T15:09:11.771Z",
    "lastModifiedDate": "2023-05-31T15:09:11.771Z",
    "createdByClientId": "{CREATED_CLIENT_ID}",
    "lastModifiedByClientId": "{MODIFIED_CLIENT_ID}"
}
```
