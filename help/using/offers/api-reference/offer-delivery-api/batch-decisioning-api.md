---
title: Batch Decisioning API
description: Learn how to use the Batch Decisioning API to select the best offers for audiences' profiles within a predefined decision scope.
feature: Decision Management, API
topic: Integrations
role: Data Engineer
level: Experienced
exl-id: 1ed01a6b-5e42-47c8-a436-bdb388f50b4e
---

# Deliver offers using the [!DNL Batch Decisioning] API {#deliver-offers-batch}

The [!DNL Batch Decisioning] API allows organizations to use decisioning functionality for all profiles in a given audience in one call. The offer content for each profiles in the audience is placed in an Adobe Experience Platform dataset where it is available for custom batch workflows.

With the [!DNL Batch Decisioning] API, you can populate a dataset with the best offers for all profiles in an Adobe Experience Platform audience for decision scopes. For example, an organization may want to run [!DNL Batch Decisioning] so they can send offers to a message delivery vendor. Those offers are then used as content that is sent out for batch message delivery to the same audience of users. 

To do this, the organization would:

* Run the [!DNL Batch Decisioning] API, which contains two requests:
    
    1. A **Batch POST request** to start a workload to batch process offer selections.  
    
    2. A **Batch GET request** to get batch workload status.

* Export the dataset to the message delivery vendor API. 

