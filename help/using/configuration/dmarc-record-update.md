---
solution: Journey Optimizer
product: journey optimizer
title: Comply with new DMARC requirement
description: Learn why and when you must set DMARC record in Journey Optimizer
feature: Subdomains, Channel Configuration, Deliverability
topic: Administration
role: Admin
level: Experienced
keywords: subdomain, domain, mail, dmarc, record
exl-id: 15b10a61-6ecd-4ffa-b1c2-21e862263f6d
---
# Comply with new DMARC requirement {#dmarc-record-update}

>[!CONTEXTUALHELP]
>id="ajo_admin_dmarc_banner_link"
>title="Learn more on mandatory DMARC update"
>abstract="As part of their enforcing industry best practices, Google and Yahoo are both requiring that you have a **DMARC record** for any domain you use to send email to them, starting on **February 1st, 2024**.<br>Consequently, you must make sure that you have DMARC record set up for all the subdomains that you have delegated to Adobe in Journey Optimizer."

Domain-based Message Authentication, Reporting, and Conformance (DMARC) is an email authentication method that allows domain owners to protect their domain from unauthorized use. By offering a clear policy to email providers/ISPs, it helps prevent malicious actors from sending emails claiming to be from your domain. Implementing DMARC reduces the risk of legitimate emails being marked as spam or rejected, and improve your email deliverability.

As part of their enforcing industry best practices, Google and Yahoo! are both requiring a **DMARC record** for any domain you use to send email to them. This new requirement applies starting **February 1st, 2024**.

>[!CAUTION]
>
>Failing to comply with this new requirement from Gmail and Yahoo! is expected to result in emails landing into the spam folder or getting blocked.

Consequently, Adobe strongly recommends you ensure that you have DMARC record set up for all the subdomains that you have delegated to Adobe in [!DNL Journey Optimizer]. Follow the steps below that apply to your case:

* If you have [fully delegated](delegate-subdomain.md#full-subdomain-delegation) your sending subdomains to Adobe, follow one of the options below:

    * Set up DMARC on the parent domain of your delegated subdomains **in your hosting solution**.
        or
    * Set up DMARC on your delegated subdomains **in the [!DNL Journey Optimizer]** configuration user interface - with no extra work on your hosting solution. [Learn how](dmarc-record.md#implement-dmarc)

* If you have set up your sending subdomains with [CNAME](delegate-subdomain.md#cname-subdomain-delegation), follow one of the options below:

    * Set up DMARC on your subdomains or on the parent domain of your subdomains **in your hosting solution**.
        or
    * Set up DMARC on your delegated subdomains **in the [!DNL Journey Optimizer]** configuration user interface. [Learn how](dmarc-record.md#implement-dmarc)
    
    >[!IMPORTANT]
    >
    >However, the CNAME set up also requires some additional entry in your hosting solution. Consequently, make sure you coordinate with your IT department so that they can perform the update detailed in [this section](dmarc-record.md#implement-dmarc).

The most recent timelines shared by Google and Yahoo! are as follows:

* Google:

    * **February 2024** – Temporary bounces designed to provide warning of non-compliance will begin. Emails will still be delivered as normal after a short delay if you are not yet in compliance. If you are fully in compliance there will be no temporary bounces and you will not be affected.

    * **April 2024** – Blocks will begin for senders who are not in compliance with DMARC requirement. Only a portion of non-compliant email will be blocked at first, with the percentage blocked increasing over time.

    * **June 1st, 2024** – Any sender not in full compliance will experience blocking.

* Yahoo! has not provided exact dates, but has said "the rollout of enforcement will begin in February 2024. Enforcement will be gradually rolled out".

>[!NOTE]
>
>If you have any questions or need support, contact your Adobe Deliverability Consultant or your Adobe representative.

**Useful links**

* Learn more about DMARC in the [Deliverability Best Practice Guide](https://experienceleague.adobe.com/docs/deliverability-learn/deliverability-best-practice-guide/additional-resources/technotes/implement-dmarc.html#about){target="_blank"}
* Read out the [Google Gmail announcement](https://blog.google/products/gmail/gmail-security-authentication-spam-protection/){target="_blank"}
* Read out the [Yahoo! announcement](https://blog.postmaster.yahooinc.com/post/730172167494483968/more-secure-less-spam){target="_blank"}

<!--Find more guidance about these changes in the [Deliverability Best Practice Guide]-->
