---
title: Update collections
description: Collections are subsets of offers based on predefined conditions defined by a marketer, such as category of the offer.
feature: Decision Management, API, Collections
topic: Integrations
role: Data Engineer
level: Experienced
exl-id: bf12d22f-e6c0-45fd-a2b2-149d3f4cf882
---
# Update a collection {#update-collection}

You can modify or update a collection by making a PATCH request to the [!DNL Offer Library] API

For more information on JSON Patch, including available operations, see the official [JSON Patch documentation](https://jsonpatch.com/).

## Accept and Content-Type headers {#accept-and-content-type-headers}

The following table shows the valid values which comprise the *Content-Type* and *Accept* fields in the request header:

| Header name | Value |
| ----------- | ----- |
| Accept | `application/vnd.adobe.platform.xcore.xdm.receipt+json; version=1` |
| Content-Type | `application/vnd.adobe.platform.xcore.patch.hal+json; version=1; schema="https://ns.adobe.com/experience/offer-management/offer-filter;version=0.1"` |

**API format**

```http
PATCH /{ENDPOINT_PATH}/{CONTAINER_ID}/instances/{INSTANCE_ID}
```

| Parameter | Description | Example |
| --------- | ----------- | ------- |
| `{ENDPOINT_PATH}` | The endpoint path for repository APIs. | `https://platform.adobe.io/data/core/xcore/` |
| `{CONTAINER_ID}` | The container where the collections are located. | `e0bd8463-0913-4ca1-bd84-6309134ca1f6` |
| `{INSTANCE_ID}` | The instance id of the collection you wish to update. | `0bf31c20-13f1-11eb-a752-e58fd7dc4cb3` |

**Request**

```shell
curl -X PATCH \
  'https://platform.adobe.io/data/core/xcore/e0bd8463-0913-4ca1-bd84-6309134ca1f6/instances/0bf31c20-13f1-11eb-a752-e58fd7dc4cb3' \
  -H 'Accept: application/vnd.adobe.platform.xcore.xdm.receipt+json; version=1' \
  -H 'Content-Type: application/vnd.adobe.platform.xcore.patch.hal+json; version=1; schema="https://ns.adobe.com/experience/offer-management/offer-filter;version=0.1"' \
-H 'Authorization: Bearer  {ACCESS_TOKEN}' \
-H 'x-api-key: {API_KEY}' \
-H 'x-gw-ims-org-id: {IMS_ORG}' \
-H 'x-sandbox-name: {SANDBOX_NAME}' \
-d '[
    {
            "op": "add",
            "path": "/_instance/xdm:filterType",
            "value": "anyTags"
    },
    {
            "op": "add",
            "path": "/_instance/xdm:ids",
            "value": ["xcore:tag:124e147572cd7866"]
    }
]'
```

| Parameter | Description |
| --------- | ----------- |
| `op` | The operation call used to define the action needed to update the connection. Operations include: `add`, `replace`, and `remove`. |
| `path` | The path of the parameter to be updated. |
| `value` | The new value you want to update your parameter with. |

**Response**

A successful response returns the updated details of the collection, including its unique instance ID and collection `@id`.

```json
{
    "instanceId": "0bf31c20-13f1-11eb-a752-e58fd7dc4cb3",
    "@id": "xcore:offer-filter:124e3594ce8b4930",
    "repo:etag": 1,
    "repo:createdDate": "2023-10-21T22:59:17.345797Z",
    "repo:lastModifiedDate": "2023-10-21T22:59:17.345797Z",
    "repo:createdBy": "{CREATED_BY}",
    "repo:lastModifiedBy": "{MODIFIED_BY}",
    "repo:createdByClientId": "{CREATED_CLIENT_ID}",
    "repo:lastModifiedByClientId": "{MODIFIED_CLIENT_ID}"
}
```
