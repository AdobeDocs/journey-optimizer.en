---
solution: Journey Optimizer
product: journey optimizer
title: Review and activate a campaign
description: Learn how to review and activate campaigns in Journey Optimizer
feature: Campaigns
topic: Content Management
role: User
level: Intermediate
keywords: campaign, review, validation, activation, activating, optimizer
exl-id: 86f35987-f0b7-406e-9ae6-0e4a2e651610
TQID: https://experienceleague.adobe.com/Q9UQEnAqQNFD869w4lQOQxcbH82SwDZyT8Q-9RvRD5k
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: d556b755-390a-43f0-be32-a08cf6236126
    internal-label: Configuration
  - id: a653cc2e-bc85-4353-a306-399e5b247978
    internal-label: Journey Optimizer campaigns
subfeature_v2:
  - id: f7479fa1-474b-479d-8c98-f6cee5865a38
    internal-label: API triggered campaigns
  - id: ee67bd4a-25ee-4cdd-9eab-0d7549fde0c6
    internal-label: Campaign management
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
level_v2:
  - id: b5a62a22-46f7-4f0d-b151-3fc640bef588
    internal-label: Intermediate
topic_v2:
  - id: c1579802-ddd4-4214-8a91-97b2066abe11
    internal-label: Troubleshooting
  - id: e0eb8757-182f-49f3-94a4-1587d16f5094
    internal-label: Personalization
---
# Execute an API triggered campaign {#execute}

Once your campaign has been activated, you need to retrieve the generated sample cURL request and use it into the API to build your payload and trigger the campaign.

## Must-read {#must-read}

* **Campaign start/end dates** - If you have configured a specific start and/or end date when creating the campaign, it will not be executed outside these dates, and API calls will fail.

* **Call timeout** - The call to the Interactive Message Execution REST API has a timeout of 60 sec. However internal retries are in place in case of unexpected timeouts to guarantee the delivery.

## Trigger the campaign {#trigger}

1. Open the campaign, then copy-paste the payload request from the **[!UICONTROL cURL request]** section. This payload includes all personalization (profile and context) variables used in the message. It is available once the campaign is live.

    ![](assets/api-triggered-curl.png)

    >[!IMPORTANT]
    >
    >The endpoints in the cURL section differ between standard and [High throughput campigns](../campaigns/api-triggered-high-throughput.md).

1. Use this cURL request into the APIs to build your payload and trigger the campaign. For more information, refer to the [Interactive Message Execution API documentation](https://developer.adobe.com/journey-optimizer-apis/references/messaging#tag/execution), where all endpoints for standard and High throughput campaigns are listed.

    API call examples are also available on [this page](https://developer.adobe.com/journey-optimizer-apis/references/messaging-samples).

## Troubleshooting {#troubleshooting}

### Email delivery delays {#delivery-delays}

If email delivery times exceed expectations, investigate potential outages or performance issues with external services, such as cloud infrastructure providers or email service providers. Journey Optimizer logs record message departure timestamps, which can help determine whether delays occurred downstream in the delivery pipeline.

### Azure cosmos DB authentication errors (500 internal server error) {#cosmosdb-auth-errors}

If you encounter **500 Internal Server Errors** when triggering API-triggered campaigns, and the system logs show a **403 Forbidden** error from Azure Cosmos DB with a message such as:

_"Access to your account is currently revoked because the Azure Cosmos DB service is unable to obtain the AAD authentication token for the account's default identity"_

This error typically occurs when the Azure service principal required for Cosmos DB authentication has been disabled, deleted, or misconfigured.

+++How to resolve this issue

1. **Verify your Azure service principal** - Ensure that your Azure service principal or managed identity is enabled and has not been disabled or deleted in your Azure Active Directory.

1. **Check permissions** - Confirm that the service principal has the necessary permissions to access the Azure Key Vault and Cosmos DB resources. The service principal must have appropriate role assignments to authenticate with Azure Cosmos DB.

1. **Review Azure Cosmos DB CMK configuration** - If you are using Customer-Managed Keys (CMK), consult the [Azure Cosmos DB CMK troubleshooting guide](https://learn.microsoft.com/en-us/azure/cosmos-db/cmk-troubleshooting-guide#azure-active-directory-token-acquisition-error){target="_blank"} for detailed steps to restore AAD token acquisition.

1. **Re-enable and test** - After correcting the configuration, re-enable the service principal if it was disabled, and re-test your transactional campaign API calls to confirm that authentication succeeds and messages are delivered.

>[!NOTE]
>
>This issue is typically caused by a misconfiguration or accidental disabling of the Azure service principal required for Cosmos DB authentication. Keeping the service principal enabled and properly configured will prevent this error in the future.

+++
