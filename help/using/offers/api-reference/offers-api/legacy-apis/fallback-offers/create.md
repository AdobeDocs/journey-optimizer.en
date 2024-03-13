---
title: Create a fallback offer
description: A fallback offer is sent to customers if they are not eligible for other offers
feature: Decision Management, API
topic: Integrations
role: Data Engineer
level: Experienced
exl-id: 1a9c074a-187a-45b1-9ad0-378aeef0d03d
---
# Create a fallback offer {#create-fallback-offer}

You can create a fallback offer by making a POST request to the [!DNL Offer Library] API, while providing your container ID.

## Accept and Content-Type headers {#accept-and-content-type-headers}

The following table shows the valid values which comprise the *Content-Type* and *Accept* fields in the request header:

| Header name | Value |
| ----------- | ----- |
| Accept | `application/vnd.adobe.platform.xcore.xdm.receipt+json; version=1` |
| Content-Type | `application/schema-instance+json; version=1;  schema="https://ns.adobe.com/experience/offer-management/fallback-offer;version=0.1"` |

**API format**

```http
POST /{ENDPOINT_PATH}/{CONTAINER_ID}/instances
```

| Parameter | Description | Example |
| --------- | ----------- | ------- |
| `{ENDPOINT_PATH}` | The endpoint path for repository APIs. | `https://platform.adobe.io/data/core/xcore/` |
| `{CONTAINER_ID}` | The container where the fallback offers are located. | `e0bd8463-0913-4ca1-bd84-6309134ca1f6` |

**Request**

```shell
curl -X POST \
  'https://platform.adobe.io/data/core/xcore/e0bd8463-0913-4ca1-bd84-6309134ca1f6/instances' \
  -H 'Accept: application/vnd.adobe.platform.xcore.xdm.receipt+json; version=1' \
  -H 'Content-Type: application/schema-instance+json; version=1;  schema="https://ns.adobe.com/experience/offer-management/fallback-offer;version=0.1"' \
  -H 'Authorization: Bearer {ACCESS_TOKEN}' \
  -H 'x-api-key: {API_KEY}' \
  -H 'x-gw-ims-org-id: {IMS_ORG}' \
  -H 'x-sandbox-name: {SANDBOX_NAME}' \
  -d '{
        "xdm:status": "approved",
        "xdm:name": "Fallback for sales",
        "xdm:representations": [
            {
                "xdm:components": [
                    {
                        "dc:language": [
                            "en"
                        ],
                        "@type": "https://ns.adobe.com/experience/offer-management/content-component-html",
                        "dc:format": "text/html"
                    }
                ],
                "xdm:channel": "https://ns.adobe.com/xdm/channel-types/web",
                "xdm:placement": "xcore:offer-placement:124e0be5699743d3"
            }
        ]
}'
```

**Response**

A successful response returns information on the newly created fallback offer, including its unique instance ID and placement `@id`. You can use the instance ID in later steps to update or delete your fallback offer. You can use your unique fallback offer `@id` in a later tutorial to create a decision.


```json
{
    "instanceId": "b3966680-13ec-11eb-9c20-8323709cfc65",
    "@id": "xcore:fallback-offer:124e2e764b1ac1b9",
    "repo:etag": 1,
    "repo:createdDate": "2023-10-21T22:28:11.111732Z",
    "repo:lastModifiedDate": "2023-10-21T22:28:11.111732Z",
    "repo:createdBy": "{CREATED_BY}",
    "repo:lastModifiedBy": "{MODIFIED_BY}",
    "repo:createdByClientId": "{CREATED_CLIENT_ID}",
    "repo:lastModifiedByClientId": "{MODIFIED_CLIENT_ID}"
}
```
