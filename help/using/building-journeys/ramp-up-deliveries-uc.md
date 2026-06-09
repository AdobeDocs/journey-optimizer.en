---
solution: Journey Optimizer
product: journey optimizer
title: Ramp up your deliveries
description: Learn how to ramp up your deliveries
feature: Journeys, Use Cases, IP Warmup Plans
topic: Content Management
role: User, Developer
level: Intermediate, Experienced
hide: true
keywords: deliverability, journey, use case, email, reputation
exl-id: 83d1b68d-011a-4109-b5f0-6ca1ade2944d
version: Journey Orchestration
TQID: https://experienceleague.adobe.com/en0jMw69ddHSQrIH05-9FfGuDwNKb36f5Lp3fLp2oAk
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: b3538224-471e-4c63-a444-9b19d89ae29c
    internal-label: Activities
  - id: d998adac-2f81-400b-a669-d07bb196e4eb
    internal-label: Journeys
  - id: df64005d-8f9a-422e-ba4d-c6f6dc3454b4
    internal-label: Use cases
subfeature_v2:
  - id: d8353d85-5da7-453d-bd68-40ad33fa0ab7
    internal-label: Action activities
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
level_v2:
  - id: b5a62a22-46f7-4f0d-b151-3fc640bef588
    internal-label: Intermediate
---
# Use case: ramp up your deliveries{#use-case-ramp-up-your-deliveries}

If you recently moved to another email service provider, IP address, or email domain or subdomain, you need to establish your reputation as a sender. Otherwise, your deliveries might be blocked or moved to the spam folder of the recipients' mailbox. Learn how to increase your email reputation with IP warming in the [Deliverability Best Practice Guide](https://experienceleague.adobe.com/docs/deliverability-learn/deliverability-best-practice-guide/additional-resources/generic-resources/increase-reputation-with-ip-warming.html){target="_blank"}.

To warm up your IP, you can gradually ramp up the number of your deliveries. Read more about [optimizing deliverability in Journey Optimizer](../reports/deliverability.md).

The purpose of this use case is to create a journey to ramp up your email deliveries. To configure this journey, follow these steps:

1. Create a journey. [Read more](journey-gs.md).

1. Add an **[!UICONTROL Optimize]** activity to the journey. [Read more](optimize.md).

1. In the **[!UICONTROL Condition]** activity settings, set the maximum number of recipients for your delivery:

   1. In the **[!UICONTROL Optimize]** activity settings, select **[!UICONTROL Conditions]** method and set the **[!UICONTROL Type]** field to **[!UICONTROL Profile cap]**. [Read more](conditions.md#profile_cap).

   1. Set the **[!UICONTROL Limit]** field to the maximum number of recipients for this delivery.

    ![Profile cap condition configuration for controlling delivery volume](assets/profile-cap-condition.png)

      You can gradually increase this limit up to the total number of your subscribers.

1. Add an **[!UICONTROL Email]** action activity to the nominal path after the **[!UICONTROL Condition]** activity.

    ![Email message configuration in ramped delivery journey](assets/ramp-up-deliveries-message.png)

    When the journey runs, the message is sent the entering profiles, up to the maximum number of profiles that you have specified. When this limit is reached, the entering profiles take the alternate path.

1. Complete the journey with the activities of your choice.

After your IP has warmed up, you can remove this condition.

+++AI Assistant — Page context

- **TL;DR:** This use case describes how to build an Adobe Journey Optimizer journey that gradually ramps up email delivery volume using a Profile cap condition to protect sender reputation during IP warming.

**Intents:**
- Build a journey to gradually increase email delivery volume for IP warming
- Configure a Profile cap condition to limit the number of recipients per delivery run
- Protect sender reputation when switching to a new email service provider, IP address, or domain
- Remove the volume cap condition once the IP is fully warmed up

**Glossary:**
- **IP warming**: The process of gradually increasing email send volume from a new IP address or domain to build sender reputation with mailbox providers *(product-specific)*
- **Profile cap**: A condition type in the Optimize activity that limits the maximum number of profiles that receive a message in a given journey run *(product-specific)*
- **Optimize activity**: A journey canvas activity used to apply conditions, targeting rules, or experimentation to control how profiles flow through a journey *(product-specific)*

**Guardrails:**
- A Profile cap condition must be set in the Optimize activity's Conditions method to control delivery volume.
- Profiles that exceed the cap take the alternate path defined in the journey.
- The profile cap limit should be increased gradually over time up to the total number of subscribers.

**Terminology:**
- Canonical name: Ramp-up deliveries — Acronym: none — variants: IP warming, IP warmup, delivery ramp-up
- Synonyms: "IP warming" = "IP warmup" = "sender reputation building"
- Do not confuse: "Profile cap" ≠ "audience size limit" (Profile cap is a per-run delivery limit; audience size is the total number of qualified profiles)

**FAQ:**
- **Q: Why do I need to ramp up deliveries when switching to a new IP or domain?** — A new IP or domain has no sending history, so mailbox providers may block or spam-folder messages until a positive reputation is established through gradual, increasing volume.
- **Q: How does the Profile cap condition control delivery volume?** — It sets a maximum number of profiles that can receive the message in a single journey run; profiles beyond that limit take an alternate path instead.
- **Q: When can I remove the Profile cap condition?** — Once the IP is fully warmed up and your sender reputation is established, you can remove the condition from the journey.
- **Q: Can I increase the cap gradually over time?** — Yes; you can update the Limit field in the Profile cap condition to progressively increase the number of recipients per run up to your full subscriber count.

+++
