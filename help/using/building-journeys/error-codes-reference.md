---
solution: Journey Optimizer
product: journey optimizer
title: Error codes reference
description: Learn about common error codes in Adobe Journey Optimizer and how to troubleshoot them
feature: Journeys, Monitoring
topic: Content Management
role: User
level: Intermediate
keywords: error, codes, troubleshooting, journey, campaign, messages
---

# Error codes reference {#error-codes}

Adobe Journey Optimizer uses standardized error codes to help you quickly identify and resolve issues across journeys, campaigns, and message configurations. Understanding these error codes can significantly reduce troubleshooting time and help you maintain optimal campaign performance.

## Understanding error code structure {#error-code-structure}

Adobe Journey Optimizer error codes follow a consistent naming pattern that helps identify the component and issue type:

* **Service prefix**: Indicates which Adobe Journey Optimizer service generated the error (e.g., CJMPTS for Push/Transport Service, CJMRT for Journey Runtime, CJMMAS for Message Authoring Service)
* **Error number**: Unique identifier for the specific error condition
* **HTTP status code**: Standard HTTP status code (e.g., 400, 403, 422, 500)

Example: `CJMRT-030012-422` indicates a Journey Runtime error (CJMRT) with error number 030012 and HTTP status 422 (Unprocessable Entity).

## Where to find error codes {#find-error-codes}

Error codes appear in several locations within Adobe Journey Optimizer:

* Journey execution reports and logs
* Campaign activation screens
* Message validation warnings
* System notifications and alerts
* API responses (when using REST APIs)

When an error occurs, note the complete error code and any accompanying request ID, as these are essential for troubleshooting and support escalation.

## Common error codes by service {#error-codes-by-service}

### CJMPTS: Push and Transport Service errors {#cjmpts-errors}

These errors occur during push notification delivery and message transport operations.

| Error Code | Description | Root Cause | Resolution |
|------------|-------------|-----------|-----------|
| **CJMPTS-1510-500** | Internal server error on push-channel send | Backend push/transport malfunction; provider or infrastructure error | 1. Check channel provisioning settings<br/>2. Verify push credentials are valid<br/>3. Retry the operation<br/>4. If persistent, contact Adobe Support with request ID<br/><br/>**Related documentation**: [Push configuration](../push/push-configuration.md) |
| **CJMPTS-1023-500** | Internal server error during push send/process (third-party gateways) | Temporary cloud malfunction or unknown service error | 1. Verify provider/channel configuration<br/>2. Check third-party gateway status<br/>3. Retry after a few minutes<br/>4. Review logs for additional context<br/><br/>**Related documentation**: [Push notifications](../push/create-push.md) |
| **CJMPTS-1310-500** | Internal error from Render Service (preview or live send) | Downstream template renderer failed, usually due to JSON/template syntax issues | 1. Validate template syntax and structure<br/>2. Check all personalization variables are valid<br/>3. Use a test payload to identify the issue<br/>4. Simplify template complexity if needed<br/><br/>**Related documentation**: [Message templates](../content-management/content-templates.md), [Personalization syntax](../personalization/personalization-syntax.md) |

### CJMRT: Journey Runtime and API errors {#cjmrt-errors}

These errors occur during journey execution, event processing, and API operations.

