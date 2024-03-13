---
title: Create a decision rule
description: Decision rules are constraints added to a personalized offer and applied to a profile to determine eligibility.
feature: Decision Management, API
topic: Integrations
role: Data Engineer
level: Experienced
exl-id: 12c49f4c-a1b5-4841-ab98-663b4c771fb6
---
# Create a decision rule {#create-decision-rule}

Decision rules are constraints added to a personalized offer and applied to a profile to determine eligibility.

## Accept and Content-Type headers {#accept-and-content-type-headers}

The following table shows the valid values which comprise the *Content-Type* and *Accept* fields in the request header:

| Header name | Value |
| ----------- | ----- |
| Accept | `application/vnd.adobe.platform.xcore.xdm.receipt+json; version=1` |
| Content-Type | `application/schema-instance+json; version=1;  schema="https://ns.adobe.com/experience/offer-management/eligibility-rule;version=0.3"` |

**API format**

```http
POST /{ENDPOINT_PATH}/{CONTAINER_ID}/instances
```

| Parameter | Description | Example |
| --------- | ----------- | ------- |
| `{ENDPOINT_PATH}` | The endpoint path for repository APIs. | `https://platform.adobe.io/data/core/xcore/` |
| `{CONTAINER_ID}` | The container where the decision rules are located. | `e0bd8463-0913-4ca1-bd84-6309134ca1f6` |

**Request**

```shell
curl -X POST \
  'https://platform.adobe.io/data/core/xcore/e0bd8463-0913-4ca1-bd84-6309134ca1f6/instances' \
  -H 'Accept: application/vnd.adobe.platform.xcore.xdm.receipt+json; version=1' \
  -H 'Content-Type: application/schema-instance+json; version=1;  schema="https://ns.adobe.com/experience/offer-management/eligibility-rule;version=0.3"' \
-H 'Authorization: Bearer {ACCESS_TOKEN}' \
-H 'x-api-key: {API_KEY}' \
-H 'x-gw-ims-org-id: {IMS_ORG}' \
-H 'x-sandbox-name: {SANDBOX_NAME}' \
-d '{
    "xdm:name": "Sales rule",
    "description": "Decisioning rule for sales",
    "xdm:condition": {
        "xdm:type": "PQL",
        "xdm:format": "pql/text",
        "xdm:value": "profile.person.name.firstName.equals(\"Joe\", false)"
    },
    "xdm:definedOn": {
        "profile": {
            "xdm:schema": {
                "$ref": "https://ns.adobe.com/xdm/context/profile_union",
                "version": "1"
            },
            "xdm:referencePaths": [
                "person.name.firstName"
            ]
        }
    }
}'
```

**Response**

A successful response returns information on the newly created decision rule, including its unique instance ID and placement `@id`. You can use the instance ID in later steps to update or delete your decision rule. You can use your unique decision rule `@id` in a later tutorial to create personalized offers.

```json
{
    "instanceId": "eaa5af90-13d9-11eb-9472-194dee6dc381",
    "@id": "xcore:eligibility-rule:124e0faf5b8ee89b",
    "repo:etag": 1,
    "repo:createdDate": "2023-10-21T20:13:43.048666Z",
    "repo:lastModifiedDate": "2023-10-21T20:13:43.048666Z",
    "repo:createdBy": "{CREATED_BY}",
    "repo:lastModifiedBy": "{MODIFIED_BY}",
    "repo:createdByClientId": "{CREATED_CLIENT_ID}",
    "repo:lastModifiedByClientId": "{MODIFIED_CLIENT_ID}"
}
```
