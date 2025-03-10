---
title: Delete an eligibility rule
description: Eligibility rules allow you to define the eligible candidates based on what you want to target, such as profile attributes and audiences.
feature: Decision Management, API, Collections
topic: Integrations
role: Data Engineer
level: Experienced
---
# Delete an eligibility rule {#delete-eligibility-rule}

It may occasionally be necessary to remove (DELETE) an eligibility rule. This is done by performing a DELETE request to the Offer Library API using the ID of the eligibility rule you wish to delete.

**API format**

```http
DELETE /{ENDPOINT_PATH}/eligibility-rules/{ID}
```

| Parameter | Description | Example |
| --------- | ----------- | ------- |
| `{ENDPOINT_PATH}` | The endpoint path for persistence APIs. | `https://platform.adobe.io/data/core/dps` |
| `{ID}` | The id of the entity you wish to delete.| `rule1234` |

**Request**

```shell
curl -X DELETE 'https://platform.adobe.io/data/core/dps/offer-rules/rule1234' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer {ACCESS_TOKEN}' \
-H 'x-api-key: {API_KEY}' \
-H 'x-gw-ims-org-id: {IMS_ORG}' \
-H 'x-sandbox-name: {SANDBOX_NAME}'
```

**Response**

A successful response returns HTTP status 200 and a blank body.

You can confirm the deletion by attempting a lookup (GET) request to the rule. You should receive an HTTP status 404 (Not Found) because the rule has been removed.
