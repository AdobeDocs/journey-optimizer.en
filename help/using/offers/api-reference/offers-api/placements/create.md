---
solution: Journey Optimizer, Experience Platform
product: Journey Optimizer
title: Create a placement
description: Placements are containers that are used to showcase your offers.
feature: Decision Management, API
badge: label="Legacy" type="Informative"
topic: Integrations
role: Developer
level: Experienced
exl-id: 7b735873-86f5-466f-b079-5e84d9f03a08
version: Journey Orchestration
TQID: https://experienceleague.adobe.com/PejC1r03FVJHa-wZGWejoDr3Tla3w7S6Os-kn7GD7R4
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: a4cb03e1-327e-499d-9de8-e0c0db8a63a2
    internal-label: Decision capabilities (AJO)
  - id: ad78185d-8f79-40ad-9bad-cbde74af74ee
    internal-label: Guardrails and limitations
role_v2:
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
topic_v2:
  - id: a004cc84-67b9-4a33-a3a7-8ec7273ef4dc
    internal-label: Metadata
subfeature_v2:
  - id: a7a194a0-75e2-4913-8a83-14714fbf68e6
    internal-label: Decisioning API
  - id: eb547372-2a95-4d13-b0fd-f720c9895880
    internal-label: Edge Decisioning (AJO)
---
# Create a placement {#create-placement}

>[!TIP]
>
>Decisioning, [!DNL Adobe Journey Optimizer]'s new decisioning capability, is now available via the code-based experience and email channels! [Learn more](../../../../experience-decisioning/gs-experience-decisioning.md)


You can create a placement by making a POST request to the [!DNL Offer Library] API.

## Accept and Content-Type headers {#accept-and-content-type-headers}

The following table shows the valid values which comprise the *Content-Type* field in the request header:

| Header name | Value |
| ----------- | ----- |
| Content-Type | `application/json` |

**API format**

```http
POST /{ENDPOINT_PATH}/placements
```

| Parameter | Description | Example |
| --------- | ----------- | ------- |
| `{ENDPOINT_PATH}` | The endpoint path for persistence APIs. | `https://platform.adobe.io/data/core/dps/` |

**Request**

```shell
curl -X POST 'https://platform.adobe.io/data/core/dps/placements' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer {ACCESS_TOKEN}' \
-H 'x-api-key: {API_KEY}' \
-H 'x-gw-ims-org-id: {IMS_ORG}' \
-H 'x-sandbox-name: {SANDBOX_NAME}' \
-d '{
    "name": "New placement",
    "description": "Placement description",
    "componentType": "html",
    "channel": "https://ns.adobe.com/xdm/channel-types/email",
    "itemCount": 1,
    "allowDuplicatePlacements": false,
    "returnContent": true,
    "returnMetaData": {
        "decisionName": false,
        "offerName": false,
        "offerAttributes": false,
        "offerPriority": false,
        "placementName": false,
        "channelType": false,
        "contentType": false
    }
}'
```

**Response**

A successful response returns the details of the newly created placement, and placement `id`. You can use the it later steps to update or delete your placement. You can use your unique placement `id` in later tutorials to create decisions, decision rules, and fallback offers.

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
