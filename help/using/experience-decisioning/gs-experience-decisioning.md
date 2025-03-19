---
title: Get started with Decisioning
description: Learn more on Decisioning
feature: Decisioning
topic: Integrations
role: User
level: Intermediate
exl-id: 4c57dbf9-b2a4-42da-8aa3-5a1b3a475a32
---
# Get started with Decisioning {#get-started-experience-decisioning}

>[!CONTEXTUALHELP]
>id="ajo_email_enable_experience_decisioning"
>title="What is decisioning?"
>abstract="Decisioning is a new tooling besides Decision management to pick the best items from decision engine and deliver to each individual. It requires additional setup in order to use it."

## What is Decisioning {#about}

Decisioning simplifies personalization by offering a centralized catalog of marketing offers known as 'decision items' and a sophisticated decision engine. This engine leverages rules and ranking criteria to select and present the most relevant decision items to each individual.

These decision items are seamlessly integrated into a wide range of inbound surfaces through the [new code-based experience channel](https://experienceleague.adobe.com/en/docs/journey-optimizer/using/code-based-experience/get-started-code-based), now accessible within Journey Optimizer campaigns.

>[!IMPORTANT]
>
>Decisioning decision policies are available for use in code-based experience campaigns only.

➡️ An end-to-end use case showing how to create decisions and use them in content experiments with the code-based experience channel is presented in [this section](experience-decisioning-uc.md).

## Decisioning key steps {#steps}

The main steps to work with Decisioning are as follows:

1. **Assign proper permissions**. Decisioning is only available to users with access to a Decisioning related **[!UICONTROL role]** such as Decision managers. If you cannot access Decisioning, your permissions must be extended.

    +++Learn how to assign the Decision managers role

    1. To assign a role to a user in the [!DNL Permissions] product, navigate to the **[!UICONTROL Roles]** tab and select Decision managers.

        ![](assets/decision_permission_1.png)

    1. From the **[!UICONTROL Users]** tab, click **[!UICONTROL Add user]**.

        ![](assets/decision_permission_2.png)

    1. Type in your user's name or email address or select the user fom the list and click **[!UICONTROL Save]**.

        If the user was not previously created, refer to the [Add users documentation](https://experienceleague.adobe.com/en/docs/experience-platform/access-control/ui/users).

        ![](assets/decision_permission_3.png)

    Your user should then receive an email redirecting to your instance.

    +++

1. **Configure custom attributes**: Tailor the item catalog to your specific requirements by setting up custom attributes into the catalog's schema.
    
    ➡️ [Learn how to configure the item catalog](catalogs.md)

1. **Create decision items** to show to your targeted audience.

    ➡️ [Learn how to create decisiong items](items.md) ([API documentation](api-reference/decisions-items/create.md))

1. **Organize with collections**: Use collections to categorize decision items based on attribute-based rules. Incorporate collections into your selection strategies to determine which collection of decision items should be considered.

    ➡️ [Learn how to manage item collections](collections.md) ([API documentation](api-reference/items-collections/create.md))

1. **Create decision rules**: Decision rules are used in decision items and/or selection strategies to determine to whom a decision item can be shown.

    ➡️ [Learn how to create decision rules](rules.md)

1. **Implement ranking methods**: Create ranking methods and apply them within decision strategies to determine the priority order for selecting decision items.
    
    ➡️ [Learn how to create ranking methods](ranking.md)

1. **Create selection strategies**: Build selection strategies that leverage collections, decision rules, and ranking methods to identify the decision items suitable for displaying to profiles.

    ➡️ [Learn how to create selection strategies](selection-strategies.md) ([API documentation](api-reference/selection-strategies/create.md))

1. **Create a decision policy and embed it into your code-based campaign**: Decision policies combine multiple selection strategies to determine the eligible decision items to display to the intended audience. 
    
    ➡️ [Learn how to work with decision policies](create-decision.md)
    ➡️ To successfully deliver the offer via the Code-Based channel, follow the implementation steps in [this section](../code-based/code-based-implementation-samples.md)
