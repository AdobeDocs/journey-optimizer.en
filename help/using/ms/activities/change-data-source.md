---
solution: Journey Optimizer
product: journey optimizer
title: Use the Change data source activity
description: Learn how to use the Change data source activity
---
# Change data source {#change-data-source}

>[!CONTEXTUALHELP]
>id="acw_orchestration_change_data_source"
>title="Change data source"
>abstract="The **Change data source** activity allows you to select a different data source for the Working table of your multi-step campaign."

The **Change data source** activity is a **targeting** activity. This activity allows you to change the data source used by your multi-step campaign's Working table. This provides more flexibility by allowing you to manage data across your different databases and improve performances.

In multi-step campaigns, data transported from one activity to another through transitions is stored in a temporary **Working table**. By default, Working tables are created in the same database as the source of the processed data. For example, when querying the "Profiles" table, stored on the Cloud database, a Working table is created on the same Cloud database.

In some cases, either data is not available on the current database or is not efficient enough to perform unitary operations. You may therefore need to force the multi-step campaign to use a different database to perform such operations by adding a **[!UICONTROL Change data source]** activity.

Detailed information on Campaign architecture is available in [Campaign v8 (client console) documentation](https://experienceleague.adobe.com/docs/campaign/campaign-v8/config/architecture/architecture.html)

>[!IMPORTANT]
>
>Please note that the **[!UICONTROL Change Dimension]** and **[!UICONTROL Change Data source]** activities should not be added in one row. If you need to use both activities consecutively, make sure you include an **[!UICONTROL Enrichement]** activity in between them. This ensures proper execution and prevents potential conflicts or errors.

<!--

Let's say you want to send to your  VIP customers a unique offer code that they can redeem on your online store. To do this, you need to:

1. Query VIP customers on the "Profiles" table located on the Cloud database,
1. Retrieve an offer code for each targeted profile through API calls,
1. Update each profile with the assigned offer code,
1. Send an email to the profiles with their offer code.

In this situation, it is recommended to execute the offer code assignment operation on the local database, which is better suited for unitary operations. To do this, you need to add a **[!UICONTROL Change data source]** activity before the operation in order to execute it on the Campaign local database.

Before executing the operation, the working table is copied to the local database so that the operation can run there. Once done, the system detects that the profiles that we want to update are on another location. The data is therefore automatically copied back to the Cloud database where the "Profiles" table is located.
-->

## Configure the Change data source activity {#configure}

Follow these steps to configure the **Change dimension** activity:

![](../assets/workflow-change-data-source-add.png)

1. Add a **Change data source** activity to your workmulti-step campaignflow.

1. Define the data source where you want to move the Working table:

   * **[!UICONTROL Default Campaign database (PostgreSQL)]**: Use the default Campaign local database.
   * **[!UICONTROL FDA external account]**: Use external Cloud databases connected to Adobe Campaign through Federated Data Access capability.

      >[!AVAILABILITY]
      >
      >Campaign configuration and connection to external systems are restricted to advanced users and only available from the client console. [Learn more](https://experienceleague.adobe.com/docs/campaign/campaign-v8/connect/fda.html){target="_blank"}

1. Configure your multi-step campaign to perform the desired operations using the new data source.

<!--
## Example {#example}

The workflow belows illustrates the use case detailed earlier, i.e. sending VIP customers offer codes that they can redeem on our online store.

-->
