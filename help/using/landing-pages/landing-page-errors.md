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

## Permissions and access {#access}

These errors occur when your user does not have the permission or the access needed to work with landing pages.

See also [Built-in permissions](../administration/ootb-permissions.md).

| Error code | Message | How to fix |
|---|---|---|
| **CJMMAS-1070-403** | You do not have read permission on landing pages. Landing pages require the message level permission. | Landing pages use the permissions of messages. Ask your administrator to grant the read permission on landing pages on your product profile. [Learn more](../administration/ootb-permissions.md) |
| **CJMMAS-1071-403** | You do not have write permission on landing pages. Landing pages require the message level permission. | Landing pages use the permissions of messages. Ask your administrator to grant the write permission on landing pages on your product profile. [Learn more](../administration/ootb-permissions.md) |
| **CJMMAS-1072-403** | You do not have publish permission on landing pages. Landing pages require the message level permission. | Landing pages use the permissions of messages. Ask your administrator to grant the publish permission on your product profile. To test or publish a landing page, you need the **[!UICONTROL Publish Messages]** permission. [Learn more](../administration/ootb-permissions.md) |
| **CJMMAS-1073-403** | You do not have delete permission on landing pages. Landing pages require the message level permission. | Landing pages use the permissions of messages. Ask your administrator to grant the delete permission on landing pages on your product profile. [Learn more](../administration/ootb-permissions.md) |
| **CJMMAS-1078-403** | You do not have permission to access this landing page. Please contact your administrator to request access. | You do not have access to this landing page. Ask your administrator for access to the object. [Learn more](../administration/object-based-access.md) |

## Publication and status {#publication}

These errors occur when you publish, edit, or delete a landing page, and the status of the landing page does not allow it.

See also [Manage your landing pages](manage-lp.md).

