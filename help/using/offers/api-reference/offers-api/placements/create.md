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
  - id: edbd1a0e-46c8-49da-8c10-dba9ec80bba9
    internal-label: Experience Platform
feature_v2:
  - id: ed0d8d0e-04b9-4326-be72-a0fbca265377
    internal-label: Integrations
  - id: fe338112-e2ce-4876-8989-fc4d497613f1
    internal-label: Email
  - id: fe96aceb-8194-4a8a-a6b0-75302d02804d
    internal-label: Integrations
role_v2:
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
topic_v2:
  - id: a004cc84-67b9-4a33-a3a7-8ec7273ef4dc
    internal-label: Metadata
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
