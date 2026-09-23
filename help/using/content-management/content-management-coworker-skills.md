---
solution: Journey Optimizer
product: journey optimizer
title: Coworker for content management
description: Discover the CX Enterprise Coworker content management tools available to discover, create, and manage Journey Optimizer content assets, with in-depth guidance and sample prompts.
feature: Overview
topic: Artificial Intelligence
role: User
level: Beginner
mini-toc-levels: 1
exl-id: 9f23a6f5-7221-4f87-95cd-047955ca33d5
feature_v2:
  - id: dc22c819-3f29-4e91-8b7d-5c6719831141
    internal-label: Content management
subfeature_v2:
  - id: d595a60b-bcf5-4a63-a189-66a0be755cc7
    internal-label: Templates
---

# Coworker for content management {#content-management-coworker-skills}

>[!BEGINSHADEBOX]

**On this page:** Discover the CX Enterprise Coworker content management tools available in Adobe Journey Optimizer — to browse, create, update, clone, and publish content templates, fragments, landing pages, and journey/campaign inline content — with detailed guidance, example prompts, and best practices. 

Learn more:

* [Coworker skills for Journey Optimizer](../start/ai-features.md#cx-coworker-skills) — overview of Coworker skills across Journeys, Loyalty, and Content Management in Journey Optimizer.
* [Coworker documentation](https://experienceleague.adobe.com/en/docs/cx-enterprise-ai/experience-cloud-ai/coworker/overview){target="_blank"} — overview of Coworker's Campaigns, Chat, and Projects capabilities.
* [Coworker Chat UI guide](https://experienceleague.adobe.com/en/docs/cx-enterprise-ai/experience-cloud-ai/coworker/chat/ui-guide){target="_blank"} — how to access and navigate Coworker Chat.

>[!ENDSHADEBOX]

## Content Management tools {#content-management}

>[!AVAILABILITY]
>
>Content Management is available for all customers who have access to Coworker.

Journey Optimizer users are able to discover and manage content assets — content templates, fragments, landing pages, and journey/campaign inline message content — directly from Coworker using natural language prompts. It lets you go from "tell me about my content" to "go build, update, and publish it," without leaving the conversation. This capability is powered by 15 read and write-capable MCP tools for Journey Optimizer content.

### Key use cases

1. **Browse and inspect content**

   * List available content templates, fragments, or landing pages, and retrieve their structure, metadata, and status.
   * Retrieve the inline message content configured on a journey or campaign action node.

   Sample prompts:
   * "List my email content templates."
   * "Show me the fragments available for my summer campaign."
   * "Get the details of landing page page-123."
   * "What content is configured for the email variant of the action node in campaign camp-789?"

1. **Create content templates**

   * Create a new content template for any channel.

   Sample prompts:
   * "Create an email template named Summer Sale with this HTML content."
   * "Create a new SMS template called Flash Alert."

1. **Update content templates**

   * Fully replace the content of an existing template.

   Sample prompts:
   * "Update template abc-123 with this new HTML body."

1. **Create, update, clone, and publish fragments**

   * Create a new HTML or expression fragment.
   * Update an existing fragment's content or metadata.
   * Clone an existing fragment under a new name.
   * Submit a draft fragment for publication.

   Sample prompts:
   * "Create an HTML fragment named Promo Banner with this markup."
   * "Update fragment frag-456 to change its name to Promo Banner V2."
   * "Clone fragment abc-123 as Promo Banner - Summer (Variant B)."
   * "Publish fragment frag-456."

1. **Update inline message content**

   * Replace one channel variant on a campaign or journey action node's inline message.
   * List the channel variants defined on a journey or campaign action node.

   Sample prompts:
   * "Update the email variant of the action node in campaign camp-789 with this new content."
   * "What channel variants are defined on this action node?"

### In scope

The following capabilities are supported by Content Management:

* **List and get content templates**: Browse content templates and retrieve their structure and metadata.
* **List and get fragments**: Browse content and expression fragments and retrieve their details.
* **List and get landing pages**: Browse landing pages and retrieve their metadata and page content.
* **Get campaign/journey inline content**: Retrieve the inline message content configured on a campaign or journey action node, including multi-lingual variants.
* **Create content templates**: Create a new template for any channel.
* **Update content templates**: Fully replace the content of an existing template.
* **Create, update, clone, and publish fragments**: Create new fragments, update existing ones, clone a fragment under a new name, and submit a draft fragment for publication.
* **Update inline message content**: Replace a channel variant on a campaign/journey action node's inline message, including multi-lingual variants, and list the channel variants defined on an action node.

### Out of scope

The following functionalities are currently not supported:

* **Full-text search across templates or fragments**
* **Template or fragment validation** (orphaned references, broken links, deprecated components)
* **Creating or publishing landing pages**
* **Deleting content templates, fragments, or landing pages**

### Prompting best practices

1. **Reference IDs when known**: Provide the template, fragment, landing page, or campaign/journey ID when asking to get, update, clone, or publish a specific asset.
1. **Be explicit about the channel**: When creating a template or fragment, specify the channel or content type (email, HTML fragment, expression fragment).
1. **Confirm before publishing**: Review a fragment's content after creating or updating it before asking Coworker to publish it.
1. **Provide complete replacement content**: Update operations replace content in full, so include the complete HTML body or variant content in your prompt.

{{$include /help/_includes/do-not-localize/start/ai-augmented-content-management-coworker-skills.md}}
