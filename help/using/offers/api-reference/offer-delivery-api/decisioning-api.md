---
title: Deliver offers
description: Decision Management is a collection of services and UI programs that enables marketers to create and deliver end-user personalized offer experiences across channels and applications using business logic and decision rules.
feature: Decision Management, API
topic: Integrations
role: Data Engineer
level: Experienced
exl-id: 692d0aae-6fa1-40b8-a35f-9845d78317a3
---
# Deliver offers using the Decisioning API {#decisioning-api}

With Decision Management, you can create and deliver end-user personalized offer experiences, across channels and applications using business logic and decision rules. An offer is a marketing message that may have rules associated with it that specify who is eligible to see the offer.

You can create and deliver offers by making a POST request to the [!DNL Decisioning] API.

This tutorial requires a working understanding of APIs, specifically with regards to Decision Management. For more information, see the [Decision Management API developer guide](../getting-started.md). This tutorial also requires that you have a unique placement ID and decision ID value available. If you have not acquired these values, see the tutorials for [creating a placement](../offers-api/placements/create.md) and [creating a decision](../activities-api/activities/create.md).

➡️  [Discover this feature in video](#video)

## Required headers {#required-headers}

The following table shows the valid values which comprise the *Content-Type* and *Accept* fields in the request header:

| Header name | Value |
| ----------- | ----- |
| Accept | `application/vnd.adobe.xdm+json; schema="https://ns.adobe.com/experience/offer-management/decision-response;version=1.0"` |
| Content-Type | `application/vnd.adobe.xdm+json; schema="https://ns.adobe.com/experience/offer-management/decision-request;version=1.0"` |
| Authorization | `Bearer {ACCESS_TOKEN}` |
| x-gw-ims-org-id| `{IMS_ORG}` |
| x-sandbox-name| `{SANDBOX_NAME}` |
| x-api-key| `{API_KEY}` |

* All requests that contain a payload (POST,PUT,PATCH) require the content-type header

## API request {#request}

### API format

```https
POST /{ENDPOINT_PATH}/decisions
```

| Parameter | Description | Example |
| --------- | ----------- | ------- |
<!-- | `{ENDPOINT_PATH}` | The endpoint path for repository APIs. | `https://platform.adobe.io/data/core/ods` | -->

### Request

```shell
curl -X POST \
  'https://platform.adobe.io/data/core/ods/decisions' \
  -H 'Accept: application/vnd.adobe.xdm+json; schema="https://ns.adobe.com/experience/offer-management/decision-response;version=1.0"' \
  -H 'Content-Type: application/vnd.adobe.xdm+json; schema="https://ns.adobe.com/experience/offer-management/decision-request;version=1.0"'
  -H 'Authorization: Bearer {ACCESS_TOKEN}' \
  -H 'x-api-key: {API_KEY}' \
  -H 'x-gw-ims-org-id: {IMS_ORG}' \
  -H 'x-sandbox-name: {SANDBOX_NAME}'
  -d '{
        "xdm:propositionRequests": [
            {
              "xdm:placementId": "xcore:offer-placement:ffed0456",
              "xdm:activityId": "xcore:offer-activity:ffed0123",
              "xdm:itemCount": 2
            },
            {
              "xdm:placementId": "xcore:offer-placement:ffed0012",
              "xdm:activityId": "xcore:offer-activity:fffc0789"
            }
        ],
        "xdm:profiles": [
            {
              "xdm:identityMap": {
                "SWCUSTID": [
                {
                    "xdm:id": "123@abc.com"
                }
                ]
            },
            "xdm:decisionRequestId": "0AA00002-0000-1224-c0de-cjf98Csj43"
            }
        ],
        "xdm:allowDuplicatePropositions": {
            "xdm:acrossActivities": true,
            "xdm:acrossPlacements": true
        },
        "xdm:mergePolicy": {
            "xdm:id": "5f3ed32f-eaf1-456c-b0f0-7b338c4cb18a"
        },
        "xdm:responseFormat": {
            "xdm:includeContent": true,
            "xdm:includeMetadata": {
            "xdm:activity": [
                "name"
            ],
            "xdm:option": [
                "name"
            ],
            "xdm:placement": [
                "name"
            ]
            }
        }
      }'
```

| Property | Description | Example |
| -------- | ----------- | ------- |
| `xdm:propositionRequests` | This object contains the placement and decision identifiers. |
| `xdm:propositionRequests.xdm:placementId` | The unique placement identifier. | `"xdm:placementId": "xcore:offer-placement:ffed0456"` |
| `xdm:propositionRequests.xdm:activityId` | The unique decision identifier. | `"xdm:activityId": "xcore:offer-activity:ffed0123"` |
| `xdm:itemCount` | The number of offers to be returned. The maximum number is 30. | `"xdm:itemCount": 2` |
| `xdm:profiles` | This object holds information about the profile for which the decision is requested. For an API request this will contain one profile. |
| `xdm:profiles.xdm:identityMap` | This object holds a set of end user identities based on the namespace integration code of the identity. The identity map can carry more than one identity of each namespace. For more information on namespaces, see [this page](../../../audience/get-started-identity.md). | `Email: [{"xdm:id": "123@abc.com"}]` |
| `xdm:profiles.xdm:decisionRequestId` | The ID generated by the client that can be used to uniquely identify a profile decision request. This ID is echoed back in the response and does not influence the outcome of the decision. | `"xdm:decisionRequestId": "0AA00002-0000-1224-c0de-cjf98Csj43"` |
| `xdm:allowDuplicatePropositions` | This object the control structure of the De-duplication rules. It consists of a series of flags that indicate if the same option can be proposed across a certain dimension. A flag that is set to true means duplicates are allowed and should not be removed across the category indicated by the flag. A flag set to false means that the decision engine should not make the same proposition across the dimension and instead pick the next best option for one of the sub-decisions. |
| `xdm:allowDuplicatePropositions.xdm:acrossActivities` | If set to true, multiple decisions may get assigned the same option. | `"xdm:acrossActivities": true` |
| `xdm:allowDuplicatePropositions.xdm:acrossPlacements` | If set to true, multiple placements may get assigned the same option. | `"xdm:acrossPlacements": true` |
| `xdm:mergePolicy.xdm:id` | Identifies the merge policy by which to govern the data returned by profile access service. If one is not specified in the request, Decision Management won't pass along anything profile access service, else it would pass the id provided by the caller. | `"xdm:id": "5f3ed32f-eaf1-456c-b0f0-7b338c4cb18a"` |
| `xdm:responseFormat` | A set of flags that formats the response content. |
| `xdm:responseFormat.xdm:includeContent` | A boolean value that, if set to `true`, includes content to the response. | `"xdm:includeContent": true` |
| `xdm:responseFormat.xdm:includeMetadata` | An object that is used to specify what additional metadata is returned. If this property is not included, then `xdm:id` and `repo:etag` are returned by default. | `name` |
| `xdm:responseFormat.xdm:activity` | This flag identifies the specific metadata information returned for `xdm:activity`. | `name` |
| `xdm:responseFormat.xdm:option` | This flag identifies the specific metadata information returned for `xdm:option`. | `name`, `characteristics` |
| `xdm:responseFormat.xdm:placement` | This flag identifies the specific metadata information returned for `xdm:placement`. | `name`, `channel`, `componentType` |

### Response

A successful response returns information on your proposition, including its unique `xdm:propositionId`.

```json
{
  "xdm:propositionId": "5d0ffb5e-dfc6-4280-99b6-0bf3131cb8b8",
  "xdm:propositions": [
    {
      "xdm:activity": {
        "xdm:id": "xcore:activity:ffed0123",
        "repo:etag": 4
      },
      "xdm:placement": {
        "xdm:id": "xcore:placement:ffed0456",
        "repo:etag": 1
      },
      "xdm:options": [
        {
          "xdm:id": "xcore:personalized-option:ccc0111",
          "repo:etag": 3,
          "@type": "https://ns.adobe.com/experience/decisioning/content-component-html-template",
          "xdm:content": "<html>some html</html>"
        },
        {
          "xdm:id": "xcore:personalized-option:ccc0222",
          "repo:etag": 5,
          "@type": "https://ns.adobe.com/experience/decisioning/content-component-html-template",
          "xdm:content": "<html>hello, world</html>",
          "xdm:score": 45.65
        }
      ]
    },
    {
      "xdm:activity": {
        "xdm:id": "xcore:activity:ffed0123",
        "repo:etag": 4
      },
      "xdm:placement": {
        "xdm:id": "xcore:placement:ffed0789",
        "repo:etag": 2
      },
      "xdm:fallback": {
        "xdm:id": "xcore:fallback:ccc0222",
        "repo:etag": 5,
        "@type": "https://ns.adobe.com/experience/decisioning/content-component-imagelink",
        "dc:format": "image/png",
        "xdm:deliveryURL": "https://cdn.adobe.com/content/1445323-1134331.png",
        "xdm:content": "https://www.adobe.com/index2.html"
      }
    }
  ],
  "ode:createDate": 1566497582038
}
```

| Property | Description | Example |
| -------- | ----------- | ------- |
| `xdm:propositionId` | The unique identifier for the proposition entity associated with an XDM DecisionEvent. | `"xdm:propositionId": "5d0ffb5e-dfc6-4280-99b6-0bf3131cb8b8"` |
| `xdm:propositions` | This object contains a single decision proposition. Multiple options can be returned for the decision. If no options are found, then the decision's fallback offer is returned. Single decision propositions always includes either an `options` property or a `fallback` property. When present, the `options` property cannot be empty. |
| `xdm:propositions.xdm:activity` | This object contains the unique identifier for a decision. | `"xdm:id": "xcore:activity:ffed0123"` |
| `xdm:propositions.xdm:placement` | This object contains the unique identifier for an offer placement. | `"xdm:id": "xcore:placement:ffed0456"` |
| `xdm:propositions.xdm:options` | This object contains a single option, including its unique identifier. If present, this object cannot be empty. | `xdm:id": "xcore:personalized-option:ccc0111` |
| `xdm:propositions.xdm:options.@type` | Defines the type of the component. `@type` acts as the processing contract for the client. When the experience is assembled, the composer will look for the component(s) that have a specific type. | `https://ns.adobe.com/experience/offer-management/content-component-imagelink` |
| `xdm:propositions.xdm:content` | The format of the response content. | Response content can be: `text`, `html block`, or `image link` |
| `xdm:score` | The score for an option that is computed as a result of a ranking function associated with the option or the decision. This field will be returned by the API if a ranking function is involved in determining the score of an offer during the ranking. | `"xdm:score": 45.65` |
| `xdm:propositions.xdm:fallback` | This object contains a single fallback offer, including its unique identifier. | `"xdm:id": "xcore:fallback:ccc0222"` |
| `xdm:propositions.xdm:fallback.dc:format` | The physical or digital manifestation of the resource. Typically, format should include the media-type of the resource. The format may be used to determine the software, hardware or other equipment needed to display or operate the resource. It is recommended to select a value from a controlled vocabulary, for example, the list of [Internet Media Types](https://www.iana.org/assignments/media-types/) defining computer media formats. | `"dc:format": "image/png"` or `"image/jpeg"`|
| `xdm:propositions.xdm:fallback.xdm:deliveryURL` | An optional URL to read the asset from a content delivery network or service endpoint. This URL is used to access the asset publicly from a user agent. | `https://d37yhxrr0p3l3l.cloudfront.net/0fd0f090-a148-11ea-89e3-f1f2ad52f7e8/urn:aaid:sc:US:a68c86a6-9295-4940-a083-11916b665500/0/40d78a12-f8b6-3f07-8e67-7cb8ae2cc7ec` |
| `ode:createDate` | The time when the decision response message was created. This is represented as epoch time. | `"ode:createDate": 1566497582038` |

**Response codes**

The table below lists all codes that can be returned in the response:

|Code|Description|
|  ---  |  ---  |
|200|Success. Decision was made for given activities|
|400|Invalid request parameter. The request cannot be understood by the server due to malformed syntax.|
|403|Forbidden, insufficient permissions.|
|422|Unprocessable entity. The request syntax is correct, however, due to semantic errors it is unable to be processed.|
|429|Too many requests. The user has sent too many requests in a given amount of time.|
|500|Internal server error. The server encountered an unexpected condition which prevented it from fulfilling the request.|
|503|Service unavailable due to server overload. The server is currently unable to handle the request due to a temporary overloading.|

<!-- ## Tutorial video {#video}

The following video is intended to support your understanding of the components of Decision Management.

>[!NOTE]
>
>This video applies to the Offer Decisioning application service built on Adobe Experience Platform. However, it provides generic guidance to use Offer in the context of Journey Optimizer.

>[!VIDEO](https://video.tv.adobe.com/v/329919/?quality=12) -->

## Next steps {#next-steps}

By following this API guide, you have created and delivered offers using the [!DNL Decisions] API. For more information, see the [overview on Decision Management](../../../offers/get-started/starting-offer-decisioning.md).
