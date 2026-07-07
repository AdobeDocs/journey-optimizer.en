---
solution: Journey Optimizer
product: journey optimizer
title: View SMS usage metrics
description: Learn how to generate SMS usage reports to reconcile messaging volume with vendor billing in Journey Optimizer.
feature: SMS, Channel Configuration
role: Admin
level: Intermediate
---
# Generate SMS usage report {#sms-usage-report}

>[!CONTEXTUALHELP]
>id="ajo_admin_sms_usage_metrics"
>title="SMS usage metrics"
>abstract="Generate SMS usage reports to reconcile messaging volume with vendor billing. Reports list mobile-terminated (MT) and mobile-originated (MO) counts for each short code or phone number, aggregated by day."

>[!BEGINSHADEBOX]

**On this page:** Generate SMS usage reports in Adobe Journey Optimizer to reconcile mobile-terminated (MT) and mobile-originated (MO) volume with vendor billing, using a Sinch MMS API credential and downloadable CSV output.

>[!ENDSHADEBOX]

SMS usage metrics are available when you purchase SMS through Adobe Journey Optimizer. Reports summarize send and receive traffic by short code or phone number, aggregated by day, for the last **90 days**.

To view usage metrics, an administrator must:

1. [Create a Sinch MMS API credential](mobile-configuration-sinch.md#sinch-mms) used only to retrieve usage data from Sinch.

    Usage reports require an API credential with **[!UICONTROL SMS vendor]** set to **Sinch MMS**. This credential connects Journey Optimizer to Sinch so usage data can be retrieved. It is separate from Sinch credentials used to send SMS or MMS messages, although the field values come from the same Sinch project.

1. [Configure and retrieve an SMS usage report](#configure-sms-usage-report).

These steps require the **[!UICONTROL Manage SMS settings]** permission. [Learn more about permissions](../administration/high-low-permissions.md#administration-permissions).

## Configure and view SMS usage reports {#configure-sms-usage-report}

>[!CONTEXTUALHELP]
>id="ajo_admin_sms_usage_report_name"
>title="Report name"
>abstract="Enter a label that helps you recognize this report in the list later, for example, May 2026 billing review."

>[!CONTEXTUALHELP]
>id="ajo_admin_sms_usage_credential"
>title="SMS credentials"
>abstract="Select the Sinch API credential whose send and receive traffic should appear in this report. To add or update credentials, go to **Administration** > **Channels** > **API credentials**, then choose **SMS Vendor** > **Sinch MMS**."

>[!CONTEXTUALHELP]
>id="ajo_admin_sms_usage_start_date"
>title="Start date"
>abstract="First day of the date range to include in the report. Usage data is available only for the last 90 days."

The SMS usage reports present mobile-originated (MO) and mobile-terminated (MT) volume by short code to support reconciliation between vendor billing and messaging activity in Journey Optimizer. 

1. In the left rail, browse to **[!UICONTROL Administration]** > **[!UICONTROL Channels]** > **[!UICONTROL SMS Settings]**. 

1. Access the **[!UICONTROL View SMS usage metrics]** menu, then, click **[!UICONTROL Configure new report]**.

    ![](assets/usage_report_1.png)
  
1. Configure the report:

    * **[!UICONTROL Report name]**: enter a label that helps you recognize your report.
    * **[!UICONTROL SMS credentials]**: select the **Sinch MMS** API credential you previously created for your SMS usage reporting.
    * **[!UICONTROL Start date]** and **[!UICONTROL End date]**: set the date range for the report. Usage data is available only for the last 90 days.

      ![](assets/usage_report_2.png)

1. Click **[!UICONTROL Configure report]** to submit the request. 

1. On the **[!UICONTROL Submitted reports]** list, find the report you configured and click **[!UICONTROL Retrieve report]**. 

    The status changes to **Pending** while the report is generated.

1. Once your report status is updated to **[!UICONTROL Ready]**, click **[!UICONTROL View]** to open the report. The report includes:

    * **Usage summary**: total mobile-originated (MO) and mobile-terminated (MT) messages for the selected dates, broken down by short code.

    * **Daily SMS volume**: SMS volume by day, broken down by short code.

      ![](assets/usage_report_3.png)

1. To export the report, click **[!UICONTROL Download CSV]**. Journey Optimizer downloads a CSV file for the report you are viewing.
