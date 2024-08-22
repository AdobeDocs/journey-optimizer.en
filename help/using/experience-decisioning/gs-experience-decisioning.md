---
title: Get started with Experience Decisioning
description: Learn more on Experience decisioning
feature: Experience Decisioning
topic: Integrations
role: User
level: Intermediate
badge: label="Limited Availability"
exl-id: 4c57dbf9-b2a4-42da-8aa3-5a1b3a475a32
---
# Get started with Experience Decisioning {#get-started-experience-decisioning}

>[!AVAILABILITY]
>
>Experience Decisioning is currently only available for a set of organizations (Limited Availability). To gain access, contact your Adobe representative.
>
>For now, the feature is unavailable for customers who have purchased the Adobe **Healthcare Shield** and **Privacy and Security Shield** add-on offerings.

## What is Experience Decisioning {#about}

Experience Decisioning simplifies personalization by offering a centralized catalog of marketing offers known as 'decision items' and a sophisticated decision engine. This engine leverages rules and ranking criteria to select and present the most relevant decision items to each individual.

These decision items are seamlessly integrated into a wide range of inbound surfaces through the [new code-based experience channel](https://experienceleague.adobe.com/en/docs/journey-optimizer/using/code-based-experience/get-started-code-based), now accessible within Journey Optimizer campaigns. Experience Decisioning decision policies are available for use in code-based experience campaigns only.


## Experience Decisioning key steps {#steps}

The main steps to work with Experience Decisioning are as follows:

1. **Assign proper permissions**. Experience Decisioning is only available to users with access to a Experience Decisioning related **[!UICONTROL role]** such as Decision managers. If you cannot access Experience Decisioning, your permissions must be extended.

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

1. **Create decision items** to show to your targeted audience.

1. **Organize with collections**: Use collections to categorize decision items based on attribute-based rules. Incorporate collections into your selection strategies to determine which collection of decision items should be considered.

1. **Create decision rules**: Decision rules are used in decision items and/or selection strategies to determine to whom a decision item can be shown.

1. **Implement ranking methods**: Create ranking methods and apply them within decision strategies to determine the priority order for selecting decision items.

1. **Create selection strategies**: Build selection strategies that leverage collections, decision rules, and ranking methods to identify the decision items suitable for displaying to profiles.

1. **Embed a decision policy into your code-based campaign**: Decision policies combine multiple selection strategies to determine the eligible decision items to display to the intended audience.
