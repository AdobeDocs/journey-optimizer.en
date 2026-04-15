---
solution: Journey Optimizer
product: journey optimizer
title: Work with MCP clients
description: Learn how to connect Adobe Journey Optimizer to MCP clients using the MCP server
feature: Integrations
topic: Content Management, Artificial Intelligence
badge: label="Beta" type="Informative"
role: User, Developer
level: Beginner, Intermediate
hide: true
---
# Work with MCP clients {#ajo-mcp}

>[!AVAILABILITY]
>
>The [!DNL Adobe Journey Optimizer] MCP server is currently available in **Claude Web** and **Claude Desktop** only. Support for additional MCP-compatible applications will be added in future releases.

The [!DNL Adobe Journey Optimizer] MCP integration lets you query campaigns, journeys, and offers using plain-language prompts — without writing API calls or navigating product screens. This page explains how the integration works, what you can do with it, and how to get started.

## What is the Model Context Protocol? {#mcp-overview}

Marketing and customer-experience teams increasingly rely on chat-based applications and developer tools — such as Anthropic Claude, OpenAI ChatGPT, Cursor, and Microsoft Copilot Studio — to streamline their day-to-day work. These applications support the **Model Context Protocol (MCP)**, an open standard that lets applications expose back-end tools to large language models (LLMs) in a uniform way.

[!DNL Adobe Journey Optimizer] now provides an MCP server that surfaces campaign, journey, loyalty, and sandbox operations directly inside any MCP-compatible application. With the [!DNL Adobe Journey Optimizer] MCP integration, different personas can collaborate around the same orchestration data — without writing queries against the [!DNL Adobe Journey Optimizer] REST API or navigating multiple UI screens. Customers can describe their intent conversationally and let the LLM invoke the appropriate MCP tools.

## Key capabilities {#mcp-capabilities}

The [!DNL Adobe Journey Optimizer] MCP server lets you inspect, summarize, and troubleshoot journeys, campaigns, and offers directly from your AI assistant. All operations are **read-only** — the MCP server surfaces retrieve APIs as plain-language answers so you can:

* **Understand journey logic** — Get a human-readable summary of any journey's branching, conditions, and actions.
* **Check campaign readiness** — Identify blockers that prevent a campaign from being published.
* **Spot coverage gaps** — See which channels are covered across your live journeys and campaigns, and where gaps exist.
* **Audit your orchestration portfolio** — Review the full status of campaigns and journeys without parsing JSON or jumping across product screens.

## Use cases {#mcp-use-cases}

The following examples show how to interact with the [!DNL Adobe Journey Optimizer] MCP server using natural language:

| Goal | Example prompt |
|---|---|
| **Summarize campaign details** | "Get campaign cmp456 and summarize audience, schedule, status, and packages." |
| **Inventory & status audit** | "What do we have and what state is it in? Show live vs. draft vs. completed/stopped/archived counts for campaigns." |
| **Check publish readiness** | "Why is campaign cmp456 not ready to publish? Show me the blockers." |
| **Compare objects** | "Compare campaigns abc123 and xyz789 — what changed in status and schedule?" |
| **Audit your portfolio** | "Across all live journeys and campaigns, which channels are covered and where are the gaps?" |
| **Channel coverage & mix** | "Show the channel footprint across journeys, campaigns, and offer placements — email-only vs. multi-channel, push/SMS/in-app usage, and mismatches between journey channels." |

## Prerequisites {#mcp-prerequisites}

Before connecting the [!DNL Adobe Journey Optimizer] MCP server to your MCP client, ensure the following:

* You have an active [!DNL Adobe Journey Optimizer] license.
* You have access to a supported MCP-compatible application (currently Claude Web or Claude Desktop).
* You have the necessary permissions in [!DNL Adobe Journey Optimizer] to view campaigns, journeys, and offers.

## Connect the [!DNL Adobe Journey Optimizer] MCP server {#mcp-connect}

>[!NOTE]
>
>This integration is in Beta. Detailed setup steps will be published when it reaches general availability. Contact your Adobe representative to request early access and receive configuration instructions.

During the Beta phase, your Adobe representative will provide:

* The MCP server endpoint URL specific to your organization.
* Authentication credentials for connecting your AI assistant to [!DNL Adobe Journey Optimizer].
* Guidance on configuring the MCP server in Claude Desktop or Claude Web.

<!--
Step-by-step connection instructions to be added here, including:
- How to obtain MCP server credentials from [!DNL Adobe Journey Optimizer]
- How to configure the MCP server in Claude Desktop / Claude Web
- How to authenticate
-->

## Frequently asked questions {#mcp-faq}

+++Which MCP clients are supported?

The [!DNL Adobe Journey Optimizer] MCP server is currently available for **Claude Web** and **Claude Desktop**. Support for additional MCP-compatible applications may be added in future releases.
+++

+++What [!DNL Adobe Journey Optimizer] objects can I access via MCP?

You can access campaigns, journeys, offers, loyalty data, and sandbox information. Operations are read-only (retrieve APIs); write operations are not supported in the current release.
+++

+++Do I need developer access to use the [!DNL Adobe Journey Optimizer] MCP server?

No. The MCP server is designed for both marketing and technical personas. Marketers can interact with it using natural language prompts in any supported MCP client, while developers can also use it in developer tools that support MCP.
+++

+++Is my data sent to the MCP client provider?

When you submit a prompt, the MCP client may send relevant context (including [!DNL Adobe Journey Optimizer] data returned by the MCP server) to its model for processing. Review the privacy and data-handling policies of your MCP client provider before connecting to production data.
+++

+++What permissions do I need in [!DNL Adobe Journey Optimizer]?

You need at minimum **View** permissions for the objects you want to query — campaigns, journeys, or offers. No write permissions are required because the MCP server only performs read operations. Contact your [!DNL Adobe Journey Optimizer] administrator if you are unsure about your current access level.
+++

+++Can I use the MCP server in sandbox environments?

Yes. The MCP server respects your [!DNL Adobe Journey Optimizer] sandbox configuration. You can query sandbox-specific data by specifying the sandbox in your prompt or by connecting with credentials scoped to a particular sandbox.
+++
