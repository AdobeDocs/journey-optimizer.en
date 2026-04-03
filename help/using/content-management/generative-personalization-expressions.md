---
solution: Journey Optimizer
product: journey optimizer
title: AI Assistant for Personalization Expressions
description: Learn how to use AI Assistant in the Journey Optimizer Personalization Editor to generate new expressions from natural language, explain or fix existing code, and refine selections.
feature: Content Assistant
topic: Content Management, Artificial Intelligence
role: User
level: Intermediate
mini-toc-levels: 1
---
# AI Assistant for Personalization Expressions{#generative-personalization-expressions}

>[!IMPORTANT]
>
>Before starting using this capability, read out related [Guardrails and Limitations](gs-generative.md#generative-guardrails).
></br>
>
>You must agree to a [user agreement](https://www.adobe.com/legal/licenses-terms/adobe-dx-gen-ai-user-guidelines.html) before you can use AI Assistant in Journey Optimizer. For more information, contact your Adobe representative.

## Overview {#where-available}

In the [!UICONTROL Personalization Editor], [!UICONTROL AI Assistant] helps you generate new personalization from plain language, explain what existing expressions do, and fix issues in selected code, so that you spend less time on syntax and manual field discovery. You can also iterate on a selection or ask for other changes in conversation.

* For broader AI Assistant setup and languages, see [Get started with AI Assistant](gs-generative.md).
* For more information on personalization in [!DNL Journey Optimizer], see [Get started with personalization](../personalization/personalize.md).
* For prompt ideas, see [AI prompt best practices](ai-assistant-prompting-guide.md).

You use [!UICONTROL AI Assistant] in the [!UICONTROL Personalization Editor] wherever that editor is available — for example in the subject line, body, and other fields that open it. For where and how to open the editor, see [Add personalization](../personalization/personalization-build-expressions.md#where).

Depending on your campaign or journey context and release, the assistant can work with data and constructs the [!UICONTROL Personalization Editor] already exposes — for example **profile** attributes, **segment** membership, **journey** and **system** context, **helper** functions, and related personalization sources.

## Generate personalization expressions {#generate}

These steps cover generating personalization expressions from scratch. To work with code already in the editor, see [Edit, fix or explain existing code](#edit-existing).

1. In your message or content open the **[!UICONTROL Personalization Editor]** and click the **[!UICONTROL AI Assistant]** button.

    ![](assets/ai-perso-access.png)

1. In the text field, describe the personalization expression you want in plain language — for example which profile attributes, segments, or logic you need, then click **[!UICONTROL Generate]**.

    You can also use ready-to-use prompts from the **[!UICONTROL Quick Prompts]** section. Example: Personalized Greeting, Generate Promo Code.

    ![](assets/ai-perso-generate.png)

1. You can keep discussing with the assistant in a multi-turn conversation: it keeps context from your prompts so you can refine the same expression step by step. To start over, click the **[!UICONTROL New session]**.

    ![](assets/ai-perso-question.png)

1. After you generate an expression, click the **[!UICONTROL Show previews for sample profiles]** button to preview the output by impersonating a sample profile, and to see the associated payload as JSON.

    ![](assets/ai-perso-preview.png)

1. To implement the output in your personalization expression, click **[!UICONTROL Apply]**. You can also copy the output and paste it where you need it using the ![Copy icon](../orchestrated/assets/do-not-localize/activity-copy.svg) icon.

## Edit, fix or explain existing code {#edit-existing}

You can select an existing personalization expression and use AI Assistant to fix personalization issues, explain what the code does, or ask for other changes.

1. Select existing personalization code in the editor.

1. Right-click the selection and choose **[!UICONTROL Edit with AI Assistant]** so the assistant uses your selection as context.

    ![](assets/ai-perso-right-click.png)

1. **[!UICONTROL AI Assistant]** opens. In **[!UICONTROL Quick Commands]**, click **[!UICONTROL Explain]** or **[!UICONTROL Fix]**, or use the text field to ask for other changes and start a conversation.

    ![](assets/ai-perso-edit.png)

1. When you use **[!UICONTROL Fix]**, click **[!UICONTROL Show fix details]** in the discussion to show an explanation of the fix and a line-by-line before and after preview.

    ![](assets/ai-perso-fix.png)

1. As when you generate a personalization expression, click **[!UICONTROL Apply]** to implement the assistant output in your expression. For example, if you asked for an explanation of the code, applying can add comments in the expression that describe what it does.
