---
solution: Journey Optimizer
product: journey optimizer
title: Perform data lifecycle operations
description: Learn how to perform data lifecycle operations
feature: Privacy, Monitoring
role: User
level: Intermediate
exl-id: 8045b559-bf5e-4b5f-9da4-accd44641a68
TQID: https://experienceleague.adobe.com/-zue9aNrWtfL3MGs7OjH-1CF436mzPh50fsru8OSEq8
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: aeebb91a-f216-4d5f-8da1-3a7e6f696ed0
    internal-label: Data management activity
  - id: bb359667-ec7d-4d4b-8663-5850fc219d32
    internal-label: Administration
subfeature_v2:
  - id: a9cf78bf-e9e4-4836-85a5-b6b3cf93bf56
    internal-label: Consent management (AJO)
  - id: f365ec33-2b99-4b7f-b4ee-c743dd7f615f
    internal-label: Data governance
  - id: c8d5f2ce-ba44-43e9-a2bf-94a3d7d85ec3
    internal-label: Data privacy requests
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
level_v2:
  - id: b5a62a22-46f7-4f0d-b151-3fc640bef588
    internal-label: Intermediate
topic_v2:
  - id: aa2f3246-cb95-4b30-8899-fdf7d73550cc
    internal-label: Reporting
  - id: d095671a-1355-40aa-8b5f-06c33c68080b
    internal-label: Security
  - id: f4e6943a-c91a-4134-a2c7-f4f20cfff2f0
    internal-label: Privacy
---
# Perform data lifecycle operations {#data-hygiene}

>[!AVAILABILITY]
>
>Data lifecycle capabilities are currently only available for organizations that have purchased the **Healthcare Shield** and **Privacy and Security Shield** add-on offerings.

As data is continuously ingested into Adobe Experience Platform, it becomes crucial to ensure your data is used as intended, updated when necessary, and deleted per organizational policies.

These tasks can be accomplished using the **[!UICONTROL Data Lifecycle]** menu, which allows you to configure and schedule data lifecycle operations, ensuring that your records are properly maintained.

![](assets/data-hygiene.png)


## Recommendations {#data-hygiene-recommendations}

When performing data hygiene operations (such as deleting identities or datasets), be aware that historical delivery events associated with deleted identities will no longer appear in standard reporting or datalake queries. This can result in discrepancies between the number of emails reported as **Delivered** and the number of emails **Received** in recipient inboxes, especially for older journeys. 

Before executing large-scale deletions, validate and export any required delivery or reporting data. If reconciliation is needed after data hygiene, coordinate with Adobe support to access archived logs or use Message Feedback Event Dataset queries for recent data.  

## Learn more {#data-hygiene-learn-more}

For more information on the Privacy Service and how to perform data lifecycle operations, refer to Adobe Experience Platform documentation:

* [Privacy Service overview](https://experienceleague.adobe.com/docs/experience-platform/privacy/home.html)
* [Data Lifecycle in Adobe Experience Platform](https://experienceleague.adobe.com/docs/experience-platform/hygiene/home.html)
