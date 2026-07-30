---
solution: Journey Optimizer
product: journey optimizer
title: Personalize content in Journey Optimizer
description: Get Started with personalization.
feature: Personalization
topic: Personalization
role: Developer
level: Beginner
keywords: expression, editor, start, personalization
exl-id: f448780b-91bc-455e-bf10-9a9aee0a0b24
feature_v2:
  - id: fda7be7c-b81e-42c0-95a9-616e5b893c03
    internal-label: Build expressions
subfeature_v2:
  - id: a757b957-83f3-4a4d-9775-a93854f84f77
    internal-label: Conditional instruction
  - id: cb09dcb7-3367-4b63-b02c-8a1356eb876e
    internal-label: Main functions
---
# Get started with personalization{#add-personalization}

>[!BEGINSHADEBOX]

**On this page:** Get started with personalization in Adobe Journey Optimizer, including how the personalization editor works, the profile data you can use, the learning playground, and inline editing.

>[!ENDSHADEBOX]

>[!CONTEXTUALHELP]
>id="ajo_homepage_card5"
>title="Personalize experiences"
>abstract="Use **Adobe Journey Optimizer** to adapt your messages to each specific recipient by leveraging the data and information you have about them. It can be their first name, interests, where they live, what they bought, and more."

[!DNL Adobe Journey Optimizer] personalization capabilities allow you to adapt your messages to each specific recipient by leveraging the data and information you have about them. It can be their first name, interests, where they live, what they bought, and more.  

## How personalization works

Using the **personalization editor**, you can select, arrange, customize and validate all the data to create a customized personalization for your content, and leverage various tools such as helper functions or predefined expressions to tailor messages effectively.

Journey Optimizer employs an inline personalization syntax based on Handlebars which allows you to create expressions with contents enclosed by double curly braces **`{{}}`**.

When processing the message, Journey Optimizer replaces the expression with the data contained in the Experience Platform dataset. For example, `Hello {{profile.person.name.firstName}} {{profile.person.name.lastName}}` dynamically becomes `Hello John Doe`. Using this syntax, you can personalize messages across multiple fields, including email subject lines, message bodies, push notifications, or URLs.

## Data used for personalization

