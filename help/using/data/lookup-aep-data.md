---
solution: Journey Optimizer
product: journey optimizer
title: Use Adobe Experience Platform data
description: Learn how to use Adobe Experience Platform datasets in [!DNL Journey Optimizer] Decisioning and personalization capabilities.
badge: label="Limited Availability" type="Informative"
feature: Personalization, Rules
topic: Personalization
role: Data Engineer
level: Intermediate
keywords: expression, editor
mini-toc-levels: 1
exl-id: 44a8bc87-5ab0-45cb-baef-e9cd75432bde
---
# Use Adobe Experience Platform data {#aep-data}

>[!CONTEXTUALHELP]
>id="lookup-aep-data"
>title="Enable for lookup"
>abstract="Enableing a dataset for lookup allows you to leverage its data with Journey Optimizer personalization and Decisioning capabilities."

>[!AVAILABILITY]
>
>This feature is currently available to all customers as a limited availability release.

Journey Optimizer allows you to leverage data from Adobe Experience Platform data with personalization and Decisioning capabilities. To do this, record-based datasets needed for lookup personalization must first be enabled for the lookup service as described below.

## Must-read

### Guardrails & guidelines {#guidelines}

Before you begin, please review the following restrictions and guidelines:

* Datasets enabled for lookup should not contain any Personally Identifiable Information (PII).  
* Datasets enabled for lookup and used in personalization are not protected from deletion. It is up to you to keep track of which datasets are being used for personalization to ensure they are not deleted or removed. 
* Datasets must be associated with a schema that is NOT of Profile or Event type.  
* Schemas must have a primary identity. Only a single, primary key can be used for lookups. 

### Entitlement for lookup service

| Feature Component | Limits | Notes |
| ------- | ------- | ------- |
| Enabled Lookup Datasets | Max 10 per organization | Maximum number of datasets that can be configured for lookup at any given time. This limit applies to the total combined number of lookup datasets across both production and development sandboxes within the customer instance. |
| Dataset Record Count | Up to 2 million records per dataset | Maximum number of records allowed in a single dataset, calculated as the total count across all batches within that dataset. |
| Record Size | Up to 2 KB per record | Default maximum record size supported. |
| Dataset Size | Up to 4 GB | Maximum size of an individual dataset, not the combined size across all datasets in a sandbox. The record count and dataset size limits are independent guardrails — both must be satisfied. |
| Dataset Frequency Updates | Up to 5 updates per day per dataset | Maximum frequency of update operations allowed for a single dataset per day. |

>[!NOTE]
>
>If additional volumes are needed beyond the guardrails listed above, please contact your Adobe representative.

### Additional performance considerations 

The below recommendations are guidance to avoid delays in deliverability:

| Consideration | Recommended limit | Description |
| ------- | ------- | ------- |
| Attributes per Lookup | Up to 20 | Number of data fields retrieved per record in a single lookup activity.|
| Lookup Activities | Up to 5 per journey | Each journey can contain up to 5 separate lookup activities. Each lookup can target a different dataset.|

## Enable a dataset for data lookup {#enable}

In order to leverage data from your dataset for personalization, you need to enable the dataset for lookup.

### Prerequisites {#prerequisites-enable}

The schema associated with your dataset that you wish to enable for lookup must be of record-type. The schema should NOT be of profile or event class. 

+++Example

![](assets/data-lookup-schema.png)

+++

The schema must have a primary identity defined.

+++Example

![](assets/data-lookup-primary.png)

+++

If a custom namespace was not yet defined, ensure that the identity is a non-person identifier.

+++Example

![](assets/aep-data-namespace.png)

+++

### Enable the dataset for lookup in the dataset management interface 

In the dataset management user interface, use the toggle to enable the dataset for lookup.  
 
![](assets/aep-data-enable.png)

>[!NOTE]
>
>It is recommended that the dataset is NOT also enabled for profile, as this can lead to an increase in profile richness and is not needed to perform the lookups.  

### API Method

Follow the directions detailed in [this documentation](https://developer.adobe.com/journey-optimizer-apis/references/authentication/) to configure your environment to send API commands. 

#### Prerequisites

* The developer project must have the Adobe Journey Optimizer and Adobe Experience Platform APIs added to their project. 

    ![](assets/aep-data-api.png)

* You must have manage datasets permission as part of your role.

* The schema for which the dataset is based on must contain a primary identity that can act as the lookup key. 

#### API call structure 

```shell

curl -s -XPATCH "https://platform.adobe.io/data/core/entity/lookup/dataSets/${DATASET_ID}/${ACTION}" \ -H "Authorization: Bearer ${ACCESS_TOKEN}" \ -H "x-api-key: ${API_KEY}" \ -H "x-gw-ims-org-id: ${IMS_ORG}" \ -H "x-sandbox-name: ${SANDBOX_NAME}" 

```

Where: 

* URL is `https://platform.adobe.io/data/core/entity/lookup/dataSets/${DATASET_ID}/${ACTION}`
* Dataset ID is the dataset for which you wish to enable. 
* Action is enable OR disable. 
* Access token can be retrieved from the developer console. 
* API key can be retrieved from the developer console. 
* IMS Org ID is your Adobe organization. 
* Sandbox Name is the sandbox name the dataset is in (i.e. prod, dev etc.). 

>[!NOTE]
>
>If you encounter the error below when attempting an API call to enable datasets, try removing the Adobe Journey Optimizer APIs from your developer console project and then re-adding them:
>
>`"error_code": "403003",`
>`"message": "Api Key is invalid"`

## Dataset monitoring

Once a dataset has been enabled for lookup, you can review the status of ingestion into the lookup service by going to the **[!UICONTROL Monitoring]** menu and selecting the **[!UICONTROL Journey Optimizer]** tab.

This process indicator helps in understanding when new batches of data are available in the lookup service.  

![](assets/aep-data-monitoring.png)

<!--Ivan Mironchuk
Note - we have a bug here currently. Will need to update screenshot once the lookup service will accurately reflect the progress.-->

## Next steps

After a dataset has been enabled for lookup using an API call, you can use the data with [!DNL Journey Optimizer] personalization and Decisioning capabilities. For more information, refer to these sections:

* [Use Adobe Experience Platform data for personalization](../personalization/aep-data-perso.md)
* [Use Adobe Experience Platform data for decisioning](../experience-decisioning/aep-data-exd.md)
