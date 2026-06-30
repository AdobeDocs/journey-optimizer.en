---
title: Custom channel prerequisites and guardrails
description: Learn about the prerequisites, guardrails, and required permissions to set up and use custom channels in Adobe Journey Optimizer.
feature: Custom Channel
topic: Content Management
role: Admin
level: Experienced
---

# Custom channel prerequisites and guardrails {#custom-channel-prerequisites}

Before configuring and using custom channels in [!DNL Journey Optimizer], review the prerequisites and guardrails described on this page.

## Prerequisites {#prerequisites}

### License {#license}

Custom channels are available to all [!DNL Adobe Journey Optimizer] customers. No additional license is required. Usage is monetized per number of messages sent, cumulatively with other outbound messaging channels in your contract.

### External API endpoint {#api-endpoint}

Your external messaging system must expose an HTTPS endpoint that [!DNL Journey Optimizer] can call via HTTP POST. The endpoint must:

* Accept the payload format your channel defines (typically JSON).
* Support one of the authentication methods available in the Channel Builder: None, API Key, Basic authentication, OAuth 2.0, or Custom.
* Return an HTTP 2xx response to acknowledge successful receipt of the request.

>[!IMPORTANT]
>
>Only HTTPS endpoints are supported.

### Required permissions {#permissions}

The following permissions are required depending on the task. For a complete list of permissions and how to assign them to product profiles, refer to the [permissions reference](../administration/ootb-permissions.md).

| Task | Required permission |
|------|---------------------|
| Access the Channel Builder and view custom channels | **[!UICONTROL View custom channels]** |
| Create, edit, or archive custom channels | **[!UICONTROL Manage custom channels]** |
| View channel configurations | **[!UICONTROL View channel configurations]** |
| Create or edit channel configurations | **[!UICONTROL Manage channel configurations]** |
| Use a custom channel in a journey | **[!UICONTROL Manage journeys]** and **[!UICONTROL Publish journeys]** |
| Use a custom channel in a campaign | **[!UICONTROL Manage campaigns]** and **[!UICONTROL Publish campaigns]** |

## Guardrails and limitations {#guardrails}

<!--

### Phase 1 availability {#phase-1}

The following capabilities are available at GA. Features listed as *Future release* are not yet available.

| Capability | Availability |
|---|---|
| Channel Builder (create, configure, test) | GA |
| API credentials management | GA |
| Subdomain delegation for link tracking | GA |
| Channel configurations | GA |
| Use in Campaigns | GA |
| Use in Journeys | GA |
| Use in Orchestrated Campaigns | GA |
| Content authoring with code editor | GA |
| Full personalization (PE) — all capabilities except Experience Decisioning | GA |
| Expression fragments | GA |
| Click tracking on links (branded domain) | GA |
| Simulate / Preview & Proof | GA |
| Content experimentation | GA |
| OOTB Reporting: Live (24h) and Business Reporting (CJA) | GA |
| RBAC / ABAC | GA |
| Consent enforcement (CPES) | GA |
| Multilingual messaging | Future release |
| Business rules | Future release |
| Experience Decisioning (ExD) through PE | Future release |
| Reporting via webhook (delivered, read, seen) | Future release |
| Content templates for custom channels | Future release |
| AEM Content Fragment integration | Future release |
| AI Content Accelerator | Future release |
| Sandbox tooling (promote channel to another sandbox) | Future release |

-->

### Throughput and throttling {#throughput}

* The default throttling limit for a custom channel is **5,000 requests per second**, configurable at the channel level in the Channel Builder.
* Timeout default: **5,000 milliseconds**.
* Retry: enabled by default, with a default count of **3** retries (configurable range: 0–10).

If your external API endpoint enforces its own rate limits, align them with the throttling settings defined in the Channel Builder to avoid errors.

### IP allowlist {#ip-allowlist}

If your external system requires allowlisting specific IP addresses, Adobe provides documentation on the outbound IP ranges used by [!DNL Journey Optimizer]. Contact Adobe Customer Care to obtain the current list of IPs to allowlist.
