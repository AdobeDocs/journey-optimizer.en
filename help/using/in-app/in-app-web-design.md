---
title: Design your Web In-app content
description: Learn how to design your Web In-app content
feature: In App
topic: Content Management
role: User
level: Beginner
keywords: in-app, message, creation, start
hide: yes
hidefromtoc: yes
---
# Design your Web In-app content {#in-app-web-design}

>[!BEGINSHADEBOX]

**Table of content**

* [Configure the Web In-app channel](configure-in-app-web.md)
* [Create your Web In-app message campaign](create-in-app-web.md)
* Design your Web In-app content

>[!ENDSHADEBOX]

To edit the In-app message content click the **[!UICONTROL Edit content]** button from the **[!UICONTROL Action]** menu of your Campaign.

![](assets/in_app_web_surface_7.png)

The **[!UICONTROL Advanced formatting]** toggle activates additional options to customize the experience.

Once your In-app message is created, and its content defined and personalized, you can review and activate it. Notifications will then be sent according to the campaign schedule. Learn more in [this page](send-in-app.md).

## Message layout {#message-layout}

From the **[!UICONTROL Message Layout]** section, select one of the four different layout options to choose from depending on your messaging needs. 

![](assets/in_app_web_design_1.png)

* **[!UICONTROL Fullscreen]**: This type of layout covers the entire screen of your audience devices.
    
    It supports media (image, video), text and button components.

* **[!UICONTROL Modal]**: This layout appears in a large alert-style window, your application is still visible in the background.

    It supports media (image, video), text and button components.

* **[!UICONTROL Banner]**: This type of layout appears as a native OS alert message.

    You can only add a **[!UICONTROL Header]** and a **[!UICONTROL Body]** to your message.

* **[!UICONTROL Custom]**: The custom message mode allows you to directly import and edit one of your pre-configured HTML messages.

    * Select **[!UICONTROL Compose]** to enter or paste your raw HTML code.
    
        Use the left pane to leverage Journey Optimizer personalization capabilities. For more on this, refer to [this section](../personalization/personalize.md).
    
    * Select **[!UICONTROL Import]** to import the HTML or .zip file containing your HTML content.

## Content tab {#content-tab}

From the **Content** tab, you can define and personalize the content of the notification and the style of the **Close** button. You can also add a media to your In-app notification, and add action buttons from this tab.

### Close button {#close-button}

![](assets/in_app_web_design_2.png)

Choose the **[!UICONTROL Style]** of your **[!UICONTROL Close button]**.

Available styles are:

* **[!UICONTROL Simple]**
* **[!UICONTROL Circle]**
* **[!UICONTROL Custom image]** from a Media URL or your Assets.

+++More options with advanced formatting

If the **[!UICONTROL Advanced formatting mode]** is switched on, you can check the **[!UICONTROL Color]** option to choose the color and opacity of your button.

+++

### Media {#add-media}

The **[!UICONTROL Media]** field allows you to add media to your In-app message to create a compelling experience for end user.

![](assets/in_app_web_design_3.png)

Type-in your Media URL or click the **[!UICONTROL Select Assets]** icon to directly add assets stored in your Assets library to your In-app message. [Learn more about asset management](../content-management/assets-essentials.md).
You can also add an **[!UICONTROL Alternative text]** for screen reading applications.

+++More options with advanced formatting

If the **[!UICONTROL Advanced formatting mode]** is switched on, you can customize the **[!UICONTROL Max height]** and **[!UICONTROL Max width]** of your media. 

+++

### Content {#title-body}

To compose your message, enter the content in the **[!UICONTROL Header]** and **[!UICONTROL Body]** fields.

![](assets/in_app_web_design_4.png)

Use the **[!UICONTROL Personalization]** icon to add personalization. Learn more about personalization in Adobe Journey Optimizer Expression Editor [in this section](../personalization/personalize.md).

+++More options with advanced formatting

If the **[!UICONTROL Advanced formatting mode]** is switched on, you can choose for your **[!UICONTROL Header]** and **[!UICONTROL Body]**:

* the **[!UICONTROL Font]**
* the **[!UICONTROL Pt size]**
* the **[!UICONTROL Font Color]**
* the **[!UICONTROL Alignment]**
+++

### Buttons {#add-buttons}

Add buttons for users to interact with your In-app message.

![](assets/in_app_web_design_5.png)

To personalize your button:

1. Edit the Button #1 text (primary) field. You can also use the **[!UICONTROL Personalization]** icon to define content and personalization data.

1. Choose your **[!UICONTROL Interact event]** which defines your button's action after users interacted with it.

1. Enter your web URL or deeplink in the **[!UICONTROL Target]** field.

1. To add multiple buttons, click **[!UICONTROL Add button]**.

+++More options with advanced formatting

If the **[!UICONTROL Advanced formatting mode]** is switched on, you can choose for your **[!UICONTROL Buttons]**:

* the **[!UICONTROL Font]**
* the **[!UICONTROL Pt size]**
* the **[!UICONTROL Font Color]**
* the **[!UICONTROL Alignment]**
* the **[!UICONTROL Button style]**
* the **[!UICONTROL Radius]**
* the **[!UICONTROL Button color]**

+++

## Settings tab {#settings-tab}

From the **Settings** tab, you can define the message layout and preview your In-app message. You can also access advanced formatting options.

### Layout {#layout-options}

![](assets/in_app_web_design_6.png)

The **[!UICONTROL Background image]** field allows you to add a background to your In-app message:

* A media from an URL link.

* A background color.

### Message {#message-tab}

![](assets/in_app_web_design_7.png)

The UI takeover option, enabled by default, allows you to darken the background behind your In-app message to emphasize the focus on your content.

+++More options with advanced formatting

If the **[!UICONTROL Advanced formatting mode]** is switched on, you can further personalize your message with the following options:

* **[!UICONTROL Customize UI takeover]**: allows you to select a color to display in the background and its opacity.

* **[!UICONTROL Customize size]**: allows you to adjust your In-app notification's width and height.

* **[!UICONTROL Customize position]**: allows you to customize the position of your In-app messages on your users' screen. You can change the Vertical and Horizontal alignments.

* **[!UICONTROL Message round corner]**: allows you to add round corner to your In-app notification by changing the **[!UICONTROL Corner radius]**.

+++

**Related topics:**

* [Test and send your In-app message](send-in-app.md)
* [In-app report](../reports/campaign-global-report.md#inapp-report)
* [In-app configuration](inapp-configuration.md)