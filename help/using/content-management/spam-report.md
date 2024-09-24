---
title: Use email spam report
description: Learn how to use the email spam report.
feature: Preview
role: User
level: Beginner
exl-id: 9ab43b14-41cf-49f1-bdcf-6fee58db5000
---
# Email spam report {#spam-report}

>[!CONTEXTUALHELP]
>id="ajo_simulate_spam_report"
>title="Email spam report"
>abstract="The Spam report lets you check your email content spam scoring. This score indicates if ISPs or Mailbox providers will consider your message as a spam or not. The lower the score, the better. If your email content score is above 2, you should consider fixing issues which are causing tests to fail."

You can check your email content spam scoring in a dedicated Spam report. Using [SpamAssassin](https://spamassassin.apache.org/){target="_blank"}, Adobe Journey Optimizer can test your email content and give it a score to indicate if ISPs or Mailbox providers will consider it as a spam or not.

When editing or previewing your email content, the **[!UICONTROL Spam report]** button provides a scoring and advice to improve scores for each individual item that is listed.

This capability allows you to determine whether a message could be considered as spam by the anti-spam tools used upon receipt, and to take actions if this is the case. Many email inbox providers use tools as part of their spam filtering process. Sending emails with a bad score can severely impact your deliverability.

To access the **[!UICONTROL Spam report]**, follow the steps below.

1. From the **[!UICONTROL Simulate]** screen, click the **[!UICONTROL Spam report]** button.

    ![](assets/spam-report-button.png)

<!--
    You can also open the [Email Designer](../email/content-from-scratch.md), click the **[!UICONTROL More]** button and select **[!UICONTROL Check spam score]** from the menu.

    ![](assets/spam-report-check-score.png)
-->

1. An anti-spam checking is automatically performed and the **[!UICONTROL Spam report]** window displays the results. It shows how your content is doing in terms of body layout, structure, image size, spam trigger words if any, etc.

    ![](assets/spam-report-high-score.png)

1. Check the scores and descriptions for each item.

    The lower the score, the better. If the score is higher than 5, a warning is displayed: it indicates that some messages may be blocked or marked as spam when received. Best practice is to have a score lower than 2.

    >[!NOTE]
    >
    >Spam score is derived via [SpamAssassin](https://spamassassin.apache.org/){target="_blank"}, and rules are not owned by Adobe. For more details about these rules, refer to the SpamAssassin documentation.
    >

1. Based on that scoring, if you consider that some elements can be improved, edit your content in the [Email Designer](../email/content-from-scratch.md) and make the necessary updates.

1. Once your changes are done, browse back to the **[!UICONTROL Spam report]** screen to ensure your score has improved.

    ![](assets/spam-report-low-score.png)

<!--You can also check the message's alerts for warnings on potential risk of spam detection. Follow the steps below.

1. Click the **[!UICONTROL Alerts]** button on top right of the screen. [Learn more on email alerts](../email/create-email.md#check-email-alerts)

1. If **[!UICONTROL Spam checker alert]** is displayed, you should check your content for a potential risk of spam using the **[!UICONTROL Spam report]** feature as detailed above.

    ![](assets/spam-report-alert.png)
-->
