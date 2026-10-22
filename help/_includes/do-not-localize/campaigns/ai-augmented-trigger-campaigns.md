---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how to retrieve the generated cURL request of an activated API triggered campaign and use it in the APIs to trigger the campaign, with troubleshooting for email delivery delays and Azure Cosmos DB authentication errors.

**Intents:**

* Retrieve the generated sample cURL request of a live API triggered campaign
* Use the cURL request in the APIs to build the payload and trigger the campaign
* Know that campaign start and end dates and a call timeout apply to the API call
* Find the endpoints for standard and High throughput campaigns
* Troubleshoot email delivery delays and 500 Internal Server Errors caused by Azure Cosmos DB authentication

**Glossary:**

* **cURL request**: Section of the campaign that holds the generated sample request; its payload includes all personalization (profile and context) variables used in the message
* **Interactive Message Execution REST API**: The API into which you use the cURL request to build your payload and trigger the campaign *(product-specific)*
* **Azure service principal**: The identity required for Azure Cosmos DB authentication *(product-specific)*

**Guardrails:**

* If a specific start and/or end date was configured when creating the campaign, the campaign is not executed outside these dates, and API calls fail.
* The call to the Interactive Message Execution REST API has a timeout of 60 sec. Internal retries are in place in case of unexpected timeouts to guarantee the delivery.
* The endpoints in the cURL section differ between standard and High throughput campaigns.

**Prerequisites and permissions:**

* The campaign must be activated: the cURL request is available once the campaign is live.

**Applicability:**

* Applies to API triggered campaigns, both standard and High throughput.

**Terminology:**

* Canonical name: Execute an API triggered campaign
* Acronym: CMK — Customer-Managed Keys (used on the page body)

**FAQ:**

* **Q: Where do I find the request to trigger my campaign?** — Open the campaign, then copy-paste the payload request from the **cURL request** section. It is available once the campaign is live.
* **Q: What does the cURL payload contain?** — All personalization (profile and context) variables used in the message.
* **Q: Why do my API calls fail?** — If a specific start and/or end date was configured when creating the campaign, it is not executed outside these dates, and API calls fail.
* **Q: Where are the endpoints for standard and High throughput campaigns listed?** — In the Interactive Message Execution API documentation.
* **Q: Where can I find API call examples?** — On the messaging samples page of the Journey Optimizer APIs documentation.

**Troubleshooting:**

* Email delivery delays — If email delivery times exceed expectations, investigate potential outages or performance issues with external services, such as cloud infrastructure providers or email service providers. [!DNL Journey Optimizer] logs record message departure timestamps, which can help determine whether delays occurred downstream in the delivery pipeline.
* Azure cosmos DB authentication errors (500 internal server error) — Symptom: 500 Internal Server Errors when triggering API-triggered campaigns, and the system logs show a 403 Forbidden error from Azure Cosmos DB with a message such as "Access to your account is currently revoked because the Azure Cosmos DB service is unable to obtain the AAD authentication token for the account's default identity". Cause: the Azure service principal required for Cosmos DB authentication has been disabled, deleted, or misconfigured. Documented resolution: verify that the Azure service principal or managed identity is enabled and has not been disabled or deleted in your Azure Active Directory; check that the service principal has the necessary permissions and role assignments to access the Azure Key Vault and Cosmos DB resources; if you are using Customer-Managed Keys (CMK), consult the Azure Cosmos DB CMK troubleshooting guide; after correcting the configuration, re-enable the service principal if it was disabled, and re-test your transactional campaign API calls to confirm that authentication succeeds and messages are delivered.

**Related pages:**

* Differences between standard and High throughput endpoints: High throughput campaigns (campaigns/api-triggered-high-throughput.md)
* All endpoints for standard and High throughput campaigns: Interactive Message Execution API documentation (https://developer.adobe.com/journey-optimizer-apis/references/messaging#tag/execution)
* API call examples: page linked as "this page", messaging samples of the Journey Optimizer APIs documentation (https://developer.adobe.com/journey-optimizer-apis/references/messaging-samples)
* Azure Cosmos DB CMK errors: Azure Cosmos DB CMK troubleshooting guide (https://learn.microsoft.com/en-us/azure/cosmos-db/cmk-troubleshooting-guide#azure-active-directory-token-acquisition-error)

+++

<!-- ai-section-version: 1 | source-hash: 47d6b8d9 -->
