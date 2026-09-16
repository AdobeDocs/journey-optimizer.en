---
solution: Journey Optimizer
product: journey optimizer
title: CX Coworker content management tools
description: Discover the CX Coworker content management tools available to discover, create, and manage Journey Optimizer content assets, with in-depth guidance and sample prompts.
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

# CX Coworker content management tools {#content-management-coworker-skills}

>[!BEGINSHADEBOX]

**On this page:** Discover the CX Coworker content management tools available in Adobe Journey Optimizer — to browse, create, update, clone, and publish content templates, fragments, landing pages, and journey/campaign inline content; to plan campaign strategy and generate on-brand copy and images across channels, locales, audiences, and variants; and to build, review, and hand off accessible email HTML — with detailed guidance, example prompts, and best practices.

Learn more:

* [CX Coworker skills for Journey Optimizer](ai-features.md#cx-coworker-skills) — overview of CX Coworker skills across Journeys, Loyalty, and Content Management in Journey Optimizer.
* [CX Coworker documentation](https://experienceleague.adobe.com/en/docs/cx-enterprise-ai/experience-cloud-ai/coworker/overview){target="_blank"} — overview of Coworker's Campaigns, Chat, and Projects capabilities.
* [Coworker Chat UI guide](https://experienceleague.adobe.com/en/docs/cx-enterprise-ai/experience-cloud-ai/coworker/chat/ui-guide){target="_blank"} — how to access and navigate Coworker Chat.

>[!ENDSHADEBOX]

## Content Management tools {#content-management}

>[!AVAILABILITY]
>
>Content Management is available for all customers who have access to CX Coworker.

Journey Optimizer users are able to discover and manage content assets — content templates, fragments, landing pages, and journey/campaign inline message content — directly from CX Coworker using natural language prompts. It lets you go from "tell me about my content" to "go build, update, and publish it," without leaving the conversation. This capability is powered by 15 read and write-capable MCP tools for Journey Optimizer content.

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

## Message Copy skill {#message-copy}

>[!AVAILABILITY]
>
>Message Copy is available for all customers who have access to CX Coworker. Generating images with a custom, brand-trained model requires production access to Firefly Services.

Message Copy takes a campaign or creative brief and turns it into a multi-dimensional content plan — spanning channels, touchpoints, locales, audiences, and variants — then generates the net-new copy and images to fill it. Generated content can be evaluated against brand and channel standards, edited in place, and saved back to the active solution (Adobe Journey Optimizer, Adobe Campaign v8, or Marketo).

### Key use cases

1. **Campaign and content strategy planning**

   * Capture the campaign strategy — objective, KPIs, audience strategy, channels, recurrence, and scheduling.
   * Brainstorm message maps, narrative arcs, and channel roles, and compare content strategy options before copy is written.
   * Structure the copy execution spec and build a multi-dimensional content plan matrix (channels × touchpoints × locales × audiences × variants).

1. **Copy generation across channels**

   * Generate net-new, on-brand copy for email, SMS, push, WhatsApp, social, and banner, grounded in your brand kit and voice.

1. **Image generation and variation**

   * Generate, crop, overlay, vary, and sign campaign images using Firefly.

1. **Copy evaluation, editing, and visual QA**

   * Assess and score existing copy against brand and channel standards at any point in its lifecycle.
   * Make in-place edits to existing copy — applying evaluation fixes, rephrasing, translating, or reacting to the latest preview.
   * Render copy HTML to a screenshot for visual inspection of hierarchy, spacing, hero dominance, and CTA placement.

1. **Multi-dimensional content expansion**

   * Fan an approved content plan matrix out into per-unit copy across every channel, locale, audience, and variant it defines.

1. **Publishing to your marketing solution**

   * Save accepted copy back to the active solution as an asset, a draft, or directly into the source template.

### In scope skills

The following capabilities are supported by Message Copy:

* **Campaign and creative brief capture**: Captures campaign strategy and structures it into a copy execution spec.
* **Content strategy planning**: Brainstorms message maps, narrative arcs, and channel roles ahead of copy generation.
* **Content plan matrix**: Builds a multi-dimensional plan across channels, touchpoints, locales, audiences, and variants.
* **Net-new copy generation**: Generates on-brand copy for email, SMS, push, WhatsApp, social, and banner.
* **Image generation**: Generates, crops, overlays, varies, and signs campaign images using Firefly.
* **Copy evaluation**: Scores existing copy against brand and channel standards.
* **In-place editing**: Applies fixes, rephrasing, translation, and directed revisions to existing copy.
* **Campaign expansion**: Fans an approved content plan out into per-unit copy across all defined dimensions.
* **Visual QA**: Renders copy HTML to a screenshot for visual inspection.
* **Save-back**: Saves approved content back to Adobe Journey Optimizer, Adobe Campaign v8, or Marketo.

### Out of scope skills

The following functionalities are currently not supported:

* **Automatic sub-field variant explosion**: Content plan cells are treated as whole copies — combinatorial sub-field variants, such as heading × subheading × CTA, are not auto-generated.
* **Selectable creative-direction options**: Content strategy options are presented as conversational text rather than selectable option cards.
* **Automatic character-limit trimming**: Channel character limits are carried into the brief but copy is not automatically trimmed to fit.
* **Firefly model catalog and selection**: There is no curated list of Firefly models to browse or validate against.
* **Aspect-ratio-driven generation**: Aspect ratio currently affects image cropping only, not the generation itself, and there are no named size presets.
* **Hero image reuse and advanced image editing**: Reusing a hero image and edit operations such as inpainting, background removal, and upscaling are planned but not yet available.
* **Engagement and predictive scoring**: Copy evaluation currently covers quality and compliance scoring only.
* **Journey-entry-point brief capture**: Capturing campaign strategy directly from the journey creation entry point is not yet supported.

### Prompting best practices

1. **Start with the brief**: Provide the campaign objective, audience, and channels up front so the content plan matrix reflects your intended scope.
1. **Specify plan dimensions**: Call out the channels, touchpoints, locales, audiences, and variants you want represented in the content plan.
1. **Include brand context**: Reference your brand kit or voice guidelines so generated copy and images stay on-brand.
1. **State character limits**: Provide channel character limits explicitly, and review generated copy to confirm it fits before publishing.
1. **Review before saving**: Evaluate and edit generated copy before asking Coworker to save it back to Adobe Journey Optimizer, Adobe Campaign v8, or Marketo.

## Email Design skill {#email-design}

>[!AVAILABILITY]
>
>Email Design is available for all customers who have access to CX Coworker.

Email Design turns a brief, a reference image or screenshot, or a Figma frame or URL into on-brand, accessible email HTML. It composes a block structure and styling, builds the HTML, reviews it for compliance, design quality, and accessibility, and hands the approved email off to Adobe Journey Optimizer or Adobe Campaign.

### Key use cases

1. **Email structure and styling planning**

   * Plan block structure and styling for an email — a layout plan — from a marketing objective and brand inputs.

1. **Email HTML creation and editing**

   * Build, adapt, edit, or refine email HTML from a layout plan, a reference screenshot, or a Figma design link.

1. **Brand design system management**

   * Set up, derive, enrich, and extend a brand's reusable email design system — tokens, layout patterns, and brand language — which feeds into email composition and building.

1. **Email review**

   * Audit an assembled email for on-brand, send-ready compliance — brand and channel guidelines, colors, fonts, plan adherence, and deliverability.
   * Get subjective design feedback on visual hierarchy, spacing, narrative flow, and brand fit.
   * Run a WCAG 2.1 AA accessibility audit covering contrast, alt text, reading order, link text, and font size.

1. **Handoff to your marketing solution**

   * Export and package an approved email for sending, and deliver it to Adobe Journey Optimizer or Adobe Campaign.

### In scope skills

The following capabilities are supported by Email Design:

* **Layout planning**: Plans block structure and styling from a marketing objective and brand inputs.
* **HTML build and edit**: Builds, adapts, edits, and refines email HTML from a layout plan, a screenshot, or a Figma design link.
* **Design system management**: Maintains a brand's reusable email design system — tokens, layout patterns, and brand language.
* **Compliance review**: Audits an assembled email against brand and channel guidelines and deliverability standards.
* **Design review**: Provides subjective design feedback on hierarchy, spacing, narrative flow, and brand fit.
* **Accessibility review**: Runs a WCAG 2.1 AA accessibility audit.
* **Handoff**: Exports and delivers approved HTML to Adobe Journey Optimizer or Adobe Campaign.

### Out of scope skills

The following functionalities are currently not supported:

* **Template switching**: Rebuilding an approved email onto a different template is planned but not yet available.
* **Per-slot content fitting**: A content-fit engine that manages per-slot character limits is planned but not yet available.
* **Figma-comment round-trip**: Using Figma comments as edit intent is planned but not yet available.
* **Template library and auto-match**: A reusable template library with automatic matching is planned but not yet available.
* **Lookalike and net-new template generation**: Generating templates trained from provided HTML samples is planned but not yet available.
* **Automatic accessibility fixes**: The accessibility review is report-only and does not apply fixes automatically.

### Prompting best practices

1. **Start from copy or a reference**: Provide campaign copy, a reference screenshot, or a Figma design link to ground the layout plan and HTML build.
1. **Reference your design system**: Point to your brand's design tokens and layout patterns so composed emails stay consistent.
1. **Request all three reviews**: Ask for compliance, design, and accessibility review before treating an email as send-ready.
1. **Iterate before handoff**: Refine the HTML based on review feedback, then hand off only the approved version to Adobe Journey Optimizer or Adobe Campaign.

{{$include /help/_includes/do-not-localize/start/ai-augmented-content-management-coworker-skills.md}}
