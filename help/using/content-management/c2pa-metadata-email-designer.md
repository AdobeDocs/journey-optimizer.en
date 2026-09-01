---
solution: Journey Optimizer
product: journey optimizer
title: C2PA metadata in Email and Landing Page Designer
description: Learn what happens to C2PA metadata already attached to an image as it moves through the email and landing page designer in Adobe Journey Optimizer.
feature: Content Management
topic: Content Management, Artificial Intelligence
role: User
level: Beginner
---

# C2PA metadata in Email and Landing Page Designer {#c2pa-email-landing-page-designer}

>[!BEGINSHADEBOX]

**On this page:** Learn what happens to C2PA metadata already attached to an image as it moves through the email and landing page designer in Adobe Journey Optimizer.

>[!ENDSHADEBOX]

>[!INFO]
>
>New laws are emerging around generative AI transparency, and Adobe is working to meet applicable requirements across jurisdictions. C2PA metadata are the provenance tool Adobe uses to meet the requirements of these laws.

The email and landing page designer does not generate or edit images itself. It references images that were already generated or edited with generative AI in another Adobe tool, such as Generate content, Adobe Express, or Firefly, or in a partner model. C2PA metadata already attached to those images are preserved and unchanged as you build, publish, and send.

## C2PA metadata are preserved as you build and send {#c2pa-preserved}

The following table summarizes what happens to C2PA metadata at each step of building and sending content with the email and landing page designer.

| Action | What happens | C2PA metadata preserved? | Example |
| --- | --- | --- | --- |
| **Insert an image into a template** | The designer adds a reference to an image already generated or edited with generative AI elsewhere, such as Generate content, Adobe Express, Firefly, or a partner model. The image file itself is not changed. | Yes, unchanged | A Firefly-generated banner is inserted into an email template. |
| **Resize, reposition, or add alt text** | Only display properties in the template's HTML change. The image file is not re-encoded. | Yes, unchanged | An image is resized to fit a mobile layout and given alt text. |
| **Publish** | The email or landing page is published, and the image is stored for delivery. | Yes, unchanged | A campaign is published and its images are stored for send. |
| **Send an email or view a landing page** | The image is delivered to the recipient's inbox or displayed on the live page. | Yes, unchanged | A recipient opens the email and downloads the image; the credential still matches the original. |

## Content types and their scope {#c2pa-content-types}

* **Images**: Covered. C2PA metadata already attached to an image are preserved as it is inserted, adjusted, published, and delivered, as shown above.
* **Video, audio, text**: Not applicable. The email and landing page designer does not generate or edit these content types with generative AI.

## What happens as your content moves {#c2pa-content-moves}

C2PA metadata travel with the image across the email and landing page designer in Adobe Journey Optimizer, from your editor through storage to the recipient's inbox or the live page. No credential is created, changed, or removed at any of these steps.

If an image does not carry generative AI C2PA metadata, because it was not generated or edited with generative AI, no credential appears on it here. That is expected, not an error.

## Checking a credential {#c2pa-checking-credential}

There is not yet a way to inspect a Content Credential directly inside the email or landing page designer.

## Additional resources

* [C2PA metadata in Generate content](generative-c2pa-metadata.md)
* [Generative AI content transparency](https://experienceleague.adobe.com/en/docs/cx-enterprise-ai/experience-cloud-ai/overview/content-transparency)
