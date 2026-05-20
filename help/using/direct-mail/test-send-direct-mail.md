---
solution: Journey Optimizer
product: journey optimizer
title: Check & send a direct mail message
description: Learn how to check and send a direct mail message in Journey Optimizer
feature: Direct Mail, Test Profiles, Preview
topic: Content Management
role: User
level: Beginner
keyword: direct, mail, configuration, direct-mail, provider
exl-id: 69a19190-d2e2-4858-a1df-ffd008226e2b
TQID: https://experienceleague.adobe.com/4GZKFKOx-D-RT1mssiV5vpmZQSJGVbGMro8Q-suhtPE
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: d556b755-390a-43f0-be32-a08cf6236126
    internal-label: Configuration
  - id: d998adac-2f81-400b-a669-d07bb196e4eb
    internal-label: Journeys
  - id: dc22c819-3f29-4e91-8b7d-5c6719831141
    internal-label: Content management
subfeature_v2:
  - id: b3a93754-a8b8-46eb-9421-7eccaeeb3dff
    internal-label: Best practices
  - id: f8d2e9f0-69c9-40cd-890f-71336c8dfff7
    internal-label: Preview
  - id: fb9a80eb-bebc-492f-a0e9-584595621ebb
    internal-label: Publish
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
level_v2:
  - id: e8ccd51f-da0d-4e3b-939b-e30d5ebb1ea5
    internal-label: Beginner
topic_v2:
  - id: aa2f3246-cb95-4b30-8899-fdf7d73550cc
    internal-label: Reporting
  - id: f4e6943a-c91a-4134-a2c7-f4f20cfff2f0
    internal-label: Privacy
---
# Check & send a direct mail message {#direct-mail-test-send}

Learn how to preview the extraction file, validate and activate your direct mail campaign or journey, and manage postal mail consent in Journey Optimizer.

## Before you start {#before-you-start}

Before you test and send a direct mail message, [create the message and configure the extraction file](create-direct-mail.md). Ensure you have also completed [direct mail channel configuration](direct-mail-configuration.md).

## Preview the extraction file {#preview-dm}

Once the content of the extraction file has been defined, you can use test profiles to preview it. If you inserted personalized content, you can check how this content is displayed in the message, using test profile data.

To do this, click **[!UICONTROL Simulate content]** then add a test profile to check how the extraction file rendering using the test profile data.

![Simulate content preview for a direct mail extraction file](assets/direct-mail-simulate.png){width="800" align="center"}

Detailed information on how to select test profiles and preview your content is available in the [Content Management](../content-management/preview-test.md) section.

Once that the file content is ready to be sent, close the simulate screen then click the **[!UICONTROL Review to activate]** button.

## Validate & activate the direct mail campaign {#dm-validate}

>[!IMPORTANT]
>
> If your campaign is subject to an approval policy, you will need to request approval in order to be able to send your Direct mail campaign. [Learn more](../test-approve/gs-approval.md)

Before activating the direct mail campaign, make sure that the campaign or journey and the extraction file are configured properly. To do this, check alerts in the upper section of the editor. Some of them are simple warnings, but others can prevent you from sending the message. Two types of alerts can happen: warnings and errors.

* **Warnings** refer to recommendations and best practices. For example, a warning message is displayed if your SMS message is empty.

* **Errors** prevent you from publishing the campaign, as long as they are not resolved. For example, an error message warns you when the subject line is missing.

![Review and activate screen showing direct mail campaign validation alerts](assets/direct-mail-review.png){width="800" align="center"}

When your direct mail campaign is ready, complete the configuration of your [journey](../building-journeys/journey-gs.md) or [campaign](../campaigns/create-campaign.md) to send it.

>[!NOTE]
>
>The exported file by default ends with a newline. This ensures compatibility with standard data-processing tools.

Once sent, you can measure the impact of your direct mail campaign or journey within the reports. For more about direct mail reporting, refer to these sections:
* [Direct mail campaign report](../reports/campaign-global-report-cja-direct.md)
* [Direct mail journey report](../reports/journey-global-report-cja-direct.md)

## Manage consent for direct mail {#dm-consent-management}

In [!DNL Journey Optimizer], consent is handled by the Experience Platform [Consent schema](https://experienceleague.adobe.com/docs/experience-platform/xdm/field-groups/profile/consents.html){target="_blank"}. By default, the value for the consent field is empty and treated as consent to receive your communications.

If a profile has opted out from receiving direct mail, in the corresponding Experience Platform profile attributes, the value for `consents.marketing.postalMail.val` will be `n` and the corresponding profile will be excluded from subsequent deliveries.

To enable it again, the profile attribute has to be changed back to `consents.marketing.postalMail.val` : `y`.

To manage a profile's attributes, go to Experience Platform and access the profile by selecting an identity namespace and a corresponding identity value. Learn more in the [Experience Platform documentation](https://experienceleague.adobe.com/docs/experience-platform/profile/ui/user-guide.html#getting-started){target="_blank"}.

Learn more about managing opt-out in Journey Optimizer in [this section](../privacy/opt-out.md).

## Related topics {#related-topics}

* [Get started with direct mail](get-started-direct-mail.md)
* [Create a direct mail message](create-direct-mail.md)
* [Configure direct mail channel](direct-mail-configuration.md)
* [Preview and test content](../content-management/preview-test.md)

For common questions about direct mail, see [Get started with direct mail](get-started-direct-mail.md).
