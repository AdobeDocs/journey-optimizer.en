---
title: Lookup an eligibility rule
description: Eligibility rules allow you to define the eligible candidates based on what you want to target, such as profile attributes and audiences.
feature: API, Collections, Decisioning
topic: Integrations
role: Developer
level: Experienced
exl-id: a74f4c87-0b89-4583-97f5-df8e2a30a19b
version: Journey Orchestration
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: a4cb03e1-327e-499d-9de8-e0c0db8a63a2
    internal-label: Decision capabilities
  - id: a984631b-2bae-4860-9b15-69c41a799dcb
    internal-label: APIs and SDKs
  - id: 629f438c-ea49-5ade-aa39-c2a256ff3036
    internal-label: API
  - id: afaef773-049d-566d-8a3b-49ba521f73e5
    internal-label: Collections
subfeature_v2:
  - id: a7a194a0-75e2-4913-8a83-14714fbf68e6
    internal-label: Decisioning API
  - id: eb547372-2a95-4d13-b0fd-f720c9895880
    internal-label: Edge Decisioning
role_v2:
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
level_v2:
  - id: d378ca77-2da1-4f39-ad92-1917fe974a38
    internal-label: Experienced
---
# Lookup a eligibility rule {#list-eligibility-rule}

You can look up specific eligibility rule by making a GET request to the Offer Library API that includes the ID in the request path.

**API format**

```http
GET /{ENDPOINT_PATH}/offer-rules/{ID}
```

| Parameter | Description | Example |
| --------- | ----------- | ------- |
| `{ENDPOINT_PATH}` | The endpoint path for persistence APIs. | `https://platform.adobe.io/data/core/dps` |
| `{ID}` | The ID of the entity you wish to look up. | `rule1234` |

**Request**

```shell
curl -X GET 'https://platform.adobe.io/data/core/dps/offer-rules/rule1234' \
-H 'Accept: *,application/json' \
-H 'Authorization: Bearer {ACCESS_TOKEN}' \
-H 'x-api-key: {API_KEY}' \
-H 'x-gw-ims-org-id: {IMS_ORG}' \
-H 'x-sandbox-name: {SANDBOX_NAME}'
```

**Response**

A successful response returns the details of the eligibility rule.

```json
{
    "created": "2024-10-28T01:18:08.506Z",
    "modified": "2024-10-28T01:18:08.506Z",
    "etag": 1,
    "schemas": [
        "https://ns.adobe.com/experience/offer-management/eligibility-rule"
    ],
    "createdBy": "3254197F65569E890A49422F@658557135fa10b860a494019",
    "lastModifiedBy": "3254197F65569E890A49422F@658557135fa10b860a494019",
    "id": "dps:eligibility-rule:19af09a9ae45a8d3",
    "name": "dasdsa",
    "description": "",
    "exdRule": false,
    "condition": {
        "type": "PQL",
        "format": "pql/text",
        "value": "personalEmail.address.equals(\"youz@adobe.com\", false)"
    },
    "segmentModel": {
        "lifecycleState": "published",
        "expression": {
            "isValid": true,
            "logicalOperator": "and",
            "profileAttributesContainer": {
                "exclude": false,
                "items": [
                    {
                        "comparisonType": "equals",
                        "component": {
                            "id": "profile.personalEmail.address",
                            "__entity__": true,
                            "type": "Sz"
                        },
                        "isCaseSensitive": false,
                        "isPlaceholder": false,
                        "originalLocation": [],
                        "value": [
                            "youz@adobe.com"
                        ],
                        "itemType": "segmentRule"
                    }
                ],
                "logicalOperator": "and",
                "itemType": "segmentContainer"
            },
            "xEventAttributesContainer": {
                "exclude": false,
                "items": [],
                "logicalOperator": "then",
                "itemType": "eventTypeCardContainer"
            },
            "itemType": "segmentDefinition"
        },
        "isMissingAnsibleModel": false,
        "relationalExpression": false,
        "deprecated": {
            "status": false,
            "reason": ""
        },
        "description": "",
        "evaluationInfo": {
            "batch": {
                "enabled": true
            },
            "continuous": {
                "enabled": false
            },
            "synchronous": {
                "enabled": false
            }
        },
        "labels": [],
        "tags": [],
        "canHaveFolder": true,
        "mergePolicyId": "24526dbe-d615-4d41-9ebb-fd7f2b3dcdc2",
        "name": "dasdsa",
        "namespace": "ups"
    }
}
```
