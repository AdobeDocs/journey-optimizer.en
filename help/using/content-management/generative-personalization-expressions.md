---
solution: Journey Optimizer
product: journey optimizer
title: AI Assistant for Personalization Expressions
description: Learn how to use AI Assistant in Journey Optimizer to generate personalization expressions from natural language — from the Personalization Editor or from the Email Designer toolbar.
feature: Content Assistant
topic: Content Management, Artificial Intelligence
role: User
level: Intermediate
mini-toc-levels: 1
---
# AI assistant for personalization expressions{#generative-personalization-expressions}

>[!IMPORTANT]
>
>Before starting using this capability, read out related [Guardrails and Limitations](gs-generative.md#generative-guardrails).
></br>
>
>You must agree to a [user agreement](https://www.adobe.com/legal/licenses-terms/adobe-dx-gen-ai-user-guidelines.html) before you can use AI Assistant in Journey Optimizer. For more information, contact your Adobe representative.

## Overview {#where-available}

[!UICONTROL AI Assistant] helps you generate new personalization from plain language, explain what existing expressions do, and fix issues in selected code, so that you spend less time on syntax and manual field discovery. You can also iterate on a selection or ask for other changes in conversation. It is available in two ways:

* **[!UICONTROL Personalization Editor]** — wherever the editor is available (subject line, body, and other fields that open it). For where and how to open the editor, see [Add personalization](../personalization/personalization-build-expressions.md#where).
* **Email Designer** — when you select a component, use **[!UICONTROL Add expression]** in the contextual toolbar to open the assistant in a toolbox. See [Generate from the Email Designer](#generate-email-designer).

For broader AI Assistant setup and languages, see [Get started with AI Assistant](gs-generative.md). For personalization concepts, see [Get started with personalization](../personalization/personalize.md). For prompt ideas, see [AI prompt best practices](ai-assistant-prompting-guide.md).

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

1. After you generate an expression, click **[!UICONTROL Show previews for sample profiles]** to see how the expression evaluates with sample data and to view the associated payload as JSON. For this check, the assistant generates a limited set of synthetic sample profiles; they are not saved or stored in your organization.

    If you need custom or additional sample profiles, describe what you need in the discussion with the assistant and include the keyword **preview** in your prompt so it can generate the right preview profiles for your check.

    ![](assets/ai-perso-preview-button.png)

    +++Preview example

    ![](assets/ai-perso-preview.png)

    >[!NOTE]
    >
    >Additional previews are for spot checking. The assistant is tuned to generate roughly one to five profiles, asking for a very large number may cause the request to fail.
    
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

In the Email Designer, you can use [!UICONTROL AI Assistant for personalization expressions] from the contextual toolbar without opening the full [!UICONTROL Personalization Editor] first.

1. In the Email Designer, select the component you want to personalize, and click at the location where you want to insert the expression.

1. In the contextual toolbar, click **[!UICONTROL Add expression]**.

    ![](assets/ai-perso-add-expression.png)

1. A toolbox opens where you can prompt AI Assistant for personalization. Type what you need in plain language, the assistant suggests profile fields and other attributes that match your prompt so you can build the expression faster.

1. The assistant generates the expression.

    ![](assets/ai-perso-add-expression-insert.png)

    You can:

    * Validate the expression output with sample values - use the **[!UICONTROL Preview]** tab.
    * Generate another suggestion from the same prompt - use **[!UICONTROL Regenerate]**.
    * Clear the discussion and start over - use **[!UICONTROL Reset]**.
    * Refine the expression in the full editor - click the ![Edit icon](assets/do-not-localize/Smock_Edit_18_N.svg "Edit") icon to open **[!UICONTROL Personalization Editor]**.

1. When you are satisfied with the result, click **[!UICONTROL Insert]** to add the expression to your content.
