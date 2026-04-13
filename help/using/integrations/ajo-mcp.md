---
solution: Journey Optimizer
product: journey optimizer
title: Work with AI assistants via MCP
description: Learn how to connect Adobe Journey Optimizer to AI assistants using the MCP server
feature: Integrations
topic: Content Management, Artificial Intelligence
badge: label="Limited availability" type="Informative"
role: User, Developer
level: Beginner, Intermediate
---
# Work with AI assistants via MCP {#ajo-mcp}

>[!AVAILABILITY]
>
>The [!DNL Adobe Journey Optimizer] MCP server is currently available in **Claude Web** and **Claude Desktop** only.

## What is the Model Context Protocol? {#mcp-overview}

Marketing and customer-experience teams increasingly rely on chat-based applications and developer tools — such as Anthropic Claude, OpenAI ChatGPT, Cursor, and Microsoft Copilot Studio — to streamline their day-to-day work. These applications support the **Model Context Protocol (MCP)**, an open standard that lets applications expose back-end tools to large language models (LLMs) in a uniform way.

[!DNL Adobe Journey Optimizer] now provides an MCP server that surfaces campaign, journey, loyalty, and sandbox operations directly inside any MCP-compatible application. With the [!DNL Adobe Journey Optimizer] MCP integration, different personas can collaborate around the same orchestration data — without writing queries against the [!DNL Adobe Journey Optimizer] REST API or navigating multiple UI screens. Customers can describe their intent conversationally and let the LLM invoke the appropriate MCP tools.

## Key capabilities {#mcp-capabilities}

The [!DNL Adobe Journey Optimizer] MCP server lets you inspect, summarize, and troubleshoot [!DNL Adobe Journey Optimizer] journeys, campaigns, and offers directly from your AI assistant. [!DNL Adobe Journey Optimizer]'s retrieve APIs are turned into plain-language answers so you can:

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

Before connecting the [!DNL Adobe Journey Optimizer] MCP server to your AI assistant, ensure the following:

* You have an active [!DNL Adobe Journey Optimizer] license.
* You have access to a supported MCP-compatible application (currently Claude Web or Claude Desktop).
* You have the necessary permissions in [!DNL Adobe Journey Optimizer] to view campaigns, journeys, and offers.

## Connect the [!DNL Adobe Journey Optimizer] MCP server {#mcp-connect}

>[!NOTE]
>
>Detailed setup steps will be added once the integration is generally available. Contact your Adobe representative for early access.

<!--
Step-by-step connection instructions to be added here, including:
- How to obtain MCP server credentials from [!DNL Adobe Journey Optimizer]
- How to configure the MCP server in Claude Desktop / Claude Web
- How to authenticate
-->

## Frequently asked questions {#mcp-faq}

+++Which AI assistants are supported?

The [!DNL Adobe Journey Optimizer] MCP server is currently available for **Claude Web** and **Claude Desktop**. Support for additional MCP-compatible applications may be added in future releases.
+++

+++What [!DNL Adobe Journey Optimizer] objects can I access via MCP?

You can access campaigns, journeys, offers, loyalty data, and sandbox information. Operations are read-only (retrieve APIs); write operations are not supported in the current release.
+++

+++Do I need developer access to use the [!DNL Adobe Journey Optimizer] MCP server?

No. The MCP server is designed for both marketing and technical personas. Marketers can interact with it using natural language prompts in Claude, while developers can also use it in developer tools that support MCP.
+++

+++Is my data sent to the AI assistant provider?

When you submit a prompt, the AI assistant may send relevant context (including [!DNL Adobe Journey Optimizer] data returned by the MCP server) to its model for processing. Review the privacy and data-handling policies of your AI assistant provider before connecting to production data.
+++

