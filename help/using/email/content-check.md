---
solution: Journey Optimizer
product: journey optimizer
title: Content checks in the Email Designer
description: Learn how to use content checks in the Email Designer to catch HTML and CSS issues before sending your emails in Journey Optimizer.
feature: Email Design
topic: Content Management
role: User
level: Beginner, Intermediate
keywords: email, content check, HTML, CSS, validation, rendering, quality
---

# Content check in the Email Designer {#content-check}

>[!CONTEXTUALHELP]
>id="ajo_email_content_check"
>title="Validate your email content"
>abstract="Content checks automatically detect HTML and CSS issues in your email before you send. They flag unsupported tags, empty divs, and size limits that can break rendering in Gmail or Microsoft Outlook. Issues are surfaced as errors, warnings, or informational notices, with contextual details and one-click fixes where available."

[!DNL Journey Optimizer] includes automated technical validation directly in the Email Designer, helping you catch HTML and CSS issues before sending.

Results are surfaced as errors, warnings, or informational notices in the authoring panel, with contextual details and one-click fixes where available, so issues can be resolved without leaving the Email Designer.

## Access content checks {#access-content-checks}

Content checks are always available in the Email Designer. To view them, click the Issues icon in the right rail to open the **[!UICONTROL Content check]** pane — all detected issues are listed there.

![Content check pane in the Email Designer with issues](assets/content-check.png)