| Error code | Message | How to fix |
|---|---|---|
| **CJMMAS-3012-400** | Bad request. The landing page is in the process of being published. Please wait until publishing is complete and try again. | The landing page is being published. Wait until the publication completes, then try again. [Learn more](create-lp.md#publish-landing-page) |
| **CJMMAS-3104-400** | Unable to publish landing page. The landing page is already published or is in publishing state. | The landing page is already published or is being published. Check its status, and wait until the publication completes if needed. [Learn more](create-lp.md#publish-landing-page) |
| **CJMMAS-3002-400** | Updation of Published Landing Page is not permitted. | A published landing page cannot be updated. Unpublish the landing page to make this change, then publish it again. [Learn more](manage-lp.md) |
| **CJMMAS-3006-400** | Bad request. Updating a published landing page is not permitted. | A published landing page cannot be updated. Unpublish the landing page to make this change, then publish it again. [Learn more](manage-lp.md) |
| **CJMMAS-3010-400** | Bad Request. Cannot create subpage for a published landing page. | A subpage cannot be added to a published landing page. Unpublish the landing page to add the subpage, then publish it again. [Learn more](manage-lp.md) |
| **CJMMAS-3011-400** | Bad request. A published landing page cannot be deleted. Please unpublish the landing page before deleting. | A published landing page cannot be deleted. Unpublish it first, then delete it. If a message links to it, the link is broken once the page is unpublished. [Learn more](manage-lp.md) |
| **CJMMAS-3107-400** | Validation Error in the Landing Page. | The landing page failed validation. Fix the errors displayed. [Learn more](create-lp.md#configure-primary-page) |
| **CJMMAS-3200-422** | No pages found to validate within this landing page. | The landing page has no page to validate. Add a primary page to the landing page. [Learn more](create-lp.md#configure-primary-page) |
| **CJMMAS-3201-422** | No Primary page found. | The landing page has no primary page. Add a primary page to the landing page. [Learn more](create-lp.md#configure-primary-page) |
| **CJMMAS-3013-400** | The tags are invalid. The specified tag does not exist or is not applicable on the entity. Please verify the tag and try again. | One or more tags do not exist or do not apply to landing pages. Select existing tags. [Learn more](../start/search-filter-categorize.md#tags) |

## Page URL, name, and content {#url}

These errors occur when a page does not have a URL, a name, or content, or when its URL is already used.

See also [Create and publish landing pages](create-lp.md).

| Error code | Message | How to fix |
|---|---|---|
| **CJMMAS-3101-400** | Landing page publish URL is not present. | The landing page has no publish URL. Define a URL for the page. [Learn more](create-lp.md#configure-primary-page) |
| **CJMMAS-3202-422** | The URL is empty in the primary page ''{pageName}''. Provide a URL and try again. | The primary page has no URL. Define a URL for the primary page. [Learn more](create-lp.md#configure-primary-page) |
| **CJMMAS-3300-422** | A URL has not been specified for the subpage ''{pageName}''. Specify a URL. | The subpage has no URL. Define a URL for the subpage. [Learn more](create-lp.md#configure-primary-page) |
| **CJMMAS-3102-400** | The URL of page ''{pageName}'' is already in use for another published landing page. Specify a unique URL and try again. | The URL of the page is already used by another published landing page. Give the page a unique URL. [Learn more](create-lp.md#configure-primary-page) |
| **CJMMAS-3103-400** | The URLs of pages ''{pageName1}'' and ''{pageName2}'' are the same. Specify unique URLs and try again. | Two pages of the landing page have the same URL. Give each page a unique URL. [Learn more](create-lp.md#configure-primary-page) |
| **CJMMAS-3203-422** | No HTML has been provided for the primary Page ''{pageName}''. Provide HTML for the page and try again. | The primary page has no HTML content. Open the page designer and add the content. [Learn more](design-lp.md) |
| **CJMMAS-3301-422** | There is no HTML for the subpage ''{pageName}''. Provide the HTML. | The subpage has no HTML content. Open the page designer and add the content. [Learn more](design-lp.md) |
| **CJMMAS-3204-200** | There is no page name for the primary page. Provide a page name and try again. | The primary page has no name. Enter a page name. [Learn more](create-lp.md#configure-primary-page) |
| **CJMMAS-3302-200** | No page name is specified for subpage ''{pageName}''. Provide a page name. | The subpage has no name. Enter a page name. [Learn more](create-lp.md#configure-primary-page) |
| **CJMMAS-3400-422** | Validation Error. The primary page HTML template size has exceeded the limit of 1 MB. Reduce the size of the template and try again. | The HTML template of the primary page is larger than 1 MB and is rejected. Reduce the size of the template. [Learn more](../start/guardrails.md#content-authoring) |
| **CJMMAS-3401-422** | Validation Error. The subpage HTML template size has exceeded the limit of 1 MB. Reduce the size of the template and try again. | The HTML template of the subpage is larger than 1 MB and is rejected. Reduce the size of the template. [Learn more](../start/guardrails.md#content-authoring) |

## Forms and subscription lists {#forms}

These errors occur when the form of the primary page, or the subscription list it uses, is not valid.

See also [Landing pages guardrails](../start/guardrails.md#lp-guardrails) and [Create a subscription list](subscription-list.md).

| Error code | Message | How to fix |
|---|---|---|
| **CJMMAS-3218-422** | Multiple forms are present in the primary page ''{pageName}''. Only one form is allowed. | A page can have only one form. Keep one **[!UICONTROL Form]** component on the primary page. Forms cannot be used in subpages. [Learn more](../start/guardrails.md#lp-guardrails) |
| **CJMMAS-3223-422** | The primary page does not contain a form component, but a subscription list is selected. To reset the page, add a form component and remove it. | The primary page has no form component, but a subscription list is still set. Add a form component, then remove it, to reset the page. [Learn more](lp-content.md#use-form-component) |
| **CJMMAS-3224-422** | The primary page does not contain a form component, but a configuration is set. To reset the page, add a form component and remove it. | The primary page has no form component, but a form configuration is still set. Add a form component, then remove it, to reset the page. [Learn more](lp-content.md#use-form-component) |
| **CJMMAS-3205-422** | A subscription list is not selected in the primary page ''{pageName}''. Select a subscription list and try again. | The primary page has no subscription list. Select a valid subscription list. [Learn more](subscription-list.md) |
| **CJMMAS-3220-422** | An invalid subscription list is set in the primary page ''{pageName}''. Specify a valid subscription list. | The subscription list set in the primary page is not valid. Select a valid subscription list. [Learn more](subscription-list.md) |
| **CJMMAS-3219-422** | A subscription list that is not live is present in the primary page ''{pageName}''. Specify a live subscription list. | The subscription list is not live. Select a live subscription list, or check its start and end dates. [Learn more](subscription-list.md) |
| **CJMMAS-3225-422** | Multiple email text boxes are present in the primary page ''{pageName}''. | The form has more than one email text box. Keep one email text box in the form. [Learn more](lp-content.md#use-form-component) |
| **CJMMAS-3226-422** | A subscription list is associated to the email text box in the primary page ''{pageName}'' but is not associated with a checkbox or a button. Please update the primary page and try again. | A subscription list is associated with the email text box but not with a checkbox or a button. Associate the subscription list with a checkbox or a button. [Learn more](lp-content.md#use-form-component) |
| **CJMMAS-3227-422** | Duplicate subscription lists ''{subscriptionLists}'' present in the primary page ''{pageName}'' are not allowed. Please update the primary page to remove duplicates and try again. | The same subscription list is used more than once in the form. Use each subscription list only once. [Learn more](lp-content.md#use-form-component) |
| **CJMMAS-3206-422** | Form fields have duplicate names in the primary page ''{pageName}''. Give the fields unique names. | Two or more form fields have the same name. Rename the duplicates so that each name is unique. [Learn more](lp-content.md#use-form-component) |
| **CJMMAS-3207-422** | Form fields have empty names in the primary page ''{pageName}''. Enter names in the unnamed form fields. | Some form fields have no name. Name the unnamed fields. [Learn more](lp-content.md#use-form-component) |
| **CJMMAS-3208-422** | Multiple Call to Action buttons are present in Primary Page ''{pageName}''. | Keep a single call to action button on the primary page. [Learn more](lp-content.md#use-form-component) |
| **CJMMAS-3214-422** | The data error or data confirmation tag is missing in the form in the primary page ''{pageName}''.  Please enter the tag. | The data error or data confirmation tag is missing in the form. Add the tag, and make sure the matching inline confirmation and error elements are in the HTML. [Learn more](lp-content.md#use-form-component) |
| **CJMMAS-3215-422** | No confirmation or error actions are set in the primary page ''{pageName}''. Set the actions and try again. | No confirmation or error action is set for the form. Set one confirmation action and one error action. [Learn more](lp-content.md#use-form-component) |
| **CJMMAS-3216-422** | Multiple confirmation or error actions are present in the primary page ''{pageName}''. Only one confirmation or error action is allowed. | The form has more than one confirmation or error action. Keep one confirmation action and one error action. [Learn more](lp-content.md#use-form-component) |
| **CJMMAS-3217-422** | Inline confirmation and error elements are not present in the HTML for the primary page ''{pageName}''. Specify the inline confirmation and error elements, then try again. | The inline confirmation and error elements are missing in the HTML of the primary page. Add them to the HTML. [Learn more](lp-content.md#use-form-component) |

## Expiration {#expiration}

These errors occur when the expiration of the primary page is not configured completely.

See also [Configure the primary page](create-lp.md#configure-primary-page).

| Error code | Message | How to fix |
|---|---|---|
| **CJMMAS-3209-422** | The expiration date is empty in the primary page ''{pageName}''. Specify an expiration date. | The expiration date is empty. Set an expiration date for the primary page. [Learn more](create-lp.md#configure-primary-page) |
| **CJMMAS-3210-422** | Expiration Action is empty in the primary page ''{pageName}''. Specify an expiration action. | The expiration action is empty. Select the action to run when the page expires: **[!UICONTROL Redirect URL]**, **[!UICONTROL Custom page]**, or **[!UICONTROL Browser error]**. [Learn more](create-lp.md#configure-primary-page) |
| **CJMMAS-3211-422** | The redirect URL is empty in the primary page ''{pageName}'' expiration action. Specify a redirect URL. | The redirect URL of the **[!UICONTROL Redirect URL]** action is empty. Enter a URL. [Learn more](create-lp.md#configure-primary-page) |
| **CJMMAS-3221-422** | An invalid redirect URL is set in the primary page ''{pageName}''. Set a valid redirect URL. | The redirect URL of the **[!UICONTROL Redirect URL]** action is not valid. Enter a valid URL. [Learn more](create-lp.md#configure-primary-page) |
| **CJMMAS-3212-422** | Subpage is empty or invalid in the primary page ''{pageName}'' expiration action. Specify a valid subpage. | The subpage of the **[!UICONTROL Custom page]** action is empty or not valid. Select an existing subpage, and create the subpage first if it does not exist. [Learn more](create-lp.md#configure-subpages) |
| **CJMMAS-3000-400** | Bad request. There is an invalid subpage name in the primary page expiration action. Correct the invalid name and try again. | The subpage name in the **[!UICONTROL Custom page]** action is not valid. Select an existing subpage, and create the subpage first if it does not exist. [Learn more](create-lp.md#configure-subpages) |
| **CJMMAS-3009-400** | Bad request. There is an invalid subpage name in the primary page expiration action. Correct the invalid name and try again. | The subpage name in the **[!UICONTROL Custom page]** action is not valid. Select an existing subpage, and create the subpage first if it does not exist. [Learn more](create-lp.md#configure-subpages) |
| **CJMMAS-3213-422** | The text for the primary page ''{pageName}'' expiration text action is missing. Enter the text. | Type the error text for the **[!UICONTROL Browser error]** action. [Learn more](create-lp.md#configure-primary-page) |
| **CJMMAS-3222-422** | The expiration date selected in the primary page ''{pageName}'' has passed. Select a future date. | The expiration date has passed. Select a date in the future. [Learn more](create-lp.md#configure-primary-page) |
| **CJMMAS-3303-422** | Subpage ''{pageName}'' for expiry action contains contextual attributes of the primary page. Select a different subpage or remove the primary page contextual attributes from it. | The subpage of the expiration action uses contextual attributes of the primary page. Select another subpage, or remove those attributes from it. [Learn more](create-lp.md#configure-subpages) |

## Links from messages {#links}

These errors occur when a message or a landing page links to a landing page that is not published, does not exist, or has expired.

See also [Manage your landing pages](manage-lp.md).

| Error code | Message | How to fix |
|---|---|---|
| **CJMMAS-1306-400** | Please publish the included landing page and try again. | The included landing page is not published. Publish it, then try again. [Learn more](create-lp.md#publish-landing-page) |
| **CJMMAS-1309-400** | The landing page ''{sourceName}'' links to a landing page that is not published. Please publish the included landing page before retrying. | The landing page named in the message links to a landing page that is not published. Publish the linked landing page, then try again. [Learn more](create-lp.md#publish-landing-page) |
| **CJMMAS-1307-400** | The message ''{sourceName}'' links to a landing page that does not exist. Please specify an existing landing page. | The message named in the error links to a landing page that does not exist. Select an existing landing page in the link. [Learn more](../email/message-tracking.md) |
| **CJMMAS-1310-400** | The landing page ''{sourceName}'' links to a landing page that does not exist. Please specify an existing landing page. | The landing page named in the error links to a landing page that does not exist. Select an existing landing page in the link. [Learn more](../email/message-tracking.md) |
| **CJMMAS-1308-400** | The message ''{sourceName}'' links to an expired landing page. Link to an unexpired landing page and try again. | The message named in the error links to an expired landing page. Link to a landing page that has not expired, or change its expiration date. [Learn more](manage-lp.md) |
| **CJMMAS-1311-400** | The landing page ''{sourceName}'' links to an expired landing page. Link to an unexpired landing page and try again. | The landing page named in the error links to an expired landing page. Link to a landing page that has not expired, or change its expiration date. [Learn more](manage-lp.md) |

## Related topics {#related}

* [Get started with landing pages](get-started-lp.md)
* [Create and publish landing pages](create-lp.md)
* [Create the landing page content](lp-content.md)
* [Manage your landing pages](manage-lp.md)
* [Landing pages guardrails](../start/guardrails.md#lp-guardrails)
* [Error codes reference](../building-journeys/error-codes-reference.md)

{{$include /help/_includes/do-not-localize/landing-pages/ai-augmented-landing-page-errors.md}}
