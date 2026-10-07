---
solution: Journey Optimizer, Experience Platform
product: Journey Optimizer
title: Create a decision rule
description: Decision rules are constraints added to a personalized offer and applied to a profile to determine eligibility.
feature: Decision Management, API
badge: label="Legacy" type="Informative"
topic: Integrations
role: Developer
level: Experienced
exl-id: 6a05efca-31bd-46d5-998d-ff3038d9013f
version: Journey Orchestration
TQID: 'https://experienceleague.adobe.com/wpVQ64pwXQz9So3T8MLgooq3gmwEBC28lEq3UllDDL8'
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
  - id: edbd1a0e-46c8-49da-8c10-dba9ec80bba9
    internal-label: Experience Platform
feature_v2:
  - id: ad78185d-8f79-40ad-9bad-cbde74af74ee
    internal-label: Guardrails and limitations
  - id: a4cb03e1-327e-499d-9de8-e0c0db8a63a2
    internal-label: Decision capabilities
  - id: a984631b-2bae-4860-9b15-69c41a799dcb
    internal-label: APIs and SDKs
  - id: 629f438c-ea49-5ade-aa39-c2a256ff3036
    internal-label: API
subfeature_v2:
  - id: a7a194a0-75e2-4913-8a83-14714fbf68e6
    internal-label: Decisioning API
  - id: eb547372-2a95-4d13-b0fd-f720c9895880
    internal-label: Edge Decisioning
  - id: b4e198c6-7f7a-437c-9abd-3255b73e0994
    internal-label: Decision management limitations
role_v2:
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
level_v2:
  - id: d378ca77-2da1-4f39-ad92-1917fe974a38
    internal-label: Experienced
---
# Create a decision rule {#create-decision-rule}

>[!TIP]
>
>Decisioning, [!DNL Adobe Journey Optimizer]'s new decisioning capability, is now available via the code-based experience and email channels! [Learn more](../../../../experience-decisioning/gs-experience-decisioning.md)


Decision rules are constraints added to a personalized offer and applied to a profile to determine eligibility.

## Accept and Content-Type headers {#accept-and-content-type-headers}

The following table shows the valid values which comprise the *Content-Type* field in the request header:

| Header name | Value |
| ----------- | ----- |
| Content-Type | `application/json` |

**API format**

```http
POST /{ENDPOINT_PATH}/offer-rules
```

| Parameter | Description | Example |
| --------- | ----------- | ------- |
| `{ENDPOINT_PATH}` | The endpoint path for persistence APIs. | `https://platform.adobe.io/data/core/dps/` |

**Request**

```shell
curl -X POST 'https://platform.adobe.io/data/core/dps/offer-rules' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer {ACCESS_TOKEN}' \
-H 'x-api-key: {API_KEY}' \
-H 'x-gw-ims-org-id: {IMS_ORG}' \
-H 'x-sandbox-name: {SANDBOX_NAME}' \
-d '{
    "name": "Sales rule",
    "description": "Decisioning rule for sales",
    "condition": {
        "type": "PQL",
        "format": "pql/text",
        "value": "profile.person.name.firstName.equals(\"Joe\", false)"
    },
    "definedOn": {
        "profile": {
            "schema": {
                "ref": "https://ns.adobe.com/xdm/context/profile_union",
                "version": "1"
            },
            "referencePaths": [
                "person.name.firstName"
            ]
        }
    }
}'
```

**Response**

A successful response returns information on the newly created decision rule `id`. You can use the `id` in later steps to update or delete your decision rule or use it in a later tutorial to create decisions, decision rules, and fallback offers.

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
