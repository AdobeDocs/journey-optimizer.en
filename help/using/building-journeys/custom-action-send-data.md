---
solution: Journey Optimizer
product: journey optimizer
title: Send data to AEP
description: Learn how to send data to AEP
feature: Journeys, Use Cases
topic: Content Management
role: User, Developer
level: Intermediate, Experienced
keywords: journey, use case
version: Journey Orchestration
feature_v2: []
subfeature_v2: []
---
# Use case: create a custom action to send data to [!DNL Adobe Experience Platform]{#send-data-to-aep}

If you recently moved to another email service provider, IP address, or email domain or subdomain, establish your reputation as a sender. Otherwise, deliveries might be blocked or moved to recipients' spam folders. For guidance, see the [Deliverability Best Practice Guide](https://experienceleague.adobe.com/docs/deliverability-learn/deliverability-best-practice-guide/additional-resources/generic-resources/increase-reputation-with-ip-warming.html){target="_blank"}.

To warm up your IP, you can gradually ramp up the number of your deliveries. Read more about [optimizing deliverability in Journey Optimizer](../reports/deliverability.md).

The purpose of this use case is to create a journey to ramp up your email deliveries. To configure this journey, follow these steps:

1. Create a journey. [Read more](journey-gs.md).

1. Add an **[!UICONTROL Optimize]** activity to the journey. [Read more](optimize.md).

1. In the **[!UICONTROL Condition]** activity settings, set the maximum number of recipients for your delivery:

   1. In the **[!UICONTROL Optimize]** activity settings, select **[!UICONTROL Conditions]** method and set the **[!UICONTROL Type]** field to **[!UICONTROL Profile cap]**. [Read more](conditions.md#profile_cap).

   1. Set the **[!UICONTROL Limit]** field to the maximum number of recipients for this delivery.

    ![Profile cap condition to control custom action execution volume](assets/profile-cap-condition.png)

      You can gradually increase this limit up to the total number of your subscribers.

1. Add an **[!UICONTROL Email]** action activity to the nominal path after the **[!UICONTROL Condition]** activity.

    ![Journey with custom action for sending data to external system](assets/ramp-up-deliveries-message.png)

    When the journey runs, the message is sent the entering profiles, up to the maximum number of profiles that you have specified. When this limit is reached, the entering profiles take the alternate path.

1. Complete the journey with the activities of your choice.

After your IP has warmed up, you can remove this condition.

+++AI Assistant — Page context

* **TL;DR:** This page walks through a journey-based IP warming use case that gradually ramps up email delivery volume using a Profile cap condition to protect sender reputation.

**Intents:**

* Build an IP warming journey to gradually increase email send volume
* Configure a Profile cap condition to limit the number of recipients per delivery
* Add an Email action activity to the nominal journey path
* Remove the profile cap condition once IP warming is complete

**Glossary:**

* **IP warming**: The process of gradually increasing email send volume from a new IP address to establish sender reputation *(product-specific)*
* **Profile cap**: A condition type in Journey Optimizer that limits the maximum number of profiles that can take a specific journey path *(product-specific)*
* **Nominal path**: The primary branch of a journey that profiles follow when conditions are met *(product-specific)*

**Guardrails:**

* A Profile cap condition must be set on the Condition activity to control delivery volume during IP warming.
* Profiles exceeding the cap limit are routed to the alternate path.
* The journey must be recreated or modified after IP warming is complete to remove the cap condition.

**Terminology:**

* Canonical name: IP warming — Acronym: n/a — variants: IP warm-up, sender reputation warm-up
* Synonyms: "Profile cap" = "recipient limit condition"
* Do not confuse: "IP warming" ≠ "email authentication" (SPF/DKIM/DMARC setup is separate)

**FAQ:**

* **Q: Why do I need to warm up my IP?** — New IP addresses have no sending history, so mailbox providers may block or spam-folder messages until reputation is established.
* **Q: What happens to profiles that exceed the profile cap?** — They take the alternate path defined in the Condition activity.
* **Q: How do I increase the cap over time?** — Edit the Limit field in the Condition activity settings and gradually raise it up to your total subscriber count.
* **Q: When can I remove the profile cap condition?** — Once your IP has sufficient sending history and deliverability metrics are stable, you can remove the condition from the journey.

+++
