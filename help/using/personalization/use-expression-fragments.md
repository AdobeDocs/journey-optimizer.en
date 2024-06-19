---
solution: Journey Optimizer
product: journey optimizer
title: Use expression fragments
description: Learn how to use expression fragments in the [!DNL Journey Optimizer] personalization editor.
feature: Personalization, Fragments
topic: Personalization
role: Data Engineer
level: Intermediate
keywords: expression, editor, library, personalization
exl-id: 74b1be18-4829-4c67-ae45-cf13278cda65
---
# Leverage expression fragments {#use-expression-fragments}

When using the **personalization editor**, you can leverage all the expression fragments that have been created or saved to the current sandbox.

A fragment is a reusable component that can be referenced across [!DNL Journey Optimizer] campaigns and journeys. This functionality allows to prebuild multiple custom content blocks that can be used by marketing users to quickly assemble contents in an improved design process. [Learn how to create and manage fragments](../content-management/fragments.md).

➡️ [Learn how to manage, author and use fragments in this video](../content-management/fragments.md#video-fragments)

## Use an expression fragment {#use-expression-fragment}

To add expression fragments to your content, follow the steps below.

>[!NOTE]
>
>You can add up to 30 fragments in a given delivery. Fragments can only be nested up to 1 level.

1. Open the [personalization editor](personalization-build-expressions.md) and select the **[!UICONTROL Fragments]** button on the left pane.

    The list displays all the expression fragments that have been created or saved as fragments on the current sandbox. They are sorted by creation date: recently added expression fragments are shown first in the list. [Learn more](../content-management/fragments.md#create-expression-fragment)

    ![](assets/expression-fragments-pane.png)

    You can also refresh this list. 
    
    >[!NOTE]
    >
    >If some fragments were modified or added while you are editing your content, the list will be updated with the latest changes.

1. Click the + icon next to an expression fragment to insert the corresponding fragment ID into the editor.

    ![](assets/expression-fragment-add.png)

    >[!CAUTION]
    >
    >You can add any **Draft** or **Live** fragment to your content. However, you won't be able to activate your journey or campaign if a fragment with the Draft status is being used in it. At journey or campaign publication, draft fragments will show an error and you'll need to approve them to be able to publish.
    >
    > Please note that fragments statuses are being rolled out gradually over the course of several days following Journey Optimizer June release. While some users will have immediate access, others may experience a delay before it becomes available in their environments. If this enhancement is not yet available in your environment, please note that fragment do not require to be **Live** to be used in your journeys and campaigns.

1. Once the fragment ID has been added, if you open the corresponding expression fragment and [edit it](../content-management/fragments.md#edit-fragments) from the interface, the changes are synchronized. They are automatically propagated to all draft or live journeys/campaigns containing that fragment ID.

1. Click the **[!UICONTROL More actions]** button next to a fragment. From the contextual menu that opens, select **[!UICONTROL View fragment]** to get more information about that fragment. The **[!UICONTROL Fragment ID]** is also displayed and can be copied from here.

    ![](assets/expression-fragment-view.png)

1. You can open the expression fragment in another window to edit its content and properties - either using the **[!UICONTROL Open fragment]** option in the contextual menu or from the **[!UICONTROL Fragment info]** pane. [Learn how to edit a fragment](../content-management/fragments.md#edit-fragments)

    ![](assets/expression-fragment-open.png)

1. You can then customize and validate your content as usual using all the personalization and authoring capabilities of the [personalization editor](personalization-build-expressions.md).

>[!NOTE]
>
>If you create an expression fragment that contains multiple line breaks and use it in [SMS](../sms/create-sms.md#sms-content) or [push](../push/design-push.md) content, the line breaks are preserved. Thus make sure to test your [SMS](../sms/send-sms.md) or [push](../push/send-push.md) messsage before sending it.

## Break inheritance {#break-inheritance}

When adding a fragment ID to the personalization editor, the changes made to the original expression fragment are synchronized.

However, you can also paste the content of an expression fragment into the editor. From the contextual menu, select **[!UICONTROL Paste fragment]** to insert that content.

![](assets/expression-fragment-paste.png)

In that case, the inheritance from the original fragment is broken. The content of the fragment is copied into the editor, and the changes are not synchronized anymore.

It becomes a standalone element that is no longer linked to the original fragment; you can edit it as any other element in your code.

