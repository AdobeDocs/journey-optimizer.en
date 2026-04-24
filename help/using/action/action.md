---
solution: Journey Optimizer
product: journey optimizer
title: Get started with actions
description: Learn how to work with actions
feature: Journeys, Actions, Custom Actions
topic: Administration
role: Developer, Admin
level: Experienced
keywords: actions, journey, messages, sending, connections
exl-id: 7f0cda1d-daf0-4d4c-9978-ddef81473813
TQID: https://experienceleague.adobe.com/u-fLClLKK9cC7D2BwO5vxdW11tywPDRWzOMBtYUj5Ts
product_v2:
  - id: cb954087-f4fc-4456-afb9-e939cabcdc79
    internal-label: Journey Optimizer
feature_v2:
  - id: b3538224-471e-4c63-a444-9b19d89ae29c
    internal-label: Activities
  - id: bb359667-ec7d-4d4b-8663-5850fc219d32
    internal-label: Administration
  - id: d556b755-390a-43f0-be32-a08cf6236126
    internal-label: Configuration
  - id: d998adac-2f81-400b-a669-d07bb196e4eb
    internal-label: Journeys
  - id: fe338112-e2ce-4876-8989-fc4d497613f1
    internal-label: Email
subfeature_v2:
  - id: c2beecbb-b93e-4ae3-baa9-72adcdc06781
    internal-label: Action configuration
  - id: cfba2953-2ce9-4b00-a00c-71cd338ae63f
    internal-label: Custom actions
  - id: e30b0a1a-b594-47b8-af94-1e3a2be6df11
    internal-label: Get started
role_v2:
  - id: c66ffd68-0f65-42bb-aa23-b4020f12e0bd
    internal-label: Admin
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
topic_v2:
  - id: c1579802-ddd4-4214-8a91-97b2066abe11
    internal-label: Troubleshooting
  - id: eddd9b14-83bd-4ff4-9072-54a4a484abb7
    internal-label: Administration
---
# Get started with custom actions {#about_actions}

>[!CONTEXTUALHELP]
>id="ajo_journey_action_list"
>title="Custom actions"
>abstract="Actions are connections through which you deliver personalized, real-time experiences to customers such as push notifications, email, SMS, or any other means of digital engagement you use in your business."

Actions are connections through which you deliver personalized, real-time experiences to customers such as push notifications, email, SMS, or any other means of digital engagement you use in your business.

➡️ [Discover this feature in video](#video)

[!DNL Journey Optimizer] comes with built-in message capability. Custom actions enable you to configure connection of a third-party system to send messages or API calls. An action can be configured with any service from any provider that can be called through a REST API with a JSON-formatted payload.

* If you are using Adobe Campaign v7 or v8, an integration is available upon request. Refer to [this page](../action/acc-action.md).

* If you are using a third-party system to send messages such as Epsilon, Facebook, Adobe Developer, Firebase, etc, you need to create and configure a custom action. Refer to [this page](../action/about-custom-action-configuration.md).

>[!CAUTION]
>
>The configuration of custom actions must be performed by a **technical user**.

Custom actions are additional actions defined by technical users and made available to marketers: once configured, they appear in the left palette of your journey, in the **[!UICONTROL Action]** category. Learn more on [this page](../building-journeys/about-journey-activities.md#action-activities). 

To view the action list or configure a new action, select **[!UICONTROL Configurations]** in the ADMINISTRATION menu section. In the  **[!UICONTROL Actions]** section, click **[!UICONTROL Manage]**. The list of actions is displayed. See [this page](../start/user-interface.md) for more information on the interface.

![](assets/custom1.png)

Learn how to troubleshoot a custom action [on this dedicated page](../action/troubleshoot-custom-action.md).

## How-to video {#video}

Learn how to configure custom actions.

>[!VIDEO](https://video.tv.adobe.com/v/3428396?quality=12)

## Additional resources

Browse the sections below to learn more about configuring and using your custom actions:

* [Configure your custom actions](../action/about-custom-action-configuration.md) - Learn how to create and configure a custom action
* [Use custom actions](../building-journeys/using-custom-actions.md) - Learn how to use custom actions in your journeys
* [Pass collections into custom action parameters](../building-journeys/collections.md) - Learn how to pass a collection in custom action parameters that is dynamically populated at runtime
* [Custom action troubleshooting](../action/troubleshoot-custom-action.md) - Learn how to troubleshoot a custom action

