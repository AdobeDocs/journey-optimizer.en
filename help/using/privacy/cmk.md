---
solution: Journey Optimizer
product: journey optimizer
title: Customer Managed Keys
description: Learn how to setup and manage customer keys for Adobe Journey Optimizer.
feature: Privacy, Monitoring
role: Developer, User, Admin, Leader
level: Intermediate
exl-id: f0985d1f-0bcf-452f-bd46-dfeca0424f01
---
# Set up and manage Customer Managed Keys for Adobe Journey Optimizer {#cmk}

>[!AVAILABILITY]
>
>[!DNL Customer Managed Keys] functionality is currently available only for organizations that have purchased the [Healthcare Shield or Privacy & Security Shield](https://experienceleague.adobe.com/docs/events/customer-data-management-voices-recordings/governance/healthcare-shield.html) add-on offering.

With Adobe Journey Optimizer, [Healthcare Shield](https://www.adobe.com/trust/compliance/hipaa-ready.html) and Privacy & Security Shield customers have the ability to leverage Azure Customer Managed Keys (CMK) and apply them to their data.

The setup process for Journey Optimizer involves two parts, leveraging technology from both Adobe Experience Platform and Customer Journey Analytics (CJA):

* Follow the steps outlined in the [Customer Managed Keys in Adobe Experience Platform](https://experienceleague.adobe.com/docs/experience-platform/landing/governance-privacy-security/customer-managed-keys.html) documentation.
* Follow the steps outlined in the [Customer Managed Keys in Customer Journey Analytics](https://experienceleague.adobe.com/docs/analytics-platform/using/cja-privacy/cmk.html) documentation. 
    
  Completing this setup process is necessary, even if you haven't purchased Customer Journey Analytics (CJA), as certain components of CJA are used in the background.

To go through the setup process, you can refer to the step-by-step detailed instructions in [Customer Managed Keys in Adobe Experience Platform](https://experienceleague.adobe.com/docs/experience-platform/landing/governance-privacy-security/encryption.html) documentation.

Both Adobe Experience Platform and Customer Managed Keys ensure the security of your data by encrypting it in transit and at rest. Your data remains protected, regardless of whether you use Customer Managed Keys.

For more information on data encryption in Adobe Experience Platform, you can refer to the [documentation](https://experienceleague.adobe.com/docs/experience-platform/landing/governance-privacy-security/encryption.html) on Data encryption.
