---
solution: Journey Optimizer
product: journey optimizer
title: AI Assistant for Personalization Expressions
description: Learn how to use AI Assistant in Journey Optimizer to generate personalization expressions from natural language in the Personalization Editor, and how the Add expression control works in the Email Designer.
feature: Content Assistant
topic: Content Management, Artificial Intelligence
role: User
level: Intermediate
mini-toc-levels: 1
feature_v2: []
subfeature_v2:
  - id: d6e0d39b-5df3-4c72-8263-fd834397ee97
    internal-label: AI content generation
  - id: c41e8697-e629-4c38-96b3-564faaa17acf
    internal-label: Dynamic content
---
# AI assistant for personalization expressions{#generative-personalization-expressions}

>[!BEGINSHADEBOX]

**On this page:** Learn how to use AI Assistant in Adobe Journey Optimizer to generate, fix, and explain personalization expressions from natural language in the Personalization Editor and the Email Designer.

>[!ENDSHADEBOX]

>[!IMPORTANT]
>
>Before starting using this capability, read out related [Guardrails and Limitations](gs-generative.md#generative-guardrails).
></br>
>
>You must agree to a [user agreement](https://www.adobe.com/legal/licenses-terms/adobe-dx-gen-ai-user-guidelines.html) before you can use AI Assistant in Journey Optimizer. For more information, contact your Adobe representative.

## Overview {#where-available}

[!UICONTROL AI Assistant] helps you generate new personalization from plain language, explain what existing expressions do, and fix issues in selected code, so that you spend less time on syntax and manual field discovery. You can also iterate on a selection or ask for other changes in conversation. It is available in two ways:

* **[!UICONTROL Personalization Editor]** — wherever the editor is available across channels (subject line, body, and other fields that open it). This is the general path for AI-assisted personalization. For where and how to open the editor, see [Add personalization](../personalization/personalization-build-expressions.md#where).
* **Email Designer toolbar** — when you author emails in the Email Designer, select a component and use **[!UICONTROL Add expression]** in the contextual toolbar to open the assistant in a toolbox without opening the full editor first. This entry point is not available outside email authoring. See [Generate from the Email Designer](#generate-email-designer).

For broader AI Assistant setup and languages, see [Get started with AI Assistant](gs-generative.md). For personalization concepts, see [Get started with personalization](../personalization/personalize.md). To write prompts that produce usable expressions, see [Write effective prompts for personalization expressions](#prompt-best-practices). For content-generation prompt ideas (tone, style, brand), see [AI prompt best practices](ai-assistant-prompting-guide.md).

Depending on your campaign or journey context, the assistant can work with data and constructs the [!UICONTROL Personalization Editor] already exposes — for example profile attributes, segment membership, helper functions, and related personalization sources.

>[!NOTE]
>
>The assistant keeps context from your prompts only while [!UICONTROL AI Assistant] stays open in that session. Closing the assistant or the editor clears the conversation; the next time you open the assistant, you start a new conversation.

## Generate personalization expressions {#generate}

These steps cover generating personalization expressions from scratch. To work with code already in the editor, see [Edit, fix or explain existing code](#edit-existing).

1. In your message or content, open the **[!UICONTROL Personalization Editor]**.

1. Place your cursor in the editor where you want generated personalization code to be inserted, then click the **[!UICONTROL AI Assistant]** button.

    ![](assets/ai-perso-access.png)

1. In the text field, describe the personalization expression you want in plain language — for example which profile attributes, segments, or logic you need, then click **[!UICONTROL Generate]**.

    You can also use ready-to-use prompts from the **[!UICONTROL Quick Prompts]** section, such as personalized greeting, promo code generation, and more.

    ![](assets/ai-perso-generate.png)

    >[!NOTE]
    >
    >Any unrelated prompt or question returns an out-of-scope error. Adjust your prompt and ask a relevant question about the personalization you need.

1. You can keep discussing with the assistant in a multi-turn conversation: it keeps context from your prompts so you can refine the same expression step by step. To start over, click the **[!UICONTROL New session]** button.

    ![](assets/ai-perso-question.png)

1. After you generate an expression, click **[!UICONTROL Show previews for sample profiles]** to see how the expression evaluates against **one** synthetic sample profile and to view the associated payload as JSON. The preview is a **single** spot check so you can gain confidence that your code resolves as expected — it does **not** simulate multiple recipients, varied data, or full coverage. Sample data is not saved or stored in your organization.

    If you need the sample adjusted (for example, different attributes emphasized), describe what you need in the discussion with the assistant and include the keyword **preview** in your prompt.

    ![](assets/ai-perso-preview-button.png)

    +++Preview example

    ![](assets/ai-perso-preview.png)

    >[!NOTE]
    >
    >Do not expect multiple preview rows or exhaustive scenarios here. The control is intentionally limited to **one** sample evaluation for a quick code check, not partial coverage across many profiles. Asking for an unrealistically large set of previews may cause the request to fail.
    
    +++

    >[!NOTE]
    >
    >This control is for a quick check of your personalization code in the editor — not a full message preview of your content. For complete validation of the experience, use your usual simulation flow. [Learn how to preview & test your content](../content-management/preview-test.md)

1. To implement the output in your personalization expression, click **[!UICONTROL Apply]**. The assistant output is inserted at the cursor location in the personalization editor. To replace code that is already there instead, select that code in the editor first, then use **[!UICONTROL Edit with AI Assistant]** (see [Edit, fix or explain existing code](#edit-existing)).

    You can also copy the output and paste it where you need it using the ![Copy icon](../orchestrated/assets/do-not-localize/activity-copy.svg) icon.

## Edit, fix or explain existing code {#edit-existing}

You can select an existing personalization expression and use AI Assistant to fix personalization issues, explain what the code does, or ask for other changes.

1. Select existing personalization code in the editor.

1. Right-click the selection and choose **[!UICONTROL Edit with AI Assistant]** so the assistant uses your selection as context.

    ![](assets/ai-perso-right-click.png)

1. **[!UICONTROL AI Assistant]** opens. In **[!UICONTROL Quick Commands]**, click **[!UICONTROL Explain]** or **[!UICONTROL Fix]**, or use the text field to ask for other changes and start a conversation.

    ![](assets/ai-perso-edit.png)

1. When you use **[!UICONTROL Fix]**, click **[!UICONTROL Show fix details]** in the discussion to show an explanation of the fix and a line-by-line before and after preview.

    ![](assets/ai-perso-fix.png)

1. As when you generate a personalization expression, click **[!UICONTROL Apply]** to implement the assistant output. It replaces the code you had selected in the personalization editor. For example, if you asked for an explanation of the code, applying will add comments in the expression that describe what it does.

## Generate from the Email Designer toolbar {#generate-email-designer}

>[!NOTE]
>
>This section applies only when you edit **email** content in the Email Designer. For other channels, use the **[!UICONTROL Personalization Editor]**.

In the Email Designer, you can use [!UICONTROL AI Assistant for personalization expressions] from the contextual toolbar without opening the full [!UICONTROL Personalization Editor] first.

1. In the Email Designer, select the component you want to personalize, and click at the location where you want to insert the expression.

1. In the contextual toolbar, click **[!UICONTROL Add expression]**.

    ![](assets/ai-perso-add-expression.png)

1. A toolbox opens where you can prompt AI Assistant for personalization. Type what you need in plain language, the assistant suggests profile fields and other attributes that match your prompt so you can build the expression faster.

1. The assistant generates the expression.

    ![](assets/ai-perso-add-expression-insert.png)

    You can:

    * Validate the expression output with one sample value - use the **[!UICONTROL Preview]** tab.
    * Generate another suggestion from the same prompt - use **[!UICONTROL Regenerate]**.
    * Clear the discussion and start over - use **[!UICONTROL Reset]**.
    * Refine the expression in the full editor - click the ![Edit icon](assets/do-not-localize/Smock_Edit_18_N.svg "Edit") icon to open **[!UICONTROL Personalization Editor]**.

1. When you are satisfied with the result, click **[!UICONTROL Insert]** to add the expression to your content.

## Write effective prompts for personalization expressions {#prompt-best-practices}

Prompts for personalization expressions differ from content-generation prompts, which center on tone, style, and brand. Because the assistant builds template logic that resolves against profile and contextual data, your prompt should describe that logic precisely. Start from the customer experience you want to deliver, then express it in terms the assistant can translate into an expression.

An effective prompt generally defines four elements:

* **Data source** — the profile attribute, context data, segment, offer, or other resource to evaluate. Include the exact field path when you know it, such as `profile.person.name.firstName`.
* **Condition** — the logic to apply, for example whether a value exists or matches a specific criterion.
* **Output** — what to display when the condition is met, including any required format.
* **Fallback** — what to display when the data is missing or the condition is not met.

For example, a request to *take the customer's renewal date, add one year, format it as MM/dd/yy, and display nothing when the renewal date is missing* provides a data source, a transformation, an output format, and a fallback — everything the assistant needs to produce a usable expression.

### Recommendations {#prompt-recommendations}

To get the most relevant results:

* Keep each prompt focused on a single personalization rule rather than combining several unrelated rules in one request.
* Reference only fields, fragments, offers, and datasets that exist in your environment. The assistant works with what the editor exposes and does not create data sources for you.
* Describe fallback behavior for optional or potentially missing data, so the expression resolves gracefully for every profile.
* State the expected output structure explicitly when it matters — for example, the keys an offer payload must return as JSON.
* When you edit existing code, provide only the relevant expression as context instead of an entire message, and use **[!UICONTROL Explain]** to understand code before you apply a **[!UICONTROL Fix]** or other change.

## Data and setup requirements {#requirements}

The assistant generates expressions from the resources the [!UICONTROL Personalization Editor] already exposes, so the underlying data must be configured and available. If a prompt does not return a usable expression, confirm that:

* the field you referenced belongs to a schema that is active in your environment,
* any fragment you want to reuse is published,
* any dataset used for a lookup is enabled for lookups, and
* your request relates to template personalization rather than another task.

When the setup is correct, refine the prompt by clarifying the data source, condition, output, and fallback, then generate again.
