---
solution: Journey Optimizer
product: journey optimizer
title: Generate personalization with AI
description: Learn how to generate personalization with AI in the Journey Optimizer Personalization Editor—create, refine, and explain expressions from natural language with AI Assistant.
feature: Content Assistant
topic: Content Management, Artificial Intelligence
role: User
level: Intermediate
mini-toc-levels: 1
---
# Generate personalization with AI {#generative-personalization-expressions}

>[!IMPORTANT]
>
>Before starting using this capability, read out related [Guardrails and Limitations](gs-generative.md#generative-guardrails).
></br>
>
>You must agree to a [user agreement](https://www.adobe.com/legal/licenses-terms/adobe-dx-gen-ai-user-guidelines.html) before you can use AI Assistant in Journey Optimizer. For more information, contact your Adobe representative.

In the [!UICONTROL Personalization Editor], [!UICONTROL AI Assistant] helps you work in natural language: you can draft or adjust personalization expressions, ask for changes to a selection, or get a concise explanation of existing code. The assistant supports multi-turn clarification and shows [!UICONTROL Reasoning] so you can review how a suggestion was built before you insert it, with less friction around syntax and schema discovery.

For more information on personalization in [!DNL Journey Optimizer], see [Get started with personalization](../personalization/personalize.md).

For org-level AI access and agreements, see [Get started with AI Assistant](gs-generative.md). For prompt ideas, see [AI prompt best practices](ai-assistant-prompting-guide.md).

## Where it is available {#where-available}

You use [!UICONTROL AI Assistant] in the [!UICONTROL Personalization Editor] wherever that editor is available—for example in the subject line, body, and other fields that open it. It applies to authoring flows where Journey Optimizer uses the editor, such as **campaigns**, **API-triggered campaigns**, and **journeys**, across **native channels** that support the editor.

Depending on your release, language support may start with **English** only; additional languages may follow.

## Open the assistant {#access-configure}

1. In your message or content, use **[!UICONTROL Add personalization]** (or equivalent) to open the **[!UICONTROL Personalization Editor]**.

1. Open **[!UICONTROL AI Assistant]** from the editor to use the assistant in context with your expression work.

1. Optional: Switch between the assistant and **raw code** view when you need to edit the script directly. Returning to the assistant typically keeps your working context until you close the editor, depending on your session.

    ![Personalization editor with AI Assistant available for expressions](assets/perso-expressions-genai-1.png){zoomable="yes"}

## Describe what you need {#generate-content}

1. In the **[!UICONTROL Prompt]** field, describe the personalization you want in plain language—for example which profile attributes, segments, or logic you need.

1. Use **multi-turn** conversation when the assistant asks clarifying questions (for example to disambiguate fields or confirm test values).

1. Review **[!UICONTROL Reasoning]** to see how the assistant built the logic and which variables or functions it used. Attributes you cannot access (per field-level access controls) are not exposed in reasoning or in the suggested code, consistent with the editor.

1. If several schema fields match your request, pick from the suggested options when the assistant lists **variable disambiguation** choices.

1. When the suggestion is ready, use **[!UICONTROL Insert]** or **[!UICONTROL Replace]** (or equivalent) to place code in the editor—**append** or **replace** the current selection depending on what you choose.

1. You can **cancel** an in-progress generation when the UI provides that option.

## Edit or explain existing code {#edit-existing}

1. Select existing personalization code in the editor.

1. Use **[!UICONTROL Edit with AI]** (or equivalent) so the assistant uses your selection as context.

1. Ask the assistant to **refactor**, **simplify**, or **explain** the snippet. Explanations help you validate logic written by you or by the assistant.

## Validate before send {#refine-finalize}

1. Always validate outputs with the editor and **simulation / proofing** flows before production sends. [Learn more about personalization](../personalization/personalize.md).

1. The assistant may suggest code that still requires review for your audience, brand, and compliance rules.

1. For advanced helpers and edge cases, continue to rely on [Personalization syntax](../personalization/personalization-syntax.md) and [Add personalization](../personalization/personalization-build-expressions.md).

>[!NOTE]
>
>Capabilities such as integrations, saved expressions, or offer decisioning may not be in scope for every release. If a request is not supported, the assistant should indicate that limitation.

## See also {#see-also}

* [Get started with AI Assistant](gs-generative.md)
* [Generate text with AI](generative-text.md)
* [Generate images with AI](generative-image.md)
* [Add personalization](../personalization/personalization-build-expressions.md)
