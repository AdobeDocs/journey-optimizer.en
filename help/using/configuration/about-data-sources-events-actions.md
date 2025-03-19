---
solution: Journey Optimizer
product: journey optimizer
title: Configure journeys
description: Learn how to configure Data Sources, Events and Actions
feature: Application Settings
topic: Administration
role: Admin
level: Intermediate
keywords: configuration, journey, dashboard, data sources, events, actions
exl-id: c144d44f-031f-4ca2-800e-d3878af400a5
---
# Configure Data Sources, Events & Actions {#configure-journeys}

>[!CONTEXTUALHELP]
>id="ajo_journey_configuration_dashboard"
>title="About journey configuration"
>abstract="In order to send messages with journeys, you need to configure Data Sources, Events and Actions. Data sources allow you to define a connection to a system to retrieve additional information that will be used in your journeys, for example in your conditions. Events allow you to trigger your journeys when an event is received. Custom actions allow you to connect to a third-party system to send your messages. If you are using Journey Optimizer built-in message capabilities you do not need to configure an action."

In order to send messages with journeys, you need to configure **[!UICONTROL Data Sources]**, **[!UICONTROL Events]** and **[!UICONTROL Actions]**.

![](assets/admin-menu.png)

## Data Sources {#data-sources}

The Data Source configuration allows you to define a connection to a system to retrieve additional information that will be used in your journeys. [Learn more](../../using/datasource/about-data-sources.md)

## Events {#events}

Events allow you to trigger your journeys unitarily to send messages, in real-time, to the individual flowing into the journey.

In the event configuration, you configure the events expected in the journeys. The incoming events' data is normalized following Adobe Experience Data Model (XDM). Events come from Streaming Ingestion APIs for authenticated and unauthenticated events (such as Adobe Mobile SDK events). [Learn more](../../using/event/about-events.md)
 
## Actions {#actions}

Journey Optimizer message capabilities are built-in: you only need to add a channel action activity to your journey. If you are using a third-party system to send your messages, you can create a custom action. [Learn more](../../using/action/action.md)

## Browse through Adobe Experience Platform fields {#friendly-names-display}

When defining [event payload](../event/about-creating.md#define-the-payload-fields), [field group payload](../datasource/configure-data-sources.md#define-field-groups) and selecting fields in the [expression editor](../building-journeys/expression/expressionadvanced.md), the display name is displayed in addition to the field name. This information is retrieved from the schema definition in the Experience Data Model.

If descriptors such as "xdm:alternateDisplayInfo" are provided while setting up schemas, the user-friendly names will replace display names. It is especially useful when working with "eVars" and generic fields. You can configure friendly name descriptors via an API call. For more information, see the [Schema Registry developer guide](https://experienceleague.adobe.com/docs/experience-platform/xdm/api/getting-started.html){target="_blank"}.

![](assets/xdm-from-descriptors.png) 

If a friendly name is available, then the field will be displayed as `<friendly-name>(<name>)`. If no friendly name is available, the display name will appear, for example `<display-name>(<name>)`. If none of them are defined, only the technical name of the field will be displayed `<name>`.

>[!NOTE]
>
>Friendly names are not retrieved when you select fields from a union of schemas.
