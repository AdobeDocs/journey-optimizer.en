---
solution: Journey Optimizer
product: journey optimizer
title: Error codes reference
description: Learn about common error codes in [!DNL Adobe Journey Optimizer] and how to troubleshoot them
feature: Journeys, Monitoring
topic: Content Management
role: User
level: Intermediate
keywords: error, codes, troubleshooting, journey, campaign, messages
exl-id: 84924153-1bb5-465a-b91c-797628fc816c
feature_v2:
  - id: baecb07f-ce89-4ebb-9cd9-0f7c053f944f
    internal-label: Journey management
subfeature_v2:
  - id: bf4bee78-72fe-48e8-ba77-2ecb14c2827d
    internal-label: Journey troubleshooting
---
# Error codes reference {#error-codes}

>[!BEGINSHADEBOX]

**On this page:** Learn how Adobe Journey Optimizer error codes are structured, where to find them, and how to troubleshoot common errors across journeys, campaigns, and message configurations.

>[!ENDSHADEBOX]

[!DNL Adobe Journey Optimizer] uses standardized error codes to help you quickly identify and resolve issues across journeys, campaigns, and message configurations. Understanding these error codes can significantly reduce troubleshooting time and help you maintain optimal campaign performance.

## Understanding error code structure {#error-code-structure}

[!DNL Adobe Journey Optimizer] error codes follow a consistent naming pattern that helps identify the component and issue type:

* **Service prefix**: Indicates which [!DNL Adobe Journey Optimizer] service generated the error.
  Examples: AJOJAS (Journey Authoring Service), CJMPTS (Push/Transport Service), CJMRT (Journey Runtime), CJMMAS (Message Authoring Service), CJMCMP (Campaign), CJMTL (Transport Layer), CJMRPS (Reporting/Provisioning Service)
* **Error number**: Unique identifier for the specific error condition
* **HTTP status code**: Standard HTTP status code (e.g., 400, 403, 422, 500)

Example: `CJMRT-000071-400` indicates a Journey Runtime error (CJMRT) with error number 000071 and HTTP status 400 (Bad Request).

## Where to find error codes {#find-error-codes}

Error codes appear in the following locations within [!DNL Adobe Journey Optimizer]:

* Journey execution reports and logs
* Campaign activation screens
* Message validation warnings
* System notifications and alerts
* API responses (when using REST APIs)

When an error occurs, note the complete error code and any accompanying request ID, as these are essential for troubleshooting and support escalation.

For error codes grouped by feature area, see the [Troubleshooting overview](../../rp_landing_pages/troubleshooting-overview-landing-page.md).

## Find error codes by feature area {#error-pages}

Each of the following pages lists the error codes of one feature area, with the exact message and how to fix it.

| Feature area | Page | Prefixes |
|---|---|---|
| Journeys | [Journey validation errors](journey-validation-errors.md) | AJOJAS |
| Campaigns | [Campaign errors](../campaigns/campaign-errors.md) | CJMCMP |
| Campaigns | [Orchestrated campaign errors](../orchestrated/orchestrated-campaign-errors.md) | CJMOC |
| Campaigns | [Relational schema and dataset errors](../orchestrated/relational-schema-errors.md) | CJMDMS |
| Campaigns | [Audience composition errors](../audience/audience-composition-errors.md) | CJMRT |
| Content | [Content authoring errors](../content-management/content-authoring-errors.md) | CJMMAS, CJMRT |
| Content | [Fragments and AEM content errors](../content-management/fragments-errors.md) | CJMMAS, AJOCBS, AJOAGS |
| Content | [Multilingual content errors](../content-management/multilingual-errors.md) | CJMRT, AJOCTO, CJMMAS |
| Content | [Landing page errors](../landing-pages/landing-page-errors.md) | CJMMAS |
| Content | [Proof and simulation errors](../content-management/proof-simulation-errors.md) | CJMPTS, AJOTDS, CJMSAS |
| Content | [Personalization errors](../personalization/personalization-errors.md) | CJMTL, CJMRT |
| Configuration | [Subdomain delegation and DNS errors](../configuration/subdomain-delegation-errors.md) | CJMRT |
| Configuration | [IP warmup plan errors](../configuration/ip-warmup-plan-errors.md) | CJMRT |
| Configuration | [Custom channel, inbound action, and reporting dataset errors](../configuration/channel-reporting-errors.md) | CJMRT, CJMIAS, CJMRPS |