<!-- (Refer to the [export jobs endpoint documentation](https://experienceleague.adobe.com/docs/experience-platform/segmentation/api/export-jobs.html) to learn more about exporting audiences.) -->

>[!NOTE]
>
>Batch decisioning can also be performed using Journey Optimizer interface. For more information, refer to [this section](../../batch-delivery.md), which provides information on global prerequisites and limitations to take inbto account when using batch decisioning.

* **The number of running batch jobs per dataset**: Up to five batch jobs can be run at a time, per dataset. Any other batch requests with the same output dataset are added to the queue. A queued job is picked up to process once the previous job has finished running. 
* **Frequency capping**: A batch runs off of the profile snapshot that occurs once a day. The [!DNL Batch Decisioning] API caps the frequency and always loads profiles from the most recent snapshot.

## Getting started {#getting-started}

Before using this API, make sure you complete the following pre-requisite steps.

### Prepare the decision {#prepare-decision}

To prepare one or more decisions, make sure you have created a dataset, an audience, and a decision. Those prerequisites are detailed in [this section](../../batch-delivery.md).

### API requirements {#api-requirements}

All [!DNL Batch Decisioning] requests require the following headers in addition to the ones referred to in the [Decision Management API developer guide](../getting-started.md):

* `Content-Type`: `application/json`
* `x-request-id`: A unique string that identifies the request.
* `x-sandbox-name`: The sandbox name.

## Start a batch process {#start-a-batch-process}

To start a workload to batch process decisions, make a POST request to the `/workloads/decisions` endpoint.

>[!NOTE]
>
>Detailed information on batch jobs' processing time are available in [this section](../../batch-delivery.md).

**API format**

```https
POST {ENDPOINT_PATH}/workloads/decisions
```

| Parameter | Description | Example |
| --------- | ----------- | ------- |
| `{ENDPOINT_PATH}` | The endpoint path for repository APIs. | `https://platform.adobe.io/data/core/dwm` |

**Request**

```shell
curl -X POST 'https://platform.adobe.io/data/core/dwm/workloads/decisions' \
-H 'x-request-id: f671a589-eb7b-432f-b6b9-23d5b796b4dc' \
-H 'Content-Type: application/json' \
-H 'x-api-key: {API_KEY}' \
-H 'x-gw-ims-org-id: {IMS_ORG}' \
-H 'x-sandbox-name: {SANDBOX_NAME}' \
-H 'x-sandbox-id: {SANDBOX_ID}' \
-H 'Authorization: Bearer {ACCESS_TOKEN}' \
-d '{
  "xdm:segmentIds": [
    "609028e4-e66c-4776-b0d9-c782887e2273"
  ],
  "xdm:dataSetId": "6196b4a1a63bd118dafe093c",
  "xdm:propositionRequests": [
        {
            "xdm:activityId": "xcore:offer-activity:1410cdcda196707b",
            "xdm:placementId": "xcore:offer-placement:1410c4117306488a",
            "xdm:itemCount": 1
        }
  ],
  "xdm:includeContent": false
}'
```

| Property | Description | Example |
| -------- | ----------- | ------- |
| `xdm:segmentIds` | The value is an array that contains the unique identifier of the audience. It can only contain one value. |`609028e4-e66c-4776-b0d9-c782887e2273`|
| `xdm:dataSetId` | The output dataSet that decision events can be written into. |`6196b4a1a63bd118dafe093c`|
| `xdm:propositionRequests` | A wrapper that contains the `placementId` and `activityId` ||
| `xdm:activityId` | The unique identifier of the decision. |`xcore:offer-activity:1410cdcda196707b`|
| `xdm:placementId`| The unique placement identifier. |`xcore:offer-placement:1410c4117306488a`|
| `xdm:itemCount` | This is an optional field showing the number of items such as options requested for the decisioning scope. By default, the API returns one option per scope, but you can explicitly ask for more options by specifying this field. A minimum of 1 and a maximum of 30 options can be requested per scope. | `1`|
| `xdm:includeContent` | This is an optional field and is `false` by default. If `true`, the offer content is included in the decision events of dataset. |`false` |

Refer to the [Decision Management documentation](../../get-started/starting-offer-decisioning.md) for an overview of the main concepts and properties.

**Response**

```json
{
    "@id": "47efef25-4bcf-404f-96e2-67c4f784a1f5",
    "xdm:imsOrgId": "9GTO98D5F@AdobeOrg",
    "ode:createDate": 1648078924834,
    "ode:status": "QUEUED"
}
```

| Property | Description | Example |
| -------- | ----------- | ------- |
| `@id` | The UUID generated by decision management that identifies a single workload. | `5d0ffb5e-dfc6-4280-99b6-0bf3131cb8b8` |
| `xdm:imsOrgId` | The Organization ID. |`9GTO98D5F@AdobeOrg`|
| `xdm:containerId`| The container ID. |`0948b1c5-fff8-3b76-ba17-909c6b93b5a2`|
| `ode:createDate`| The time when the decision workload request was created. |`1648078924834`|
| `ode:status`| The status of the workload. | `ode:status: "QUEUED"`|

## Retrieve information on a batch decision {#retrieve-information-on-a-batch-decision}

To retrieve information on a specific decision, make a GET request to the `/workloads/decisions` endpoint while providing the corresponding workload ID value for your decision.

**API format**

```https
GET {ENDPOINT_PATH}/workloads/decisions/{WORKLOAD_ID}
```

| Parameter | Description | Example |
| --------- | ----------- | ------- |
| `{ENDPOINT_PATH}` | The endpoint path for repository APIs. | `https://platform.adobe.io/data/core/dwm` |
| `{WORKLOAD_ID}` | The UUID generated by decision management that identifies a single workload. | `47efef25-4bcf-404f-96e2-67c4f784a1f5` |

**Request**

```shell
curl -X GET 'https://platform.adobe.io/data/core/dwm/workloads/decisions/f395ab1f-dfaf-48d4-84c9-199ad6354591' \
-H 'x-request-id: 7832a42a-d4e5-413b-98e8-e49bef056436' \
-H 'Content-Type: application/json' \
-H 'x-api-key: {API_KEY}' \
-H 'x-gw-ims-org-id: {IMS_ORG}' \
-H 'x-sandbox-name: {SANDBOX_NAME}' \
-H'x-sandbox-id: {SANDBOX_ID}' \
-H 'Authorization: Bearer {ACCESS_TOKEN}'
```

**Response**

```json
{
   "@id": "f395ab1f-dfaf-48d4-84c9-199ad6354591",
    "xdm:imsOrgId": "{IMS_ORG}",
    "ode:createDate": 1648076994405,
    "ode:status": "COMPLETED"
}
```

| Property | Description | Example |
| -------- | ----------- | ------- |
| `@id` | The UUID generated by decision management that identifies a single workload. |`5d0ffb5e-dfc6-4280-99b6-0bf3131cb8b8` |
| `xdm:imsOrgId` | The Organization ID |`9GTO98D5F@AdobeOrg`|
| `xdm:containerId`| The Container ID |`0948b1c5-fff8-3b76-ba17-909c6b93b5a2`|
| `ode:createDate`| The time when Decision Workload request was created. |`1648076994405`|
| `ode:status`| The status of the workload starts with "QUEUED" and changes to "PROCESSING", "INGESTING", "COMPLETED" or "ERROR". |`ode:status: "COMPLETED"`|
| `ode:statusDetail`| This shows more details such as sparkJobId and batchID if the status is "PROCESSING" or "INGESTING". It shows the error details if the status is "ERROR". ||

## Next steps {#next-steps}

By following this API guide, you have checked for the workload status and delivered offers using the [!DNL [!DNL Batch Decisioning]] API. For more information, see the [overview on Decision Management](../../get-started/starting-offer-decisioning.md).