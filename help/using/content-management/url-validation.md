---
title: Validate URLs in your content
description: Learn how URL validation checks the web links in your message content before you send.
feature: Preview
role: User
level: Beginner
exl-id: fb1e4880-f874-401e-b1a5-df6956694457
feature_v2:
  - id: dc22c819-3f29-4e91-8b7d-5c6719831141
    internal-label: Content management
subfeature_v2:
  - id: f8d2e9f0-69c9-40cd-890f-71336c8dfff7
    internal-label: Preview
---

# Validate URLs in your content {#url-validation}

>[!BEGINSHADEBOX]

**On this page:** Learn how Adobe Journey Optimizer checks the web links in your message content when you preview it, so you can catch broken, insecure, or unreachable URLs before you send.

>[!ENDSHADEBOX]

When you preview your message content, [!DNL Journey Optimizer] automatically checks the web links it contains. Validation runs after your personalization is resolved, so real URLs are checked rather than unresolved template tokens. This helps you catch broken or inaccessible links before your message reaches your audience.

## Where to find it {#access}

URL validation runs automatically from the **[!UICONTROL Simulate content]** screen. It's available for channel actions in journeys and campaigns, across all channels.

### [!BADGE Limited Availability]{type=Informative} Content templates {#content-templates}

URL validation is also available when you preview [content templates](content-templates.md).

>[!AVAILABILITY]
>
>URL validation for content templates is released in Limited Availability (LA). Contact your Adobe representative to gain access.

## How it works {#how-it-works}

* Every `http://` and `https://` URL in your content is checked — including links, images, and stylesheets, not only clickable text links.
* Each URL is checked to confirm that the host resolves, responds with a success status, and responds within an acceptable time. Only the response status is checked; page content is never downloaded.
* If issues are found, they're identified along with the reason and guidance on how to fix them.

>[!IMPORTANT]
>
>**Limit: max 50 URLs.** If your content contains more than 50 URLs, validation doesn't just skip the extras — the entire request is rejected and no result is returned. Reduce the number of links in your content to get a validation result.

## What gets flagged {#invalid-urls}

| Issue | Example | Why it's flagged | What to do |
|---|---|---|---|
| Insecure scheme | `http://example.com` | HTTP links aren't secure. | Change the link to use `https://`. |
| Malformed URL | Empty URL, bad host, spaces | The URL can't be parsed. | Fix the URL format. |
| Scheme typo | `hhttps://`, `ttps://` | The scheme isn't recognized. | Correct the scheme. |
| Broken or unreachable | A 404 response, or a domain that doesn't resolve | The page doesn't exist or the host can't be reached. | Verify the URL is correct and the host is online. |
| Internal or blocked address | `localhost`, `192.168.x.x`, `169.254.169.254` | Internal or private network addresses are blocked for security reasons. | Don't link to internal addresses in customer-facing content. |
| Timeout | The host took too long to respond | The host didn't respond in time. | The destination service may be slow or temporarily down. Try again later. |

## What doesn't get checked {#not-checked}

The following aren't flagged as broken, even if they appear in your content:

* **Non-web links** — `adbinapp://`, `mailto:`, `tel:`, `sms:`, and `data:` URIs aren't web URLs.
* **Relative links** — `/page` or `./image.jpg` have no host to check.
* **Anchors** — `#section` is a local page reference.
* **Empty links** — An empty `href` isn't a link.

## Caveats {#caveats}

>[!IMPORTANT]
>
>**Personalized links are always flagged as invalid — this is expected, not a bug.** If a link contains a personalization token, that token isn't resolved during validation, so the URL is incomplete and can never be reached. This happens every time, whether or not the underlying link actually works.
>
>For example, these will always show as invalid:
>
>* `https://example.com/profile/{{crmID}}`
>* `https://example.com/offer?promoCode={{promoCode}}`
>
>Before you report or try to fix a flagged link, check whether it contains a personalization token (usually shown as `{{ }}` placeholders). If it does, treat it as an expected false positive and verify the link manually instead — there's no way to resolve the token from the validation result alone.

Beyond personalized links, content is scanned for URLs wherever they appear, not only in clickable links — so a few other categories are also commonly flagged as false positives:

* **Adobe namespace URLs**, such as `xmlns="http://ns.adobe.com/..."` in XML/HTML, are identifiers rather than pages to visit. They return a 404, which is expected.
* **CDN resource URLs** — images, fonts, or stylesheets that aren't meant to be clicked. If the CDN is slow or temporarily unavailable, they may show as invalid.
* **URLs in comments or metadata** that are never shown to your recipients but are still checked.

>[!NOTE]
>
>Before treating a flagged URL as a real issue, check whether it contains a personalization token, is a namespace/CDN/metadata URL, or is an actual user-facing link.

## Best practices {#best-practices}

1. Use `https://` for all links — HTTP links aren't allowed.
1. Confirm external dependencies — CDN URLs, third-party APIs, and remote images — are healthy before you preview.
1. Expect any link containing a personalization token to always show as invalid — this is expected. Verify these links manually instead of relying on the validation result.
1. Stay under the 50-URL limit — going over it doesn't trim the extras, it rejects the whole validation request. Consider splitting your content across multiple messages or templates.
1. Expect namespace or data URIs in your schema to show as invalid — that's expected, since they aren't meant to be clicked.

## Troubleshooting {#troubleshooting}

| Issue | Why | Solution |
|---|---|---|
| "This link uses HTTP. Only HTTPS links are allowed." | Insecure scheme | Update the URL to use `https://`. |
| "This link couldn't be reached." | 404 response or timeout | Verify the URL is correct and the host is online. |
| No validation result is returned at all | Content contains more than 50 URLs, so the entire request is rejected | Reduce the number of links in your content, then preview again. |
| A link with a `{{ }}` personalization token is flagged as invalid | Expected — see [Caveats](#caveats). This always happens for personalized links, even valid ones. | Ignore the flag and verify the link manually. |
| A flagged URL actually works fine and isn't personalized | False positive — see [Caveats](#caveats) | It's likely a namespace URL, a CDN resource, or content in comments/metadata — safe to ignore if it isn't user-facing. |
