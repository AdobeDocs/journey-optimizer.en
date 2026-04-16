---
title: Optimize email text for AI inboxes
description: Refine the plain text layer of email in Journey Optimizer so AI-assisted inbox clients can use your offers and CTAs when they summarize mail or extract intent—in the Email Designer with Optimize with AI.
feature: Email Design
topic: Content Management, Artificial Intelligence
role: User
level: Beginner, Intermediate
exl-id: 0c2f95ce-28a0-480c-9829-b7e4975b6340
hide: true
---
# Optimize email text for AI inboxes {#email-text-optimizer}

[!DNL Adobe Journey Optimizer] comes with an email-channel capability that helps you structure a specific version of your messages for improved AI-assisted inbox experiences—such as [!DNL Apple Intelligence] and [!DNL Google Gemini] in [!DNL Gmail]—so they can answer questions and summarize mail based on your content more accurately, with better results.

You can use this capability to refine a dedicated text version of your messages so AI-assisted inbox experiences are more likely to surface the offers, calls to action, and details you intend—rather than thin auto-generated text or unrelated context.

## How it works {#how-it-works}

Typical questions recipients may ask in AI-assisted inbox experiences are *What is this email about?* or *What are these offers?*.

* The answers provided by these AI assistants may be a short summary (for example that the message is promotional, mentions VIP early access and a sale, and includes links to product categories) but still omit objectives the marketer cared about because the assistants are inferring from whatever text they effectively see—not necessarily the full story you intended.

* Also, the assistants may proactively search for discounts or coupons related to the brand and fold those into the answer, so the user is no longer looking at only what your message actually promised. That behavior is useful to end users, but dilutes control for marketers who need answers to track the real terms in the send.

To prevent these issues, [!DNL Journey Optimizer] creates an additional text version of your messages so that coupons, discount ranges, call to actions, and other priorities appear up front in clear linear copy.

>[!NOTE]
>
>This dedicated text version is not the same as the default or custom plain text version of your messages. [Learn more](text-version-email.md)

The goal is for inbox AI to ground summaries and Q&A in your defined offers and actions—instead of leaning on a thin default text part or on unrelated web results.

>[!IMPORTANT]
>
>Exact AI-assistant behaviors depend on the inbox provider and model version. After your email is delivered, answers and summaries provided by external AI clients can be wrong, incomplete, or mixed with web results.
>
>The Optimize email text for AI inboxes capability only generates a dedicated text version in Journey Optimizer; it does not guarantee how a third-party assistant will interpret or display the message. Read more about the [limitations and risks of third-party inbox AI](#inbox-ai-risks).

## Recommended use cases {#use-cases}

<!--
* **Critical details only in images** — Offers, promo codes, or deadlines shown in banners or graphics are invisible in plain text. Use the optimizer (and manual edits) so the same facts appear as text, improving extraction by AI summaries and text-only clients.
-->

* **Dense or fragmented auto-generated text** — When default plain text is hard to scan, optimization can produce a clearer linear narrative with explicit offers and links.

* **Controlling inbox Q&A** — When you expect recipients to ask assistants *what the email is about* or *what the offers are*, a strong ai-inbox version reduces partial summaries and avoids reliance on web-supplemented answers that are not tied to your approved copy.

## Optimize for AI inbox experiences {#optimize-with-ai}

>[!IMPORTANT]
>
>Before you use this capability, read the related [Risks and limitations](#inbox-ai-risks).
>
>To access this feature, you must agree to a user agreement which displays the first time you use Generative AI in [!DNL Journey Optimizer]. For more information, read the [Adobe Experience Cloud Generative AI User Guidelines](https://www.adobe.com/legal/licenses-terms/adobe-gen-ai-user-guidelines.html){target="_blank"}.

To optimize the plain text version of your email for AI inboxes with [!DNL Journey Optimizer], follow the steps below.

1. Open your email in the [Email Designer](content-from-scratch.md) (from a campaign, journey, or template, depending on your workflow).

1. Click the **[!UICONTROL Optimize for AI Inbox]** button to generate an improved version that highlights key information for AI-assisted reading and summarization.

    ![Optimize for AI Inbox button in the Email Designer](assets/optimize-for-ai-button.png){zoomable="yes" width="80%"}

1. If this is the first time you are using Generative AI in [!DNL Journey Optimizer], you will be asked to agree to the user agreement. To learn more, check out the [Adobe Generative AI User Guidelines](https://www.adobe.com/legal/licenses-terms/adobe-gen-ai-user-guidelines.html){target="_blank"}.

    ![Generative AI user agreement dialog in Journey Optimizer](assets/optimize-ai-inbox-agreement.png){width=50%}

    Click **[!UICONTROL Agree]** to continue.

1. The generated version is displayed.

    ![Generated version optimized for AI inboxes](assets/optimize-ai-inbox-output.png){zoomable="yes" width="80%"}

    >[!NOTE]
    >
    >**Optimize email text for AI inboxes** does not change your HTML design, layout, or images.

1. To make changes to the content automatically generated, select the **[!UICONTROL Enable edit]** toggle and manually edit the content as needed.

1. Once happy with your version, click **[!UICONTROL Optimize Email]** button to confirm.

1. Your email is now successfully optimized for AI inboxes. 

1. To access or edit the optimized version, click the **[!UICONTROL Optimized for AI Inbox]** button.

    ![Re-optimize button in the Email Designer](assets/optimize-ai-inbox-optimized-button.png){zoomable="yes" width="80%"}

1. The optimized version is displayed. You can **[!UICONTROL Remove optimization]** or click **[!UICONTROL Re-optimize]** to generate a new version.

    ![Previously optimized version in the Email Designer](assets/optimize-ai-inbox-optimized-version.png){zoomable="yes" width="80%"}

    >[!NOTE]
    >
    >If you make changes to the original HTML content, you need to re-optimize the version for AI inboxes.

## Risks and limitations of third-party inbox AI {#inbox-ai-risks}

The Optimize email for AI inboxes capability helps you prepare a version of your email for how mailbox providers may process your [!DNL Journey Optimizer] sends. It does not control those providers' products. Once a message is delivered, any AI features in [!DNL Gmail], [!DNL Apple] Mail, [!DNL Outlook], or other clients operate under their terms, models, and policies—not Adobe's.

* **Unpredictable presentation** — Summaries, notification blurbs, and conversational answers can omit offers, misstate prices or dates, merge content with unrelated web results, or paraphrase in ways that no longer match your approved copy. Behavior changes when vendors update models or UI without notice.

* **No guarantee of parity with HTML** — Recipients who rely on previews or assistant answers may never see your full HTML design, images, or legal footers. What they believe the message "says" may come only from a short AI-generated digest.

* **Privacy, compliance, and data use** — Inbox AI may process message content on provider infrastructure subject to that provider's privacy policy, retention, and regional rules. Organizations in regulated industries should assess whether recipient use of such features affects their obligations, independent of how the email was authored in [!DNL Journey Optimizer].

* **Brand and legal exposure** — Incorrect or incomplete AI summaries can still create customer confusion or disputes about promotions, terms, or opt-out language. **Optimize email for AI inboxes** does not ensure that a third party's model will reproduce the optimized version of your email faithfully.

* **[!UICONTROL Optimize for AI Inbox]** in [!DNL Journey Optimizer] — The authoring-time control in the Email Designer is separate from end-user inbox assistants. Always review generated plain text before send.

## Related topics {#related-topics}

* [Get started with email design](get-started-email-design.md)
* For Adobe generative features more broadly, see [Get started with AI Assistant to create content](../content-management/gs-generative.md).
