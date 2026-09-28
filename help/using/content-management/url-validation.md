---
title: Validate URLs in your content
description: Learn how URL validation checks the web links in your message content before you send.
badge: label="Limited availability" type="Informative"
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

>[!AVAILABILITY]
>
>This capability is released in Limited Availability (LA) for a set of customers. Contact your Adobe representative to gain access.

When you preview your message content, [!DNL Journey Optimizer] automatically checks the web links it contains. Validation runs after your personalization is resolved, so real URLs are checked rather than unresolved template tokens. This helps you catch broken or inaccessible links before your message reaches your audience.

## Where to find it {#access}

URL validation runs automatically from the **[!UICONTROL Simulate content]** screen, for channel actions in journeys and campaigns across all channels, and when you preview [content templates](content-templates.md).

## How it works {#how-it-works}

* Every `http://` and `https://` URL in your content is checked — including links, images, and stylesheets, not only clickable text links.
* Each URL is checked to confirm that the host resolves, responds with a success status, and responds within an acceptable time. Only the response status is checked; page content is never downloaded.
* If issues are found, they're identified along with the reason and guidance on how to fix them.

>[!IMPORTANT]
>
>If your content contains more than 50 URLs, validation doesn't just skip the extras — the entire request is rejected and no result is returned. Reduce the number of links in your content to get a validation result.

## What gets flagged {#invalid-urls}

| Issue | Example | Error message | Why it's flagged |
|---|---|---|---|
| Insecure scheme | `http://example.com` | "This link uses HTTP. Only HTTPS links are allowed." | HTTP links aren't secure. |
| Malformed URL | Empty URL, bad host, spaces | "This link couldn't be reached." | The URL can't be parsed. |
| Scheme typo | `hhttps://`, `ttps://` | "This link couldn't be reached." | The scheme isn't recognized. |
| Broken or unreachable | A 404 response, or a domain that doesn't resolve | "This link couldn't be reached." | The page doesn't exist or the host can't be reached. |
| Internal or blocked address | `localhost`, `192.168.x.x`, `169.254.169.254` | "This link couldn't be reached." | Internal or private network addresses are blocked for security reasons. |
| Timeout | The host took too long to respond | "This link couldn't be reached." | The host didn't respond in time. |

For steps to fix each of these, see [Troubleshooting](#troubleshooting).

## What doesn't get checked {#not-checked}

The following aren't flagged as broken, even if they appear in your content:

* **Non-web links** — `adbinapp://`, `mailto:`, `tel:`, `sms:`, and `data:` URIs aren't web URLs.
* **Relative links** — `/page` or `./image.jpg` have no host to check.
* **Anchors** — `#section` is a local page reference.
* **Empty links** — An empty `href` isn't a link.

## Caveats {#caveats}

>[!IMPORTANT]
>
>**Personalized links are always flagged as invalid.** If a link contains a personalization token, that token isn't resolved during validation, so the URL is incomplete and can never be reached. This happens every time, whether or not the underlying link actually works.
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
1. Expect any link containing a personalization token to always show as invalid. Verify these links manually instead of relying on the validation result.
1. Stay under the 50-URL limit — going over it doesn't trim the extras, it rejects the whole validation request. Consider splitting your content across multiple messages or templates.
1. Expect namespace or data URIs in your schema to show as invalid — that's expected, since they aren't meant to be clicked.

## Troubleshooting {#troubleshooting}

| Issue | Why | Solution |
|---|---|---|
| "This link uses HTTP. Only HTTPS links are allowed." | Insecure scheme | Update the URL to use `https://`. |
| "This link couldn't be reached." | Malformed URL, scheme typo, 404 response, blocked internal address, or timeout — see [What gets flagged](#invalid-urls) | Fix the URL, or verify the host is correct, online, and reachable. |
| No validation result is returned at all | Content contains more than 50 URLs, so the entire request is rejected | Reduce the number of links in your content, then preview again. |
| A link with a `{{ }}` personalization token is flagged as invalid | Expected — see [Caveats](#caveats). This always happens for personalized links, even valid ones. | Ignore the flag and verify the link manually. |
| A flagged URL actually works fine and isn't personalized | False positive — see [Caveats](#caveats) | It's likely a namespace URL, a CDN resource, or content in comments/metadata — safe to ignore if it isn't user-facing. |

