---
title: Simulate inbound actions
description: Learn how to simulate inbound experiences in Action campaigns before activation.
feature: Campaigns, Preview
topic: Content Management
role: User
level: Beginner
badge: label="Private Beta" type="Informative"
hide: true
exl-tag: PrivateBeta
---

# Simulate inbound experiences {#simulate-inbound-experiences}

>[!BEGINSHADEBOX]

**On this page:** Validate inbound Action campaign experiences with simulated users before going live, including link and QR preview, simulation behavior, and key limitations.

>[!ENDSHADEBOX]

>[!AVAILABILITY]
>
>This capability is currently in Private Beta. To request access, contact your Adobe representative.

## Overview {#inbound-simulation-overview}

Inbound experience simulation lets you validate personalized inbound experiences for an **Action campaign** with simulated users before the campaign is live. Use it to verify targeting, decisioning, rendered content, and troubleshoot behavior across web and mobile preview paths.

When simulation mode starts, the campaign enters the **[!UICONTROL Simulation]** status. You can navigate away and return later while simulation remains active, and campaign content and configuration are locked for editing (similar to a published state). Simulated experiences are not exposed to your production audience.

For the full campaign review flow, including content preview and simulation context, see [Review and activate an Action campaign](../campaigns/review-activate-campaign.md).

## Enter and run simulation mode {#enter-simulation-mode}

To enter simulation mode:

1. In your Action campaign, access the **[!UICONTROL Review to activate]** interface then select the **[!UICONTROL Simulate actions]** tab.

    ![](assets/simulation-mode-enter.png)

1. Select the simulated users you want to use for the simulation using one of the available methods:

    * **[!UICONTROL Browse inventory]** - Select previously created simulated users.
    * **[!UICONTROL Create from form]** - Create a simulated user field by field.
    * **[!UICONTROL Create from JSON]** - Import a JSON file simulated user profile payload.

    ![](assets/simulation-mode-ui.png)
    
    For more details on creating and managing simulated users, refer to [Create and manage simulated users](../building-journeys/simulate-journey.md#test-users).

1. Once simulated users are selected or created, they appear in the center pane. For each user, you can view details, update the user information, or remove the user from the simulation list.

    ![](assets/simulation-mode-users.png)

1. To generate the simulated output for each user, click the **[!UICONTROL Generate link]** button. This generates:

   * A shareable URL to preview the rendered inbound experience for the selected user.
   * A QR code for mobile preview scenarios.

1. For each simulated user, use the generated controls to validate the experience:

    ![](assets/simulation-mode-generate.png)

    | Button | What it does |
    | --- | --- |
    | ![Open link button](assets/simulation-action-open.png) | Open the generated link in a browser to preview the inbound experience for that simulated user. |
    | ![Copy link button](assets/simulation-action-copy.png) | Copy the generated link so you can share it or paste it into another browser or device. |
    | ![QR code button](assets/simulation-action-qr.png) | Open the QR code (if available for the channel), select **[!UICONTROL iOS]** or **[!UICONTROL Android]**, scan the code with your device camera, and enter the displayed code when prompted. |
    | ![More actions button](assets/simulation-action-more.png) | Open additional options to **[!UICONTROL Open assurance session]** or **[!UICONTROL New assurance session]** and continue troubleshooting in the Assurance user interface. |

1. You can leave simulation mode at any time by clicking **[!UICONTROL Stop simulation]** in the campaign action bar, for example if you need to go back and edit the campaign.