| Error Code | Description | Root Cause | Resolution |
|------------|-------------|-----------|-----------|
| **CJMRT-030012-422** | Unprocessable entity - failed action, invalid event, or bad payload | Invalid input data (e.g., nonexistent audience, event, or attribute) | 1. Double-check input/event payload structure<br/>2. Verify referenced objects (audiences, datasets) exist and are active<br/>3. Validate all required fields are present<br/>4. Test with a known-good payload<br/><br/>**Related documentation**: [Journey troubleshooting](troubleshooting.md), [Events configuration](../event/about-events.md) |
| **CJMRT-130004-400** | Bad request - malformed input in journey node or channel config | Journey payload or configuration references removed/invalid resource | 1. Review journey node configuration<br/>2. Verify all referenced resources (messages, audiences, actions) exist<br/>3. Fix or update broken references<br/>4. Rebuild journey configuration if necessary<br/><br/>**Related documentation**: [Journey creation](journey-gs.md), [Custom actions](../action/about-custom-action-configuration.md) |
| **CJMRT-000032-409** | Conflict - resource already exists | Attempt to create resource with duplicate ID or name | 1. Use unique IDs and names for all resources<br/>2. Check for existing resources with same identifier<br/>3. Delete or rename conflicting objects<br/>4. Review naming conventions<br/><br/>**Related documentation**: [Journey versions](journey-gs.md#journey-versions) |
| **CJMRT-170016-400** | Bad request during journey config/preview | Payload missing required dependency or broken template link | 1. Validate all required resources are active<br/>2. Ensure templates and content blocks are published<br/>3. Check all dependencies are properly linked<br/>4. Review journey test mode results<br/><br/>**Related documentation**: [Testing journeys](testing-the-journey.md), [Journey dependencies](journey-gs.md) |
| **CJMRT-080608-400** | Bad request in domain/channel/delegation | Required DNS records or email/SMS configuration missing | 1. Complete DNS configuration for email domains<br/>2. Verify subdomain delegation is complete<br/>3. Run configuration wizards again<br/>4. Allow time for DNS propagation (up to 72 hours)<br/><br/>**Related documentation**: [Channel surfaces](../configuration/channel-surfaces.md), [Subdomain delegation](../configuration/delegate-subdomain.md) |
| **CJMRT-110100-500** | Internal error on payload | Backend data/config bug or unsupported configuration | 1. Retry the operation<br/>2. Simplify configuration if using advanced features<br/>3. Escalate to Adobe Support with request ID and exact payload<br/>4. Check for known issues in release notes<br/><br/>**Related documentation**: [Journey troubleshooting](troubleshooting.md) |

### CJMMAS: Message Authoring Service errors {#cjmmas-errors}

These errors occur when creating, editing, or publishing messages, presets, and content.

| Error Code | Description | Root Cause | Resolution |
|------------|-------------|-----------|-----------|
| **CJMMAS-1149-400** | Bad request when saving message, preset, or variant | Required fields missing in message or bad configuration | 1. Complete all required fields (marked with asterisk)<br/>2. Validate message/preset configuration<br/>3. Check field value formats and constraints<br/>4. Review validation messages in UI<br/><br/>**Related documentation**: [Email channel](../email/get-started-email.md), [Channel surfaces](../configuration/channel-surfaces.md) |
| **CJMMAS-2073-422** | Unprocessable entity in message preset edit | Validation error, unsupported field, or improper syntax | 1. Correct syntax/field errors as indicated<br/>2. Compare to a known-good configuration<br/>3. Use message UI validation before saving<br/>4. Review field requirements in documentation<br/><br/>**Related documentation**: [Message presets](../configuration/channel-surfaces.md), [Email settings](../email/email-settings.md) |
| **CJMMAS-1300-500** | Internal error from message authoring | Backend crash due to infrastructure issue, large content, or service downtime | 1. Simplify template/content (reduce size/complexity)<br/>2. Retry the operation<br/>3. Save work incrementally<br/>4. If persistent, escalate to Adobe Support<br/><br/>**Related documentation**: [Content templates](../content-management/content-templates.md) |
| **CJMMAS-2001-200** | Success status but error banner: opt-out link missing | Required unsubscribe link missing in email variant | 1. Add opt-out/unsubscribe link to all email variants<br/>2. Ensure link is present in every language version<br/>3. Use personalization helper to insert opt-out link<br/>4. Test all variants before publishing<br/><br/>**Related documentation**: [Opt-out management](../privacy/opt-out.md), [Email design](../email/content-from-scratch.md) |
| **CJMMAS-1603-403** | Forbidden when updating/publishing template or preset | User lacks required permission/role, or action not allowed in current state | 1. Verify user has appropriate permissions (Message Manager, Author, etc.)<br/>2. Check preset/template status (draft, published, archived)<br/>3. Request access from administrator if needed<br/>4. Review product profile assignments<br/><br/>**Related documentation**: [Permissions](../administration/permissions.md), [Access control](../administration/permissions-overview.md) |

### CJMCMP: Campaign errors {#cjmcmp-errors}

These errors occur during campaign creation, configuration, and activation.

| Error Code | Description | Root Cause | Resolution |
|------------|-------------|-----------|-----------|
| **CJMCMP-2050-400** | Bad request in campaign activation or approval | Campaign references invalid/missing policy or segment | 1. Audit all campaign node configurations<br/>2. Verify policy/segment links are current and valid<br/>3. Update with correct configuration<br/>4. Re-test campaign before activation<br/><br/>**Related documentation**: [Campaign creation](../campaigns/create-campaign.md), [Campaign approval](../test-approve/gs-approval.md) |

## General troubleshooting approach {#troubleshooting-approach}

When encountering an error code, follow this systematic approach:

1. **Identify the error**: Note the complete error code, HTTP status, and any accompanying message or request ID.

2. **Find the service**: Use the service prefix (CJMPTS, CJMRT, CJMMAS, CJMCMP) to identify which component is affected.

3. **Check the status code**:
   * **400 (Bad Request)**: Review input data and configuration
   * **403 (Forbidden)**: Check permissions and access rights
   * **409 (Conflict)**: Look for duplicate or conflicting resources
   * **422 (Unprocessable Entity)**: Validate data against schema requirements
   * **500 (Internal Server Error)**: Retry and potentially escalate to support

4. **Review recent changes**: Consider what was modified recently (journey updates, new campaigns, configuration changes, etc.).

5. **Consult documentation**: Use the links provided in this guide to access detailed documentation for the affected feature.

6. **Retry when appropriate**: For 500-series errors, a simple retry after a few minutes often resolves transient issues.

7. **Escalate when needed**: If the error persists after following resolution steps, contact Adobe Support with:
   * Complete error code
   * Request ID (if available)
   * Steps to reproduce
   * Relevant configuration details

## Best practices to avoid common errors {#best-practices}

### Before journey activation {#journey-best-practices}

* **Validate all resources**: Ensure all referenced audiences, data sources, and custom actions are active
* **Test thoroughly**: Use test mode to identify issues before publishing ([Learn more](testing-the-journey.md))
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
4. **Engage community**: Post questions in the [Adobe Journey Optimizer Community](https://experienceleaguecommunities.adobe.com/t5/journey-optimizer/ct-p/journey-optimizer){target="_blank"}
5. **Contact Adobe Support**: Submit a support ticket with all relevant details

>[!NOTE]
>
>This error code reference is continuously updated as new codes are identified and documented. For the most current information, check the [Adobe Journey Optimizer Community blogs](https://experienceleaguecommunities.adobe.com/t5/journey-optimizer-blogs/bg-p/journey-optimizer-blogs){target="_blank"} regularly.

**Related topics**

* [Demystifying Adobe Journey Optimizer Error Codes: Part 1](https://experienceleaguecommunities.adobe.com/t5/journey-optimizer-blogs/demystifying-adobe-journey-optimizer-error-codes-root-causes-and/ba-p/760884){target="_blank"}
* [Demystifying Adobe Journey Optimizer Error Codes: Part 2](https://experienceleaguecommunities.adobe.com/t5/journey-optimizer-blogs/demystifying-adobe-journey-optimizer-error-codes-root-causes-and/bc-p/782661){target="_blank"}

