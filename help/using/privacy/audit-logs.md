---
solution: Journey Optimizer
product: journey optimizer
title: Audit actions on Journey Optimizer resources
description: Learn how to track actions performed on Journey Optimizer resources.
feature: Monitoring
role: User
level: Intermediate
exl-id: 759b014a-c834-4331-bffd-5bc159ec555d
TQID: https://experienceleague.adobe.com/Usk3qin9P4IZlKw-gEI4zaKO-aRtaKq9-0GMVlOecjA
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
  - id: a004cc84-67b9-4a33-a3a7-8ec7273ef4dc
    internal-label: Metadata
  - id: c7d04a2c-412a-4c9d-9d7a-4456eaa5adeb
    internal-label: Governance
  - id: d095671a-1355-40aa-8b5f-06c33c68080b
    internal-label: Security
  - id: f4e6943a-c91a-4134-a2c7-f4f20cfff2f0
    internal-label: Privacy
---
# Audit actions on Journey Optimizer resources {#track-changes}

## About audit logs {#audit-logs}

>[!IMPORTANT]
>
>To view and export audit log, you must have the **[!DNL View User Activity Log]** permission granted. [Learn more](../administration/ootb-product-profiles.md)

With Journey Optimizer, you can identify actions performed by users in the system on various services and capabilities like journeys, messages, landing pages etc.

This allows you to increase the visibility of activities performed in the system, troubleshoot issues, and help your business comply with regulations and corporate data stewardship policies.

Each action is recorded with metadata in "audit logs" which are accessible in Adobe Experience Platform. For more on audit logs, including how to view and manage them in UI or API, refer to [Adobe Experience Platform documentation](https://experienceleague.adobe.com/docs/experience-platform/landing/governance-privacy-security/audit-logs/overview.html).

![](assets/audit-logs.png)

## Event types captured by audit logs {#events}

The following table outlines which actions on which Journey Optimizer resources are recorded by audit logs. The full list of actions captured in the Audit logs is available in [Adobe Experience Plaform documentation](https://experienceleague.adobe.com/docs/experience-platform/landing/governance-privacy-security/audit-logs/overview.html#category).

>[!NOTE]
>
>Audit logs related to **decision management** are only visible from the CSV file that can be downloaded using the **[!UICONTROL Download log]** button.

| Resource | Action            |
|-----------|------------------|
| AJO campaign | Create / Delete / Update / Activate / Stop |
| AJO channel general setting | Create / Delete / Update |
| AJO IP pool | Create / Delete / Update |
| AJO landing page | Create / Delete / Update / Publish / Unpublish |
| AJO landing page HTML template | Create / Delete / Update |
| AJO landing page preset | Create / Delete / Update |
| AJO landing page subdomain | Create / Delete / Update |
| AJO message preset | Create / Delete / Update |
| AJO PTR record | Create / Delete / Update |
| AJO saved expression template | Create / Delete / Update |
| AJO SMS API credentials | Create / Delete / Update |
| AJO subdomain | Create / Delete / Update |
| AJO suppression list | Create / Delete / Download CSV |
| Field group | Create / Delete / Update |
| Journey | Create / Delete / Update / Stop / Publish |
| Journey custom action | Create / Delete / Update |
| Journey datasource | Create / Delete / Update |
| Journey event | Create / Delete / Update |
| Message frequency rule | Create / Delete / Update |
| Ranking strategy | Create / Delete / Update |
