---
solution: Journey Optimizer
product: journey optimizer
title: Use the Reconciliation activity
description: Learn how to use the Reconciliation activity in an orchestrated campaign
badge: label="Alpha"
hide: yes
hidefromtoc: yes
exl-id: 0d5cfffe-bc6c-40bc-b3e1-5b44368ac76f
---
# Reconciliation {#reconciliation}

>[!CONTEXTUALHELP]
>id="ajo_orchestration_reconciliation"
>title="Reconciliation activity"
>abstract="The **Reconciliation** activity is a **Targeting** activity which allows you to define the link between Adobe Journey Optimizer and the data in a work table." 

>[!CONTEXTUALHELP]
>id="ajo_orchestration_reconciliation_field"
>title="Reconciliation select field"
>abstract="Reconciliation select field" 

>[!CONTEXTUALHELP]
>id="ajo_orchestration_reconciliation_condition"
>title="Reconciliation create condition"
>abstract="Reconciliation create condition" 

>[!CONTEXTUALHELP]
>id="ajo_orchestration_reconciliation_complement"
>title="Reconciliation generate complement"
>abstract="Reconciliation generate complement" 

+++ Table of Contents

| Welcome to orchestrated campaigns | Launch your first orchestrated campaign | Query the database | Ochestrated campaigns activities|
|---|---|---|---|
|[Get started with orchestrated campaigns](../gs-orchestrated-campaigns.md)<br/><br/>[Configuration steps](../configuration-steps.md)<br/><br/>[Key steps for orchestrated campaign creation](../gs-campaign-creation.md)|[Create an orchestrated campaign](../create-orchestrated-campaign.md)<br/><br/>[Orchestrate activities](../orchestrate-activities.md)<br/><br/>[Send messages with orchestrated campaigns](../send-messages.md)<br/><br/>[Start and monitor the campaign](../start-monitor-campaigns.md)<br/><br/>[Reporting](../reporting-campaigns.md)|[Work with the Query Modeler](../orchestrated-rule-builder.md)<br/><br/>[Build your first query](../build-query.md)<br/><br/>[Edit expressions](../edit-expressions.md)|[Get started with activities](about-activities.md)<br/><br/>Activities:<br/>[And-join](and-join.md) - [Build audience](build-audience.md) - [Change dimension](change-dimension.md) - [Combine](combine.md) - [Deduplication](deduplication.md) - [Enrichment](enrichment.md) - [Fork](fork.md) - [Reconciliation](reconciliation.md) - [Split](split.md) -  [Wait](wait.md)|

{style="table-layout:fixed"}

+++

<br/>

The **[!UICONTROL Reconciliation]** activity is a **[!UICONTROL Targeting]** activity which allows you to define the link between the data in Adobe Journey Optimizer and the data in a work table, for example data loaded from an external file.

The **[!UICONTROL Enrichment]** activity lets you add additional data to your orchestrated campaign, for example, by combining data from multiple sources or linking to a temporary resource. In contrast, the **[!UICONTROL Reconciliation]** activity is used to match unidentified or external data with existing resources in the database.

**[!UICONTROL Reconciliation]** requires that the related records already exist in the system. For instance, if you import a purchase file listing products, timestamps, and customer information, both the products and customers must already be present in the database to establish the link.

## Configure the Reconciliation activity {#reconciliation-configuration}

>[!CONTEXTUALHELP]
>id="ajo_orchestration_reconciliation_targeting"
>title="Targeting dimension"
>abstract="Select the new targeting dimension. A dimension lets you define the targeted population: recipients, app subscribers, operators, subscribers, etc. By default, the current targeting dimension is selected." 

>[!CONTEXTUALHELP]
>id="ajo_orchestration_reconciliation_rules"
>title="Reconciliation rules"
>abstract="Select reconciliation rules to use for the deduplication. To use attributes, select the **Simple attributes** option and choose the source and destination fields. To create your own reconciliation condition using the query modeler, select the **Advanced reconciliation conditions** option."
>additional-url="https://experienceleague.adobe.com/en/docs/campaign-web/v8/query-database/query-modeler-overview" text="Work with the query modeler"

>[!CONTEXTUALHELP]
>id="ajo_orchestration_reconciliation_targeting_selection"
>title="Select the targeting dimension"
>abstract="Select the targeting dimension for your inbound data to reconcile with." 
>additional-url="https://experienceleague.adobe.com/docs/campaign-web/v8/audiences/gs-audiences-recipients.html#targeting-dimensions" text="Targeting dimensions"

>[!CONTEXTUALHELP]
>id="ajo_orchestration_keep_unreconciled_data"
>title="Keep unreconciled data"
>abstract="By default, non reconciled data are kept in the outbound transition and available in the worktable for future use. To remove unreconciled data, desactivate the **Keep unreconciled data** option." 

>[!CONTEXTUALHELP]
>id="ajo_orchestration_reconciliation_attribute"
>title="Reconciliation attribute"
>abstract="Select the attribute to use to reconciliate data, and click Confirm." 

Follow these steps to configure the **[!UICONTROL Reconciliation]** activity:

1. Add a **[!UICONTROL Reconciliation]** activity to your workflow.

1. Choose a new targeting dimension to define who you are targeting such as recipients or subscribers.

1. Set the field(s) to use for matching your incoming data with existing profiles.

1. To match data using basic fields, select **[!UICONTROL Simple attributes]**.

1. Set the matching fields:

    * **[!UICONTROL Source]**: lists the incoming data fields.

    * **[!UICONTROL Destination]**: refers to fields in the selected targeting dimension.

    A match occurs when both values are equal, for example, matching by **[!UICONTROL Email]** to identify profiles.

    ![](../assets/workflow-reconciliation-criteria.png)

1. To add more matching rules, click **[!UICONTROL Add rule]**. All conditions must be met for a match to occur.

1. For more complex conditions, choose **[!UICONTROL Advanced reconciliation conditions]**. Use the [query modeler](../orchestrated-rule-builder.md) to define custom logic.

1. To filter which data to reconcile, click **[!UICONTROL Create filter]** and define your condition in the query modeler.

1. By default, unmatched records are kept in the outbound transition and stored in the worktable. To remove these, enable the **[!UICONTROL Keep unreconciled data]** option.

## Example {#example-reconciliation}

This example uses the **[!UICONTROL Reconciliation]** activity in Adobe Journey Optimizer to ensure that emails are sent only to recognized customers. The data flows in through a **[!UICONTROL Read Audience]** activity that targets users with previous orders. The **[!UICONTROL Reconciliation]** activity then matches this incoming data to existing profiles in the database using the email field.

![](../assets/workflow-reconciliation-sample-1.0.png)
