---
solution: Journey Optimizer
product: journey optimizer
title: Check content quality in the Email Designer
description: Learn how to use content checks in the Email Designer to catch HTML and CSS issues before sending your emails in Journey Optimizer.
feature: Email Design
topic: Content Management
role: User
level: Beginner, Intermediate
keywords: email, content check, HTML, CSS, validation, rendering, quality
---

# Check content quality in the Email Designer {#content-check}

[!DNL Journey Optimizer] includes automated technical validation directly in the Email Designer, helping you catch HTML and CSS issues before sending. Results are surfaced as errors, warnings, or informational notices in the authoring panel, with contextual details and one-click fixes where available, so issues can be resolved without leaving the editor.

## Access content check {#access-content-check}

Content checks are always available in the Email Designer. To view them, click the warning triangle icon in the right rail to open the **[!UICONTROL Content check]** pane — all detected issues are listed there.

Checks run against the current saved state of your email. After making edits, save your content to recalculate — a **Stale check** badge appears whenever content has changed since the last calculation.

When no issues are detected, the pane displays **No issues detected.**

## Understand severity levels {#severity}

Checks are surfaced with three severity levels:

| Severity | Description |
|---|---|
| **Error** | A critical issue that will cause delivery or rendering failures. Resolve before sending. |
| **Warning** | A potential issue that may affect rendering in specific email clients. Recommended to review and resolve. |
| **Info** | Informational notice about a condition that does not block sending but may affect the long-term maintainability of your content. |

For each detected issue, select **[!UICONTROL Show details]** to see more context, and **[!UICONTROL Show fix]** to apply a one-click fix where available. After a fix is applied, the panel confirms with **Fix applied successfully.** If the fix cannot be applied automatically, **Fix could not be applied** is displayed.

## Content checks reference {#reference}

### Unsupported HTML elements {#html-elements}

| Check | Severity | What it means |
|---|---|---|
| **Script tag** | Error | Your content contains a `<script>` tag, which is not supported in any email system. Remove it to avoid delivery and rendering issues. |
| **Base tag** | Error | Your content contains a `<base>` tag, which can cause link and resource resolution issues in the Email Designer. Remove it. |
| **Meta tag with refresh** | Warning | Your content contains an HTML meta tag with refresh, which is not supported in the Email Designer. Remove it to prevent unexpected behavior. |
| **Empty divs** | Warning | Your content contains empty divs, which can cause layout issues in Microsoft Outlook. Remove the empty divs and use the spacing of sibling elements instead. |

### CSS issues {#css}

| Check | Severity | What it means |
|---|---|---|
| **CSS size exceeds Gmail limit** | Error | Total CSS size exceeds Gmail's 16 KB limit. This will cause rendering issues in Gmail. Reduce CSS or use the **[!UICONTROL Apply fix]** action to remove unused CSS rules. |
| **CSS size approaching Gmail limit** | Warning | Total CSS size is close to Gmail's 16 KB limit and could cause rendering issues if more CSS is added. |
| **Fragment CSS size** | Warning | Total CSS size for this fragment exceeds 3 KB. Combining it with other fragments could push the total email CSS over Gmail's 16 KB limit. |
| **Unused CSS rules** | Warning | Content contains unused CSS rules that could cause rendering issues in Gmail. Use **[!UICONTROL Apply fix]** to remove CSS rules referencing elements that are no longer present in the email. |
| **System-generated CSS modified** | Info | Your content has modifications to the system-generated default CSS. These changes may be overridden by future Email Designer updates. To preserve your styles, add them using the [Custom CSS](custom-css.md) feature instead. |

### HTML size {#html-size}

| Check | Severity | What it means |
|---|---|---|
| **HTML size exceeds Gmail limit** | Error | Estimated HTML size exceeds Gmail's 100 KB limit and will cause rendering issues in Gmail. |
| **HTML size approaching Gmail limit** | Warning | Estimated HTML size is close to Gmail's 100 KB limit and could cause rendering issues if more HTML is added. |
| **Fragment HTML size** | Warning | Estimated HTML size for this fragment exceeds 20 KB. Combined with other fragments, it could push the total email HTML over Gmail's 100 KB limit. |

## About HTML and CSS size estimation {#size-estimation}

HTML and CSS size values shown in the content check panel are **estimates computed at authoring time**. They reflect the full rendered payload as it exists in the editor at that moment, and include:

* All markup, tags, layout wrappers, and inline styles
* Inlined CSS (Email Designer inlines styles before calculating size, which inflates the figure compared to an external stylesheet)
* All text content and personalization tokens, counted at their placeholder length — not their resolved value
* All referenced fragments, expanded inline with their full HTML and CSS weight
* **All branches of conditional if-else blocks**, because conditions are not evaluated until send time

The actual size delivered to recipients is often smaller:

* Only the branch matching each recipient's profile is rendered at send time. A template measuring 120 KB in the editor may produce a 60 KB email for most recipients.
* Resolved personalization values are typically shorter than the placeholder tokens.
* Email HTML minification, when enabled, strips whitespace, comments, and redundant characters at send time.

>[!NOTE]
>
>Size warnings are proactive signals designed to help you optimize content before sending — they are not hard blocks. The 90% threshold warning gives you early notice to reduce content before reaching the client limit.