## Common error codes by service {#error-codes-by-service}

Use this section to find error codes grouped by service.

### AJOJAS: Journey authoring errors {#ajojas-errors}

Errors returned when you validate, test, or publish a journey are listed in [Journey validation errors](journey-validation-errors.md).

### CJMPTS: Push and transport service errors {#cjmpts-errors}

These errors occur during push notification delivery and message transport operations.

| Error code | Description | Root cause | Resolution |
|------------|-------------|-----------|-----------|
| **CJMPTS-1410-500** | Internal server error on push/channel send action | Channel backend outage, expired credentials, misconfiguration, or provider bug | 1. Retry after delay<br/>2. Check provider configurations and quotas<br/>3. Verify push credentials are valid<br/>4. Test with an alternate channel<br/>5. If persistent, contact Adobe Support with request ID<br/><br/>**Related documentation**: [Push configuration](../push/push-configuration.md) |
| **CJMPTS-1006-404** | Push/SMS fails with "resource not found" | Referenced provider/channel does not exist, is misspelled, or was deprovisioned | 1. Review and correct provider/channel references and IDs<br/>2. Audit sandbox/organization configuration<br/>3. Verify channel configurations are active<br/>4. Re-create channel configuration if necessary<br/><br/>**Related documentation**: [Channel surfaces](../configuration/channel-surfaces.md) |
| **CJMPTS-1510-500** | Internal server error on push-channel send | Backend push/transport malfunction; provider or infrastructure error | 1. Check channel provisioning settings<br/>2. Verify push credentials are valid<br/>3. Retry the operation<br/>4. If persistent, contact Adobe Support with request ID<br/><br/>**Related documentation**: [Push configuration](../push/push-configuration.md) |
| **CJMPTS-1023-500** | Internal server error during push send/process (third-party gateways) | Temporary cloud malfunction or unknown service error | 1. Verify provider/channel configuration<br/>2. Check third-party gateway status<br/>3. Retry after a few minutes<br/>4. Review logs for additional context<br/><br/>**Related documentation**: [Push notifications](../push/create-push.md) |
| **CJMPTS-1310-500** | Internal error from Render Service (preview or live send) | Downstream template renderer failed, usually due to JSON/template syntax issues | 1. Validate template syntax and structure<br/>2. Check all personalization variables are valid<br/>3. Use a test payload to identify the issue<br/>4. Simplify template complexity if needed<br/><br/>**Related documentation**: [Message templates](../content-management/content-templates.md), [Personalization syntax](../personalization/personalization-syntax.md) |

### CJMRT: Journey Runtime and API errors {#cjmrt-errors}

These errors occur during journey execution, event processing, and API operations.

