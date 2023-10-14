---
title: Delete a collection
description: Collections are subsets of offers based on predefined conditions defined by a marketer, such as category of the offer.
feature: Offers, API, Collections
topic: Integrations
role: Data Engineer
level: Experienced
exl-id: 2eaa0092-2436-4679-83f1-7530ab4a858f
---
# Delete a collection {#delete-collection}

It may occasionally be necessary to remove (DELETE) a collection. This is done by performing a DELETE request to the [!DNL Offer Library] API using the `id` of the collection you wish to delete.

**API format**

```http
DELETE /{ENDPOINT_PATH}/offer-collections/{ID}
```

| Parameter | Description | Example |
| --------- | ----------- | ------- |
| `{ENDPOINT_PATH}` | The endpoint path for persistence APIs. | `https://platform.adobe.io/data/core/dps` |
| `{ID}` | The id of the entity you wish to delete.| `offerCollection1234` |

**Request**

```shell
curl -X DELETE 'https://platform.adobe.io/data/core/dps/tags/tag1234' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer  {ACCESS_TOKEN}' \
-H 'x-api-key: {API_KEY}' \
-H 'x-gw-ims-org-id: {IMS_ORG}' \
-H 'x-sandbox-name: {SANDBOX_NAME}'
```

**Response**

A successful response returns HTTP status 200 and a blank body.

You can confirm the deletion by attempting a lookup (GET) request to the collection. You should receive an HTTP status 404 (Not Found) because the collection has been removed.
