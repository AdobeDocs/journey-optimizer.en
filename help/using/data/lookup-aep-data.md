---
solution: Journey Optimizer
product: journey optimizer
title: Use Adobe Experience Platform data (Beta)
description: Learn how to use Adobe Experience Platform datasets in [!DNL Journey Optimizer] Decisioning and personalization capabilities.
badge: label="Beta" type="Informative"
feature: Personalization, Rules
topic: Personalization
role: Data Engineer
level: Intermediate
keywords: expression, editor
exl-id: 44a8bc87-5ab0-45cb-baef-e9cd75432bde
---
# Use Adobe Experience Platform data {#aep-data}

>[!AVAILABILITY]
>
>This feature is currently available to all customers as a public beta.
>
>In order to use this capability, you must first accept beta terms for your organization.

Journey Optimizer allows you to leverage data from Adobe Experience Platform in [!DNL Journey Optimizer]. To do this, datasets needed for lookup personalization must first be enabled through an API call as described below. Once done, you can use their data with [!DNL Journey Optimizer] personalization and Decisioning capabilities.

## Beta restrictions and guidelines {#guidelines}

Before you begin, please review the following restrictions and guidelines:

* **Dataset size** is limited to 5GB for production datasets and 1GB for dev sandbox datasets
* **A maximum of 50 datasets can be enabled** for lookup per organization at any time.
* **Number of records** is restricted to 5M in production datasets and 1M in dev sandbox datasets.
* **Data Usage Labelling and Enforcement** is not enforced at this time for datasets enabled for lookup.
* **Datasets enabled for lookup and used in personalization are not protected from deletion**. It is up to you to keep track of which datasets are being used for personalization to ensure they are not deleted or removed.
* **Data Usage Labelling and Enforcement** is not enforced at this time for datasets enabled for lookup.

## Enable a dataset for data lookup {#enable}

In order to leverage data from your dataset for personalization, you need to use an API call to retrieve its status and enable lookup service.

### Prerequisites {#prerequisites-enable}

* Follow the directions detailed in [this documentation](https://developer.adobe.com/journey-optimizer-apis/references/authentication/) to configure your environment to send API commands.
* The developer project must have the Adobe Journey Optimizer and Adobe Experience Platform APIs added to their project.

    ![](assets/aep-data-api.png)

* You must have manage datasets permission as part of your role.
* The schema for which the dataset is based on must contain a **primary identity** that can act as the lookup key.

### API call structure {#call}

```

curl -s -XPATCH "https://platform.adobe.io/data/core/entity/lookup/dataSets/${DATASET_ID}/${ACTION}" \ -H "Authorization: Bearer ${ACCESS_TOKEN}" \ -H "x-api-key: ${API_KEY}" \ -H "x-gw-ims-org-id: ${IMS_ORG}" \ -H "x-sandbox-name: ${SANDBOX_NAME}"

```

Where:

* **URL** is `https://platform.adobe.io/data/core/entity/lookup/dataSets/${DATASET_ID}/${ACTION}`
* **Dataset ID** is the dataset for which you wish to enable.
* **Action** is enable OR disable.
* **Access token** can be retrieved from the developer console.
* **API key** can be retrieved from the developer console.
* **IMS Org ID** is your Adobe organization.
* **Sandbox Name** is the sandbox name the dataset is in (i.e. prod, dev etc.).

>[!NOTE]
>
>If you encounter the error below when attempting an API call to enable datasets, try removing the Adobe Journey Optimizer APIs from your developer console project and then re-adding them.
>
>```
>
>"error_code": "403003", 
>"message": "Api Key is invalid"
>
>```

Once a dataset has been enabled for lookup using an API call, you can use its data with [!DNL Journey Optimizer] personalization and Decisioning capabilities.

* [Use Adobe Experience Platform data for personalization](../personalization/aep-data-perso.md)
* [Use Adobe Experience Platform data for decisioning](../experience-decisioning/aep-data-exd.md)
