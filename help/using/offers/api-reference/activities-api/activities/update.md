---
solution: Journey Optimizer, Experience Platform
product: Journey Optimizer
title: Update decisions
description: A decision contains the logic that informs the selection of an offer.
feature: Decision Management, API
badge: label="Legacy" type="Informative"
topic: Integrations
role: Developer
level: Experienced
exl-id: 98c5ccf9-2a7f-4129-a520-d0671a86e13d
version: Journey Orchestration
TQID: https://experienceleague.adobe.com/KUJuVzsryTRtcVfxPPkolvVQyh67PlZCNHAyP87sIIE
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
  - id: edbd1a0e-46c8-49da-8c10-dba9ec80bba9
    internal-label: Experience Platform
feature_v2:
  - id: b3538224-471e-4c63-a444-9b19d89ae29c
    internal-label: Activities
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
# Update a decision {#update-decision}

>[!TIP]
>
>Decisioning, [!DNL Adobe Journey Optimizer]'s new decisioning capability, is now available via the code-based experience and email channels! [Learn more](../../../../experience-decisioning/gs-experience-decisioning.md)


You can modify or update a decision by making a PATCH request to the [!DNL Offer Library] API.

For more information on JSON Patch, including available operations, see the official [JSON Patch documentation](https://jsonpatch.com/).

## Accept and Content-Type headers {#accept-and-content-type-headers}

The following table shows the valid values which comprise the *Content-Type* and *Accept* fields in the request header:

| Header name | Value |
| ----------- | ----- |
| Content-Type | `application/json` |

**API format**

```http
PATCH /{ENDPOINT_PATH}/offer-decisions/{ID}
```

| Parameter | Description | Example |
| --------- | ----------- | ------- |
| `{ENDPOINT_PATH}` | The endpoint path for persistence APIs. | `https://platform.adobe.io/data/core/dps/` |
| `{ID}` | The id of the entity you wish to update. | `offerDecision1234` |

**Request**

```shell
curl -X PATCH 'https://platform.adobe.io/data/core/dps/offer-decisions/offerDecision1234' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer {ACCESS_TOKEN}' \
-H 'x-api-key: {API_KEY}' \
-H 'x-gw-ims-org-id: {IMS_ORG}' \
-H 'x-sandbox-name: {SANDBOX_NAME}' \
-d '[
    {
        "op": "replace",
        "path": "/name",
        "value": "Updated offer decision"
    },
    {
        "op": "replace",
        "path": "/description",
        "value": "Updated offer decision description"
    }
]'
```

| Parameter | Description |
| --------- | ----------- |
| `op` | The operation call used to define the action needed to update the connection. Operations include: `add`, `replace`, `remove`, `copy` and `test`. |
| `path` | The path of the parameter to be updated. |
| `value` | The new value you want to update your parameter with. |

**Response**

A successful response returns the updated details of the decision, including decision `id`.

```json
{
    "etag": 2,
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
