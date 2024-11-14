---
solution: Journey Optimizer
product: journey optimizer
title: Custom upload (CSV) & Federated Audience Composition
description: Learn key information and best practices while working with Custom upload (CSV) and Federated Audience Composition audiences.
feature: Audiences, Profiles
topic: Content Management
role: User
level: Beginner
mini-toc-levels: 1
exl-id: d2365e3f-fbef-43c2-bf2a-0a868cb93015
---
# Custom upload (CSV) & Federated Audience Composition {#csv-fac}

## About Custom upload & Federated Audience Composition {#about}

In addition to segment definitions and audience composition, [!DNL Journey Optimizer] allows you to generate and target audiences by importing them from a CSV file, or leveraging data from your data warehouse.

* **Custom upload**: Import an audience using a CSV file. Learn how to import audiences in Adobe Experience Platform [Segmentation Service documentation](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/ui/audience-portal#import-audience){target="_blank"}.

* **Federated Audience Composition**: Federate datasets directly from your existing data warehouse to build and enrich Adobe Experience Platform audiences and attributes all in one system. Please read the guide on [Federated Audience Composition](https://experienceleague.adobe.com/en/docs/federated-audience-composition/using/home).

You can target these audience in Journey Optimizer or activate them to any destination supported by Adobe Experience Platform

➡️ [Discover these features in video](#video)

## Must-read {#must-read}

This section provides key information to keep in mind while working with Custom upload (CSV files) and Federated Audience Composition audiences.

* **Preview and proof support:** Currently, preview and proof is not supported for audiences created using CSV upload or Federated Audience Composition. Keep this in mind when planning your campaigns.

* **Activation delay:** Audiences are ready for use in Journey Optimizer right after ingestion completes. While this is typically within one hour, it's subject to some variability.

* **Activated records & identity stitching:** Every record in the audience is activated, including any duplicates. During the next UPS profile export, these records will go through identity stitching. As a result, the number of activated records may differ from the number of profiles after identity stitching.

* **Targeting new profiles:** When a match is not found between a record and a UPS profile, a new empty profile is created. This profile is linked to the enrichment attributes which are stored in the data lake. Because this new profile is empty, targeting fields typically used in Journey Optimizer (e.g., personalEmail.address, mobilePhone.number) are empty and therefore cannot be used for targeting.

    To solve this, you can specify the "execution field" (or "execution address" depending on the channel) in the channel configuration as 'identityMap'. This will ensure that the attribute chosen as the identity at audience creation will be the one used for targeting in Journey Optimizer.

## How-to videos {#video}

Learn how to upload audiences in CSV format into Adobe Experience Platform. 

>[!VIDEO](https://video.tv.adobe.com/v/3421714?quality=12)

Learn more on Federated Audience Composition.

>[!VIDEO](https://video.tv.adobe.com/v/3432261?quality=12)