Personalization is based on the profile data that are managed by the **XDM Individual Profile** schema defined in Adobe Experience Platform. The **XDM Individual Profile** schema is the only schema you can use to personalize content in [!DNL Journey Optimizer]. Learn more in [Adobe Experience Platform Data Model (XDM) documentation](https://experienceleague.adobe.com/docs/experience-platform/xdm/home.html){target="_blank"}.

You can also leverage **computed attributes** to personalize your content. Computed attributes allow you to summarize individual behavioral events into computed profile attributes available on Adobe Experience Platform. [Learn how to work with computed attributes](../audience/computed-attributes.md)

In addition, [!DNL Journey Optimizer] allows you to leverage data from Adobe Experience Platform in the personalization editor to personalize your content. To do this, datasets needed for lookup personalization must first be enabled through an API call. Once done, you can use their data to personalize your content into Journey Optimizer. This feature is currently available in beta. [Learn more](../personalization/aep-data-perso.md)

## Learn and experiment with personalization {#playground}

**[!DNL Adobe Journey Optimizer]** includes an interactive tool designed to help you learn and experiment with personalization capabilities.

This playground provides a simulated environment to write and test personalization code using sample data without requiring live datasets. You can leverage predefined code samples, edit dummy profile payloads, and preview the output of your personalization code in real-time. 

![personalization playground](assets/playground.png)

➡️ [Access the personalization playground](https://experienceleague.adobe.com/en/apps/journey-optimizer/ajo-personalization){target="_blank"}

## Generate content for personalization expressions {#ai-personalization-expressions}

In the **[!UICONTROL Personalization Editor]** or from the Email Designer toolbar (**[!UICONTROL Add expression]**), **[!UICONTROL Generate Content]** helps you generate new expressions from natural language, explain what existing code does, and fix issues in a selection, then apply the output when it matches your intent.

![](../content-management/assets/ai-perso-generate.png)

➡️ [Learn how to work with Generate content for personalization expressions](../content-management/generative-personalization-expressions.md)

## Inline editing of profile attributes {#inline-personalization}

You can insert profile attribute expressions directly while editing content in the **Email Designer** or the **Push channel** editor, without opening the full personalization editor.

To do so, follow these steps:

1. Type `{{` in any text field. An inline autocomplete dropdown opens at the cursor position.
1. Start typing to filter available profile attributes.
1. Select the attribute you need — it is inserted as a personalization token at the cursor position.

![](assets/inline-profile-attributes.png)

## Let's dive deeper

Now that you have an understanding of personalization in **[!DNL Journey Optimizer]**, it's time to dive deeper into these documentation sections to start working with the feature.

<table style="table-layout:fixed"><tr style="border: 0;">
<td>
<a href="personalization-build-expressions.md">
<img alt="add personalization" src="assets/do-not-localize/add.png">
</a>
<div>
<a href="personalization-build-expressions.md"><strong>Add personalization</strong></a>
</div>
<p>
</td>
<td>
<a href="../personalization/personalization-syntax.md">
<img alt="Lead" src="assets/do-not-localize/syntax.png">
</a>
<div><a href="../personalization/personalization-syntax.md"><strong>Personalization syntax</strong>
</div>
<p>
</td>
<td>
<a href="../personalization/functions/functions.md">
<img alt="Infrequent" src="assets/do-not-localize/functions.png">
</a>
<div>
<a href="../personalization/functions/functions.md"><strong>Helper functions list</strong></a>
</div>
<p></td>
<td>
<a href="../personalization/personalization-recipes.md">
<img alt="Infrequent" src="assets/do-not-localize/uc.png">
</a>
<div>
<a href="../personalization/personalization-recipes.md"><strong>Personalization recipes</strong></a>
</div>
<p></td>
<td>
<a href="../personalization/personalization-use-case.md">
<img alt="Infrequent" src="assets/do-not-localize/uc.png">
</a>
<div>
<a href="../personalization/personalization-use-case.md"><strong>Personalization use cases</strong></a>
</div>
<p></td>
</tr></table>

## How-to videos{#video-perso}

Learn how to use contextual event information from a journey to personalize a message.

>[!VIDEO](https://video.tv.adobe.com/v/334165?quality=12)

Learn how to add profile-based personalization to a message and how to use audience membership as a pre-condition to a personalization block.

>[!VIDEO](https://video.tv.adobe.com/v/334078?quality=12)

Learn how to leverage the personalization editor playground to write and test personalization code using sample data.

>[!VIDEO](https://video.tv.adobe.com/v/3457868?quality=12)

Explore more video tutorials on personalization features and best practices in [Personalization tutorials](https://experienceleague.adobe.com/en/docs/journey-optimizer-learn/tutorials/personalize-content/personalization-editor-overview){target="_blank"}

## Quick reference {#quick-reference}

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

>[!BEGINTABS]

>[!TAB Overview]

**TL;DR**

This page introduces personalization in Journey Optimizer — how the Handlebars-based personalization editor works, what data it uses, the interactive playground, Generate Content for expressions, and inline attribute editing in the Email Designer and Push editor.

**Intents**

* Understand how Journey Optimizer personalization works (Handlebars syntax with double curly braces)
* Identify the data sources available for personalization (XDM Individual Profile schema, computed attributes, AEP dataset lookup in beta)
* Experiment with personalization using the interactive playground without a live sandbox
* Use AI to generate, explain, or fix personalization expressions from natural language
* Insert profile attributes inline in the Email Designer or Push editor by typing `{{`

>[!TAB Glossary]

* **Personalization editor**: The full-featured tool for building, customizing, and validating personalization expressions; available in any Journey Optimizer field that supports personalization. *(product-specific)*
* **XDM Individual Profile schema**: The only schema that can be used to personalize content in Journey Optimizer; defines all profile attributes available for personalization. *(product-specific)*
* **Computed attributes**: Pre-calculated profile attributes summarizing individual behavioral events into profile-level values; available as personalization data alongside standard XDM profile fields. *(product-specific)*
* **Personalization playground**: An interactive, simulated environment on Experience League for writing and testing personalization code with sample data — no live datasets or sandbox required. *(product-specific)*
* **Inline editing**: The ability to type `{{` in any text field in the Email Designer or Push channel editor to trigger an autocomplete dropdown and insert profile attributes without opening the full personalization editor. *(product-specific)*
* **Generate Content (personalization expressions)**: An AI tool in the personalization editor and Email Designer that generates personalization expressions from natural language, explains existing code, and fixes issues in a selection. *(product-specific)*

>[!TAB Terminology]

* **Canonical name:** personalization — variants: content personalization, message personalization, expression personalization
* **Canonical name:** personalization editor — variants: personalization capabilities
* **Do not confuse:** Personalization editor (used to build content expressions in messages and offers — supports both Handlebars and PQL) ≠ Advanced expression editor (used in the journey for conditions on data sources and event information, custom wait activities, and action parameters mapping — provides built-in functions and operators that differ from those in the personalization editor)
* **Do not confuse:** inline editing (type `{{` in Email Designer or Push for quick attribute insertion without opening the full editor) ≠ personalization editor (full tool for complex expressions, helper functions, conditional rules, and fragments)
* **Do not confuse:** XDM Individual Profile schema (the only schema usable for personalization in Journey Optimizer) ≠ other AEP schemas (not usable for personalization unless exposed via dataset lookup)

>[!TAB Guardrails & Limitations]

* XDM Individual Profile schema is the only schema that can be used to personalize content in Journey Optimizer.
* AEP dataset lookup for personalization requires datasets to be enabled through an API call before use; this feature is currently in beta.
* Inline editing (typing `{{` in Email Designer or Push editor) supports profile attributes only.

>[!TAB FAQ]

**Q: What data can be used for personalization in Journey Optimizer?**

Profile data from the XDM Individual Profile schema, computed attributes (behavioral events summarized at the profile level), and AEP record dataset lookup (currently beta — requires datasets to be enabled via API).

**Q: What is the personalization playground?**

An interactive, simulated environment on Experience League where you can write and test personalization code using sample data, without requiring a live Journey Optimizer sandbox or real datasets.

**Q: How does inline attribute editing work?**

Type `{{` in any text field in the Email Designer or Push channel editor to open an autocomplete dropdown at the cursor position. Start typing to filter profile attributes, then select one to insert it as a personalization token. Only profile attributes are available inline.

**Q: What can Generate Content do in the personalization editor?**

It can generate new personalization expressions from natural language descriptions, explain what existing code does, and fix issues in a selected expression — then apply the output when it matches your intent.

>[!ENDTABS]

<!-- ai-section-version: 1 | source-hash: 248b894f -->
