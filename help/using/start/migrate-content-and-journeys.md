---
solution: Journey Optimizer
product: journey optimizer
title: Migrate content and journeys
description: Learn how to migrate email content templates and import journeys from external platforms using the Journey Optimizer onboarding hub.
feature: Get Started
topic: Content Management
role: User
level: Intermediate
badge: label="Limited Availability" type="Informative"
---
# Migrate content and journeys {#migrate-content-and-journeys}

If you are moving to [!DNL Journey Optimizer] from another marketing platform, the [onboarding hub](onboarding-hub.md) includes a migration workspace that imports your existing email content and journeys instead of requiring you to rebuild them from scratch.

## Set up a connection {#set-up-a-connection}

To import content or journeys through an API, first connect [!DNL Journey Optimizer] to your source platform:

1. In the migration workspace, select **Manage connections**.
2. Select **Create connection** and provide a connection name, base URL, client ID, client secret, and token URL.
3. Select **Create**.
4. Optionally, mark a connection as default so it is pre-selected the next time you import content or journeys.

>[!TIP]
>
>A connection is not required if you upload HTML files or screenshots instead of importing through an API.

## Import email content {#import-email-content}

1. In the migration workspace, upload an email's HTML file, or browse an existing connection to select one.
2. Review the imported HTML next to the original source.
3. Map each personalization placeholder to the corresponding profile attribute. The migration workspace converts the source scripting syntax to [!DNL Handlebars] syntax automatically.
4. Select a folder to upload the email's images to [!DNL Experience Manager Assets].
5. Select **Migrate**, then select **View in [!DNL Journey Optimizer]** to open the new content template.

Each imported email shows a status of needs review, migrated, or failed, so you know what still needs attention.

## Import journeys {#import-journeys}

1. In the migration workspace, upload a screenshot of the journey flow, or import through an API connection.
2. Preview the journey that the migration workspace generates from your source.
3. For each message step, select a channel configuration and content template.
4. Select the audience for the journey.
5. Select **Apply changes**, then select **View in [!DNL Journey Optimizer]** to open the journey canvas.

As with email content, each imported journey shows a status so you can see what is migrated, what needs review, or what failed.

## Track migration progress {#track-migration-progress}

The migration workspace overview shows how many journeys and email templates are imported, in progress, migrated, or failed. Use this view to prioritize what still needs review.

## Related resources {#related-resources}

* [Journey Optimizer onboarding hub](onboarding-hub.md) — Ramp up on [!DNL Journey Optimizer] with guided instructions, use cases, and videos.
* [Build your first journey](../building-journeys/journey-gs.md) — Create a journey from scratch instead of migrating one.
