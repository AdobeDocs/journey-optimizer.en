---
solution: Journey Optimizer
product: journey optimizer
title: Global report
description: Learn how to use data from the global report
feature: Reporting
topic: Content Management
role: User
level: Intermediate
exl-id: ec15e700-7659-4dbf-8446-6534ea48c5c8
---
# Get started with Global Report {#global-report}

>[!NOTE]
>
> If custom queries are made through APIs when using Query service, please expect some delay for your reports.

Use the **[!UICONTROL Global report]** to measure the impact of your journeys and deliveries over a selected time period.

* If you want to target a journey or deliveries in the context of a journey, from the **[!UICONTROL Journeys]** menu, access your journey and click the **[!UICONTROL View report]** button. You can then find the Journey, Email, SMS and Push global reports.

    ![](assets/report_journey.png)

* If you want to target a campaign, from the **[!UICONTROL Campaigns]** menu, access your campaign and click the **[!UICONTROL Reports]** button.

    ![](assets/report_campaign.png)

* If you want to switch from the **[!UICONTROL Live report]** to the **[!UICONTROL Global report]** for your delivery, click **[!UICONTROL All time]** from the tab switcher.

    ![](assets/report_5.png)

For a detailed list of every metric available in Adobe Journey Optimizer, refer to [this page](#list-of-components-global)

## Customize dashboard {#modify-dashboard}

Each reporting dashboard can be modified by changing the time period and resizing or removing widgets. Changing the widgets only impacts the current user's dashboard. Other users will see their own dashboards or the ones set by default.

1. From your Global report, select a Start and End time to target specific data.

    ![](assets/report_modify_1.png)

1. For your Journey reports that involve multiple configured **[!UICONTROL Actions]**, choose a specific **[!UICONTROL Action]** from the drop-down menu.

1. If you want to target only one or multiple recurring messages, select it from the **[!UICONTROL Execution time]** drop-down.

    ![](assets/report_modify_12.png)

1. Choose if you want to exclude test events from your reports with the toggle bar. For more information on test events, refer to [this page](../building-journeys/testing-the-journey.md).

    Note that the **[!UICONTROL Exclude test events]** option is only available for Journey reports.

    ![](assets/report_modify_2.png)

1. Click **[!UICONTROL Modify]** to start customizing your dashboard.

    ![](assets/report_modify_3.png)

1. Adjust the widgets size by dragging its bottom-right corner.

    ![](assets/report_modify_4.png)

1. Click **[!UICONTROL Remove]** to remove any widget you don't need.

   ![](assets/report_modify_5.png)

1. Once you are satisfied with the display order and the size of your widgets, click **[!UICONTROL Save]**.

1. To customize the way your data is displayed, you can switch from different visualization options, such as graphs, tables, and donut charts.

   ![](assets/report_modify_10.png)

Your dashboard is now saved. Your different changes will be reapplied for a later use of your live reports. If needed, use the **[!UICONTROL Reset]** option to restore the default widgets and widgets' order.

## Export your reports {#export-reports}

You can easily export your different reports to PDF or CSV formats, which enables you to share or print them. Steps to export reports are detailed in the tabs below.

➡️ [Discover this feature in video](#video-csv)


>[!BEGINTABS]

>[!TAB Export your report as a CSV file]

1. From your report, click **[!UICONTROL Export]** and select **[!UICONTROL CSV file]** to generate a CSV file at overall report-level. 

   ![](assets/export_1.png)

1. You can also choose to export data from a specific widget. Click **[!UICONTROL Export widget data to CSV]** next to the selected widget.

   ![](assets/export_3.png)

1. Your file is automatically downloaded and can be located in your local files.

    If you generated the file at the report level, it contains detailed information for each widget, including its title and data.

    If you generated the file at the widget level, it specifically provides data for the selected widget.

>[!TAB Export your report as a PDF file]

1. From your report, click **[!UICONTROL Export]** and select **[!UICONTROL PDF file]**.

   ![](assets/export_2.png)

1. From the Print window, configure your document as needed. Note that options may vary depending on your browser.

1. Choose to print or save your report as PDF.

1. Locate the folder where you want to save your file, rename it if needed and click Save.

Your report is now available to view or share in a pdf file.



>[!ENDTABS]


### Export reports (video) {#video-csv}

Learn how to download a CSV report for a report and for a single widget in the following how-to video.

>[!VIDEO](https://video.tv.adobe.com/v/3424603?quality=12)



>[!CONTEXTUALHELP]
>id="ajo_report_campaign_ctr"
>title="CTR"
>abstract="CTR widget"

>[!CONTEXTUALHELP]
>id="ajo_report_campaign_clicks"
>title="Clicks"
>abstract="Clicks widget"

>[!CONTEXTUALHELP]
>id="ajo_report_campaign_delivered"
>title="Delivered"
>abstract="Delivered widget"

>[!CONTEXTUALHELP]
>id="ajo_report_campaign_overview"
>title="Campaign overview"
>abstract="Campaign overview widget"

>[!CONTEXTUALHELP]
>id="ajo_report_campaign_funnel"
>title="Campaign funnel results"
>abstract="Campaign funnel results widget"

>[!CONTEXTUALHELP]
>id="ajo_report_campaign_tracking_link"
>title="Tracked link labels"
>abstract="Tracked link labels widget"

>[!CONTEXTUALHELP]
>id="ajo_report_campaign_displays"
>title="Displays"
>abstract="Displays widget"

<!--campaign email-->

>[!CONTEXTUALHELP]
>id="ajo_report_campaign_email_delivered_click"
>title="Delivered & Click trend"
>abstract="Delivered & Click trend widget"

>[!CONTEXTUALHELP]
>id="ajo_report_campaign_email_delivery_status"
>title="Delivery status"
>abstract="Delivery status widget"

>[!CONTEXTUALHELP]
>id="ajo_report_campaign_email_sending_statistics"
>title="Sending statistics"
>abstract="Sending statistics widget"

>[!CONTEXTUALHELP]
>id="ajo_report_campaign_email_tracking_statistics"
>title="Tracking statistics"
>abstract="Tracking statistics widget"

>[!CONTEXTUALHELP]
>id="ajo_report_campaign_email_domains"
>title="Email domains"
>abstract="Email domains widget"

>[!CONTEXTUALHELP]
>id="ajo_report_campaign_email_tracked_link"
>title="Tracked link labels"
>abstract="Tracket link labels widget"

>[!CONTEXTUALHELP]
>id="ajo_report_campaign_email_tracked_link_urls"
>title="Tracked link URLs"
>abstract="Tracked link URLs widget"

>[!CONTEXTUALHELP]
>id="ajo_report_campaign_email_subjects"
>title="Email subjects"
>abstract="Email subjects widget"

>[!CONTEXTUALHELP]
>id="ajo_report_campaign_email_bounce_reasons"
>title="Bounce reasons"
>abstract="Bounce reasons widget"

>[!CONTEXTUALHELP]
>id="ajo_report_campaign_email_exclude"
>title="Exclude reasons"
>abstract="Exclude reasons widget"

>[!CONTEXTUALHELP]
>id="ajo_report_campaign_email_error"
>title="Error reasons"
>abstract="Error reasons widget"


<!--campaign push-->

>[!CONTEXTUALHELP]
>id="ajo_report_campaign_push_sending_statistics"
>title="Sending statistics"
>abstract="Sending statistics widget"

>[!CONTEXTUALHELP]
>id="ajo_report_campaign_push_tracking_statistics"
>title="Tracking statistics"
>abstract="Tracking statistics widget"

>[!CONTEXTUALHELP]
>id="ajo_report_campaign_push_tracked_link"
>title="Tracked link labels"
>abstract="Tracket link labels widget"

>[!CONTEXTUALHELP]
>id="ajo_report_campaign_push_tracked_link_urls"
>title="Tracked link URLs"
>abstract="Tracked link URLs widget"

>[!CONTEXTUALHELP]
>id="ajo_report_campaign_push_bounce_reasons"
>title="Bounce reasons"
>abstract="Bounce reasons widget"

>[!CONTEXTUALHELP]
>id="ajo_report_campaign_push_exclude"
>title="Excluded reasons"
>abstract="Excluded reasons widget"

>[!CONTEXTUALHELP]
>id="ajo_report_campaign_push_email_error"
>title="Error reasons"
>abstract="Error reasons widget"

<!--campaign inapp-->


>[!CONTEXTUALHELP]
>id="ajo_report_campaign_inapp_impression"
>title="Impression & Click trend"
>abstract="Impression & Click trend widget"

>[!CONTEXTUALHELP]
>id="ajo_report_campaign_inapp_clicks"
>title="Clicks"
>abstract="Clicks widget"

>[!CONTEXTUALHELP]
>id="ajo_report_campaign_inapp_displays"
>title="Displays"
>abstract="Displays widget"

>[!CONTEXTUALHELP]
>id="ajo_report_campaign_inapp_tracking_data"
>title="Tracking data"
>abstract="Tracking data widget"

>[!CONTEXTUALHELP]
>id="ajo_report_campaign_inapp_tracked_link"
>title="Tracked link labels"
>abstract="Tracked link labels widget"

>[!CONTEXTUALHELP]
>id="ajo_report_campaign_inapp_tracked_link_urls"
>title="Tracked link URLs"
>abstract="Tracked link URLs widget"

<!--campaign sms-->


>[!CONTEXTUALHELP]
>id="ajo_report_campaign_sms_delivered_click"
>title="Delivered & Click trend"
>abstract="Delivered & Click trend widget"

>[!CONTEXTUALHELP]
>id="ajo_report_campaign_sms_delivery_status"
>title="Delivery status"
>abstract="Delivery status widget"

>[!CONTEXTUALHELP]
>id="ajo_report_campaign_sms_tracked_link"
>title="Tracked link labels"
>abstract="Tracket link labels widget"

>[!CONTEXTUALHELP]
>id="ajo_report_campaign_sms_tracked_link_urls"
>title="Tracked link URLs"
>abstract="Tracked link URLs widget"

>[!CONTEXTUALHELP]
>id="ajo_report_campaign_sms_inbound"
>title="SMS inbound message"
>abstract="SMS inbound message widget"

>[!CONTEXTUALHELP]
>id="ajo_report_campaign_sms_message_type"
>title="SMS message type"
>abstract="SMS message type widget"

>[!CONTEXTUALHELP]
>id="ajo_report_campaign_sms_providers"
>title="SMS providers"
>abstract="SMS providers widget"

>[!CONTEXTUALHELP]
>id="ajo_report_campaign_sms_bounce"
>title="Bounce reasons"
>abstract="Bounce reasons widget"

>[!CONTEXTUALHELP]
>id="ajo_report_campaign_sms_exclude"
>title="Exclude reasons"
>abstract="Exclude reasons widget"

>[!CONTEXTUALHELP]
>id="ajo_report_campaign_sms_error"
>title="Error reasons"
>abstract="Error reasons widget"
