---
solution: Journey Optimizer
product: journey optimizer
title: Simulate content variations
description: Learn how to preview all your content variants side by side, manage them from the bottom action bar, and switch to the classic experience in the redesigned Simulate content variations experience.
feature: Email, Email Rendering, Personalization, Preview, Proofs
topic: Content Management
role: User
level: Intermediate
hide: true
exl-id: d9f7e0a3-b8c2-4e5f-92a1-3c1d7e8a4f65
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: dc22c819-3f29-4e91-8b7d-5c6719831141
    internal-label: Content management
subfeature_v2:
  - id: f8d2e9f0-69c9-40cd-890f-71336c8dfff7
    internal-label: Preview
  - id: a5683ded-e5d5-4ec6-b9fd-e1b56a94ab96
    internal-label: Proofs
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
level_v2:
  - id: b5a62a22-46f7-4f0d-b151-3fc640bef588
    internal-label: Intermediate
topic_v2:
  - id: bcc5edb5-84c3-4940-9f84-ed88b6c16274
    internal-label: Experimentation
  - id: e0eb8757-182f-49f3-94a4-1587d16f5094
    internal-label: Personalization
---

# Simulate content variations {#simulate-content-variations}

>[!BEGINSHADEBOX]

**On this page:** Preview all your content variants at a glance in a side-by-side grid, manage them from a consolidated bottom action bar, and switch back to the classic experience at any time.

>[!ENDSHADEBOX]

The **[!UICONTROL Simulate content variations]** experience has been redesigned to make testing and comparing your variants faster and easier. All variants now render together in a single scrollable grid, and every control you need — navigation, zoom, viewport, locale, variant generation, and more — is available from a single bottom action bar.

## What's new in this experience {#whats-new}

When you open the simulate content variations screen for the first time, a welcome dialog summarizes the key improvements:

* **All variants, side by side** — Every variant renders together in a scrollable grid, so you can compare them at a glance instead of clicking through one at a time.
* **Controls in one place** — Navigate between test variants, zoom, and switch viewport, locale, or simulated users from a single bottom action bar.
* **More room for your previews** — The left rail and extra header layers have been removed to give previews more screen real estate.

Click **[!UICONTROL Explore the new experience]** to dismiss the dialog and start using the redesigned interface. You can switch back to the classic layout at any time from the bottom action bar.

>[!NOTE]
>
>The redesigned experience is available for the Email, SMS, Push notification, and all inbound channels (Web, Code-based experience, In-app, Content cards), as well as Orchestrated campaigns.

## Access the experience {#access}

From your content, click **[!UICONTROL Simulate content]** to open the content simulation screen.

If variants are already available, the preview grid is shown immediately. If none exist yet, a blank variant is displayed and you can start creating them using any of the methods described below.

## Create and manage variants {#manage-variants}

Variants are managed from the **variants list view**. To switch between the preview grid and the variants list, click the **toggle view** button (the leftmost icon in the bottom action bar).

![Bottom action bar toggle](assets/simulate-new-toolbar.png)

### Variants list view {#variants-list}

In the variants list view, each variant is displayed as a card showing its profile attributes. For example:

* **Variant 1** — `Person > First name: Anna`
* **Variant 2** — `Person > First name: Guybrush`
* **Variant 3** — `Person > First name: John`

The currently active variant is highlighted with a blue border.

From each variant card you can:

* Click **[!UICONTROL Edit]** to update the attribute values for that variant.
* Click the **[!UICONTROL ...]** menu to access additional options such as duplicating or deleting the variant.

![Variants list view](assets/simulate-new-variants-list.png)

### Add variants {#add-variants}

From the bottom action bar, use the **[!UICONTROL +]** button to add a new blank variant manually, or use the following options in the **[!UICONTROL ...]** menu to populate variants in bulk:

* **Upload data** — Import a CSV, JSON, or JSONLINES file where each row or entry becomes a variant. Download the file template from the upload dialog to use the correct format.
* **[!UICONTROL Generate]** — Let AI automatically create variants by analyzing your content's personalization fields and conditional branches. Generated variants replace any existing ones.
* **[!UICONTROL Select variants]** — Pick from your saved simulated users to use as variant data. See [Select variants from simulated users](#simulated-users).

>[!NOTE]
>
>You can add up to 30 variants manually or via file upload. When using AI generation, up to 40 variants can be created depending on your content's complexity.

### Auto-generate variants {#auto-generate}

To auto-generate variants using AI, click the **[!UICONTROL Generate]** button in the bottom action bar. The system analyzes your content, identifies personalization fields and conditional branches, and generates as many variants as needed to cover them with realistic values.

>[!NOTE]
>
>Clicking **[!UICONTROL Generate]** replaces all existing variants, including any added manually or from a file.

### Select variants from simulated users {#simulated-users}

You can base your variants on **simulated users** — reusable, profile-like test entities that are saved across sessions and can be shared with other users. Unlike manually entered variants, simulated users persist beyond the current browser session.

Simulated users are created and managed from the journey **[!UICONTROL Simulation]** feature. For the full procedure, see [Create and manage simulated users](../building-journeys/simulate-journey.md#test-users).

To use simulated users as variants:

1. Click **[!UICONTROL Select variants]** in the bottom action bar.
1. Select the simulated users you want to use from the list, then click **[!UICONTROL Select]**.

The selected simulated users are added as variants. You can edit a variant's attribute values locally for testing, but those changes are not saved back to the simulated user record.

## Preview variants in the grid {#preview-grid}

Click the **toggle view** button in the bottom action bar to switch to the preview grid. All variants render side by side, each in its own column with a numbered indicator at the top.

For SMS and Push channels, each variant is shown in a phone mockup so you can assess layout and content length in context.

![Variants preview grid — SMS example](assets/simulate-new-sms-grid.png)

Use the **bottom action bar** to control the preview:

| Control | Description |
|---|---|
| **Toggle view** (leftmost icon) | Switch between the variants list and the preview grid. |
| **< > navigation** | Page through variants when more variants exist than fit on screen. Click a page number to jump directly to that set. |
| **Zoom** | Zoom in or out on the preview grid. |
| **Viewport** | Switch between desktop and mobile viewport to check responsive rendering. |
| **Locale** | Switch the display locale when using multilingual content. |
| **[!UICONTROL Generate]** | Auto-generate variants with AI (replaces existing variants). |
| **[!UICONTROL Select variants]** | Pick simulated users to use as variants. |
| **[!UICONTROL ...]** | Access additional options: upload data from a file, export variants, and more. |

## Send proofs {#proofs}

You can send proofs to email addresses for one or more variants directly from the simulation screen. This works the same way as in the classic experience.

1. Ensure variants are available, then click the **[!UICONTROL Send Proof]** button in the top header.
1. In the **[!UICONTROL Recipients]** field, enter the email address and click **[!UICONTROL Add]**. You can add up to 10 recipients.
1. Select the variant(s) to use in the proof. If multiple variants are selected, the email includes one proof per variant.
1. Click **[!UICONTROL Send Proof]** to send.

To track sent proofs, click **[!UICONTROL View proofs]** in the top header.

## Switch to the classic experience {#classic}

If you prefer the previous layout, click **[!UICONTROL Switch to classic experience]** in the bottom action bar at any time. The classic experience documentation is available at [Simulate content variations (classic experience)](simulate-sample-input.md).