| Error code | Description | Root cause | Resolution |
|------------|-------------|-----------|-----------|
| **CJMRT-110001-500** | Maximum runs exceeded for workflow step (e.g., IP Affinity Provisioning step times out) | Workflow/provisioning job did not complete within retries/time allowed, often due to infrastructure/service lag or temporary backend issue | 1. Retry after some time<br/>2. Check [Adobe Status](https://status.adobe.com/){target="_blank"} for outages<br/>3. Escalate to Adobe Support with workflow/job/org details<br/>4. Provide logs and network captures if available<br/><br/>**Related documentation**: [Journey troubleshooting](troubleshooting.md) |
| **CJMRT-000071-400** | Data usage policy violation | The journey or campaign configuration uses a field restricted by a data governance policy | 1. Select the **[!UICONTROL Alerts]** button and open the error to see the policy violation<br/>2. Use the data lineage diagram to find the configuration changes to make<br/>3. Make the configuration changes before you activate your journey or campaign<br/><br/>**Related documentation**: [Data Governance](../action/action-privacy.md#violation) |
| **CJMRT-000013-401** | Unauthorized error during message runtime operation/API event | Authentication failure: token is expired, permissions are missing, or the integration/user has lost environment access | 1. Verify permissions and roles<br/>2. Refresh authentication token<br/>3. Use a known-valid user/service account<br/>4. Review product profile assignments<br/><br/>**Related documentation**: [Permissions](../administration/permissions.md) |
| **CJMRT-080605-400** | Bad request from journey runtime (e.g., node trigger, action, etc.) | Configuration references a removed/renamed or out-of-date feature/template/channel | 1. Validate all resource references<br/>2. Audit journey configuration and feature flags<br/>3. Update broken references<br/>4. Review recent system updates and migrations<br/><br/>**Related documentation**: [Journey creation](journey-gs.md) |
| **CJMRT-130004-400** | Bad request - malformed input in journey node or channel config | Journey payload or configuration references removed/invalid resource | 1. Review journey node configuration<br/>2. Verify all referenced resources (messages, audiences, actions) exist<br/>3. Fix or update broken references<br/>4. Rebuild journey configuration if necessary<br/><br/>**Related documentation**: [Journey creation](journey-gs.md), [Custom actions](../action/about-custom-action-configuration.md) |
| **CJMRT-000032-409** | Conflict - resource already exists | Attempt to create resource with duplicate ID or name | 1. Use unique IDs and names for all resources<br/>2. Check for existing resources with same identifier<br/>3. Delete or rename conflicting objects<br/>4. Review naming conventions<br/><br/>**Related documentation**: [Journey creation](journey-gs.md) |
| **CJMRT-170016-400** | Bad request during journey config/preview | Payload missing required dependency or broken template link | 1. Validate all required resources are active<br/>2. Ensure templates and content blocks are published<br/>3. Check all dependencies are properly linked<br/>4. Review journey test mode results<br/><br/>**Related documentation**: [Testing journeys](testing-the-journey.md), [Journey dependencies](journey-gs.md) |
| **CJMRT-080608-400** | Bad request in domain/channel/delegation | Required DNS records or email/SMS configuration missing | 1. Complete DNS configuration for email domains<br/>2. Verify subdomain delegation is complete<br/>3. Run configuration wizards again<br/>4. Allow time for DNS propagation (up to 72 hours)<br/><br/>**Related documentation**: [Channel surfaces](../configuration/channel-surfaces.md), [Subdomain delegation](../configuration/delegate-subdomain.md) |
| **CJMRT-110100-500** | Internal error on payload | Backend data/config bug or unsupported configuration | 1. Retry the operation<br/>2. Simplify configuration if using advanced features<br/>3. Escalate to Adobe Support with request ID and exact payload<br/>4. Check for known issues in release notes<br/><br/>**Related documentation**: [Journey troubleshooting](troubleshooting.md) |

### CJMMAS: message authoring service errors {#cjmmas-errors}

These errors occur when creating, editing, or publishing messages, presets, and content.

| Error code | Description | Root cause | Resolution |
|------------|-------------|-----------|-----------|
| **CJMMAS-1732-500** | Proof has failed - All assets not published when sending proof/test with AEM asset | Recently published asset isn't in AJO yet; asset ID mismatch; cross-repo use; AEM sync lag | 1. Use only published asset IDs from the correct repository/environment<br/>2. Allow time for sync between AEM and AJO<br/>3. Retry with a known-good asset<br/>4. Verify asset publishing status in AEM<br/><br/>**Related documentation**: [Assets integration](../integrations/assets.md) |
| **CJMMAS-1069-500** | Internal error saving or publishing message template | Backend exception (infrastructure/service bug or content issue); unsupported markup/feature | 1. Simplify or reduce the template complexity<br/>2. Re-add content in incremental steps to identify the issue<br/>3. Check the [Adobe Status page](https://status.adobe.com/){target="_blank"}<br/>4. Remove unsupported features or markup<br/><br/>**Related documentation**: [Content templates](../content-management/content-templates.md) |
| **CJMMAS-1149-400** | Bad request when saving message, preset, or variant | Required fields missing in message or bad configuration | 1. Complete all required fields (marked with asterisk)<br/>2. Validate message/preset configuration<br/>3. Check field value formats and constraints<br/>4. Review validation messages in UI<br/><br/>**Related documentation**: [Email channel](../email/get-started-email.md), [Channel surfaces](../configuration/channel-surfaces.md) |
| **CJMMAS-2073-400** | Message body not valid: the required `to` property is missing | The message body does not contain the required `to` property | 1. Provide the `to` property in the message body<br/>2. Try again |
| **CJMMAS-1300-500** | Internal error from message authoring | Backend crash due to infrastructure issue, large content, or service downtime | 1. Simplify template/content (reduce size/complexity)<br/>2. Retry the operation<br/>3. Save work incrementally<br/>4. If persistent, escalate to Adobe Support<br/><br/>**Related documentation**: [Content templates](../content-management/content-templates.md) |
| **CJMMAS-2001-200** | Success status but error banner: opt-out link missing | Required unsubscribe link missing in email variant | 1. Add opt-out/unsubscribe link to all email variants<br/>2. Ensure link is present in every language version<br/>3. Use personalization helper to insert opt-out link<br/>4. Test all variants before publishing<br/><br/>**Related documentation**: [Opt-out management](../privacy/opt-out.md), [Email design](../email/content-from-scratch.md) |
| **CJMMAS-1603-403** | Forbidden when updating/publishing template or preset | User lacks required permission/role, or action not allowed in current state | 1. Verify user has appropriate permissions (Message Manager, Author, etc.)<br/>2. Check preset/template status (draft, published, archived)<br/>3. Request access from administrator if needed<br/>4. Review product profile assignments<br/><br/>**Related documentation**: [Permissions](../administration/permissions.md), [Access control](../administration/permissions-overview.md) |

### CJMCMP: Campaign errors {#cjmcmp-errors}

These errors occur during campaign creation, configuration, and activation.

| Error code | Description | Root cause | Resolution |
|------------|-------------|-----------|-----------|
| **CJMCMP-6003-400** | "There is at least one incorrect campaign" when publishing/test mode journey/message | Node references a missing, unpublished, or invalid campaign; legacy or cloned journey not creating inlines | 1. Open each message node and verify configuration<br/>2. Re-link or re-add message nodes<br/>3. Activate test mode to force creation of inline campaigns<br/>4. Move to the new journey wizard if issue is frequent<br/><br/>**Related documentation**: [Journey creation](journey-gs.md), [Testing journeys](testing-the-journey.md) |
| **CJMCMP-2003-400** | UI banner: "The experiment is incorrect" in Email Designer | Stale or missing experiment/data provider; failed experiment cleanup, schema mismatch, or UI validation bug | 1. Remove unused experiment fields<br/>2. Validate schema and data provider connections<br/>3. Reload UI and clear browser cache<br/>4. Recreate node/email if issue unresolved<br/><br/>**Related documentation**: [Content experiments](../content-management/content-experiment.md) |
| **CJMCMP-2050-400** | Bad request in campaign activation or approval | Campaign references invalid/missing policy or segment | 1. Audit all campaign node configurations<br/>2. Verify policy/segment links are current and valid<br/>3. Update with correct configuration<br/>4. Re-test campaign before activation<br/><br/>**Related documentation**: [Campaign creation](../campaigns/create-campaign.md), [Campaign approval](../test-approve/gs-approval.md) |

### CJMTL: transport layer errors {#cjmtl-errors}

These errors occur during message transport and delivery operations.

| Error code | Description | Root cause | Resolution |
|------------|-------------|-----------|-----------|
| **CJMTL-010018-422** | "Personalization not allowed in domain name" when saving/sending content | Overly strict validation temporarily broke dynamic href domain personalization | 1. Refactor links if using domain variables<br/>2. Verify the latest AJO version is in use<br/>3. Retry the operation<br/>4. Use static domains if issue persists<br/><br/>**Related documentation**: [Personalization syntax](../personalization/personalization-syntax.md), [Email design](../email/content-from-scratch.md) |
| **CJMTL-010011-422** | Unprocessable entity - Push/SMS/Email send fails, says "invalid field" | Payload or recipient/contact data missing or invalid | 1. Inspect logs for specific field errors<br/>2. Fix profile/contact information<br/>3. Validate with test profile<br/>4. Refactor payload format as needed<br/><br/>**Related documentation**: [Profile management](../audience/get-started-profiles.md), [Test profiles](../audience/creating-test-profiles.md) |

### CJMRPS: reporting and provisioning service errors {#cjmrps-errors}

These errors occur during reporting configuration and dataset provisioning operations.

| Error code | Description | Root cause | Resolution |
|------------|-------------|-----------|-----------|
| **CJMRPS-1047-409** | "Conflict. Dataset has been added already" when adding reporting dataset | Attempting to add a dataset which is already provisioned | 1. Review dataset configuration in reporting settings<br/>2. Do not re-add datasets already present<br/>3. Use official migration checklists for reporting migration<br/>4. Remove duplicate dataset references<br/><br/>**Related documentation**: [Reporting overview](../reports/gs-reports.md), [Campaign reports](../reports/campaign-global-report-cja.md), [Journey reports](../reports/journey-global-report-cja.md) |

## General troubleshooting approach {#troubleshooting-approach}

When encountering an error code, follow this systematic approach:

1. **Identify the error**: Note the complete error code, HTTP status, and any accompanying message or request ID.

2. **Find the service**: Use the service prefix (AJOJAS, CJMPTS, CJMRT, CJMMAS, CJMCMP, CJMTL, CJMRPS) to identify which component is affected.

3. **Check the status code**:
   * **400 (Bad Request)**: Review input data and configuration
   * **403 (Forbidden)**: Check permissions and access rights
   * **409 (Conflict)**: Look for duplicate or conflicting resources
   * **422 (Unprocessable Entity)**: Validate data against schema requirements
   * **500 (Internal Server Error)**: Retry and potentially escalate to support

4. **Review recent changes**: Consider what was modified before the error first appeared (journey updates, new campaigns, configuration changes, etc.).

5. **Consult documentation**: Use the links provided in this guide to access detailed documentation for the affected feature.

6. **Retry when appropriate**: For 500-series errors, a simple retry after a short delay often resolves transient issues.

7. **Escalate when needed**: If the error persists after following resolution steps, [contact Adobe Support](../start/user-interface.md#support-ticket-guidelines) with the complete error code, request ID (if available), steps to reproduce, and relevant configuration details.

## Best practices to avoid common errors {#best-practices}

Use these practices to reduce avoidable errors and improve reliability.

### Before journey activation {#journey-best-practices}

* **Validate all resources**: Ensure all referenced audiences, events, data sources, and custom actions are properly configured
* **Test thoroughly**: Use test mode to identify issues before publishing ([Learn more](testing-the-journey.md))
* **Validate volumes**: Use dry run to validate audience reach and branch logic before going live ([Learn more](journey-dry-run.md))
* **Check permissions**: Verify you have necessary access rights for all components
* **Review dependencies**: Ensure all linked messages and content are published

### When creating messages {#message-best-practices}

* **Complete required fields**: Always fill in all mandatory fields before saving
* **Include opt-out links**: Add unsubscribe links to all email variants ([Learn more](../privacy/opt-out.md))
* **Validate personalization**: Test all dynamic content with sample profiles ([Learn more](../personalization/personalization-build-expressions.md))
* **Keep templates manageable**: Avoid overly complex templates that may cause rendering issues

### For campaign management {#campaign-best-practices}

* **Verify audience data**: Ensure target audiences are properly configured and populated
* **Check approval status**: Understand approval requirements before attempting to activate ([Learn more](../test-approve/gs-approval.md))
* **Monitor configurations**: Regularly review channel surfaces and presets for validity
* **Plan DNS changes**: Allow sufficient time for DNS propagation when updating domains

## Additional resources {#additional-resources}

* [Journey troubleshooting](troubleshooting.md)
* [Execution troubleshooting](troubleshooting-execution.md)
* [Inbound activities troubleshooting](troubleshooting-inbound.md)
* [Custom actions troubleshooting](../action/troubleshoot-custom-action.md)
* [Journey FAQs](journey-faq.md)
* [Guardrails and limitations](../start/guardrails.md)

## Getting support {#getting-support}

If you encounter persistent errors that cannot be resolved using this guide:

1. **Gather information**: Collect the error code, request ID, timestamps, and steps to reproduce
2. **Check system status**: Visit [Adobe Status](https://status.adobe.com/){target="_blank"} for known service issues
3. **Search documentation**: Review [Adobe Experience League](https://experienceleague.adobe.com/docs/journey-optimizer.html){target="_blank"} for solutions
4. **Engage community**: Post questions in the [[!DNL Adobe Journey Optimizer] Community](https://experienceleaguecommunities.adobe.com/t5/journey-optimizer/ct-p/journey-optimizer){target="_blank"}
5. **Contact Adobe Support**: [Submit a support ticket](../start/user-interface.md#support-ticket-guidelines) with all relevant details

>[!NOTE]
>
>This error code reference is continuously updated as new codes are identified and documented. For the most current information, check the [[!DNL Adobe Journey Optimizer] Community blogs](https://experienceleaguecommunities.adobe.com/t5/journey-optimizer-blogs/bg-p/journey-optimizer-blogs){target="_blank"} regularly.

{{$include /help/_includes/do-not-localize/building-journeys/ai-augmented-error-codes-reference.md}}
