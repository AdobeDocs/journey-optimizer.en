---
solution: Journey Optimizer
product: journey optimizer
title: Preview, validate, and send your LINE message
description: Learn how to preview and validate a LINE message, resolve warnings and errors, request approval when required, and activate or publish it in a journey or campaign
feature: Line
topic: Content Management
role: User
level: Beginner
exl-id: fd8437c6-0052-4116-af60-5624569bda65
TQID: https://experienceleague.adobe.com/Bfu4AL1axI4XUq0PKXuN0PnnxNvq4MB-O7Bzz66mtbU
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: d0a62d3c-b79e-47e4-929e-40ef3cffa037
    internal-label: Communication channels
  - id: dc22c819-3f29-4e91-8b7d-5c6719831141
    internal-label: Content management
subfeature_v2:
  - id: b3a93754-a8b8-46eb-9421-7eccaeeb3dff
    internal-label: Best practices
  - id: f8d2e9f0-69c9-40cd-890f-71336c8dfff7
    internal-label: Preview
  - id: e09fc1e6-407c-418f-adc5-e2ffe8b8986e
    internal-label: LINE channel
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
level_v2:
  - id: e8ccd51f-da0d-4e3b-939b-e30d5ebb1ea5
    internal-label: Beginner
---

# Preview, validate, and send your LINE message {#send-line}

>[!BEGINSHADEBOX]

**On this page:** Preview and validate your LINE message, resolve warnings and errors, request approval when required, and complete the journey or campaign configuration to send the message.

>[!ENDSHADEBOX]

## Before you start {#before-you-start}

Before you begin, make sure that:

* LINE is enabled for your organization. If LINE is not available, contact your Adobe representative to request activation.
* A LINE channel configuration is available in Journey Optimizer. See [Configure the LINE channel](./line-configuration.md).
* You have added a LINE action to a journey or campaign and defined the message content. See [Create a LINE message](./create-line.md).

## Preview your LINE message {#preview-line}

After you define your message content, use **[!UICONTROL Simulate content]** to preview the message before sending it.

You can use either of the following options:

| Simulation option | Use it to |
| --- | --- |
| **[!UICONTROL Simulate content]** | Test content variations with sample input data or AI auto-generation. |
| **[!UICONTROL Simulate content]** > **[!UICONTROL Simulate content (AEP profiles)]** | Preview the message with test profiles. |

Review each variation and verify that the message content and personalized values are displayed as expected.

For detailed information about previewing and testing content, see [Preview and test content](../content-management/preview-test.md).

## Validate your content {#line-validate}

Before you continue, review the alerts shown at the top of the message editor.

Journey Optimizer displays two types of alerts:

* **Warnings** are recommendations or best-practice suggestions. They do not prevent you from testing or sending the message.
* **Errors** identify issues that must be resolved before you can test or activate the journey, or publish the campaign.

Resolve all errors before continuing. Address warnings when they indicate that the message may not provide the intended customer experience.

## Request approval when required {#line-approval}

If your campaign is subject to an approval policy, request approval before sending the message.

See [Learn how to request approval](../test-approve/gs-approval.md).

## Send your LINE message {#line-send}

When the message is ready, return to the journey or campaign that contains the LINE action and complete its configuration:

* **Journey:** Complete the journey configuration, then activate the journey.
* **Campaign:** Complete the campaign configuration, then publish the campaign.

If you cannot activate the journey or publish the campaign, return to the message editor and resolve any remaining errors.

## Related tasks {#related-tasks}

* [Get started with LINE](./get-started-line.md)
* [Create a LINE message](./create-line.md)
* [Configure the LINE channel](./line-configuration.md)

{{$include /help/_includes/do-not-localize/line/ai-augmented-send-line.md}}