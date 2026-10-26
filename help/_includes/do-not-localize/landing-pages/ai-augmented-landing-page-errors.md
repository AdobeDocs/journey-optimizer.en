---
title: AI Knowledge Reference
---
# AI Knowledge Reference

+++ AI Knowledge Reference

This section contains structured knowledge intended to support interpretation, retrieval, and question answering related to this topic.

For complete understanding, this information should be combined with the documentation on this page. Neither source is intended to stand alone; the page describes the feature, while this section provides additional context that helps disambiguate terminology, intent, applicability, and constraints.

* **TL;DR:** The page gives the cause and the fix for the errors that [!DNL Adobe Journey Optimizer] returns when you create, validate, publish, delete, or link to a landing page, grouped by feature: permissions and access, publication and status, page URL, name, and content, forms and subscription lists, expiration, and links from messages.

**Intents:**
* Know what to note and whom to contact when an error persists after the listed steps.

* Identify a landing page error from its code: the prefix **CJMMAS**, the error number, and the HTTP status.
* Find which permission or access a landing page action requires when a 403 error is returned.
* Understand why a landing page cannot be published, updated, or deleted in its current status.
* Fix a validation error on the URL, the name, the HTML content, the form, the subscription list, or the expiration of the primary page.
* Fix an error returned when a message or a landing page links to a landing page that is not published, does not exist, or has expired.

**Glossary:**

* **CJMMAS** *(product-specific)*: prefix of the landing page error codes.
* **Error code**: the prefix **CJMMAS**, followed by an error number and an HTTP status, for example **CJMMAS-1070-403**.
* **Primary page**: a page that a landing page must have. The form, the subscription list, and the expiration are configured on it.
* **Subpage**: a page of a landing page other than the primary page, used for example as the page of the **[!UICONTROL Custom page]** expiration action. Do not add forms to subpages.
* **Expiration action**: what happens when the primary page expires, with three options: **[!UICONTROL Redirect URL]**, **[!UICONTROL Custom page]**, or **[!UICONTROL Browser error]**.

**Guardrails:**

* The HTML template of the primary page or of a subpage cannot exceed 1 MB (hard limit): a larger template returns a validation error (**CJMMAS-3400-422** for the primary page, **CJMMAS-3401-422** for a subpage).
* A primary page can have only one form. Do not add forms to subpages.
* A form has one email text box, one confirmation action, and one error action, with the matching inline confirmation and error elements in the HTML. Use each subscription list only once in the form, and give the form fields unique names.
* A published landing page cannot be updated, no subpage can be added to it, and it cannot be deleted. Unpublish it first.
* Each page must have a unique URL: the URL of a page cannot be already used by another published landing page, and two pages cannot have the same URL.
* The expiration date must be in the future.

**Prerequisites and permissions:**

* Landing pages use the permissions of messages. To work with landing pages, your role needs the message permission for the action, added by your administrator:
  * Read (**CJMMAS-1070-403**): **[!DNL View messages]** or **[!DNL Manage messages]**.
  * Write (**CJMMAS-1071-403**) and delete (**CJMMAS-1073-403**): **[!DNL Manage messages]**.
  * Publish (**CJMMAS-1072-403**): **[!DNL Publish messages]**.
* Access to a specific landing page can also be required (**CJMMAS-1078-403**): ask your administrator to add one of the access labels applied to the landing page to your role.

**Terminology:**

* **Canonical name:** Landing page errors

**FAQ:**
* **Q: What do I do if the error persists after the listed steps?** — Note the error code, the message, the request ID, and the campaign, journey, or activity concerned, and keep the logs or screenshots. For a permission or access error, contact your administrator; otherwise contact Adobe Support with these details. For all the support options, see the Getting support section of the error codes reference.

