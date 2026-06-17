---
solution: Journey Optimizer
product: journey optimizer
title: AI-powered brand corrections
description: Learn how to configure and use AI-powered brand corrections in Adobe Journey Optimizer.
feature: Brand Guidelines
topic: Content Management
role: User
level: Intermediate
exl-id: a872a3a4-f05b-439d-923e-5191b6e06d34
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: d0a62d3c-b79e-47e4-929e-40ef3cffa037
    internal-label: Communication channels
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
level_v2:
  - id: b6b77c26-2a48-4a62-9ceb-5ae67f4dfde5
    internal-label: Intermediate
topic_v2:
  - id: e0eb8757-182f-49f3-94a4-1587d16f5094
    internal-label: Personalization
---

# AI-powered brand corrections and editorial suggestions {#brand-corrections-ai}

>[!AVAILABILITY]
>
>This capability is available to Adobe Journey Optimizer users with active Brand Guidelines and AI Assistant entitlements. Contact your Adobe representative for access details.

## Overview {#overview}

Adobe Journey Optimizer extends its GenAI-powered brand compliance tooling across all supported content channels — SMS, push notifications, web content, and email. When the Brand QA engine detects content that violates brand guidelines or fails editorial quality criteria, the system automatically generates corrected alternatives that you can review and apply directly within the authoring workflow.

This transforms brand validation from a passive checklist into an active, fix-as-you-go experience. Instead of identifying violations and returning to the editor to resolve each issue manually, content authors receive targeted, AI-generated suggestions that align with the organization's established brand voice, tone, and style guidelines — all without leaving the content editor.

This feature is designed for content marketers, copywriters, and campaign operators who need to move content from draft to activation quickly while maintaining brand compliance at scale.

## Prerequisites {#prerequisites}

Before using AI-powered brand corrections, confirm the following:

- **Brand Guidelines** are configured in Adobe Journey Optimizer. Without an active brand profile, the system cannot generate brand-aligned correction suggestions.
- The **AI Assistant** feature is enabled for your Adobe Experience Cloud organization.
- You have the appropriate permissions to create and edit content for the relevant channel (SMS, push, web, or email).
- At least one content item is available for review in the Journey Optimizer content editor.

>[!NOTE]
>
>Brand correction suggestions are generated using Adobe's generative AI infrastructure and are subject to the AI Assistant usage policies applicable to your organization. Always review accepted suggestions before publishing.

## How it works {#how-it-works}

Brand corrections integrate directly into the Brand QA validation flow within the Journey Optimizer content editor. The end-to-end process works as follows.

**Step 1 — Brand QA scan**: When you run a brand validation check on your content — either manually from the review panel or triggered by a workflow rule — the system evaluates each content block against your configured brand guidelines. Checks cover tone of voice, terminology, prohibited language, editorial standards, and regulatory requirements.

**Step 2 — Violation detection and flagging**: Any content segment that does not meet brand or editorial quality criteria is flagged with a violation indicator. The type of violation — for example, tone mismatch, prohibited term usage, or guideline non-compliance — is displayed alongside the flagged segment so authors understand exactly what needs to change.

**Step 3 — AI suggestion generation**: For each flagged segment, Journey Optimizer automatically generates one or more corrected alternatives using the AI Assistant. Suggestions are grounded in your active brand guidelines, ensuring that recommended text reflects the correct voice, terminology, and editorial style specific to your organization.

**Step 4 — Inline preview and review**: Suggested corrections appear inline, directly adjacent to the flagged content in the Brand QA side panel. You can compare the original text with the AI-generated alternative without navigating away from the editor.

**Step 5 — Accept or dismiss**: Accept a suggestion with a single click to replace the flagged content with the corrected version. Alternatively, dismiss the suggestion and edit the content manually. Accepting a suggestion immediately updates the content block and marks the violation as resolved in the QA panel.

**Step 6 — Re-validation**: After applying corrections, re-run the Brand QA scan to confirm all violations are resolved before publishing or activating the content in a journey or campaign.

## Configure {#configure}

No additional configuration is required beyond the standard prerequisites. The feature activates automatically within the Brand QA panel when a brand profile is associated with your content and the AI Assistant is enabled for your organization.

To start using AI-powered brand corrections:

1. Open the content editor for the relevant channel — SMS, push notification, web, or email.
2. In the editor toolbar, select **Brand Guidelines** and choose the applicable brand profile from the dropdown menu.
3. Draft or open your content, then select **Brand QA** from the review panel to initiate a scan.
4. Review flagged violations in the **Brand QA** side panel. For each flagged item, an AI-generated suggestion appears automatically.
5. Click **Apply** to accept a suggestion, or **Dismiss** to handle the correction manually.
6. Re-run **Brand QA** to verify all violations are resolved, then proceed with your standard approval or activation workflow.

### Supported channels {#supported-channels}

AI-powered brand corrections are available across the following content types in Adobe Journey Optimizer:

| Channel | Supported content elements |
|---|---|
| **Email** | Subject line, preheader, body text, CTA labels |
| **SMS** | Message body |
| **Push notifications** | Title, body text |
| **Web** | Headline, body copy, button labels |

>[!NOTE]
>
>Supported content elements may vary depending on your channel configuration and the brand guidelines defined in your brand profile. Image and visual asset validation is not in scope for AI-generated text corrections.

## Key benefits {#key-benefits}

**Reduced manual editing effort**: Content authors no longer need to cross-reference brand guidelines manually for every flagged issue. AI suggestions surface ready-to-apply alternatives, dramatically reducing the time spent in the correction cycle.

**Consistent brand compliance**: Corrections are grounded in the same brand guidelines used for validation. Accepted suggestions maintain consistency with the approved brand voice and editorial standards across all channels, reducing the risk of inconsistent messaging in multi-channel campaigns.

**Faster content production**: By turning brand QA into a streamlined fix-as-you-go workflow, teams move content through the review cycle more quickly, reducing turnaround time between draft and activation. Campaign operators can resolve an entire set of violations in a single pass without switching between tools.

**Cross-channel coverage**: Whether producing an SMS campaign, a mobile push sequence, or a web in-app message, brand correction suggestions are available consistently across all supported content surfaces — ensuring brand standards are upheld everywhere your brand communicates.

## Related topics {#related-topics}

- [Get started with Brand Guidelines](../content-management/brands.md)
- [Use the AI Assistant for content generation](../content-management/ai-assistant.md)
- [Create an SMS message](../sms/create-sms.md)
- [Create a push notification](../push/create-push.md)
- [Get started with web channel](../web/get-started-web.md)
- [Preview and test your content](../content-management/preview-test.md)