>[!NOTE]
>
>Checks are automatically run against the current state of your email and after each edit. [Learn more](#recalculation)

Checks are surfaced with three severity levels:

| Severity | Color | Description |
|---|---|---|
| **Error** | Red | A critical issue that will cause delivery or rendering failures. Resolve before sending. |
| **Warning** | Orange | A potential issue that may affect rendering in specific email clients. Recommended to review and resolve. |
| **Info** | Blue | Informational notice about a condition that does not block sending but may affect the long-term maintainability of your content. |

When no issues are detected, the pane displays **No issues detected** and the corresponding icon is green.

![Content check pane in the Email Designer with no issues](assets/content-check-no-issues.png)

Depending on the issue, you can view more context, apply a one-click fix, or save your email to refresh a check result.

* For some detected issue, you can click the **[!UICONTROL Show details]** button to see more context. Click **[!UICONTROL Hide details]** to collapse.
    ![Content check pane in the Email Designer with details](assets/content-check-details.png){width="80%"}
* Similary, you can click the **[!UICONTROL Show fix]** button and apply a one-click fix where available. If the fix cannot be applied automatically, a messsage is displayed and you must manually solve the issue.
    ![Content check pane in the Email Designer with Apply fix button](assets/content-check-fix.png){width="80%"}

### Recalculation of checks {#recalculation}

Most checks — such as unsupported HTML elements, empty divs, and HTML size — are recalculated each time you edit your email, so they always reflect your current content.

Other checks, such as CSS size, are calculated from the serialized content — the version of your email as it is loaded or saved — not from the live editing state in the Email Designer. In this case, the saved content can differ slightly from what you see while editing. If you make edits without saving, a **[!UICONTROL Stale check]** label appears to indicate the result may no longer be accurate. Save your email to refresh the calculation.

![Content check pane in the Email Designer with Stale check label](assets/content-check-stale.png){width="100%"}

## Fix detected issues {#fix-issues}

The tables below list all possible messages and the recommended action for each. Expand the category matching the message you see in the **[!UICONTROL Content check]** pane.

+++ Unsupported HTML elements

| Message | Severity | What to do |
|---|---|---|
| Your content contains a `<script>` tag, which is not supported in any email system. Remove it to avoid delivery and rendering issues. | Error | Locate and remove all `<script>` tags from your HTML content. |
| Your content contains a `<base>` tag, which can cause link and resource resolution issues in the Email Designer. To fix, you need to remove it. | Error | Remove the `<base>` tag from your HTML. |
| Your content contains an HTML meta tag with refresh, which is not supported in the Email Designer. Remove it to prevent unexpected behavior. | Warning | Remove the meta refresh tag from your HTML. |
| Your content contains empty divs, which can cause layout issues in Microsoft Outlook (MSO). To fix this, remove the empty divs and use the spacing of sibling elements instead. | Warning | Delete the empty `<div>` elements and adjust padding or margin on surrounding elements to maintain spacing. |

+++

+++ CSS issues

| Message | Severity | What to do |
|---|---|---|
| Total CSS size exceeds Gmail's 16 KB limit and will cause rendering issues in Gmail. | Error | Use **[!UICONTROL Apply fix]** to remove unused CSS rules automatically, or manually simplify your styles. |
| Total CSS size is close to Gmail's 16 KB limit and could cause rendering issues if more CSS is added. | Warning | Use **[!UICONTROL Apply fix]** to remove unused CSS rules, or reduce styles before adding more content. |
| Total CSS size for this fragment exceeds 3 KB. Combining this with other fragments could cause the total email CSS to exceed Gmail's 16 KB limit and cause rendering issues. | Warning | Simplify the CSS in this fragment to keep the combined email CSS under 16 KB. |
| Content contains unused CSS rules. This could cause rendering issues in Gmail. | Warning | Use **[!UICONTROL Apply fix]** to automatically remove CSS rules that reference elements no longer present in the email. |

<!--
| Message | Severity | What to do |
|---|---|---|
| Your content has modifications to the system-generated default CSS. These changes may be overridden by future Email Designer updates. To preserve your styles, add them using the Custom CSS feature instead. | Info | Move your custom styles to [Custom CSS](custom-css.md) to ensure they are preserved across Email Designer updates. |
-->

+++

+++ HTML size

| Message | Severity | What to do |
|---|---|---|
| Estimated HTML size exceeds Gmail's 100 KB limit and will cause rendering issues in Gmail. The actual HTML size may differ at send time. | Error | Reduce email content — remove unnecessary elements, simplify structure, or split content across multiple sends. |
| Estimated HTML size is close to Gmail's 100 KB limit and could cause rendering issues if more HTML is added. The actual HTML size may differ at send time. | Warning | Simplify content before adding more. Emails exceeding the Gmail limit will be clipped for recipients. |
| Estimated HTML size for this fragment exceeds 20 KB. Combining this with other fragments could cause the total email HTML to exceed Gmail's 100 KB limit and cause rendering issues. The actual HTML size may differ at send time. | Warning | Reduce the HTML in this fragment to keep the combined email size under Gmail's 100 KB limit. |

+++

## About HTML and CSS size {#size-estimation}

HTML and CSS size values shown in the Email Designer are **estimates computed at authoring time**. They reflect the full rendered payload as it exists in the editor at that moment, and include:

* **HTML structure** – all markup, tags, layout wrappers, and inline styles
* **Inlined CSS** – Email Designer inlines styles before calculating size, which is standard for email clients but inflates the raw figure compared to an external stylesheet
* **Text content** – all copy and personalization tokens, counted at their placeholder length (not their resolved value)
* **Fragments** – all referenced fragments are expanded inline, so each fragment contributes its full HTML/CSS weight to the total
* **Conditional blocks (if-else)** – **all branches** are included in the size estimate at authoring time, because conditions are not evaluated until send time
* **Images** – only the image reference (src URL) is counted, not the binary image data itself

### Why the estimate can differ from the delivered size {#size-estimate-difference}

The size shown is a worst-case upper-bound estimate, not the exact email a recipient will receive. It may differ for the following reasons:

* **Conditional content**: At send time, only the branch matching the recipient's profile is rendered. A template showing 120 KB in the editor might produce a 60 KB email for most recipients.
* **Personalization tokens**: Placeholder tokens are counted at their raw token length. Resolved values are usually shorter.
* **HTML size optimization**: If the **[!UICONTROL Optimize HTML size]** option is enabled, whitespace, comments, and redundant characters are stripped at send time, reducing the final payload. [Learn more](create-email.md#optimize-html-size)

### What size warnings mean for authors {#size-warnings}

Size warnings (for example, HTML exceeding 100 KB) are **proactive signals** to help you optimize your email before sending — they are not hard blocks, and they do not reflect the exact size recipients will see. They exist to help avoid:

* Emails being clipped by Gmail, which clips messages at approximately 102 KB of HTML
* Slow rendering on mobile devices or on low-bandwidth connections