* **Q: What does the prefix CJMMAS mean?** — It is the prefix of the landing page errors, followed by an error number and an HTTP status.
* **Q: Why do I get "You do not have write permission on landing pages"?** — Landing pages use the permissions of messages. Ask your administrator to add the message permission for the action to your role: **[!DNL Manage messages]** for write (**CJMMAS-1071-403**) and delete (**CJMMAS-1073-403**), **[!DNL View messages]** or **[!DNL Manage messages]** for read (**CJMMAS-1070-403**), and **[!DNL Publish messages]** for publish (**CJMMAS-1072-403**).
* **Q: Why can I not update or delete my landing page?** — A published landing page cannot be updated, and a subpage cannot be added to it (**CJMMAS-3002-400**, **CJMMAS-3006-400**, **CJMMAS-3010-400**). It cannot be deleted either (**CJMMAS-3011-400**). Unpublish it, then make the change and publish it again, or delete it. If a message links to it, the link is broken once the page is unpublished.
* **Q: Why does publishing fail with "Unable to publish landing page"?** — For **CJMMAS-3104-400**, the landing page is already published or is being published: check its status, and wait until the publication completes if needed. For **CJMMAS-3012-400**, the landing page is being published: wait until the publication completes, then try again.
* **Q: Why is my URL refused?** — The landing page has no publish URL (**CJMMAS-3101-400**), the primary page has no URL (**CJMMAS-3202-422**), or the subpage has no URL (**CJMMAS-3300-422**): define a URL. The URL of the page is already used by another published landing page (**CJMMAS-3102-400**), or two pages of the landing page have the same URL (**CJMMAS-3103-400**): give each page a unique URL.
* **Q: Why does a message fail because of a landing page link?** — The landing page that you link to is not published (**CJMMAS-1306-400**, **CJMMAS-1309-400**: publish it, then try again), does not exist (**CJMMAS-1307-400** for a message, **CJMMAS-1310-400** for a landing page: select an existing landing page in the link), or has expired (**CJMMAS-1308-400** for a message, **CJMMAS-1311-400** for a landing page: link to a landing page that has not expired, or change its expiration date).

**Troubleshooting:**

* **Permissions and access** (**CJMMAS-1070-403** to **CJMMAS-1073-403**, **CJMMAS-1078-403**): see the prerequisites and the FAQ. For **CJMMAS-1078-403**, "You do not have permission to access this landing page. Please contact your administrator to request access.": ask your administrator to add one of the access labels applied to the landing page to your role.
* **Publication and status**:
    * "Bad request. The landing page is in the process of being published. Please wait until publishing is complete and try again." (**CJMMAS-3012-400**): see the FAQ.
    * "Validation Error in the Landing Page." (**CJMMAS-3107-400**): open the alerts at the top right of the screen, resolve each error, then try again.
    * "No pages found to validate within this landing page." (**CJMMAS-3200-422**) and "No Primary page found." (**CJMMAS-3201-422**): the landing page has no page to validate, or no primary page. Add a primary page to the landing page.
    * "The tags are invalid. The specified tag does not exist or is not applicable on the entity. Please verify the tag and try again." (**CJMMAS-3013-400**): the specified tag does not exist or is not applicable on the entity. Select tags that exist and apply to landing pages.
* **Page URL, name, and content**:
    * No HTML (**CJMMAS-3203-422** for the primary page, **CJMMAS-3301-422** for a subpage): the page has no HTML content. Open the page designer and add the content.
    * "There is no page name for the primary page. Provide a page name and try again." (**CJMMAS-3204-200**) and **CJMMAS-3302-200**: the page has no name. Enter a page name.
