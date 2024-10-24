---
title: Web channel configuration
description: Create web channel configuration
feature: Web Channel, Channel Configuration
topic: Content Management
role: Admin
level: Experienced
exl-id: 2161baf0-38b7-4397-bffe-083929e8033a
---
# Configure your web experiences {#web-configuration}

## Create a web channel configuration {#create-web-configuration}

A web configuration is a web property identified by a URL where the content will be delivered. It can match a single page URL or multiple pages, allowing you to deliver modifications across one or several web pages.

To create a web channel configuration, follow the steps below.

1. Access the **[!UICONTROL Channels]** > **[!UICONTROL General settings]** > **[!UICONTROL Channel configurations]** menu, then click **[!UICONTROL Create channel configuration]**.

    ![](assets/web_config_1.png)

1. Enter a name and a description (optional) for the configuration.

    >[!NOTE]
    >
    > Names must begin with a letter (A-Z). It can only contain alpha-numeric characters. You can also use underscore `_`, dot`.` and hyphen `-` characters.

1. To assign custom or core data usage labels to the configuration, you can select **[!UICONTROL Manage access]**. [Learn more on Object Level Access Control (OLAC)](../administration/object-based-access.md)

1. Select the **Web** channel.

    ![](assets/web_config_2.png)

1. Select **[!UICONTROL Marketing action]**(s) to associate consent policies to the messages using this configuration. All consent policies associated with the marketing action are leveraged in order to respect the preferences of your customers. [Learn more](../action/consent.md#surface-marketing-actions)

1. In the **[!UICONTROL Web settings]** section, select one of the following options:

   * **[!UICONTROL Single page]** - If you want to apply the changes to a single page only, enter a **[!UICONTROL Page URL]**.

   * **[!UICONTROL Pages matching rule]** - To target multiple URLs matching the same rule, build a pages matching rule, and enter a **[!UICONTROL Default authoring and preview URL]**. [Learn more](#web-page-matching-rule)

1. Click **[!UICONTROL Submit]** to save your changes.

You can now select this configuration when using the Web channel in your campaigns or journeys.

## Build a pages matching rule {#web-page-matching-rule}

>[!CONTEXTUALHELP]
>id="ajo_admin_page_rule"
>title="Build a pages matching rule"
>abstract="To efficiently manage and target a group of URLs that share the same criteria, create a Pages matching rule. This rule enables you to consolidate multiple URLs under one guideline, simplifying the application of consistent settings and actions across these pages."

>[!CONTEXTUALHELP]
>id="ajo_admin_default_url"
>title="Define a URL for content authoring and preview"
>abstract="This field ensures that the pages generated or matched by the rule have a designated URL, essential for both creating and previewing content effectively."

When creating a web or [code-based experience](../code-based/get-started-code-based.md) configuration, you can build a **[!UICONTROL Pages matching rule]** to target multiple URLs matching the same rule. You can therefore apply the same content changes across multiple pages at once.

For example, you may want to apply the changes to a hero banner across a whole website, or add a top image that displays on all the product pages of a website.

1. When configuring your [web](#web-configuration) or [code-based experience](../code-based/code-based-configuration.md), select **[!UICONTROL Pages matching rule]**.

1. Define your criteria for the **[!UICONTROL Domain]** and **[!UICONTROL Page]** fields. Check the available operators in [this section](#available-operators).

    For example, if you want to edit elements that are displayed on all the women product pages of your Luma website, select **[!UICONTROL Domain]** > **[!UICONTROL Starts with]** > `luma` and **[!UICONTROL Page]** > **[!UICONTROL Contains]** > `women`.

    ![](assets/web_config_3.png)

1. If your use case cannot be modeled using one rule, you have the option to add multiple rules. Click **[!UICONTROL Add another page rule]** and repeat the step above.

   >[!NOTE]
   >
   >You can add up to 10 rules.

1. You can use the **[!UICONTROL Or]** or **[!UICONTROL Exclude]** operators between the different rules.

   **[!UICONTROL Exclude]** is useful when one of the pages that match the rule defined should not be targeted. For example, you can target all `luma.com` pages that contain `product`, excluding the following page: `https://luma.com/blogs/productinfo`.

    ![](assets/web_config_4.png)

1. Enter the **[!UICONTROL Default authoring and preview URL]**. This step ensures that the pages generated or matched by the rule have a designated URL for both content creation and preview purposes.

### Available operators for building page matching rules {#available-operators}

When creating a [rule that matches multiple pages](#web-page-matching-rule), you can use different operators on the **[!UICONTROL Domain]** and on the **[!UICONTROL Path]** sections to build your desired rule. The available operators are listed below.

* **Domain**

    | Operator  | Description  | Examples   | 
    |---|---|---|
    | Equals  | Exact match of the domain.  | 
    | Starts with  | Matches all the domains (including sub-domains) which start with the string entered.  | Ex: "Starts with: dev" -> matches all the domains and subdomains that start with "dev", like: dev.example.com, dev.products.example.com, developer.example.com   | 
    | Ends with  | Matches all the domains (including sub-domains) which end with the string entered.  | Ex: "Ends with: example.com" -> matches all the domains and subdomains that ends with "example.com", like: stage.example.com, prod.example.com, myexample.com   |  
    | Wildcard matching  | "Wildcard matching" operator allows the user to define a wildcard match in the middle of the the string, like "dev.*.example.com". The validation rules are that the value must contain one and only one wildcard (asterisk) when the operator is "wildcard matching".  | Ex: "Wildcard matching: dev.*.example.com" -> matches domains like: dev.products.example.com, dev.mytest.products.example.com, dev.blog.example.com   | 
    | Any  | Matches all the domains – useful when testing a particular path across domains  |


* **Path**

<table>
    <thead>
    <tr>
        <th><strong>Operator</th>
        <th><strong>Description</th>
        <th><strong>Examples</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td>Equals</td>
        <td>Exact match of the path. </td>
        <td></td>
    </tr>
    <tr>
        <td>Starts with</td>
        <td>Matches all the paths (including sub-paths) which start with the string entered.</td>
        <td></td>
    </tr>
    <tr>
        <td>Ends with</td>
        <td>Matches all the paths (including sub-paths) which end with the string entered.</td>
        <td></td>
    </tr>
    <tr>
        <td>Any</td>
        <td>Matches all the paths – useful when targeting all paths under one or multiple domains.</td>
        <td></td>
    </tr>
    <tr>
        <td>Wildcard matching</td>
        <td>"Wildcard matching" operator allows the user to define an internal wildcard inside the path, like "/products/*/detail".  The wildcard character * in Path ** component, matches any sequence of characters until the first / character is encountered.  /*/ matches any sequence of characters (including sub-paths)</td>
        <td>Ex: "Wildcard matching: /products/*/detail", matches all the paths like: <ul><li>example.com/products/yoga/detail</li><li>example.com/products/surf/detail</li><li>example.com/products/tennis/detail</li><li>example.com/products/yoga/pants/detail</li></ul>Ex: "Matches: /prod*/detail, matches all the paths like: <ul><li>example.com/products/detail</li><li>example.com/production/detail</li></ul>does not match paths like: <ul><li>example.com/products/yoga/detail</li></ul></td>
    </tr>
    <tr>
        <td>Contains</td>
        <td>"contains" gets translated to a wildcard like "mystring" and matches all the paths that contain this sequence of characters.</td>
        <td>Ex: "Contains: product", matches all the paths that contain the string product, like: <ul><li>example.com/products</li><li>example.com/yoga/perfproduct</li><li>example.com/surf/productdescription</li><li>example.com/home/product/page</li></ul></td>
    </tr>
    </tbody>
</table>
