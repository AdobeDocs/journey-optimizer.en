---
solution: Journey Optimizer
product: journey optimizer
title: AI-powered brand corrections
description: Learn how to configure and use AI-powered brand corrections in Adobe Journey Optimizer.
feature: Brand Validation
topic: Content Management
role: User
level: Intermediate
exl-id: dd4fde0e-86c8-4a57-86ba-202e3be2c41f
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: d0a62d3c-b79e-47e4-929e-40ef3cffa037
    internal-label: Communication channels
subfeature_v2:
  - id: c96d2aa5-76a2-443d-8d23-5de95577c909
    internal-label: Mobile SDK
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
level_v2:
  - id: b6b77c26-2a48-4a62-9ceb-5ae67f4dfde5
    internal-label: Intermediate
topic_v2:
  - id: e0eb8757-182f-49f3-94a4-1587d16f5094
    internal-label: Personalization
  - id: cdd65e7e-8839-44a2-bc21-0e03623b5dd1
    internal-label: Optimization
---

# AI-powered brand corrections {#brand-corrections}

>[!AVAILABILITY]
>
>This capability is available for Adobe Journey Optimizer and applies to Push, SMS, and Web content channels.

## Overview {#overview}

When content is flagged during Brand QA, Adobe Journey Optimizer can automatically generate corrected or improved text alternatives using generative AI. Instead of manually rewriting flagged copy, you receive inline suggestions that align with your brand guidelines — which you can review, preview, and apply with a single click.

This turns the Brand QA step from a blocking review gate into a **fix-as-you-go experience**, reducing time spent on manual corrections and accelerating content production across channels.

This feature is designed for content marketers, copywriters, and campaign operators who need to maintain brand compliance across high-volume, multi-channel campaigns without slowing down production workflows.

## How it works {#how-it-works}

Brand QA in Adobe Journey Optimizer evaluates your content against your organization's brand guidelines — including tone of voice, terminology, messaging standards, and editorial rules. When a violation or quality issue is detected, the system flags the affected content element and, where supported, automatically generates a recommended replacement using the Adobe generative AI engine.

The end-to-end flow is as follows:

1. **Brand QA scan** — When you run a brand check on your content (Push notification body, SMS message text, or Web content block), the system evaluates each element against active brand rules.
2. **Violation detection** — Elements that fail one or more brand criteria are flagged with a severity indicator (for example, critical, warning, or suggestion).
3. **AI suggestion generation** — For each flagged element, the system automatically generates one or more corrected text alternatives. Suggestions are produced by the Adobe generative AI engine, which is aware of both the violation reason and your brand's guidelines context.
4. **Inline preview** — The suggested replacement text appears inline, directly alongside the flagged original. You can compare the original and suggested versions side by side before making any change.
5. **One-click apply** — If the suggestion meets your needs, select **Apply** to replace the flagged text with the AI-generated version. The content editor updates immediately and the brand flag is cleared.
6. **Manual override** — You are never locked into the AI suggestion. You can edit the suggestion before applying it, dismiss it and write your own correction, or ignore the flag entirely if the context warrants an exception.

>[!NOTE]
>
>AI-generated suggestions are recommendations only. Your team retains full editorial control. Always review suggestions in the context of your campaign before applying them.

## Prerequisites {#prerequisites}

Before using AI-powered brand corrections, ensure the following conditions are met:

- **Brand guidelines configured** — Your organization must have at least one active brand profile set up in Adobe Journey Optimizer. Brand profiles define the rules against which content is evaluated. Contact your Adobe administrator or brand manager to verify that brand profiles are published and associated with your sandboxes.
- **Content AI features enabled** — AI-powered content assistance must be enabled for your organization and sandbox. This is managed at the product profile level in Adobe Admin Console. If AI suggestions do not appear after a brand scan, confirm with your administrator that the AI content generation entitlement is active.
- **Supported content type** — Brand corrections with AI suggestions are supported for the following content types: Push notification title and body, SMS message text, and Web content blocks edited through the Journey Optimizer Web Designer. Rich media assets (images, video) are evaluated for brand compliance separately and are not in scope for text-level AI corrections.
- **Editing permissions** — You must have edit access to the journey, campaign, or content template in which the flagged content resides.

## Configure {#configure}

No additional configuration is required to enable AI-powered brand corrections if your organization already uses Brand QA. The AI suggestion layer activates automatically when brand violations are detected in supported content types.

To run a brand check and access AI suggestions:

1. Open your campaign or journey in Adobe Journey Optimizer.
2. Navigate to the content step for the relevant channel (Push, SMS, or Web).
3. Select **Check brand alignment** (or open the **Brand QA** panel from the content editor toolbar).
4. Wait for the scan to complete. Flagged elements are highlighted in the canvas and listed in the **Brand issues** panel on the right.
5. For each flagged item, expand the issue row to view the violation reason and the AI-generated suggestion.
6. Use **Preview** to see the suggested text rendered in the content canvas.
7. Select **Apply suggestion** to replace the flagged text, or select **Edit** to modify the suggestion before applying.
8. After all issues are resolved or acknowledged, re-run the brand check to confirm compliance.

>[!NOTE]
>
>Applying a suggestion updates the live content in the editor but does not automatically publish or activate the campaign. You must complete the remaining campaign configuration and activation steps as normal.

### Working with multiple suggestions {#multiple-suggestions}

For some violations, the AI engine may generate more than one alternative. In those cases, the **Brand issues** panel displays a numbered list of options. Use the forward and back arrows to cycle through alternatives before selecting the one that best fits your intent. Each alternative is generated with a different stylistic approach — for example, one may prioritize conciseness while another emphasizes tone alignment.

### Bulk corrections {#bulk-corrections}

If multiple elements in the same content piece are flagged, you can apply suggestions individually or use the **Apply all suggestions** action at the top of the **Brand issues** panel to accept all AI-generated replacements in a single step. Review the list carefully before using bulk apply, as this action replaces all flagged text simultaneously.

>[!NOTE]
>
>Bulk apply is available only when all flagged items have an associated AI suggestion. Items with no suggestion available (for example, image compliance flags) are skipped and remain flagged for manual review.

## Related topics {#related-topics}

- [Brand guidelines overview](../content-management/brands.md)
- [Run a brand check on your content](../content-management/brand-score.md)
- [AI Assistant for content generation](../content-management/gs-generative.md)
- [Create a push notification](create-push.md)
- [Create an SMS message](../sms/create-sms.md)
- [Edit web content with Journey Optimizer](../web/edit-web-content.md)
