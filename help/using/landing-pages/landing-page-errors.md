---
solution: Journey Optimizer
product: journey optimizer
title: Landing page errors
description: Learn what common errors mean when you create, validate, publish, and link landing pages in Adobe Journey Optimizer, and how to fix them
feature: Landing Pages, Subscriptions
topic: Content Management
role: User
level: Intermediate
keywords: error, troubleshooting, landing page, form, subscription list, publish
---
# Landing page errors {#landing-page-errors}

>[!BEGINSHADEBOX]

**On this page:** Find the cause and the fix for the errors that [!DNL Adobe Journey Optimizer] returns when you create, validate, publish, delete, or link to a landing page, grouped by feature.

>[!ENDSHADEBOX]

Landing page errors use the prefix **CJMMAS**, followed by an error number and an HTTP status. For the other error code prefixes, see the [error codes reference](../building-journeys/error-codes-reference.md).

If the error persists after you follow the steps, note the error code, the message, the request ID, and the campaign, journey, or activity concerned, and keep the logs or screenshots. Then contact your administrator for a permission or access error, or [contact Adobe Support](../start/user-interface.md#support-ticket-guidelines) with these details. For all the support options, see [Getting support](../building-journeys/error-codes-reference.md#getting-support).

## Permissions and access {#access}

These errors occur when your user does not have the permission or the access needed to work with landing pages.

See also [Built-in permissions](../administration/ootb-permissions.md).

| Error code | Message | How to fix |
|---|---|---|
| **CJMMAS-1070-403** | You do not have read permission on landing pages. Landing pages require the message level permission. | Ask your administrator to add the **[!DNL View messages]** or **[!DNL Manage messages]** permission to your role, as landing pages use the message permissions. [Learn more](../administration/ootb-permissions.md) |
| **CJMMAS-1071-403** | You do not have write permission on landing pages. Landing pages require the message level permission. | Ask your administrator to add the **[!DNL Manage messages]** permission to your role, as landing pages use the message permissions. [Learn more](../administration/ootb-permissions.md) |
| **CJMMAS-1072-403** | You do not have publish permission on landing pages. Landing pages require the message level permission. | Ask your administrator to add the **[!DNL Publish messages]** permission to your role, as landing pages use the message permissions. [Learn more](../administration/ootb-permissions.md) |
| **CJMMAS-1073-403** | You do not have delete permission on landing pages. Landing pages require the message level permission. | Ask your administrator to add the **[!DNL Manage messages]** permission to your role, as landing pages use the message permissions. [Learn more](../administration/ootb-permissions.md) |
| **CJMMAS-1078-403** | You do not have permission to access this landing page. Please contact your administrator to request access. | Ask your administrator to add one of the access labels applied to the landing page to your role. [Learn more](../administration/object-based-access.md) |

## Publication and status {#publication}

These errors occur when you publish, edit, or delete a landing page, and the status of the landing page does not allow it.

See also [Manage your landing pages](manage-lp.md).

| Error code | Message | How to fix |
|---|---|---|
| **CJMMAS-3012-400** | Bad request. The landing page is in the process of being published. Please wait until publishing is complete and try again. | Wait until the publication completes, then try again. [Learn more](create-lp.md#publish-landing-page) |
| **CJMMAS-3104-400** | Unable to publish landing page. The landing page is already published or is in publishing state. | Check the status of the landing page, and wait until the publication completes if it is being published. [Learn more](create-lp.md#publish-landing-page) |
| **CJMMAS-3002-400** | Updation of Published Landing Page is not permitted. | Unpublish the landing page, make the change, then publish it again. [Learn more](manage-lp.md) |
| **CJMMAS-3006-400** | Bad request. Updating a published landing page is not permitted. | Unpublish the landing page, make the change, then publish it again. [Learn more](manage-lp.md) |
| **CJMMAS-3010-400** | Bad Request. Cannot create subpage for a published landing page. | Unpublish the landing page, add the subpage, then publish it again. [Learn more](manage-lp.md) |
| **CJMMAS-3011-400** | Bad request. A published landing page cannot be deleted. Please unpublish the landing page before deleting. | Unpublish the landing page first, then delete it. Links to it from messages are broken once it is unpublished. [Learn more](manage-lp.md) |
| **CJMMAS-3107-400** | Validation Error in the Landing Page. | Open the alerts at the top right of the screen, resolve each error, then try again. [Learn more](create-lp.md#check-alerts) |
| **CJMMAS-3200-422** | No pages found to validate within this landing page. | Add a primary page to the landing page. [Learn more](create-lp.md#configure-primary-page) |
| **CJMMAS-3201-422** | No Primary page found. | Add a primary page to the landing page. [Learn more](create-lp.md#configure-primary-page) |
| **CJMMAS-3013-400** | The tags are invalid. The specified tag does not exist or is not applicable on the entity. Please verify the tag and try again. | Select tags that exist and apply to landing pages. [Learn more](../start/search-filter-categorize.md#tags) |

## Page URL, name, and content {#url}

These errors occur when a page does not have a URL, a name, or content, or when its URL is already used.

See also [Create and publish landing pages](create-lp.md).

| Error code | Message | How to fix |
|---|---|---|
| **CJMMAS-3101-400** | Landing page publish URL is not present. | Define a publish URL for the landing page. [Learn more](create-lp.md#configure-primary-page) |
| **CJMMAS-3202-422** | The URL is empty in the primary page ''{pageName}''. Provide a URL and try again. | Define a URL for the primary page. [Learn more](create-lp.md#configure-primary-page) |
| **CJMMAS-3300-422** | A URL has not been specified for the subpage ''{pageName}''. Specify a URL. | Define a URL for the subpage. [Learn more](create-lp.md#configure-primary-page) |
| **CJMMAS-3102-400** | The URL of page ''{pageName}'' is already in use for another published landing page. Specify a unique URL and try again. | Give the page a unique URL that no other published landing page uses. [Learn more](create-lp.md#configure-primary-page) |
| **CJMMAS-3103-400** | The URLs of pages ''{pageName1}'' and ''{pageName2}'' are the same. Specify unique URLs and try again. | Give each page of the landing page a unique URL. [Learn more](create-lp.md#configure-primary-page) |
| **CJMMAS-3203-422** | No HTML has been provided for the primary Page ''{pageName}''. Provide HTML for the page and try again. | Open the page designer and add the HTML content to the page. [Learn more](design-lp.md) |
| **CJMMAS-3301-422** | There is no HTML for the subpage ''{pageName}''. Provide the HTML. | Open the page designer and add the HTML content to the page. [Learn more](design-lp.md) |
| **CJMMAS-3204-200** | There is no page name for the primary page. Provide a page name and try again. | Enter a page name. [Learn more](create-lp.md#configure-primary-page) |
| **CJMMAS-3302-200** | No page name is specified for subpage ''{pageName}''. Provide a page name. | Enter a page name. [Learn more](create-lp.md#configure-primary-page) |
| **CJMMAS-3400-422** | Validation Error. The primary page HTML template size has exceeded the limit of 1 MB. Reduce the size of the template and try again. | Reduce the size of the HTML template to 1 MB or less. [Learn more](../start/guardrails.md#content-authoring) |
| **CJMMAS-3401-422** | Validation Error. The subpage HTML template size has exceeded the limit of 1 MB. Reduce the size of the template and try again. | Reduce the size of the HTML template to 1 MB or less. [Learn more](../start/guardrails.md#content-authoring) |

## Forms and subscription lists {#forms}

These errors occur when the form of the primary page, or the subscription list it uses, is not valid.

See also [Landing pages guardrails](../start/guardrails.md#lp-guardrails) and [Create a subscription list](subscription-list.md).

| Error code | Message | How to fix |
|---|---|---|
| **CJMMAS-3218-422** | Multiple forms are present in the primary page ''{pageName}''. Only one form is allowed. | Keep one **[!UICONTROL Form]** component on the primary page and remove the others. Do not add forms to subpages. [Learn more](../start/guardrails.md#lp-guardrails) |
| **CJMMAS-3223-422** | The primary page does not contain a form component, but a subscription list is selected. To reset the page, add a form component and remove it. | Add a form component to the primary page, then remove it, to clear the subscription list. [Learn more](lp-content.md#use-form-component) |
| **CJMMAS-3224-422** | The primary page does not contain a form component, but a configuration is set. To reset the page, add a form component and remove it. | Add a form component to the primary page, then remove it, to clear the form configuration. [Learn more](lp-content.md#use-form-component) |
| **CJMMAS-3205-422** | A subscription list is not selected in the primary page ''{pageName}''. Select a subscription list and try again. | In the **[!UICONTROL Form]** component, select the subscription list that the checkbox updates. [Learn more](subscription-list.md) |
| **CJMMAS-3220-422** | An invalid subscription list is set in the primary page ''{pageName}''. Specify a valid subscription list. | Select a valid subscription list for the primary page. [Learn more](subscription-list.md) |
| **CJMMAS-3219-422** | A subscription list that is not live is present in the primary page ''{pageName}''. Specify a live subscription list. | Select a live subscription list, or check the start and end dates of the one you selected. [Learn more](subscription-list.md) |
| **CJMMAS-3225-422** | Multiple email text boxes are present in the primary page ''{pageName}''. | Keep one email text box in the form. [Learn more](lp-content.md#use-form-component) |
| **CJMMAS-3226-422** | A subscription list is associated to the email text box in the primary page ''{pageName}'' but is not associated with a checkbox or a button. Please update the primary page and try again. | In the **[!UICONTROL Form]** component, select the subscription list on a checkbox, or in the button **[!UICONTROL Opt in]** action. [Learn more](lp-content.md#use-form-component) |
| **CJMMAS-3227-422** | Duplicate subscription lists ''{subscriptionLists}'' present in the primary page ''{pageName}'' are not allowed. Please update the primary page to remove duplicates and try again. | Use each subscription list only once in the form. [Learn more](lp-content.md#use-form-component) |
| **CJMMAS-3206-422** | Form fields have duplicate names in the primary page ''{pageName}''. Give the fields unique names. | Rename the form fields so that each name is unique. [Learn more](lp-content.md#use-form-component) |
| **CJMMAS-3207-422** | Form fields have empty names in the primary page ''{pageName}''. Enter names in the unnamed form fields. | Enter a name in each unnamed form field. [Learn more](lp-content.md#use-form-component) |
| **CJMMAS-3208-422** | Multiple Call to Action buttons are present in Primary Page ''{pageName}''. | In the **[!UICONTROL Form]** component, keep one button in the **[!UICONTROL Call to action]** section and remove the others. [Learn more](lp-content.md#use-form-component) |
| **CJMMAS-3214-422** | The data error or data confirmation tag is missing in the form in the primary page ''{pageName}''.  Please enter the tag. | Add the data error or data confirmation tag to the form, and make sure the matching inline confirmation and error elements are in the HTML. [Learn more](lp-content.md#use-form-component) |
| **CJMMAS-3215-422** | No confirmation or error actions are set in the primary page ''{pageName}''. Set the actions and try again. | Set one confirmation action and one error action for the form. [Learn more](lp-content.md#use-form-component) |
| **CJMMAS-3216-422** | Multiple confirmation or error actions are present in the primary page ''{pageName}''. Only one confirmation or error action is allowed. | Keep one confirmation action and one error action. [Learn more](lp-content.md#use-form-component) |
| **CJMMAS-3217-422** | Inline confirmation and error elements are not present in the HTML for the primary page ''{pageName}''. Specify the inline confirmation and error elements, then try again. | Add the inline confirmation and error elements to the HTML of the primary page. [Learn more](lp-content.md#use-form-component) |

## Expiration {#expiration}

These errors occur when the expiration of the primary page is not configured completely.

See also [Configure the primary page](create-lp.md#configure-primary-page).

| Error code | Message | How to fix |
|---|---|---|
| **CJMMAS-3209-422** | The expiration date is empty in the primary page ''{pageName}''. Specify an expiration date. | Set an expiration date for the primary page. [Learn more](create-lp.md#configure-primary-page) |
| **CJMMAS-3210-422** | Expiration Action is empty in the primary page ''{pageName}''. Specify an expiration action. | Select the action to run when the page expires: **[!UICONTROL Redirect URL]**, **[!UICONTROL Custom page]**, or **[!UICONTROL Browser error]**. [Learn more](create-lp.md#configure-primary-page) |
| **CJMMAS-3211-422** | The redirect URL is empty in the primary page ''{pageName}'' expiration action. Specify a redirect URL. | Enter a URL in the **[!UICONTROL Redirect URL]** action. [Learn more](create-lp.md#configure-primary-page) |
| **CJMMAS-3221-422** | An invalid redirect URL is set in the primary page ''{pageName}''. Set a valid redirect URL. | Enter a valid URL in the **[!UICONTROL Redirect URL]** action. [Learn more](create-lp.md#configure-primary-page) |
| **CJMMAS-3212-422** | Subpage is empty or invalid in the primary page ''{pageName}'' expiration action. Specify a valid subpage. | In the **[!UICONTROL Custom page]** action, select an existing subpage. Create the subpage first if it does not exist. [Learn more](create-lp.md#configure-subpages) |
| **CJMMAS-3000-400** | Bad request. There is an invalid subpage name in the primary page expiration action. Correct the invalid name and try again. | In the **[!UICONTROL Custom page]** action, select an existing subpage. Create the subpage first if it does not exist. [Learn more](create-lp.md#configure-subpages) |
| **CJMMAS-3009-400** | Bad request. There is an invalid subpage name in the primary page expiration action. Correct the invalid name and try again. | In the **[!UICONTROL Custom page]** action, select an existing subpage. Create the subpage first if it does not exist. [Learn more](create-lp.md#configure-subpages) |
| **CJMMAS-3213-422** | The text for the primary page ''{pageName}'' expiration text action is missing. Enter the text. | Type the error text for the **[!UICONTROL Browser error]** action. [Learn more](create-lp.md#configure-primary-page) |
| **CJMMAS-3222-422** | The expiration date selected in the primary page ''{pageName}'' has passed. Select a future date. | Select an expiration date in the future. [Learn more](create-lp.md#configure-primary-page) |
| **CJMMAS-3303-422** | Subpage ''{pageName}'' for expiry action contains contextual attributes of the primary page. Select a different subpage or remove the primary page contextual attributes from it. | Select another subpage, or remove the contextual attributes of the primary page from it. [Learn more](create-lp.md#configure-subpages) |

## Links from messages {#links}

These errors occur when a message or a landing page links to a landing page that is not published, does not exist, or has expired.

See also [Manage your landing pages](manage-lp.md).

| Error code | Message | How to fix |
|---|---|---|
| **CJMMAS-1306-400** | Please publish the included landing page and try again. | Publish the included landing page, then try again. [Learn more](create-lp.md#publish-landing-page) |
| **CJMMAS-1309-400** | The landing page ''{sourceName}'' links to a landing page that is not published. Please publish the included landing page before retrying. | Publish the landing page that the named landing page links to, then try again. [Learn more](create-lp.md#publish-landing-page) |
| **CJMMAS-1307-400** | The message ''{sourceName}'' links to a landing page that does not exist. Please specify an existing landing page. | In the link of the message named in the error, select an existing landing page. [Learn more](../email/message-tracking.md) |
| **CJMMAS-1310-400** | The landing page ''{sourceName}'' links to a landing page that does not exist. Please specify an existing landing page. | In the link of the landing page named in the error, select an existing landing page. [Learn more](../email/message-tracking.md) |
| **CJMMAS-1308-400** | The message ''{sourceName}'' links to an expired landing page. Link to an unexpired landing page and try again. | Link to a landing page that has not expired, or change the expiration date of the linked landing page. [Learn more](manage-lp.md) |
| **CJMMAS-1311-400** | The landing page ''{sourceName}'' links to an expired landing page. Link to an unexpired landing page and try again. | Link to a landing page that has not expired, or change the expiration date of the linked landing page. [Learn more](manage-lp.md) |

## Related topics {#related}

* [Get started with landing pages](get-started-lp.md)
* [Create and publish landing pages](create-lp.md)
* [Create the landing page content](lp-content.md)
* [Manage your landing pages](manage-lp.md)
* [Landing pages guardrails](../start/guardrails.md#lp-guardrails)
* [Error codes reference](../building-journeys/error-codes-reference.md)

{{$include /help/_includes/do-not-localize/landing-pages/ai-augmented-landing-page-errors.md}}