* **Forms and subscription lists**:
    * "Multiple forms are present in the primary page ''{pageName}''. Only one form is allowed." (**CJMMAS-3218-422**): keep one **[!UICONTROL Form]** component on the primary page and remove the others. Do not add forms to subpages.
    * The primary page has no form component but a subscription list or a form configuration is still set (**CJMMAS-3223-422**, **CJMMAS-3224-422**): add a form component to the primary page, then remove it, to clear the subscription list (**CJMMAS-3223-422**) or the form configuration (**CJMMAS-3224-422**).
    * The primary page has no subscription list selected (**CJMMAS-3205-422**): in the **[!UICONTROL Form]** component, select the subscription list that the checkbox updates. The subscription list set in it is not valid (**CJMMAS-3220-422**): select a valid subscription list for the primary page.
    * "A subscription list that is not live is present in the primary page ''{pageName}''. Specify a live subscription list." (**CJMMAS-3219-422**): select a live subscription list, or check its start and end dates.
    * "Multiple email text boxes are present in the primary page ''{pageName}''." (**CJMMAS-3225-422**): keep one email text box in the form.
    * A subscription list is associated with the email text box but not with a checkbox or a button (**CJMMAS-3226-422**): in the **[!UICONTROL Form]** component, select the subscription list on a checkbox, or in the button **[!UICONTROL Opt in]** action.
    * Duplicate subscription lists (**CJMMAS-3227-422**): the same subscription list is used more than once in the form. Use each subscription list only once.
    * Duplicate form field names (**CJMMAS-3206-422**): rename the duplicates so that each name is unique.
    * Empty form field names (**CJMMAS-3207-422**): name the unnamed fields.
    * "Multiple Call to Action buttons are present in Primary Page ''{pageName}''." (**CJMMAS-3208-422**): in the **[!UICONTROL Form]** component, keep one button in the **[!UICONTROL Call to action]** section and remove the others.
    * The data error or data confirmation tag is missing in the form (**CJMMAS-3214-422**): add the tag, and make sure the matching inline confirmation and error elements are in the HTML.
    * No confirmation or error action is set (**CJMMAS-3215-422**): set one confirmation action and one error action.
    * More than one confirmation or error action (**CJMMAS-3216-422**): keep one confirmation action and one error action.
    * Inline confirmation and error elements missing in the HTML of the primary page (**CJMMAS-3217-422**): add them to the HTML.
* **Expiration**:
    * Expiration date empty (**CJMMAS-3209-422**): set an expiration date for the primary page.
    * Expiration action empty (**CJMMAS-3210-422**): select the action to run when the page expires: **[!UICONTROL Redirect URL]**, **[!UICONTROL Custom page]**, or **[!UICONTROL Browser error]**.
    * Redirect URL empty (**CJMMAS-3211-422**) or not valid (**CJMMAS-3221-422**): enter a URL, or a valid URL, for the **[!UICONTROL Redirect URL]** action.
    * Subpage empty or not valid (**CJMMAS-3212-422**), or subpage name not valid (**CJMMAS-3000-400**, **CJMMAS-3009-400**): select an existing subpage for the **[!UICONTROL Custom page]** action. Create the subpage first if it does not exist.
    * "The text for the primary page ''{pageName}'' expiration text action is missing. Enter the text." (**CJMMAS-3213-422**): type the error text for the **[!UICONTROL Browser error]** action.
    * "The expiration date selected in the primary page ''{pageName}'' has passed. Select a future date." (**CJMMAS-3222-422**): select a date in the future.
    * "Subpage ''{pageName}'' for expiry action contains contextual attributes of the primary page. Select a different subpage or remove the primary page contextual attributes from it." (**CJMMAS-3303-422**): select another subpage, or remove those attributes from it.
* **Links from messages**: see the FAQ. For an expired landing page, link to a landing page that has not expired, or change its expiration date.

**Related pages:**

* Built-in permissions: Built-in permissions (administration/ootb-permissions.md)
* Access to an object: Object level access control (administration/object-based-access.md)
* Publishing and unpublishing: Manage your landing pages (landing-pages/manage-lp.md)
* Publishing and configuring the primary page and subpages: Create and publish landing pages (landing-pages/create-lp.md)
* Form component: Create the landing page content (landing-pages/lp-content.md)
* Subscription lists: Create a subscription list (landing-pages/subscription-list.md)
* Landing pages guardrails: Landing pages guardrails (start/guardrails.md)
* Other error code prefixes: Error codes reference (building-journeys/error-codes-reference.md)
* Support options when an error persists: Getting support (building-journeys/error-codes-reference.md)
* Contacting Adobe Support: Support ticket guidelines (start/user-interface.md)

+++

<!-- ai-section-version: 1 | source-hash: b3c020a7 -->
