---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** This page explains how the Adobe Journey Optimizer MCP server (Beta) lets you query campaigns, journeys, and offers with plain-language prompts from MCP-compatible clients through read-only tools, and how to connect to it.

**Intents:**

* Understand the Model Context Protocol and how the Journey Optimizer MCP server exposes read-only tools to LLMs
* Learn the available campaign, journey, and channel configuration tools
* Query campaigns, journeys, and offers using natural-language prompts
* Verify channel configuration details and governance policies
* Connect the MCP server through a supported MCP client
* Understand prerequisites and permissions for using the integration

**Glossary:**

* **Model Context Protocol (MCP)**: Open standard that lets applications expose back-end tools to large language models in a uniform way *(product-specific)*
* **Adobe Journey Optimizer MCP server**: Server that surfaces campaign and sandbox operations inside MCP-compatible applications, exposing retrieve APIs as plain-language answers *(product-specific)*
* **Visualize your journeys**: Tool that renders journeys with interactive tools so you can explore their structure and flow visually *(product-specific)*
* **Marketing actions**: Available actions listed for data governance policy enforcement *(product-specific)*

**Guardrails:**

* This is a Beta feature, provided "as is" without warranty of any kind, and is considered Confidential Information of Adobe.
* All operations are read-only; write operations (creating, updating, or deleting objects) are not supported in the current Beta release.
* The MCP server is currently available in Claude Web, Claude Desktop, and Cursor.
* Prerequisites: an active Journey Optimizer license, access to a supported MCP-compatible application, and the necessary permissions to view campaigns, journeys, and offers (at minimum View permissions for the objects you query).
* When you submit a prompt, the MCP client may send relevant context, including Journey Optimizer data returned by the server, to its model for processing.
* Adobe encourages testing integrations in a sandbox environment prior to productive use and validating all MCP-initiated actions and responses before relying on them.

**Terminology:**

* Canonical name: Adobe Journey Optimizer MCP server — Acronym: MCP (Model Context Protocol) — variants: AJO MCP server, MCP integration
* Synonyms: "MCP client" = "MCP-compatible application"
* Do not confuse: campaign statuses "DRAFT" / "LIVE" / "STOPPED" / "COMPLETED" (used by the List Campaigns tool) ≠ channel configuration statuses "draft" / "active" / "archived" / "deactivated" (used by the List Channel Configurations tool)

**FAQ:**

* **Q: Which MCP clients are supported?** — Claude Web, Claude Desktop, and Cursor; support for additional MCP-compatible applications may be added in future releases.
* **Q: Can the MCP server change my data?** — No; all operations are read-only and write operations are not supported in the current release.
* **Q: What permissions do I need?** — At minimum View permissions for the objects you want to query (campaigns, journeys, or offers); no write permissions are required.
* **Q: What server endpoint URL do I use?** — `https://ajo-mcp.adobe.io/mcp`; in Claude Web or Claude Desktop, go to Connectors and select Adobe Journey Optimizer.
* **Q: Do I need developer access?** — No; the MCP server is designed for both marketing and technical personas.
* **Q: Can I use it with sandboxes?** — Yes; the MCP server respects your sandbox configuration and you can query sandbox-specific data.

+++

<!-- ai-section-version: 1 | source-hash: d1e40580 -->
