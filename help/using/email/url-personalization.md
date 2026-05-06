---
solution: Journey Optimizer
product: journey optimizer
title: Personalize URLs in emails
description: Learn best practices and limitations for dynamically generating URLs while keeping tracking reliable
feature: Email Design, Monitoring
topic: Content Management
role: User
level: Intermediate, Experienced
keywords: url, link, personalization, tracking, encode, curly braces

---
# Personalize URLs in emails {#url-personalization}

Personalized URLs help you deliver contextual experiences through your [!DNL Journey Optimizer] email messages, such as generating recipient-specific links or appending dynamic parameters.

They take recipients to specific pages of a website, or to a personalized microsite, depending on the profile attributes.

## Personalize a URL {#personalize-url}

To personalize a URL, follow the steps below.

1. In the Email Designer, select an element in the content and [insert a link](message-tracking.md#insert-links) using the contextual toolbar.

    >[!IMPORTANT]
    >
    >Personalization is only available for **[!UICONTROL External link]**, **[!UICONTROL Unsubscription link]** and **[!DNL Opt-Out]**. Make sure to select an appropriate link type.

1. Select the personalization icon.

    ![](assets/message-tracking-insert-link-perso.png)

1. Use the personalization editor to add the profile attributes you want to personalize the URL with.

1. Save your changes.

Here are some examples of personalized URLs:

* `https://www.adobe.com/users/{{profile.person.name.lastName}}` 
* `https://www.adobe.com/users?uid={{profile.person.name.firstName}}`
* `https://www.adobe.com/usera?uid={{context.journey.technicalProperties.journeyUID}}`
* `https://www.adobe.com/users?uid={{profile.person.crmid}}&token={{context.token}}`

>[!NOTE]
>
>When editing a personalized URL in the personalization editor, helper functions and audiences membership are disabled for security reasons.
>
>Spaces are not supported in the personalization tokens used inside urls.

For reliable rendering and tracking, follow the [best practices and guardrails](#best-practices) below.

## Personalize a complete/base URL {#personalize-complete-base-url}

Journey Optimizer also supports personalizing the **entire** URL or the **base domain** of a URL, for example:

```html
<a href="{{profile.social.link}}" />
<a href="{{profile.social.baseUrl}}/profile" />
<a href="https://{{profile.social.baseUrl}}/profile" />
```

>[!IMPORTANT]
>
>To enable complete or base URL personalization, contact Adobe and provide your list of accepted domains. This is required to help prevent unsafe redirects.

## Personalize URL tracking parameters {#personalize-url-tracking-parameters}

[URL tracking](url-tracking.md) is managed at the channel configuration level and applies to all URLs included in your message content. You can also personalize URL tracking parameters for an individual link in the Email Designer. This lets you append a recipient-specific parameter to a single link (for example, to pass an identifier to your web analytics tools).

To do so, [insert a link](message-tracking.md#insert-links), select the personalization icon, add the URL tracking parameter and select the profile attribute of your choice from the [personalization editor](../personalization/personalization-build-expressions.md).

![](assets/message-tracking-perso-parameter.png)

Repeat the steps above for each link you want to add this tracking parameter to.

Now when the email is sent out, this parameter is automatically appended to the end of the URL. You can then capture this parameter in web analytics tools or in performance reports.

>[!NOTE]
>
>To verify the final URL, you can [send a proof](../content-management/proofs.md) and click the link in the content of the email once you receive the proof. The URL should display the tracking parameter. For example: <https://luma.enablementadobe.com/content/luma/us/en.html?utm_contact=profile.userAccount.contactDetails.homePhone.number>


<!--
## Best practices and guardrails {#best-practices}

To keep links valid, clickable, and trackable, follow the best practices and guardrails below.

### Braces for dynamic URLs {#use-braces}

When inserting a URL that contains personalization, use three curly braces (`{{{ ... }}}`) for the dynamic portion of the URL. This prevents escaping from altering special characters (for example `/` and `+`) and helps avoid broken URLs, incorrect redirects, or tracking issues.

Here is an example:

```html
<a href="https://example.com/path/{{{profile.person.customSlug}}}?ref={{{context.system.source.id}}}">View details</a>
```

>[!IMPORTANT]
>
>Using raw output (`{{{ ... }}}`) means the value is inserted as-is. Only use it with values you trust and that are intended to be URL-safe (for example, values you generate or validate upstream).

### Correct URL tracking {#enable-url-tracking}

* When using personalization to generate the URL, ensure the resolved value starts with `http`/`https` for every recipient. Otherwise, tracking may not be applied and the link may not behave as expected.

* Do not use dynamic logic such as `let`, `each`, or `if` statements directly in the personalization editor's URL field. These are disabled for security reasons.

* If your scenario involves complex logic to generate personalized URLs, avoid placing that logic directly in the personalization editor's URL field. Instead:
    * Add the necessary logic and statements in the HTML content above or near the URL field.
    * Generate and store personalized attributes separately, then reference them in your email content.

### URL encoding and length {#encoding}

* URI syntax rules ([RFC 3986 standard](https://datatracker.ietf.org/doc/html/rfc3986){target="_blank"}) apply to all URLs in your email content. However, personalized URLs are more likely to surface encoding issues because recipient-specific values can introduce reserved characters (for example in query parameters). Therefore, ensure your dynamic values are URL-encoded (especially spaces, `&`, `#`, `%`, and `+`) and avoid using `+` for query values.

* Very long URLs can be truncated or rejected by browsers, mail clients, or downstream systems. For example, mirror page URLs can grow significantly when runtime personalization is heavy. Keep personalized payloads small and avoid embedding large objects into URLs.

### Recommended validation steps {#validation}

Before activating a journey or campaign, follow the recommendations below:

* Send a [proof](../content-management/proofs.md) and click links to confirm the resolved URL starts with `http`/`https` and keeps the expected structure.
* If tracking parameters are appended, confirm the final URL includes them (either via configuration-level URL tracking or per-link tracking parameters).
-->
