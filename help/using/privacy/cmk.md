---
solution: Journey Optimizer
product: journey optimizer
title: Customer Managed Keys
description: Learn how to setup and manage customer keys for Adobe Journey Optimizer.
feature: Privacy, Monitoring
role: Developer, User, Admin, Leader
level: Intermediate
exl-id: f0985d1f-0bcf-452f-bd46-dfeca0424f01
TQID: https://experienceleague.adobe.com/yCl5CISD1-Xx6gfcK2sWdFWAeE0LicO-3r3YndB2cVQ
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
  - id: c66ffd68-0f65-42bb-aa23-b4020f12e0bd
    internal-label: Admin
  - id: f8a45b24-4be7-4f1b-909b-60d06b483a20
    internal-label: Leader
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
level_v2:
  - id: b5a62a22-46f7-4f0d-b151-3fc640bef588
    internal-label: Intermediate
topic_v2:
  - id: c7d04a2c-412a-4c9d-9d7a-4456eaa5adeb
    internal-label: Governance
  - id: d095671a-1355-40aa-8b5f-06c33c68080b
    internal-label: Security
  - id: f4e6943a-c91a-4134-a2c7-f4f20cfff2f0
    internal-label: Privacy
---
# Set up & manage customer managed keys {#cmk}

>[!AVAILABILITY]
>
>[!DNL Customer Managed Keys] functionality is currently available only for organizations that have purchased the [Healthcare Shield or Privacy & Security Shield](https://experienceleague.adobe.com/docs/events/customer-data-management-voices-recordings/governance/healthcare-shield.html){target="_blank"} add-on offering.

With Adobe Journey Optimizer, [Healthcare Shield](https://www.adobe.com/trust/compliance/hipaa-ready.html){target="_blank"} and Privacy & Security Shield customers have the ability to leverage Azure Customer Managed Keys (CMK) and apply them to their data.

The setup process for Journey Optimizer involves two parts, leveraging technology from both Adobe Experience Platform and Customer Journey Analytics (CJA):

* Follow the steps outlined in the [Customer Managed Keys in Adobe Experience Platform](https://experienceleague.adobe.com/docs/experience-platform/landing/governance-privacy-security/customer-managed-keys.html){target="_blank"} documentation.
* Follow the steps outlined in the [Customer Managed Keys in Customer Journey Analytics](https://experienceleague.adobe.com/docs/analytics-platform/using/cja-privacy/cmk.html){target="_blank"} documentation. 
    
  Completing this setup process is necessary, even if you haven't purchased Customer Journey Analytics (CJA), as certain components of CJA are used in the background.

To go through the setup process, you can refer to the step-by-step detailed instructions in [Customer Managed Keys in Adobe Experience Platform](https://experienceleague.adobe.com/docs/experience-platform/landing/governance-privacy-security/encryption.html){target="_blank"} documentation.

Both Adobe Experience Platform and Customer Managed Keys ensure the security of your data by encrypting it in transit and at rest. Your data remains protected, regardless of whether you use Customer Managed Keys.

For more information on data encryption in Adobe Experience Platform, you can refer to the [documentation](https://experienceleague.adobe.com/docs/experience-platform/landing/governance-privacy-security/encryption.html){target="_blank"} on Data encryption.
