---
solution: Journey Optimizer
product: journey optimizer
title: Dynamic media
description: Use Dynamic media with Journey Optimizer
topic: Content Management
role: User
level: Beginner
hide: yes
hidefromtoc: yes
exl-id: 4c1d39c4-3154-4bec-ac3c-c2ead7164d69
---
# Insert countdown timer {#countdown}

Create urgency and maximize conversions with Dynamic Media countdown timers that update in real-time when recipients open your emails. This feature is ideal for flash sales, limited-time offers, and time-sensitive promotions.

For example, as a marketer for a retail brand, you're running a 48-hour flash sale. By using the countdown timer in your promotional emails:

* Recipients who open immediately see "47 hours remaining"
* Recipients who open 24 hours later see "23 hours remaining"  
* Recipients who open after the sale ends see "Sale ended"

For more information on how to create your Dynamic Media in Adobe Experience manager, refer [to this document](assets/do-not-localize/countdown.pdf).


1. In **[!DNL Adobe Experience Manager]**, create a Dynamic Media template and add a countdown timer component to it.

    ![](assets/timer-1.png)

1. In **[!DNL Journey Optimizer]**, create a new campaign or open an existing one, then access the Email Designer.

1. Drag and drop an **[!UICONTROL HTML component]** into your email content.

1. Select **[!UICONTROL Show the source code]** to edit the HTML directly.

    ![](assets/timer-2.png)

1. From the **[!UICONTROL Edit HTML]** menu, navigate to **[!UICONTROL Assets]** and click **[!UICONTROL Open asset selector]** to browse and select your published Dynamic Media template.

    ![](assets/timer-3.png)

1. In the **[!UICONTROL Custom attributes]** menu, configure any customizable URL parameters as needed for your template.

    Click **[!UICONTROL Save]** when finished.

    ![](assets/timer-4.png)

1. Select the asset in the Email Designer, then access the **[!UICONTROL Styles]** menu.

    Configure the following settings:
    * **Banner text**: The text displayed with your timer
    * **End time**: The date and time when the countdown expires. Enter the time in GMT (Greenwich Mean Time) only. The system does not accept other time zones.
    * **Fallback text**: The message shown after the timer ends

    ![](assets/timer-5.png)

1. Click **[!UICONTROL Preview]** to view the timer with real-time countdown updates and verify your configuration.

When recipients open the email, they see the accurate time remaining for your flash sale. If they reopen the email later, the countdown automatically updates to reflect the current time remaining. After the end date, the default message appears automatically.
